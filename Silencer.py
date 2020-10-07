import discord
from discord.ext import commands
from discord.utils import get
import random
import webbrowser


bot = commands.Bot(command_prefix = '!')

silenced = "Silenced"
divider = "(((|||)))"
master_role = "Master Of Silence"

# Check if user has Master of Silence role
def check(ctx):

    master = get(ctx.message.guild.roles, name=master_role)
    
    for role in ctx.author.roles:
        if role == master:
            return True
        
    return False


# Print Login message
@bot.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(bot))


# Kill program
@bot.command()
async def killS(ctx):
    
    if check(ctx):
        await bot.close()


# Mute all in channel
@bot.command(description="used to mute all users in a voice channel", aliases=["M"])
async def m(ctx):

    if check(ctx):
        channel = ctx.author.voice.channel
        muted = get(ctx.message.guild.roles, name=silenced)
        
        for member in channel.members:
            await member.add_roles(muted)


# Unmute all in channel
@bot.command(description="used to unmute all users in a voice channel", aliases=["U"])
async def u(ctx):

    if check(ctx):
        channel = ctx.author.voice.channel
        muted = get(ctx.message.guild.roles, name=silenced)
        
        for member in channel.members:
            await member.remove_roles(muted)


# Mute specific user
@bot.command(description="used to mute a specific user", aliases=["Mute", "MUTE"])
async def mute(ctx, member: discord.Member):

    if check(ctx):
        muted = get(ctx.message.guild.roles, name=silenced)
        await member.add_roles(muted)
        

# Unmute specific user
@bot.command(description="used to unmute a specific user", aliases=["Unmute", "UNMUTE"])
async def unmute(ctx, member: discord.Member):

    if check(ctx):
        muted = get(ctx.message.author.guild.roles, name=silenced)
        await member.remove_roles(muted)


# BANNING CAREFUL SUDO
@bot.command(description="USE ONLY IF YOU REALLY KNOW WHAT YOU ARE DOING")
async def ban(ctx, member: discord.Member, sudo):

    if check(ctx) and sudo == "SUDO":
        await member.kick()


# Add a role to user
@bot.command(description="used to add a new role to specific user", aliases=["addrole", "AddRole", "Addrole", "ADDROLE"])
async def addRole(ctx, member: discord.Member, role_name):

    if check(ctx) and str(ctx.message.author).split("#")[0] == "SMAEL":
        role = get(ctx.message.guild.roles, name=role_name)
        await member.add_roles(role)


# Add master role to user
@bot.command(description="used to add the Master Of Silence role to specific user", aliases=["Master", "MASTER"])
async def master(ctx, member: discord.Member):

    if check(ctx) and str(ctx.message.author).split("#")[0] == "SMAEL":
        role = get(ctx.message.guild.roles, name=master_role)
        await member.add_roles(role)


# Remove a role from user
@bot.command(description="used to remove a role from specific user", aliases=["removerole", "RemoveRole", "Removerole", "REMOVEROLE"])
async def removeRole(ctx, member: discord.Member, role_name):

    if check(ctx):
        role = get(ctx.message.author.guild.roles, name=role_name)
        await member.remove_roles(role)


# Rename voice channel
@bot.command(description="used to rename the voice channel user is in", aliases=["renamechannel", "RenameChannel", "Renamechannel", "RENAMECHANNEL"])
async def renameChannel(ctx, new_name):

    if check(ctx):
        channel = ctx.message.author.voice.channel
        await channel.edit(name=new_name)


# Move member to another voice channel
@bot.command(description="used to move a user to another voice channel", aliases=["Move", "MOVE"])
async def move(ctx, member: discord.Member, channel):

    if check(ctx):
        target = get(ctx.message.guild.voice_channels, name=channel)
        await member.move_to(target)


# Vyvetrat
@bot.command(description="used to VYVETRAT SA", aliases=["Vyvetrajsa", "VyvetrajSa", "vyvetrajSa", "VYVETRAJSA"])
async def vyvetrajsa(ctx, member: discord.Member):

    if check(ctx):
        target = get(ctx.message.guild.voice_channels, name="Vetračka")
        await member.move_to(target)
        

# Change nickname of a user
@bot.command(description="used to change the nickname of a user", aliases=["Rename", "RENAME"])
async def rename(ctx, member: discord.Member, name):

    if check(ctx):
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


# Save text to file
@bot.command(description="used to save a block of text", aliases=["Saveguard", "SaveGuard", "SAVEGUARD"])
async def saveguard(ctx, text, tag):

    tag = tag.replace("\n", "   ")
    text = text.replace("\n", "   ")

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
async def fetch(ctx, tag):

    with open("saves.txt", "r") as file:

        exists = False

        for line in file:
            line = line.split(divider)

            if line[0] == tag:
                await ctx.send("Here you go:")
                await ctx.send(line[1])
                exists = True
                
        if not exists:
            await ctx.send("Tag doesn't exist")
            await ctx.send("Use !saveguard to save a new block")


# Show saved tags
@bot.command(description="used to get all saved tags", aliases=["showtags", "ShowTags", "Showtags", "SHOWTAGS"])
async def showTags(ctx):

    with open("saves.txt", "r") as file:

        await ctx.send("Saved tags:")
        
        for line in file:
            await ctx.send(line.split(divider)[0])


# Remove from text file
@bot.command(description="used to remove block from file", aliases=["Erase", "ERASE"])
async def erase(ctx, tag):

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
            
    await bot.process_commands(message)
    
bot.run('NzUzMzY5NDczOTcyNjk5MjE4.X1lL_w.da0llbTo4iww49JZdGSnGceoI6A', bot=True)
