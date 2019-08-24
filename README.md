# Music Bot  

Music Bot is a Python program using the DiscordPy api to run a bot that will respond to commands typed in your Discord server. Some things it can do: 

  - Type a command to get a specific Spotify playlist linked in the chat
  - Give you a randomly selected Spotify playlist 
  - Give you a list of all available commmands 

## Installation

Music Bot requires [DiscordPy](https://github.com/Rapptz/discord.py) to run.

Install the dependencies:

```sh
$ pip install discordpy
```

For additional features wanted to create your own Discord bot, follow the 
link above to see how to install DiscordPy with additional support features. 

##### Note:
If you experience issues with using pip to install DiscordPy do this instead: 
  - In terminal, navigate to the directory you want to install to 
  - Use the following commands: 
```sh
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ pip install -e .
```

## Setup 

##### Create the Bot:
  - If you do not have a Discord server, first create one
  - Go to the Discord [Developer Portal page](https://discordapp.com/developers/applications/)
  - Log in if you aren't, then choose "Create an application"
  - Pick a name, take note of your "Client ID"
  - Under "Application Settings", choose "Add Bot"
  - Choose your bot permissions, at the very least: 
        1. Send Messages
        2. Read Message History
  - Take note of "Permissions Integer"
  - Follow this link: 
        - https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}
        - replacing {CLIENTID} & {PERMISSIONINT} with the values noted before
  - Select your server and approve your bot!

##### Setup the Application:
  - You can add your token by simply adding {YOURTOKEN} to token.txt
  - Or in 'music_bot.py', you can change the line:
```sh
token = open('token.txt', 'r').read()
```
  - to:
```sh
token = '{YOURTOKEN}'
```

All set! That's everything you need to run Music Bot!

## Feedback
Please feel free to leave any feedback on the bot, let me know what kind of bot you 
create, and let me know if you think there are any changes that should be made. 



