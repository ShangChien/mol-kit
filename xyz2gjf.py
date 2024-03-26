from pathlib import Path as P
from ase.io import read
_generator=P.cwd().glob('*.log')
print('start...')
for i in _generator:
	### read xyz file
	atoms=read(i)
	### write gjf file
	atoms.write(i.stem+'.gjf',format='gaussian-in',chk=i.stem+'.chk',  # type: ignore
				mem='30GB',nprocshared='32',
        method='b3lyp', basis='6-31g(d)',
        opt='',freq='',
        charge=0, mult=1,)
	print(i.stem+'.gjf converted successful;')
print('done!')
input('转换完成，输入任何字符，回车关闭窗口')

