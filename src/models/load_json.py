import json
import os

class JsonService:
    def __init__(self,file):
        self.file = file

    def dump_json(self,data):
        with open (self.file,'w',encoding='utf-8') as f:
            json.dump(data,f,indent=4,ensure_ascii=True)


    def read_json(self):
        if os.path.exists(self.file):
            with open(self.file,'r', encoding='utf-8') as f:
                return json.load(f)
        return []
