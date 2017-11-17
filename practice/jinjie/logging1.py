# coding: utf-8
# Author: lee_zix

import logging

logger = logging.getLogger()
handler = logging.FileHandler('handler.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logger.addHandler(handler)
handler.setFormatter(formatter)
logger.setLevel(logging.NOTSET)

logger.debug('this is debug content')

