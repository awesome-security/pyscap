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
class MetadataType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}title': {'type': 'String'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}affected': {'append': 'affecteds', 'class': 'AffectedType', 'min': 0, 'max': None},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}reference': {'append': 'references', 'class': 'ReferenceType', 'min': 0, 'max': None},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}description': {'type': 'String'},
            '*': {'ignore': True},
        },
    }
