# 커스텀 알람 제작 등 모든 알람을 타이머 지정으로 사용자를 깨우는 프로그램

# <기본 설정>
# 일어나는 시간, 타이머 설정
# 원하는 알람 타입 선택 (NOISE / QUITE)
# 몇 분간 알람을 재생하는가

# <커스텀 설정>
#  일어나는 시간, 타이머 설정
#  원하는 알람 음악 설정 (url 달기)

# 시나리오
#  프로그램을 사용하여 알람 메뉴를 보여준다.
#  메뉴에서 기본 설정, 커스텀 설정 둘 중 하나를 선택한다.
#  일어나는 시간, 타이머 둘 중 하나 골라 선택한다.
#  원하는 알람 타입을 선택하거나 음악 url을 넣어서 설정한다.
#  알람 재생 길이
#  마지막으로 알람 듣고 일어나면 됨!


# import WakeUpGame.game.frompoop as frompoop
# import WakeUpGame.game.catchBug as catchBug
# import sqlite3  # pip install pysqlite3
import sys
import os
import multiprocessing
import random
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
import playsound  # pip install playsound==1.2.2
import pygame  # pip install pygame --pre
from pygame import mixer
from app import *
mixer.init()  # Initialzing pyamge mixer


# conn = sqlite3.connect('data.sqlite', isolation_level=None)
# c = conn.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS users\
# (id INTEGER PRIMARY KEY, alarm TEXT, timer TEXT, game TEXT, combobox TEXT)")

root = Tk()
root.resizable(False, False)
root.geometry("750x400-40+50")
root.title("peo-ddeug")  # 창 제목
root.configure(background='white')

backImg = tkinter.PhotoImage(file="img/original.png")
label = tkinter.Label(root, image=backImg)
label.pack()

root.title("peo-ddeug")  # 창 제목


def btnpress():
    timer()

# 체크박스의 참, 거짓을 판단 후 2초 대기하다가 게임 화면을 연다.


def game():
    if value.get() == 1:
        time.sleep(2)
        openGame()
    else:
        return False

# 게임 파일을 랜덤으로 골라서 랜덤 게임을 화면에 띄운다


def bugGame():
    root.destroy()
    import catchBug


def poopGame():
    root.destroy()
    import frompoop


def openGame():
    pathG = "/peo-ddeug/WakeUpGame"
    gamefile = [os.path.join(pathG, f)
                for f in os.listdir(pathG) if f.endswith('.py')]
    randomgame = random.choice(gamefile)

    print("완전 재밌는 게임 ♨ " + os.path.basename(randomgame))

    if randomgame == "catchBug.py":
        bugGame()
    elif randomgame == "poopGame.py":
        poopGame()

    # 알람 파일을 배열에 담아 랜덤으로 꺼내 재생 / 알람 타입 확인 후 알맞는 알람 재생


def alarm():
    # https://stackoverflow.com/questions/60250171/how-to-play-random-mp3-files-in-pygame
    pathN = "/peo-ddeug/soundfile/NOISE"
    pathQ = "/peo-ddeug/soundfile/QUITE"
    pathD = "/peo-ddeug/soundfile/developerPICK"

    # 폴더의 모든 파일 목록을 가져오는 데 사용 / endswtich 문자열이 mp3로 끝나는지
    N_mp3 = [os.path.join(pathN, f)
             for f in os.listdir(pathN) if f.endswith('.mp3')]
    Q_mp3 = [os.path.join(pathQ, f)
             for f in os.listdir(pathQ) if f.endswith('.mp3')]
    D_mp3 = [os.path.join(pathD, f)
             for f in os.listdir(pathD) if f.endswith('.mp3')]

    type = alarmType.get()          # 알람 타입을 지정하는 콤보박스 값
    stopSec = int(mSec.get()) * 60  # 알람 울릴 시간을 정한 입력박스 값

    if type == "NOISE":
        randomMP3 = random.choice(N_mp3)
        # https://yunwoong.tistory.com/41
        print(f'{stopSec} 초 동안')
        print('고막을 때리는 곡 재생 ♬ ' + os.path.basename(randomMP3))

        # https://stackoverflow.com/questions/57158779/how-to-stop-audio-with-playsound-module
        mixer.music.load(randomMP3)  # loading music
        mixer.music.play()  # play music
        time.sleep(stopSec)  # delay
        mixer.music.stop()  # stop music

        # game function call
        if stopSec == 0:
            game()

        # playsound.playsound(randomMP3)
        # https://ko.code-paper.com/python/examples-does-playsound-python-stop-script
        # mp = multiprocessing.Process(target=playsound, args=(randomMP3,))
        # mp.start()
        # time.sleep(m)
        # mp.terminate()

    elif type == "QUITE":
        randomMP3 = random.choice(Q_mp3)
        print(f'{stopSec} 초 동안')
        print('QUITE라고 조용할까? 일어나야지!!! 곡 재생 ~ ♬ ' + os.path.basename(randomMP3))

        mixer.music.load(randomMP3)  # loading music
        mixer.music.play()  # play music
        time.sleep(stopSec)  # delay
        mixer.music.stop()  # stop music

        # game function call
        if stopSec == 0:
            game()

    elif type == "개발자 PICK":
        randomMP3 = random.choice(D_mp3)
        print(f'{stopSec} 초 동안')
        print('개발자 PICK 곡 재생 ~ ♬ ' + os.path.basename(randomMP3))

        mixer.music.load(randomMP3)  # loading music
        mixer.music.play()  # play music
        time.sleep(stopSec)  # delay
        mixer.music.stop()  # stop music

        # game function call
        if stopSec == 0:
            game()

# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=amethyst_lee&logNo=222021293449&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# https: // opentutorials.org/module/3181/18809


def timer():
    btnCb['state'] = tkinter.NORMAL
    btnCb1['state'] = tkinter.NORMAL
    cntSec = int(sec.get()) * 60
    while (cntSec != 0):
        cntSec = cntSec-1
        time.sleep(1)
        print(cntSec)

    # 음악을 튼다.
    if cntSec == 0:
        # 선택한 옵션들에 맞는 음악을 재생
        # alarm()
        # m = int(mSec.get()) * 60
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
# btnCb = tkinter.Button(root, text="확인")
# btnCb.place(x=350, y=230)
# btnCb.config(command=alarm)

# DB 콤보 박스
typeDB = []
res = getType()
typeDB.append(res)
alarmTypeDB = tkinter.ttk.Combobox(root, width=10, height=10, value=typeDB)
alarmTypeDB.set("선택")
alarmTypeDB.place(x=570, y=230)

# root라는 창에 입력창 생성
sec = tkinter.Entry(root, width=15)
sec.config(fg="black")  # 입력창 배경, 글자색 설정
sec.place(x=230, y=140)
# sec.bind("<Return>", timer)  # 엔터를 치면 결과라는 함수를 실행하라
sec.bind(timer)  # 엔터를 치면 결과라는 함수를 실행하라
strSec = sec.get()

# 몇 초간 음악 재생할지 결정
mSec = tkinter.Entry(root, width=15)
mSec.config(fg="black")  # 입력창 배경, 글자색 설정
mSec.place(x=570, y=140)
# sec.bind("<Return>", timer)  # 엔터를 치면 결과라는 함수를 실행하라
mSec.bind(timer)  # 엔터를 치면 결과라는 함수를 실행하라
strMsec = mSec.get()

# 게임 여부 체크버튼
# https://gomming.tistory.com/59
value = IntVar()
gameChk = tkinter.Checkbutton(root, text="기상 게임", variable=value)
gameChk.place(x=230, y=310)
gameChk.bind(game)

# 확인 버튼
btnImg = PhotoImage(file='img/button.png')
btnOk = tkinter.Button(root, image=btnImg)
btnOk.place(x=530, y=320)
btnOk.config(command=btnpress)

btnCb = tkinter.Button(root, text="벌레 게임", state=tkinter.DISABLED)
btnCb.place(x=455, y=355)
btnCb.config(command=bugGame)

btnCb1 = tkinter.Button(root, text="똥 게임", state=tkinter.DISABLED)
btnCb1.place(x=460, y=325)
btnCb1.config(command=poopGame)


def save_window():
    new = Tk()
    new.title("알람 DB 저장")
    new.geometry("280x160")
    tkinter.Label(new, text="알람 DB 저장").grid(padx=10, pady=10)
    title = tkinter.Entry(new).place(x=20, y=60)

    def save_type():
        saveType("title", str(sec.get()), str(mSec.get()), alarmType.get())

    sv = tkinter.Button(new, text="저장", width=10,
                        command=save_type).place(x=180, y=80)

    ex = tkinter.Button(new, text="확인", width=10,
                        command=new.destroy).place(x=180, y=110)

    # def exit():
    #     new.destroy()

    new.mainloop()


btnSave = tkinter.Button(root, text="알람 저장")
btnSave.place(x=370, y=350)
t = alarmType.get()
btnSave.config(command=save_window)

root.mainloop()
