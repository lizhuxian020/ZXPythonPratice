# coding: utf-8
# Author: lee_zix

import os
from utils.log_tools import init_logger

logger = init_logger('./temp/delete_file_log.txt', 'delete_file')

def delete_file(dirpath, containname):
    """
    delete file which name contain specify string thought dir_path
    :param dirpath: direction path
    :param containname: specify string
    :return:
    """
    if not isinstance(dirpath, str):
        return False
    if os.path.isdir(dirpath):
        for x in os.listdir(dirpath):
            fullfile = os.path.join(dirpath, x)
            if os.path.isfile(fullfile):
                if containname in os.path.basename(fullfile):
                    try:
                        os.remove(fullfile)
                    except Exception, ex:
                        logger.error(ex)
                    else:
                        logger.debug('success delete: %s' % fullfile)
            else:
                delete_file(fullfile, containname)
    else:
        print 'param: %s is not direction or not exist' % repr(dirpath)

    pass

if __name__ == '__main__':

    delete_file('/Users/lzx/Desktop/WXRes/grade_4', 'pic')