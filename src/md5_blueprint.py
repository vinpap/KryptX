import logging
import logging.handlers

from flask import render_template, abort
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint

class MD5Blueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        super().__init__('MD5', 'HASHING')
        self.add_url_rule("/md5", "md5", self.MD5)
        
    
    def MD5(self):
        
        """This method is called when a request is sent to /md5"""
        
        try:
            
            return render_template("index.html")
        
        except TemplateNotFound:
            
            abort(404)
    

        