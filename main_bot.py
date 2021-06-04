import discord.ext 
import os
from discord.ext import commands
from dotenv import load_dotenv
from list_event import get_list_event
from dateutil.parser import parse as dtparse
from datetime import datetime as dt

#initilaise load_dotenv() - loads .env file
load_dotenv()
#Extracting api token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '$')

tmfmt = '%d %B, %H:%M %p'  #time format for the .strftime method
event_dict_list = get_list_event()

@bot.command(name = 'eventstoday')

async def eventstoday(ctx):
    
    for event in event_dict_list:
        datetime = event["datetime"]
        stime = dt.strftime(dtparse(datetime), format=tmfmt)
        html_Link = event["html_link"]
        title_description = event["eventtitle"]
        embed=discord.Embed(title = title_description, url=html_Link, description= stime, colour = 0xf74f18)
        embed.set_thumbnail(url="https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
        await ctx.send(embed=embed)
    





bot.run(TOKEN)