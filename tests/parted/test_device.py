#!/usr/bin/python
#
# Test cases for the methods in the parted.device module itself
#
# Copyright (C) 2009  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): David Cantrell <dcantrell@redhat.com>
#

import parted
import unittest

# One class per method, multiple tests per class.  For these simple methods,
# that seems like good organization.  More complicated methods may require
# multiple classes and their own test suite.
class DeviceNewTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceGetSetTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceOpenTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceCloseTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceDestroyTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceRemoveFromCacheTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceBeginExternalAccessTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceEndExternalAccessTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceReadTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceWriteTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceSyncTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceCheckTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceStartSectorToCylinderTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceEndSectorToCylinderTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceStartCylinderToSectorTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceEndCylinderToSectorTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceGetSizeTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceGetSizeAsSectorsTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceGetConstraintTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

class DeviceGetPedDeviceTestCase(unittest.TestCase):
    def runTest(self):
        # TODO
        self.fail("Unimplemented test case.")

# And then a suite to hold all the test cases for this module.
def suite():
    suite = unittest.TestSuite()
    suite.addTest(DeviceNewTestCase())
    suite.addTest(DeviceGetSetTestCase())
    suite.addTest(DeviceOpenTestCase())
    suite.addTest(DeviceCloseTestCase())
    suite.addTest(DeviceDestroyTestCase())
    suite.addTest(DeviceRemoveFromCacheTestCase())
    suite.addTest(DeviceBeginExternalAccessTestCase())
    suite.addTest(DeviceEndExternalAccessTestCase())
    suite.addTest(DeviceReadTestCase())
    suite.addTest(DeviceWriteTestCase())
    suite.addTest(DeviceSyncTestCase())
    suite.addTest(DeviceCheckTestCase())
    suite.addTest(DeviceStartSectorToCylinderTestCase())
    suite.addTest(DeviceEndSectorToCylinderTestCase())
    suite.addTest(DeviceStartCylinderToSectorTestCase())
    suite.addTest(DeviceEndCylinderToSectorTestCase())
    suite.addTest(DeviceGetSizeTestCase())
    suite.addTest(DeviceGetSizeAsSectorsTestCase())
    suite.addTest(DeviceGetConstraintTestCase())
    suite.addTest(DeviceGetPedDeviceTestCase())
    return suite

s = suite()
unittest.TextTestRunner(verbosity=2).run(s)