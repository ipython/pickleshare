PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike 
shelve, many processes can access the database simultaneously. Changing a 
value in database is immediately visible to other processes accessing the 
same database.

Concurrency is possible because the values are stored in separate files. Hence
the "database" is a directory where *all* files are governed by PickleShare.

Example usage::
    
    from pickleshare import *
    db = PickleShareDB('~/testpickleshare')
    db.clear()
    print "Should be empty:",db.items()
    db['hello'] = 15
    db['aku ankka'] = [1,2,313]
    db['paths/are/ok/key'] = [1,(5,46)]
    print db.keys()


This module is certainly not ZODB, but can be used for low-load 
(non-mission-critical) situations where tiny code size trumps the 
advanced features of a "real" object database.

Installation guide: easy_install pickleshare

Author: Ville Vainio <vivainio@gmail.com>
License: MIT open source license.

Version note: this is an early beta version of the module. It has been tested (and works)
in both Linux and Windows. This will probably end up as the interactive persistence 
system for IPython 0.7.2+, to make inter-ipython-session data sharing possible in real time.

A 'pickleshare' script will be installed for "administration"/testing.

Changes since 0.1:

* del db['key'] can no longer croak on permission denied on windows 
