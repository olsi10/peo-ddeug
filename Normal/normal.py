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
import tkinter.ttk
import tkinter.messagebox as msgbox
from tokenize import group
from turtle import bgcolor, width
from tkinter import filedialog
import tkinter.font
import time
import datetime
import playsound
import pygame
import random
import os
from multiprocessing import Process
import sys

# import sqlite3  # pip install pysqlite3

# conn = sqlite3.connect('data.sqlite', isolation_level=None)
# c = conn.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS users\
# (id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone TEXT, regist_date TEXT)")

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

# 메세지 요청 박스  만약 게임 플레이 여부가 false 라면 음악을 멈추겠냐는 확인 박스를 띄운다
def okcancel():
    msgbox.askquestion(title="예 / 아니요",
                       message="어서 잠에서 깨세요!! (확인을 누르면 기상 게임 화면으로 넘어갑니다.")

# 버튼 누르면 알람 설정에 따라


def btnpress():
    timer()

# 알람 타입 값 가져오기


def alarm():

    # https://stackoverflow.com/questions/60250171/how-to-play-random-mp3-files-in-pygame
    pathN = "E:/peo-ddeug/soundfile/NOISE"
    pathQ = "E:/peo-ddeug/soundfile/QUITE"
    pathD = "E:/peo-ddeug/soundfile/developerPICK"

    # 폴더의 모든 파일 목록을 가져오는 데 사용 / endswtich 문자열이 mp3로 끝나는지
    N_mp3 = [os.path.join(pathN, f)
             for f in os.listdir(pathN) if f.endswith('.mp3')]
    Q_mp3 = [os.path.join(pathQ, f)
             for f in os.listdir(pathQ) if f.endswith('.mp3')]
    D_mp3 = [os.path.join(pathD, f)
             for f in os.listdir(pathD) if f.endswith('.mp3')]

    type = alarmType.get()

    if type == "NOISE":
        randomMP3 = random.choice(N_mp3)
        # https://yunwoong.tistory.com/41
        print('고막을 때리는 곡 재생 ♬ ' + os.path.basename(randomMP3))
        playsound.playsound(randomMP3)
    elif type == "QUITE":
        randomMP3 = random.choice(Q_mp3)
        print('QUITE라고 조용할까? 개발자를 믿지 마라! 곡 재생 ~ ♬ ' +
              os.path.basename(randomMP3))
        playsound.playsound(randomMP3)
    elif type == "개발자 PICK":
        randomMP3 = random.choice(D_mp3)
        print('개발자 PICK 곡 재생 ~ ♬ ' + os.path.basename(randomMP3))
        playsound.playsound(randomMP3)

    # print(sec.get())  # 알람 몇 분인지 값 가져오기

    # 게임 플레이 여부


def chkOK():
    if value.get() == 1:
        print("게임 플레이 여부 -> 참")
    else:
        print("게임 플레이 여부 -> 거짓")

# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=amethyst_lee&logNo=222021293449&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# https: // opentutorials.org/module/3181/18809

# 시간이 다 되었을 때


def timer():
    cntSec = int(sec.get()) * 60
    while (cntSec != 0):
        cntSec = cntSec-1
        time.sleep(1)
        print(cntSec)

    # 음악을 튼다.
    if cntSec == 0:
        # 선택한 옵션들에 맞는 음악을 재생
        alarm()

# 최근에 이 라이브러리(버전 1.3.0)를 설치해서 테스트해봤는데 오디오 파일 재생이 안 되면서 다음과 같은 에러가 발생했습니다.
# 그래서 playsound 버전을 1.2.2 로 낮췄더니 굿굿


inputTime = tkinter.Label(root, text="타이머 시간 입력 (초)", font="메이플스토리")

# 콤보 박스
type = ["개발자 PICK", "NOISE", "QUITE"]
alarmType = tkinter.ttk.Combobox(root, width=12, height=10, value=type)
alarmType.set("선택")
alarmType.place(x=230, y=230)

# 콤보 박스 확인 버튼(체크 종류 확인)
btnCb = tkinter.Button(root, text="확인")
btnCb.place(x=350, y=230)
# btnCb.config(command=alarm)

# DB 콤보 박스
typeDB = ["NOISE, 30분", "QUITE 10분", "개발자 PICK 2분"]
alarmTypeDB = tkinter.ttk.Combobox(root, width=10, height=10, value=type)
alarmTypeDB.set("선택")
alarmTypeDB.place(x=570, y=230)
alarmTypeDB.config(state="readonly")  # 사용자의 입력 제한

# root라는 창에 입력창 생성
sec = tkinter.Entry(root, width=20)
sec.config(fg="black")  # 입력창 배경, 글자색 설정
sec.place(x=200, y=140)
# sec.bind("<Return>", timer)  # 엔터를 치면 결과라는 함수를 실행하라
sec.bind(timer)  # 엔터를 치면 결과라는 함수를 실행하라


# 게임 여부 체크버튼
value = IntVar()
gameChk = tkinter.Checkbutton(root, text="기상 게임", variable=value)
gameChk.place(x=230, y=310)
gameChk.config(command=chkOK)

# 확인 버튼
btnImg = PhotoImage(file='img/button.png')
btnOk = tkinter.Button(root, image=btnImg)
btnOk.place(x=490, y=320)
btnOk.config(command=btnpress)

root.mainloop()
