import os

if os.path.isfile('.pyrc.py'):
    exec(open('.pyrc.py').read())
