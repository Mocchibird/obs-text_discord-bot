import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FILE_PATH = os.getenv('FILE_PATH')

# Define the intents and enable the message content intent
intents = discord.Intents.default()
intents.message_content = True

# Define the bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()  # Sync the command tree

# Create a slash command
@bot.tree.command(name="text", description="Update the text file")
async def text(interaction: discord.Interaction, content: str):
    try:
        # Overwrite the local text file with the content provided
        with open(FILE_PATH, 'w') as file:
            file.write(content)
        
        # Send an ephemeral response
        await interaction.response.send_message('Text file has been updated.', ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}', ephemeral=True)

# Run the bot
bot.run(TOKEN)
