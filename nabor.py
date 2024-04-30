from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я ваш лид-магнит бот. '
        'Чтобы получить специальный промокод, выполните следующие шаги:\n'
        '1. Подпишитесь на наш канал @nurtasbai.\n'
        '2. После подписки вернитесь и напишите команду /check_subscription.\n'
        'Мы проверим вашу подписку и отправим вам ваш уникальный промокод!'
)

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_id = '@nurtasbai'
    try:
        member = await context.bot.get_chat_member(chat_id, user_id)
        if member.status in ['member', 'creator', 'administrator']:
            await update.message.reply_text('Вы уже подписаны на наш канал! Вот ваш промокод: Saturn')
        else:
            await update.message.reply_text('Пожалуйста, подпишитесь на наш канал, чтобы получить промокод.')
    except Exception as e:
        await update.message.reply_text('Произошла ошибка при проверке вашей подписки. Убедитесь, что бот является администратором канала.')

app = ApplicationBuilder().token("6379043032:AAHfMoUIONAVL0UZtYbHdmizBdnnthigR-w").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check_subscription", check_subscription))


app.run_polling()
