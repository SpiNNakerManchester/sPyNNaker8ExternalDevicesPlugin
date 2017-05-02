import os
import unittest

import spinn_utilities.package_loader as package_loader


class ImportAllModule(unittest.TestCase):

    def test_import_all(self):
        if os.environ.get('CONTINUOUS_INTEGRATION', None) == 'True':
            package_loader.load_module("spynnaker8_external_devices_plugin",
                                       remove_pyc_files=False)
        else:
            package_loader.load_module("spynnaker8_external_devices_plugin",
                                       remove_pyc_files=True)
