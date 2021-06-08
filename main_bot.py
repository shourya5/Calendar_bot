import discord.ext 
import os
from discord.ext import commands
from dotenv import load_dotenv
from list_event import get_list_event
from dateutil.parser import parse as dtparse
import datetime

#initilaise load_dotenv() - loads .env file
load_dotenv()
#Extracting api token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '$')

tmfmt1 = '%H:%M'  #time format for the .strftime method
tmfmt2 = '%m/%d/%Y'


@bot.command(name = 'eventstoday')

async def eventstoday(ctx,number_events=5):
     
        S_tart = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        E_nd =  datetime.datetime.utcnow().replace(hour=23, minute=59, second=59,microsecond=0).isoformat() + 'Z'
        event_dict_list = get_list_event(number_events,S_tart,E_nd)
        if len(event_dict_list) == 0:
            embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,url="https://calendar.google.com/calendar/u/0/r?mode=week")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title = f" :calendar_spiral: Upcoming Events", 
            url="https://calendar.google.com/calendar/u/0/r?mode=week", 
            description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
            embed.set_thumbnail(url="https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
            for event in event_dict_list:
                #set variables
                startdatetime = event["start_datetime"]
                enddatetime = event["end_datetime"]
                eventdescription = event["event_desc"]
                stime = datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt1)
                etime = datetime.datetime.strftime(dtparse(enddatetime), format=tmfmt1)
                html_Link = event["html_link"]
                title_description = event["eventtitle"]
                #embedding fields
                embed.add_field(name=f'{title_description} from {stime} to {etime}', 
                value = f"[{eventdescription}]({html_Link})", inline = False)
                embed.set_footer(text = f"For {datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt2)}")
                
            await ctx.send(embed=embed)

@bot.command(name = 'eventstommorow')
async def eventstommorow(ctx,number_events=5):
        
    
    
        S_tart = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0,microsecond=0).isoformat() + 'Z' # 'Z' indicates UTC time
        E_nd =  datetime.datetime.utcnow().replace(hour=23, minute=59, second=59,microsecond=0).isoformat() + 'Z'
        event_dict_list = get_list_event(number_events,S_tart,E_nd)
        if len(event_dict_list) == 0:
            embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,url="https://calendar.google.com/calendar/u/0/r?mode=week")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title = f" :calendar_spiral: Events Tommorrow", 
            url="https://calendar.google.com/calendar/u/0/r?mode=week", 
            description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
            embed.set_thumbnail(url="https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
            for event in event_dict_list:
                #set variables
                startdatetime = event["start_datetime"]
                enddatetime = event["end_datetime"]
                eventdescription = event["event_desc"]
                stime = datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt1)
                etime = datetime.datetime.strftime(dtparse(enddatetime), format=tmfmt1)
                html_Link = event["html_link"]
                title_description = event["eventtitle"]
                #embedding fields
                embed.add_field(name=f'{title_description} from {stime} to {etime}', 
                value = f"[{eventdescription}]({html_Link})", inline = False)
                embed.set_footer(text = f"For {datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt2)}")
                
            await ctx.send(embed=embed)
@bot.command(name = 'eventsyesterday')
async def eventsyesterday(ctx,number_events=5):
        
    
        S_tart = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0,microsecond=0).isoformat() + 'Z' # 'Z' indicates UTC time
        E_nd =  datetime.datetime.utcnow().replace(hour=23, minute=59, second=59,microsecond=0).isoformat() + 'Z'
        event_dict_list = get_list_event(number_events,S_tart,E_nd)
        if len(event_dict_list) == 0:
            embed=discord.Embed(title = "No Events Found", colour = 0xf74f18,url="https://calendar.google.com/calendar/u/0/r?mode=week")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title = f" :calendar_spiral: Events Tommorrow", 
            url="https://calendar.google.com/calendar/u/0/r?mode=week", 
            description= f'for upto {len(event_dict_list)} events ', colour = 0xf74f18)
            embed.set_thumbnail(url="https://img.icons8.com/fluent/48/000000/google-calendar--v2.png")
            for event in event_dict_list:
                #set variables
                startdatetime = event["start_datetime"]
                enddatetime = event["end_datetime"]
                eventdescription = event["event_desc"]
                stime = datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt1)
                etime = datetime.datetime.strftime(dtparse(enddatetime), format=tmfmt1)
                html_Link = event["html_link"]
                title_description = event["eventtitle"]
                #embedding fields
                embed.add_field(name=f'{title_description} from {stime} to {etime}', 
                value = f"[{eventdescription}]({html_Link})", inline = False)
                embed.set_footer(text = f"For {datetime.datetime.strftime(dtparse(startdatetime), format=tmfmt2)}")
                
            await ctx.send(embed=embed)



bot.run(TOKEN)