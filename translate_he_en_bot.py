#!/usr/bin/python3
# -*- coding: utf-8 -*-


from googletrans import Translator
from textblob import TextBlob
import textblob.exceptions
from pyrogram import Client, InlineQueryResultArticle, InputTextMessageContent, Filters
token = "YOUR TOKEN HERE"
app = Client('translatebot',
                bot_token=token) # connect to the bot


@app.on_message(Filters.private) # decorator
def trnslate(_, message): # create function
    if message.text != '/start':
        try:

            text = TextBlob(message.text)
            result = text.detect_language() # automatic identification
            t = message.text
            if result == 'iw':
                trans1 = Translator().translate(t, src=result, dest='en').text
                message.reply(trans1)
            elif result == 'en':
                trans = Translator().translate(t, src=result, dest='he').text
                message.reply(trans) # reply translate
        except BaseException as e:
            print(e)


@app.on_inline_query() #decorator
def answer(client, inline_query): # create function
    try:

        if inline_query.query:  # check what the user is type
            query_ = TextBlob(inline_query.query)
            result_query = query_.detect_language()
            if result_query == 'iw': # result of identification

                text = inline_query.query #query
                trans = Translator().translate(text, src=result_query, dest='en').text #result translator

                inline_query.answer(results=[InlineQueryResultArticle(id='transkate',
                                                                      title=inline_query.query, #title of answer
                                                                      description=trans, #description of answer
                                                                      input_message_content=InputTextMessageContent( #the message
                                                                          f"""**source**: {inline_query.query}\n\n
**translate:** {trans}"""
                                                                      ))] # list, answers for queries

                )

                return client

            elif result_query == 'en': # result of identification

                text = inline_query.query #query
                trans = Translator().translate(text, src=result_query, dest='he').text #result translator

                inline_query.answer(results=[InlineQueryResultArticle(id='transkate',
                                                                      title=inline_query.query,
                                                                      description=trans,
                                                                      input_message_content=InputTextMessageContent(
                                                                          f"""**source**: {inline_query.query}\n\n
**translate:** {trans}"""
                                                                      ))]
                                    # list, answers for queries

                                    )


                return client
    except textblob.exceptions.TranslatorError or Exception: #exceptions
        inline_query.answer(results=[],
                            switch_pm_text="You must enter a min of three characters for identification...", #write minimum 3 characters
                            switch_pm_parameter='start')


app.run() # run
