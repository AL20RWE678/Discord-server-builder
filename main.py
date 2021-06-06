import discord, pyfiglet, json
from discord.ext import commands
import os, importlib.util
from dep import *


TOKEN = json.load(open("./config.json")).get("token")
DELETE_MSG = json.load(open("./config.json")).get("delete_messages")
if DELETE_MSG == None: DELETE_MSG = "no"





async def delete_msg(ctx):
    if DELETE_MSG == "yes":
        await ctx.message.delete() 



@Bot.command()
async def set(ctx, *, a):
    if DEBUG != True: #Protection
        print("False")
        if (".." in a) or ('/' in a) or (":" in a):
            await ctx.channel.send("You are not allowed to do that!, it could be a unsafe.")
            return
    await delete_msg(ctx)
    args = ' '.join(a.split()) #Splits args and gets rid of double spaces.
   #Import the file needed and run the command
    spec = importlib.util.spec_from_file_location(args.split("/ ")[-1]+".py", args.split(" ")[0]+".py") 
    a = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a)
    await a.Start(ctx, args.replace(args.split(" ")[0], ""))

@Bot.command()
async def setup(ctx, *, args):
    await set(ctx, a=args) #The setup function does the same thing as set but with a different name.





@Bot.event
async def on_message(msg):
    await Bot.process_commands(msg)
    args = state.current_state
    if state.current_state != None and "member_join" not in state.current_state:
        spec = importlib.util.spec_from_file_location(args.split("/ ")[-1]+".py", args.split(" ")[0]+".py") 
        a = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(a)
        await a.on_state(msg)

async def on_command_error(ctx, exp):
    await ctx.reply(f"` Error: ` `{exp}`")


def main():
    Bot.run(TOKEN, bot=False)
    print("Started . . .")

main()