# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:05:01 2017

@author: Lenovo
"""

import discord
import requests
import random
import time

boards = ['3', 'a', 'aco', 'adv', 'an', 'asp', 'b', 'bant', 'biz', 'c', 'cgl', 'ck', 'cm', 'co', 'd', 'diy', 'e', 'f', 'fa', 'fit', 'g', 'gd', 'gif', 'h', 'hc', 'his', 'hm', 'hr', 'i', 'ic', 'int', 'jp', 'k', 'lgbt', 'lit', 'm', 'mlp', 'mu', 'n', 'news', 'o', 'out', 'p', 'po', 'pol', 'qa', 'qst', 'r', 'r9k', 's', 's4s', 'sci', 'soc', 'sp', 't', 'tg', 'toy', 'trash', 'trv', 'tv', 'u', 'v', 'vg', 'vip', 'vp', 'vr', 'w', 'wg', 'wsg', 'wsr', 'x', 'y']


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    def ranPic(board, img):
        pictures = []
        r = requests.get("http://a.4cdn.org/{}/catalog.json".format(board))
        r = r.json()
        for page in r:
            for thread in page["threads"]:
                try:
                    if thread["ext"] != ".webm":
                        pictures.append("{}{}" .format(thread["tim"],thread["ext"]))
                    for reply in thread["last_replies"]:
                        try:
                            if reply["ext"] != ".webm":
                                pictures.append("{}{}" .format(reply["tim"],reply["ext"]))
                        except:
                            pass
                except:
                    pass
        pic = random.choice(pictures)
        time.sleep(1)
        return pic

    if message.content.startswith('!ranpic '):
        board = message.content
        board = board.split()
        board = board[-1]
        assert board in boards
        await client.send_message(message.channel, "http://i.4cdn.org/{}/{}".format(board, ranPic(board, False)))
        """else:
            image = ranPic(board, True)
            with open("{}".format(image), "wb") as f:
                f.write(requests.get("http://i.4cdn.org/{}/{}".format(board, ranPic(board, True))).content)
            await client.send_file(message.channel, image)"""


client.run('MzkzMDc0ODAwMzI4OTY2MTQ1.DRwwWg.T957p9hNkYvXC0VYSTWaqWJDPXE')
