import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from rsa_algo import RSAAlgo

class RSABlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.algo = RSAAlgo()
        
        url = "/rsa"
        super().__init__('RSA', 'MODERN', url)
        
        self.add_url_rule(url, "rsa", self.RSA)
        self.add_url_rule(url + "/encryption", "rsa_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "rsa_decryption", self.displayDecryptedText, methods=["POST"])
        self.add_url_rule(url + "/keysgeneration", "rsa_keys_generation", self.displayKeysPair, methods=["POST"])
        
    
    def RSA(self):
        
        """This method is called when a request is sent to /rsa"""
        
        try:
            
            return render_template("rsa.html", allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
    

    def displayEncryptedText(self):
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        
        
        """if len(bytes(key, encoding='utf-8')) not in range(8, 16, 24):
            
            errorMsg = ("This key is not valid. Please enter a key of 64, "
                        "128 or 192 bits. This amounts to 8, 16 or 24 "
                        "characters in ASCII")
            try:

                return render_template("rsa.html",
                                   mode="encryptionError",
                                   error=errorMsg,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
            except TemplateNotFound:
            
                abort(404)"""
        
        encryptedText = str(self.algo.encrypt(message, key))
        
        try:

            return render_template("rsa.html",
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
        
        """if len(bytes(key, encoding='utf-8')) not in range(8, 16, 24):
            
            errorMsg = ("This key is not valid. Please enter a key of 64, "
                        "128 or 192 bits. This amounts to 8, 16 or 24 "
                        "characters in ASCII")
            try:

                return render_template("rsa.html",
                                   mode="decryptionError",
                                   error=errorMsg,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
            except TemplateNotFound:
            
                abort(404)"""
        
        decryptedText = self.algo.decrypt(message, key)
        
        try:

            return render_template("rsa.html", 
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)

    def displayKeysPair(self):
        
        keysPair = self.algo.generateKeysPair()
        
        try:

            return render_template("rsa.html", 
                                   mode="displayKeysPair",
                                   privateKey=keysPair[0],
                                   publicKey=keysPair[1],
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)