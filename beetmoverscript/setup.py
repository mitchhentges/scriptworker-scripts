import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "version.txt")) as f:
    version = f.read().rstrip()

setup(
    name="beetmoverscript",
    version=version,
    description="TaskCluster Beetmover Script",
    author="Mozilla Release Engineering",
    author_email="release+python@mozilla.com",
    url="https://github.com/mozilla-releng/beetmoverscript/",
    packages=find_packages(),
    package_data={
        "beetmoverscript": ["data/*", "templates/*"],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "beetmoverscript = beetmoverscript.script:main",
        ],
    },
    license="MPL2",
    install_requires=[
        'arrow',
        'Jinja2',
        'boto3',
        'mozilla-version',
        'redo',
        'scriptworker',
    ],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
)
