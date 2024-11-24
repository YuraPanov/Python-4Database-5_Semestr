import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Загрузка аудиофайла
filename = 'Noita__2024-11-11__20-12-36_trim_audio.mp3'
y, sr = librosa.load(filename, sr=None)

# 1. Амплитудно-временной сигнал
plt.figure(figsize=(12, 12))

# Подплоть для амплитудно-временного сигнала
ax1 = plt.subplot(5, 1, 1)
librosa.display.waveshow(y, sr=sr, ax=ax1)
ax1.set_title('Амплитудно-временной сигнал')
ax1.set_xlabel('Время (секунды)')
ax1.set_ylabel('Амплитуда')

# 2. Частотный спектр с использованием преобразования Фурье
n = len(y)
frequencies = np.fft.fftfreq(n, 1/sr)  # Вычисляем частоты
Y = fft(y)  # Преобразование Фурье

# Отображение только положительных частот
plt.subplot(5, 1, 2)
plt.plot(frequencies[:n//2], np.abs(Y)[:n//2])  # Амплитуда спектра
plt.title('Частотный спектр')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')

# 3. Спектрограмма
# Вычисление спектрограммы с использованием STFT
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Подплоть для спектрограммы
ax2 = plt.subplot(5, 1, 3)
img = librosa.display.specshow(D, x_axis='time', y_axis='log', sr=sr, ax=ax2)
ax2.set_title('Спектрограмма')
ax2.set_xlabel('Время (секунды)')
ax2.set_ylabel('Частота (Гц)')

# Добавление цветовой шкалы
plt.colorbar(img, ax=ax2, format='%+2.0f dB')

# 4. Спектральный центроид
centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

# Подплоть для спектрального центроида
ax3 = plt.subplot(5, 1, 4)
ax3.semilogy(centroid, label='Спектральный центроид', color='r')
ax3.set_ylabel('Спектральный центроид (Гц)')
ax3.set_xlabel('Время (секунды)')
ax3.set_title('Спектральный центроид')

# 5. Мел-цепстральные коэффициенты (MFCC)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Подплоть для мел-цепстральных коэффициентов
ax4 = plt.subplot(5, 1, 5)
librosa.display.specshow(mfcc, x_axis='time', sr=sr, ax=ax4)
ax4.set_ylabel('MFCC коэффициенты')
ax4.set_xlabel('Время (секунды)')
ax4.set_title('Мел-цепстральные коэффициенты')

# Печать значений MFCC в виде массива
print("Мел-цепстральные коэффициенты (MFCC):")
print(mfcc)

# 6. Вычисление темпа
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
print(f"Темп: {tempo} BPM")

# 7. Вычисление битов
# Количество битов определяется на основе сигнала в тактовом режиме, где расчёт битов
# можно проводить как количество ударов в минуту на основе темпа
bit_depth = np.log2(np.max(np.abs(y)))  # Примерная оценка битовой глубины

print(f"Приблизительная битовая глубина: {bit_depth:.2f} бит")

# Увеличиваем расстояние между графиками
plt.tight_layout()
plt.show()
