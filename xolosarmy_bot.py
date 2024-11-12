from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests


import requests

# Replace with your Telegram Bot token
telegram_token = 'TG_Token'



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



async def memo_posts(update, context):
    # Set up the GraphQL endpoint and query
    url = "https://graph.cash/graphql"
    query = """
        query ($address: Address!) {
            address (address: $address) {
                profile {
                    posts(newest: true, start: "2030-01-01T00:00:00-00:00") {
                        lock {
                            address
                        }
                        tx {
                            hash
                            seen
                            blocks {
                                block {
                                    hash
                                    timestamp
                                }
                            }
                        }
                        text   
                    }
                }
            }
        }
    """

    # Define the variables with your Bitcoin Cash legacy address
    variables = {
        "address": "BCH_LEGACY_ADDRESS"  # Replace with your BCH legacy address
    }

    # Set up the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request to the GraphQL endpoint
    response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Check if there are any posts in the response data
        posts = data.get("data", {}).get("address", {}).get("profile", {}).get("posts", [])
        if posts:
            latest_post = posts[0]
            post_text = latest_post['text']
            tx_hash = latest_post['tx']['hash']
            timestamp = latest_post['tx']['seen']
            message = f"Latest Memo.cash Post:\n{post_text}\nTx: {tx_hash}\nTimestamp: {timestamp}"
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


