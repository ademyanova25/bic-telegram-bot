from telegram import Bot
import os
from datetime import datetime
import pytz

# Переменные из GitHub Secrets
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Формируем сообщение
moscow_tz = pytz.timezone('Europe/Moscow')
now = datetime.now(moscow_tz).strftime('%H:%M %d.%m.%Y')

message = (
    f"📍 Финал дня ({now} МСК)\n\n"
    "Пройдитесь по чек-листу перед тем как выключиться:\n\n"
    "• Статус по дню — в проектный чат (или в общий, если не на проекте)\n"
    "• Все актуальные файлы — в рабочие папки\n"
    "• Документы и вкладки — закрыты\n"
    "• Формула времени — заполнена\n\n"
    "Если всё сделали — просто отметьтесь реакцией ✅\n"
    "Хорошего вечера!"
)

# Отправляем
bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
