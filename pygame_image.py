import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習1
    kkimg = pg.image.load("ex01/fig/3.png")
    kkimg = pg.transform.flip(kkimg, True, False)
    kkimgs = [kkimg,pg.transform.rotozoom(kkimg, 10, 1.0)] #練習3 こうかとんsurfaceのリスト
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = (tmr%1600)
        screen.blit(bg_img, [-x, 0]) #練習4　背景画像を表示
        screen.blit(bg_img, [1600-x, 0])#練習6 こうかとん動く
        screen.blit(kkimgs[tmr%2],[300,200])#練習5 こうかとんはばたく
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()