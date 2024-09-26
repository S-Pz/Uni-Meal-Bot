import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from filter import lunch_filter, dinner_filter, response_format, response_format_2
from dotenv import load_dotenv
import datetime
#Load file .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
BOT_USERNAME = os.getenv('BOT_USERNAME')

#commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text('Boas vindas \U0001F60E \U0001F389, para mais informações digite: /ajuda ou /sobre!')
    
async def about_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    head = "Bot idealizado e criado pelos alunos da computação:\n......\nSeu intuito é o de facilitar a visualização dos cardápios." 
    obs = '\n \U0000203C >*OBS:* O bot não se encontra em sua versão final ainda sofrerá bastantes alterações.'
    
    await update.message.reply_text(head + obs, parse_mode='Markdown')

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This command is under construction")

async def lunch_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [
            InlineKeyboardButton("Cap", callback_data='Cap'),
            InlineKeyboardButton("Cco", callback_data='Cco'),
            InlineKeyboardButton("Cdb", callback_data='Cdb'),
            InlineKeyboardButton("Csa", callback_data='Csa'),
            InlineKeyboardButton("Csl", callback_data='Csl'),
            InlineKeyboardButton("Ctan", callback_data='Ctan')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Qual ru deseja consultar o cardápio do almoço ? \U0001F914", reply_markup = reply_markup)

async def lunch_menus(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    choice = query.data
    
    if (choice == 'Cap'):
        try:
            menu:str = '../csv/cap_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'Csl'):
        try:
            menu:str = '../csv/csl_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'Cco'):
        try:
            menu:str = '../csv/cco_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
       
    elif choice == 'Cdb':
        try:
            menu:str = '../csv/cdb_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')            

    elif choice == 'Csa':
        try:
            menu:str = '../csv/csa_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')

    elif choice == 'Ctan':
        try:
            menu:str = '../csv/ctan_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
    else:
        await query.message.reply_text('Selecione uma opção válida. \U0001F605 !', parse_mode = 'Markdown')

async def dinner_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [
            InlineKeyboardButton("Cap", callback_data='Cap'),
            InlineKeyboardButton("Cco", callback_data='Cco'),
            InlineKeyboardButton("Cdb", callback_data='Cdb'),
            InlineKeyboardButton("Csa", callback_data='Csa'),
            InlineKeyboardButton("Csl", callback_data='Csl'),
            InlineKeyboardButton("Ctan", callback_data='Ctan')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Qual ru deseja consultar o cardápio do jantar ? \U0001F914", reply_markup = reply_markup)

async def dinner_menus(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    choice = query.data

    if (choice == 'Cap'):
        try:
            menu:str = '../csv/cap_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'Csl'):
        try:
            menu:str = '../csv/csl_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'Cco'):
        try:
            menu:str = '../csv/cco_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
       
    elif choice == 'Cdb':
        try:
            menu:str = '../csv/cdb_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')            

    elif choice == 'Csa':
        try:
            menu:str = '../csv/csa_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')

    elif choice == 'Ctan':
        try:
            menu:str = '../csv/ctan_menu.csv'
            date:datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
    else:
        await query.message.reply_text('Selecione uma opção válida. \U0001F605 !', parse_mode = 'Markdown')

#responses
def handle_responses(text: str, date) -> str:
    
    processed:str = text.lower()
    
    if ('almoço ctan' in processed)  or ('almoco ctan' in processed):
        try:
            menu = '../csv/ctan_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
    
    elif ('almoço csa' in processed) or ('almoco csa' in processed):
        try:
            menu = '../csv/csa_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cdb' in processed) or ('almoco cdb' in processed):
        try:
            menu = '../csv/cdb_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cco' in processed)or ('almoco cco' in processed):
        try:
            menu = '../csv/cco_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço csl' in processed)or ('almoco csl' in processed):
        try:
            menu = '../csv/csl_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cap' in processed)or ('almoco cap' in processed):
        try:
            menu = '../csv/cap_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
    
    return 'Não entendi a sua mensagem. \U0001F605 !'

#When call this function, pass too the BOT_USERNAME
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message_type = update.message.chat.type
    #print("message_type")
    text: str = update.message.text
    date = update.message.date.today()

    #Debug information
    print(f'User({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':

        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME,'').strip()
            print(new_text)
            response: str = handle_responses(new_text, date)
        else:
            return
    else:
        response: str = handle_responses(text,date)

    #print('Bot', response)
    await update.message.reply_text(response, parse_mode = 'Markdown')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
    #print(f'Update{update} coused error {context.error}')