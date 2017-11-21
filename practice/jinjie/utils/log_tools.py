# coding: utf-8
# Author: lee_zix

import logging
import file_tools


root_logger = logging.getLogger()
root_logger.setLevel(logging.NOTSET)


def init_logger(log_file_path, logger_name=''):
    # valid path
    if file_tools.make_sure_path(log_file_path, 'f'):
        logger = logging.getLogger(logger_name)
        handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        logger.setLevel(logging.NOTSET)
        logger.addHandler(handler)
        return logger
    else:
        print 'fail to create path: %s ' % log_file_path
        return None


def log_directly(log_file_path):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='log_file_path',
                        filemode='a')

    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')


if __name__ == '__main__':
    # logger = init_logger('./tmp/test.txt', 'txtlog')
    # if logger is not None:
    #     print 'has logger'
    #     logger.debug('what thr fuck')
    # else:
    #     print 'logger is none'


    loggerInfo = logging.getLogger('infoLogger')
    handler = logging.FileHandler('./tmp/infoLogger.txt')
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    loggerInfo.addHandler(handler)

    loggerInfo.setLevel(logging.NOTSET)

    loggerInfo.debug("debugmessage")

    loggerInfo.info("infomessage")

    loggerInfo.warn("warnmessage")

    loggerInfo.error("errormessage")

    loggerInfo.critical("criticalmessage")





