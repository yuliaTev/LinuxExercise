import json
import os


class Utils:

    def convert_to_json(self, objectToConvert):
        return json.dumps(objectToConvert)

    def produce_command(self, command):
        f = os.popen(command)
        return f.read()