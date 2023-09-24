from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

APP_ID = os.environ.get('APP_ID')
API_HASH = os.environ.get('API_HASH')
SESSION = os.environ.get('SESSION')
FROM = '@Offerzone_deals,@rinkusamra,@telugutechtvdeals,@iamprasadtech,@AMAZINGLOOTSDEALS,@Best_shopping_offers_and_deals '
TO_ = '@ExtraPeBot'
FROM = FROM.split(",")
TO = [TO_]

BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)

@csrf_exempt
def home(request):
    return HttpResponse("Telegram bot is running.")

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(i, event.message)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    BotzHubUser.start()
    print("\nBotzHubUser Is Now Working\n")
    BotzHubUser.run_until_disconnected()