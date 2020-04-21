import logging
import logging.handlers

from flask import Blueprint

class BaseBlueprint(Blueprint):
    
    def __init__(self, blueprintName, algoType):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        super().__init__(blueprintName, __name__)
        self.__blueprintName = blueprintName
        self.__algoType = algoType
        self.__url = ""
        
        
    @property
    def blueprintName(self):

        return self.__blueprintName

    @blueprintName.setter
    def blueprintName(self, newName) :

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the name of the blueprint cannot be changed from outside the blueprint class")
            
    
    @property
    def algoType(self):

        return self.__algoType

    @algoType.setter
    def algoType(self, newAlgoType) :

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the type of the blueprint's algorithm cannot be changed from outside the blueprint class")
        
    
    @property
    def url(self):

        return self.__url

    @url.setter
    def url(self, newURL) :

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : blueprint URL cannot be changed from outside the blueprint class")
        