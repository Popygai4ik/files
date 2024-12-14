from pytube import YouTube

video_url = "https://youtu.be/R-qAL-0IFug"  # ссылка на видео
yt = YouTube(video_url)  # создание объекта YouTube с указанной ссылкой
stream = yt.streams.get_by_resolution("480p") # получение видеопотока с наивысшим разрешением
stream.download()  # загрузка видео по указанному пути
