"""
//
//  main.py
//  py-bot-uprm
//
//  Created by Fernando Bermudez on 06/10/2020.
//  Edited by Fernando Bermudez on August 8,2020
//  Copyright © 2020 bermedDev. All rights reserved.

"""


import asyncio
import os
from datetime import datetime
import encrypt_token as et

import discord
import RPS
import bot
import log

client = discord.Client()
guild = client.get_guild(718624993470316554)
_PLAYING = False
battle_cries = {
        731572939434098691 : "https://tenor.com/view/smashbros-lucina-gif-14611011", #Lucina
        731573113325879407 : "https://i.gifer.com/777O.gif", #Wario
        731573203411140679 : "https://tenor.com/view/fox-smash-bros-come-at-me-gif-13203706", #Fox
        731573284474454117 : "https://tenor.com/baz34.gif", #Peach
        731573154467807364 : "https://tenor.com/view/super-smash-bros-for-wii-u-princess-rosalina-luma-rosalina-and-luma-video-game-gif-17524513", #Rosalina
        731573039082373160 : "https://giphy.com/gifs/holmes-professor-chulock-qzDuPFbEYiEVy", #Pikachu
        731572838640910431 : "https://tenor.com/view/zelda-the-legend-of-zelda-link-master-sword-ocarina-of-time-gif-5833491", #Link
        731572994413166723 : "https://tenor.com/view/super-smash-bros-ultimate-zelda-gif-12180489", #Zelda
        718630411093278783 : "https://tenor.com/view/super-smash-brothers-super-smash-bros-nintendo-switch-2018-gif-11303168" #Smash
        }


async def task():
    log.debug(f'[INFO] [Time: {datetime.utcnow()}] Starting.')
    await client.wait_until_ready()
    log.debug(f'[INFO] [Time: {datetime.utcnow()}] Started.')
    while True:
        await asyncio.sleep(1)


def handle_exit():
    log.debug(f"[DEBUG] Handling")
    client.loop.run_until_complete(client.logout())
    for t in asyncio.Task.all_tasks(loop=client.loop):
        if t.done():
            t.exception()
            continue
        t.cancel()
        try:
            client.loop.run_until_complete(
                asyncio.wait_for(t, 5, loop=client.loop))
            t.exception()
        except asyncio.InvalidStateError:
            pass
        except asyncio.TimeoutError:
            pass
        except asyncio.CancelledError:
            pass


while True:
    @client.event
    async def on_message(message : discord.Message):

        if (message.author.bot):
            # Events related to bot response
            return

        log.debug(f'[INFO] [Func: on_message] MessageObj: {message}')

        if message.content == "!ping":
            await message.channel.send("Pong! :)")

        if message.content == "!marco":
            await message.channel.send("Polo! :)")

        if message.content == "!team_gif":

            """
            loop thru al the roles
            if the role matches a certain group, send the cry of that group
            """

            for role in message.author.roles: #goes thru all roles of memeber
                for id, cry in battle_cries.items():
                    if role.id == id:
                        log.debug("[CRY] ACTIVATED GIF")
                        await message.channel.send(battle_cries[id])
                        return
        if message.content == "roles":
            log.debug(message.author.roles)

        if message.content == "!rps":
            global _PLAYING
            if not _PLAYING:
                _PLAYING = True
                await RPS.rockPaperScissors(client,message)
                _PLAYING = False
            else:
                return

        log.debug('[INFO] passed the filter')

        # Created event passed Message object to use for response of bot to discord client




    @client.event
    async def on_message_edit(before: discord.Message, after: discord.Message):
        pass

    @client.event
    async def on_member_join(member: discord.Member):
        pass


    @client.event
    async def on_member_update(before, after):
        pass

    @client.event
    async def on_ready():
        log.debug(f'[DEBUG] Guild Obj: {client.guilds}')
        log.debug('[VERBOSE] On Ready Finished.')

    client.loop.create_task(task())
    try:
        TOKEN = et.cipher_decrypt(bot.readToken(),2020)
        client.loop.run_until_complete(client.start(TOKEN))
    except SystemExit as e:
        log.debug(f'[DEBUG] Error {e}')
        handle_exit()
    except KeyboardInterrupt:
        handle_exit()
        client.loop.close()
        log.debug("[DEBUG] Program ended")
        break

    log.debug("[DEBUG] Bot restarting")
    client = discord.Client(loop=client.loop)
