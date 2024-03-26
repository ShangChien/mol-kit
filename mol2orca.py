from pathlib import Path as P
from ase.io import read
_generator=P.cwd().glob('*.mol')
print('start...')
line1='''! B3LYP/G def2-SVP def2/J opt freq tightSCF noautostart nopop CPCM(TOLUENE)
%maxcore  7000
%pal nprocs  32 end
* xyz   0   1'''
for i in _generator:
	### read mol file
	atoms=read(i,format='mol')
	### write xyz file
	atoms.write(i.stem+'-GS-CPCM.inp',format='xyz',fmt='%14.8f')
	with open(i.stem+'-GS-CPCM.inp','r') as f:
		lines=f.readlines()
		lines[0]=line1
		lines.append('*\n')
	with open(i.stem+'-GS-CPCM.inp','w') as f:
		f.writelines(lines)
		f.close()
	print(i.stem+'.gjf converted successful;')
print('done!')
input('转换完成，输入任何字符，回车关闭窗口')