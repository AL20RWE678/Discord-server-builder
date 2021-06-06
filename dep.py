import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.members = True 
Bot = commands.Bot(command_prefix=json.load(open("config.json")).get("prefix"), self_bot=True, intents=intents)

class State:
    def __init__(self):
        self.current_state = None
    def change(self, s):
        self.current_state = s

state = State()

DEBUG = json.load(open("config.json")).get("debug")


class Prefix:
    def __init__(self):
        self.prefix = json.load(open("config.json")).get("prefix")
    def change(self, p):
        self.prefix = p 
        print(p)
        Bot.command_prefix = p

prefix = Prefix()

