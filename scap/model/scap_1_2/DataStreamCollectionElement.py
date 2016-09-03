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
class DataStreamCollectionElement(Model):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/scap/source/1.2',
        'tag_name': 'data-stream-collection',
        'elements': {
            '{http://scap.nist.gov/schema/scap/source/1.2}data-stream': {'max': None, 'class': 'DataStreamElement', 'map': 'data_streams'},
            '{http://scap.nist.gov/schema/scap/source/1.2}component': {'max': None, 'class': 'ComponentElement', 'map': 'components' },
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-component': {'max': None, 'min': 0, 'class': 'ExtendedComponentElement', 'map': 'extended_components' },
            '{http://www.w3.org/2000/09/xmldsig#}Signature': {'max': None, 'min': 0, 'ignore': True},
        },
        'attributes': {
            'id': {'required': True, 'type': 'DataStreamCollectionIDPattern'},
            'schematron-version':{'type': 'Token', 'required': True, 'ignore': True},
        },
    }
    def __init__(self):
        super(DataStreamCollectionElement, self).__init__()    # {http://scap.nist.gov/schema/scap/source/1.2}data-stream-collection

        # self.components = {}
        # self.data_streams = {}
        # self.extended_components = {}
        #
        self.selected_data_stream = None

    def resolve_reference(self, ref):
        if ref[0] == '#':
            ref = ref[1:]
            if ref in self.components:
                return self.components[ref]
            elif self.selected_data_stream:
                logger.debug('Reference ' + ref + ' not in components; checking selected data stream')
                return self.data_streams[self.selected_data_stream].resolve_reference('#' + ref)
            else:
                # we're the top level parent
                logger.critical('Reference ' + ref + ' not in ' + str(list(self.components.keys())))
                import sys
                sys.exit()
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()