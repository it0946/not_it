import json
#from main import bot # breaks this apparently?

# Misc config functions to do with config.json  

config = json.load(open('config.json', 'r'))
respond_to = config['id']

async def saveConfig(newConfig: dict):
    with open('config.json', 'w') as file:
        file.write(json.dumps(newConfig))

async def id_exists(id: int): # Check if the id exists in the array
        for _id in respond_to:
            if id == _id: 
                return True

async def addid(id: int): # Add an ID to the array
    if not await id_exists(id):
        newConfig = config
        newConfig['id'].append(id)
        await saveConfig(newConfig)

async def change_prefix(newPrefix: str):
    newConfig = config
    newConfig['prefix'] = newPrefix
    await saveConfig(newConfig)

async def delid(id: int): # Remove an ID from the array
    if await id_exists(id):
        newConfig = config
        newConfig['id'].pop(await indexof(id, 'id'))
        await saveConfig(newConfig)

async def indexof(id: int, arg: str): # Get the index of an id in the config
    for i in range(0, len(config[arg])):
        if config[arg][i] == id:
            return i
