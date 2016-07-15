# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import inspect, urlparse, logging
from scap.credential_store import CredentialStore

logger = logging.getLogger(__name__)
class Host(object):
    # TODO should be in a config file
    default_scheme = 'ssh'

    @staticmethod
    def parse(spec):
        import ssh_host
        import winrm_host
        if spec.find('://') == -1:
            spec = Host.default_scheme + '://' + spec
        url = urlparse.urlparse(spec)
        if url.scheme == 'ssh':
            creds = CredentialStore()
            if creds.has_section(url.hostname):
                if url.username:
                    creds.set(url.hostname, 'ssh_username', url.username)
                if url.password:
                    creds.set(url.hostname, 'ssh_password', url.password)
            t = ssh_host.SSHHost(url.hostname, port=(url.port if url.port else 22))
        elif url.scheme == 'winrm':
            #t = winrm_host.WinRMHost(url.hostname, port=(url.port if url.port else 0))
            raise NotImplementedError('winrm hosts are not implemented')
        else:
            logger.critical('Unsupported host scheme: ' + url.scheme)
            sys.exit()
        return t

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.collectors = []

    def get_hostname(self):
        return self.hostname

    def line_from_command(self, cmd):
        return self.exec_command(cmd).readline()

    def lines_from_command(self, cmd):
        return self.exec_command(cmd).readlines()

    def line_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readline()

    def lines_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readlines()

    def connect(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def disconnect(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_command(self, cmd):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def can_privileged_command(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_privileged_command(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def collect_facts(self):
        self.facts = {}

        # have to use while vs. for loop so collectors can add other collectors
        i = 0
        while i < len(self.collectors):
            try:
                self.collectors[i].collect_facts()
            except Exception, e:
                logger.warning('Collector ' + self.collectors[i].__class__.__name__ + ' failed: ' + str(e))
            i += 1
