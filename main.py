import discord
import os
import random
from replit import db
from Keep_alive import keep_alive


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


  msg = message.content
  if db["responding"]:
    options = cheers
    if "nc" in db.keys():
      options.extend(db["nc"])
    
    if any (word in msg for word in under):
      await message.channel.send(random.choice(options))
      await message.channel.send('https://64.media.tumblr.com/d689c98881f65023cd720185133d58dc/bb66baf54a3034eb-6e/s400x600/eeca7e5f83cb08aed4ffae089ba5a307ab164932.gif')
  
  if msg.startswith("$new"):
    newm = msg.split("$new ",1)[1]
    updates(newm)
    await message.channel.send("New Cheer Added, Thank You")
    await message.channel.send('https://i.pinimg.com/originals/79/09/6b/79096bbc936192cfb40cacf07f6f4802.gif')
  
  if msg.startswith("$list"):
    nc = []
    if "nc" in db.keys():
      nc = db["nc"]
    await message.channel.send(nc)

  if msg.startswith("$respond"):
    value = msg.split("$respond ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Waifu is Responding to Sad Weebs .")
    else:
      db["responding"] = False
      await message.channel.send("Waifu is not Responding to Sad Weebs .")

keep_alive()    
client.run(os.getenv('TOKEN'))