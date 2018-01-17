# err_logging2.py

import logging
logging.basicConfig(level=logging.ERROR)
#debug，info，warning，error || there are four levels to control the message

s = '0'
n = int(s)
logging.info('wow, n = %d' % n)
print(10 / n)
