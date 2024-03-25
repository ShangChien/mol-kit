# [mol-kit](https://pypi.org/project/mol-kit/ 'mol-kit docs')

# install:
``` sh
pip install mol-kit
```

## This library currently has several main features:

- handle input file format conversions for DFT calculation (such as: ORCA, GAUSSIAN, VASP...) 
- handle file format conversions for visualization molecule 2D&3D structure.
- fast and robust conformer calculation (need [xtb-python](https://xtb-python.readthedocs.io/en/latest/installation.html 'xtb-python install tutorial') installed)
	- this feature stands on the shoulders of [rdkit](https://github.com/rdkit 'rdkit github') and [xtb](https://github.com/grimme-lab/xtb 'xtb github')
	- usage:
		- python ./mol-kit.py -w 3 -ag FIRE -i in -o out 
		- '--weight', '-w', 
		Number of conformations sampled per molecule = Rotatable molecular bonds * weight', default=3;
		- '--algorithm', '-ag', 
		Structural optimization iterative algorithm, LBFGS,FIRE', default='FIRE';
		- '--in_path', '-i', 
		Folder of molecules to be calculated, default='in';
		- '--out_path', '-o',
		Folder for the result output', default='out'
