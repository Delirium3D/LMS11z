from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 'TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, который поможет тебе узнать, как правильно цитировать и использовать информацию из интернета в своих работах.\n'
                                    'Ты можешь использовать следующие команды:\n'
                                    '/start - Начать общение с ботом\n'
                                    '/info - Информация о боте\n'
                                    '/cite - Как правильно цитировать интернет-ресурсы\n'
                                    '/stop - Остановить бота')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Этот чат-бот создан студентом Спирин Никита Владимироваич Б9123-09.03.02ПРС.')

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('До свидания! Если у тебя будут вопросы, просто напиши.')

async def cite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Вот как правильно цитировать интернет-ресурсы:\n\n'
                                    '1. Укажите автора (если он известен).\n'
                                    '2. Название статьи или страницы в кавычках.\n'
                                    '3. Название веб-сайта курсивом.\n'
                                    '4. URL страницы.\n'
                                    '5. Дата доступа (когда вы посмотрели эту страницу).\n\n'
                                    'Пример:\n'
                                    'Иванов, И. "Название статьи". *Название сайта*. URL (дата доступа: ДД.ММ.ГГГГ).')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("cite", cite))

    application.run_polling()

if __name__ == '__main__':
    main()
