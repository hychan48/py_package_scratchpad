# PyTest
import sys
import pytest
import logging as log

from paramiko.client import SSHClient,WarningPolicy
from os.path import expanduser
from pathlib import Path
# https://docs.paramiko.org/en/stable/api/client.html
def test_name():
    # log.warning("hi")
    client = SSHClient()

    id_rsa = Path(expanduser('~')).joinpath(".ssh","id_rsa")
    assert id_rsa.exists()
    client.load_system_host_keys(filename=str(id_rsa))
    # client.load_host_keys(filename=str(id_rsa))
    client.set_missing_host_key_policy(WarningPolicy)


    # client.connect('localhost', port=2022, username='root') # fine
    client.connect('localhost', port=2022, username='root',allow_agent=False) # fine
    # client.connect('localhost', port=2022, username='root',look_for_keys=False) # will crash
    # client.connect('localhost', port=2022, username='root',look_for_keys=False,allow_agent=False) # will crash

    i = 1
    i = 10
    for x in range(i):
        stdin, stdout, stderr = client.exec_command('ls -l')
        # log.warning(stdout)
        # paramiko.ChannelFile
        # https: // docs.paramiko.org / en / stable / api / file.html?highlight = readlines  # paramiko.file.BufferedFile.readlines
        stdouts = stdout.readlines()
        # class paramiko.file.BufferedFile?
        # log.warning(stdouts) # returns ["total 0\n"]
        assert stdouts[0] == 'total 0\n'

    client.close()

if __name__ == '__main__':
    pytest.main(sys.argv)
