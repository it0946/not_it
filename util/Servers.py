import json
import discord
from discord.ext import commands
from util.Config import Config

class Servers:
    def __init__(self):
        self.servers: dict = json.load(open('servers.json', 'r'))
        self.config: dict = json.load(open('config.json', 'r'))

    async def server_exists(self, id: int):
        for serverID in self.servers:
            if serverID == id:
                return True

    async def add_server(self, id: int, name: str, prefix: str):
        newServers = self.servers
        newServers[id] = {'name': name, 'server_prefix': prefix}
        with open('servers.json') as file:
            file.write(json.dumps(newServers))

    async def change_prefix(self, id: int, newPrefix: str): # Changed server prefix
        newServers = self.servers
        newServers[str(id)]['server_prefix'] = newPrefix
        with open('servers.json', 'w') as file:
            file.write(json.dumps(newServers)) 

    async def get_prefix(self, message: discord.Message, bot: commands.Bot):
        config = self.config
        servers = self.servers
        prefixes = [f'<@!{self.bot.user.id}> ', f'<@{self.bot.user.id}> ']
        if message.guild is None:
            prefix = config['default_prefix']
        else:
            prefix = servers[id]['server_prefix']
        prefixes.append(prefix)
        return(prefixes)



    async def _get_prefix(self, message: discord.Message):
        if message.guild is None:
            return(self.config['default_prefix'])
        servers = self.servers
        return(servers[str(id)]['server_prefix'])