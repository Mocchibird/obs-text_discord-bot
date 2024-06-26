# OBS Text Updater Discord Bot

This Discord bot allows users to update a local text file via a slash command. The updated text file can be used with OBS (Open Broadcaster Software) to display dynamic content on your stream. The bot responds with ephemeral messages, ensuring that command invocations and responses are private to the user who invoked the command.

## Features

- Slash command (`/text`) to update a local text file.
- Ephemeral responses to keep the channel clean.
- Simple configuration with environment variables.

## Prerequisites

- Python 3.8 or higher
- A Discord bot token

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/obs-text-discord-bot.git
    cd obs-text-discord-bot
    ```

2. **Create and activate a Conda environment:**
    ```sh
    conda create --name obs-discord-bot python=3.8
    conda activate obs-discord-bot
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project directory with the following content:**
    ```
    DISCORD_TOKEN=your-discord-bot-token
    FILE_PATH=path/to/your/textfile.txt
    REMOTE_FILE_PATH = /path/to/remote/file.txt

    HOSTNAME = your_remote_host_ip
    USERNAME = your_remote_username
    SSH_KEY_PATH = /path/to/your/private/key
    ```

5. **Enable Privileged Gateway Intents:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Select your application.
   - Navigate to the "Bot" tab.
   - Enable the "MESSAGE CONTENT INTENT".
   - Save changes.

## Usage

1. **Run the bot:**
    To change local files
    ```sh
    python bot.py
    ```

    To change remote files
    ```sh
    python remote_bot.py
    ```
    
2. **Invite the bot to your server:**
   - Generate an invite link from the Discord Developer Portal with the necessary permissions (including slash commands).
   - Open the invite link in your browser and invite the bot to your server.

3. **Invoke the slash command in Discord:**
   - Open Discord and go to a text channel where the bot has access.
   - Type `/text Your desired content here` and press Enter.
   - For example: `/text Hello, OBS! This is a test message.`

## Troubleshooting

- Ensure the bot token and file path are correctly set in the `.env` file.
- Make sure the bot has the necessary permissions and intents enabled in the Discord Developer Portal.
- Check the bot's logs for any error messages and ensure the bot is running.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
