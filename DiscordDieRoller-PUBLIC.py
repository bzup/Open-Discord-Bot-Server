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
import json
import discord
import typing
from discord.ext import commands
from random import randint

# Disambiguation, for neatness.
client = discord.Client()


def defvals(var):
    a_file = open("scoreboard.json", "r")
    default = json.load(a_file)
    a_file.close()
    return default[str(var)]


# Command Prefix can be changed here.
bot = commands.Bot(command_prefix="/")


@bot.event  # Login message.
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command(name="debug",
             help="Debug info. NERD!")  # Debug command. Is probably redundant but is useful for development.
async def debug(ctx):
    await ctx.send("Logged in as: {0.user}.  In guilds: {0.guilds}. websocket {0.ws}".format(bot))  # Change the format if you are going to use a prefix other than bot.


@bot.command(name="dice", help="Dice roller with dice multiplier that also gives the separate rolls\" values. ")  # Die roller command that returns the sum of a random array and the array itself.
async def dice(ctx, args, multiply: typing.Optional[int] = 1):  # will not return until all three args are given.
    number = [0]
    for x in number:
        number.append(randint(1, int(args)))  # Casting is IMPORTANT!
        if len(number) == int(multiply) + 1:  # This prevents an infinite loop.
            break
        else:
            x = + 1
    await ctx.send(sum(number))  # Remove this if you just want the array, not the sum.
    await ctx.send(number[1:])  # Remove this if you just want the sum, not the array.


@bot.command(name="healthsheet", help="DM\"s only!")
async def healthsheet(ctx, goto: typing.Optional[str] = "pl1", operator: typing.Optional[str] = "=", value: typing.Optional[int] = defvals("pl1")):
    a_file = open("scoreboard.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object[str(goto)] = int(value)
    json.dump(json_object, a_file)

    a_file = open("scoreboard.json", "w")
    if operator == "=":
        json_object[str(goto)] = int(value)
        json.dump(json_object, a_file)
    elif operator == "+":
        json_object[str(goto)] =+ int(value)
        json.dump(json_object, a_file)
    elif operator == "-":
        json_object[str(goto)] =- int(value)
        json.dump(json_object, a_file)
    a_file.close()

    await ctx.send("Player 1 Health: " + str(json_object["pl1"]) + " HP")
    await ctx.send("Player 2 Health: " + str(json_object["pl2"]) + " HP")
    await ctx.send("Player 3 Health: " + str(json_object["pl3"]) + " HP")
    await ctx.send("Player 4 Health: " + str(json_object["pl4"]) + " HP")
    await ctx.send("Player 5 Health: " + str(json_object["pl5"]) + " HP")


@bot.command(name="yeet", help="An easter egg, that you just happened to find.")  # Nothing to see here.
async def yeet(ctx):
    await ctx.send("（╯°□°）╯")


bot.run("")  # Put your bot token here.
