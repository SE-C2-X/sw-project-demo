import tkinter as tk
from tkinter import messagebox

# 登录界面
class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title('用户登录')
        master.geometry('300x180')
        tk.Label(master, text='用户名:').pack(pady=(20, 0))
        self.entry_user = tk.Entry(master)
        self.entry_user.pack()
        tk.Label(master, text='密码:').pack(pady=(10, 0))
        self.entry_pwd = tk.Entry(master, show='*')
        self.entry_pwd.pack()
        tk.Button(master, text='登录', command=self.login).pack(pady=15)

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pwd.get()
        if username == 'admin' and password == '123456':
            messagebox.showinfo('登录成功', '欢迎，管理员！')
        else:
            messagebox.showerror('登录失败', '用户名或密码错误')

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()