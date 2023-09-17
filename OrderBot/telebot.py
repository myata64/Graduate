import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

bot_token = '6428504172:AAGCYRFt1xZn_MzFAlQAVzteEnGbLman8lI'
api_endpoint = 'http://localhost:8000/api/orders/'

async def get_orders(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get(api_endpoint)
        data = response.json()

        orders = data

        chat_id = update.effective_chat.id
        for order in orders:
            text = f"Заказ #{order['id']}\nДата: {order['order_date']}\nСтатус: {order['status']}"
            await context.bot.send_message(chat_id=chat_id, text=text)

    except Exception as e:
        await update.message.reply_text("Произошла ошибка при получении заказов.")
        print(str(e))


if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('start', get_orders)
    application.add_handler(start_handler)

    application.run_polling()