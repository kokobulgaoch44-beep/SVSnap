import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    filters
)
from handlers.start import start
from handlers.cv import handle_cv, reset
from handlers.payment import send_invoice, pre_checkout, successful_payment

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CallbackQueryHandler(send_invoice, pattern="^pay$"))
    app.add_handler(PreCheckoutQueryHandler(pre_checkout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_cv))

    print("CVSnap is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
