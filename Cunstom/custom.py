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
import tkinter.ttk
from tokenize import group
from turtle import bgcolor, width
from tkinter import filedialog
import tkinter.font
import webbrowser
import time


root = Tk()
root.resizable(False, False)
root.geometry("750x400-40+50")
root.title("peo-ddeug")  # 창 제목
root.configure(background='white')

backImg = tkinter.PhotoImage(file="img/custom.png")
label = tkinter.Label(root, image=backImg)
label.pack()

root.title("peo-ddeug")  # 창 제목


def btnpress():
    timer()

# 입력된 결과를 실행하는 함수


def resultURL():
    getentURL = str(entURL.get())
    webbrowser.open(getentURL)

# 타이머를 맞추고


def timer():
    cntSec = int(sec.get()) * 60
    while (cntSec != 0):
        cntSec = cntSec-1
        time.sleep(1)
        print(cntSec)

    # 음악을 튼다.
    if cntSec == 0:
        # 선택한 옵션들에 맞는 음악을 재생
        resultURL()


# url을 입력할 입력창 생성
entURL = tkinter.Entry(root, width=20)
entURL.config(fg="black")  # 입력창 배경, 글자색 설정
entURL.place(x=200, y=220)
entURL.bind(resultURL)  # 엔터를 치면 결과라는 함수를 실행하라.

# 타이머를 입력할 입력창 생성
sec = tkinter.Entry(root, width=15)
sec.config(fg="black")  # 입력창 배경, 글자색 설정
sec.place(x=200, y=140)
# sec.bind("<Return>", timer)  # 엔터를 치면 결과라는 함수를 실행하라
sec.bind(timer)  # 엔터를 치면 결과라는 함수를 실행하라

inputTime = tkinter.Label(root, text="타이머 시간 입력 (초)", font="메이플스토리")

# DB 콤보 박스
typeDB = ["NOISE, 30분", "QUITE 10분", "개발자 PICK 2분"]
alarmTypeDB = tkinter.ttk.Combobox(root, width=10, height=10, value=type)
alarmTypeDB.set("선택")
alarmTypeDB.place(x=570, y=230)
alarmTypeDB.config(state="readonly")  # 사용자의 입력 제한


# 게임 여부 체크버튼
value = IntVar()
gameChk = tkinter.Checkbutton(root, text="기상 게임", variable=value)
gameChk.place(x=230, y=310)

# 확인 버튼
btnImg = PhotoImage(file='img/button.png')
btnOk = tkinter.Button(root, image=btnImg)
btnOk.place(x=490, y=320)
btnOk.config(command=btnpress)

root.mainloop()
