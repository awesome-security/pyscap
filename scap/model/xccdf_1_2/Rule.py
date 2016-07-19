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

from scap.model.xccdf_1_2.GroupRuleCommon import GroupRuleCommon
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Rule(GroupRuleCommon):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        self.id = el.attrib['id']
        if el.attrib['selected'] == 'true' or el.attrib['selected'] == '1':
            self.selected = True
        else:
            self.selected = False

        self.check = None
        comp_el = el.find("./xccdf_1_2:complex-check", Engine.namespaces)
        if comp_el:
            from scap.model.xccdf_1_2.ComplexCheck import ComplexCheck
            self.check = ComplexCheck()
            self.check.from_xml(self, el)
        else:
            self.checks = {}
            from scap.model.xccdf_1_2.Check import Check
            for el in el.findall("./xccdf_1_2:check", Engine.namespaces):
                check = Check()
                check.from_xml(self, el)
                if 'selector' in el.attrib:
                    self.checks[el.attrib['selector']] = check
                    if self.check is None:
                        self.check = check
                else:
                    self.check = check
        if self.check is None:
            logger.critical('Could not load check from rule ' + self.id)
            import sys
            sys.exit()

        # TODO: multiple

    def select_check(self, selector):
        self.check = self.checks[selector]
