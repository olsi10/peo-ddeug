from tkinter import *
from tkinter import filedialog

width, height = 800, 460  # 창 크기 설정

root = Tk()
root.geometry('{0}x{1}'.format(width, height))  # 창크기 설정
root.resizable(True, False)  # 크기 조정 가능 여부

root.title("peo-ddeug")  # 창 제목

# path, image = None, None

# 파일 불러오기
# path = filedialog.askopenfilename(filetypes=[(
#     'Image File', 'jpg'), ('Image File', 'png'), ('Image File', 'gif'), ('Image File', 'bmp')])
# path = path.replace('\\', '/')

# if path == '':
#     exit()

# print(path)


# 텍스트 / Label(위치, text ="텍스트").pack() -> 첫번째 인자값(위치)에 보여줘라
Label(root, text='퍼뜩퍼뜩').pack()

# 버튼 / grid, frame
btn_width, btn_height = 10, 3


#Button(위치, text='텍스트', width=너비, height=높이).pack()
Button(root, text='기본 알람', width=btn_width, height=btn_height).pack()
Button(root, text='커스텀 알람', width=btn_width, height=btn_height).pack()

# pack과 grid 메소드는 함께 사용할 수 없다. <에러 발생> 그래서 frame을 대체제로 사용


root.mainloop()
