import logging
import logging.handlers

from flask import render_template, abort
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint

class RSABlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.__url = "/rsa"
        
        super().__init__('RSA', 'MODERN')
        self.add_url_rule(self.__url, "rsa", self.RSA)
        
    
    def RSA(self):
        
        """This method is called when a request is sent to /rsa"""
        
        try:
            
            return render_template("index.html")
        
        except TemplateNotFound:
            
            abort(404)
    

        