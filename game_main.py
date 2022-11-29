from tkinter import *
from tkinter import filedialog
import tkinter.font
from tokenize import group
from turtle import bgcolor, width

root = Tk()
root.geometry("750x400-40+50")
root.resizable(False, False)
root.configure(background='white')


backImg = tkinter.PhotoImage(file="img/mainImg.png")
mainLabel = tkinter.Label(root, image=backImg)
mainLabel.pack()

root.title("peo-ddeug")  # 창 제목


def click1():
    root.destroy()
    import WakeUpGame.catchBug as catchBug


def click():
    root.destroy()
    import WakeUpGame.frompoop as frompoop


btn_font = tkinter.font.Font(family="메이플스토리", size=13)

btn_width, btn_height = 15, 3

btnN = tkinter.Button(root, text='개구리 잡기 게임', font=btn_font,
                      width=btn_width, height=btn_height, bg='white')
btnC = tkinter.Button(root, text='똥 피하기 게임', font=btn_font,
                      width=btn_width, height=btn_height, bg='white')

btnN.place(x=200, y=180)
btnC.place(x=380, y=180)

btnN.config(command=click1)
btnC.config(command=click)


# frame.pack()

root.mainloop()

# type 의 객체를 생성하고 Button있지만 즉시 grid메서드를 호출하여 를 반환합니다
# None. 따라서 pButton가 할당 None되고 이것이 다음 행이 실패하는 이유입니다.
# 즉, 먼저 버튼을 생성하고 에 할당 pButton한 다음 그 위에 작업을 수행합니다.
# Nonetype 에러나는 이유 : 스택오버플로우 출처
