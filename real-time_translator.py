from deep_translator import GoogleTranslator

to_translate = 'мрiя'

translated = GoogleTranslator(source='uk', target='ru').translate(to_translate)

print(translated)