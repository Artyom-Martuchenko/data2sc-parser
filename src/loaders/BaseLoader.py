import json
from abc import ABC, abstractmethod


class BaseLoader(ABC):
    def __init__(self):
        self._info = {}
        self._info['entities'] = {}
        self._info['relations'] = {}
        self._info['triplets'] = []

    @abstractmethod
    def getEntity(self, entity, lang='en'):
        pass

    def getEntities(self, entities, lang='en'):
        for entity in entities:
            self.getEntity(entity, lang=lang)

    def getJson(self):
        return json.dumps(self._info)
