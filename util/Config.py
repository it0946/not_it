import json
# Going to turn config.py into a class here

class Config:
    def __init__(self):
        config_file = json.load(open('config.json', 'r'))
        self.default_prefix = config_file['default_prefix']
        self.token = config_file['token']
        self.ids = config_file['id']
    
    async def log_id(id: int): # for on_ready()
        with open('config.json', 'w') as file:
            newFile = file
            newFile['bot'] = id
            file.write(json.dumps(newFile)) 
