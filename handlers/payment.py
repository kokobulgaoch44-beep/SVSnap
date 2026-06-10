from telegram import Update, LabeledPrice
from telegram.ext import ContextTypes
from ai.analyzer import analyze_paid

async def send_invoice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title="CVSnap Full Analysis",
        description="CV rewritten + ATS killers fixed + keywords + cover letter + killer sentence",
        payload="full_analysis",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice("Full Analysis", 300)]
    )

async def pre_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cv_text = context.user_data.get("cv", "")
    job_text = context.user_data.get("job", "")

    await update.message.reply_text(
        "✅ Payment received!\n\n"
        "🔍 Preparing your full analysis...\n\n"
        "This may take up to 60 seconds ⏳"
    )

    try:
        analysis = await analyze_paid(cv_text, job_text)
        await update.message.reply_text(analysis)
        await update.message.reply_text(
            "━━━━━━━━━━━━━━━━━━━━\n"
            "✅ Done! Good luck with your application!\n\n"
            "Want to analyze another job? Use /start\n"
            "━━━━━━━━━━━━━━━━━━━━"
        )
    except Exception as e:
        await update.message.reply_text("⚠️ Something went wrong. Please contact support.")
