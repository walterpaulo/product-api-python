from lzma import FORMAT_ALONE
from src.server.instance import server

from src.controllers.home import *
from src.controllers.products import *

server.run()
