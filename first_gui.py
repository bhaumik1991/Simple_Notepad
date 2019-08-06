# from tkinter import *
# from tkinter.ttk import *
# window = Tk()
# window.title("Welcome to First GUI")
# window.geometry("400x300")
# combo = Combobox(window)
# combo['values'] = (1,2,3,4,5, "Text")
# combo.current(1)
# combo.grid(column=0,row=0)
# # lbl = Label(window, text="Hello", font=("Garmond Bold",25))
# # lbl.grid(column=0, row=0)
# # txt = Entry(window,width=10,state="disabled")
# # txt.grid(column=1,row=0)
# # def clicked():
# #     res = "Welcome " +txt.get()
# #     lbl.configure(text= res)
# #
# # btn = Button(window, text="Click me", bg="Blue", fg="Yellow", command=clicked)
# # btn.grid(column=2, row=0)
# window.mainloop()

# import socket
# ip = socket.gethostbyname('www.google.com')
# print(ip)


import shutil
dest = r"C:\Users\bhaum\Documents\Result"
src = r"C:\Users\bhaum\Documents\Wondershare_Filmora"
# s = os.listdir(src)
# print(s)
def copy(src,dest):
    try:
        shutil.copytree(src, dest)
        print("Copied")
    except shutil.Error as e:
        print("Directory not copied. Error: %s % e")
    except FileExistsError:
        print("File already exists!")
if __name__ == '__main__':
    copy(src,dest)

    # try:
    #     os.mkdir(dest)
    #     print("Directory is created")
    # except FileExistsError:
    #     print("Directory alreay exists!")


# try:
#     a = int(input("Enter 1st number:"))
#     b = int(input("Enter 2nd number:"))
#     c = a/b
#     print("a/b = %d"%c)
# except Exception:
#     print("Can not devided by zero")

# try:
#     a = int(input("Enter 1st number:"))
#     b = int(input("Enter 1st number:"))
#     if b is 0:
#         raise ArithmeticError
#     else:
#         print("a/b =",a/b)
# except ArithmeticError:
#     print("Can not devided by zero")

# try:
#     file = open("abc.txt","r")
# except IOError:
#     print("file not found")
# else:
#     print("opened succesfully!")
#     file.close()

# try:
#     file = open("abc.txt","r")
#     try:
#         file.write("Hi I am good")
#     finally:
#         file.close()
#         print("file closed")
# except:
#     print("Error")
#
