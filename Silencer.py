import discord, keyboard, time, asyncio
from discord.ext import commands
from discord.utils import get
from threading import Thread


bot = commands.Bot(command_prefix = '!')

silenced = "Silenced"
channelMaster = discord.channel
roleMaster = discord.guild.Role

@bot.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(bot))

# join voice channel
@bot.command()
async def addS(ctx):
    global channelMaster
    global roleMaster
    
    channel = ctx.author.voice.channel
    channelMaster = channel
    roleMaster = get(ctx.message.author.guild.roles, name=silenced)
    
    await channel.connect()

# leave voice channel
@bot.command()
async def removeS(ctx):
    await ctx.message.guild.voice_client.disconnect()

# end program
@bot.command()
async def killS(ctx):
    await bot.close()

# mute all in channel
@bot.command()
async def m(ctx):
    channel = ctx.author.voice.channel
    muted = get(ctx.message.author.guild.roles, name=silenced)
    for member in channel.members:
        await member.add_roles(muted)

# unmute all in channel
@bot.command()
async def u(ctx):
    channel = ctx.author.voice.channel
    muted = get(ctx.message.author.guild.roles, name=silenced)
    for member in channel.members:
        await member.remove_roles(muted)

# mute specific user
@bot.command()
async def mute(ctx, member: discord.Member):
    muted = get(ctx.message.author.guild.roles, name=silenced)
    await member.add_roles(muted)

# unmute specific user
@bot.command()
async def unmute(ctx, member: discord.Member):
    muted = get(ctx.message.author.guild.roles, name=silenced)
    await member.remove_roles(muted)

# kick test
##@bot.command()
##async def ban(ctx, member: discord.Member):
##    if ctx.member.role == "Admin"
##    await member.kick()

# Add a role
@bot.command()
async def addRole(ctx, member: discord.Member, text):
    void = get(ctx.message.author.guild.roles, name="Void")
    for member_role in ctx.message.author.roles:
        if member_role == void:
            role = get(ctx.message.author.guild.roles, name=text)
            await member.add_roles(role)

# Remove a role
@bot.command()
async def removeRole(ctx, member: discord.Member, text):
    void = get(ctx.message.author.guild.roles, name="Void")
    for member_role in ctx.message.author.roles:
        if member_role == void:
            role = get(ctx.message.author.guild.roles, name=text)
            await member.remove_roles(role)

# Rename Voice channel
@bot.command()
async def renameChannel(ctx, text):
    channel = ctx.message.author.voice.channel
    await channel.edit(name=text)

# Move member
@bot.command()
async def move(ctx, member: discord.Member, text):
    target = discord.utils.get(ctx.message.guild.voice_channels, name=text)
    await member.move_to(target)

# Vyvetrat
@bot.command()
async def vyvetrajsa(ctx, member: discord.Member):
    target = discord.utils.get(ctx.message.guild.voice_channels, name="Vetračka")
    await member.move_to(target)
    
# Change nickname
@bot.command()
async def rename(ctx, member: discord.Member, text):
    await member.edit(nick=text)

# Add maths
@bot.command()
async def add(ctx, num1, num2):
    await ctx.send(num1 + " + " + num2 + " = " + str(int(num1) + int(num2)))

# Subtract maths
@bot.command()
async def subtract(ctx, num1, num2):
    await ctx.send(num1 + " - " + num2 + " = " + str(int(num1) - int(num2)))

# Multiply maths
@bot.command()
async def multiply(ctx, num1, num2):
    await ctx.send(num1 + " * " + num2 + " = " + str(int(num1) * int(num2)))

# Divide maths
@bot.command()
async def divide(ctx, num1, num2):
    await ctx.send(num1 + " : " + num2 + " = " + str(int(num1) / int(num2)))

# Recursion
@bot.command()
async def recursion(ctx, num):
    num = int(num)
    if num < 5:
        await ctx.send("!recursion " + str(num + 1))



##async def muteKey():
##    
##    global channelMaster
##    global roleMaster
##    
##    for member in channelMaster.members:
##        await member.add_roles(roleMaster)
##
##async def keyStart():
##  
##    pressed = False
##    
##    while True:
##        
##        try:
##            
##            if keyboard.is_pressed('2'):
##                if not pressed:
##                    pressed = True
##                    await muteKey()
##
##                    #loop = asyncio.new_event_loop()
##                    #try:
##                    #    loop.run_until_complete(muteKey())
##                    #finally:
##                    #    loop.close()
##                    
##            else:
##                pressed = False
##                
##        except Exception as e:
##            print("EXCEPTION: ", e)
##
##    await asyncio.sleep(2)
##
##def botStart():
##    bot.loop.create_task(keyStart())
bot.run('NzUzMzY5NDczOTcyNjk5MjE4.X1lL_w.da0llbTo4iww49JZdGSnGceoI6A', bot=True)
##
##botStart()
###Thread(target = botStart).start()
###Thread(target = keyStart).start()
