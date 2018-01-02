# coding: utf-8
# Author: lee_zix


import os, sys, re


need_process_list = ['PAFFCar', 'PAFFPersonalCenter', 'PAFFFaceCheck', 'PAFFLocalDiscount', 'PAFFLogin', 'PAFFMyHouse', 'PAFFRewardPoint']

root_path = '/Users/lzx/workFile/pinganPro/guangzhou/APP_IOS'


def check_file(dir_path):
    """check dir_path and modify podspec file"""
    module_name = dir_path.split('/')[-1]
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        return
    podSpec_path = os.path.join(dir_path, module_name + '.podspec')
    if not os.path.exists(podSpec_path) and not os.path.isfile(podSpec_path):
        return
    podspec_content = ''
    with open(podSpec_path, 'r') as f:
        for line in f:
            if '#s.au' in line:
                line = line.replace('#', '')
                print "完成处理: ", module_name, line
            if 's.description' in line:
                c = re.compile(r'.*s.description.*=.*"(.*)".*')
                p = c.match(line)

                if p:
                    desc_content = p.groups()[0]
                    if len(desc_content) == 0:
                        line = re.sub(r"\"\"", "\"asd\"", line)
                        print "完成处理: ", module_name, line

            podspec_content += line
        pass

    with open(podSpec_path, 'w') as f:
        f.write(podspec_content)
        pass

    # file_obj = open(podSpec_path, 'r')
    # print file_obj.read()
    # file_obj.close()
    pass


if __name__ == '__main__':

    for x in need_process_list:
        file_path = os.path.join(root_path, x)
        check_file(file_path)




