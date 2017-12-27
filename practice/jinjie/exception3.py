# coding: utf-8
# Author: lee_zix

import logging

logger = logging.getLogger()
handler = logging.FileHandler('/tmp/logging.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

logger.debug('this is debug messgae')
print 'end'