from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import os

TOKEN = os.getenv("8096317036:AAF9OM9mH1czKbjI9SKNj7R4N5-FqN-XSMo")
CHAT_ID = os.getenv("-1002842464332")

bot = Bot(token=TOKEN)
scheduler = BlockingScheduler(timezone=pytz.timezone('Europe/Moscow'))

def send_reminder():
    message = (
        "📍 Финал дня\n\n"
        "Пройдитесь по чек-листу перед тем как выключиться:\n\n"
        "• Статус по дню — в проектный чат (или в общий, если не на проекте)\n"
        "• Все актуальные файлы — в рабочие папки\n"
        "• Документы и вкладки — закрыты\n"
        "• Формула времени — заполнена\n\n"
        "Если всё сделали — просто отметьтесь реакцией ✅\n"
        "Хорошего вечера!"
    )
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')

scheduler.add_job(send_reminder, 'cron', day_of_week='mon-fri', hour=17, minute=30)
print("BIC запущен.")
scheduler.start()
