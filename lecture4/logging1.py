#!/usr/bin/env python3 -tt

import logging


# log = logging.Logger()
logging.basicConfig(filename='task2.log', level=logging.DEBUG)

# logging.basicConfig(level=logging.DEBUG)

logging.debug("Contents of x: ".format(5))
logging.info("File saved successfully")
logging.warning("Missing required field 'age' - ignoring the person")
logging.error("Unable to load data file")
logging.critical("Unable to start the program! Aborting execution")

# print("Logging1: " + __name__)
# if __name__ == "__main__":
#     print(__name__)

