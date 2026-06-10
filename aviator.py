import pygame as pg
from sys import exit
import random as r
import math as m
import os, sys

def resource_path(rel_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)

          
pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((1000,500))
pg.display.set_caption("AVIATOR")

repulo_icon = pg.image.load(resource_path('repulo_ikon.png')).convert_alpha()
pg.display.set_icon(repulo_icon)

repulo = pg.transform.rotozoom(pg.image.load(resource_path('repulo.png')).convert_alpha(), 0, 1/4)
fel = True

szoveg = pg.font.Font(None, 40)
szoveg2 = pg.font.Font(None, 48)

hatter = pg.image.load(resource_path('hatter_0.png'))
hatter_kezdet = 0


def megadas(x, y, also, felso):

    karakterek = ['0','1','2','3','4','5','6','7','8','9','.']
    x = ""

    screen.blit(hatter,(0,0))

    nincshiba = True

    while True:

            screen.blit(hatter,(0,0))
            fvszoveg = szoveg.render(f'{x}', False, 'Black')
            fvszoveg_r = fvszoveg.get_rect(center = (500-len(x),275))
            balhatter_r = balszoveg_r.inflate(20,10)
            pg.draw.rect(screen,'White', balhatter_r)
            pg.draw.rect(screen,'Black', balhatter_r,2)
            screen.blit(balszoveg, balszoveg_r)
            screen.blit(fvszoveg,fvszoveg_r)
            
            kezdoszoveg = szoveg.render(f'Enter your {y}! ({also}-{felso})', False, 'Black')
            kezdoszoveg_r = kezdoszoveg.get_rect(center = (500,220))
            screen.blit(kezdoszoveg, kezdoszoveg_r)

            if nincshiba:
                    hibauzenet = szoveg.render('', False, 'Black')
                    hibauzenet_r = hibauzenet.get_rect(center = (500, 360))
                    for event in pg.event.get():
                            if event.type == pg.QUIT:
                                    pg.quit()
                                    exit()

                            if event.type == pg.KEYDOWN:
                                    try:
                                            if chr(event.key) in karakterek:
                                                    if len(x) < 7:
                                                            x += chr(event.key)
                                                            fvszoveg = szoveg.render(f'{x}', False, 'Black')
                                                            screen.blit(fvszoveg, fvszoveg_r)
                                                    else:
                                                            x = x
                                    except ValueError:
                                            x = x
                                            continue

                                    if event.key == pg.K_BACKSPACE:
                                            x = x[:-1]

                                    if event.key == pg.K_RETURN:
                                            try:
                                                    x = float(x)
                                            except ValueError:
                                                    nincshiba = False
                                                    screen.blit(hibauzenet, hibauzenet_r)
                                                    x = ""
                                                    continue

                                            if x <  float(also.replace(',', '')) or x > float(felso.replace(',', '')):
                                                    nincshiba = False
                                                    screen.blit(hibauzenet, hibauzenet_r)
                                                    x = ""
                                            else:
                                                    return x
                                            
                                    screen.blit(hibauzenet, hibauzenet_r)
                    
            else:
                    hibauzenet = szoveg.render(f'Invalid {y}! (Press Enter)', False, 'Black')
                    hibauzenet_r = hibauzenet.get_rect(center = (500, 360))
                    screen.blit(hibauzenet, hibauzenet_r)
                    screen.blit(fvszoveg, fvszoveg_r)

                    for event in pg.event.get():
                            if event.type == pg.QUIT:
                                    pg.quit()
                                    exit()

                            if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_RETURN:
                                            screen.blit(hatter,(0,0))
                                            nincshiba = True

            pg.display.update()


def randomf():
        random = r.randint(1,1002)

        if random < 80:
                return r.randint(0,10)
        elif random >= 80 and random < 300:
                return r.randint(0,50)
        elif random >= 300 and random < 600:
                return r.randint(50,100)
        elif random >= 600 and random < 790:
                return r.randint(100,200)
        elif random >= 790 and random < 900:
                return r.randint(200,500)
        elif random >= 900 and random < 920:
                return r.randint(500,900)
        elif random >= 920 and random < 960:
                return r.randint(900,1900)
        elif random >= 960 and random < 980:
                return r.randint(1900,4900)
        elif random >= 980 and random < 995:
                return r.randint(4900,9900)
        elif random >= 995 and random < 997:
                return r.randint(9900,49900)
        elif random >= 997 and random < 999:
                return r.randint(49900,99900)
        elif random == 999:
                return r.randint(99900,499900)
        elif random == 1000:
                return r.randint(499900,999900)
        else:
                return r.randint(999900,9999900)


balszoveg = szoveg.render(f'Bal: 0', False, 'Black')
balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))

try:
    with open("egyenleg.txt", "r") as fajl:
        egyenleg = float(fajl.read())

except FileNotFoundError:
    egyenleg = megadas("egyenleg", "balance", "50", "1,000,000")
    
    with open("elozmenyek.txt", "a", encoding="utf-8") as fajl:
        fajl.write(f"\nÚj feltöltés: {egyenleg:.2f} Ft\n")

allapot = "tipp"
tipp = 0

balszoveg = szoveg.render(f'Bal: {egyenleg:.2f}', False, 'Black')
balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))
uj = szoveg.render('Next Round', False, "Black")
uj2 = szoveg.render('Deposit', False, "Black")
jatekvegeszoveg = szoveg.render('You dont have enough money to play.', False, 'Black')
jatekvegeszoveg_r = jatekvegeszoveg.get_rect(center = (500,250))


while True:
        
        idokulonbseg = clock.tick(60) / 1000.0

        for event in pg.event.get():
                if event.type == pg.QUIT:
                        pg.quit()
                        exit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                        if uj_r.collidepoint(event.pos):
                                allapot = "tipp"

                if event.type == pg.MOUSEBUTTONDOWN:
                        if uj2_r.collidepoint(event.pos):
                                egyenleg = megadas("egyenleg", "balance", "50", "1,000,000")
                                with open("elozmenyek.txt", "a", encoding="utf-8") as fajl:
                                    fajl.write(f"\nÚj feltöltés: {egyenleg:.2f} Ft\n")
                                allapot = "tipp"

        balszoveg = szoveg.render(f'Bal: {egyenleg:.2f}', False, 'Black')
        balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))
        balhatter_r = balszoveg_r.inflate(20,10)
        pg.draw.rect(screen,'White', balhatter_r)
        pg.draw.rect(screen,'Black', balhatter_r,2)
        screen.blit(balszoveg, balszoveg_r)

        if allapot == "tipp":

                uj_r = uj.get_rect(center = (5000, 5000))
                uj2_r = uj2.get_rect(center = (5000, 5000))

                osszeg = megadas("osszeg", "bet amount", "50", f"{egyenleg:.2f}")
                tipp = megadas("tipp", "guess", "1", "100,000")
                random2 = randomf()

                szorzo = random2/100+1

                gyorsulas = 0.0045
                akt_odds = 1.0

                repulo_r = repulo.get_rect(midbottom = (500,400))

                allapot = "jatek"

        screen.blit(hatter,(hatter_kezdet,0))
        hatter_kezdet -= 15
        if hatter_kezdet < -1000: 
                hatter_kezdet = 0

        if allapot == "jatek":

                if akt_odds < szorzo:
                        if fel:
                                repulo_r.y -= 2
                                if repulo_r.top < 100:
                                        fel = False
                        else:
                                repulo_r.y += 2
                                if repulo_r.bottom > 400:
                                        fel = True
                        if akt_odds <= tipp:
                                odds = szoveg.render(f'{akt_odds:.2f}x' , False, 'Black')
                                odds_r = odds.get_rect(center = (500,450))
                                oddshatter_r = odds_r.inflate(20,10)
                                pg.draw.rect(screen,'Pink', oddshatter_r)
                                pg.draw.rect(screen,'Black', oddshatter_r,2)
                        else:
                                odds = szoveg.render(f'{akt_odds:.2f}x' , False, 'Black')
                                odds_r = odds.get_rect(center = (500,450))
                                oddshatter_r = odds_r.inflate(20,10)
                                pg.draw.rect(screen,'Green', oddshatter_r)
                                pg.draw.rect(screen,'Black', oddshatter_r,2)

                        screen.blit(odds,odds_r)
                        screen.blit(repulo, repulo_r)

                        akt_odds *= (1 + gyorsulas * idokulonbseg)

                        if akt_odds > 1.00:
                                gyorsulas = 0.08
                        if akt_odds > 1.01:
                                gyorsulas = 0.15

                else:
                        eredeti_osszeg = osszeg
                        eredeti_mentve = False
                        allapot = "korvege"

        if allapot == "korvege":

                if tipp < akt_odds:
                        nyertel_e = szoveg.render('You won!', False, 'Black')
                        egyenleg += tipp*osszeg-osszeg
                        osszeg = 0
                else:
                        nyertel_e = szoveg.render('You lost!', False, 'Black')
                        egyenleg -= osszeg
                        osszeg = 0
                
                repulo_r.y -= 8
                
                tipped = szoveg.render(f'Your guess was {tipp:.2f}x', False, "Black")
                balszoveg = szoveg.render(f'Bal: {egyenleg:.2f}', False, 'Black')
                vege_szoveg = szoveg.render(f'The game ended at {akt_odds:.2f}x',False,'Black')

                nyertel_e_r = nyertel_e.get_rect(center = (500,470))
                uj_r = uj.get_rect(bottomright = (980, 490))
                tipped_r = tipped.get_rect(center = (500, 380))
                vege_szoveg_r = vege_szoveg.get_rect(center = (500,430))
                
                screen.blit(vege_szoveg,vege_szoveg_r)
                screen.blit(nyertel_e, nyertel_e_r)
                ujhatter_r = uj_r.inflate(20,10)
                pg.draw.rect(screen,'White', ujhatter_r)
                pg.draw.rect(screen,'Black', ujhatter_r,2)
                screen.blit(uj,uj_r)
                screen.blit(tipped,tipped_r)
                screen.blit(repulo, repulo_r)
                if eredeti_mentve == False:
                    with open("elozmenyek.txt", "a", encoding="utf-8") as fajl:
                        fajl.write(
                            f"Fogadási összeg: {eredeti_osszeg:.2f} | "
                            f"Tipp: {tipp:.2f}x | "
                            f"Szorzó: {szorzo:.2f}x | "
                            f"Új egyenleg: {egyenleg:.2f}\n"
                        )

                    with open("egyenleg.txt", "w", encoding="utf-8") as fajl:
                        fajl.write(str(egyenleg))

                    eredeti_mentve = True

                if egyenleg < 50:
                        if os.path.exists("egyenleg.txt"):
                            os.remove("egyenleg.txt")
                        allapot = "jatekveg"
                
        if allapot == "jatekveg":
                
                uj2_r = uj2.get_rect(bottomright = (980, 490))

                screen.blit(hatter,(0,0))
                screen.blit(jatekvegeszoveg, jatekvegeszoveg_r)
                screen.blit(vege_szoveg,vege_szoveg_r)
                screen.blit(nyertel_e, nyertel_e_r)
                screen.blit(tipped,tipped_r)
                uj2hatter_r = uj2_r.inflate(20,10)
                pg.draw.rect(screen,'White', uj2hatter_r)
                pg.draw.rect(screen,'Black', uj2hatter_r,2)
                screen.blit(uj2,uj2_r)

        balszoveg = szoveg.render(f'Bal: {egyenleg:.2f}', False, 'Black')
        balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))
        balhatter_r = balszoveg_r.inflate(20,10)
        pg.draw.rect(screen,'White', balhatter_r)
        pg.draw.rect(screen,'Black', balhatter_r,2)
        screen.blit(balszoveg, balszoveg_r)
        

        pg.display.update()
        clock.tick(60)