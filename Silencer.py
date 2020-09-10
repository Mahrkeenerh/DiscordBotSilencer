import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix = '!')

silenced = "Silenced"

@bot.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(bot))

### send message
##await ctx.send('no')

# join voice channel
@bot.command()
async def addS(ctx):
    channel = ctx.author.voice.channel
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
async def muteAll(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        muted = get(ctx.message.author.guild.roles, name=silenced)
        await member.add_roles(muted)

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

# unmute all in channel
@bot.command()
async def unmuteAll(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        muted = get(ctx.message.author.guild.roles, name=silenced)
        await member.remove_roles(muted)


bot.run('NzUzMzY5NDczOTcyNjk5MjE4.X1lL_w.da0llbTo4iww49JZdGSnGceoI6A', bot=True)
