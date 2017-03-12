import os, collections, signal, sys, subprocess, socket
#import triforcetools
#from systemd import daemon
#from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep

#naomi 1 games

Wheeler_DX_18 = {'image':'18wheeler.jpg', 'name':'18Wheeler(DLX)', 'rom':'18_Wheeler_DX.bin' }
Wheeler_STD_18 = {'image':'18wheeler.jpg', 'name':'18Wheeler(STD)', 'rom':'18_Wheeler_STD.bin' }
AirlinePilots = {'image':'airlinepilots.jpg', 'name':'AirlinePilot', 'rom':'AirlinePilots.bin' }
Akatsuki_Bk_Ausf_Achse = {'image':'akatsuki.jpg', 'name':'AkatsukiBlitzkampfAufAsche', 'rom':'Akatsuki_Bk_Ausf_Achse.bin' }
AlienFront = {'image':'alienfront.jpg', 'name':'AlienFront', 'rom':'AlienFront.bin' }
AzumangaDaiohPuzzleBobble_v3 = {'image':'azumanga.jpg', 'name':'AzumangaDaiohPuzzleBobble', 'rom':'AzumangaDaiohPuzzleBobble_v3.bin' }
BorderDown_v3 = {'image':'bdrdown.png', 'name':'BorderDown', 'rom':'BorderDown_v3.bin' }
BurningCasino_v3 = {'image':'burningc.jpg', 'name':'BurningCasino', 'rom':'BurningCasino_v3.bin' }
Capcom_Vs_SNK_2_Millionaire_Fighting_2001 = {'image':'cvsgd.png', 'name':'Capcomvs.SNK2M.Fighting2001', 'rom':'Capcom_Vs_SNK_2_Millionaire_Fighting_2001.bin' }
Capcom_vs_SNK_Millenium_Fight_2000 = {'image':'cvs2gd.png', 'name':'Capcomvs.SNKM.Fight2K', 'rom':'Capcom_vs_SNK_Millenium_Fight_2000.bin' }
Capcom_vs_SNK_Millenium_Fight_2000_Pro = {'image':'cvsgd.png', 'name':'Capcomvs.SNKM.Fight2KPro', 'rom':'Capcom_vs_SNK_Millenium_Fight_2000_Pro.bin' }
ChaosField_v3 = {'image':'chaosfield.jpg', 'name':'ChaosField', 'rom':'ChaosField_v3.bin' }
CleopatraFortunePlus_v6 = {'image':'cleof.jpg', 'name':'CleopatraFortunePlus', 'rom':'CleopatraFortunePlus_v6.bin' }
ConfidentialMission = {'image':'confmiss.png', 'name':'ConfidentialMission', 'rom':'ConfidentialMission.bin' }
CosmicSmash = {'image':'csmash.png', 'name':'CosmicSmash', 'rom':'CosmicSmash.bin' }
CrazyTaxi = {'image':'crazytaxi.jpg', 'name':'CrazyTaxi', 'rom':'CrazyTaxi.bin' }
DeadOrAlive2 = {'image':'doa2.png', 'name':'DeadorAlive2', 'rom':'DeadOrAlive2.bin' }
DeadOrAlive2Millenium = {'image':'doa2m.png', 'name':'DeadorAlive2Millenium', 'rom':'DeadOrAlive2Millenium.bin' }
DeathCrimsonOX = {'image':'deathcox.png', 'name':'DeathCrimsonOX', 'rom':'DeathCrimsonOX.bin' }
DokiDokiIdolStarSeeker = {'image':'dokidoki.png', 'name':'DokiDokiIdolStarSeeker', 'rom':'DokiDokiIdolStarSeeker.bin' }
DynamiteDekaEx = {'image':'dybb99.png', 'name':'DynamiteDekaEx', 'rom':'DynamiteDekaEx.bin' }
Giant_Gram_2000 = {'image':'gram2000.png', 'name':'GiantGram2KZnProWrestle3', 'rom':'Giant_Gram_2000.bin' }
Giant_Gram_EPR = {'image':'gram2000.png', 'name':'GiantGramZen.ProWrestle2', 'rom':'Giant_Gram_EPR-21820_PATCHED.bin' }
GigaWing2 = {'image':'gigawing2.jpg', 'name':'Gigawing2', 'rom':'GigaWing2.bin' }
GuiltyGearXX = {'image':'ggx.png', 'name':'GuiltyGearXX', 'rom':'GuiltyGearXX.bin' }
GuiltyGearXXAccentCore_v6 = {'image':'ggxx.png', 'name':'GuiltyGearXXAccentCore', 'rom':'GuiltyGearXXAccentCore_v6.bin' }
GuiltyGearXXReload = {'image':'ggxxrl.png', 'name':'GuiltyGearXXReload', 'rom':'GuiltyGearXXReload.bin' }
GuiltyGearXXSlash_v6 = {'image':'ggxxsla.png', 'name':'GuiltyGearXXSlash', 'rom':'GuiltyGearXXSlash_v6.bin' }
GunSpike = {'image':'gunspike.jpg', 'name':'Gunspike', 'rom':'GunSpike.bin' }
HeavyMetalGeomatrix = {'image':'hmgeo.png', 'name':'HeavyMetalGeomatrix', 'rom':'HeavyMetalGeomatrix.bin' }
Ikaruga_v3 = {'image':'ikaruga.png', 'name':'Ikaruga', 'rom':'Ikaruga_v3.bin' }
Illvelo_v6 = {'image':'irubero.jpg', 'name':'Illvelo', 'rom':'Illvelo_v6.bin' }
Jambo_Safari = {'image':'jambo.jpg', 'name':'JamboSafari', 'rom':'Jambo_Safari.bin' }
JingyStormTheArcade = {'image':'jingystm.png', 'name':'JingyStormTheArcade', 'rom':'JingyStormTheArcade.bin' }
karous_v3 = {'image':'karous.png', 'name':'Karous', 'rom':'karous_v3.bin' }
kov7spirits = {'image':'kov7sprt.jpg', 'name':'KnightsofValorSevenSpirits', 'rom':'kov7spirits.bin' }
KuruKuruChameleon_v3 = {'image':'kurucham.png', 'name':'KuruKuruChameleon', 'rom':'KuruKuruChameleon_v3.bin' }
LaKeyboardxyu_v3 = {'image':'keyboard.png', 'name':'LaKeyboardxyu', 'rom':'LaKeyboardxyu_v3.bin' }
Lupin3TheShooting = {'image':'lupinsho.png', 'name':'Lupin3TheShooting', 'rom':'Lupin3-TheShooting.bin' }
LupinTheTyping = {'image':'luptype.png', 'name':'LupinTheTyping', 'rom':'Lupin-TheTyping.bin' }
mamonorov6 = {'image':'moeru.png', 'name':'Mamoru-kunwaNoro.Shimatta!', 'rom':'mamonorov6.bin' }
MarvelVsCapcom2 = {'image':'mvsc2.png', 'name':'Marvelvs.Capcom2', 'rom':'MarvelVsCapcom2.bin' }
TheMazeOfTheKings = {'image':'mok.png', 'name':'MazeoftheKing', 'rom':'TheMazeOfTheKings.bin' }
MeltyBloodActCadenza = {'image':'meltybld.png', 'name':'MeltyBloodActCadenza[A]', 'rom':'MeltyBloodActCadenza(RevA).bin' }
MeltyBloodActCadenzaVerB_v3 = {'image':'meltyb.png', 'name':'MeltyBloodActCadenza[B]', 'rom':'MeltyBloodActCadenzaVerB_v3.bin' }
MeltyBloodActCadenzaVerB2_v3 = {'image':'meltyba.png', 'name':'MeltyBloodActCadenza[B2]', 'rom':'MeltyBloodActCadenzaVerB2_v3.bin' }
MeltyBloodActressAgain_v6 = {'image':'meltyba.png', 'name':'MeltyBloodActressAgain', 'rom':'MeltyBloodActressAgain_v6.bin' }
MeltyBloodActressAgain = {'image':'meltyba.png', 'name':'MeltyBloodActressAgainNP', 'rom':'MeltyBloodActressAgain.bin' }
MobileSuitGundam_FederationVsZeon = {'image':'gundmgd.png', 'name':'MobSuitGundamFed.VsZeon', 'rom':'MobileSuitGundam-FederationVsZeon.bin' }
MobileSuitGundam_FederationVsZeonDX = {'image':'gundmxgd.png', 'name':'MobSuitGundamFed.VsZeonDX', 'rom':'MobileSuitGundam-FederationVsZeonDX.bin' }
MonkeyBall = {'image':'monkeyba.png', 'name':'MonkeyBall', 'rom':'MonkeyBall.bin' }
MusapeysChocoMarker = {'image':'chocomk.png', 'name':'MusapeysChocoMarker', 'rom':'MusapeysChocoMarker.bin' }
NoukonePuzzleTakoron = {'image':'konekone.jpg', 'name':'NomisoKoneKonePuzzleTakoron', 'rom':'NoukonePuzzleTakoron.bin' }
Powerstone = {'image':'pstone.png', 'name':'PowerStone', 'rom':'Powerstone.bin' }
PowerStone2 = {'image':'pstone2.png', 'name':'PowerStone2', 'rom':'PowerStone2.bin' }
RivalSchools2_ProjectJustice = {'image':'projectjustice.jpg', 'name':'ProjectJusticeRivalSchool2', 'rom':'RivalSchools2-ProjectJustice.bin' }
Psyvariar2_v6 = {'image':'psyvar2.png', 'name':'Psyvariar2', 'rom':'Psyvariar2_v6.bin' }
Puyo_Puyo_Da_EPR = {'image':'puyofev.png', 'name':'PuyoPuyoDa', 'rom':'Puyo_Puyo_Da_EPR-22206_PATCHED.bin' }
PuyoPuyoFever_v6 = {'image':'puyofev.png', 'name':'PuyoPuyoFever', 'rom':'PuyoPuyoFever_v6.bin' }
QuizKeitaiQMode = {'image':'quizqgd.png', 'name':'QuizKeitaiQMode', 'rom':'QuizKeitaiQMode.bin' }
Radirgy_v3 = {'image':'radirgy.png', 'name':'Radirgy', 'rom':'Radirgy_v3.bin' }
RadirgyNoa_v6 = {'image':'radirgy.png', 'name':'RadirgyNoa', 'rom':'RadirgyNoa_v6.bin' }
Samba_De_Amigo_EPR = {'image':'samba.png', 'name':'SambadeAmigo', 'rom':'Samba_De_Amigo_EPR-22966B_Patched.bin' }
Sega_Marine_Fishing = {'image':'segamarinefishing.jpg', 'name':'SegaMarineFishing', 'rom':'Sega_Marine_Fishing_EPR-22221.bin' }
SegaStrikeFighter = {'image':'ss2005.png', 'name':'SegaStrikeFighter', 'rom':'SegaStrikeFighter.bin' }
SegaTetris = {'image':'tetkiwam.png', 'name':'SegaTetris', 'rom':'SegaTetris.bin' }
senkov3 = {'image':'senko.png', 'name':'SenkonoRonde', 'rom':'senkov3.bin' }
senkonewv6 = {'image':'senko.png', 'name':'SenkonoRondeNewVer', 'rom':'senkonewv6.bin' }
SenkoNoRondeSP_v3 = {'image':'senko.png', 'name':'SenkonoRondeSP', 'rom':'SenkoNoRondeSP_v3.bin' }
ShikigamiNoShiroII_v6 = {'image':'shikgam2.png', 'name':'ShikigaminoShiroII', 'rom':'ShikigamiNoShiroII_v6.bin' }
ShootingLove2007Exzeal_v6 = {'image':'exzeal.jpg', 'name':'ShootingLove2007-Exzeal', 'rom':'ShootingLove2007-Exzeal_v6.bin' }
Slashout = {'image':'slashout.png', 'name':'SlashOut', 'rom':'Slashout.bin' }
spawn = {'image':'spawn.png', 'name':'Spawn', 'rom':'spawn.bin' }
SpikersBattle = {'image':'spkrbtl.png', 'name':'SpikersBattle', 'rom':'SpikersBattle.bin' }
SportsJam = {'image':'sprtjam.png', 'name':'SportsJam', 'rom':'SportsJam.bin' }
StreetFighterZero3Upper = {'image':'sfz3ugd.png', 'name':'StreetFighterZero3Upper', 'rom':'StreetFighterZero3Upper.bin' }
SuperShanghai2005_v6 = {'image':'ss2005.png', 'name':'SuperShanghai2005', 'rom':'SuperShanghai2005_v6.bin' }
SuperShanghai2005VerA_v6 = {'image':'ss2005.png', 'name':'SuperShanghai2005[A]', 'rom':'SuperShanghai2005VerA_v6.bin' }
TetrisKiwamemichi_v6 = {'image':'tetkiwam.png', 'name':'TetrisKiwamemichi', 'rom':'TetrisKiwamemichi_v6.bin' }
ToyFighter = {'image':'toyfight.png', 'name':'ToyFighter', 'rom':'ToyFighter.bin' }
TriggerHeartExelica_v6 = {'image':'trgheart.png', 'name':'TriggerHeartExelica', 'rom':'TriggerHeartExelica_v6.bin' }
Trizeal_v3 = {'image':'trizeal.png', 'name':'Trizeal', 'rom':'Trizeal_v3.bin' }
TheTypingOfTheDead = {'image':'totd.png', 'name':'TypingoftheDead', 'rom':'TheTypingOfTheDead.bin' }
UnderDefeat_v3 = {'image':'undefeat.png', 'name':'UnderDefeat', 'rom':'UnderDefeat_v3.bin' }
Usagui_YamashiroMahjongHen_v3 = {'image':'usagui.png', 'name':'UsaguiYamashiroMahjongHen', 'rom':'Usagui-YamashiroMahjongHen_v3.bin' }
VirtuaAthlete = {'image':'vathlete.png', 'name':'VirtuaAthlete', 'rom':'VirtuaAthlete.bin' }
VirtuaGolf = {'image':'virgolf.png', 'name':'VirtuaGolf', 'rom':'VirtuaGolf.bin' }
VirtuaNBA = {'image':'virnba.png', 'name':'VirtuaNBA', 'rom':'VirtuaNBA.bin' }
VirtuaStriker2 = {'image':'vs2_2k.png', 'name':'VirtuaStriker2Ver.2000', 'rom':'VirtuaStriker2-2000.bin' }
VirtuaTennis = {'image':'vtennisg.png', 'name':'VirtuaTennis', 'rom':'VirtuaTennis.bin' }
VirtuaTennis2 = {'image':'vtennis2.png', 'name':'VirtuaTennis2', 'rom':'VirtuaTennis2.bin' }
WaveRunnerGP = {'image':'wrgp.jpg', 'name':'WaveRunnerGP', 'rom':'WaveRunnerGP.bin' }
WorldSeriesBaseball = {'image':'wsbbgd.png', 'name':'WorldSeriesBaseball', 'rom':'WorldSeriesBaseball.bin' }
WWF_Royal_Rumble = {'image':'wwfrr.jpg', 'name':'WWFRoyalRumble', 'rom':'WWF_Royal_Rumble.bin' }
ZeroGunner2 = {'image':'zerogunner2.jpg', 'name':'ZeroGunner2', 'rom':'ZeroGunner2.bin' }
ZombieRevenge = {'image':'zombrvn.png', 'name':'ZombieRevenge', 'rom':'ZombieRevenge.bin' }

#atomiswave
AnimalBasket = {'image':'animal_basket.png', 'name':'AnimalBasket', 'rom':'gdrom_anmlbskt.bin' }
DemolishFist = {'image':'dfist.jpg', 'name':'DemolishFist', 'rom':'demolishfist.bin' }
DirtyPigskinFootball = {'image':'dirtypigskin.jpg', 'name':'DirtyPigskinFootball', 'rom':'gdrom_dirtypigskin_v3.bin' }
dol222 = {'image':'dolphinb.png', 'name':'DolphinBlue', 'rom':'dol222.bin' }
DolphinBlue = {'image':'dolphinb.png', 'name':'DolphinBlue', 'rom':'dolphinblue.bin' }
FasterThanSpeed = {'image':'faster_than_speed.png', 'name':'FasterThanSpeed', 'rom':'ftspeed.bin' }
FOTNS_Naomi2_Fixed = {'image':'fotns.png', 'name':'FistoftheNorthStar', 'rom':'FOTNS_Naomi2_Fixed.bin' }
GuiltyGearIsuka = {'image':'guiltygearisuka.jpg', 'name':'GuiltyGearIsuka', 'rom':'GuiltyGearIsuka.bin' }
GuiltyGearX15 = {'image':'ggx15.jpg', 'name':'GuiltyGearX15', 'rom':'ggx15.bin' }        
TheKingofFightersXI = {'image':'kofxi.png', 'name':'TheKingofFightersXI', 'rom':'gdrom_KOFXI_v5.bin' }
TheKingofFightersXIAF = {'image':'kofxi.png', 'name':'TheKingofFightersXI(Unlocked)', 'rom':'gdrom_KOFXI_v5_AllFighters.bin' }
TheKingofFightersNeowave = {'image':'kofneowave.jpg', 'name':'TheKingofFightersNeowave', 'rom':'KingOfFightersNeowave.bin' }
KnightsofValour = {'image':'kovss.jpg', 'name':'KnightsofValour', 'rom':'kov7spirits.bin' }
KnightsofValour7 = {'image':'kovss.jpg', 'name':'KnightsofValour7', 'rom':'kov7spirits_Naomi2_Fixed.bin' }
MaximumSpeed = {'image':'maximum_speed.jpg', 'name':'MaximumSpeed', 'rom':'gdrom_maxspeed_v4.bin' }
MetalSlug6 = {'image':'ms6.png', 'name':'MetalSlug6', 'rom':'mslug6.bin' }
MetalSlug6Blood = {'image':'ms6.png', 'name':'MetalSlug6(Blood)', 'rom':'AWViolentMetalSlug6.bin' }
TheRumbleFish = {'image':'rumble-fish.png', 'name':'TheRumbleFish', 'rom':'gdrom-rumblefish.bin' }
TheRumbleFish2 = {'image':'rumblefish2.png', 'name':'TheRumbleFish2', 'rom':'gdrom_rumblef2_v4.bin' }
SalaryMan = {'image':'salaryman.jpg', 'name':'SalaryMan', 'rom':'gdrom_salmankt_JVS_OK_BIOS_OK_Video_OK.bin' }
SamuraiShodown6 = {'image':'samurai-shodown-6.jpg', 'name':'SamuraiShodown6', 'rom':'SamuraiShowdownVI.bin' }
SamuraiShodownVI = {'image':'samurai-shodown-6.jpg', 'name':'SamuraiShodownVI', 'rom':'gdrom_salmankt_JVS_OK_BIOS_OK_Video_OK.bin' }
SegaBassFishingChallenge = {'image':'basschallenge.jpg', 'name':'SegaBassFishingChallenge', 'rom':'basschanllenge.bin' }
SegaClayChallenge = {'image':'claychallenge.png', 'name':'SegaClayChallenge', 'rom':'gdrom_sprtshot.bin' }
SportsShootingUSA = {'image':'sportsshooting.jpg', 'name':'SportsShootingUSA', 'rom':'ftspeed.bin' }
SushiBar = {'image':'shushibar.jpg', 'name':'SushiBar', 'rom':'gdrom_Sushibar_v2.bin' }

#Naomi 2
BeachSpikers = {'image':'BeachSpikers.png', 'name':'BeachSpikers~', 'rom':' BeachSpikers.bin' }
ClubKartEuropeanSession = {'image':'clubkarteurope.gif', 'name':'ClubKartEuropeanSession', 'rom':'ClubKartEuropeanSessionUnlocked.bin' }
InitialD3Export = {'image':'idasv3logo.gif', 'name':'InitialD3Export', 'rom':'Initial_D3_Export.bin' }
InitialD2Export = {'image':'Initial2.png', 'name':'InitialD2Export', 'rom':'InitialD2exp.bin' }
InitialDExport = {'image':'', 'name':'InitialDExport', 'rom':'InitialDexp.bin' }
InitialD2Japanese = {'image':'initald-japamn.jpg', 'name':'InitialD2Japanese', 'rom':'InitialD2jap.bin' }
InitialDJapanese = {'image':'InitialDJapan.jpg', 'name':'InitialDJapanese', 'rom':'InitialDjap.bin' }
KingOfRoute66 = {'image':'kor66.jpg', 'name':'KingOfRoute66', 'rom':'KingOfRoute66.bin' }
VirtuaFighter4EvoverB = {'image':'vf4evo.jpg', 'name':'VirtuaFighter4EvoverB', 'rom':'VirtuaFighter4Evo_verb.bin' }
VirtuaFighter4FinalTunedverB = {'image':'vf4tuned.jpg', 'name':'VirtuaFighter4FinalTunedverB', 'rom':'VirtuaFighter4FinalTuned_verb.bin' }
VirtuaStriker3 = {'image':'virtuastriker3.jpg', 'name':'VirtuaStriker3', 'rom':'VirtuaStriker3.bin' }


			
#naomi1 = [sf3, giga2, underd ]
naomi1 = [Wheeler_DX_18 , Wheeler_STD_18 , AirlinePilots , Akatsuki_Bk_Ausf_Achse , AlienFront , AzumangaDaiohPuzzleBobble_v3 , BorderDown_v3 , BurningCasino_v3 , Capcom_Vs_SNK_2_Millionaire_Fighting_2001 , Capcom_vs_SNK_Millenium_Fight_2000 , Capcom_vs_SNK_Millenium_Fight_2000_Pro , ChaosField , CleopatraFortunePlus_v6 , ConfidentialMission , CosmicSmash , CrazyTaxi , DeadOrAlive2 , DeadOrAlive2Millenium , DeathCrimsonOX , DokiDokiIdolStarSeeker , DynamiteDekaEx , Giant_Gram_2000 , Giant_Gram_EPR , GigaWing2 , GuiltyGearXX , GuiltyGearXXAccentCore_v6 , GuiltyGearXXReload , GuiltyGearXXSlash_v6 , GunSpike , HeavyMetalGeomatrix , Ikaruga_v3 , Illvelo_v6 , Jambo_Safari , JingyStormTheArcade , karous_v3 , kov7spirits , KuruKuruChameleon_v3 , LaKeyboardxyu_v3 , Lupin3TheShooting , LupinTheTyping , mamonorov6 , MarvelVsCapcom2 , TheMazeOfTheKings , MeltyBloodActCadenza , MeltyBloodActCadenzaVerB_v3 , MeltyBloodActCadenzaVerB2_v3 , MeltyBloodActressAgain_v6 , MeltyBloodActressAgain , MobileSuitGundam_FederationVsZeon , MobileSuitGundam_FederationVsZeonDX , MonkeyBall , MusapeysChocoMarker , NoukonePuzzleTakoron , Powerstone , PowerStone2 , RivalSchools2_ProjectJustice , Psyvariar2_v6 , Puyo_Puyo_Da_EPR , PuyoPuyoFever_v6 , QuizKeitaiQMode , Radirgy_v3 , RadirgyNoa_v6 , Samba_De_Amigo_EPR , Sega_Marine_Fishing , SegaStrikeFighter , SegaTetris , senkov3 , senkonewv6 , SenkoNoRondeSP_v3 , ShikigamiNoShiroII_v6 , ShootingLove2007Exzeal_v6 , Slashout , spawn , SpikersBattle , SportsJam , StreetFighterZero3Upper , SuperShanghai2005_v6 , SuperShanghai2005VerA_v6 , TetrisKiwamemichi_v6 , ToyFighter , TriggerHeartExelica_v6 , Trizeal_v3 , TheTypingOfTheDead , UnderDefeat_v3 , Usagui_YamashiroMahjongHen_v3 , VirtuaAthlete , VirtuaGolf , VirtuaNBA , VirtuaStriker2 , VirtuaTennis , VirtuaTennis2 , WaveRunnerGP , WorldSeriesBaseball , WWF_Royal_Rumble , ZeroGunner2 , ZombieRevenge , AnimalBasket , DemolishFist , DirtyPigskinFootball , dol222 , DolphinBlue , FasterThanSpeed , FOTNS_Naomi2_Fixed , GuiltyGearIsuka , GuiltyGearX15 , TheKingofFightersXI , TheKingofFightersXIAF , TheKingofFightersNeowave , KnightsofValour , KnightsofValour7 , MaximumSpeed , MetalSlug6 , MetalSlug6Blood , TheRumbleFish , TheRumbleFish2 , SalaryMan , SamuraiShodown6 , SamuraiShodownVI , SegaBassFishingChallenge , SegaClayChallenge , SportsShootingUSA , SushiBar , BeachSpikers , ClubKartEuropeanSession , InitialD3Export , InitialD2Export , InitialDExport , InitialD2Japanese , InitialDJapanese , KingOfRoute66 , VirtuaFighter4EvoverB , VirtuaFighter4FinalTunedverB , VirtuaStriker3]


rom_dir = '/boot/roms'

bin = 'StreetFighterZero3Upper.bin'
top = '<html><body><p align="center"><font face="verdana" color="grey">'
footer = "</font></p></body></html>"

webpage = open('/var/www/html/index.html', 'w')             # open input file
webpage.write(top)

#foundromfiles = [romf[:-1] for romf in os.popen('dir '+rom_dir+ ' /B')]
# Uncomment for 'ls' NOT 'dir'!!!
foundromfiles = os.popen('ls '+rom_dir).readlines( )


#print foundromfiles

for game in naomi1:
	#print game['rom']
	for rom in foundromfiles:
		rom = rom.rstrip()
		#print "rom = "+rom
		#print "game['rom'] = "+game['rom']
		if (rom == game['rom']):
			#print "-- found game[rom] = "+game['rom']+" = rom: "+rom
			webpage.write("<a href='load.php?rom="+game['rom']+"'>"+"<img src=images/"+game['image']+"></br>"+game['name']+"</a></br></br>")
			#print "found rom: "+rom
	
	#if not os.path.isfile(rom_dir+game['rom']):
	#if (game['rom'] == bin):
		
		#print "<a href='http://192.168.1.1/aaa.html?game="+game['rom']+"></a><br>"

# Purge game dictionary of game files that can't be found
# missing_games = []
# for key, value in games.iteritems():
    # if not os.path.isfile(rom_dir+value):
        # missing_games.append(key)
# for missing_game in missing_games:
    # del games[missing_game]		
		
webpage.write("</br>");

webpage.write("<a href='reboot.php'>"+"Reboot PI"+"</a></br></br>")
webpage.write("<a href='shutdown.php'>"+"Shut Down & Power Off PI"+"</a></br></br>")		
		
webpage.close()
		
