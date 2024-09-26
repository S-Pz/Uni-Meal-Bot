import responses as responses
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

#The API_KEY is obtaindend in response module

if __name__ =='__main__':

    print('Starting...')
    app = Application.builder().token(responses.API_KEY).build()

    #Commands
    app.add_handler(CommandHandler('iniciar', responses.start_command))
    
    app.add_handler(CommandHandler('sobre', responses.about_command))
    app.add_handler(CommandHandler('ajuda', responses.help_command))
    
    app.add_handler(CommandHandler('almoco', responses.lunch_command))
    app.add_handler(CallbackQueryHandler(responses.lunch_menus))
    
    app.add_handler(CommandHandler('jantar', responses.dinner_command))
    app.add_handler(CallbackQueryHandler(responses.dinner_menus))
    
    #Message
    app.add_handler(MessageHandler(filters.TEXT, responses.handle_message))

    #error
    app.add_error_handler(responses.error)

    #polls the bot
    print('Polling..')
    app.run_polling(poll_interval = 4)
    print('Finished')