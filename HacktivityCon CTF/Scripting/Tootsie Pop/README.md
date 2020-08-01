# Tootsie Pop

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
How many licks does it take to get to the center of a tootsie pop?

Download the file below.
```

- [pop.zip](./pop.zip)

# Exploitation

The flag has been compressed recursively with various types of compressing tools, namely 'xz', 'zip', 'bzip', 'gzip'. You can write a script to use the `file` command to find out the compression type of the current file and decompress it depending upon the type of compression.

```python
import subprocess
import os

filetypes = ['xz', 'zip', 'bzip', 'gzip']

while True:
    x = subprocess.check_output('ls', shell=True).decode().split('\n')[0]
    print(x)

    y = subprocess.check_output(f'file {x}', shell=True).decode()
    print(y)

    if 'gzip' in y:
        if not x.endswith('.gz'):
            os.system(f'mv {x} {x}.gz')
            x = f'{x}.gz'
        os.system(f'gunzip {x}')
        print('Uncompressed gzip')

    if 'XZ' in y:
        if not x.endswith('.xz'):
            os.system(f'mv {x} {x}.xz')
            x = f'{x}.xz'
        os.system(f'unxz {x}')
        print('Uncompressed xz')

    if 'bzip2' in y:
        if not x.endswith('.bz2'):
            os.system(f'mv {x} {x}.bz2')
            x = f'{x}.bz2'
        os.system(f'bzip2 -d {x}')
        print('Uncompressed bz2')

    if 'Zip' in y:
        if not x.endswith('.zip'):
            os.system(f'mv {x} {x}.zip')
            x = f'{x}.zip'
        os.system(f'unzip {x}')
        print('Uncompressed zip')
        os.system(f'mv {x} trash/{x}')

    if 'ASCII' in y:
        os.system(f'cat {x}')
        break
```

Remember to have a `trash` folder in the same directory as your script. Once it decompresses all, it gives you the flag in a file called `8c4be4`.

```bash
$ python script.py
...
...
flag{the_answer_is_1548_licks}
```


The flag is:

```
flag{the_answer_is_1548_licks}
```