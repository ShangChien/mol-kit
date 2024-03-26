from pathlib import Path
for file in Path.cwd().glob('*.gjf'):###只会转换后缀为.gjf的文件
    line1 = file.name.partition('.')[0]
    with open(file,'r') as f:
        lines=f.readlines()
        lines[0]='%chk='+line1+'-cosmors.chk\n'
        lines[1]='%mem=10GB\n'
        lines[2]='%nprocshared=60\n'
        lines[3]='#p BP86/def2TZVP scrf=cosmors geom=connectivity\n' 
        lines.append(line1+'.cosmo\n'+'\n')   
    with open(file,'w') as f:
        f.writelines(lines)
        f.close()