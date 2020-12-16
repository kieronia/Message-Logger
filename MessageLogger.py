from discord.ext import commands
import discord
import json
import requests
import asyncio
prefix = "!"
token = "abc.def"
#token here - go in inspect element -> local storage -> filter items -> type token -> control r to reload -> see it and copy it (QUICKLY)
#tokens give access to your account - avoid anyone asking for your token or files that seem to send your token anywhere
#changing your password should reset your token.
webhookurl = "https://discord.com/api/webhooks/123/abc.webhookhere"



client = commands.Bot(prefix, self_bot=True)
@client.event
async def on_connect():
    print(" > Connected - Ready to log!")
@client.event
async def on_message_edit(before, after):
    print(f" > Message Edited, Original Message Content : \n > {before.content}\n Final Message Content \n > {after.content}")
    deleteformat = {
      "embeds": [
        {
          "description": f"Original:\n```{before.content}```\nAfter\n```{after.content}```",
          "color": 15177480,
          "author": {
            "name": "Edited Message Details"
          },
          "footer": {
            "text": f"Message Edited By {before.author.name}#{before.author.discriminator}",
            "icon_url": f"{before.author.avatar_url}"
          }
        }
      ],
      "username": "Message Deleted - github.com/kieronia",
      "avatar_url": "https://media.tenor.com/images/83d6a5ed40a24164dfe1e4e19fad23d9/tenor.gif"
    }
    requests.post(webhookurl,json=deleteformat)
    await client.process_commands(after)

@client.event
async def on_message_delete(message):
    print(f" > Message Deleted, Message Content : \n > {message.content}\n")
    deleteformat = {
      "embeds": [
        {
          "description": f"```{message.content}```",
          "color": 15140872,
          "author": {
            "name": "Deleted Message Content"
          },
          "footer": {
            "text": f"Message Sent By {message.author.name}#{message.author.discriminator}",
            "icon_url": f"{message.author.avatar_url}"
          }
        }
      ],
      "username": "Message Deleted - github.com/kieronia",
      "avatar_url": "https://media.tenor.com/images/83d6a5ed40a24164dfe1e4e19fad23d9/tenor.gif"
    }
    requests.post(webhookurl,json=deleteformat)
    await client.process_commands(message)       
client.run(token, bot=False)
