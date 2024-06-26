import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import paramiko

# Load environment variables from .env file
load_dotenv()

# Get the bot token and SSH details from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
HOSTNAME = os.getenv('HOSTNAME')
USERNAME = os.getenv('USERNAME')
SSH_KEY = os.getenv('SSH_KEY_PATH')
REMOTE_FILE_PATH = os.getenv('REMOTE_FILE_PATH')

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

# Function to write content to a remote file via SSH
def write_to_remote_file(content: str):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=HOSTNAME, username=USERNAME, key_filename=SSH_KEY)
    
    sftp = ssh.open_sftp()
    with sftp.file(REMOTE_FILE_PATH, 'w') as remote_file:
        remote_file.write(content)
    sftp.close()
    ssh.close()

# Create a slash command
@bot.tree.command(name="text", description="Update the remote text file")
async def text(interaction: discord.Interaction, content: str):
    try:
        # Write the content to the remote file
        write_to_remote_file(content)
        
        # Send an ephemeral response
        await interaction.response.send_message('Remote text file has been updated.', ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}', ephemeral=True)

# Run the bot
bot.run(TOKEN)