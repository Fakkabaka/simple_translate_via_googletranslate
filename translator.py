from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

text = input("Введите текст для перевода: ")

translated = translator.translate(text, dest='en')#впиши в терминал googletrans.LANGUAGES и получи другие языки

print(translated.text)
