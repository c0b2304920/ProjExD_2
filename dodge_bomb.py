import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DELTA={pg.K_UP:(0, -5),
        pg.K_DOWN:(0, +5),
        pg.K_LEFT:(-5, 0),
        pg.K_RIGHT:(+5, 0)}


def main():
    """
    brnbnrgnjjjjjjjjjjjjjjjjjnri
    """
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img=pg.Surface((20,20))
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_rct=bb_img.get_rect()
    bb_rct.centery=random.randint(0,WIDTH)
    bb_rct.centery=random.randint(0,HEIGHT)
    vx,vy=+5,+5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        for key,value in DELTA.items():
            if key_lst[key]:
                sum_mv[0]+=value[0]
                sum_mv[1]+=value[1]
        
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img,bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    