# Generic solution to install Multiple non-existing module
# !!! Check this on primary Python, not just on big IDE and venv.

import importlib
import subprocess

module_list = ['requests', 'bs4']

for module in module_list:
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
