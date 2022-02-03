"""
@author: Furqan Abaid
"""

#Imports
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import threading
from selenium.webdriver import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PyInstaller.utils.hooks.qt import add_qt5_dependencies
from PyInstaller.utils.hooks import collect_data_files
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import webbrowser as newtab
import math

def isNaN(string):
    return string != string
#opening excel file
def openExcel():
    global excelFile
    global usernames
    global passwords
    print("Opening Excel file")
    filePath = askopenfilename()
    print("filePath: ",filePath)
    excelFile = pd.read_excel(filePath)


global url
global s
url=r"https://sellercenter.daraz.pk/apps/seller/login?redirect_url=https%3A%2F%2Fsellercenter.daraz.pk%2F"
s=Service(ChromeDriverManager().install())

def openlinks():
    index=2
    driver = webdriver.Chrome(service=s)
    driver.get(row[index])
    driver.execute_script("window.open('"+row[index]+"');")
    index=index+1
    if(index>=len(row)):
        return
    
    
def openWebPage(row):
    user_name=row[0]
    pass_word=row[1]
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(url)
   
    delay=10
    myElem1 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J-m-content"]/div/div[2]/div[3]/form/div/div[1]/span/input')))
    myElem1.send_keys(user_name)
    myElem2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J-m-content"]/div/div[2]/div[3]/form/div/div[2]/span/input')))
    myElem2.send_keys(pass_word)
    myElem3 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J-m-content"]/div/div[2]/div[3]/form/div/div[3]/button')))
    myElem3.click()
   
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=s)
    openlinks()
    

def start():
    if len(entry0.get()) == 0:
        for i in range(len(excelFile)):
                row=excelFile.iloc[i]
                t1 = threading.Thread(target=openWebPage,args=(row,))
                t1.start()
    if len(entry0.get()) != 0:
        a=int(entry0.get())
        for j in range(a):
           print("Executing...")
           row=excelFile.iloc[j]
           t1 = threading.Thread(target=openWebPage,args=(row,))
           t1.start()








#UI
window = Tk()

window.geometry("500x300")
window.configure(bg = "#1d1d1d")
canvas = Canvas(
    window,
    bg = "#1d1d1d",
    height = 300,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = openExcel,
    relief = "flat")

b0.place(
    x = 159, y = 97,
    width = 181,
    height = 25)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = start,
    relief = "flat")

b1.place(
    x = 159, y = 191,
    width = 181,
    height = 25)

canvas.create_text(
    250.0, 142.0,
    text = "Enter Limit",
    fill = "#ffffff",
    font = ("None", int(12.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    249.5, 167.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 159, y = 156,
    width = 181,
    height = 20)

window.resizable(False, False)
window.mainloop()

