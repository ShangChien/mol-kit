from pathlib import Path
from ase.io import read
a=read(Path(Path.cwd(),'CONTCAR'))
a.pbc=False
a.cell=[0,0,0]
a.write(Path(Path.cwd(),a.symbols.get_chemical_formula()+'.gjf'),format='gaussian-in',
        mem='30GB',nprocshared='28',
        method='b3lyp', basis='6-31G*',em='GD3BJ',
        opt='',freq='',
        charge=0, mult=1,)