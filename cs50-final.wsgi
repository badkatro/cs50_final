import sys 
import logging 

logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0, "/var/www/vhosts/badkatro.dev/cs50.badkatro.dev/cs50_final") 

from app import app as application