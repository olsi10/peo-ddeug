try:
    import Tkinter as tk
except:
    import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="퍼뜩퍼뜩", font=('Jua', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.geometry("800x600")
        tk.resizable(False, False)
        tk.title("peo-ddeug")  # 창 제목


# title_font = tkinter.font.Font(family="함초롬바탕")
# btn_font = tkinter.font.Font(family="함초롬바탕", size=10)

# title = tkinter.Label(root, text='퍼뜩퍼뜩', font=title_font)
# title.place(x=100, y=0)

# btn_width, btn_height = 10, 3

# frame = tkinter.Frame(root, bg='#80c1ff', bd=5)

# btnN = tkinter.Button(root, text='기본 알람', font=btn_font,
#                       width=btn_width, height=btn_height)
# btnN.grid(row=0, column=0)

# btnC = tkinter.Button(root, text='커스텀 알람', font=btn_font,
#                       width=btn_width, height=btn_height)
# btnC.grid(row=0, column=1)

# btnN.place(x=300, y=200)
# btnC.place(x=400, y=200)

# btnN.config(command=click)
# btnC.config(command=click1)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
