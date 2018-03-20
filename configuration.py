import os
from serializer import Serializer as s

class Configuration():
    def create(self):
        # Create a new default configuration file
        config = {}
        config['opus_libs'] = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
        config['token'] = ""
        config['assert'] = False
        open('configuration.json', 'w+').write(s.toJson(config)).close()

    def get(self):
        # Get contents of configuration file
        if not os.path.isfile('configuration.json'):
            self.create()
        with open('configuration.json') as json_data:
            configuration = s.fromJson(json_data.read())
        return configuration