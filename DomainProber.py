#!/bin/python

import urllib.request
import multiprocessing
from sys import *

def Main():
    if len( argv) == 1:
        print ("usage:./DomainProbe.py <domain-list-file>")
    elif len ( argv) == 2:
        p1 = multiprocessing.Process( target=probeDomain)
        print ("[*] STARTING PROBER")
        p1.start()
        p1.join()

def probeDomain():
    GREEN = '\033[32;1m'
    RED = '\033[31;1m'
    DONE = '\033[0m'

    domain_list_file = argv[1]
    f = open( domain_list_file, "r")
    domains = []

    for i in f:
        if i[:4] == "http":
            domains.append(i.strip('\n'))
        else:
            domains.append("https://{}".format(i).strip('\n'))

    for i in domains:
        try:
            res = urllib.request.urlopen(  str( i), timeout=4).getcode()
            if res == 200:
                print ( str( i) + GREEN + " --> UP" + DONE )
            elif res == 404:
                print ( str( i) + RED + " --> NOT FOUND" + DONE )
        except urllib.error.URLError:
            print ( str( i) + RED + " --> URL ERROR" + DONE )
        except KeyboardInterrupt:
            sys.exit()
        except:
            #print ( str( i) + RED + " --> UNABLE TO RESOLVE HOST" + DONE )
            print ("error")



if __name__ == '__main__':
    Main()
