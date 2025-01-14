from moviepy import ImageSequenceClip

# Параметры
path_to_images = "render/"  # Укажите путь к папке с изображениями
name_ = "output_video.mp4"              # Имя результата
fps = 24                                   # Частота кадров вашего видео

# Получение списка изображений
import os
images = [os.path.join(path_to_images, img) for img in sorted(os.listdir(path_to_images)) if img.endswith('.png')]

# Создание видео из изображений
clip = ImageSequenceClip(images, fps=fps)
clip.write_videofile(
    name_,
    codec='libx264',
    preset='slow',  # Настройка скорости/качества кодирования
    ffmpeg_params=['-crf', '18']  # Контроль качества через CRF
)
