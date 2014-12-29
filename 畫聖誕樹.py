#! /usr/bin/python3

from tkinter import *
from random import randint
#---------------------------------參數設定---------------------------------
#畫布設定
畫布寬度 = 400
畫布高度 = 500

#顏色設定
背景顏色 = "black"
樹幹顏色 = "gray"
樹葉顏色 = "green"

#聖誕樹設定
聖誕樹尺寸 = 40
層數 = 3
遞進值 = 10

#下雪設定
數量 = 100
顆粒大小 = {'min': 12, 'max': 22} #顆粒大小 = (12,22)
偏移量 = {'x': 1, 'y': 1.25} #偏移量 = (2, 5)
#--------------------------------------------------------------------------

#---------------------------------定義函數---------------------------------
def 畫聖誕樹(畫布,尺寸, 遞進值, 層數):
    現在的位置 = {'x': 畫布寬度/2, 'y': 畫布高度}
    現在的位置['y'] -= (尺寸)
    畫樹幹(畫布, 現在的位置, 尺寸, 樹幹顏色)

    for i in range(層數,0,-1):
        現在的位置['y'] -= (尺寸 + i*遞進值)
        畫三角形(畫布, 現在的位置, 尺寸 + i*遞進值, 樹葉顏色)
        現在的位置['y'] += (尺寸 + i*遞進值) * 0.4

def 畫三角形(畫布, 現在的位置, 三角形腰長, 顏色):
    頂點 = [0,0,-三角形腰長,三角形腰長,三角形腰長,三角形腰長,0,0]
    for i in range(4):
        頂點[i*2] += 現在的位置['x']
        頂點[i*2+1] += 現在的位置['y']

    畫布.create_polygon(頂點, fill = 顏色)

def 畫樹幹(畫布, 現在的位置, 尺寸, 顏色):
    寬度 = 尺寸 * 0.3
    長度 = 尺寸

    頂點 = [-寬度, 0, 寬度, 長度]
    for i in range(2):
        頂點[i*2] += 現在的位置['x']
        頂點[i*2+1] += 現在的位置['y']

    畫布.create_rectangle(頂點, fill = 顏色, outline=顏色)

def 增加層數():
    層數_ = 層數+1 if 層數 < 8 else 層數
    層數輸入.delete(0, END)
    層數輸入.insert(0, 層數_)

def 減少層數():
    層數_ = 層數-1 if 層數 > 0 else 0
    層數輸入.delete(0, END)
    層數輸入.insert(0, 層數_)

def 畫雪_前景(分類基準):
    for i in 雪:
        雪座標 = i[1], i[0], i[1]+i[2], i[0]+i[2]
        if i[2] > 分類基準:
            畫布.create_oval(雪座標, fill = "#bbffff", outline = "")

def 畫雪_背景(分類基準):
    for i in 雪:
        雪座標 = i[1], i[0], i[1]+i[2], i[0]+i[2]
        if i[2] <= 分類基準:
            畫布.create_oval(雪座標, fill = "#ACFAFF", outline = "")

def 造雪(數量):
    雪 = []
    for i in range(數量):
        #一顆雪的屬性(y, x, r)
        雪.append((randint(0, 畫布高度), randint(0, 畫布寬度), randint(顆粒大小['min'], 顆粒大小['max'])))
    return 雪

def 更改降雪量():
    try:
        global 數量
        數量 = int(降雪量輸入.get())
        global 雪
        雪 = 造雪(數量)
    except:
        降雪量輸入.delete(0, END)
        降雪量輸入.insert(0, 數量)

#--------------------------------------------------------------------------

#---------------------------------程式主體---------------------------------
視窗 = Tk()
視窗.title("聖誕快樂")

#層數設定
層數文字 = Label(視窗, text="層數", font=(20))
層數輸入 = Entry(視窗)
層數輸入.delete(0, END)
層數輸入.insert(0, 層數)
按鈕_減 = Button(視窗, text="-", command=減少層數, font=(30), width=3)
按鈕_加 = Button(視窗, text="+", command=增加層數, font=(30), width=3)

#降雪量設定
降雪量文字 = Label(視窗, text="降雪量", font=(20))
降雪量輸入 = Entry(視窗)
降雪量輸入.delete(0, END)
降雪量輸入.insert(0, 數量)
按鈕_降雪量 = Button(視窗, text="更改", command=更改降雪量, font=(30), width=3)
#視窗.bind('<Return>', 更改降雪量)

畫布 = Canvas(視窗, width = 畫布寬度, height = 畫布高度, bg = 背景顏色)

雪 = 造雪(數量)

def 畫面更新():
    畫布.delete(ALL)

    global 層數
    try:
        層數 = int(層數輸入.get())
    except:
        pass

    global 雪
    雪 = [((y+偏移量['y']*r/顆粒大小['max'])%畫布高度, ((x+偏移量['x']*r/顆粒大小['max']))%畫布寬度, r) for (y, x, r) in 雪]

    分類基準 = (顆粒大小['min']+顆粒大小['max'])/2
    畫雪_背景(分類基準)
    畫聖誕樹(畫布, 聖誕樹尺寸, 遞進值, 層數)
    畫雪_前景(分類基準)

    視窗.after(10, 畫面更新)

畫面更新()

層數文字.grid(row = 0,column = 0, columnspan = 2)
層數輸入.grid(row = 1,column = 0, columnspan = 2)
按鈕_減.grid(row = 2,column = 0)
按鈕_加.grid(row = 2,column = 1)
降雪量文字.grid(row = 3,column = 0, columnspan = 2)
降雪量輸入.grid(row = 4,column = 0, columnspan = 2)
按鈕_降雪量.grid(row = 5,column = 0, columnspan = 2)
畫布.grid(row = 0, column = 2,rowspan=40)


視窗.mainloop()
#--------------------------------------------------------------------------
