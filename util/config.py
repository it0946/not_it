import json

# Misc config functions to do with config.json  

config = json.load(open('config.json', 'r'))
respond_to = config['id']

async def id_exists(id: int): # Check if the id exists in the array
        for _id in respond_to:
            if id == _id: 
                return True

async def addid(id: int): # Add an ID to the array
    if not await id_exists(id):
        newConfig = config
        newConfig['id'].append(id)
        with open('config.json', 'w') as file:
            file.write(json.dumps(newConfig))

async def delid(id: int): # Remove an ID from the array
    if await id_exists(id):
        newConfig = config
        index = await indexof(id)
        newConfig['id'].pop(index)
        with open('config.json', 'w') as file:
            file.write(json.dumps(newConfig))

async def indexof(id: int): # Get the index of an ID for delid()
    for i in range(0, len(config['id'])):
        if config['id'][i] == id:
            return i