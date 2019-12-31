 # Telegram-bots-and-user-bots


codes to create telegram bots  user bot, the bots created by [jonatan](https://t.me/yonibee) with [pyrogram](https://github.com/pyrogram/pyrogram) library.

[link to pyrogram docs](https://docs.pyrogram.ml/start/Usage)
# to use you need install libraries:

```bash
$ pip install pyrogram
```

```bash
$ pip install TgCrypto
```


This is a basic library that is required for all of my codes.

There is a files, to use them you need to install libraries, [firsts line is xxx import, you need install xxx if not on the computer]

>### to get `api_id` and `api_hash` you need:
I think you should use an

[telegram create new app](https://my.telegram.org/auth)

you need create app , after this, you get api_id and api_hash


#### using example:
```python
 from pyrogram import Client
  
 bot = Client(session_name='session_name', 

 api_id=0,

 api_hash=""
 
 )
 
```

[if you create bot [not a ~~userbot~~] add this: ```bot_token=```]

```python
@app.on_message()
def pyrogram(client, message):
    bot.send_message(message.chat.id,
                      'mine first code')
bot.run()
```
