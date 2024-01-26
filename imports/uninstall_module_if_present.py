# Generic solution to uninstall Python module from within

import subprocess

module = 'requests'

try:
    subprocess.run(['pip', 'uninstall', module, '-y'])
    print(f'{module} module uninstalled.')
except subprocess.CalledProcessError:
    print(f'Unable to uninstall {module} module. Check with terminal manually.')
