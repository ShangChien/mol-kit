from pathlib import Path as P
from pymatgen.io.gaussian import GaussianOutput

def log2gjf(fd:P) -> None:
  try:  
    ipath=fd
    opath=P(P.cwd(),fd.stem+'.gjf')
    gaussian=GaussianOutput(ipath)
    gaussianInput=gaussian.to_input(mol=None,
      link0_parameters={'%mem':'30GB','%NProcShared':'32','%chk':fd.stem+'.chk'},  
      functional='B3LYP', basis_set='6-31g(d)', 
      route_parameters={'opt':'','freq':''}, 
      input_parameters=None, dieze_tag='#p', 
      title='generate by template', 
      charge=0, spin_multiplicity=1,
      cart_coords=True,
    )
    gaussianInput.write_file(opath,cart_coords=True)
    print(ipath.stem+'.gjf converted successful;')
  except:
    print(fd.stem+'.gjf converted failed;')

_generator=P.cwd().glob('*.log')
for _file in _generator:
  log2gjf(_file)
input('finished')