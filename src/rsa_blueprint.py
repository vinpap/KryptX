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
    

        