import json
import discord

async def change_prefix(id: int, newPrefix: str): # TODO: adapt to multi server
    servers = json.load(open('servers.json', 'r'))
    newServers = servers
    newServers[str(id)]['server_prefix'] = newPrefix
    with open('servers.json', 'w') as file:
        file.write(json.dumps(newServers)) 

async def server_exists(id):
    servers = json.load(open('servers.json', 'r'))
    for serverID in servers:
        if serverID == str(id):
            return True

async def add_server(id: int, name: str, prefix: str):
    servers = json.load(open('servers.json', 'r'))
    newServers = servers
    newServers[id] = { "name": name, "server_prefix": prefix }
    with open('servers.json', 'w') as file:
        file.write(json.dumps(newServers))

async def get_guild_prefix(id: int):
    servers = json.load(open('servers.json', 'r'))
    return(servers[str(id)]['server_prefix'])

async def get_prefix(bot, msg: discord.Message):
    config = json.load(open('config.json', 'r'))
    prefixes = [f'<@!{bot.user.id}> ', f'<@{bot.user.id}> ']
    if msg.guild is None:
        prefix = config['default_prefix']
    else:
        prefix = await get_guild_prefix(msg.guild.id)
    prefixes.append(prefix)
    return(prefixes)
