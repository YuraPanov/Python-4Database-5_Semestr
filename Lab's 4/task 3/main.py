import cv2

# video_path = "D:/Python_LabsAndProjekt/Python4workWith_DataBase_5semester/Lab's 4/movies/2023-07-03 22-36-07.mp4"
video_path = input("Введите путь к видеофайлу: ")
cap = cv2.VideoCapture(video_path)

# Получение FPS и имени файла
fps = cap.get(cv2.CAP_PROP_FPS)
file_name = video_path.split('/')[-1]  # Получение имени файла из пути

# Проверка, что видеофайл открылся
if not cap.isOpened():
    print("Ошибка: не удалось открыть видео. Проверьте путь к файлу.")
else:
    # Чтение и отображение каждого кадра
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Отображение текста на кадре
        text = f"File: {file_name} | FPS: {fps:.2f}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Показ кадра с текстом
        cv2.imshow("Video", frame)

        # Нажмите 'q' для выхода из видео
        if cv2.waitKey(int(1000 // fps)) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
