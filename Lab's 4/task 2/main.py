import os
import numpy as np
from moviepy.editor import VideoFileClip
from skimage import transform, io
from colorama import Fore, init

init(autoreset=True)  # Автоматически сбрасывать цвет текста после вывода


def ClipVideo(name_video, time_start, time_end, folder, frame_step):
    if not os.path.exists(name_video):
        return print(Fore.RED + '[-] Исходное видео не найдено')

    video = VideoFileClip(name_video)
    duration = video.duration

    if name_video == folder:
        return print(Fore.RED + '[-] Указанное имя совпадает с исходником')
    if duration < time_end:
        return print(Fore.RED + '[-] Указанное время окончания видео больше исходника')
    if time_start < 0:
        return print(Fore.RED + '[-] Указанное время начала видео не подходит')

    # Обрезка видео по указанному интервалу
    video = video.subclip(time_start, time_end)
    width = 250
    frame_num = 0
    for t in range(time_start, time_end + frame_step, frame_step):
        frame = video.get_frame(t)
        resized_frame = transform.resize(frame, (width, int(frame.shape[0] * width / frame.shape[1])))
        resized_frame = (resized_frame * 255).astype(np.uint8)
        frame_filename = os.path.join(folder, f"{frame_num}.png")
        io.imsave(frame_filename, resized_frame)
        frame_num += 1

    video.close()


print("Введите для работы путь до исходника через /")
name_video = input()
print("Введите секунду начала")
time_start = int(input())
print("Введите секунду конца")
time_end = int(input())
print("Введите папку сохранения")
folder = input()
print("Введите периодичность кадрирования")
frame_step = int(input())

ClipVideo(name_video, time_start, time_end, folder, frame_step)
