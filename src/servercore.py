"""Main server module. This class manages the homepage and loads all the 
blueprints (one encryption method = one blueprint)"""

import logging
import logging.handlers

from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

from aes_blueprint import AESBlueprint
from blowfish_blueprint import BlowfishBlueprint
from caesarcipher_blueprint import CaesarCipherBlueprint
from des_blueprint import DESBlueprint
from enigmam3_blueprint import EnigmaM3Blueprint
from md5_blueprint import MD5Blueprint
from rsa_blueprint import RSABlueprint
from sha_blueprint import SHABlueprint
from vigenerecipher_blueprint import VigenereCipherBlueprint

class ServerCore:
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.app = Flask(__name__)
        self.app.add_url_rule("/", "index", self.index)
        
        self.allAlgos = []
        self.historicalAlgos = []
        self.outdatedAlgos = []
        self.modernAlgos = []
        self.hashingAlgos = []
        
        self.loadBlueprints()
    
    def loadBlueprints(self):
        
        """Each encryption method has its own blueprint. All the different
        blueprints must be loaded here"""
        
        self.aes = AESBlueprint()
        self.app.register_blueprint(self.aes)
        self.modernAlgos.append(self.aes.blueprintName)
        self.logger.debug("Blueprint added: " + self.aes.blueprintName + ". Algorithm type: " + self.aes.algoType)
        
        self.blowfish = BlowfishBlueprint()
        self.app.register_blueprint(self.blowfish)
        self.modernAlgos.append(self.blowfish.blueprintName)
        self.logger.debug("Blueprint added: " + self.blowfish.blueprintName + ". Algorithm type: " + self.blowfish.algoType)
        
        self.caesarCipher = CaesarCipherBlueprint()
        self.app.register_blueprint(self.caesarCipher)
        self.historicalAlgos.append(self.caesarCipher.blueprintName)
        self.logger.debug("Blueprint added: " + self.caesarCipher.blueprintName + ". Algorithm type: " + self.caesarCipher.algoType)
        
        self.des = DESBlueprint()
        self.app.register_blueprint(self.des)
        self.outdatedAlgos.append(self.des.blueprintName)
        self.logger.debug("Blueprint added: " + self.des.blueprintName + ". Algorithm type: " + self.des.algoType)
        
        self.enigmaM3 = EnigmaM3Blueprint()
        self.app.register_blueprint(self.enigmaM3)
        self.historicalAlgos.append(self.enigmaM3.blueprintName)
        self.logger.debug("Blueprint added: " + self.enigmaM3.blueprintName + ". Algorithm type: " + self.enigmaM3.algoType)
        
        self.md5 = MD5Blueprint()
        self.app.register_blueprint(self.md5)
        self.hashingAlgos.append(self.md5.blueprintName)
        self.logger.debug("Blueprint added: " + self.md5.blueprintName + ". Algorithm type: " + self.md5.algoType)
        
        self.rsa = RSABlueprint()
        self.app.register_blueprint(self.rsa)
        self.modernAlgos.append(self.rsa.blueprintName)
        self.logger.debug("Blueprint added: " + self.rsa.blueprintName + ". Algorithm type: " + self.rsa.algoType)
        
        self.sha = SHABlueprint()
        self.app.register_blueprint(self.sha)
        self.hashingAlgos.append(self.sha.blueprintName)
        self.logger.debug("Blueprint added: " + self.sha.blueprintName + ". Algorithm type: " + self.sha.algoType)
        
        self.vigenereCipher = VigenereCipherBlueprint()   
        self.app.register_blueprint(self.vigenereCipher)
        self.historicalAlgos.append(self.vigenereCipher.blueprintName)
        self.logger.debug("Blueprint added: " + self.vigenereCipher.blueprintName + ". Algorithm type: " + self.vigenereCipher.algoType)
        
        
        self.allAlgos = self.historicalAlgos + self.outdatedAlgos + self.modernAlgos + self.hashingAlgos
        self.allAlgos.sort()
        self.historicalAlgos.sort()
        self.outdatedAlgos.sort()
        self.modernAlgos.sort()
        self.hashingAlgos.sort()
        
        
    def launchServer(self):
        
        """This function is not intended for use in a production server!"""

        self.logger.info("Launching server")
        self.app.run(debug=True, threaded=True)
        
    def index(self):
        
        """This method is called when a request is sent to the homepage"""
        
        try:
            
            return render_template("index.html", allAlgos=self.allAlgos, 
                                   historicalAlgos=self.historicalAlgos, 
                                   outdatedAlgos=self.outdatedAlgos,
                                   modernAlgos=self.modernAlgos,
                                   hashingAlgos=self.hashingAlgos)
        
        except TemplateNotFound:
            
            abort(404)
        