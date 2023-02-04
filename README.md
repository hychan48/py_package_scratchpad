# Python Package Scratchpad

# Initial Packages to Test
* ssh clients
  * Paramiko
    * https://pypi.org/project/paramiko/
  * SSH Tunneling / Port Forwarding
  * stdin
* yaml parsers
  * PyYaml
    * https://pypi.org/project/PyYAML/#:~:text=YAML%20is%20a%20data%20serialization,API%2C%20and%20sensible%20error%20messages.
* sqlite3 orm
  * https://pypi.org/project/SQLAlchemy/
  * https://pypi.org/project/ORM-SQLite/
* file transfer
  * scp
  * paramiko?
* fire
  * https://pypi.org/project/fire/
* PyTest
* Path Utils
* Jupiter - more light weight approach?

# Testing Suites

# Lower Priority
* dnspython
* build

# Wheel Creation


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

# Write to File

## JSON / Dict converter

# Delete File
Path().unlink(missing_ok=False)

# Copy File
#https://stackoverflow.com/questions/123198/how-to-copy-files
shutil.copy("src","dir")



```

# PyTest
* https://docs.pytest.org/en/latest/
* https://pypi.org/project/pytest/
* naming conventions
* suites
* 