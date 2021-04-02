import discord
import os
import random
from replit import db


client = discord.Client()


@client.event 
async def on_ready(): 
  print ('Welcome to the Cult Bois {0.user}'.format(client))

newUserDMMessage="Welcome Fellow WEEB"
  
#Public Welcome
@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await client.send_message(member, newUserDMMessage)
    await client.send_message(discord.Object(id='CHANNELID'), 'Welcome!')
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #CHANNEL")

#Mod Leave Announcement
@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    await client.send_message(discord.Object(id='CHANNELID'), '**' + member.mention + '** just left.')
    print("Sent message to #CHANNEL")

under = ["Fuc",":)","sad","rona","yaar","unhappy","miserable","depressing","depressed"]
cheers = ["No sad noises allowed","Headpats incoming","Yoshi Yoshi","Cheering Waifu Noises"]

def updates(newm):
  if "newc" in db.keys():
    cheer = db["newc"]
    cheer.append(newm)
    db ["newc"]  = newm
  else:
    db ["newc"] = [newm]


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('Moshi'):
    await message.channel.send('Hi There!')
    await message.channel.send('https://i.pinimg.com/originals/ba/a3/dd/baa3ddd24a354d10df6d795f012a3370.jpg')

  if message.content.startswith('Daisuki'):
    await message.channel.send('Hmmmm I like you too you know')
    await message.channel.send('https://i.pinimg.com/564x/e1/b9/16/e1b9166cbfb152f0462d11bb23b05aae.jpg')
  
  if message.content.startswith('Thoughts about me'):
    await message.channel.send('You are special to me')
    await message.channel.send('https://images.alphacoders.com/955/955398.jpg')
  
  if message.content.startswith('Are you free ?'):
    await message.channel.send('For you always,')
    await message.channel.send('https://i.pinimg.com/originals/bf/56/76/bf567654f5aeca953a587d33f976ae17.jpg')
  
  if message.content.startswith('Cheer me up'):
    await message.channel.send('Are you feeling okay ?')
    await message.channel.send('https://64.media.tumblr.com/c182421edc6ddb6da00fce23102b10d4/6fef5335e503c26b-e3/s1280x1920/479daa2560445d1036b73b0ac8d0187f6a2c1fa7.jpg')
  
  if message.content.startswith('You are cute'):
    await message.channel.send('What are you saying !')
    await message.channel.send('https://fsa.zobj.net/crop.php?r=KzxXK0CFm5NK6RkuSZOQiKqqtMnnP72mQImXwULeYioZOIFaC7qEMoTuPj2snE2dD3UVwCYosEaY7n2ypSXX5XRW5CzDaMKZx5AhBQtdDlQo3kbX6yx-mVv7SzqzORa5XpI6mNXkWQwKzwFo')
  
  if message.content.startswith('Tell me about yourself'):
    await message.channel.send('Me, just a Waifu ')
    await message.channel.send('https://fsb.zobj.net/crop.php?r=Okk7VFqEN6AgI1QvzW7XyJ88jNjtDDK1_-oNo7mhTqCQ1ASsJuGBj3li2e1M7VC5JXeK2X2Bpt2DMlzf7aeic4gHKpdQCIfBAv5bjkuPqLGNwII44Hwu8vbMXThabDqz1_wZTLZuO-dEKT5b')

  if message.content.startswith('Anything new'):
    await message.channel.send('Not really')
    await message.channel.send('https://i.redd.it/zrk1pr0caj051.jpg')

  msg = message.content
  options = cheers
  if "newc" in db.keys():
    options.extend(db["newc"])
  
  if any (word in msg for word in under):
    await message.channel.send(random.choice(options))
    await message.channel.send('https://thumbs.gfycat.com/CriminalBruisedChinchilla-size_restricted.gif')
  
  if msg.startswith("$new"):
    newm = msg.split("$new ",1)[1]
    updates(newm)
    await message.channel.send("New Cheer Added, Thank You")
    await message.channel.send('https://i.pinimg.com/originals/79/09/6b/79096bbc936192cfb40cacf07f6f4802.gif')
    
client.run(os.getenv('TOKEN'))
