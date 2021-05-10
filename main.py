import discord
import os
import random
import datetime 
import timers
import nacl
from replit import db
from Keep_alive import keep_alive
from discord.ext import commands
import youtube_dl

client = commands.Bot(command_prefix="$" , help_command=None)

@client.command()
async def moshi(ctx):
    embed=discord.Embed(title=random.choice(greet), description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def insult(ctx):
    embed=discord.Embed(title=random.choice(insults), description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def daisuki(ctx):
    embed=discord.Embed(title=random.choice(replylove), description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def thoughts(ctx):
    embed=discord.Embed(title="You are special to me", description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def free(ctx):
    embed=discord.Embed(title="For you always", description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def cute(ctx):
    embed=discord.Embed(title="No Doubts here !", description=" ", color=0x5733FF)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="My Commands !", description="Here you go Master hmmmph", color=0xFF0080)
    embed.add_field(name="$cute", value="Cute Reactions", inline=True)
    embed.add_field(name="$moshi", value="Regular Greetings", inline=True)
    embed.add_field(name="$daisuki", value="Type of Bot", inline=True)
    embed.add_field(name="$thoughts", value="Regular thoughts", inline=True)
    embed.add_field(name="$free", value="For those loners out there", inline=True)
    embed.add_field(name="$insultme", value="For those masochists out there", inline=True)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/0f/ce/37/0fce372b50c5939e4e8623282c45f4c4.gif")
    await ctx.send(embed=embed)

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.event 
async def on_ready(): 
  print ('Welcome to the Cult Bois {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sad Weebs"))

newUserDMMessage="Welcome Fellow WEEB"
#Dictionary for response
under = ["Fuc",":)","sad","dead","rona","yaar","unhappy","miserable","depressing","depressed"]

cheers = ["No sad noises allowed","Headpats incoming","Yoshi Yoshi","Cheering Waifu Noises"]

greet = ["Greetings","Howdy","Kon'nichiwa","Yaho","koncha","Hi there","Hello again","Welcome back"]

replylove = ["B-Baka!","Urusai, urusai, urusai!!","BAKA CHI","Hmmmm I like you too you know","Kanchigai suru na! Baka !","Kawaikunee "]

insults =["Do you even have FRIENDS?","If you’re only capable of inhaling air and spitting it back out, then that air conditioner over there is superior to you.","Stop being such a Steph","I came here to laugh at you","Excuse me, but why are you still breathing","Please Die as soon as Possible"]

gifs =["https://64.media.tumblr.com/8c2317f139b7e6e430ae732f57efc102/tumblr_phmkfoYigb1vxhp12_500.jpg","https://static.zerochan.net/Oshino.Shinobu.full.992155.jpg","https://64.media.tumblr.com/8c2317f139b7e6e430ae732f57efc102/tumblr_phmkfoYigb1vxhp12_500.jpg","https://i.pinimg.com/564x/e1/b9/16/e1b9166cbfb152f0462d11bb23b05aae.jpg","https://i.pinimg.com/originals/bf/56/76/bf567654f5aeca953a587d33f976ae17.jpg","https://i.pinimg.com/originals/3b/01/66/3b0166877c77ee667631e5fe661caaab.jpg","https://media2.giphy.com/media/a6pzK009rlCak/200.gif","https://media.tenor.com/images/b153fc302e83eff4988081f40ed710a7/tenor.gif","https://www.icegif.com/wp-content/uploads/anime-icegif-15.gif","https://pa1.narvii.com/6304/dd786318f973e55617fd9bb5507d673d564cafdf_hq.gif","https://cdn2.scratch.mit.edu/get_image/gallery/28272388_170x100.png","https://i.pinimg.com/originals/65/ab/8d/65ab8dccc16162edc54a6f5f60eb4b85.gif","https://i.gifer.com/Y1Kn.gif","http://pa1.narvii.com/7369/5f4560df2997c24a47fd4bed5e4ac799ebd88456r1-320-259_00.gif","https://media.tenor.com/images/99eaa944db640e03c0cd45278d8dbc38/tenor.gif","https://steamuserimages-a.akamaihd.net/ugc/791983956793785237/EF7A8E751BFCF86FE60EC57F58F2EDE760A94242/","https://thumbs.gfycat.com/RashDapperAustralianfurseal-max-1mb.gif"]

if "responding" not in db.keys():
  db["responding"] = True

def updates(newm):
  if "nc" in db.keys():
    cheer = db["nc"]
    cheer.append(newm)
    db ["nc"]  = newm
  else:
    db ["nc"] = [newm]


@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return
  #Bot response based 
  msg = message.content
  if db["responding"]:
    options = cheers
    if "nc" in db.keys():
      options.extend(db["nc"])
    
    if any (word in msg for word in under):
      #await message.channel.send(random.choice(options))
      #await message.channel.send('')
      embed=discord.Embed(title=random.choice(options), description=" ", color=0xFF3357)
      embed.set_image(url="https://64.media.tumblr.com/d689c98881f65023cd720185133d58dc/bb66baf54a3034eb-6e/s400x600/eeca7e5f83cb08aed4ffae089ba5a307ab164932.gif")
      await message.channel.send(embed=embed)
  
  if msg.startswith("!new"):
    newm = msg.split("!new ",1)[1]
    updates(newm)
    #await message.channel.send("New Cheer Added, Thank You")
    #await message.channel.send('')
    embed=discord.Embed(title="New Cheer Added, Thank You", description=" ", color=0xFF3357)
    embed.set_image(url="https://i.pinimg.com/originals/79/09/6b/79096bbc936192cfb40cacf07f6f4802.gif")
    await message.channel.send(embed=embed)
  
  if msg.startswith("!list"):
    nc = []
    if "nc" in db.keys():
      nc = db["nc"]
    await message.channel.send(nc)

  if msg.startswith("!respond"):
    value = msg.split("!respond ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      #await message.channel.send("Waifu is Responding to Sad Weebs .")
      embed=discord.Embed(title="Waifu is Responding to Sad Weebs .", description=" ", color=0x00FF00)
      await message.channel.send(embed=embed)

    else:
      db["responding"] = False
      #await message.channel.send("Waifu is not Responding to Sad Weebs .")
      embed=discord.Embed(title="Waifu is not Responding to Sad Weebs .", description=" ", color=0xFF0000)
      await message.channel.send(embed=embed)

keep_alive()    
client.run(os.getenv('TOKEN'))