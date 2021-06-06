import sys
sys.path.insert(0, "../dep.py")
from log import *
from dep import prefix


async def Start(ctx, args):
    args = args.split(" ")
    del args[0]
    prefix.change(args)
    await ctx.send(Log(f"Prefix changed."))