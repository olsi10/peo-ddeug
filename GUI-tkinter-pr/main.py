from tkinter import *
from tkinter import filedialog

width, height = 800, 460  # 창 크기 설정

root = Tk()
root.geometry('{0}x{1}'.format(width, height))  # 창크기 설정
root.resizable(True, False)  # 크기 조정 가능 여부

root.title("peo-ddeug")  # 창 제목

path, image = None, None

# 파일 불러오기
path = filedialog.askopenfilename(filetypes=[(
    'Image File', 'jpg'), ('Image File', 'png'), ('Image File', 'gif'), ('Image File', 'bmp')])
path = path.replace('\\', '/')

if path == '':
    exit()

print(path)
