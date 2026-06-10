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

def balancef():

        karakterek = ['0','1','2','3','4','5','6','7','8','9','.']
        balance = ""

        screen.blit(hatter,(0,0))

        nincshiba = True

        while True:

                screen.blit(hatter,(0,0))
                balanceszoveg = szoveg.render(balance, False, 'Black')
                balanceszoveg_r = balanceszoveg.get_rect(center = (500-len(balance),275))

                screen.blit(balanceszoveg,balanceszoveg_r)
                
                kezdoszoveg = szoveg.render('Enter your balance! (50-1,000,000)', False, 'Black')
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
                                                        if len(balance) < 9:
                                                                balance += chr(event.key)
                                                                balanceszoveg = szoveg.render(balance, False, 'Black')
                                                                screen.blit(balanceszoveg, balanceszoveg_r)
                                                        else:
                                                                balance = balance
                                        except ValueError:
                                                balance = balance
                                                continue

                                        if event.key == pg.K_BACKSPACE:
                                                balance = balance[:-1]

                                        if event.key == pg.K_RETURN:
                                                try:
                                                        balance = float(balance)
                                                except ValueError:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        balance = ""
                                                        continue

                                                if balance < 50 or balance > 1000000:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        balance = ""
                                                else:
                                                        return balance
                                                
                                        screen.blit(hibauzenet, hibauzenet_r)
                        
                else:
                        hibauzenet = szoveg.render('Invalid balance! (Press Enter)', False, 'Black')
                        hibauzenet_r = hibauzenet.get_rect(center = (500, 360))
                        screen.blit(hibauzenet, hibauzenet_r)
                        screen.blit(balanceszoveg, balanceszoveg_r)

                        for event in pg.event.get():
                                if event.type == pg.QUIT:
                                        pg.quit()
                                        exit()

                                if event.type == pg.KEYDOWN:
                                        if event.key == pg.K_RETURN:
                                                screen.blit(hatter,(0,0))
                                                nincshiba = True

                pg.display.update()

def betf():

        karakterek = ['0','1','2','3','4','5','6','7','8','9','.']
        bet = ""

        screen.blit(hatter,(0,0))
        nincshiba = True

        while True:

                screen.blit(hatter,(0,0))
                betszoveg = szoveg.render(bet, False, 'Black')
                betszoveg_r = betszoveg.get_rect(center = (500-len(bet),275))
                balhatter_r = balszoveg_r.inflate(20,10)
                pg.draw.rect(screen,'White', balhatter_r)
                pg.draw.rect(screen,'Black', balhatter_r,2)
                screen.blit(balszoveg, balszoveg_r)
                screen.blit(betszoveg,betszoveg_r)
                
                kezdoszoveg = szoveg.render('Enter your bet! (50-1,000,000)', False, 'Black')
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
                                                        if len(bet) < 9:
                                                                bet += chr(event.key)
                                                                betszoveg = szoveg.render(bet, False, 'Black')
                                                                screen.blit(betszoveg, betszoveg_r)
                                                        else:
                                                                bet = bet
                                        except ValueError:
                                                bet = bet
                                                continue

                                        if event.key == pg.K_BACKSPACE:
                                                bet = bet[:-1]

                                        if event.key == pg.K_RETURN:
                                                try:
                                                        bet = float(bet)
                                                except ValueError:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        bet = ""
                                                        continue

                                                if bet < 50 or bet > balance:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        bet = ""
                                                else:
                                                        return bet

                                        screen.blit(hibauzenet, hibauzenet_r)
                        
                else:
                        hibauzenet = szoveg.render('Invalid bet! (Press Enter)', False, 'Black')
                        hibauzenet_r = hibauzenet.get_rect(center = (500, 360))
                        screen.blit(hibauzenet, hibauzenet_r)
                        screen.blit(betszoveg, betszoveg_r)

                        for event in pg.event.get():
                                if event.type == pg.QUIT:
                                        pg.quit()
                                        exit()

                                if event.type == pg.KEYDOWN:
                                        if event.key == pg.K_RETURN:
                                                screen.blit(hatter,(0,0))
                                                screen.blit(balszoveg, balszoveg_r)
                                                nincshiba = True

                pg.display.update()

def tippf():

        karakterek = ['0','1','2','3','4','5','6','7','8','9','.']
        tipp = ""

        screen.blit(hatter,(0,0))
        nincshiba = True

        while True:

                screen.blit(hatter,(0,0))
                oddsszoveg = szoveg.render(tipp, False, 'Black')
                oddsszoveg_r = oddsszoveg.get_rect(center = (500-len(tipp),275))
                balhatter_r = balszoveg_r.inflate(20,10)
                pg.draw.rect(screen,'White', balhatter_r)
                pg.draw.rect(screen,'Black', balhatter_r,2)
                screen.blit(balszoveg, balszoveg_r)
                screen.blit(oddsszoveg,oddsszoveg_r)
                
                kezdoszoveg = szoveg.render('Enter an odds! (1-100,000)', False, 'Black')
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
                                                        if len(tipp) < 8:
                                                                tipp += chr(event.key)
                                                                oddsszoveg = szoveg.render(tipp, False, 'Black')
                                                                screen.blit(oddsszoveg, oddsszoveg_r)
                                                        else:
                                                                tipp = tipp
                                        except ValueError:
                                                tipp = tipp
                                                continue

                                        if event.key == pg.K_BACKSPACE:
                                                tipp = tipp[:-1]

                                        if event.key == pg.K_RETURN:
                                                try:
                                                        tipp = float(tipp)
                                                except ValueError:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        tipp = ""
                                                        continue

                                                if tipp < 0 or tipp > 100000:
                                                        nincshiba = False
                                                        screen.blit(hibauzenet, hibauzenet_r)
                                                        tipp = ""
                                                else:
                                                        return tipp
                                                
                                        screen.blit(hibauzenet, hibauzenet_r)
                        
                else:
                        hibauzenet = szoveg.render('Invalid odds! (Press Enter)', False, 'Black')
                        hibauzenet_r = hibauzenet.get_rect(center = (500, 360))
                        screen.blit(hibauzenet, hibauzenet_r)
                        screen.blit(oddsszoveg, oddsszoveg_r)

                        for event in pg.event.get():
                                if event.type == pg.QUIT:
                                        pg.quit()
                                        exit()

                                if event.type == pg.KEYDOWN:
                                        if event.key == pg.K_RETURN:
                                                screen.blit(hatter,(0,0))
                                                screen.blit(balszoveg, balszoveg_r)
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

balance = balancef()
allapot = "tipp"
tipp = 0

balszoveg = szoveg.render(f'Bal: {balance:.2f}', False, 'Black')
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
                                balance = balancef()
                                allapot = "tipp"

        balszoveg = szoveg.render(f'Bal: {balance:.2f}', False, 'Black')
        balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))
        balhatter_r = balszoveg_r.inflate(20,10)
        pg.draw.rect(screen,'White', balhatter_r)
        pg.draw.rect(screen,'Black', balhatter_r,2)
        screen.blit(balszoveg, balszoveg_r)

        if allapot == "tipp":

                uj_r = uj.get_rect(center = (5000, 5000))
                uj2_r = uj2.get_rect(center = (5000, 5000))

                bet = betf()
                tipp = tippf()
                random2 = randomf()

                gyorsulas = 0.0045
                akt_odds = 1.0

                repulo_r = repulo.get_rect(midbottom = (500,400))

                allapot = "jatek"

        screen.blit(hatter,(hatter_kezdet,0))
        hatter_kezdet -= 15
        if hatter_kezdet < -1000: 
                hatter_kezdet = 0

        if allapot == "jatek":

                if akt_odds < random2/100+1:
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
                        allapot = "korvege"

        if allapot == "korvege":

                if tipp < akt_odds:
                        nyertel_e = szoveg.render('You won!', False, 'Black')
                        balance += tipp*bet-bet
                        bet = 0
                else:
                        nyertel_e = szoveg.render('You lost!', False, 'Black')
                        balance -= bet
                        bet = 0
                
                repulo_r.y -= 8
                
                tipped = szoveg.render(f'Your guess was {tipp:.2f}x', False, "Black")
                balszoveg = szoveg.render(f'Bal: {balance:.2f}', False, 'Black')
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

                if balance < 50:
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

        balszoveg = szoveg.render(f'Bal: {balance:.2f}', False, 'Black')
        balszoveg_r = balszoveg.get_rect(bottomleft = (20, 490))
        balhatter_r = balszoveg_r.inflate(20,10)
        pg.draw.rect(screen,'White', balhatter_r)
        pg.draw.rect(screen,'Black', balhatter_r,2)
        screen.blit(balszoveg, balszoveg_r)
        

        pg.display.update()
        clock.tick(60)