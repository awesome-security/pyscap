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

logger = logging.getLogger(__name__)
class ItemType(Model):
    ATTRIBUTE_MAP = {
        'abstract': {'ignore': True, 'type': 'Boolean', 'default': False},
        'cluster-id': {'ignore': True, 'type': 'NCName'},
        'extends': {'ignore': True, 'type': 'NCName'},
        'hidden': {'ignore': True, 'type': 'Boolean', 'default': False},
        'prohibitChanges': {'ignore': True, 'type': 'Boolean', 'default': False},
        'Id': {'ignore': True, 'type': 'ID'},
    }
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}status': {'class': 'StatusType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}dc-status': {'class': 'DCStatusType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}version': {'class': 'VersionType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}title': {'class': 'TextWithSubType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}description': {'class': 'HTMLTextWithSubType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}warning': {'class': 'WarningType', 'type': 'String', 'append': 'warnings'},
        '{http://checklists.nist.gov/xccdf/1.2}question': {'class': 'TextType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}reference': {'class': 'ReferenceType', 'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}metadata': {'class': 'MetadataType', 'ignore': True},
    }
    # abstract
    # def __init__(self):
    #     super(ItemType, self).__init__()
    #
    #     self.warnings = []
    #
    def from_xml(self, parent, el):
        super(ItemType, self).from_xml(parent, el)

        for warning in self.warnings:
            logger.warning('Warning:\n' + warning)
