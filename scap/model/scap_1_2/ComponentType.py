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
class ComponentType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'ComponentIDPattern'},
            'timestamp': {'ignore': True, 'type': 'DateTime'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}Benchmark': { 'class': 'BenchmarkType', 'in': 'model'},
            '{http://scap.nist.gov/schema/ocil/2.0}ocil': {'class': 'OCILType', 'in': 'model'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions': {'class': 'OVALDefintionsType', 'in': 'model'},
            '{http://cpe.mitre.org/dictionary/2.0}cpe-list': {'ignore': True, 'in': 'model'},
            '{http://checklists.nist.gov/xccdf/1.2}Tailoring': {'ignore': True, 'in': 'model'},
        },
    }
    # def __init__(self):
    #     super(ComponentType, self).__init__()    # {http://checklists.nist.gov/xccdf/1.2}component
    #
    #     self.model = None

    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Benchmark' \
    #         or sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil' \
    #         or sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions':
    #         self.model = Model.load(self, sub_el)
    #     else:
    #         return super(ComponentType, self).parse_element(sub_el)
    #     return True
