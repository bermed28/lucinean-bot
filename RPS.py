import discord
from discord import client
from random import randint as randomNumber

weapons = ["paper","scissors","rock"]

#(index+1) % len(list)
async def rockPaperScissors(client : discord.Client, message : discord.Message):
    userWins = 0
    botWins = 0
    while True:
        if userWins == 2 or botWins == 2:
            break

        await message.channel.send("Choose your weapon: rock/paper/scissors")
        response = await client.wait_for("message", check=lambda response_message: response_message.author == message.author)
        if response.content not in weapons:
            await message.channel.send("Choose one of the weapons i told you could use")
            continue
        botChoice = randomNumber(0, 2)
        await message.channel.send(weapons[botChoice])
        index = -1
        for i in range(len(weapons)):
            if response.content == weapons[i]:
                index = i
                break

        if index == (botChoice + 1) % len(weapons):
            userWins += 1
            await message.channel.send(f"{message.author.nick} wins: {userWins}, Bot Wins: {botWins}")
        elif botChoice == (index + 1) % len(weapons):
            botWins += 1
            await message.channel.send(f"{message.author.nick} wins: {userWins}, Bot Wins: {botWins}")
        else:
            await message.channel.send("It was a tie :(")

    if userWins == 2:
        await message.channel.send(f"{message.author.nick} wins!")
    else:
        await message.channel.send(f"I win!")








