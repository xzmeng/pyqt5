import subprocess
import sys

source = sys.argv[1]
target = source.replace('.ui', '.py')

subprocess.run(['pyuic5', source,
                '-o', target])