#! /usr/bin/python3

from tkinter import *

#---------------------------------參數設定---------------------------------
畫布寬度 = 400
畫布高度 = 500
背景顏色 = "white"
聖誕樹尺寸 = 40
層數 = 3
遞進值 = 10
#--------------------------------------------------------------------------

#---------------------------------定義函數---------------------------------
def 畫聖誕樹(畫布,尺寸, 遞進值, 層數):
    現在的位置 = {'橫軸': 畫布寬度/2, '縱軸': 畫布高度}
    現在的位置['縱軸'] -= (尺寸)
    畫樹幹(畫布, 現在的位置, 尺寸, "black")

    for i in range(層數,0,-1):
        現在的位置['縱軸'] -= (尺寸 + i*遞進值)
        畫三角形(畫布, 現在的位置, 尺寸 + i*遞進值, "green")
        現在的位置['縱軸'] += (尺寸 + i*遞進值) * 0.4

def 畫三角形(畫布, 現在的位置, 三角形腰長, 顏色):
    頂點 = [0,0,-三角形腰長,三角形腰長,三角形腰長,三角形腰長,0,0]
    for i in range(4):
        頂點[i*2] += 現在的位置['橫軸']
        頂點[i*2+1] += 現在的位置['縱軸']

    畫布.create_polygon(頂點, fill = 顏色)

def 畫樹幹(畫布, 現在的位置, 尺寸, 顏色):
    寬度 = 尺寸 * 0.3
    長度 = 尺寸

    頂點 = [-寬度, 0, 寬度, 長度]
    for i in range(2):
        頂點[i*2] += 現在的位置['橫軸']
        頂點[i*2+1] += 現在的位置['縱軸']

    畫布.create_rectangle(頂點, fill = 顏色)

def 增加層數():
    畫布.delete(ALL)
    global 層數
    層數 += 1 if 層數 < 8 else 0
    畫聖誕樹(畫布, 聖誕樹尺寸, 遞進值, 層數)

def 減少層數():
    畫布.delete(ALL)
    global 層數
    層數 -= 1 if 層數 > 0 else 0
    畫聖誕樹(畫布, 聖誕樹尺寸, 遞進值, 層數)

#--------------------------------------------------------------------------

#---------------------------------程式主體---------------------------------
視窗 = Tk()
視窗.title("聖誕快樂")

按鈕_減 = Button(視窗, text="-", command=減少層數)
按鈕_加 = Button(視窗, text="+", command=增加層數)

按鈕_減.pack(side = 'left')
按鈕_加.pack(side = 'left')

畫布 = Canvas(視窗, width = 畫布寬度, height = 畫布高度, bg = 背景顏色)

畫聖誕樹(畫布, 聖誕樹尺寸, 遞進值, 層數)
畫布.pack(side = 'left')

視窗.mainloop()
#--------------------------------------------------------------------------
