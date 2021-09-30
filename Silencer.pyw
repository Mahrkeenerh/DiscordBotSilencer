import discord, time, datetime, asyncio
from discord.ext import commands
from discord.utils import get


remind_stuff = []
tasks = []

command_char = "+"
silenced = "Silenced"
divider = "(((|||)))"
master_role = "Master Of Silence"
startTime = 0


bot = commands.Bot(command_prefix = command_char, intents=discord.Intents().all())


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
        if user_substring.lower().strip() in str(member.nick).lower() or user_substring.lower().strip() in str(member).lower():
            memberList.append(member)

    return memberList


# Check if channel exists
def checkChannel(ctx, channel_substring):

    channels = ctx.message.guild.voice_channels

    for channel in channels:
        if channel_substring.lower().strip() in str(channel).lower():
            return channel


# Bot is ready
@bot.event
async def on_ready():

    global startTime, tasks

    startTime = time.time()
    print('Successfully logged in as {0.user}'.format(bot))

    channel = bot.get_channel(766598196511899658)

    if int(datetime.date.today().strftime("%d %m %y").split()[1]) in [11, 12, 1]:
        await channel.send("Ho ho, I'm awake now!")
    else:
        await channel.send("Wasup, I'm awake now!")

    for i in tasks:
        i.cancel()
    
    tasks.append(bot.loop.create_task(remind_loop()))
    tasks.append(bot.loop.create_task(pod_ma()))
    

# Join a voice channel
@bot.command()
async def join(ctx):

    memberList = checkUser(ctx, "Silencer#6477")
    target = get(ctx.message.guild.voice_channels, name=None)
    
    for member in memberList:
        await member.move_to(target)
    
    channel = ctx.author.voice.channel
    await channel.connect()


# Leave voice channel
@bot.command()
async def leave(ctx):

    memberList = checkUser(ctx, "Silencer#6477")
    target = get(ctx.message.guild.voice_channels, name=None)
    
    for member in memberList:
        await member.move_to(target)


# Kill program
@bot.command(description="used to turn bot off", aliases=["kills"])
async def killS(ctx):
    
    if str(ctx.message.author).split("#")[0] == "SMAEL":
        await ctx.send("I will never forget this!\nThat's a lie.")
        await bot.close()


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


# # BANNING CAREFUL SUDO
# @bot.command(description="USE ONLY IF YOU REALLY KNOW WHAT YOU ARE DOING")
# async def ban(ctx, user_substring, sudo):

#     if not check(ctx):
#         return

#     memberList = checkUser(ctx, user_substring)

#     if sudo == "SUDO":
#         await ctx.send("Oh no no no")
#         #for member in ret:
#             #await member.kick()


# Add a role to user
@bot.command(description="used to add a new role to specific user", aliases=["addrole", "AddRole", "Addrole", "ADDROLE"])
async def addRole(ctx, user_substring, role_name):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    role = get(ctx.message.guild.roles, name=role_name)

    if str(ctx.message.author).split("#")[0] == "SMAEL":
        for member in memberList:
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
    
    if str(ctx.message.author).split("#")[0] == "SMAEL":
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
async def move(ctx, user_substring, channel_substring):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    channel = checkChannel(ctx, channel_substring)

    if channel == None:
        await ctx.send(channel_substring + " doesn't exist!")
        return

    for member in memberList:
        if str(ctx.author).split("#")[0] == "SMAEL" or channel.user_limit == 0 or channel.user_limit > len(channel.members):
            try:
                await member.move_to(channel)
            except:
                await ctx.send(str(member) + " is not connected to a channel")


# Move all members to another voice channel
@bot.command(description="used to move all users to another voice channel", aliases=["moveall", "MoveAll", "Moveall", "MOVEALL"])
async def moveAll(ctx, *, channel_substring):

    if not check(ctx):
        return

    channel = checkChannel(ctx, channel_substring)

    if channel == None:
        await ctx.send(channel_substring + " doesn't exist!")
        return

    for member in ctx.author.voice.channel.members:
        if str(ctx.author).split("#")[0] == "SMAEL" or channel.user_limit == 0 or channel.user_limit > len(channel.members):
            await member.move_to(channel)


# Kick member from voice channel
@bot.command(description="used to kick a user from voice channel", aliases=["Kick", "KICK"])
async def kick(ctx, *, user_substring):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)
    target = get(ctx.message.guild.voice_channels, name=None)
    
    for member in memberList:
        await member.move_to(target)


# Kick all members from voice channel
@bot.command(description="used to kick all users from voice channel", aliases=["kickall", "KickAll", "Kickall", "KICKALL"])
async def kickAll(ctx):

    if not check(ctx):
        return
    
    target = get(ctx.message.guild.voice_channels, name=None)
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
async def rename(ctx, user_substring, *, name):

    if not check(ctx):
        return

    memberList = checkUser(ctx, user_substring)

    for member in memberList:
        await member.edit(nick=name)


# Ping
@bot.command(aliases=["Ping", "PING"])
async def ping(ctx):
    
    await ctx.send("Pong! " + str(round(bot.latency * 1000)) + "ms")


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
            await ctx.send("Saved " + tag)


# Read from text file
@bot.command(description="used to get saved blocks", aliases=["Fetch", "FETCH"])
async def fetch(ctx, *, tag):

    global command_char

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
            await ctx.send("Use " + command_char + "saveguard to save a new block")
            await ctx.send("Use " + command_char + "showTags to show saved tags")


# Show saved tags
@bot.command(description="used to get all saved tags", aliases=["showtags", "ShowTags", "Showtags", "SHOWTAGS"])
async def showTags(ctx):

    with open("saves.txt", "r") as file:

        out = "Saved tags:"
        
        for line in file:
            out += "\n" + line.split(divider)[0]
        
        await ctx.send(out)


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


# Create new Reminder
@bot.command(description="used to remind yourself something\n\n\
If setting full date, it must be in format: year:month:day:hour:minute:second\n\
otherwise use number + time unit (d, h, m, s)\n\nExample: remindme message 10h 5m",
             aliases=["remindme", "Remindme", "RemindMe", "REMINDME"])
async def remindMe(ctx, message, *, time):

    global remind_stuff

    time_array = time.strip().lower().split()

    if time_array[0][-1] not in "dhms":
        time = datetime.datetime.strptime(time_array[0], "%Y:%m:%d:%H:%M:%S")
        remind_stuff.append((ctx.channel.id, ctx.author.id, message, time))
        
        save_remind_stuff()
        
        await ctx.send("I will remind you at:" + time.strftime("%Y.%m.%d %H:%M:%S"))
        
    else:
        current_time = datetime.datetime.today()

        days = hours = minutes = seconds = 0

        for time_unit in time_array:

            if "d" in time_unit:
                days = float(time_unit[:-1])
            if "h" in time_unit:
                hours = float(time_unit[:-1])
            if "m" in time_unit:
                minutes = float(time_unit[:-1])
            if "s" in time_unit:
                seconds = float(time_unit[:-1])

        next_time = current_time + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        remind_stuff.append((ctx.channel.id, ctx.author.id, message, next_time))

        save_remind_stuff()

        await ctx.send("I will remind you at: " + next_time.strftime("%Y.%m.%d %H:%M:%S"))


# Load all reminders from file
def load_remind_stuff():

    global remind_stuff, divider

    file = open("remind_stuff", "r", encoding="utf-8")

    remind_stuff = []

    for line in file:
        channel, author, message, time = line.strip().split(divider)
        time = datetime.datetime.strptime(time, "%Y:%m:%d:%H:%M:%S")
        
        remind_stuff.append((int(channel), author, message, time))

    file.close()


# Save reminders to file
def save_remind_stuff():

    global remind_stuff, divider

    file = open("remind_stuff", "w", encoding="utf-8")

    for line in remind_stuff:

        channel, author, message, time = line
        channel = str(channel)
        author = str(author)
        time = time.strftime("%Y:%m:%d:%H:%M:%S")

        print(channel + divider + author + divider + message + divider + time, file=file)

    file.close()


# Remind Me something
async def remind_loop():
    await bot.wait_until_ready()

    global remind_stuff

    load_remind_stuff()

    while not bot.is_closed():

        changed = False

        for remind_piece in remind_stuff:

            if remind_piece[3] < datetime.datetime.today():

                channel = bot.get_channel(remind_piece[0])
                
                await channel.send("<@" + str(remind_piece[1]) + ">")
                await channel.send(remind_piece[2])

                remind_stuff.remove(remind_piece)
                changed = True

        if changed:      
            save_remind_stuff()
        
        await asyncio.sleep(1)


# Remove last message from general
@bot.command(description="DELYNCAK", aliases=["poplast", "Poplast", "PopLast"]) 
async def popLast(ctx, channel_id):

    channel = bot.get_channel(int(channel_id))

    await (await channel.history(limit=1).flatten())[0].delete()


# POD MA
async def pod_ma():

    await bot.wait_until_ready()
    
    channel = bot.get_channel(766598196511899658)

    while not bot.is_closed():

        if datetime.datetime.now().minute == 30:

            await channel.send("Koľko je hodín?")
            await channel.send(datetime.datetime.now().strftime("%H:%M"))
            await channel.send("POĎ MA CICAŤ!")
            await asyncio.sleep(59 * 60)

        await asyncio.sleep(1)


# ERROR HANDLER
@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Neznám: " + str(error))


# Remove extra messages
@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.channel.id != 766598196511899658 and message.channel.id != 762383597973798953 and message.channel.id != 763403142356271114:

        if True in [i.name == "Bots" for i in message.author.roles] or (len(message.content) > 0 and message.content[0] in ".!-+"):
            await asyncio.sleep(1)
            await message.delete()


file = open("secrets.txt", "r")
bot.run(file.readline(), bot=True)
