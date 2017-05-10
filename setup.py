import os
from setuptools import setup
from collections import defaultdict

__version__ = None
exec(open("spynnaker8_external_devices_plugin/_version.py").read())
assert __version__

install_requires = ['sPyNNaker8 >= 1!4.0.0a5, < 1!5.0.0',
                    'sPyNNakerExternalDevicesPlugin >= 1!4.0.0a5, < 1!5.0.0',
                    'pynn>=0.8, <0.9']

# Build a list of all project modules, as well as supplementary files
main_package = "spynnaker8_external_devices_plugin"
data_extensions = {".aplx", ".xml", ".json", ".xsd"}
config_extensions = {".cfg", ".template"}
main_package_dir = os.path.join(os.path.dirname(__file__), main_package)
start = len(main_package_dir)
packages = []
package_data = defaultdict(list)
for dirname, dirnames, filenames in os.walk(main_package_dir):
    if '__init__.py' in filenames:
        package = "{}{}".format(
            main_package, dirname[start:].replace(os.sep, '.'))
        packages.append(package)
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext in data_extensions:
            package = "{}{}".format(
                main_package, dirname[start:].replace(os.sep, '.'))
            package_data[package].append("*{}".format(ext))
            break
        if ext in config_extensions:
            package = "{}{}".format(
                main_package, dirname[start:].replace(os.sep, '.'))
            package_data[package].append(filename)

url = "https://github.com/SpiNNakerManchester/sPyNNaker8ExternalDevicesPlugin"

setup(
    name="sPyNNaker8ExternalDevicesPlugin",
    version=__version__,
    description="Spinnaker External Devices Plugin extended for PyNN8",
    url=url,
    packages=packages,
    package_data=package_data,
    install_requires=install_requires
)