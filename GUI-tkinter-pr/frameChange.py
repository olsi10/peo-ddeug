import tkinter
window = tkinter.Tk()
window.title("Frame_Change")
window.geometry("600x600+200+200")

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")

def openFrame(frame):
	frame.tkraise()
    
btnToFrame1 = tkinter.Button(frame3, 
    text="Change To Frame1", 
    padx=10, 
    pady=10,
    command=lambda:[openFrame(frame1)])

btnToFrame2 = tkinter.Button(frame1, 
    text="Change To Frame2", 
    padx=10, 
    pady=10,
    command=lambda:[openFrame(frame2)])
btnToFrame3 = tkinter.Button(frame2, 
    text="Change To Frame3", 
    padx=10, 
    pady=10,
    command=lambda:[openFrame(frame3)])

btnToFrame1.pack()
btnToFrame2.pack()
btnToFrame3.pack()

openFrame(frame1) #기본메인화면
window.mainloop()

# https://lcs1245.tistory.com/entry/Python-tkinter-Frame%ED%94%84%EB%A0%88%EC%9E%84-%EC%A0%84%ED%99%98%ED%95%98%EA%B8%B0
# 프레임 전환 예제