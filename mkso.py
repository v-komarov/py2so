#!/usr/bin/python
#coding:utf-8

import os
import argparse

#### Иключения ####
exc = ['__init__','settings','settings_local','urls','wsgi','manage']


def MakeSO(args):
    
    
    for root, dirs, files in  os.walk(args.dir):
	for name in files:
	    fullname = os.path.join(root,name)
	    if name.split('.')[-1] == 'py' and exc.count(name.split('.')[-2]) == 0:
		print fullname
		os.system('cython %s' % fullname)
		cfullname = '%s.c' % os.path.join(root,name.split('.')[-2])
		if os.path.exists(cfullname):
		    ofullname = '%s.o' % os.path.join(root,name.split('.')[-2])
		    os.system('gcc -c -fPIC -I/usr/include/python2.7/ %s -o %s' % (cfullname,ofullname))
		    if os.path.exists(ofullname):
			sfullname = '%s.so' % os.path.join(root,name.split('.')[-2])
			os.system('gcc -shared %s -o %s' % (ofullname,sfullname))
			

def Clear(args):

    for root, dirs, files in  os.walk(args.dir):
	for name in files:
	    fullname = os.path.join(root,name)
	    if name.split('.')[-1] == 'py' and exc.count(name.split('.')[-2]) == 0:
		print fullname
		sfullname = '%s.so' % os.path.join(root,name.split('.')[-2])
		ofullname = '%s.o' % os.path.join(root,name.split('.')[-2])
		cfullname = '%s.c' % os.path.join(root,name.split('.')[-2])
		pycfullname = '%s.pyc' % os.path.join(root,name.split('.')[-2])
		if os.path.exists(sfullname):
		    os.remove(fullname)
		if os.path.exists(ofullname):
		    os.remove(ofullname)
		if os.path.exists(cfullname):
		    os.remove(cfullname)
		if os.path.exists(pycfullname):
		    os.remove(pycfullname)



if __name__=='__main__':

    parser = argparse.ArgumentParser(prog='mkso')
    parser.add_argument('-dir',help='write directory')
    parser.print_help()
    args = parser.parse_args()

    MakeSO(args)
    Clear(args)
