import os
import random
import ctypes
from time import sleep


def set_random_wallpaper(pictures_folder):
    pictures = [f for f in os.listdir(pictures_folder) if f.endswith('.jpg')]
    random_picture = random.choice(pictures)
    random_picture_path = os.path.join(pictures_folder, random_picture)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, random_picture_path, 0)


pictures_folder = "/res/pictures_screencast"  # Укажите путь к папке с картинками
while True:
    set_random_wallpaper(pictures_folder)
    # sleep_time = 3600
    sleep_time = 1800
    sleep(sleep_time)
