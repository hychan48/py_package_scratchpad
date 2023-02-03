# Python Package Scratchpad

# Initial Packages to Test
* ssh clients
  * Paramiko
    * https://pypi.org/project/paramiko/
* yaml parsers
  * PyYaml
    * https://pypi.org/project/PyYAML/#:~:text=YAML%20is%20a%20data%20serialization,API%2C%20and%20sensible%20error%20messages.
* sqlite3 orm
  * https://pypi.org/project/SQLAlchemy/
  * https://pypi.org/project/ORM-SQLite/
* file transfer
  * scp
* fire
  * https://pypi.org/project/fire/


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