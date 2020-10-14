import discord
from discord.ext import commands
from discord.utils import get
import random
import webbrowser
import time
import datetime
import asyncio


bot = commands.Bot(command_prefix = '!')

silenced = "Silenced"
divider = "(((|||)))"
master_role = "Master Of Silence"
startTime = 0



# Check if user has Master of Silence role
def check(ctx):

    master = get(ctx.message.guild.roles, name=master_role)
    
    for role in ctx.author.roles:
        if role == master:
            return True
        
    return False


# Check if a user exists
def checkUser(ctx, user_substring):

    members = ctx.message.guild.members

    memberList = []

    for member in members:
        if user_substring.lower() in str(member.nick).lower() or user_substring.lower() in str(member):
            memberList.append(member)


# Bot is ready
@bot.event
async def on_ready():

    global startTime

    startTime = time.time()
    print('Successfully logged in as {0.user}'.format(bot))

    channel = bot.get_channel(634029765694849027)

    await channel.send("Wasup, I'm awake now!")

    bot.loop.create_task(remindMe())


# Kill program
@bot.command()
async def killS(ctx):
    
    if not check(ctx):
        return

    await bot.close()


# Roles
@bot.command()
async def roles(ctx):
    for role in ctx.message.guild.roles:
        print(role)

    
# Members
@bot.command()
async def users(ctx):
    for member in ctx.message.guild.members:
        print(member)


# Mute all in channel
@bot.command(description="used to mute all users in a voice channel", aliases=["M"])
async def m(ctx):

    if not check(ctx):
        return
    
    muted = get(ctx.message.guild.roles, name=silenced)
        
    for member in ctx.author.voice.channel.members:
        await member.add_roles(muted)


# Unmute all in channel
@bot.command(description="used to unmute all users in a voice channel", aliases=["U"])
async def u(ctx):

    if not check(ctx):
        return
    
    muted = get(ctx.message.guild.roles, name=silenced)
        
    for member in ctx.author.voice.channel.members:
        await member.remove_roles(muted)


# Mute specific user
@bot.command(description="used to mute a specific user", aliases=["Mute", "MUTE"])
async def mute(ctx, *, user_substring):

    if not check(ctx):
        return

    muted = get(ctx.message.guild.roles, name=silenced)

    memberList = checkUser(ctx, user_substring)

    for member in memberList:
        await member.add_roles(muted)


# Unmute specific user
@bot.command(description="used to unmute a specific user", aliases=["Unmute", "UNMUTE"])
async def unmute(ctx, *, user_substring):

    if not check(ctx):
        return
    
    muted = get(ctx.message.author.guild.roles, name=silenced)

    memberList = checkUser(ctx, user_substring)

    for member in memberList:
        await member.remove_roles(muted)


# BANNING CAREFUL SUDO
@bot.command(description="USE ONLY IF YOU REALLY KNOW WHAT YOU ARE DOING")
async def ban(ctx, user_substring, sudo):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)

    if sudo == "SUDO":
        for member in ret:
            await member.kick()


# Add a role to user
@bot.command(description="used to add a new role to specific user", aliases=["addrole", "AddRole", "Addrole", "ADDROLE"])
async def addRole(ctx, member: discord.Member, role_name):

    if not check(ctx):
        return

    if str(ctx.message.author).split("#")[0] == "SMAEL":
        role = get(ctx.message.guild.roles, name=role_name)
        await member.add_roles(role)


# Add master role to user
@bot.command(description="used to add the Master Of Silence role to specific user", aliases=["Master", "MASTER"])
async def master(ctx, *, user_substring):

    if not check(ctx):
        return

    role = get(ctx.message.guild.roles, name=master_role)

    memberList = checkUser(ctx, user_substring)

    for member in memberList:
        await member.add_roles(role)


# Remove a role from user
@bot.command(description="used to remove a role from specific user", aliases=["removerole", "RemoveRole", "Removerole", "REMOVEROLE"])
async def removeRole(ctx, user_substring, role_name):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    role = get(ctx.message.author.guild.roles, name=role_name)

    for member in memberList:
        await member.remove_roles(role)


# Rename voice channel
@bot.command(description="used to rename the voice channel user is in", aliases=["renamechannel", "RenameChannel", "Renamechannel", "RENAMECHANNEL"])
async def renameChannel(ctx, *, new_name):

    if not check(ctx):
        return
    
    channel = ctx.message.author.voice.channel
    await channel.edit(name=new_name)


# Move member to another voice channel
@bot.command(description="used to move a user to another voice channel", aliases=["Move", "MOVE"])
async def move(ctx, user_substring, channel):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    target = get(ctx.message.guild.voice_channels, name=channel)

    for member in memberList:
        await member.move_to(target)


# Move all members to another voice channel
@bot.command(description="used to move all users to another voice channel", aliases=["moveall", "MoveAll", "Moveall", "MOVEALL"])
async def moveAll(ctx, *, channel):

    if not check(ctx):
        return
    
    target = get(ctx.message.guild.voice_channels, name=channel)
    channel = ctx.author.voice.channel

    for member in channel.members:
        await member.move_to(target)


# Kick member from voice channel
@bot.command(description="used to kick a user from voice channel", aliases=["Kick", "KICK"])
async def kick(ctx, *, user_substring):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    target = get(ctx.message.guild.voice_channels, name="NonExistentChannel")

    for member in memberList:
        await member.move_to(target)


# Kick all members from voice channel
@bot.command(description="used to kick all users from voice channel", aliases=["kickall", "KickAll", "Kickall", "KICKALL"])
async def kickAll(ctx):

    if not check(ctx):
        return
    
    target = get(ctx.message.guild.voice_channels, name="NonExistentChannel")
    channel = ctx.author.voice.channel

    for member in channel.members:
        await member.move_to(target)


# Vyvetrat
@bot.command(description="used to VYVETRAT SA", aliases=["vyvetrajsa", "Vyvetrajsa", "VyvetrajSa", "VYVETRAJSA"])
async def vyvetrajSa(ctx, *, user_substring):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    target = get(ctx.message.guild.voice_channels, name="Vetračka")

    for member in memberList:
        await member.move_to(target)


# Change nickname of a user
@bot.command(description="used to change the nickname of a user", aliases=["Rename", "RENAME"])
async def rename(ctx, *, user_substring, name):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)

    for member in memberList:
        await member.edit(nick=name)


# Maths add
@bot.command()
async def add(ctx, num1, num2):
    await ctx.send(num1 + " + " + num2 + " = " + str(int(num1) + int(num2)))


# Maths subtract
@bot.command()
async def subtract(ctx, num1, num2):
    await ctx.send(num1 + " - " + num2 + " = " + str(int(num1) - int(num2)))


# Maths multiply
@bot.command()
async def multiply(ctx, num1, num2):
    await ctx.send(num1 + " * " + num2 + " = " + str(int(num1) * int(num2)))


# Maths divide
@bot.command()
async def divide(ctx, num1, num2):
    await ctx.send(num1 + " : " + num2 + " = " + str(int(num1) / int(num2)))


# CowSay
@bot.command(aliases=["cowsay", "CowSay", "Cowsay", "COWSAY"])
async def cowSay(ctx):
    
    with open("jokes.txt", "r") as jokes:

        ran = random.randrange(170)
        await ctx.send("I ain't no cow you little shit")
        await ctx.send("Here's your joke:")
            
        for line in jokes:
            if ran == 0:
                await ctx.send(line)
                break
            else:
                ran -= 1


# AI
@bot.command(aliases=["AI", "Ai", "aI"])
async def ai(ctx):
    
    await ctx.send("I am smarter than just a regular AI")
    await ctx.send("This response was automatically generated by KohutikAI.org")
    await ctx.send("Beep Boop, I am a bot, don't mind me")


# Ping
@bot.command(aliases=["Ping", "PING"])
async def ping(ctx):
    
    await ctx.send("Pong! " + str(bot.latency) + "ms")


# Uptime
@bot.command(description="used to get the uptime of the bot", aliases=["Uptime", "UPTIME"])
async def uptime(ctx):
    
    global startTime
    currentTime = time.time()
    
    await ctx.send("Uptime: " + str(datetime.timedelta(seconds=round(currentTime - startTime, 0))) + " [hh : mm : ss]")


# Save text to file
@bot.command(description="used to save a block of text", aliases=["Saveguard", "SaveGuard", "SAVEGUARD"])
async def saveguard(ctx, text, tag):

    tag = tag.replace("\n", "   ")
    text = text.replace("\n", "   ")

    if divider in tag or divider in text:
        await ctx.send("Divider " + divider + " can't be used in text or tag.")
        return

    with open("saves.txt", "r+") as file:

        exists = False
        
        for line in file:
            line = line.split(divider)
            
            if line[0] == tag:
                await ctx.send("Tag already exists")
                exists = True
                
        if not exists:
            print(tag + divider + text, file=file)
            await ctx.send("Saved " + text + " as " + tag)


# Read from text file
@bot.command(description="used to get saved blocks", aliases=["Fetch", "FETCH"])
async def fetch(ctx, *, tag):

    with open("saves.txt", "r") as file:

        exists = False

        for line in file:
            line = line.split(divider)

            if line[0] == tag:
                await ctx.send("Here you go " + tag + ":")
                await ctx.send(line[1])
                exists = True
                
        if not exists:
            
            await ctx.send("Tag doesn't exist")
            await ctx.send("Use !saveguard to save a new block")
            await ctx.send("Use !showTags to show saved tags")


# Show saved tags
@bot.command(description="used to get all saved tags", aliases=["showtags", "ShowTags", "Showtags", "SHOWTAGS"])
async def showTags(ctx):

    with open("saves.txt", "r") as file:

        await ctx.send("Saved tags:")
        
        for line in file:
            await ctx.send(line.split(divider)[0])


# Remove from text file
@bot.command(description="used to remove block from file", aliases=["Erase", "ERASE"])
async def erase(ctx, *, tag):

    if not check(ctx):
        return

    with open("saves.txt", "r") as file:
        all_lines = file.readlines()

    with open("saves.txt", "w") as file:

        erased = False
        
        for line in all_lines:
            
            if line.split(divider)[0] != tag:
                print(line, end="", file=file)
                
            else:
                erased = True
                await ctx.send("Removed " + tag + " from saves")
                await ctx.send("Text: " + line.split(divider)[1])

        if not erased:
            await ctx.send("Not such tag is saved")


# GOOOGLE
@bot.command(description="used to Gooooogle", aliases=["Google", "GOOGLE"])
async def google(ctx, *, text):
    temp = str(text).strip().split(" ")
    final = ""

    for i in temp:
            final += "+" + i

    await ctx.send("https://www.google.com/search?q=" + final)


# Hide text
@bot.command(description="used to hide text", aliases=["Hide", "HIDE"])
async def hide(ctx, *, text):

    ran = random.randrange(3)
    
    if ran == 0:
        await ctx.send("||" + text + "|| ||" + len(text) * "$" + "|| ||" + len(text) * "$" + "||")
        
    elif ran == 1:
        await ctx.send("||" + len(text) * "$" + "|| ||" + text + "|| ||" + len(text) * "$" + "||")

    elif ran == 2:
        await ctx.send("||" + len(text) * "$" + "|| ||" + len(text) * "$" + "|| ||" + text + "||")

    await ctx.message.delete()


### Remind Me something
##async def remindMe():
##    await bot.wait_until_ready()
##
##    channel = bot.get_channel(634029765694849027)
##
##    while not bot.is_closed():
##        await channel.send("Hey now")
##        await asyncio.sleep(100)


### ERROR HANDLER
@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Neznám: " + str(error))


# PUUU tsooo
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if str(member) == "Puco#8084":
            channel = bot.get_channel(762278005229092864)
            await channel.send("<@354330847123341312>")
            await channel.send("Pootststso")


# EVENTS (NO COMMAND - NO ! NEEDED)
@bot.event
async def on_message(message):

    # RECURSION JOKE
    if "recursion" in str(message.content).lower():
        
        temp = message.content.strip().split(" ")
        num = int(temp[1])
        
        if num < 5:
            await message.channel.send("Recursion " + str(num + 1))

    # DAD JOKE
    if str(message.author).split("#")[0] != "Silencer":
        
        if "I'm" in message.content:
            temp = message.content.strip().split("I'm ")
            await message.channel.send("HI " + temp[1] + ", I'm DAD")
        
        elif "I am" in message.content:
            temp = message.content.strip().split("I am ")
            await message.channel.send("HI " + temp[1] + ", I am DAD")

    # INTEGRAL
    if str(message.author).split("#")[0] != "Silencer":
        if "integral" in str(message.content).lower():
        
            await message.channel.send("Here you go you lazyass:")
            await message.channel.send("https://www.wolframalpha.com/calculators/integral-calculator/")
            
    # OS SUCKS
    if str(message.author).split("#")[0] != "Silencer":
        for i in range(str(message.content).lower().count("os")):
            
            await message.channel.send("OS sucks")

    # Hele - prd
    if str(message.author).split("#")[0] != "Silencer":
        for i in range(str(message.content).lower().count("hele")):
            
            await message.channel.send("PRD")

    # KOHUTKA SUCKS
    if str(message.author).split("#")[0] != "Silencer":
        for i in range(str(message.content).lower().count("kohut")):

            await message.channel.send("Kohutka sucks")

    # 30
    if str(message.author).split("#")[0] != "Silencer":
        if "30" in str(message.content) or "tridsat" in str(message.content).lower() or "tridsať" in str(message.content).lower():

            await message.channel.send("Poď ma cicať")

    # 31
    if str(message.author).split("#")[0] != "Silencer":
        if "31" in str(message.content) or "tridsatjedna" in str(message.content).lower() or "tridsaťjedna" in str(message.content).lower():

            await message.channel.send("Poď ma cicať zjemna")

    # 33
    if str(message.author).split("#")[0] != "Silencer":
        if "33" in str(message.content) or "tridsattri" in str(message.content).lower() or "tridsaťtri" in str(message.content).lower():

            await message.channel.send("Poď ma cicať ty")
            
    await bot.process_commands(message)


bot.run('NzUzMzY5NDczOTcyNjk5MjE4.X1lL_w.da0llbTo4iww49JZdGSnGceoI6A', bot=True)
