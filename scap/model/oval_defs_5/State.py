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

from scap.Model import Model
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class State(Model):
    def from_xml(self, parent, el):
        super(State, self).from_xml(parent, el)

        self.id = el.attrib['id']

        if 'operator' in el.attrib :
            self.operator = el.attrib['operator']
        else:
            self.operator = 'AND'

        if 'deprecated' in el.attrib and el.attrib['deprecated']:
            logger.warning('Using deprecated test: ' + self.id)
