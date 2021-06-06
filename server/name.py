async def Start(ctx, args):
    await ctx.guild.edit(name=args)