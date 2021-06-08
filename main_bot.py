import os
import datetime
import discord.ext
from discord.ext import commands
from dotenv import load_dotenv
from dateutil.parser import parse as dtparse
#imports get_list_event() function from list_event.py
from list_event import get_list_event


#initilaise load_dotenv() - loads .env file
load_dotenv()
#Extracting api token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '$')

TIME_FORMAT1='%H:%M'  #time format for the .strftime method
TIME_FORMAT2='%m/%d/%Y'

#returns upcoming events today
@bot.command(name = 'eventstoday')
# displays upcoming events today
async def eventstoday(ctx,number_events=5):
    start=datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    end=datetime.datetime.utcnow().replace(hour=23, minute=59,
    second=59,microsecond=0).isoformat() + 'Z'
    event_dict_list = get_list_event(number_events,start,end)
    if len(event_dict_list) == 0:
        embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,
        url="https://calendar.google.com/calendar/u/0/r?mode=week")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title = " :calendar_spiral: Upcoming Events Today",
        url="https://calendar.google.com/calendar/u/0/r?mode=week",
        description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
        embed.set_thumbnail(url=
        "https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
        for event in event_dict_list:
            #set variables
            startdatetime = event["start_datetime"]
            enddatetime = event["end_datetime"]
            eventdescription = event["event_desc"]
            stime = datetime.datetime.strftime(dtparse(startdatetime),
            format=TIME_FORMAT1)
            etime = datetime.datetime.strftime(dtparse(enddatetime),
            format=TIME_FORMAT1)
            html_link = event["html_link"]
            title_description = event["eventtitle"]
            #embedding fields
            embed.add_field(name=f'{title_description} from {stime} to {etime}',
            value = f"[{eventdescription}]({html_link})", inline = False)
            embed.set_footer(text=
            f"For {datetime.datetime.strftime(dtparse(startdatetime), format=TIME_FORMAT2)}")
    await ctx.send(embed=embed)

#returns the next days upcoming events
@bot.command(name = 'eventstommorow')
async def eventstommorow(ctx,number_events=5):
    start = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=0,
    minute=0, second=0,microsecond=0).isoformat() + 'Z' # 'Z' indicates UTC time
    end =  datetime.datetime.utcnow().replace(hour=23, minute=59, second=59,
    microsecond=0).isoformat() + 'Z'
    event_dict_list = get_list_event(number_events,start,end)
    if len(event_dict_list) == 0:
        embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,url=
        "https://calendar.google.com/calendar/u/0/r?mode=week")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title = " :calendar_spiral:Upcoming Events Tommorrow",
        url="https://calendar.google.com/calendar/u/0/r?mode=week",
        description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
        embed.set_thumbnail(url=
        "https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
        for event in event_dict_list:
            #set variables
            startdatetime = event["start_datetime"]
            enddatetime = event["end_datetime"]
            eventdescription = event["event_desc"]
            stime = datetime.datetime.strftime(dtparse(startdatetime), format=TIME_FORMAT1)
            etime = datetime.datetime.strftime(dtparse(enddatetime), format=TIME_FORMAT1)
            html_link = event["html_link"]
            title_description = event["eventtitle"]
            #embedding fields
            embed.add_field(name=f'{title_description} from {stime} to {etime}',
            value = f"[{eventdescription}]({html_link})", inline = False)
            embed.set_footer(text =
            f"For {datetime.datetime.strftime(dtparse(startdatetime), format=TIME_FORMAT2)}")
    await ctx.send(embed=embed)
#returns the previous days past events
@bot.command(name = 'eventsyesterday')
async def eventsyesterday(ctx,number_events=5):
    start = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).replace(hour=0,
    minute=0, second=0,microsecond=0).isoformat() + 'Z' # 'Z' indicates UTC time
    end =  datetime.datetime.utcnow().replace(hour=23,
    minute=59, second=59,microsecond=0).isoformat() + 'Z'
    event_dict_list = get_list_event(number_events,start,end)
    if len(event_dict_list) == 0:
        embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,
        url="https://calendar.google.com/calendar/u/0/r?mode=week")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title = " :calendar_spiral:Past Events Yesterday",
        url="https://calendar.google.com/calendar/u/0/r?mode=week",
        description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
        embed.set_thumbnail(url=
        "https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
        for event in event_dict_list:
            #set variables
            startdatetime = event["start_datetime"]
            enddatetime = event["end_datetime"]
            eventdescription = event["event_desc"]
            stime = datetime.datetime.strftime(dtparse(startdatetime), format=TIME_FORMAT1)
            etime = datetime.datetime.strftime(dtparse(enddatetime), format=TIME_FORMAT1)
            html_link = event["html_link"]
            title_description = event["eventtitle"]
            #embedding fields
            embed.add_field(name=f'{title_description} from {stime} to {etime}',
            value = f"[{eventdescription}]({html_link})", inline = False)
            embed.set_footer(text =
            f"For {datetime.datetime.strftime(dtparse(startdatetime), format=TIME_FORMAT2)}")
    await ctx.send(embed=embed)



bot.run(TOKEN)