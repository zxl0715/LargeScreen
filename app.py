# coding=gbk
from cefpython3 import cefpython as cef

import ctypes
import tkinter as tk
import threading
import os
from configparser import ConfigParser


class Application(tk.Frame):
    navigation_bar = None
    url = 'https://www.baidu.com'
    width = 1920
    height = 1080

    def __init__(self, root, width, height, siteUrl):
        self.width = width
        self.height = height
        self.url = siteUrl
        root.geometry("{0}x{1}".format(self.width, self.height))
        tk.Frame.__init__(self, root)
        self.master.title("")
        self.bind("<Configure>", self.on_configure)

        self.browser_frame = BrowserFrame(self, self.navigation_bar, self.url)  # 浏览器框架
        self.browser_frame.grid(row=1, column=0, sticky=(tk.N + tk.S + tk.E + tk.W))
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.pack(fill=tk.BOTH, expand=tk.YES)  # 包装 Application

    def on_configure(self, event):
        if self.browser_frame:
            width = event.width
            height = event.height
            if self.navigation_bar:
                height = height - self.navigation_bar.winfo_height()
            self.browser_frame.on_Application_configure(width, height)


class BrowserFrame(tk.Frame):
    closing = False
    browser = None

    def __init__(self, master, navigation_bar=None, url='https://www.baidu.com'):
        self.navigation_bar = navigation_bar
        self.url = url
        tk.Frame.__init__(self, master)
        self.bind("<Configure>", self.on_configure)

    def embed_browser(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)

        self.browser = cef.CreateBrowserSync(
            window_info,
            url=self.url
        )
        self.message_loop_work()

    def get_window_handle(self):  # 获取窗口句柄
        if self.winfo_id() > 0:
            return self.winfo_id()

    def message_loop_work(self):  # 消息循环工作
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    def on_configure(self, _):  # 判断是否有 cef 对象
        if not self.browser:
            self.embed_browser()

    def on_Application_configure(self, width, height):  # cef 窗口大小
        if self.browser:
            pass
            ctypes.windll.user32.SetWindowPos(self.browser.GetWindowHandle(),
                                              0, 0, 0, width, height, 0x0002)


# def runserver():
#     app = Flask(__name__)
#     @app.route('/')
#     def index():
#         return '<h1>233</h1>'
#     app.run()

if __name__ == '__main__':
    # threading.Thread(target=runserver).start()

    conf = ConfigParser()
    conf.read("config.ini", 'utf-8')
    siteUrl = conf.get("main", "url");
    title = conf.get("main", "title");
    fullScreen = conf.getboolean("main", "fullScreen")
    width = conf.get("main", "width");
    height = conf.get("main", "height");
    print(siteUrl)
    print(title)
    #创建窗口
    root = tk.Tk()

    # 全屏显示的关键
    if fullScreen:
        root.overrideredirect(1)
    #     https://www.izhangchao.com/internet/internet_236356.html
    #     root.geometry('390x30+0-10')

    app = Application(root, width, height, siteUrl)

    cef.Initialize()
    #运行并显示窗口
    app.mainloop()
    cef.Shutdown()
    os._exit(0)
