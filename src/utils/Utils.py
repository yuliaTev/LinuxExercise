import json
import os


class Utils:

    @classmethod
    def convert_to_json(self, objectToConvert):
        try:
            jsonification = json.dumps(objectToConvert)
        except TypeError:
            jsonification = json.dumps(objectToConvert.__dict__)
        # and now we can avoid sending "diskObject", etc.
        # however, sending instances here means we must be careful with properties
        return jsonification

    @classmethod
    def produce_command(self, command):
        f = os.popen(command)
        return f.read().strip()
