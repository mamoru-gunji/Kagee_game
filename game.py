import sys
import pygame
from player import Player
from partner import Partner
from attack import Attack
#from gauge import Gauge
#from yolo_take import detect
import startsc
import multiprocessing

def main():
    # gameの初期化
    pygame.init()

    # cap = cv2.VideoCapture(0)

    game_width = 1280
    game_height = 720
    game_end = False

    game_center_y = 360
    
    clock = pygame.time.Clock()


    # スクリーンとバックグランドの設定
    screen = pygame.display.set_mode((int(game_width), int(game_height)))
    background = pygame.image.load('./assets/bg.jpg')
    background = pygame.transform.scale(
        background, (int(game_width), int(game_height)))

    #scoreboard = pygame.image.load('./assets/scoreboard.png')
    #scoreboard = pygame.transform.scale(
       # scoreboard, (int(game_width), 100))

    
    #フォントの定義　右の数字はフォントサイズ
    font = pygame.font.Font(None, 70)
    #bgm再生の例
    pygame.mixer.music.load("./assets/shiningstar.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
    

    startsc.show_start_screen(screen, background)
    
    #プレイヤーインスタンスの宣言
    first_player = Player(True)
    second_player = Player(False)
    #パートナーインスタンスの宣言
    first_partner = Partner(True)
    second_partner = Partner(False)
    #カニインスタンスの宣言
    first_crab = Attack(True,2,-1,20,[10,10,10])
    second_crab = Attack(False,2,-1,20,[10,10,10])
    #プレイヤーグループの設定
    player_group = pygame.sprite.Group()
    player_group.add(first_player)
    player_group.add(second_player)
    #パートナーグループの設定
    partner_group = pygame.sprite.Group()
    partner_group.add(first_partner)
    partner_group.add(second_partner)
    #アタックグループの設定
    attack_group = pygame.sprite.Group()
    attack_group.add(first_crab)
    attack_group.add(second_crab)
    

    #大事な大事なメインループ。フレームごとに一回実行
    while (game_end == False):
        for event in pygame.event.get():
            # ESCキーが押されたら終了
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                game_end = True
            #いったんかに
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_a):
                first_crab.active = True
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_a):
                first_crab.active = False
                first_crab.init = True
                
                
        #描画、アップデートゾーン
        screen.blit(background, (0, 0))
        player_group.update()
        player_group.draw(screen)
        partner_group.update()
        partner_group.draw(screen)
        attack_group.update()
        attack_group.draw(screen)
        
        
        
        #フレームレート
        pygame.display.flip()
        clock.tick(60)
        
        
    
    
        
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
    

if __name__ == '__main__':
    main()


    