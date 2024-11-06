import os
from colorama import Fore, init
from moviepy.editor import *
import argparse
def CutVideo(name_video, time_start, time_end, new_name):
    if os.path.exists(name_video):
        video = VideoFileClip(name_video)
        duration = video.duration

        if name_video == new_name:
            return print(Fore.RED + '[-] Указанное имя совпадает с исходником')
        if duration < time_end:
            return print(Fore.RED + '[-] Указанное время окончания видео больше исходника')
        if time_start < 0:
            return print(Fore.RED + '[-] Указанное время начала видео не подходит')

        cropped_video = video.subclip(time_start, time_end)
        cropped_video.write_videofile(new_name, codec="libx264")

        video.close()
        cropped_video.close()
    else:
        return
print("Введите для работы путь до исходника через /")
name_video = input()
print("Введите секунду начала")
time_start = int(input())
print("Введите секунду конца")
time_end = int(input())
print("Введите для работы путь до исходника через /")
new_name = input()
CutVideo(name_video, time_start, time_end, new_name)

