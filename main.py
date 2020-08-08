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

import bot
import log

client = discord.Client()


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
            await message.channel.send("Pong! :)")\

        if message.content == "!marco":
            await message.channel.send("Polo! :)")

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
