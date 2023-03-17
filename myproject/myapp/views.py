from asyncore import dispatcher
import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from myapp.models import ButtonCalls

from django.shortcuts import render
from myapp.models import ButtonCalls

TOKEN = 'your_bot_token'

def button(bot, update):
    query = update.callback_query
    button_name = query.data
    user = query.message.chat_id
    ButtonCalls.objects.update_or_create(user=user, button_name=button_name, defaults={'call_count': models.F('call_count') + 1})
    if button_name == 'stupid':
        message = 'Why did the stupid boy wear headphones? Because he wanted to listen to his shoes!'
    elif button_name == 'fat':
        message = 'Why did the fat boy bring a ladder to school? Because he heard the high school was up!'
    else:
        message = 'Why did the dumb boy bring a ladder to the bar? Because he heard the drinks were on the house!'
    bot.edit_message_text(text=message, chat_id=query.message.chat_id, message_id=query.message.message_id)

def start(bot, update):
    keyboard = [[InlineKeyboardButton("Stupid", callback_data='stupid'),
                 InlineKeyboardButton("Fat", callback_data='fat'),
                 InlineKeyboardButton("Dumb", callback_data='dumb')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

@csrf_exempt
def telegram(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        update = telegram.Update.de_json(json_data, Bot)
        dispatcher.process_update(update)
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['POST'])

def user_calls(request):
    users = ButtonCalls.objects.all().values('user__username', 'button_name', 'call_count').order_by('user__username')
    user_counts = {}
    for user in users:
        username = user['user__username']
        button_name = user['button_name']
        call_count = user['call_count']
        if username not in user_counts:
            user_counts[username] = {'stupid': 0, 'fat': 0, 'dumb': 0}
        user_counts[username][button_name] = call_count
    return render(request, 'user_calls.html', {'user_counts': user_counts})