# miptnews
Telegram channel with MIPT news aggregation. [Join us!](https://t.me/miptnews)

Предложения писать [сюда](https://t.me/okhlopkov) и [сюда](https://t.me/tw3lveth).

# Список источников

https://github.com/fiztehradio/miptnews/blob/master/sources

# Установка на macOS
 
Откройте terminal и введите команды 

```bash
# установить brew - усмтановщик пакетов для macOS
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# установить python3 через brew 
brew install python3
# установить все необходимые пакеты
pip3 install sqlalchemy tqdm feedparser python-telegram-bot
# скачать этот репозиторий
git clone https://github.com/ohld/miptnews
# записать в файл tokens ключи от бота и bit.ly
cd miptnews
cp tokens_template tokens
open tokens
```

# Использование

1. Во время первого запуска запустить

``` bash
python3 create_table.py
```

2. Запустить скрипт, который пробегается по спискам групп в вк, выкачивает последние посты, постит те из них, которых еще нет на канале с периодом в полчаса.

``` bash
python3 load_and_post.py
```
___
_Вдохновлен https://habrahabr.ru/post/302688/_.
