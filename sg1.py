import random
import discord
from discord.ext import commands, tasks
from discord.utils import find
import datetime
import asyncio
from discord.ext import commands
import os

prefix = "sagi "

client = commands.Bot(command_prefix=[f"{prefix}","Sagi ","SAGI ","SaGi ", "SAGi "])


@client.event
async def on_ready():
    print('Bot is online!')

    @tasks.loop(seconds=10)
    async def link_poster():
    	#await client.sendMessage(client.get_channel('816061932121096252'), 'spam')
        #channel = client.get_channel(815188659979419708)
        #client.fetchUser('816061932121096252', false).then((user) => {user.send('spam');});
        #815188659979419708
        #816061932121096252
        #800380327050608672 ch
        #print(channel)
        channel = "Direct Message with Mitul Agrawal#9655"
        await channel.send("Spam")
        #await client.send_message(channel, 'spam')
    link_poster.start() 	


    @tasks.loop(hours=1)
    async def repo():

        # extracting channel ids to send the articles at this time (minute)
        cur = db.cursor()
        cur.execute("select channel_id from channels where time_to_sec(timediff(curtime(),time)) between 0 and 59")
        channelid = cur.fetchall()

        # sending the repo link randomly with low probability
        for ch_id in channelid:
            channel = client.get_channel(int(ch_id[0]))
            p = randint(1,5000)
            if(p==4001) : await channel.send('Check out our Github Repository :\nhttps://github.com/mathrithms/Finshots-Bot')



client.remove_command('help')

'''async def change_status():
    await client.wait_until_ready()

    activities = ['playing', 'listening', 'watching']

    names = {'playing' : f"on {len(client.guilds)} servers | #help",
             'listening' : "Sunflower (Spider-Man: Into the Spider-Verse)",
             'watching' : "WandaVision"}

    types = {'playing' : discord.ActivityType.playing,
             'listening' : discord.ActivityType.listening,
             'watching' : discord.ActivityType.watching}

    while not client.is_closed():

        activity = random.choice(activities)

        name = names[activity]

        Type = types[activity] 
    
        await client.change_presence(activity=discord.Activity(type=Type, name =name))

        await asyncio.sleep(10)
'''
'''
@client.command(pass_context = True)
async def help(ctx):

	help_name = []
	help_desc = []
	help_name.append("Description")
	help_desc.append("This is a simple bot that can send updates (new articles) from FINSHOTS website to a specified channel in a server or to individual users on their DM at a specified time everyday.")
	help_name.append("hello |or| hi")
	help_desc.append("hello\nGreets You")
	help_name.append("register |or| reg")
	help_desc.append("register #<Channel Name> HH:MM\nSends Finshots Article(s) everyday at the mentioned time to the mentioned channel")
	help_name.append("register_me |or| reg_me")
	help_desc.append("register_me HH:MM\nSends Finshots Article(s) everyday at the mentioned time to your DM")
	help_name.append("set_time")
	help_desc.append("set_time HH:MM\nChange the time of recieving Finshots Article(s) in a channel by sending the command from a registered channel")
	help_name.append("set_my_time")
	help_desc.append("set_my_time HH:MM\nChange the time of recieving Finshots Article(s) in your DM")
	help_name.append("deregister |or| dereg")
	help_desc.append("deregister\nStop recieving Finshots Article(s) in a channel by sending the command from a registered channel")

	embed = discord.Embed(colour = discord.Colour.green())

	for hp in range(len(help_name)) :
	    embed.add_field(name=help_name[hp], value = help_desc[hp], inline = False)

	await ctx.send(embed=embed)
'''
@client.command()
async def sagi(ctx):
	channel_id = ctx.channel.id 
	print(channel_id)
	await ctx.send("Get Ready for Spam")

'''
@client.command(pass_context = True)
async def help_dm(ctx):

	help_name = []
	help_desc = []
	help_name.append("hello |or| hi")
	help_desc.append("hello\n\nGreets You\n-----------------------")
	help_name.append("register |or| reg")
	help_desc.append("register #<Channel Name> HH:MM\n\nSends Finshots Article(s) everyday at the mentioned time to the mentioned channel\n-----------------------")
	help_name.append("register_me |or| reg_me")
	help_desc.append("register_me HH:MM\n\nSends Finshots Article(s) everyday at the mentioned time to your DM\n-----------------------")
	help_name.append("set_time")
	help_desc.append("set_time HH:MM\n\nChange the time of recieving Finshots Article(s) in a channel by sending the command from a registered channel\n-----------------------")
	help_name.append("set_my_time")
	help_desc.append("set_my_time HH:MM\n\nChange the time of recieving Finshots Article(s) in your DM\n-----------------------")
	help_name.append("deregister |or| dereg")
	help_desc.append("deregister\n\nStop recieving Finshots Article(s) in a channel by sending the command from a registered channel\n-----------------------")

	embed = discord.Embed(colour = discord.Colour.green())
	author = ctx.message.author
	embed.set_author(name = 'Help')
	for hp in range(len(help_name)) :
	    embed.add_field(name=help_name[hp], value = help_desc[hp], inline = False)

	await author.send(embed=embed)
	await ctx.send("DM Sent!")

'''


#----------------------------------------------------------------------------------
# help command

'''
@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(description = "This is a simple bot that can send updates (new articles) from FINSHOTS website to a specified channel in a server or to individual users on their DM at a specified time everyday.", colour = discord.Colour.green())
    em.add_field(name = "Help", value = f"Use '{prefix}help <command name>' for extended information of a command.",inline = False)
    em.add_field(name = "Registration", value = "register (alias : reg)\nregister_me (alias : reg_me)", inline = False)
    em.add_field(name = "Change Time", value = "set_time\nset_my_time", inline = False)
    em.add_field(name = "De-Registration", value = "deregister (alias : dereg)\nderegister_me (alias : dereg_me)", inline = False)
    await ctx.send(embed = em)


# subcommands of help command

@help.command(aliases=['reg'])
async def register(ctx):
    em = discord.Embed(title = "register", description = "Sends Finshots Article(s) everyday at the mentioned time to the mentioned channel", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}register #<Channel Name> HH:MM")
    await ctx.send(embed=em)

@help.command(aliases=['reg_me'])
async def register_me(ctx):
    em = discord.Embed(title = "register_me", description = "Sends Finshots Article(s) everyday at the mentioned time to your DM", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}register_me HH:MM")
    await ctx.send(embed=em)

@help.command()
async def set_time(ctx):
    em = discord.Embed(title = "set_time", description = "Change the time of recieving Finshots Article(s) in a channel", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}set_time #<Channel Name> HH:MM")
    await ctx.send(embed=em)
       
@help.command()
async def set_my_time(ctx):
    em = discord.Embed(title = "set_my_time", description = "Change the time of recieving Finshots Article(s) in your DM", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}set_my_time HH:MM")
    await ctx.send(embed=em)

@help.command(aliases=['dereg'])
async def deregister(ctx):
    em = discord.Embed(title = "deregister", description = "Stop recieving Finshots Article(s) in a channel", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}deregister #<Channel Name>")
    await ctx.send(embed=em)   

@help.command(aliases=['dereg_me'])
async def deregister_me(ctx):
    em = discord.Embed(title = "deregister_me", description = "Stop recieving Finshots Article(s) in your DM", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = f"{prefix}deregister_me")
    await ctx.send(embed=em)              

'''
'''
@help.command()
async def ban(ctx):
    em = discord.Embed(title = "ban", description = "bans a member from the guild", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#ban <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title = "unban", description = "unbans a member who was banned from the guild", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#unban <member> ")
    await ctx.send(embed=em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title = "mute", description = "prevents a member from sending messages", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#mute <member> ")
    await ctx.send(embed=em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title = "unmute", description = "unmutes a muted member", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#unmute <member> ")
    await ctx.send(embed=em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title = "clear", description = "deltes the last <n> messages from the channel", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#clear <no. of messages to be deleted>")
    em.add_field(name = "Note", value = "use #clear to delete the last message")
    em.add_field(name = "Also" , value = "you can delete max. 20 messages, bcoz ishaan fixed the upper limit")
    await ctx.send(embed=em)

@help.command()
async def rule(ctx):
    em = discord.Embed(title = "rule", description = "send the rules of the server", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#rule <rule no.> ")
    await ctx.send(embed=em)

@help.command()
async def whois(ctx):
    em = discord.Embed(title = "whois", description = "send the user info of mentioned user", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#whois <member> ")
    await ctx.send(embed=em)

@help.command()
async def poll(ctx):
    em = discord.Embed(title = "poll", description = "sends a poll consisting of two options", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#poll <option 1> or <option 2> ")
    await ctx.send(embed=em)

@help.command()
async def meme(ctx):
    em = discord.Embed(title = "meme", description = "sends a random meme", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#meme")
    await ctx.send(embed=em)

@help.command()
async def hello(ctx):
    em = discord.Embed(title = "hello", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#hello")
    await ctx.send(embed=em)

@help.command()
async def fire(ctx):
    em = discord.Embed(title = "fire", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#fire")
    await ctx.send(embed=em)

@help.command()
async def lol(ctx):
    em = discord.Embed(title = "lol", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#lol")
    await ctx.send(embed=em)

@help.command()
async def lmao(ctx):
    em = discord.Embed(title = "lmao", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#lmao")
    await ctx.send(embed=em)

@help.command()
async def cool(ctx):
    em = discord.Embed(title = "cool", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#cool")
    await ctx.send(embed=em)


#@client.command(pass_context = True)
#async def help_add(ctx,*,s):
#    await ctx.send("Enter Description of Command :")
#    msg=await client.wait_for('message', check=lambda message: message.author == ctx.author)
#    help_desc.append(msg.content)	
#    help_name.append(s)
''' 
@client.group(invoke_without_command = True)
async def help(ctx):

    colours = [discord.Colour.red(),discord.Colour.blue(),discord.Colour.green(),discord.Colour.teal(),discord.Colour.orange()]   
    em = discord.Embed(description = "**FINSHOSTS HELP**\n\n", colour = random.choice(colours))
    em.add_field(name="**Who am I ???**", value="```I am a simple bot that can send updates (new articles) from FINSHOTS website to a specific channel in a server or to individual users on their DM eveyday at the time specified by user.```\n" , inline=False)
    em.add_field(name="**BOT COMMANDS:**  _(can be run in a channel or in DM to the bot)_", value="```prefix : finshots```", inline=False)
    em.add_field(name = "start", value = "```start  Finshots updates in the channel/DM at a specified time\nsyntax :  start HH:MM```", inline=False)
    em.add_field(name = "update_time", value = "```update time of the channel/DM for the Finshots updates\nsyntax :  update_time HH:MM```",  inline=False)
    em.add_field(name = "stop", value = "```stop Finshots updates for the channel/DM\nsyntax :  stop```",  inline=False)
    em.add_field(name = "latest", value = "```sends the articles of the latest date\nsyntax :  latest```",  inline=False)
    await ctx.send(embed = em)

'''
def rep()
    s = ""
    a = random(1,301)
    if(int(a)==250)
        s = "repo link comes here"
        '''

ch_id = 0 

@help.command()
async def start(ctx):
    em = discord.Embed(title = "start", description = "Send the command in a channel to receive Finshots updates there daily\nDM the command to the bot to receive Finshots updates in your DM daily", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "```finshots start HH:MM```")
    await ctx.send(embed=em)  

@help.command()
async def update_time(ctx):
    em = discord.Embed(title = "update_time", description = "Send the command in a registered channel to change the time of receiving Finshots updates there daily\nDM the command to the bot to change the time of receiving Finshots updates in your DM daily", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "```finshots update_time HH:MM```")
    await ctx.send(embed=em)    

@help.command()
async def stop(ctx):
    em = discord.Embed(title = "stop", description = "Send the command in a registered channel to stop receiving Finshots updates there\nDM the command to the bot to stop receiving Finshots updates in your DM", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "```finshots stop```")
    await ctx.send(embed=em) 

@help.command()
async def latest(ctx):
    channel_id = ctx.channel.id 
    print(client.get_channel(int(channel_id)))
    em = discord.Embed(title = "latest", description = "Send the command in a channel or DM the bot to receive articles of the latest date", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "```finshots latest```")
    await ctx.send(embed=em)   
                     

client.run("Nzk5MjIxMzQxMjk4MzYwMzUw.YAAa4A._cTIjmC3LtY2CMNmR2YNjUJdWjI")
    	