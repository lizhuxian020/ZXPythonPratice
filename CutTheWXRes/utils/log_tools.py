# coding: utf-8
# Author: lee_zix

import logging
import file_tools


def init_logger(log_file_path, logger_name=''):
    # valid path
    if file_tools.make_sure_path(log_file_path, 'f'):
        logger = logging.getLogger(logger_name)
        handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        logger.setLevel(logging.NOTSET)
        logger.addHandler(handler)
        return logger
    else:
        print 'fail to create path: %s ' % log_file_path
        return None


if __name__ == '__main__':
    logger = init_logger('.asd')
    if logger is not None:
        print 'has logger'
        logger.debug('what thr fuck')
    else:
        print 'logger is none'



