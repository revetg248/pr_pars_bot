import re
import requests
from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import const

api_id = 933902
api_hash = (const.api_hash)
phone = (const.phone)
chat = (const.chat)


client = TelegramClient('coma', api_id, api_hash)
client.start()
client.sign_in(phone)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if re.findall(r'(#)', event.raw_text, re.I):
        awesome_re = re.search("(?P<url>#[^\s]+)", event.raw_text).group("url")
        await client.send_message(chat, str(awesome_re))
        await client.send_message('cr1ccc', '⇝ Промокод получен и исполоьзован. Промокод:  ' + str(awesome_re))

client.run_until_disconnected()