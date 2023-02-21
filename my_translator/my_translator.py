import requests



URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate' # для POST запроса
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard' # для получения GET запроса
KEY = 'Zjg2MTZlNTMtNjQ3Yy00OTU3LWIyN2QtMWQ0MTFkZjg0MTJiOmUwOTE0ZDY2NTZhZDRmMmU4OTgwOWNkNTM4YzU2ZmFi' # ключ для доступа к API

description = '''Перед началом использования данного словаря, просим Вас ознакомиться со списком возможных переводов!\n 
Ch-Ch, Ch-Ru, De-Ru, El-Ru, En-En, En-Ru, En-Uk, Es-Ru, Fr-Ru, It-Ru, La-Ru, Ru-Ch, Ru-De, Ru-El
Ru-En, Ru-Es, Ru-Fr, Ru-It, Ru-Kk, Ru-Ru, Ru-Uk, Uk-En, Uk-Ru, Uk-Uk\n
Расшифровка аббревиатуры: En - Английский, Ru - Русский, De - Немецкий, It - Итальянский
Fr - Французкий, Es - Испанский, Uk - Украинский, Kk - Казахский, Ch - Китайский
La - Латинский, El - Греческий\n
Более подробную информацию по словарям вы можете получить "https://developers.lingvolive.com/ru-ru/Dictionaries"'''  # описание

languages = {'En': 1033, 'Ru': 1049, 'De': 1031, 'It': 1040, 'Fr': 1036, 'Es': 1034, 'Uk': 1058, 'Kk': 1087, 'Ch': 1028, 'La': 1142, 'El': 1032} # словарь языков и их кодов

headers_auth = {'Authorization': 'Basic ' + KEY}  # заголовки для получения токена
auth = requests.post(URL_AUTH,  headers=headers_auth) # отправка запроса POST с заголовками

if auth.status_code == 200:
    token = auth.text
    print(description)
    print()
    print("Выберите язык:")
    print(*languages.keys())
    language_firs = input('Введите аббревиатура языка: ')
    language_last = input('Введите аббревиатура языка, на который хотите перевести слово: ')

    while True:
        word = input('Введите слово для перевода: ')
        if word:
            headers_translate = {'Authorization': 'Bearer ' + token}
            params = {'text': word,
                      'srcLang': languages[language_firs],
                      'dstLang': languages[language_last]}
            req = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = req.json()
            try:
                print(res['Translation'] ['Translation'])
            except:
                print('Не найдено варианта перевода!')



else:
    print('Error!')
