# 커스텀 알람 제작 등 모든 알람을 타이머 지정으로 사용자를 깨우는 프로그램

# <기본 설정>
# 일어나는 시간, 타이머 설정
#  원하는 알람 타입 선택 (귀가 밝아요. / 귀가 어두워요)
#  알람 볼륨 설정 (5 단위 / 0 ~ 100%)
#  반복 횟수 설정 (최대 10번)

# <커스텀 설정>
#   일어나는 시간, 타이머 설정
#  원하는 알람 음악 설정 (url 달기)
#  알람 볼륨 설정 (5단위 / 0 ~ 100%)
#  반복 횟수 설정 (최대 10번)

# 시나리오
#  프로그램을 사용하여 알람 메뉴를 보여준다.
#  메뉴에서 기본 설정, 커스텀 설정 둘 중 하나를 선택한다.
#  일어나는 시간, 타이머 둘 중 하나 골라 선택한다.
#  원하는 알람 타입을 선택하거나 음악 url을 넣어서 설정한다.
#  알람 볼륨을 선택한다.
#  반복 횟수 설정하기
#  알람 설정한 것이 이게 맞는지 확인하는 창 띄우기
#  확인 / 다시하기 선택하기
#  마지막으로 알람 듣고 일어나면 됨!

from tkinter import *
from tkinter import filedialog
import tkinter.font
from tokenize import group
from turtle import bgcolor, width


root = Tk()
root.geometry("800x600")
root.resizable(False, False)

root.title("peo-ddeug")  # 창 제목


def click():
    root.destroy()
    import normal

def click1():
    root.destroy()
    import custom

title_font = tkinter.font.Font(family="함초롬바탕")
btn_font = tkinter.font.Font(family="함초롬바탕", size=10)

title = tkinter.Label(root, text='퍼뜩퍼뜩', font=title_font)
title.place(x=100, y=0)

btn_width, btn_height = 10, 3

frame = tkinter.Frame(root, bg='#80c1ff', bd=5)

btnN = tkinter.Button(root, text='기본 알람', font=btn_font,
                      width=btn_width, height=btn_height)
btnN.grid(row=0, column=0)

btnC = tkinter.Button(root, text='커스텀 알람', font=btn_font,
                      width=btn_width, height=btn_height)
btnC.grid(row=0, column=1)

btnN.place(x=300, y=200)
btnC.place(x=400, y=200)

btnN.config(command=click)
btnC.config(command=click1)

# frame.pack()

root.mainloop()