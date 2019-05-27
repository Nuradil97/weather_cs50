from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pyowm

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I can determine current weather at city.')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Just type, for example, /weather Astana')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def weather(bot, update, args):
    """Define weather at certain location"""
    owm = pyowm.OWM('c398416382b067a5673a83ac531e5899')
    text_location = "".join(str(x) for x in args)
    observation = owm.weather_at_place(text_location)
    w = observation.get_weather()
    humidity = w.get_humidity()
    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    convert_temp = temp.get('temp')
    convert_wind = wind.get('speed')
    convert_humidity = humidity
    text_temp = str(convert_temp)
    text_wind = str(convert_wind)
    text_humidity = str(convert_humidity)
    update.message.reply_text("Temperature, celsius:")
    update.message.reply_text(text_temp)
    update.message.reply_text("Wind speed, m/s:")
    update.message.reply_text(text_wind)
    update.message.reply_text("Humidity, %:")
    update.message.reply_text(text_humidity) 

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("894357045:AAGeAHYF6hXM4hotwmGQZ_td2cRxYW3gIxY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("weather", weather, pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()