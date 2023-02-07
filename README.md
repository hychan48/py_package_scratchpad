# Python Package Scratchpad

# Initial Packages to Test
* ssh clients
  * SSH Tunneling / Port Forwarding
  * stdin
  * Client connect
  1. Paramiko
    * https://pypi.org/project/paramiko/
    * also a server...
  2. parallel-ssh
    * https://parallel-ssh.readthedocs.io/en/latest/quickstart.html#single-host-client
  3. ssh2-python
    * https://pypi.org/project/ssh2-python/
  4. fabric
    * https://docs.fabfile.org/en/stable/
* yaml parsers
  * PyYaml
    * https://pypi.org/project/PyYAML/#:~:text=YAML%20is%20a%20data%20serialization,API%2C%20and%20sensible%20error%20messages.
* sqlite3 orm
  * [x] https://pypi.org/project/SQLAlchemy/
  * https://pypi.org/project/ORM-SQLite/
* file transfer
  * scp
  * paramiko?
* fire
  * https://pypi.org/project/fire/
* [x] PyTest
* [x] Path Utils
* Jupiter - more light weight approach?
* Console Color
  * termcolor 2.2.0
    * decent syntax. doesnt work with debugger (windows)
    * no work on jetbrains remote either
  * string-color
    * works on remote to ubuntu on PyCharm / Jetbrains Client
    * 

# Testing Suites
* pytest
  * logging
  * set pyproject.toml
    * look for further details
    * doesnt flush file untill the end
    * log_cli=true
      * for inline print debugging

# Lower Priority
* dnspython
* build

# Wheel Creation

# Multi Threading / Processing

# SQLite - WSL
* Using Ubuntu 22.04 WSL 2.0
```bash
# Install - don't think it needs to be installed at all
sudo apt update
sudo apt install -y sqlite3

# Launch local in-memory
sqlite3
```
```sql
-- verifiy installed version
select sqlite_version();
select * from sqlite_master;
```

# Python3 Live Templates
```python
# Make Directory
from pathlib import Path
Path().joinpath('dev', 'tmpFolder').mkdir(parents=True, exist_ok=True)

# rm -rf force
import shutil
# shutil.rmtree(str(Path().joinpath('dev', 'tmpFolder')))
shutil.rmtree(str(Path().joinpath('dev')))

# expand user
from os.path import expanduser
home = expanduser('~')
print(home)

# Open File
import json # there's also dotmap package...
with open(str(Path("dev/json_files/data.json"))) as json_file:
    data = json.load(json_file)
# Write to File
data = {
  "id": "04", 
  "name": "sunil", 
  "department": "HR"   
}
with open(str(Path("dev/json_files/out.json")), "w") as outfile:
    # json.dump(data, outfile)
    json.dump(data, outfile,indent = 2)
    # json.dump(data, outfile,indent = 4)
    # json.dumps(data, outfile,indent = 4)
## JSON / Dict converter

# Delete File
Path().unlink(missing_ok=False)

# Copy File
#https://stackoverflow.com/questions/123198/how-to-copy-files
shutil.copy("src","dir")

# PyTest
import sys
import pytest
import logging as log


def test_name():
    log.warning("hi")


if __name__ == '__main__':
    pytest.main(sys.argv)


```

# PyTest
* https://docs.pytest.org/en/latest/
* https://pypi.org/project/pytest/
* naming conventions
  * test_filename.py
    * test_*.py or *_test.py
  * def test_something():'
* setUp / before()
  * @pytest.fixture
* suites
* Print / debug
  * https://codingshower.com/pytest-print-or-dump-variables-to-console-for-debugging/
