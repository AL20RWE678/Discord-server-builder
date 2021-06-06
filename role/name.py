import sys
sys.path.insert(0, "../dep.py")
from dep import *
import discord




async def Start(ctx, args):
    args = args.split(" ")
    del args[0]
    role = discord.utils.get(ctx.guild.roles, name=args[1])
    await role.edit(name=args.replace(args.split(" ")[1], ""))