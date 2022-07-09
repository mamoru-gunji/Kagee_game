
import sys
import pygame
from player import Player
from partner import Partner, Partnerf
from defence import Defence
from attack import Attack,Elephant,Rabbit,Owl
from gauge import Hp,Hissatsu,Background,Countdown
from cutin import Cutin, Effect
#from gauge import Gauge
import startsc

import warnings
warnings.filterwarnings('ignore')

from startsc import Door, Win



def main():
    # gameの初期化
    pygame.init()

    # cap = cv2.VideoCapture(0)

    game_width = 1280
    game_height = 720
    game_end = False

    bgm_play = True
    clock = pygame.time.Clock()


    # スクリーンとバックグランドの設定
    screen = pygame.display.set_mode((int(game_width), int(game_height)), flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
    
    background = pygame.image.load('./assets/title_0000.png')
    background = pygame.transform.scale(
        background, (int(game_width), int(game_height)))
    background = background.convert_alpha()
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    black = pygame.image.load('./assets/black.png')
    black = black.convert_alpha()

    #scoreboard = pygame.image.load('./assets/scoreboard.png')
    #scoreboard = pygame.transform.scale(
       # scoreboard, (int(game_width), 100))

    fps = 60
    winlist = [False, False]

    #bgm再生の例
    pygame.mixer.music.load("./assets/wafu.mp3")
    pygame.mixer.music.set_volume(0.3)
    
    update_type = 0
    
    font = pygame.font.Font(None, 70)
    text = font.render("K.O.", True, (250, 30, 30))
    

    #両プレイヤーの行動可否フラグ
    first_able = True
    second_able = True
    
    #入力管理系統
    first_clist = [7,7,7,7,7,7,7]
    second_clist = [7,7,7,7,7,7,7]

    
    f_cc = 7
    s_cc = 7
   
    f_kani = False
    s_kani = False

    
    #プレイヤーインスタンスの宣言
    first_player = Player(True)
    second_player = Player(False)
    #パートナーインスタンスの宣言
    first_partner = Partner(True)
    second_partner = Partner(False)
    #ゲージインスタンスの宣言
    first_hp = Hp(True, screen)
    second_hp = Hp(False, screen)
    first_hissatsu = Hissatsu(True, screen)
    second_hissatsu = Hissatsu(False, screen)
    #カニインスタンスの宣言
    first_crab = Defence(True,2,12,[3,3,2,1,3])
    second_crab = Defence(False,2,12,[3,3,2,1,3])
    first_crabcutin = Cutin(True,0)
    second_crabcutin = Cutin(False,0)
    #犬カットイン
    first_dogcutin = Cutin(True,1)
    second_dogcutin = Cutin(False,1)
    first_wolfcutin = Cutin(True,4)
    #象
    first_elephant = Elephant(True)
    second_elephant = Elephant(False)
    first_elephantcutin = Cutin(True,2)
    second_elephantcutin = Cutin(False,2)
    #イーグル弱
    first_eagle = Attack(True, 8, ["./assets/se/bill.wav","./assets/se/eagle.wav",36],30,[3,6,6,6,6,6,6,6,6,6,9,6])
    first_eagle.voice.set_volume(0.15)
    first_eaglecutin = Cutin(True,3)
    second_eaglecutin = Cutin(False,3)
    second_archecutin = Cutin(False,4)
    #犬弱
    second_dog = Attack(False, 8, ["./assets/se/nail.wav","./assets/se/dog.wav",36],30,[3,6,6,6,6,6,6,6,6,9,6])
    #うさぎ
    first_rabbit = Rabbit(True)
    second_rabbit = Rabbit(False)
    first_rabbitcutin = Cutin(True,5)
    second_rabbitcutin = Cutin(False,5)
    #ふくろう
    first_owl = Owl(True)
    second_owl = Owl(False)
    first_owlcutin = Cutin(True,6)
    second_owlcutin = Cutin(False,6)
    
    #エフェクト
    effect_dageki = Effect(False, 6, 895,220,350,350,False,False,[3,3,4,4,4,4])
    effect_deffence = Effect(True, 9, 150,0,1280,720,False,False,[2,2,2,2,2,2,2,2,2,2,2])
    effect_deffence1 = Effect(False, 9, -100,0,1280,720,False,False,[2,2,2,2,2,2,2,2,2,2,2])
    
    #どあ
    door_close = Door(True)
    door_open = Door(False)
    
    #win
    win1 = Win(True)
    win2 = Win(False)
    
    #BG
    background1 = Background()
    
    #プレイヤーグループの設定
    player_group = pygame.sprite.Group()
    player_group.add(first_player)
    player_group.add(second_player)
    #パートナーグループの設定
    partner_group = pygame.sprite.Group()
    first_partner_group = pygame.sprite.Group()
    second_partner_group = pygame.sprite.Group()
    partner_group.add(first_partner)
    partner_group.add(second_partner)
    first_partner_group.add(first_partner)
    second_partner_group.add(second_partner)
    
    #アタック,ディフェンスグループの設定
    attack_group = pygame.sprite.Group()
    defence_group = pygame.sprite.Group()
    defence_group.add(first_crab)
    defence_group.add(second_crab)
    attack_group.add(first_partner.dog_atk)
    attack_group.add(first_partner.dog_atk1)
    attack_group.add(first_eagle)
    attack_group.add(second_dog)
    attack_group.add(second_partner.eagle_atk)
    attack_group.add(second_partner.eagle_atk1)
    attack_group.add(first_partner.hissatsu2)
    attack_group.add(second_partner.hissatsu2)
    attack_group.add(first_rabbit)
    attack_group.add(second_rabbit)
    attack_group.add(first_owl)
    attack_group.add(second_owl)
    #カットイングループの設定
    cutin_group = pygame.sprite.Group()
    cutin_group.add(first_crabcutin)
    cutin_group.add(second_crabcutin)
    cutin_group.add(first_dogcutin)
    cutin_group.add(second_dogcutin)
    cutin_group.add(first_elephantcutin)
    cutin_group.add(second_elephantcutin)
    cutin_group.add(first_eaglecutin)
    cutin_group.add(second_eaglecutin)
    cutin_group.add(first_wolfcutin)
    cutin_group.add(second_archecutin)
    cutin_group.add(first_rabbitcutin)
    cutin_group.add(second_rabbitcutin)
    cutin_group.add(first_owlcutin)
    cutin_group.add(second_owlcutin)
    
    #ゲージグループの設定
    gauge_group = pygame.sprite.Group()
    gauge_group.add(first_hp)
    gauge_group.add(second_hp)
    gauge_group.add(first_hissatsu)
    gauge_group.add(second_hissatsu)
    #エフェクトグループの設定
    effect_group = pygame.sprite.Group()
    effect_group.add(first_partner.dog_atk.effect)
    effect_group.add(first_partner.dog_atk1.effect)
    effect_group.add(effect_dageki)
    effect_group.add(effect_deffence)
    effect_group.add(effect_deffence1)
    #特殊なエレファントグループ
    elephant_group = pygame.sprite.Group()
    elephant_group.add(first_elephant)
    elephant_group.add(second_elephant)
    
    door_group = pygame.sprite.Group()
    door_group.add(door_close)
    door_group.add(door_open)
    
    #そのほか
    se_deffence = pygame.mixer.Sound("./assets/se/deffence.wav")
    se_deffence.set_volume(0.35)
    se_owlhit = pygame.mixer.Sound("./assets/se/owl_hit.wav")
    se_ko = pygame.mixer.Sound("./assets/se/KO.wav")
    bg_group = pygame.sprite.Group()
    bg_group.add(background1)
    
    
    
    
    #初めのやつ用
    first_playerf = Player(True)
    second_playerf = Player(False)
    
    first_partnerf = Partnerf(True)
    second_partnerf = Partnerf(False)
    
    first_hpf = Hp(True, screen)
    second_hpf = Hp(False, screen)
    first_hissatsuf = Hissatsu(True, screen)
    second_hissatsuf = Hissatsu(False, screen)
    countdown = Countdown()
    
    fgroup = pygame.sprite.Group()
    fgroup1 = pygame.sprite.Group()
    fgroup2 = pygame.sprite.Group()
    
    fgroup.add(first_partnerf)
    fgroup.add(second_partnerf)
    fgroup2.add(first_hpf)
    fgroup2.add(second_hpf)
    fgroup2.add(first_hissatsuf)
    fgroup2.add(second_hissatsuf)
     
    fgroup1.add(first_playerf)
    fgroup1.add(second_playerf)
    fgroup1.add(first_dogcutin)
    fgroup1.add(second_eaglecutin)
    fgroup1.add(countdown)
    
    startsc.show_start_screen(screen, background)
    countf = 0
    countf2 = 0
    
    #初めのやーつです
    door_open.active = True
    fcommand = '7'
    scommand = '7'
    
    while(True):
        if countf2 > 30:
            detecttxt1 = open('out.txt', 'r')
            fcommand = detecttxt1.read()
            detecttxt1.close()
    
            detect_text2 = open('out1.txt', 'r')
            scommand = detect_text2.read()
            detect_text2.close()
        
        for event in pygame.event.get():
            # ESCキーが押されたら終了
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                game_end = True
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_a):
                first_partnerf.active = True
                first_playerf.excute = True
                first_dogcutin.active = True
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_s):
                second_partnerf.active = True
                second_playerf.excute = True
                second_eaglecutin.active = True
        
        if first_partnerf.active == False and first_partnerf.active1 == False and fcommand == '4':
            first_partnerf.active = True
            first_playerf.excute = True
            first_dogcutin.active = True
            
        if second_partnerf.active == False and second_partnerf.active1 == False and scommand == '1':
            second_partnerf.active = True
            second_playerf.excute = True
            second_eaglecutin.active = True
        
        if second_partnerf.active1 == True and first_partnerf.active1 == True:
            
            if countf >= 60:
                countdown.active = True
            if countdown.finish == True:
                break
            
            countf += 1
        #アップデートゾーン
        screen.fill((50,50,50))
        fgroup2.update()
        bg_group.update()
        bg_group.draw(screen)
        fgroup.update()
        fgroup.draw(screen)
        fgroup1.update()
        fgroup1.draw(screen)
        door_group.update()
        door_group.draw(screen)
        countf2 += 1
        
        
        
        
        
        pygame.display.flip()
        clock.tick(60)
        
        
        
    #damage関数
    def damage(Player1,damage,hirumilen):
        if Player1 == True:
            first_hp.hp -= damage
            first_player.hirumi_seq[-1] = hirumilen
            first_partner.hirumi_seq[-1] = hirumilen
            if first_hp.hp <= 0.0:
                pygame.mixer.music.fadeout(1000)
                first_player.death = True
                first_partner.death = True
                if winlist[0] == False:
                    winlist[0]=True
                    winlist[1]=True
                fps = 30
            else:
                first_player.hirumi = True
                first_partner.hirumi = True
                #first_player.hirumi_init = True
                fps = 60
            first_player.excute = False
            first_player.excute_init = True
            
            first_partner.hissatsu = False
            first_partner.hissatsu_init = True
            
            first_partner.attack = False
            first_partner.attack_init = True     
            first_partner.dog_atk.active = False
            first_partner.dog_atk.init = True
            first_partner.dog_atk1.active = False
            first_partner.dog_atk1.init = True
            
            first_crab.active = False
            first_crab.hantei = False
            second_partner.crab = False
            second_owl.crab = False
            first_crab.init = True
            first_player.excute_seq[-1] = 30
            
            first_owl.active = False
            first_owl.init = True
            
            first_rabbit.active = False
            first_rabbit.init = True
            first_eagle.active = False
            first_eagle.init = True
            
        
        else:
            second_hp.hp -= damage
            second_player.hirumi_seq[-1] = hirumilen
            second_partner.hirumi_seq[-1] = hirumilen
            if second_hp.hp <= 0.0:
                pygame.mixer.music.fadeout(1000)
                second_player.death = True
                second_partner.death = True
                if winlist[0] == False:
                    winlist[0]=True
                    winlist[1]=False
                fps = 30
            else:
                second_player.hirumi = True
                second_partner.hirumi = True
                #second_player.hirumi_init = True
                fps = 60
            second_player.excute = False
            second_player.excute_init = True
            
            second_partner.hissatsu = False
            second_partner.hissatsu_init = True
            
            second_partner.attack = False
            second_partner.attack_init = True
            second_partner.eagle_atk.active = False
            second_partner.eagle_atk.init = True
            second_partner.eagle_atk1.active = False
            second_partner.eagle_atk1.init = True
            
            second_crab.active = False
            second_crab.hantei = False
            first_partner.crab = False
            first_owl.crab = False
            second_crab.init = True
            second_player.excute_seq[-1] = 30
            
            second_owl.active = False
            second_owl.init = True
            
            second_rabbit.active = False
            second_rabbit.init = True
            second_dog.active = False
            second_dog.init = True
            
        return fps

    pygame.mixer.music.play(loops=-1, start=0.0)
    #大事な大事なメインループ。フレームごとに一回実行
    while (game_end == False):
        
            
        #コマンド読み込み
        detecttxt1 = open('out.txt', 'r')
        fcommand = detecttxt1.read()
        detecttxt1.close()

        detect_text2 = open('out1.txt', 'r')
        scommand = detect_text2.read()
        detect_text2.close()
        
        if fcommand == '':
            fcommand = 7
        else:
            fcommand = (int)(fcommand)
        if scommand == '':
            scommand = 7
        else:
            scommand = (int)(scommand)
        
        first_clist2 = [0,0,0,0,0,0,0,0]
        second_clist2 = [0,0,0,0,0,0,0,0]
        first_clist.append(fcommand)
        second_clist.append(scommand)
        first_clist.pop(0)
        second_clist.pop(0)
        
        for i in range(7):
            first_clist2[first_clist[i]] += 1
            second_clist2[second_clist[i]] += 1
        
        for i in range(8):
            if i == 7:
                f_cc = 7
                break
            if first_clist2[i] >= 6:
                f_cc = i
                break
        for i in range(8):
            if i == 7:
                s_cc = 7
                break
            if second_clist2[i] >= 6:
                s_cc = i
                break
            
        #キーボードゾーン
        for event in pygame.event.get():
            # ESCキーが押されたら終了
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                game_end = True
            #いったんかに
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_a):
                f_kani = True
                
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_a):
                f_kani = False
                f_cc = 7
                
                #いぬ強攻撃
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_s):
                f_cc = 4

            #イーグル
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_d):
                f_cc = 1
            #1pぞう
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_z):
                f_cc = 5
            #うさぎ
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_x):
                f_cc = 3
            #ふくろう
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_c):
                f_cc = 2
                
            #2pかに
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_j):
                s_kani = True
                
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_j):
                s_kani = False
                s_cc = 7

               #いぬ攻撃
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_k):
               s_cc = 4

           #イーグル強攻撃
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_l):
               s_cc = 1
           #2pぞう
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_b):
               s_cc = 5
           #うさぎ
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_n):
               s_cc = 3
           #ふくろう
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_m):
               s_cc = 2
              
        if f_kani == True:
            f_cc = 0
        if s_kani == True:
            s_cc = 0
        #カニ終了判定
        if f_cc != 0 and first_crab.active == True:
            first_crab.active = False
            first_player.excute = False
            first_player.excute_init = True
            second_partner.crab = False
            second_owl.crab = False
            first_crab.init = True
            first_crab.hantei = False
            first_player.excute_seq[-1] = 15
        if s_cc != 0 and second_crab.active == True:
            second_crab.active = False
            second_crab.init = True
            second_player.excute = False
            second_player.excute_init = True
            first_partner.crab = False
            first_owl.crab = False
            second_crab.hantei = False
            second_player.excute_seq[-1] = 15
            
        #行動可否判定
        if first_player.excute == True or first_player.hirumi == True or first_player.death == True or second_player.death == True or first_partner.hissatsu2.active == True or second_partner.hissatsu2.active == True:
            first_able = False
        elif second_rabbit.active2 == True or first_partner.black == True or second_partner.black == True:
            first_able = False
        else:
            first_able = True
            
        if second_player.excute == True or second_player.hirumi == True or first_player.death == True or second_player.death == True or first_partner.hissatsu2.active == True or second_partner.hissatsu2.active == True:
            second_able = False
        elif first_rabbit.active2 == True or first_partner.black == True or second_partner.black == True:
            second_able = False
        else:
            second_able = True
            
        if first_able == False:
            f_cc = 7
        if second_able == False:
            s_cc = 7
        
            
        #読み込んだコマンドをもとに行動決定
        #Player1
        #かに
        if f_cc == 0:
            first_crab.active = True
            second_partner.crab = True
            second_owl.crab = True
            first_player.excute = True
            if first_elephant.active1 == False:
                first_crabcutin.active = True
            first_player.excute_seq[-1] = 100000
            
            if second_dog.active == True and second_dog.count < second_dog.f_hantei - second_crab.f_hantei:
                
                second_dog.rect.x += 220
        #わし
        elif f_cc == 1:
            first_eagle.active = True
            first_player.excute = True 
            if first_elephant.active1 == False:
                first_eaglecutin.active = True
            first_player.excute_seq[-1] = 90
            if second_crab.active == True:
                first_eagle.rect.x -= 270
        #ふくろう
        elif f_cc == 2:
            if first_owl.active == False and first_owl.active2 == False and first_owl.active3 == False and first_hissatsu.value >= 20.0:
                first_hissatsu.value -= 20.0
                first_player.excute = True
                if first_elephant.active1 == False:
                    first_owlcutin.active = True
                first_owl.active = True
        #うさぎ
        elif f_cc == 3:
            if first_rabbit.active2 == False and first_hissatsu.value >= 15.0 and first_rabbit.active == False:
                first_player.excute = True
                first_rabbit.active = True
                if first_elephant.active1 == False:
                    first_rabbitcutin.active = True
                    
                first_hissatsu.value -= 15.0
        #いぬ
        elif f_cc == 4:
            if first_hissatsu.value >= 100.0:
                first_partner.hissatsu = True
                first_player.excute = True
                first_player.excute_seq[-1] = 48
                if first_elephant.active1 == False:
                    first_wolfcutin.active = True
            else:
                
                first_partner.attack = True
                first_player.excute = True
                if first_elephant.active1 == False:
                    first_dogcutin.active = True
                first_player.excute_seq[-1] = 98
        #ぞう
        elif f_cc == 5:
            if first_elephant.active1 == False and  first_elephant.active == False:
                first_elephant.active = True
                first_player.excute = True
                first_elephantcutin.active = True
                first_hissatsu.value += 10.0
        
        #Player2
        #かに
        if s_cc == 0:
            second_crab.active = True
            second_player.excute = True
            first_partner.crab = True
            first_owl.crab = True
            if second_elephant.active1 == False:
                second_crabcutin.active = True
            second_player.excute_seq[-1] = 100000
            
            if first_eagle.active == True and first_eagle.count < first_eagle.f_hantei - first_crab.f_hantei:
                
                first_eagle.rect.x -= 270
        #わし
        elif s_cc == 1:
            if second_hissatsu.value >= 100.0:
                second_partner.hissatsu = True
                second_player.excute = True
                if second_elephant.active1 == False:
                    second_archecutin.active = True
                second_player.excute_seq[-1] = 48
                
            else:
                second_partner.attack_init = True
                second_partner.attack = True
                second_player.excute = True
                if second_elephant.active1 == False:
                    second_eaglecutin.active = True
                second_player.excute_seq[-1] = 106
        #ふくろう
        elif s_cc == 2:
            if second_owl.active == False and second_owl.active2 == False and second_owl.active3 == False and second_hissatsu.value >= 20.0:
                second_player.excute = True
                second_player.excute_seq[-1] = 20
                second_owl.active = True
                if second_elephant.active1 == False:
                    second_owlcutin.active = True
                second_hissatsu.value -= 20.0
        #うさぎ
        elif s_cc == 3:
            if second_rabbit.active2 == False and second_hissatsu.value >= 15.0 and second_rabbit.active == False:
                second_player.excute = True
                second_rabbit.active = True
                
                if second_elephant.active1 == False:
                    second_rabbitcutin.active = True
                second_hissatsu.value -= 15.0
                
        #いぬ
        elif s_cc == 4:
            second_dog.active = True
            second_player.excute = True 
            if second_elephant.active1 == False:
                second_dogcutin.active = True
            second_player.excute_seq[-1] = 90
            if first_crab.active == True:
                second_dog.rect.x += 220
        #ぞう
        elif s_cc == 5:
            if second_elephant.active1 == False and  second_elephant.active == False:
                second_elephant.active = True
                second_player.excute = True
                second_elephantcutin.active = True
                second_hissatsu.value += 10.0
                
        
            
        
                
        #判定判断ゾーン
        #犬強攻撃
        if first_partner.dog_atk.hantei == True:
            if second_partner.hissatsu2.active == False:
                fps = damage(False,10.0,15)
                
                first_hissatsu.value += 5.0
                second_hissatsu.value += 10.0
            first_partner.dog_atk.hantei = False
        if first_partner.dog_atk1.hantei == True:
            if second_partner.hissatsu2.active == False:
                fps = damage(False,5.0,30)
                second_crab.death = True
                first_partner.crab = False
                first_owl.crab = False
                
                first_hissatsu.value += 10.0
                second_hissatsu.value += 5.0
            first_partner.dog_atk1.hantei = False
            #イーグル強攻撃
        if second_partner.eagle_atk.hantei == True:
            if first_partner.hissatsu2.active == False:
                fps = damage(True,10.0,15)
                
                first_hissatsu.value += 10.0
                second_hissatsu.value += 5.0
            second_partner.eagle_atk.hantei = False
        if second_partner.eagle_atk1.hantei == True:
            if first_partner.hissatsu2.active == False:
                first_crab.death = True
                second_partner.crab = False
                second_owl.crab = False
                fps = damage(True,5.0,30)
                
                first_hissatsu.value += 5.0
                second_hissatsu.value += 10.0
            second_partner.eagle_atk1.hantei = False
            
            #wolf
        if first_partner.hissatsu2.hantei[0] == True:
            fps = damage(False,10.0,10)
            first_partner.hissatsu2.hantei[0] = False
        if first_partner.hissatsu2.hantei[1] == True:
            fps = damage(False,5.0,15)
            first_partner.hissatsu2.hantei[1] = False
        if first_partner.hissatsu2.hantei[2] == True:
            fps = damage(False,20.0,15)
            second_hissatsu.value += 20.0
            first_partner.hissatsu2.hantei[2] = False
        if first_partner.hangauge == True:
            first_hissatsu.value = 0
            first_partner.hangauge = False
            
            #始祖鳥
        if second_partner.hissatsu2.hantei[0] == True:
            fps = damage(True,10.0,15)
            second_partner.hissatsu2.hantei[0] = False
            
        if second_partner.hissatsu2.hantei[1] == True:
            fps = damage(True,30.0,30)
            
            first_hissatsu.value += 20.0
            second_partner.hissatsu2.hantei[1] = False
        if second_partner.hangauge == True:
            second_hissatsu.value = 0
            second_partner.hangauge = False
            
            
         #わし弱攻撃  
        if first_eagle.hantei == True:
            if second_partner.hissatsu2.active == False:
                if second_crab.hantei == False:
                    first_eagle.se.play()
                    fps = damage(False,5.0,10)
                    effect_dageki.active = True
                    first_hissatsu.value += 3.0
                    second_hissatsu.value += 7.0
                else:
                    effect_deffence.active = True
                    se_deffence.play()
                    first_hissatsu.value += 10.0
                    second_hissatsu.value += 3.0
                
            first_eagle.hantei = False
        #いぬ弱攻撃
        if second_dog.hantei == True:
            if first_partner.hissatsu2.active == False:
                if first_crab.hantei == False:
                    second_dog.se.play()
                    fps = damage(True,5.0,10)
                    first_hissatsu.value += 7.0
                    second_hissatsu.value += 3.0
                    #effect_dageki.active = True
                else:
                    effect_deffence1.active = True
                    se_deffence.play()
                    first_hissatsu.value += 3.0
                    second_hissatsu.value += 10.0
                
            second_dog.hantei = False
        #うさぎ
        if first_rabbit.hantei == True:
            if second_partner.hissatsu2.active == False:
                fps = damage(False,0,10)
            first_rabbit.hantei = False
        if second_rabbit.hantei == True:
            fps = damage(True,0,10)
            second_rabbit.hantei = False
        #ふくろう    
        if first_owl.hantei == True:
            if second_partner.hissatsu2.active == False:
                if second_crab.hantei == True:
                    se_deffence.play()
                    second_hissatsu.value += 2.0
                else:
                    fps = damage(False,1.0,0)
                    first_hissatsu.value += 1.0
                    se_owlhit.play()
            first_owl.hantei = False
        if second_owl.hantei == True:
            if first_partner.hissatsu2.active == False:
                if first_crab.hantei == True:
                    se_deffence.play()
                    first_hissatsu.value += 2.0
                else:
                    fps = damage(True,1.0,0)
                    se_owlhit.play()
                    second_hissatsu.value += 1.0
            second_owl.hantei = False
            
            
        #fpsが30のときblackを無効
        if fps == 30:
            first_partner.black = False
            second_partner.black = False
            
        #ゲーム終了判定
        if first_player.finish == True or second_player.finish == True:
            fps = 60
            if first_player.finish == True:
                first_partner.black = False
                first_partner.hissatsu2.active = False
            else:
                second_partner.black = False
                second_partner.hissatsu2.active = False
                
            for i in range(260):
                if i == 187:
                    door_close.active = True
                screen.fill((50,50,50))
                gauge_group.update()
                #gauge_group.draw(screen)
                bg_group.update()
                bg_group.draw(screen)
                partner_group.update()
                partner_group.draw(screen)
                player_group.update()
                player_group.draw(screen)
                
                defence_group.update()
                defence_group.draw(screen)
                effect_group.update()
                effect_group.draw(screen)
                attack_group.update()
                attack_group.draw(screen)
                cutin_group.update()
                cutin_group.draw(screen)
                
                
                elephant_group.update()
                elephant_group.draw(screen)
                if i == 60:
                    se_ko.play()
                if i > 60:
                    screen.blit(text, (600, 300))
                    
                door_group.update()
                door_group.draw(screen)
                pygame.display.flip()
                clock.tick(fps)
            
            opt = startsc.show_finish_screen(screen,winlist[1], door_open, door_group, win1, win2)
            if opt == 0:
                break
            else:
                main()
            
            
        
        #必殺技による暗転判定
        if first_partner.black == True or second_partner.black == True:
            update_type = 1
        else:
            update_type = 0
        
        #描画、アップデートゾーン
        if update_type == 0:
            
            screen.fill((50,50,50))
            gauge_group.update()
            #gauge_group.draw(screen)
            bg_group.update()
            bg_group.draw(screen)
            partner_group.update()
            partner_group.draw(screen)
            player_group.update()
            player_group.draw(screen)
            
            defence_group.update()
            defence_group.draw(screen)
            effect_group.update()
            effect_group.draw(screen)
            attack_group.update()
            attack_group.draw(screen)
            cutin_group.update()
            cutin_group.draw(screen)
            #エレファントグループは必ず一番最後
            elephant_group.update()
            elephant_group.draw(screen)
            
        elif update_type == 1:
            
            screen.fill((0,0,0))
            gauge_group.update()
            bg_group.draw(screen)
            partner_group.draw(screen)
            player_group.draw(screen)
            defence_group.draw(screen)
            effect_group.draw(screen)
            attack_group.draw(screen)
            cutin_group.draw(screen)
            
            elephant_group.draw(screen)
            screen.blit(black, (0, 0))
            

            
            if first_partner.black == True:
                
                first_partner.update()
                first_partner_group.draw(screen)
                
            else:
                second_partner.update()
                second_partner_group.draw(screen)
               
            
        
        first_hissatsu.value += 0.0004 * (100.0 - first_hp.hp)
        second_hissatsu.value += 0.0004 * (100.0 - second_hp.hp)
        
        
        #bgm管理ブロック
        if (first_partner.black == True or second_partner.black == True) and bgm_play == True:
            bgm_play = False
            pygame.mixer.music.pause()
        if (first_partner.black == False and second_partner.black == False) and bgm_play == False:
            bgm_play = True
            pygame.mixer.music.unpause()
        
        #フレームレート
        pygame.display.flip()
        clock.tick(fps)
        
        
    
    
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
    

if __name__ == '__main__':
    
    main()


    
