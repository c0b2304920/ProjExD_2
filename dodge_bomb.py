import os
import random
import sys
import time

import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA={pg.K_UP:(0, -5), # 練習問題1
        pg.K_DOWN:(0, +5),
        pg.K_LEFT:(-5, 0),
        pg.K_RIGHT:(+5, 0)}
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    
    # 練習問題 3
    """
    引数：こうかとんRect、または、爆弾Rect
    戻り地：真理値タプル（横判定結果、縦判定結果）
    画面内ならTrue、画面外ならFalse
    """
    yoko, tate = True, True
    
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
        
    return yoko, tate
        
def GameOver(scr: pg.Surface) -> None:
    
    # 演習１
    """
    引数：screen
    戻り地：None
    画面内ならTrue、画面外ならFalse
    """
    
    kk_cry = pg.image.load("fig/8.png") 
    go_rct = pg.Surface((WIDTH, HEIGHT))
    pg.draw.rect(go_rct, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("Game Over", True, (255, 255, 255))
    go_rct.set_alpha(215)
    scr.blit(go_rct, [0, 0])
    scr.blit(kk_cry, [(WIDTH / 3) - 30, HEIGHT / 2.2])
    scr.blit(kk_cry, [(WIDTH * 2 / 3) + 30, HEIGHT / 2.2])
    scr.blit(txt, [WIDTH * 1.15 / 3, HEIGHT / 2.1])
    pg.display.update()
    time.sleep(5)
    print("GameOver")
    
def ZoomAccs() -> tuple[list, list]:
    
    # 演習２
    """
    引数：None
    戻り地：listのtuple
    演習２
    時間とともに爆弾が拡大，加速する
    """
    
    accs = [a for a in range(1, 11)]
    imgs = []
    
    for r in range(1, 11):
        bb_img = pg.Surface((20 * r, 20 * r))
        pg.draw.circle(bb_img,(255, 0, 0), (10 * r, 10 * r), 10 * r)
        imgs.append(bb_img)
        
    return (accs, imgs)
    
def main():
    
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")   
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img = pg.Surface((20, 20))
    bb_accs, bb_imgs=ZoomAccs()  # 演習2:関数呼び出し
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10) # 練習問題2
    bb_rct = bb_img.get_rect()
    bb_rct.centery = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        screen.blit(bg_img, [0, 0]) 
        
        if kk_rct.colliderect(bb_rct):
            # GameOverの実装
            GameOver(screen)
            return 
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        
        for key,value in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += value[0]
                sum_mv[1] += value[1]
                
        bb_img=bb_imgs[min(tmr // 500, 9)]
        bb_img.set_colorkey((0, 0, 0))
        kk_rct.move_ip(sum_mv)
        avx = vx * bb_accs[min(tmr // 500, 9)] # 演習２
        avy = vy * bb_accs[min(tmr // 500, 9)]
        
        if check_bound(kk_rct) != (True, True): # 練習問題4
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
            
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(avx, avy)
        yoko, tate = check_bound(bb_rct)
        
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
            
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    
    pg.init()
    main()
    pg.quit()
    sys.exit()
    