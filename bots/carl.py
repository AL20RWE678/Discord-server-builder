import sys
sys.path.insert(0, "../dep.py")
import webbrowser
from dep import *
import discord
import time



async def Start(ctx, args):
    webbrowser.open("https://carl.gg/invite")
    state.change("member_join bots/carl.py")
    message = await ctx.send("Finding carl .")
    i = 1
    while 1: 
        if i == 4: i = 0
        i+=1
        try:
            if await ctx.guild.fetch_member(235148962103951360) is not None: 
                await message.edit(content="Carl has been added!")
                return
        except:
            pass
        await message.edit(content="Finding carl"+("."*i))
        time.sleep(0.5)