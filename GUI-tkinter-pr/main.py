from tkinter import *
from tkinter import filedialog
import tkinter.font
from tokenize import group
from turtle import bgcolor


root = tkinter.Tk()
root.geometry("800x600")

# width, height = 800, 460  # 창 크기 설정
# root.geometry('{0}x{1}'.format(width, height))  # 창크기 설정
# root.resizable(True, False)  # 크기 조정 가능 여부

root.title("peo-ddeug")  # 창 제목

# path, image = None, None

# 파일 불러오기
# path = filedialog.askopenfilename(filetypes=[(
#     'Image File', 'jpg'), ('Image File', 'png'), ('Image File', 'gif'), ('Image File', 'bmp')])
# path = path.replace('\\', '/')

# if path == '':
#     exit()

# print(path)

title_font = tkinter.font.Font(family="메이플스토리", size=30)
btn_font = tkinter.font.Font(family="메이플스토리", size=10)

# 텍스트 / Label(위치, text ="텍스트").pack() -> 첫번째 인자값(위치)에 보여줘라
title = tkinter.Label(root, text='퍼뜩퍼뜩', font=title_font)
title.place(x=200, y=300)

# title.place(x=200, y=100)

# 버튼 / grid, frame
btn_width, btn_height = 10, 3

frame = tkinter.Frame(root, bg='#80c1ff', bd=5)

# def click_btn():
#     btn_normal["text"] = "클릭했습니다"

# # 버튼 컴포넌트 생성
# Button(위치, text='텍스트', width=너비, height=높이).pack()
btn_normal = tkinter.Button(frame, text='기본 알람', font=btn_font, width=btn_width,
                            height=btn_height).grid(row=0, column=0)
btn_custom = tkinter.Button(frame, text='커스텀 알람', font=btn_font, width=btn_width,
                            height=btn_height,).grid(row=0, column=1)  # command=click_btn

# 버튼 문자열 변경 함수


# root = tkinter.Tk()
# root.title("첫 번째 버튼")
# root.geometry("800x600")
# # 버튼 컴포넌트 생성
# button = tkinter.Button(root, text="버튼 문자열", font=("Times New Roman", 24))
# # 윈도우에 버튼 배치
# button.place(x=200, y=100)
# root.mainloop()

# pack과 grid 메소드는 함께 사용할 수 없다. <에러 발생> 그래서 frame을 대체제로 사용
# frame은 div와 비슷, 요소를 묶어줌

# 코드에서 작성하신 것처럼 grid 와 pack 을 혼용하여서 쓰시면 안됩니다.
# 마치 군대에서 이등병에게 소대장이 "야, 여기 청소해" 를 함과 동시에
# 분대장인 병장이 "야, 청소 하지마" 를 얘기하는 것과 같습니다.
# 이등병은 어떻게 해야 할지 혼란스러워지겠죠..
# 인프런 나도코딩 댓글 출처

frame.pack()

root.mainloop()
