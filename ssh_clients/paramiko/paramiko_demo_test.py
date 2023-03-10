# PyTest
import sys
import pytest
import logging as log

from paramiko.client import SSHClient, WarningPolicy
from os.path import expanduser
from pathlib import Path


class SSHExecClass():
    def __init__(self, connection=""):
        # connection (todo)
        client = SSHClient()
        self.client = client
        self.environment = {}

        id_rsa = Path(expanduser('~')).joinpath(".ssh", "id_rsa")
        assert id_rsa.exists()
        client.load_system_host_keys(filename=str(id_rsa))
        client.set_missing_host_key_policy(WarningPolicy)
        client.connect('localhost', port=2022, username='root', allow_agent=False)  # fine
    def ssh_exec_cmd(self, cmd):
        log.warning(self.environment)
        stdin, stdout, stderr = self.client.exec_command(cmd, environment=self.environment)
        # return stdin, stdout, stderr, stdout.readlines()
        return stdout.readlines()
    def close(self):
        # must close client and transport
        self.client.close()

# https://docs.paramiko.org/en/stable/api/client.html
def test_name():
    # log.warning("hi")
    client = SSHClient()

    id_rsa = Path(expanduser('~')).joinpath(".ssh", "id_rsa")
    assert id_rsa.exists()
    client.load_system_host_keys(filename=str(id_rsa))
    # client.load_host_keys(filename=str(id_rsa))
    client.set_missing_host_key_policy(WarningPolicy)

    # client.connect('localhost', port=2022, username='root') # fine
    client.connect('localhost', port=2022, username='root', allow_agent=False)  # fine
    # client.connect('localhost', port=2022, username='root',look_for_keys=False) # will crash
    # client.connect('localhost', port=2022, username='root',look_for_keys=False,allow_agent=False) # will crash

    i = 1
    i = 10
    for x in range(i):
        stdin, stdout, stderr = client.exec_command('ls -l')
        # log.warning(stdout)
        # paramiko.ChannelFile
        stdouts = stdout.readlines()
        # class paramiko.file.BufferedFile?
        # log.warning(stdouts) # returns ["total 0\n"]
        assert stdouts[0] == 'total 0\n'

    client.close()


def test_tunnel():
    # https://stackoverflow.com/questions/35304525/nested-ssh-using-python-paramiko
    id_rsa = Path(expanduser('~')).joinpath(".ssh", "id_rsa")
    assert id_rsa.exists()
    host_client = SSHClient()
    host_client.set_missing_host_key_policy(WarningPolicy)
    host_client.connect('localhost', port=2022, username='root', allow_agent=False)

    host_transport = host_client.get_transport()

    # "session", "forwarded-tcpip", "direct-tcpip", or "x11"
    # vm_channel = host_transport.open_channel("direct-tcpip",("deb1",22),("localhost",2222)) # works
    # vm_channel = host_transport.open_channel("direct-tcpip",("deb1",22),("localhost",2222)) # works
    vm_channel_1 = host_transport.open_channel("direct-tcpip", ("deb1", 22), ("localhost", 22))
    vm_channel_2 = host_transport.open_channel("direct-tcpip", ("deb2", 22), ("localhost", 22))
    # works

    # vm_channel = host_transport.open_channel("session",("deb1",22),("localhost",2222)) # stalls
    # vm_channel = host_transport.open_channel("forwarded-tcpip",("deb1",22),("localhost",2222)) # errors
    # vm_channel = host_transport.open_channel("x11",("deb1",22),("localhost",2222)) # errors

    # i think the sample is reversed... jhost is host
    # jhost= is actually the vm
    vm1 = SSHClient()
    vm1.set_missing_host_key_policy(WarningPolicy)
    vm1.connect('deb1', username='root', sock=vm_channel_1)

    vm2 = SSHClient()
    vm2.set_missing_host_key_policy(WarningPolicy)
    vm2.connect('deb2', username='root', sock=vm_channel_2)
    # Execute commands
    # host_client.connect('localhost', port=2022, username='root',allow_agent=False)
    stdin, stdout, stderr = host_client.exec_command('hostname')
    log.warning(stdout.readlines()[0])

    stdin, stdout, stderr = vm1.exec_command('hostname')
    log.warning(stdout.readlines()[0])

    stdin, stdout, stderr = vm2.exec_command('hostname')
    log.warning(stdout.readlines()[0])

    # Check connection?
    # well this works quite fast

    # close all

    host_client.close()
    host_transport.close()

    vm_channel_1.close()
    vm1.close()
    vm_channel_2.close()
    vm2.close()

    assert True

def test_env_without():
    c_client = SSHExecClass()
    tmp = c_client.ssh_exec_cmd("printenv HOST_IP") # linux ssh command
    log.warning(tmp)
    assert len(tmp) == 0 # empty list
    c_client.close()

def test_env_with():
    c_client = SSHExecClass()
    c_client.environment['HOST_IP'] = '127.0.0.1'
    c_client.environment['LC_HOST_IP'] = '127.0.0.1'
    # tmp = c_client.ssh_exec_cmd("printenv HOST_IP") # linux ssh command
    # log.warning(c_client.environment)
    # tmp = c_client.ssh_exec_cmd("echo -n $HOST_IP") # linux ssh command
    # tmp = c_client.ssh_exec_cmd("echo -n $LC_HOST_IP") # linux ssh command
    tmp = c_client.ssh_exec_cmd("printenv LC_HOST_IP")
    log.warning(tmp)
    assert len(tmp) == 1 # empty list
    c_client.close()

def test_windows():
    # aoda test
    # log.warning("hi")
    from os import getenv
    assert getenv("WIN_PASS")
    client = SSHClient()
    client.set_missing_host_key_policy(WarningPolicy)
    client.connect('localhost', port=22, username=getenv("WIN_USERNAME"), password=getenv('WIN_PASS'), allow_agent=False)  # fine
    # bty default windows ssh doesnt allow env to bet set like this in it's sshd_config... so
    environment = {
        "LC_HI": 'hello world'
    }
    stdin, stdout, stderr = client.exec_command('set LC_HI', environment=environment)
    # stdin, stdout, stderr = client.exec_command('set PATH', environment=environment) # this one obv works...
    stdouts = stdout.readlines()
    log.warning(stdouts)
    # assert len(stdouts == 1  # empty list
    # assert stdouts[0] == 'total 0\n'

    client.close()
def test_sftp():
    #     https://stackoverflow.com/questions/3635131/paramikos-sshclient-with-sftp
    pass

if __name__ == '__main__':
    pytest.main(sys.argv)
