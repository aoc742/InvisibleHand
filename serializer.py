import json

class Serializer:
    def toJson(s):
        return json.dumps(s, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)

    def fromJson(serialized):
        return json.loads(serialized)