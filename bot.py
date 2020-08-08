"""
//
//  bot.py
//  py-bot-uprm
//
//  Created by Fernando Bermudez on 06/10/2019.
//  Edited by Fernando Bermudez on August 8, 2020
//  Copyright © 2020 bermedDev. All rights reserved.


"""
import discord
import log
import os



_CURRENT_DIR = os.path.dirname(__file__)
_TOKEN_FILE = os.path.join(_CURRENT_DIR, "res", "textfiles", 'token.txt')

_CLIENT_ID_NUM = 741748027542208632
_GUILD_ID_NUM = 718624993470316554


def readToken():
    f = open(os.path.join(_CURRENT_DIR, _TOKEN_FILE), "r")
    lines = f.readlines()
    return lines[0].strip()

