from telegram import Bot
import os
from datetime import datetime
import pytz

# Переменные из GitHub Secrets
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

moscow_tz = pytz.timezone('Europe/Moscow')
now = datetime.now(moscow_tz).strftime('%H:%M %d.%m.%Y')

message = (
    "📍 Перед тем как завершить день, пробегитесь по короткому чек-листу:\n\n"
    "• Обновите статус по задачам — в проектный чат (или в общий, если не на проекте)\n"
    "• Все актуальные файлы — загрузите в рабочие папки\n"
    "• Документы и вкладки — закройте\n"
    "• Формулу времени — не забудьте заполнить\n\n"
    "Если всё на месте — отметьтесь реакцией ✅\n"
    "Спасибо за день! Хорошего вечера 🌙"
)

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
