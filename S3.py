import random
import discord
from discord import colour
import requests
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import datetime
import json
import openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Color, Fill, Font, colors, Alignment
from openpyxl.cell import Cell
import time

client = commands.Bot(command_prefix=["pls ","Pls ","PLS "])

@client.event
async def on_ready():

    print('Bot is online!')
    

client.run("ODYwNjU5MTUwMjM3MjA0NTQw.YN-dSw.GhfqfeicY01VTCQwFd6T82tHiXY")