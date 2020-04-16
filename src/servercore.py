"""Main server module. This class manages the homepage and loads all the 
blueprints (one encryption method = one blueprint)"""

import logging
import logging.handlers

from flask import Flask, render_template

class ServerCore:
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.app = Flask(__name__)
        self.app.add_url_rule("/", "index", self.index)
        
    
    def launchServer (self) :
        
        """This function is not intended for use in a production server!"""

        self.logger.info("Launching server")
        self.app.run(debug = True, threaded=True)
        
    def index(self):
        
        """This method is called when a request is sent to the homepage"""
        return render_template("index.html")