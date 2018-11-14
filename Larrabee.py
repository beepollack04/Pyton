import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
name = pg.prompt (" what's ur name? ")
if name == "Larrabee":
    pg. alert ("<3")
    points += 55
    wb.open ("https://www.youtube.com/watch?v=kh6c0SOfkH4")
    t.sleep (5.5)
elif name == "Stewart":
    pg. alert (":(")
    points -= 9000000000000000000000000000000000000000000
    t.sleep (5.5)
elif name == "Susan":
    pg. alert ("ok.")
    points += 10
    wb.open ("https://www.youtube.com/watch?v=xWILHcsYVj8")
    t.sleep (5.5)
elif name== "Bob":
    pg. alert ("coolio")
    points += 15
    wb.open ("https://www.youtube.com/watch?v=sFukyIIM1XI")
    t.sleep (5.5)
elif name == "DJ":
    pg. alert ("HI")
    points += 5
    t.sleep (5.5)
elif name == "Bernardo":
    pg. alert ("WHAT UP NARDO")
    points += 12
    t.sleep (5.5)
else:
    pg. alert ("CAN I BE UUUUU, like please ")
    points += 3
    wb.open ("https://www.youtube.com/watch?v=SB1I3sCnVwE")
    t.sleep (5.5)
    
show = pg.prompt (" What is your favorite tv show? ")
if show == "Peppa Pig" and name == "Stewart":
    pg. alert ("WOW RLY HAHA not")
    t.sleep (5.5)
elif show == "Hannah Montana":
    pg. alert ("LOL XD OMG")
    points +=16
    wb.open ("https://www.youtube.com/watch?v=2827bYhQVtM")
    t.sleep (5.5)
elif show == "Peppa Pig":
    pg. alert ("This is mama pig HOOONKKKionk")
    points +=28
    wb.open ("https://www.youtube.com/watch?v=DP1pQkm9Op0")
    t.sleep (5.5)
elif show== "Paw patrol":
    pg. alert ("WOOF")
    points += 19
    t.sleep (5.5)
elif show== "Max and Ruby":
    pg. alert ("Ruby and Max")
    points += 7
    wb.open ("https://www.youtube.com/watch?v=DP1pQkm9Op0")
    t.sleep (5.5)
elif show == "Friends":
    pg. alert ("We were on a B.R.E.A.K")
    points +=15
    wb.open ("https://www.youtube.com/watch?v=Niu9Zmrx0p8")
    t.sleep (5.5)
elif show == "Barbie Life in the Dream House":
    pg. alert ("RRRRRaquel")
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=Ct6BUPvE2sM")
else:
    pg. alert("Your a vegtable")
    points += 3
    wb.open ("https://www.youtube.com/watch?v=Y4m2ySvjx8U")
    t.sleep (5.5)
    
sport = pg.prompt ("What is your favorite sport?")
if sport == "Zorbing":
    pg. alert ("Lets zorbe down a hilllll!!, " + name)
    points += 10000000000000
    wb.open ("https://www.youtube.com/watch?v=-ljbOmNX7x0")
    t.sleep (5.5)
elif sport == "Lax":
    pg. alert ("YOU WOULD")
    points -= 10
    wb.open ("https://www.youtube.com/watch?v=oAz4eKZsKqY")
    t.sleep (5.5)
elif sport== "Field Hockey":
    pg. alert ("pff, stop.")
    points -= 15 
    wb.open ("https://www.youtube.com/watch?v=IJNR2EpS0jw")
    t.sleep (5.5)
elif sport == "Hockey":
    pg. alert ("eww")
    points +=4
    wb.open ("https://www.youtube.com/watch?v=Zrki-dD3WLY")
    t.sleep (5.5)
elif sport == "curling":
    pg. alert ("Nice")
    points += 5
    t.sleep (5.5)
elif sport == "soccer":
    pg. alert ("cool")
    points +=8
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=SVctZi_V1Qs")
else:
    pg. alert("ur cool. NOT!")
    points += 18
    wb.open ("https://www.youtube.com/watch?v=IJNR2EpS0jw")
    t.sleep (5.5)
food = pg.prompt ("What is your favorite food?")
if food == "paste":
    pg. alert ("YUM")
    points +=7
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=wwFTVjN6j8U")
elif food == "fruit": 
    pg. alert ("Heathly bunch")
    wb.open ("https://www.youtube.com/watch?v=yBAXPA2ZSfM")
    points -=5
    t.sleep (5.5)
elif food == "Ice cream":
    pg. alert ("THE BEST")
    wb.open ("https://www.youtube.com/watch?v=o5-MkuEnDoA")
    points =+ 1100
    t.sleep (5.5)
elif food == "Candy":
    pg. alert ("mmmmmmm yummmmmm")
    points += 18
    t.sleep (5.5)
elif food == "Steak":
    pg. alert ("YUMMMY")
    points += 19
    t.sleep (5.5)
elif food == "Sushi":
    pg. alert ("SUSHI")
    points += 19
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=AoktpjjCLdM")
else :
    pg. alert ("decent")
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=astISOttCQ0")
    
color = pg.prompt ("What is your favorite color?")
if color == "red":
    pg.alert ("BLOOD")
    points += 5
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=n8RGxBOwCTM")
elif color == "orange":
    pg.alert ("Orange")
    points -=10
    t.sleep (5.5)
elif color == "yellow":
    pg.alert ("ur my sunshine")
    points +=10
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=dh7LJDHFaqA")
elif color == "greeen":
    pg.alert ("ur a monster")
    points += 12
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=AxcM3nCsglA")
elif color == "blue":
    pg.alert ("blueberries")
    points +=4
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=tSC4MhXXIDs")
elif color == "purple":
    pg.alert ("jelly fish")
    points +=19
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=9z8ujpPgUjI")
elif color == "pink":
    pg.alert ("Barbie")
    points += 10
    t.sleep (5.5)
    wb.open ("https://www.youtube.com/watch?v=gsyha_CeetM")
else:
    pg. alert ("COOOOLLLLL")
    points +=1
    wb.open ("https://www.youtube.com/watch?v=jofNR_WkoCE")

pg. alert ("You scored, ur cool NOT: " +  str(points))



    
