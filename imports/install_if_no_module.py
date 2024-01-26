# Generic solution to install non-existing module

import importlib
import subprocess

module = 'requests'

try:
    importlib.import_module(module)
    print(f'{module} module already installed.')
except ImportError:
    print(print(f'{module} module not existing on system. Will try to install.'))

    try:
        subprocess.run(['pip', 'install', module])
        print(f'{module} module installed successfully.')
    except subprocess.CalledProcessError:
        print(f'Unable to install module {module}.')
