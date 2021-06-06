import discord, pyfiglet, json
from discord.ext import commands
import os, importlib.util
from dep import *


TOKEN = json.load(open("./config.json")).get("token")
DELETE_MSG = json.load(open("./config.json")).get("delete_messages")
if DELETE_MSG == None: DELETE_MSG = "no"





async def process_msg(ctx):
    if DELETE_MSG == "yes":
        await ctx.message.delete() 



@Bot.command()
async def format(ctx, *, args):
    await process_msg(ctx)
    print("hi")
    await ctx.channel.send(f"```{pyfiglet.figlet_format(args)}```")

@Bot.command()
async def set(ctx, *, a):
    print(DEBUG)
    if DEBUG != True:
        print("False")
        if a.startswith("../") or (":" in a):
            print("Danger!")
            await ctx.channel.send("You are not allowed to do that!, it could be a unsafe.")
            return
    await process_msg(ctx)
    args = ' '.join(a.split()) #Splits args and gets rid of double spaces.
   #Import the file needed and run the command
    spec = importlib.util.spec_from_file_location(args.split("/ ")[-1]+".py", args.split(" ")[0]+".py") 
    a = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a)
    await a.Start(ctx, args.replace(args.split(" ")[0], ""))

@Bot.command()
async def setup(ctx, *, args):
    await set(ctx, a=args) #The setup function does the same thing as set but with a different name.





i = 0
@Bot.event
async def on_message(msg):
    await Bot.process_commands(msg)
    args = state.current_state
    if state.current_state != None and "member_join" not in state.current_state:
        spec = importlib.util.spec_from_file_location(args.split("/ ")[-1]+".py", args.split(" ")[0]+".py") 
        a = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(a)
        await a.on_state(msg)
#------------Currently doen't work, there's another way to deal with bots.---------------
# @Bot.event
# async def on_member_join(member):
#     _state = state.current_state
#     print(member.name)
#     print("works")
#     if _state != None and "member_join" in _state:
#         _state.replace("member_join ", '')
#         spec = importlib.util.spec_from_file_location(_state.split("/")[-1], _state)
#         a = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(a)
#         await a.on_state(member) 
#------------------------------------------------------

# async def on_command_error(ctx, exp):
    # await ctx.reply(f"` Error: ` `{exp}`")


def main():
    Bot.run(TOKEN, bot=False)

main()