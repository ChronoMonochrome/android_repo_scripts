#/usr/bin/python

import os

TOP="../../../../"

to_restore = (
"bionic build frameworks/av frameworks/base frameworks/native frameworks/opt/net/wifi " \
"frameworks/opt/telephony libcore " \
"packages/services/Telecomm packages/services/Telephony system/core system/security " \
"packages/apps/Apollo packages/apps/LegacyCamera packages/apps/PerformanceControl "\
"packages/apps/SpeechRecorder packages/apps/Gallery2 packages/apps/PackageInstaller "
"packages/apps/TvSettings packages/apps/SpareParts packages/apps/DeskClock packages/apps/Browser "\
"packages/apps/Stk packages/apps/PhoneCommon packages/apps/Mms packages/apps/Camera2 "\
"packages/apps/Calendar packages/apps/Dialer packages/apps/MusicFX packages/apps/Launcher3 "\
"packages/apps/Exchange packages/apps/UnifiedEmail packages/apps/HTMLViewer packages/apps/ContactsCommon "\
"packages/apps/Contacts packages/apps/KeyChain packages/apps/Tag packages/apps/FMRadio packages/apps/Calculator "\
"packages/apps/CellBroadcastReceiver packages/apps/Email packages/apps/DSPManager packages/apps/OmniTorch "\
"packages/apps/VoiceDialer packages/apps/Nfc packages/apps/InCallUI packages/apps/CertInstaller "\
"packages/apps/SoundRecorder packages/apps/Settings packages/apps/OmniGears packages/apps/BasicSmsReceiver "\
"packages/apps/Bluetooth").split(" ")

proj_list = [i.replace("\n", "") for i in open("proj.txt", "rb").readlines() ] 
revs_list = open("revs.txt", "rb").readlines()
for repo in to_restore:
	if repo in proj_list:
		try:
			rev = revs_list[proj_list.index(repo)]
		except:
			os.system("echo \"%s: revision not found\"" % repo)
			continue
		os.system("git -C %s%s checkout %s" % (TOP, repo, rev))
	else:
		os.system("echo \"%s: not found in proj.txt\"" % repo)
