import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "version.txt")) as f:
    version = f.read().rstrip()

setup(
    name="signingscript",
    version=version,
    description="TaskCluster Signing Script",
    author="Mozilla Release Engineering",
    author_email="release+python@mozilla.com",
    url="https://github.com/mozilla-releng/signingscript",
    package_data={"signingscript": ["data/*"]},
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["signingscript = signingscript.script:main"]},
    license="MPL2",
    install_requires=[
        'arrow',
        'mar',
        'signtool',
        'taskcluster',
        'requests_hawk',
        'mohawk',
        'winsign',
        'macholib',
    ],
)
