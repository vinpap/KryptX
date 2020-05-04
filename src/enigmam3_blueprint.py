import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from enigmam3_algo import EnigmaM3

class EnigmaM3Blueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.algo = EnigmaM3()
        
        url = "/enigmam3"
        super().__init__('Enigma M3', 'HISTORICAL', url)
        
        self.add_url_rule(url, "enigmam3", self.enigmam3)
        self.add_url_rule(url + "/encryption", "enigmam3_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "enigmam3_decryption", self.displayDecryptedText, methods=["POST"])
        
    
    def enigmam3(self):
        
        """This method is called when a request is sent to /enigmam3"""
        
        try:
            
            return render_template("enigmam3.html", 
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
            
    
    def displayEncryptedText(self):
        
        message = request.form["message"]
        key = request.form["key_area"]
        

        
        encryptedText = str(self.algo.encrypt(message, key))
        
        try:

            return render_template("enigmam3.html",
                                   mode="displayEncryptedText",
                                   encryptedMessage=encryptedText,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
        
    
    def displayDecryptedText(self):
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        
        decryptedText = self.algo.decrypt(message, key)
        
        try:

            return render_template("enigmam3.html", 
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
    

        