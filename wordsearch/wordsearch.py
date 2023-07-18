import discord
from redbot.core import commands

class WordSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if the message is from a bot or from the cog itself to avoid infinite loops
        if message.author.bot or message.author == self.bot.user:
            return

        # Replace 'your_word' with the word you want to search for
        word_to_search = 'your_word'

        # Check if the word is in the message content
        if word_to_search in message.content.lower():
            await message.channel.send(f"Found the word '{word_to_search}' in the message: {message.content}")

    @commands.command()
    async def wordsearch(self, ctx, word: str, limit: int = 100):
        # Check if the word is in the latest messages within the channel
        async for message in ctx.channel.history(limit=limit):
            if word.lower() in message.content.lower():
                await ctx.send(f"Found the word '{word}' in the message: {message.content}")
                return

        # If the word wasn't found in recent messages, search historical messages in the channel
        async for message in ctx.channel.history(limit=None, oldest_first=True):
            if word.lower() in message.content.lower():
                await ctx.send(f"Found the word '{word}' in a historical message: {message.content}")
                return

        await ctx.send(f"The word '{word}' was not found in the messages.")

def setup(bot):
    bot.add_cog(WordSearch(bot))