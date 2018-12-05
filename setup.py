from setuptools import setup, find_packages

setup(
    name='adventofcode2018',
    version='0.1.0',
    url='https://github.com/mattupstate/adventofcode2018',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    include_package_data=True,
    platforms='any'
)
