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

root.title("peo-ddeug")  # 창 제목


def click():
    root.destroy()
    import main


title_font = tkinter.font.Font(family="함초롬바탕", size=30)
btn_font = tkinter.font.Font(family="함초롬바탕", size=10)

# 텍스트 / Label(위치, text ="텍스트").pack() -> 첫번째 인자값(위치)에 보여줘라
title = tkinter.Label(root, text='퍼뜩퍼뜩', font=title_font, width=10)

title.place(x=280, y=0)

# 버튼 / grid, frame
btn_width, btn_height = 10, 3

frame = tkinter.Frame(root, bg='#80c1ff', bd=5)
# frame.place(x=200, y=300)

# # 버튼 컴포넌트 생성
# Button(위치, text='텍스트', width=너비, height=높이).pack()
btnN = tkinter.Button(root, text='다시 메인으로', font=btn_font,
                      width=btn_width, height=btn_height)
btnN.grid(row=0, column=0)

btnC = tkinter.Button(root, text='커스텀 알람', font=btn_font,
                      width=btn_width, height=btn_height)
btnC.grid(row=0, column=1)

btnN.place(x=300, y=100)
btnC.place(x=400, y=100)

# type 의 객체를 생성하고 Button있지만 즉시 grid메서드를 호출하여 를 반환합니다
# None. 따라서 pButton가 할당 None되고 이것이 다음 행이 실패하는 이유입니다.
# 즉, 먼저 버튼을 생성하고 에 할당 pButton한 다음 그 위에 작업을 수행합니다.
#### Nonetype 에러나는 이유 : 스택오버플로우 출처

btnN.config(command=click)

# frame.pack()

root.mainloop()
