from pyrogram import Client, Filters
token = "YOUR TOKEN HERE" # הטוקן של הבוט שלכם
user = "YOU USERNAME OR USER ID" # השם משתמש או האידי שלכם
app = Client("licenseBot",
             bot_token=token)


@app.on_message(Filters.private & Filters.command('start'))
def start(_, m):
    m.reply("""
START MESSAGE
    """)


def write(u, i):
  with open("users.txt", "a") as file:
    file.write("{} = {}\n".format(str(u), str(i)))

    
def read():
  with open("users.txt", "r") as file:
    return eval("dict({}".format(', '.join(file.readlines())))
@app.on_message(Filters.private)
def talk(_, m):
    
    write(m.message_id, m.from_user.id)
    if m.from_user.username != user:
        m.forward(user)
    else:
        if not m.reply_to_message:
            m.reply("you must reply to message")
        else:
            try:
                if hasattr(m.reply_to_message.forward_from, "id"):
                    app.send_message(m.reply_to_message.forward_from.id, m.text)
                else:
                    app.send_message(read()[m.reply_to_message.message_id], m.text)
            except Exception as e:
                print(f"{e!r}")


app.run()
