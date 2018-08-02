#!C:\Users\Sampath\PycharmProjects\HireEasy\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wheel==0.24.0','console_scripts','wheel'
__requires__ = 'wheel==0.24.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wheel==0.24.0', 'console_scripts', 'wheel')()
    )
