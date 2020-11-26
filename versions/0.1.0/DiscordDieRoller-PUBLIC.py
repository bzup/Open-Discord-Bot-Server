#  MIT License
#
#  Copyright (c) 2020 Alfred George Taylor
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

# Discord Dice Roller Bot

# Libraries. You will need PIP io install discord.
import discord
from discord.ext import commands
from random import randint

# Disambiguation, for neatness.
client = discord.Client()

# Command Prefix can be changed here.
bot = commands.Bot(command_prefix="/")


@bot.event  # Login message.
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='debug', help='Debug info. NERD!')  # Debug command. Is probably redundant but is useful for development.
async def debug(ctx):
    await ctx.send(' Logged in as: {0.user}.  In guilds: {0.guilds}. websocket {0.ws}'.format(bot))  # Change the format if you are going to use a prefix other than bot.


@bot.command(name='dice', help='Dice roller with dice multiplier that also gives the separate rolls\' values. ')   # Die roller command that returns the sum of a random array and the array itself.
async def dice(ctx, args, multiply):  # will not return until all three args are given.
    number = [0]
    for x in number:
        number.append(randint(1, int(args)))  # Casting is IMPORTANT!
        if len(number) == int(multiply) + 1:  # This prevents an infinite loop.
            break
        else:
            x = + 1
    await ctx.send(sum(number))  # Remove this if you just want the array, not the sum.
    await ctx.send(number[1:])  # Remove this if you just want the sum, not the array.


@bot.command(name='rtd', help='Simplified Die roller command. (Syntax: ctx, args)')  # Only produces one mumber from one arg.
async def rtd(ctx, args):
    number = randint(1, int(args))  # Casting is IMPORTANT!
    await ctx.send(number)

bot.run('')  # Put your bot token here.
