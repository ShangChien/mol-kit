import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
	name="mol-kit",
	version="0.0.4",
	author="Shang Chien",
	author_email="chennathan@163.com",
	description="This is a molecule structure file conversion library",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://ShangChien.github.io",
	packages=setuptools.find_packages(),
	classifiers=[
	    "Programming Language :: Python :: 3",
	    "Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=[
		'rich>=12.6.0',
		'rdkit>=2022.9.1',
		'xtb-python>=20.1',
		'numpy>=1.23.4',
		'pymatgen>= 2022.11.7'
		'ase>=3.22.1'
	],
	project_urls={
	  'Documentation':"https://ShangChien.github.io",
	},
)