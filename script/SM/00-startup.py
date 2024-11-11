import sys, os
from pathlib import Path
from IPython import get_ipython

home = Path.home()
Krek12 = home / '.Krek12'
marking = Krek12 / 'marking.py'
zrok_bin = home / '.zrok/bin/zrok'
ngrok_bin = home / '.ngrok/bin/ngrok'
startup = home / '.ipython/profile_default/startup'

sys.path.append(str(startup))

if zrok_bin.exists():
    if 'zrok' not in os.environ.get('PATH', '') or str(zrok_bin.parent) not in os.environ['PATH']:
        zrok_bin.chmod(0o755)
        os.environ['PATH'] += os.pathsep + str(zrok_bin.parent)

if ngrok_bin.exists():
    if 'ngrok' not in os.environ.get('PATH', '') or str(ngrok_bin.parent) not in os.environ['PATH']:
        ngrok_bin.chmod(0o755)
        os.environ['PATH'] += os.pathsep + str(ngrok_bin.parent)

if marking.exists():
    get_ipython().run_line_magic('run', f'{marking}')
