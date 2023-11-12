#? >> INIT / GLOBAL FILE <<
import os, pystray, gc, json, pystray, win11toast
import datetime
from threading import Thread
from ctypes import windll, byref, sizeof, c_int
from PIL import Image

#Inputs
from pynput.keyboard import Listener

import tkinter as tk
from customtkinter import CTkImage as CImg
from customtkinter import CTk
from customtkinter import CTkFrame as Frame
from customtkinter import CTkLabel as Label
from customtkinter import CTkButton as Button
from customtkinter import CTkEntry as Entry
from customtkinter import CTkScrollableFrame as ScrollFrame


#? >> APP INFO
APP_NAME = 'Key Achiever'
APP_VERSION = 6.0

#? >> COLORS and FONTS
BRAND_PRIMARY = '#ee77c7'
BRAND_PRIMARY_DK = '#815699'
TEXT = '#868686'
BACKGROUND = '#0f0e0f'
BACKGROUND_2 = '#141414'
BACKGROUND_3 = '#140e18'

RANK1 = '#e5d548'
RANK2 = '#c5cdd1'
RANK3 = '#d8a595'

FONT = 'Calibri'
COUNT = (FONT, 45, 'normal', 'bold')
TITLE_2 = (FONT, 35, 'normal', 'bold')
TITLE = (FONT, 25, 'normal', 'bold')
H2 = (FONT, 20, 'normal', 'bold')
H3 = (FONT, 18, 'normal', 'bold')
H4 = (FONT, 15, 'normal', 'bold')
H5 = (FONT, 12, 'italic', 'bold')
BTN_SM = (FONT, 15, 'normal', 'bold')

#? >> LOAD IMAGES/ICONS
normal = (20,20)
medium = (25, 25)
large = (60, 60)
ICONS = [
    CImg(dark_image=Image.open('Icons\\keycap.png'), size=large),
    CImg(dark_image=Image.open('Icons\\home.png'), size=medium),
    CImg(dark_image=Image.open('Icons\\cog.png'), size=medium)
]

#? >> ROOT AND FOLDERS
ROOT_FOLDER = os.getcwd()

if not os.path.exists('Data'):
    os.mkdir('Data')

#? >> INIT APP
from app.main import KeyAchiever
app = KeyAchiever()