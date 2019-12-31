from pyrogram import Client, Filters
token = "YOUR TOKEN HERE"
app = Client("licenseBot",
             bot_token=token)


@app.on_message(Filters.private & Filters.command('start'))
def start(_, m):
    m.reply("""
Hi, Welcome, you are in licenses bot,
SALE! global license, for all jetbrains products, and for all the life just in 250$  instead 650$,

contact us here to more details

[official license, forever].

[Manual how to install the license](http://jetbrains.ga)..
    """)


@app.on_message(Filters.private)
def talk(_, m):
    sets = {}
    sets.update({m.message_id: m.from_user.id})
    if m.from_user.username != "TgYonataNew":
        m.forward("TgYonataNew")
    else:
        if not m.reply_to_message:
            m.reply("you must reply to message")
        else:
            try:
                if hasattr(m.reply_to_message.forward_from, "id"):
                    app.send_message(m.reply_to_message.forward_from.id, m.text)
                else:
                    app.send_message(sets[m.reply_to_message.message_id], m.text)
            except Exception as e:
                print(f"{e!r}")


app.run()
