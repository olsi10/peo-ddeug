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


import imp
from tabnanny import check
from tkinter import *
from tokenize import group
from turtle import bgcolor, width
from tkinter import filedialog
import tkinter.font
import time
import datetime
import playsound
import pygame

root = Tk()
root.resizable(False, False)
root.geometry("750x400-40+50")
root.title("peo-ddeug")  # 창 제목
root.configure(background='white')

backImg = tkinter.PhotoImage(file="img/original.png")
label = tkinter.Label(root, image=backImg)
label.pack()

root.title("peo-ddeug")  # 창 제목


# def flash():
#     checkbutton1.flash()


# alarmTypeCheck1 = tkinter.IntVar()
# loopCount = tkinter.IntVar()
# askPlayGame = tkinter.IntVar()


# checkbutton1 = tkinter.Checkbutton(
#     root, text="", variable=CheckVariety_1, activebackground="blue")
# checkbutton2 = tkinter.Checkbutton(
#     root, text="△", variable=CheckVariety_2)
# checkbutton3 = tkinter.Checkbutton(
#     root, text="X", variable=CheckVariety_2, command=flash)

# checkbutton1.place(x=260, y=200)

def timer(n):
    cntSec = int(sec.get()) * 60
    while (cntSec != 0):
        cntSec = cntSec-1
        time.sleep(1)
        print(cntSec)

    if cntSec == 0:
        playsound.playsound('soundfile/quite/JingleBells.mp3')


# 최근에 이 라이브러리(버전 1.3.0)를 설치해서 테스트해봤는데 오디오 파일 재생이 안 되면서 다음과 같은 에러가 발생했습니다.
# 그래서 playsound 버전을 1.2.2 로 낮췄더니 굿굿


inputTime = tkinter.Label(root, text="타이머 시간 입력 (초)", font="메이플스토리")

# root라는 창에 입력창 생성
sec = tkinter.Entry(root, width=20)
sec.config(fg="black")  # 입력창 배경, 글자색 설정
sec.place(x=560, y=140)
sec.bind("<Return>", timer)  # 엔터를 치면 결과라는 함수를 실행하라

root.mainloop()
