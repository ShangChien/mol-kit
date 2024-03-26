import os
import shutil

#清空POSCAR-2文件夹
for file in os.listdir('POSCAR-2'):
    os.remove('POSCAR-2'+'/'+file)

#选择功能
order = input('1:S1-T1计算；2：计算AIP；3：基态优化；4：计算AEA；5：UDFT计算；6：FWHM计算-基态+激发态; 7：b3lyp优化S1态; 8：b3lyp优化S1态T1态单点; 9: pysoc计算；a：M062X优化S1态; b：M062X优化S1态T1态单点; c：M062X计算UDFT; d: M062X-TDDFT优化T1态；e: M062X优化S1态TDDFT-T1单点; ')
#执行极化率输入文件准备功能
if '1' in order:
    print('准备S1-T1输入文件')

    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-S1-T1.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p td=(50-50,nstates=6) b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '')+'\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-S1-T1.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

if '2' in order:
    print('准备b3lyp泛函下AIP计算中性分子输入文件')
#b3lyp基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-b3lyp.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-b3lyp.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

if '4' in order:
    print('准备M062X泛函下AIP计算中性分子输入文件')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-b3lyp.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-b3lyp.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

# M062X正电荷计算：
if '2' in order:
    print('准备M062X泛函下VIP正电荷计算输入文件')
    # M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-b3lyp-cation.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '1 2\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-b3lyp-cation.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

# 基态优化计算：
if '3' in order:
    print('准备基态优化')
    # M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p B3LYP/6-31g(d) opt freq geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", ".gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

# M062X负电荷计算：
if '4' in order:
    print('准备M062X泛函下AIP负电荷计算输入文件')
    # M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-b3lyp-anion.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '-1 2\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-b3lyp-anion.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

if '5' in order:
    print('UDFT输入文件')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-UDFT.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq b3lyp/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 3\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-UDFT.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

if '6' in order:
    print('FWHM计算-基态')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-S0.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq pbe1pbe/6-31G* nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-S0.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))

if '6' in order:
    print('FWHM计算-激发态')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-S1.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq td=(singlets,nstates=6,root=1) pbe1pbe/6-31G* nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-S1.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if '7' in order:
    print('b3lyp优化S1态')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-B3LYP-S1-opt.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq td=(singlets,nstates=6,root=1) b3lyp/6-31g(d) nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-B3LYP-S1-opt.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if '8' in order:
    print('b3lyp优化S1态-T1态单点')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-T1.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p b3lyp/6-31g(d) nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 3\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-T1.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if '9' in order:
    print('pysoc计算')
#M062X基态计算：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%rwf=gaussian.rwf\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n# td(50-50,nstates=5) B3LYP/TZVP 6D 10F nosymm GFInput geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-py.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if 'a' in order:
    print('M062X优化S1态')
#M062X优化S1态：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-M062X-S1-opt.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq td=(singlets,nstates=6,root=1) m062x/6-31g(d) nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-M062X-S1-opt.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if 'b' in order:
    print('m062x优化S1态-T1态单点')
#m062x优化S1态-T1态单点：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-T1.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p m062x/6-31g(d) nosymm geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 3\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-T1.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if 'c' in order:
    print('M062X计算UDFT输入文件')
#M062X计算UDFT输入文件：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-M062X-UDFT.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq m062x/6-31g(d) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 3\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-M062X-UDFT.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if 'd' in order:
    print('M062X-TDDFT优化T1态')
#M062X-TDDFT优化T1态：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-M062X-TDDFT-T1-opt.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p opt freq m062x/6-31g(d) td=(triplets,nstates=3,root=1) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-M062X-TDDFT-T1-opt.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))
            
if 'e' in order:
    print('M062X优化S1态TDDFT-T1单点')
#M062X-TDDFT优化T1态：
    files = os.listdir('POSCAR')
    for file in files:
        if '.gjf' in file:
            # 原始mol文件存放的相对路径
            path_mol = 'POSCAR/' + file
            # 修改后mol文件存放的相对路径
            path_mol2 = 'POSCAR-2' + '/' + file

            content = open(path_mol, 'r')
            content_replace = open(path_mol2, 'w')

            line = content.readlines()
            line[0] = '%chk=' + file.replace('.gjf', '') + '-TDDFT-T1.chk\n'
            line[1] = '%mem=30GB\n%nprocshared=24\n#p m062x/6-31g(d) td=(triplets,nstates=3,root=1) geom=connectivity\n'
            line[3] = file.replace('.gjf', '') + '\n'
            line[5] = '0 1\n'

            for i in line:
                content_replace.write(i)
            content.close()
            content_replace.close()
            file_2 = file.replace(".gjf", "-TDDFT-T1.gjf")
            os.rename(os.path.join('POSCAR-2', file), os.path.join('POSCAR-2', file_2))