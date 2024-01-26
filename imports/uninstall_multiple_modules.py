# Generic solution to uninstall Python modules from some list

import subprocess

module_list = ['requests', 'bs4']

for module in module_list:
    try:
        subprocess.run(['pip', 'uninstall', module, '-y'])
        print(f'{module} module uninstalled.')
    except subprocess.CalledProcessError:
        print(f'Unable to uninstall {module} module. Check with terminal manually.')
