from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from ai.analyzer import analyze_free

async def handle_cv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not context.user_data.get("cv"):
        context.user_data["cv"] = text
        await update.message.reply_text(
            "✅ CV received!\n\n"
            "💼 Step 2: Now paste the job description or job link 👇"
        )
    else:
        context.user_data["job"] = text
        cv_text = context.user_data["cv"]
        job_text = context.user_data["job"]

        await update.message.reply_text("🔍 Analyzing your CV against this job...\n\nThis takes about 30 seconds ⏳")

        try:
            analysis = await analyze_free(cv_text, job_text)
            keyboard = [[
                InlineKeyboardButton("🔓 Get Full Analysis — $3", callback_data="pay")
            ]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(analysis, reply_markup=reply_markup)
        except Exception as e:
            await update.message.reply_text("⚠️ Something went wrong. Please try again with /start")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "🔄 Reset! Let's start fresh.\n\n"
        "📄 Paste your CV below 👇"
    )
