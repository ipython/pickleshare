from setuptools import setup

# extract version from pickleshare.py
# can't import because pickleshare depends on path.py
with open('pickleshare.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version = eval(line.split('=', 1)[1])
            break

setup(
    name="pickleshare",
    version=version,
    py_modules=['pickleshare'],
    author="Ville Vainio",
    author_email="vivainio@gmail.com",
    description="Tiny 'shelve'-like database with concurrency support",
    license="MIT",
    extras_require = {
        # Ugly, but we can't do < comparison here
        ':python_version in "2.6 2.7 3.2 3.3"': ['pathlib2'],
    },
    url="https://github.com/pickleshare/pickleshare",
    keywords="database persistence pickle ipc shelve",
    long_description="""\
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
many processes can access the database simultaneously. Changing a value in 
database is immediately visible to other processes accessing the same database.

Concurrency is possible because the values are stored in separate files. Hence
the "database" is a directory where *all* files are governed by PickleShare.

Example usage::
    
    from pickleshare import *
    db = PickleShareDB('~/testpickleshare')
    db.clear()
    print("Should be empty:",db.items())
    db['hello'] = 15
    db['aku ankka'] = [1,2,313]
    db['paths/are/ok/key'] = [1,(5,46)]
    print(db.keys())

This module is certainly not ZODB, but can be used for low-load
(non-mission-critical) situations where tiny code size trumps the 
advanced features of a "real" object database.

Installation guide: pip install pickleshare
""",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
