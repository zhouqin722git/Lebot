#################

###

1、生成批量数据, 生成后壳通过source命令执行

#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import sys

file = open('intelligence_10.sql', 'w+')


for i in range(1, 1000000):
    print i

    id = "'" + str(i) + "'"
    content = "'xxxxxxxxx" + str(i) + "'"
    sql =  "INSERT INTO security_intelligence(id, content, content_type, group_id, id_path, create_id, create_time, update_id, update_time, standby1, standby2, standby3, VERSION) VALUES (%s, %s, 'single', '8ZDW4VGD78ce', '/4EOBUIG80010/4EOBUIG80013/8ZDW4VGD78ce', NULL, '1567566404794', 'FIKVIZS30007', NULL, NULL, NULL, NULL, -1);" % (id, content)

    print "当前content为: %s " % content
    print sql

    print >> file, sql
    


