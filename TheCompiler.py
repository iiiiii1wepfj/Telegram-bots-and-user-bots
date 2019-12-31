from pyrogram import Client, InlineQuery, InlineQueryResultArticle, CallbackQuery, \
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, Filters
from requests import get, post
token =  "YOUR TOKEN HERE"
langs = ','.join([x.split("|")[0].strip() for x in get("https://godbolt.org/api/languages").text.splitlines()[1:]])
app = Client("CompileBot",
             bot_token=token)


@app.on_inline_query()
async def inline(_, i: InlineQuery):
    if i.query == '':
        await i.answer(results=[],
                 switch_pm_text=langs,
                 switch_pm_parameter="langs")
    else:
        req = post("https://godbolt.org/api/compiler/g92/compile", data=i.query)
        await i.answer(results=[
            InlineQueryResultArticle(
                title="Send!",
                input_message_content=InputTextMessageContent(
                    message_text=f"<pre>{req.text.split('.org/', maxsplit=1)[1]}</pre>",
                    parse_mode="html"
                ),
            )
        ])


@app.on_callback_query()
async def compile_(_, c: CallbackQuery):
    print(c)


@app.on_message(Filters.private & Filters.create(lambda _, m: m.text.endswith("langs")))
async def get_langs(_, m):
    await m.reply("**Languages List: \n\n**" + "**" + langs.replace(',', '\n') + "**")
app.run()
