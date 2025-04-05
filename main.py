import telebot

# Token del bot de Telegram
TOKEN = '7772414887:AAEyGG4TBDwzwImJDx4CN4ZpK3U41u3eQG8'
bot = telebot.TeleBot(TOKEN)

# Función para comprobar si un usuario es administrador
def is_user_admin(chat_id, user_id):
    admin_status = ['creator', 'administrator']  # Roles considerados como administradores
    admins = bot.get_chat_administrators(chat_id)
    return any(admin.user.id == user_id and admin.status in admin_status for admin in admins)

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    chat = message.chat
    if chat.type in ['group', 'supergroup']:  # Solo proceder en grupos
        if is_user_admin(chat.id, user.id):
            response = (
                f"Hola {user.first_name} ({user.username if user.username else 'sin username'}), aquí está tu información:\n"
                f"- Tu ID de usuario de Telegram es: {user.id}\n"
                f"- Este chat es un '{chat.type}' con ID: {chat.id} y nombre: {chat.title}\n"
            )
            bot.send_message(chat.id, response)  # Enviar mensaje solo visible en el grupo
        else:
            bot.send_message(user.id, "Lo siento, no tienes permisos de administrador para ejecutar este comando.")
    else:
        bot.send_message(user.id, "Este comando solo se puede usar en grupos.")

# Función para ejecutar el bot
def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()
