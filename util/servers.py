import json

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
