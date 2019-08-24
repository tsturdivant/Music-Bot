import discord
import random 

token = open('token.txt', 'r').read()

class MusicClient(discord.Client): 

    async def on_ready(self):
        # show the bot has successfully logged in 
        print(f'We have logged in as {client.user}')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
            # dictionary of available playlists
            playlist_dict = {
                'chill_music': 'https://open.spotify.com/playlist/4KpMlRwFWtanjGyXSSfP14?si=yd1kyth-SJ-APzPM8Wl5fA',
                'bass_music': 'https://open.spotify.com/playlist/41oYAuQ94cZi4Stuub3eau?si=k1Qlx0EsSEW2C4y0GLRTWQ',
                'woodstock': 'https://open.spotify.com/playlist/6Bt59OkgCZI5I2sOK2QHCP?si=LyYZYBw4S9SjoZemws8hkg',
                'chill_indie': 'https://open.spotify.com/playlist/37i9dQZF1DX9B1hu73DioC?si=zPObgpJKSlOSNvabkwxhmQ',
                'heavy_edm': 'https://open.spotify.com/playlist/5qwnSA5mHjw2jmkx5SoobP?si=sjJyo_A_TPmfuYG5TYFmeQ',
                'remix': 'https://open.spotify.com/playlist/1MQ3lmy9Q5KuuuAIZUAtyh?si=TQHNEafWQXmbPdJqGe4_yg',
                'french': 'https://open.spotify.com/playlist/6faSeVoJAExivqOwwB8xF1?si=81oGkX12Q-mUlaBu-l0blw',
                'travis': 'https://open.spotify.com/playlist/3U3Aw4sIfgkHpALb2Grsx8?si=5NX2PU2JQQORNgQzwJ_lOQ',
                'love_the_sound': 'https://open.spotify.com/playlist/51RwKRy8VWcOTpP8kduHBZ?si=75dmJzeBTWKy5HTn13AfOQ',
                'acoustic': 'https://open.spotify.com/playlist/37i9dQZF1DWUNIrSzKgQbP?si=Lyb1LKrVSZePlqDcq_wYAw',
                'rezz_rocks': 'https://open.spotify.com/playlist/7G63BlgNFRvd7aib4KNt2Z?si=UE6XpRLHRNmO5UNhJsBfIw',
                'sad_boy': 'https://open.spotify.com/playlist/4EhSeYgdRi138Ea4x88X2O?si=8MgMryiVRdezzXjGDoASHQ',
                'drum_n_bass': 'https://open.spotify.com/playlist/5MG037sSypV015Ns1U6UwA?si=mcK4hI9eSv2sbs3SJwDmIQ',
                'house': 'https://open.spotify.com/playlist/37i9dQZF1DXa8NOEUWPn9W?si=nhCJXsImQBWI7nXB0o60ww'
            }
            # array of available commands
            command_array = [
                '!chill_music', '!bass_music', '!woodstock', '!chill_indie', '!heavy_edm', '!remix', '!french', 
                '!travis', '!love_the_sound', '!acoustic', '!rezz_rocks', '!sad_boy', '!drum_n_bass', '!house', 
                '!help', '!random'
            ]

            # print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
            if message.author.id == self.user.id: 
                return # prevent the bot from responding to its own messages

            # decision structure to properly respond to commands
            if command_array[0] in message.content:
                await message.channel.send('Chill Playlist: ')
                await message.channel.send(playlist_dict['chill_music'])

            elif command_array[1] in message.content: 
                await message.channel.send('Bass Playlist: ')
                await message.channel.send(playlist_dict['bass_music']),

            elif command_array[2] in message.content:
                await message.channel.send('Woodstock Playlist: ')
                await message.channel.send(playlist_dict['woodstock'])

            elif command_array[3] in message.content: 
                await message.channel.send('Indie Chillout: ') 
                await message.channel.send(playlist_dict['chill_indie'])

            elif command_array[4] in message.content: 
                await message.channel.send('Go Hard: ')
                await message.channel.send(playlist_dict['heavy_edm'])

            elif command_array[5] in message.content: 
                await message.channel.send('Ximer: ') 
                await message.channel.send(playlist_dict['remix'])

            elif command_array[6] in message.content: 
                await message.channel.send('French Pop: ')
                await message.channel.send(playlist_dict['french'])

            elif command_array[7] in message.content: 
                await message.channel.send("Travis's Picks: ")
                await message.channel.send(playlist_dict['travis'])

            elif command_array[8] in message.content: 
                await message.channel.send('Love the Sound:')
                await message.channel.send(playlist_dict['love_the_sound'])

            elif command_array[9] in message.content: 
                await message.channel.send('Acoustic: ')
                await message.channel.send(playlist_dict['acoustic'])

            elif command_array[10] in message.content: 
                await message.channel.send('Rezz Rocks: ') 
                await message.channel.send(playlist_dict['rezz_rocks'])

            elif command_array[11] in message.content: 
                await message.channel.send('Sad Boy: ') 
                await message.channel.send(playlist_dict['sad_boy'])

            elif command_array[12] in message.content: 
                await message.channel.send('Drum-n-Bass: ') 
                await message.channel.send(playlist_dict['drum_n_bass'])

            elif command_array[13] in message.content: 
                await message.channel.send('House Music: ') 
                await message.channel.send(playlist_dict['house'])
            
            elif command_array[14] in message.content: 
                await message.channel.send('The commands you can type are: ') 
                for command in command_array: 
                    await message.channel.send(command)
                await message.channel.send('Copy and paste one into the chat!')

            elif command_array[15] in message.content: 
                await message.channel.send('Here is a random playlist: ')
                await message.channel.send(random.choice(list(playlist_dict.values())))

client = MusicClient()            
client.run(token)