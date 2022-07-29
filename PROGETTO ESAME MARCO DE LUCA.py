#progetto per analisi bitcoin e correlazioni di Marco De Luca

'''


       .                .                    
       :"-.          .-";                    
       |:`.`.__..__.'.';|                    
       || :-"      "-; ||                    
       :;              :;                    
       /  .==.    .==.  \                    
      :      _.--._      ;                   
      ; .--.' `--' `.--. :                   
     :   __;`      ':__   ;                  
     ;  '  '-._:;_.-'  '  :                  
     '.       `--'       .'                  
      ."-._          _.-".                   
    .'     ""------""     `.                 
   /`-                    -'\                
  /`-                      -'\               
 :`-   .'              `.   -';              
 ;    /                  \    :              
:    :                    ;    ;             
;    ;                    :    :             
':_:.'                    '.;_;'             
   :_                      _;                
   ; "-._                -" :`-.     _.._    
   :_          ()          _;   "--::__. `.  
    \"-                  -"/`._           :  
   .-"-.                 -"-.  ""--..____.'  
  /         .__  __.         \               
 : / ,       / "" \       . \ ; bug          
  "-:___..--"      "--..___;-"

  
'''








'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DISCLAIMER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

#questo programma utilizza versioni gratuite di API a pagamento per i file json, di conseguenza il loro limite di utilizzo prevede:
# 
# cryptocompare : Limite massimo chiamate: 250000, al mese: 100000, al giorno: 50000, all'ora : 25000, al minuto: 2500, al secondo: 50
# 
# whales api: limite storico da  24h prima della chiamata fino a 4h prima della chiamata
# 
# cryptopanic: limite 1 al secondo per evitare congestione, per il resto l'api è gratuita 

import matplotlib.pyplot as plt
import mplcyberpunk
import requests
import matplotlib.animation as animation
import datetime as dt
import pygame
from pygame.locals import *
import matplotlib.backends.backend_agg as agg
import pygame.display
from pygame.locals import (K_DOWN, K_ESCAPE)
import time
import webbrowser
#blocco di codice per Matplotlib##################################################################################

#utilizzo di libreria estetica*****************************
plt.style.use('cyberpunk')
cybercolor = [33,41,70] #background
cybercolor_txtDomain = [234, 0, 217]


#dichiarazione matplot
fig, ax = plt.subplots()
#array per matplotlib
x = []
y = []

#################################################################################################################

def balene():
        def jbalene():
            tempo1 = '02:00:00'
            tempo2 = '04:00:00'
            formatoTempo = '%H:%M:%S'
            fromTime = dt.datetime.now()- dt.datetime.strptime(tempo2, formatoTempo)
            toTime = dt.datetime.now() - dt.datetime.strptime(tempo1, formatoTempo) #algoritmo per utilizzo della versione gratuita API (permette solo la visione di transazioni giornaliere in un tempo tra un giorno fa a un massimo di aggiornamento di 2 ore fa )
        
            todaydata = dt.datetime.today()
            todaystringa = todaydata.strftime('%Y-%m-%d')
            
            webbrowser.open('https://api.whaletrace.com/v1/HistoricTransactions?apiKey=ckxowl9h400b90117wujsi4a9&type=BTC&from='+str(todaystringa) + 'T' + str(fromTime)[12:-7] + 'Z' + '&to='+ str(todaystringa) + 'T' + str(toTime)[12:-7] + 'Z')
            r = requests.get('https://api.whaletrace.com/v1/HistoricTransactions?apiKey=ckxowl9h400b90117wujsi4a9&type=BTC&from='+str(todaystringa) + 'T' + str(fromTime)[12:-7] + 'Z' + '&to='+ str(todaystringa) + 'T' + str(toTime)[12:-7] + 'Z')
            
            Bjson = r.json()
            return Bjson
            


tempo1 = '02:00:00'
tempo2 = '04:00:00'
formatoTempo = '%H:%M:%S'
fromTime = dt.datetime.now()- dt.datetime.strptime(tempo2, formatoTempo)
toTime = dt.datetime.now() - dt.datetime.strptime(tempo1, formatoTempo) #algoritmo per utilizzo della versione gratuita API (permette solo la visione di transazioni giornaliere in un tempo tra un giorno fa a un massimo di aggiornamento di 2 ore fa )

todaydata = dt.datetime.today()
todaystringa = todaydata.strftime('%Y-%m-%d')

webbrowser.open('https://api.whaletrace.com/v1/HistoricTransactions?apiKey=ckxowl9h400b90117wujsi4a9&type=BTC&from='+str(todaystringa) + 'T' + str(fromTime)[12:-7] + 'Z' + '&to='+ str(todaystringa) + 'T' + str(toTime)[12:-7] + 'Z')
balene()
#funzione prezzo BTC, ETH, etc.       !!!SIMBOLO!!! (BTC per bitcoin, ETH per ethereum etc.)***************************
def cryptoprice(crypto, valuta):
    crypto = crypto.upper()
    valuta = valuta.upper()
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + crypto + "&tsyms=USD,JPY,EUR").json()
    print(r)
    return r[valuta]






# blocco caricamento assets


###################################################################################################################
#caricamento degli assets***************

def backgroundnews(x,y):
    imagenewsbackground = pygame.image.load(r'assets\backgroundimage.png')
    screen.blit(imagenewsbackground, (x,y))

def logobtc(x, y):
    btcico = pygame.image.load(r'assets\bitcoinico.png')
    btcico = pygame.transform.scale(btcico, (btcico.get_width()/4 , btcico.get_height()/4))
    screen.blit(btcico, (x, y))


def backgroundwhales(x, y):
    whalesbackground= pygame.image.load(r'assets\backgroundWhales.png')
    screen.blit(whalesbackground, (x, y))

def backgroundplt(x, y):
    pltbckg= pygame.image.load(r'assets\backgroundGrafico.png')    
    screen.blit(pltbckg, (x, y))

def whalesico(x, y):
    whale= pygame.image.load(r'assets\whale_icon.png')
    whale = pygame.transform.scale(whale , (whale.get_width()/6 , whale.get_height()/6)) 
    screen.blit(whale, (x, y))

def newsico(x, y):
    news= pygame.image.load(r'assets\news_icon.png')
    news = pygame.transform.scale(news , (news.get_width()/14 , news.get_height()/14)) 
    screen.blit(news, (x, y))


def infoico(x, y):
    info= pygame.image.load(r'assets\info_icon.png')
    info = pygame.transform.scale(info , (info.get_width()/9 , info.get_height()/9)) 
    screen.blit(info, (x, y))
    dimensioni = [info.get_width(), info.get_height()]
    return dimensioni #per il click

############################################################################################################################



#inizializzazione finestra*****************
screen = pygame.display.set_mode((1400, 900))
pygame.display.set_caption("MULTI- STRUMENTO DI ANALISI CRYPTO BY MARCO DE LUCA")
pygame.display.set_icon(pygame.image.load(r'assets\bitcoinico.png')) #asset logo btc
pygame.init()
screen.fill(cybercolor)
screen = pygame.display.get_surface()
pygame.display.flip()



#variabile y per la distanza delle notizie
j =  499

#distanza balene
k = 200

#Tutti gli assets*****************************

backgroundnews(-25, 500)
backgroundwhales(800, 180)
#il logo btc è stato messo nel ciclo di pygame per via del continuo aggiornamento del grafico
whalesico(1320, 150)
newsico(700, 460)
infoico(1050, 50)


#############################################################################################################################################################################################################################################################################
#INIZIO CICLO PYGAME COME FINESTRA DI INTERFACCIA GRAFICA*******************  (questo ciclo serve anche per il continuo aggiornamento delle funzioni di transazione e delle notizie)
show = True
while show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                show = False
        #click sul bottone delle info
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 1050 and my >= 50 and mx <= (1050 + infoico(1050, 50)[0]) and my <= (50+ infoico(1050, 50)[1]):
                webbrowser.open('https://academy.youngplatform.com/it/principiante/articoli/tutti', new = 2) #link ad una piattaforma per apprendimento del mondo crypto
                 
        
        #funzione animazione grafico******************
    def animate(i, x:list, y:list):   
        x.append(dt.datetime.now().strftime('%H:%M:%S')) 
        y.append(cryptoprice('BTC','EUR'))
        x = x[-20:]  #taglio tempo trascorso per evitare congestionamento del grafico in tempo reale
        y = y[-20:] #taglio dell'oscillazione del prezzo per medesimo motivo
        ax.clear()
        ax.plot(x, y , marker = '')
        plt.xticks(rotation=45, ha='right') 
        plt.subplots_adjust(bottom=0.20)
        ax.set_title('REAL TIME BITCOIN CHART')
        ax.set_xlabel('Time last')
        ax.set_ylabel('BTC VALUE')
        mplcyberpunk.add_underglow() #applicazione libreria estetica
        mplcyberpunk.add_glow_effects()


    anim = animation.FuncAnimation(fig, animate, fargs=(x,y), frames=200, interval=1000)    


#aggiunta animazione grafico all'interfaccia grafica di Pygame    
    fig.canvas.draw()
    sequenza_animazione_plt = agg.FigureCanvasAgg(fig)
    sequenza_animazione_plt.draw()
    rendering_sequenza = sequenza_animazione_plt.get_renderer() #rendering (trasformazione in codice rgb del grafico)
    trasformazione_in_codice_colore = rendering_sequenza.tostring_rgb()

    screen = pygame.display.get_surface()
    size = sequenza_animazione_plt.get_width_height()

    pygame.display.flip()
    surf = pygame.image.fromstring(trasformazione_in_codice_colore, size, "RGB")
    screen.blit(surf, (0,0))

#asset messo qui a causa dell'aggiornamento del grafico    
    backgroundplt(1,0)
    logobtc(550, -10)

# aggiornamento continuo cryptonews e sua dichiarazione****************

    def cryptonews(crypto):
        crypto = crypto.upper()
        data = requests.get('https://cryptopanic.com/api/v1/posts/?auth_token=7311e463ebb16b2bcc258b280bb0b232023e26cd&kind=news&currencies='+ crypto).json()
        return data

    
#font delle notizie***************
    newsfont = pygame.font.SysFont('samsungoneuilightcondensedv11ttf', 15)
    domainfont = pygame.font.SysFont('samsungoneuilightcondensedv11ttf', 15)


#array e ordinamento del json delle notizie*******************
    testonotizia = []
    titolopubblicatore = [] #array per il collezionamento di notizie e titoli diversi per differenziare il colore

    for i in cryptonews('BTC')["results"]:
        sources = i['source']
        titolopubblicatore.append(sources['domain']+ ' ')
        testonotizia.append(': '+ i['title'][:90] + ' ' + i['published_at'][11:]) 
    
    timedata = 'LAST NEWS PUBLISHED AT ' + i['published_at'] #ultimo aggiornamento delle notizie

    txttimedataimg = newsfont.render(timedata, True, 'GRAY')
    screen.blit(txttimedataimg, (100, 480))

    for i in range(len(testonotizia)-1): #rendering finale notizie e titoli
        txtdomainimg = domainfont.render(titolopubblicatore[i], True, 'GRAY') #colore grigio per i titoli
        txtnewsimg = newsfont.render(testonotizia[i], True, 'WHITE')  #colore bianco per le notizie
        screen.blit(txtdomainimg, (20,j))
        screen.blit(txtnewsimg, (txtdomainimg.get_width()+20, j))
        j +=20
    

    #BALENE!!!!****************** 

    def balene():
        def jbalene():
            tempo1 = '02:00:00'
            tempo2 = '04:00:00'
            formatoTempo = '%H:%M:%S'
            fromTime = dt.datetime.now()- dt.datetime.strptime(tempo2, formatoTempo)
            toTime = dt.datetime.now() - dt.datetime.strptime(tempo1, formatoTempo) #algoritmo per utilizzo della versione gratuita API (permette solo la visione di transazioni giornaliere in un tempo tra un giorno fa a un massimo di aggiornamento di 2 ore fa )
        
            todaydata = dt.datetime.today()
            todaystringa = todaydata.strftime('%Y-%m-%d')
            r = requests.get('https://api.whaletrace.com/v1/HistoricTransactions?apiKey=ckyoq52f400ip0117ewdlhea1&type=BTC&from='+str(todaystringa) + 'T' + str(fromTime)[12:-7] + 'Z' + '&to='+ str(todaystringa) + 'T' + str(toTime)[12:-7] + 'Z')
            print(r)
            Bjson = r.json()
            return Bjson
        
        arrayTransactions = [] #array finale per il collezionamento delle stringhe per la loro renderizzazione
        for i in jbalene()['data']: 

                froms= i['from']
                fromsource = froms['name']

                fromtype = froms['type']

                tos = i['to']
                tosource = tos['name']

                totype = tos['type']
                
                time = i['time']

                size = i['size']

                arrayTransactions.append('from ' + fromsource + ' ('+ fromtype + ')' + ' to ' + tosource + ' (' + totype + ')' + ' at ' + time + ' of '+ str(size) + ' BTC')
            
        return arrayTransactions




    for i in balene():
        testotransactions = newsfont.render(i, True, 'WHITE')
        screen.blit(testotransactions, (830, k))
        
        k += 20
    
 
    pygame.display.update()
    time.sleep(1) #per limite API gratuita delle notizie (MAX 1 al secondo)

##############################################################################################################################################################################################################################################################################

