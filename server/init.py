import discord
import sys
sys.path.insert(0, "../log.py")
sys.path.insert(0, "../dep.py")
from log import *
from dep import *


async def Start(ctx, args):
    for cat in ctx.guild.categories:
        try:
            await cat.delete()
        except:
            pass
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass 
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    category = await ctx.guild.create_category(name="Builder_Info")
    channel = await ctx.guild.create_text_channel(f"log", category=category)
    await channel.send(f"<@{ctx.author.id}> | Initialized!, for more info check -> <#{channel.id}>")
    await channel.send(Log(f"Initialized successfully."))
    role = await ctx.guild.create_role(name="Owner")
    perms = discord.Permissions()
    perms.update(administrator=True)
    await role.edit(colour=discord.Colour.gold(), permissions=perms)
    await ctx.message.author.add_roles(role)
    await channel.send(Log("Added") + f"  <@&{role.id}>   `role.`")

async def on_state(msg):
    if msg.content == "yes":
       await msg.reply(f"Tested") 
       state.change(None)
    state.change(None)