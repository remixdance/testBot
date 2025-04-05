import telebot
import requests

# Token del bot que obtuviste de BotFather
BOT_TOKEN = '7772414887:AAEyGG4TBDwzwImJDx4CN4ZpK3U41u3eQG8'
bot = telebot.TeleBot(BOT_TOKEN)

# Base URL de la API
BASE_API_URL = 'https://admin.paycontent.com.mx/api/v2/user/channel/public/'

@bot.message_handler(commands=['testapi'])
def test_api_command(message):
    # Aquí ponemos un ID de grupo público de ejemplo, reemplázalo con uno real o pasa como parámetro
    public_group_id = '123456789'  # Este es solo un ejemplo
    complete_api_url = f"{BASE_API_URL}{public_group_id}"

    # Especifica explícitamente que esperas recibir JSON
    headers = {'Accept': 'application/json'}

    # Realiza la solicitud GET con las cabeceras
    response = requests.get(complete_api_url, headers=headers)

    # Muestra la respuesta completa en el chat de Telegram
    if response.status_code == 200:
        bot.send_message(message.chat.id, f"API Response: {response.text}")
    else:
        bot.send_message(message.chat.id, f"Failed to fetch API data. Status Code: {response.status_code}, Response: {response.text}")

bot.polling()
