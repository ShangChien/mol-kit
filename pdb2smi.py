from pathlib import Path as P
from rdkit import Chem
_generator=P.cwd().glob('*.pdb')
print('start...')
for i in _generator:
	### read pdb file
	mol=Chem.MolFromPDBFile(i.as_posix())
	### write smiles file
	smi = Chem.MolToSmiles(mol)
	print('smi: ',smi)
	### write smi file
	with open(i.stem+'.smi','w') as f:
		f.write(smi)
print('done!')
input('转换完成，输入任何字符，回车关闭窗口')