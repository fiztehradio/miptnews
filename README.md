# miptnews
Telegram channel with MIPT news aggregation. [Join us!](telegram.me/miptnews)

Предложения писать [автору](telegram.me/okhlopkov).

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

Во время первого запуска запустить

``` bash
python3 create_table.py
```

Запустить скрипт, который пробегается по спискам групп в вк, выкачивает последние посты, постит те из них, которых еще нет на канале.

``` bash
python3 load_and_post.py
```

# Периодичный запуск

Для macOS есть прога: LaunchControl. Позволяет настроить демона, который будет запускать bash-скрипт с выбранной периодичностью. 

___
_Вдохновлен https://habrahabr.ru/post/302688/_.
