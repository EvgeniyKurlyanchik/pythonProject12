import os

import gtts

# from playsound import playsound
tts = gtts.gTTS('Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу. '
                'Их иногда ещё называют ассоциативными массивами или хеш-таблицами.'
                ' Чтобы работать со словарём, его нужно создать', lang='ru')
tts.save('converted_text.mp3')
os.system("start converted_text.mp3")
