# Python_SAK

Python wrapper for the S.A.K. API.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

## Requirements

- Python 3.8 or newer.
- API URL and KEY, from [here](https://t.me/SAKRo_bot).

## Installation

```sh
$ pip install python-sak
```

## Usage

For Example, to search for a youtube video, you can do this

```py
from asyncio import run
from aiohttp import ClientSession
from Python_SAK import SAK


async def main():
    session = ClientSession()
    arq = SAK(api_url, api_key, session)
    results = await arq.youtube("Never gonna give you up")
    videos = results.result[0]
    print(videos)
    await session.close()


run(main())
```

## Documentation

There is no documentation as of now, however, you can take help from the docstrings this way:

```py
from Python_SAK import SAK

print(help(SAK.deezer))
```

## Features as of now [List of APIs]

1. Lyrics
2. Google Translate
3. Youtube
4. Container code execution via piston
5. Reddit
6. Torrent
7. Wallpapers
8. Urban Dictionary
9. Herus AI Chatbot
10. Image Search
11. Wikipedia
12. NSFW Image Classification
13. Natural Language Processing [Spam Prediction]
14. Proxy Scraper
15. The Movie Database [TMDB]
16. Quotly [TELEGRAM]
17. Jiosaavn
18. Pypi Package Search
19. Image Search
20. Autocorrect (spell checker)
21. ASQ: Question-Answering Algorithm
22. SAK Storage, Unlimited file storage (100MB/file)

## Note

1. I'll add more features soon.
2. If you're stuck somewhere, [Pathetic Programmers](https://t.me/SakirBey1) are there to help.


Turkish / Türkçe


# Python_SAK

S.A.K. için Python sarmalayıcı API.


[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)


##Gereksinimler

- Python 3.8 veya daha yenisi.
- API URL'si ve ANAHTAR, [buradan](https://t.me/SAKRo_bot).


## Kurulum

```sh
$ pip install python-sak
```


## Kullanım

Örneğin, bir youtube videosu aramak için bunu yapabilirsiniz.

```py
from asyncio import run
from aiohttp import ClientSession
from Python_SAK import SAK


async def main():
    session = ClientSession()
    arq = SAK(api_url, api_key, session)
    results = await arq.youtube("Never gonna give you up")
    videos = results.result[0]
    print(videos)
    await session.close()


run(main())
```


## Dokümantasyon

Şu an için herhangi bir dokümantasyon yok, ancak dokümanlardan şu şekilde yardım alabilirsiniz:

```py
from Python_SAK import SAK

print(help(SAK.deezer))
```


## Şu an itibariyle özellikler [API Listesi]

1. Şarkı Sözleri
2. Google Çeviri
3. Youtube
4. Konteyner kodunun piston aracılığıyla yürütülmesi
5. Reddit
6. Torrent
7. Duvar Kağıtları
8. Kentsel Sözlük
9. Herus AI Sohbet Robotu
10. Görsel Arama
11. Vikipedi
12. NSFW Görüntü Sınıflandırması
13. Doğal Dil İşleme [Spam Tahmini]
14. Vekil Kazıyıcı
15. Film Veritabanı [TMDB]
16. Alıntı olarak [TELEGRAM]
17. Jiosaavn
18. Pypi Paket Arama
19. Görsel Arama
20. Otomatik Düzeltme (yazım denetleyicisi)
21. ASQ: Soru-Cevaplama Algoritması
22. SAK Depolama, Sınırsız dosya depolama (100MB/dosya)

## Not

1. Yakında daha fazla özellik ekleyeceğim.
2. Bir yerde takılırsanız, [Acıklı Programcılar](https://t.me/SakirBey1) yardıma hazır.
