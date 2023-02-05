# works outside of unit test

import logging

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)

logging.warning("warning log")
logging.info('I told you so')  # will not print anything
