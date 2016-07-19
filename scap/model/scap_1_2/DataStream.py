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
class DataStream(Model):
    def from_xml(self, parent, el):
        super(DataStream, self).from_xml(parent, el)

        self.id = el.attrib['id']

        # TODO dictionaries

        self.checklists = {}
        xpath = "./scap_1_2:checklists"
        xpath += "/scap_1_2:component-ref"
        for comp in el.findall(xpath, Engine.namespaces):
            ref_mapping = None
            href = comp.attrib['{' + Engine.namespaces['xlink'] + '}href']
            for cat_el in comp:
                if cat_el.tag == '{' + Engine.namespaces['xml_cat'] + '}' + 'catalog':
                    logger.debug('Loading catalog for ' + href)
                    from scap.model.xml_cat.Catalog import Catalog
                    cat = Catalog()
                    cat.from_xml(self, cat_el)
                    ref_mapping = cat.to_dict()

            ref_el = self.parent.resolve_reference(href)
            if ref_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Benchmark':
                from scap.model.xccdf_1_2.Benchmark import Benchmark
                checklist = Benchmark()
                checklist.from_xml(self, ref_el, ref_mapping=ref_mapping)
            elif ref_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil':
                from scap.model.ocil_2_0.OCIL import OCIL
                checklist = OCIL()
                checklist.from_xml(self, ref_el, ref_mapping=ref_mapping)
            else:
                logger.critical('unknown component: ' + ref_el.tag + ' for ref: ' + href)
                import sys
                sys.exit()
            self.checklists[checklist.id] = checklist

        #from scap.model.xccdf_1_2.benchmark import Benchmark
        self.checks = {}
        xpath = "./scap_1_2:checks"
        xpath += "/scap_1_2:component-ref"
        for c in el.findall(xpath, Engine.namespaces):
            href = c.attrib['{' + Engine.namespaces['xlink'] + '}href']
            checks_el = self.parent.resolve_reference(href)
            #self.checks[c.attrib['id']] = Benchmark(self, checks_el)

        # TODO: extended-components
