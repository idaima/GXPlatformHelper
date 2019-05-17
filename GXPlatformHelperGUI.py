#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import IntVar, messagebox, filedialog  # import this to fix messagebox error
import GXPlatformHelper

window = tk.Tk()
window.title('供销平台小助手')
window.geometry('460x360')

# welcome image
canvas = tk.Canvas(window, height=200, width=460)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='淘宝账号: ').place(x=50, y=150)
tk.Label(window, text='密码: ').place(x=50, y=190)

var_user_name = tk.StringVar()
var_user_name.set('')
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160, y=150)
var_user_pwd = tk.StringVar()
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show='*')
entry_user_pwd.place(x=160, y=190)

tk.Label(window, text='产品线: ').place(x=50, y=230)

var_product_line_name = tk.StringVar()
entry_product_line_name = tk.Entry(window, textvariable=var_product_line_name)
entry_product_line_name.place(x=160, y=230)

def callRB():
    pass
product_type = IntVar()
sold_button = tk.Radiobutton(window, text='已铺货', variable=product_type, command=callRB, value=0)
sold_button.place(x=50, y=270)

unsold_buton = tk.Radiobutton(window, text='未铺货', variable=product_type, command=callRB, value=1)
unsold_buton.place(x=150, y=270)

sold_button.select()


def start():
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    product_line_name=var_product_line_name.get()
    if (user_name == ''):
        tk.messagebox.showinfo(title='温馨提示', message='请输入淘宝账号 ')
        return
    if (user_pwd == ''):
        tk.messagebox.showinfo(title='温馨提示', message='请输入账号密码 ')
        return
    if (product_line_name == ''):
        tk.messagebox.showinfo(title='温馨提示', message='请输入目标产品线名称 ')
        return
    GXPlatformHelper.USER_NAME = user_name
    GXPlatformHelper.USER_PWD = user_pwd
    GXPlatformHelper.PRODUCT_LINE_NAME = product_line_name
    GXPlatformHelper.PRODUCT_STATUS = product_type.get()
    gongxiao_platform = GXPlatformHelper.gongxiao_platform()
    gongxiao_platform.login()


# start button
btn_login = tk.Button(window, text='开始', command=start)
btn_login.place(x=200, y=300)

window.mainloop()
