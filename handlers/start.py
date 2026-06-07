from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to CVSnap!\n\n"
        "🚨 75% of CVs are rejected by robots before a human ever sees them.\n\n"
        "Is yours one of them?\n\n"
        "CVSnap uses Claude AI — the only AI proven to flag real gaps instead of polishing them over.\n\n"
        "🔒 Your CV is never stored. Analyzed and deleted instantly.\n"
        "⚡ Results in 30 seconds.\n"
        "💰 Free snapshot. Full fix just $3.\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📄 Step 1: Paste your CV below 👇"
    )
