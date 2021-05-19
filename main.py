import discord
from features import MusicBot
from decouple import config
from discord.ext import commands

# client = discord.Client()

def main():
    bot = MusicBot()
    bot.run()


if __name__ == "__main__":
    main()


# client.run(config('TOKEN'))
