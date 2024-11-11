from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests


import requests

# Replace with your Telegram Bot token
telegram_token = '7586262330:AAFyJwknzeWph5MjFRzqBhcscM5xJcvScJc'

# Replace with your memo.cash BCH address
bch_address = "1Kq5hxjgyzTow9KTMzBJDuSeW3S2eHpXhx"
url = f"https://memo.cash/api/v1/profile/{bch_address}/posts"



# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the XolosArmy Network Bot! Type /help to see what I can do.")

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    Here are the commands you can use:
    /memo_posts - Share the latest memo from XolosArmy on the BCH blokchain
    /vision - Learn about the XolosArmy Vision
    /home - Get updates on NFT collections
    /XolosRamirez - Learn how to join the XolosArmy Network
    """)


async def memo_posts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bch_address = "1Kq5hxjgyzTow9KTMzBJDuSeW3S2eHpXhx"  # Legacy address
    url = f"https://memo.cash/api/v1/profile/{bch_address}/posts"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        posts_data = response.json()
        if posts_data:
            latest_post = posts_data[0]
            message = f"Latest Memo.cash Post:\n{latest_post['message']}\nTimestamp: {latest_post['time']}"
        else:
            message = "No posts found for this user."
    else:
        message = f"Error retrieving posts: {response.status_code}"
    
    await update.message.reply_text(message)



# Command to Share the Vision Link
async def vision(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🚀 Learn more about the XolosArmy Network Vision here: https://xolosArmy.xyz/#vision")

# Command to Post NFT Updates (custom message for now)
async def home(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🖼️ Check out the latest NFT updates and collections on XolosArmy: https://xolosArmy.xyz/#home")

# Command to Provide Join Information
async def XolosRamirez(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Join the XolosArmy Network today! Learn more about how to get involved here: https://xolosArmy.xyz/#XolosRamirez")

# Initialize the bot and set up command handlers
application = Application.builder().token(telegram_token).build()

# Add handlers for each command

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("memo_posts", memo_posts))
application.add_handler(CommandHandler("vision", vision))
application.add_handler(CommandHandler("home", home))
application.add_handler(CommandHandler("XolosRamirez", XolosRamirez))

# Start the bot
application.run_polling()
print("XolosArmy bot is running...")


