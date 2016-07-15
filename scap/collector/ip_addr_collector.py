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

from scap.collector.collector import Collector
import re, logging

logger = logging.getLogger(__name__)
class IPAddrCollector(Collector):
    def collect_facts(self):
        self.host.facts['network_connections'] = []
        for line in self.host.lines_from_command('ip addr'):
            # link line
            m = re.match(r'^\s+link/(ether|loopback) ([:a-f0-9]+)', line)
            if m:
                mac_address = m.group(2)
                continue

            # inet line
            m = re.match(r'^\s+inet ([0-9.]+)(/\d+)', line)
            if m:
                self.host.facts['network_connections'].append({'mac_address': mac_address, 'ip_address': m.group(1), 'subnet_mask': m.group(2)})
                continue

            # inet6 line
            m = re.match(r'^\s+inet6 ([0-9:]+)(/\d+)', line)
            if m:
                self.host.facts['network_connections'].append({'mac_address': mac_address, 'ip_address': m.group(1), 'subnet_mask': m.group(2)})
                continue
