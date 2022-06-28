import sys
import pygame
from player import Player
from partner import Partner, Partnerf
from defence import Defence
from attack import Attack,Elephant
from gauge import Hp,Hissatsu,Background,Countdown
from cutin import Cutin, Effect
from yolo_take import detect
#from gauge import Gauge
import startsc
import multiprocessing


def main():
    # gameの初期化
    pygame.init()

    # cap = cv2.VideoCapture(0)

    game_width = 1280
    game_height = 720
    game_end = False

    
    clock = pygame.time.Clock()


    # スクリーンとバックグランドの設定
    screen = pygame.display.set_mode((int(game_width), int(game_height)))
    
    background = pygame.image.load('./assets/bg.jpg')
    background = pygame.transform.scale(
        background, (int(game_width), int(game_height)))
    background = background.convert_alpha()
    
    
    black = pygame.image.load('./assets/black.png')
    black = black.convert_alpha()

    #scoreboard = pygame.image.load('./assets/scoreboard.png')
    #scoreboard = pygame.transform.scale(
       # scoreboard, (int(game_width), 100))

    fps = 60
    #フォントの定義　右の数字はフォントサイズ
    font = pygame.font.Font(None, 70)
    #bgm再生の例
    pygame.mixer.music.load("./assets/shiningstar.mp3")
    #pygame.mixer.music.play(loops=-1, start=0.0)
    update_type = 0

    #両プレイヤーの行動可否フラグ
    first_able = True
    second_able = True
    
    #入力管理系統
    first_clist = [7,7,7,7,7]
    second_clist = [7,7,7,7,7]

    
    f_cc = 7
    s_cc = 7
   

    
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
    first_eagle = Attack(True, 8, ["./assets/se/bill.wav","./assets/se/eagle.wav",36],30,[12,3,3,3,3,6,6,3,3,3,3,3])
    first_eagle.voice.set_volume(0.15)
    first_eaglecutin = Cutin(True,3)
    second_eaglecutin = Cutin(False,3)
    #犬弱
    second_dog = Attack(False, 8, ["./assets/se/nail.wav","./assets/se/dog.wav",36],30,[3,3,6,6,6,6,6,6,6,9,9])
    #エフェクト
    effect_dageki = Effect(False, 6, 895,220,350,350,False,False,[3,3,4,4,4,4])
    effect_deffence = Effect(True, 9, 675,300,250,250,False,False,[2,2,2,2,2,2,2,2,2,2])
    
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
    #特殊なエレファントグループ
    elephant_group = pygame.sprite.Group()
    elephant_group.add(first_elephant)
    elephant_group.add(second_elephant)
    
    #そのほか
    se_deffence = pygame.mixer.Sound("./assets/se/deffence.wav")
    se_deffence.set_volume(0.35)
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
    
    #初めのやーつです
    while(True):
        
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
        bg_group.update()
        bg_group.draw(screen)
        fgroup.update()
        fgroup.draw(screen)
        fgroup1.update()
        fgroup1.draw(screen)
        fgroup2.update()
        
        
        
        
        pygame.display.flip()
        clock.tick(60)
        
        
        
    #damage関数
    def damage(Player1,damage,hirumilen):
        if Player1 == True:
            first_hp.hp -= damage
            first_player.hirumi_seq[-1] = hirumilen
            if first_hp.hp <= 0.0:
                first_player.death = True
                first_partner.death = True
                fps = 30
            else:
                first_player.hirumi = True
                first_player.hirumi_init = True
                fps = 60
            first_player.excute = False
            first_player.excute_init = True
            first_partner.attack = False
            first_partner.attack_init = True
            first_partner.dog_atk.active = False
            first_partner.dog_atk.init = True
            first_partner.dog_atk1.active = False
            first_partner.dog_atk1.init = True
        
        else:
            second_hp.hp -= damage
            second_player.hirumi_seq[-1] = hirumilen
            if second_hp.hp <= 0.0:
                second_player.death = True
                second_partner.death = True
                fps = 30
            else:
                second_player.hirumi = True
                second_player.hirumi_init = True
                fps = 60
            second_player.excute = False
            second_player.excute_init = True
            second_partner.attack = False
            second_partner.attack_init = True
            second_crab.active = False
            second_crab.hantei = False
            second_crab.init = True
            
        return fps

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
        
        for i in range(5):
            first_clist2[first_clist[i]] += 1
            second_clist2[second_clist[i]] += 1
        
        for i in range(8):
            if i == 7:
                f_cc = 7
                break
            if first_clist2[i] >= 4:
                f_cc = i
                break
        for i in range(8):
            if i == 7:
                s_cc = 7
                break
            if second_clist2[i] >= 4:
                s_cc = i
                break
        #カニ終了判定
        if f_cc != 0 and first_crab.active == True:
            first_crab.active = False
            second_partner.crab = False
            first_crab.init = True
            first_crab.hantei = False
            first_player.excute_seq[-1] = 30
        if s_cc != 0 and second_crab.active == True:
            second_crab.active = False
            second_crab.init = True
            first_partner.crab = False
            second_crab.hantei = False
            second_player.excute_seq[-1] = 30
            
        #行動可否判定
        if first_player.excute == True or first_player.hirumi == True or first_player.death == True or second_player.death == True or first_partner.hissatsu2.active == True or second_partner.hissatsu2.active == True:
            first_able = False
        else:
            first_able = True
            
        if second_player.excute == True or second_player.hirumi == True or first_player.death == True or second_player.death == True or first_partner.hissatsu2.active == True or second_partner.hissatsu2.active == True:
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
            first_player.excute_seq[-1] = 60
            if second_crab.active == True:
                first_eagle.rect.x -= 220
        #ふくろう
        elif f_cc == 2:
            first_player.excute = True
            print("f_owl")
        #うさぎ
        elif f_cc == 3:
            first_player.excute = True
            print("f_rabbit")
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
                first_player.excute_seq[-1] = 90
        #ぞう
        elif f_cc == 5:
            if first_elephant.active1 == False and first_hissatsu.value >= 15.0 and first_elephant.active == False:
                first_elephant.active = True
                first_player.excute = True
                first_elephantcutin.active = True
                first_hissatsu.value -= 15.0
        
        #Player2
        #かに
        if s_cc == 0:
            second_crab.active = True
            second_player.excute = True
            first_partner.crab = True
            if second_elephant.active1 == False:
                second_crabcutin.active = True
            second_player.excute_seq[-1] = 100000
            
            if first_eagle.active == True and first_eagle.count < first_eagle.f_hantei - first_crab.f_hantei:
                
                first_eagle.rect.x -= 220
        #わし
        elif s_cc == 1:
            if second_hissatsu.value >= 100.0:
                second_partner.hissatsu = True
                second_player.excute = True
                
            else:
                second_partner.attack = True
                second_player.excute = True
                if second_elephant.active1 == False:
                    second_eaglecutin.active = True
                second_player.excute_seq[-1] = 90
        #ふくろう
        elif s_cc == 2:
            second_player.excute = True
            print("s_owl")
        #うさぎ
        elif s_cc == 3:
            second_player.excute = True
            print("s_rabbit")
        #いぬ
        elif s_cc == 4:
            second_dog.active = True
            second_player.excute = True 
            if second_elephant.active1 == False:
                second_dogcutin.active = True
            second_player.excute_seq[-1] = 90
            if first_crab.active == True:
                second_dog.rect.x -= 220
        #ぞう
        elif s_cc == 5:
            if second_elephant.active1 == False and second_hissatsu.value >= 15.0 and second_elephant.active == False:
                second_elephant.active = True
                second_player.excute = True
                second_elephantcutin.active = True
                second_hissatsu.value -= 15.0
        
            
        for event in pygame.event.get():
            # ESCキーが押されたら終了
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                game_end = True
            #いったんかに
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_a):
                first_crab.active = True
                second_partner.crab = True
                first_player.excute = True
                first_crabcutin.active = True
                first_player.excute_seq[-1] = 100000
                
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_a):
                first_crab.active = False
                second_partner.crab = False
                first_crab.init = True
                first_crab.hantei = False
                first_player.excute_seq[-1] = 30
                
                #いぬ強攻撃
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_s):
                if first_hissatsu.value >= 100.0:
                    first_partner.hissatsu = True
                    first_player.excute = True
                    first_wolfcutin.active = True
                else:
                    
                    first_partner.attack = True
                    first_player.excute = True
                    first_dogcutin.active = True
                    first_player.excute_seq[-1] = 90

            #イーグル
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_d):
                first_eagle.active = True
                first_player.excute = True 
                first_eaglecutin.active = True
                if second_crab.active == True:
                    first_eagle.rect.x -= 220
                    
                
            #2pかに
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_j):
                second_crab.active = True
                second_player.excute = True
                first_partner.crab = True
                second_crabcutin.active = True
                second_player.excute_seq[-1] = 100000
                
                if first_eagle.active == True and first_eagle.count < first_eagle.f_hantei - first_crab.f_hantei:
                    
                    first_eagle.rect.x -= 220
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_j):
                second_crab.active = False
                second_crab.init = True
                first_partner.crab = False
                second_crab.hantei = False
                second_player.excute_seq[-1] = 30
                
               #イーグル強攻撃 
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_k):
                if first_hissatsu.value >= 100.0:
                    second_partner.hissatsu = True
                    second_player.excute = True
                    
                else:
                    second_partner.attack = True
                    second_player.excute = True
                    second_eaglecutin.active = True
                    second_player.excute_seq[-1] = 90
            #ぞう
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_z):
                first_elephant.active = True
                first_player.excute = True
                first_elephantcutin.active = True
                first_hissatsu.value -= 15.0
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_b):
                second_elephant.active = True
                second_player.excute = True
                second_elephantcutin.active = True
                second_hissatsu.value -= 15.0
                
        #判定判断ゾーン
        #犬強攻撃
        if first_partner.dog_atk.hantei == True:
            fps = damage(False,15.0,15)
            first_partner.dog_atk.hantei = False
            first_hissatsu.value += 5.0
            second_hissatsu.value += 10.0
        if first_partner.dog_atk1.hantei == True:
            fps = damage(False,5.0,90)
            second_crab.death = True
            first_partner.dog_atk1.hantei = False
            first_hissatsu.value += 10.0
            second_hissatsu.value += 5.0
            #イーグル強攻撃
        if second_partner.eagle_atk.hantei == True:
            fps = damage(True,15.0,15)
            second_partner.eagle_atk.hantei = False
        if second_partner.eagle_atk1.hantei == True:
            first_crab.death = True
            fps = damage(True,5.0,90)
            second_partner.eagle_atk1.hantei = False
            
        if first_partner.hissatsu2.hantei[0] == True:
            fps = damage(False,10.0,15)
            first_partner.hissatsu2.hantei[0] = False
        if first_partner.hissatsu2.hantei[1] == True:
            fps = damage(False,10.0,15)
            first_partner.hissatsu2.hantei[1] = False
        if first_partner.hissatsu2.hantei[2] == True:
            fps = damage(False,20.0,15)
            first_partner.hissatsu2.hantei[2] = False
            
         #わし弱攻撃  
        if first_eagle.hantei == True:
            if second_crab.hantei == False:
                first_eagle.se.play()
                fps = damage(False,5.0,10)
                effect_dageki.active = True
            else:
                effect_deffence.active = True
                se_deffence.play()
                
            first_eagle.hantei = False
        #いぬ弱攻撃
        if second_dog.hantei == True:
            if first_crab.hantei == False:
                second_dog.se.play()
                fps = damage(True,5.0,10)
                #effect_dageki.active = True
            else:
                #effect_deffence.active = True
                se_deffence.play()
                
            second_dog.hantei = False
            
            #ゲーム終了判定
        if first_player.finish == True or second_player.finish == True:
            fps = 60
            for i in range(60):
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
                gauge_group.update()
                #gauge_group.draw(screen)
                #エレファントグループは必ず一番最後
                elephant_group.update()
                elephant_group.draw(screen)
                pygame.display.flip()
                clock.tick(fps)
            startsc.show_finish_screen(screen,first_player.finish)
            break
            
            
        
        #必殺技による暗転判定
        if first_partner.black == True or second_partner.black == True:
            update_type = 1
        else:
            update_type = 0
        
        #描画、アップデートゾーン
        if update_type == 0:
            
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
            gauge_group.update()
            #gauge_group.draw(screen)
            #エレファントグループは必ず一番最後
            elephant_group.update()
            elephant_group.draw(screen)
        elif update_type == 1:
            
            bg_group.draw(screen)
            partner_group.draw(screen)
            player_group.draw(screen)
            defence_group.draw(screen)
            effect_group.draw(screen)
            attack_group.draw(screen)
            cutin_group.draw(screen)
            
            gauge_group.update()
            elephant_group.draw(screen)
            screen.blit(black, (0, 0))
            

            
            if first_partner.black == True:
                
                first_partner.update()
                first_partner_group.draw(screen)
                
            else:
                second_partner.update()
                second_partner_group.draw(screen)
               
            
        
        first_hissatsu.value += 0.5
        second_hissatsu.value += 0.02
        
        
        
        
        #フレームレート
        pygame.display.flip()
        clock.tick(fps)
        
        
    
    
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
    

if __name__ == '__main__':
    detecting = multiprocessing.Process(
        target=detect.run,
        kwargs={
            'source': 0,
            'weights': 'yolo_take/best.pt',
            
        }
    )
    detecting.start()
    
    detecting1 = multiprocessing.Process(
        target=detect.run,
        kwargs={
            'source': 1,
            'weights': 'yolo_take/best.pt',
            'player': 1
        }
    )
    detecting1.start()
    main()


    