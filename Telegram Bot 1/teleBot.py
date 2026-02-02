import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
)

# Enable logging (helps you debug errors)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. DEFINING STATES: specific numbers to identify where the user is
CHOOSING_CATEGORY, TYPING_REPLY = range(2)

# --- COMMAND HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the conversation and shows the main menu."""
    
    # Create buttons
    keyboard = [
        [
            InlineKeyboardButton("Tech Support", callback_data='Tech'),
            InlineKeyboardButton("Sales", callback_data='Sales'),
        ],
        [InlineKeyboardButton("Just saying Hi!", callback_data='Greeting')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! What are you contacting us about today?",
        reply_markup=reply_markup
    )
    # Tell the bot we are now in the 'CHOOSING_CATEGORY' state
    return CHOOSING_CATEGORY

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Parses the CallbackQuery (button click) and asks for details."""
    query = update.callback_query
    
    # Must answer the query so the button stops loading
    await query.answer()
    
    # Save the user's choice to their temporary session data
    choice = query.data
    context.user_data['choice'] = choice

    await query.edit_message_text(f"You selected: **{choice}**.\n\nPlease type a short message describing your request.")
    
    # Move to the next state
    return TYPING_REPLY

async def receive_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stores the info and ends the conversation."""
    user_text = update.message.text
    category = context.user_data.get('choice', 'Unknown')

    await update.message.reply_text(
        f"✅ **Ticket Created!**\n\nCategory: {category}\nDetails: {user_text}\n\nType /start to restart."
    )

    # Clear user data and end conversation
    context.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancels and ends the conversation."""
    await update.message.reply_text("Operation cancelled. Type /start to try again.")
    return ConversationHandler.END

# --- MAIN EXECUTION ---

if __name__ == '__main__':
    application = ApplicationBuilder().token("8232520448:AAHFLZsjp7IqVKblaXmR3F3b2L5EunncICY").build()

    # The ConversationHandler holds the logic for the different "States"
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            # State 1: User is looking at buttons
            CHOOSING_CATEGORY: [CallbackQueryHandler(button_click)],
            
            # State 2: User is typing text
            TYPING_REPLY: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_text)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)

    print("Advanced Bot is running...")
    application.run_polling()