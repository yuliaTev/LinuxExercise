import json
import os


class Utils:

    @classmethod
    def convert_to_json(self, objectToConvert):
        return json.dumps(objectToConvert)

    @classmethod
    def produce_command(self, command):
        f = os.popen(command)
        return f.read()