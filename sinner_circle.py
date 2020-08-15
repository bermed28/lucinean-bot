import discord, log

circle = []
async def sinnerCircle(message : discord.Message):

    if "profanidad" in message.content:
        log.debug("[SC] ENTERED SINNER CIRCLE")
        circle.append(message.content.split("dijo")[0])
        await message.channel.send("A person has been added to the sinner circle")
        await message.channel.send(f"People in Sinner Circle: {len(circle)}")

