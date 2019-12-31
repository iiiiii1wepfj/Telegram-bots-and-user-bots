from pyrogram import Client, Message, ReplyKeyboardMarkup, KeyboardButton
app = Client(
    'detailsbot',
	bot_token="<bot token>",
	api_id=00, # replace with your api id
	api_hash="<api hash>")


@app.on_message() # handle the message
def leave(_, m: Message):
    if m.chat.type in ['group', 'supergroup']: # check the type of the group
        app.send_photo(
            chat_id=m.from_user.id,
            photo=app.download_media(m.chat.photo.big_file_id)
            if app.download_media(m.chat.photo.big_file_id) else
            'https://imgur.com/BNUuwIT',
            caption=f"""
ID: {m.chat.id};
TITLE: {m.chat.title};
TYPE: {m.chat.type};
COUNT: {len([x.user.id for x in app.iter_chat_members(m.chat.id)])}
""")
        m.chat.leave()
    elif m.chat.type == 'private' and m.text == '/start':
        m.reply(
            """
        היי נעים להכיר! אני אתן לך את כל הפרטים עליך, רק תוסיפו אותי לקבוצה שאתם רוצים לקבל עליה את כל הפרטים ותקבלו!
        רוצים לדעת מה הפרטים שלכם? לחצו "הפרטים שלי"
        רוצים לדעת מה הפרטים של משתמש אחר? העבירו הודעה ממנו פשוט מאד.
        """,
            reply_markup=ReplyKeyboardMarkup([[KeyboardButton('הפרטים שלי')]]))
    if m.text == 'הפרטים שלי':
        photo = app.get_profile_photos(m.from_user.id)
        m.reply_photo(
            photo=photo[0]['file_id'],
            caption=f"""
    ID: {m.from_user.id};
USERNAME: {m.from_user.username if m.from_user.username else "hmm null"};
LAST: {m.from_user.last_online_date};
FIRST NAME: {m.from_user.first_name};
LAST NAME: {m.from_user.last_name if m.from_user.last_name else 'hmm null'};
LANGUAGE: {m.from_user.language_code};
SCAM: {m.from_user.is_scam};
STATUS: {m.from_user.status};
""")
    if m.forward_from:
        photo = app.get_profile_photos(m.forward_from.id)
        m.reply_photo(
            photo=photo[0]['file_id']
            if photo else 'https://imgur.com/BNUuwIT',
            caption=f"""
ID: {m.forward_from.id};
USERNAME: {m.forward_from.username if m.from_user.username else "hmm null"};
LAST: {m.forward_from.last_online_date};
FIRST NAME: {m.forward_from.first_name};
LAST NAME: {m.forward_from.last_name if m.from_user.last_name else 'hmm null'};
LANGUAGE: {m.forward_from.language_code};
SCAM: {m.forward_from.is_scam};
STATUS: {m.forward_from.status};
        """)


app.run()
