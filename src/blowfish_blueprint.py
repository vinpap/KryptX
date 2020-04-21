import logging
import logging.handlers

from flask import render_template, abort
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint

class BlowfishBlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.__url = "/blowfish"
        
        super().__init__('Blowfish', 'MODERN')
        self.add_url_rule(self.__url, "blowfish", self.blowfish)
        
    
    def blowfish(self):
        
        """This method is called when a request is sent to /blowfish"""
        
        try:
            
            return render_template("index.html")
        
        except TemplateNotFound:
            
            abort(404)
    

        