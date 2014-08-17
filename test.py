import odm
import time

test=odm.odm('admin','6432114')
test.login()
fid=test.add(filename='format.png',description='this is format png')
test.publish(fid)
#test.logout()
