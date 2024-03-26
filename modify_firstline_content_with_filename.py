from pathlib import Path
for file in Path.cwd().glob('*.mol'):###只会转换后缀为.mol的文件
    line1 = file.name.partition('.')[0]+'\n'
    with open(file,'r') as f:
        lines=f.readlines()
        lines[0]=line1
    with open(file,'w') as f:
        f.writelines(lines)
        f.close()