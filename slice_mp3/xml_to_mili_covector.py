from music21 import converter

# Импортируем XML файл
score = converter.parse('C:/Users/Пользователь/PycharmProjects/ultima/res/music/output.xml')

# Экспортируем в MIDI
score.write('midi', fp='result_file.mid')

print("Конвертация завершена: файл сохранён как result_file.mid")
