from inky import InkyWHAT
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from random import choice
from font_source_sans_pro import SourceSansProSemibold

thisDisplay = InkyWHAT('black')
img = Image.new("P", (thisDisplay.WIDTH, thisDisplay.HEIGHT))
draw = ImageDraw.Draw(img)
# Opening JSON file, load JSON to dictionary 
from json import load
fileName = 'favorites.json' 
f = open(fileName ,) 
data = load(f) 
f.close() 

# ================= blank screen to start =======================
draw.rectangle([(0,0),(thisDisplay.WIDTH, thisDisplay.HEIGHT)],fill=thisDisplay.BLACK)
draw.rectangle([(1,1),(thisDisplay.WIDTH-2, thisDisplay.HEIGHT-2)],fill=thisDisplay.WHITE)

midWidth = thisDisplay.WIDTH / 2   
midHeight = thisDisplay.HEIGHT / 2


if len(data)>1:
    theKanji = data.pop()
    msgKanji = theKanji['kanji']
    msgKana  = theKanji['kanaRead']
    msgEigo  = theKanji['engRead']
else:
    msgKanji = "花菜 凛生"
    msgKana  = "ハナ-リオ"
    msgEigo  = "Hannah - Leo"
    loop = False

theKanji = choice(data)
msgKanji = theKanji['kanji']
msgKana  = theKanji['kanaRead']
msgEigo  = theKanji['engRead']


msgTime  = "Updated: " + datetime.strftime(datetime.now(),'%I:%M %p')

# find the kanji for this day of the week
kanjiWeek = "月火水木金土日"
DoW = datetime.weekday(datetime.now()) # 0 = Monday 6 = Sunday
msgDoW = kanjiWeek[DoW]


# ================= decide font sizes for display =======================

fontKanji = 128  #good size for up to 4 kanji 
fontKana = 45  # up to 9 kana
fontEigo = 36 # up to char(20)

if len(msgKanji) > 3: fontKanji = 95
if len(msgKana) > 9: fontKanji = 35
if len(msgEigo) > 20:
    fontEigo = 24
    msgEigo = msgEigo[:40] # trim message to char(40)

# ================= load fonts =======================
fontKanji = ImageFont.truetype("migu-1m-regular.ttf",fontKanji) 
fontKana  = ImageFont.truetype("migu-1m-regular.ttf",fontKana) 
fontEigo  = ImageFont.truetype(SourceSansProSemibold, fontEigo)
fontTime  = ImageFont.truetype(SourceSansProSemibold,18)
fontDoW   = ImageFont.truetype("migu-1m-regular.ttf",30) 


# get text box size for each of our fields
wKanji, hKanji = fontKanji.getsize(msgKanji)
wKana,  hKana  = fontKana.getsize(msgKana)
wEigo,  hEigo  = fontEigo.getsize(msgEigo)
wTime,  hTime  = fontTime.getsize(msgTime)

#calculate screen locations for our msgX fields
locKanji = (midWidth - wKanji/2, 10  )     # Kanji centered 10 pixels from top
locKana  = (midWidth - wKana/2, 150 )     # Kana centered hanging form line 200
locEigo  = (midWidth - wEigo/2, 200 )     # Eigo centered hanging form line 250
locTime  = (thisDisplay.WIDTH - wTime -4 , thisDisplay.HEIGHT - hTime -4) # bottom left
locDoW   = (4,270)

draw.text(locKanji, msgKanji, thisDisplay.BLACK, fontKanji)
draw.text(locKana , msgKana , thisDisplay.BLACK, fontKana)
draw.text(locEigo , msgEigo , thisDisplay.BLACK, fontEigo)
draw.text(locTime , msgTime , thisDisplay.BLACK, fontTime)
draw.text(locDoW ,  msgDoW  , thisDisplay.BLACK, fontDoW)


#display(img)
#img = img.rotate(180, expand=True)
thisDisplay.set_image(img)
thisDisplay.show()
