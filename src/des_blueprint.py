import logging
import logging.handlers

from flask import render_template, abort
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint

class DESBlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        url = "/des"
        super().__init__('DES', 'OUTDATED', url)
        
        self.add_url_rule(url, "des", self.DES)
        
    
    def DES(self):
        
        """This method is called when a request is sent to /des"""
        
        try:
            
            return render_template("index.html", allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)        
        except TemplateNotFound:
            
            abort(404)
    

        