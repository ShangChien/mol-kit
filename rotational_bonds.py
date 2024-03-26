from pathlib import Path

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def rotational_text(file_name=''):
    def get_surround_bond(bond_current=[],i=0):
        bond_searched=[]
        bond_searched.append(bond_current)
        point_searched=[]
        def get_another_point(start):
            end_point=[]
            point_searched.append(start)
            for bond in bonds: 
                if (start in bond[:-1]) and (bond not in bond_searched):
                    another_point=bond[0] if bond[1]==start else bond[1]
                    if another_point not in point_searched:
                        end_point.append(another_point)
                        bond_searched.append(bond)
            return end_point
        end_point1=get_another_point(start=bond_current[i])
        end_point2=[]
        for point in end_point1:
            end_point2.extend(get_another_point(start=point))
        end_point3=[]
        for point in end_point2:
            end_point3.extend(get_another_point(start=point))
        return bond_searched
    with open(file_name,'r') as f:
        lines=f.readlines()
    start_atom=4
    for index,line in enumerate(lines):
        try:
            if line.split()[3].isalpha() and is_number(line.split()[0]) and is_number(line.split()[1]) and is_number(line.split()[2]) :
                start_atom=index
                break
        except:
            pass
    H_index=[]
    for index,line in enumerate(lines[start_atom:]):
        try:
            if line.split()[3].isalpha():
                if line.split()[3]=='H':
                    H_index.append(index+1)
            else:
                end_atom=index+start_atom
                num_atom=index
                start_bond=end_atom
                break
        except:
            pass
    bonds=[]
    m=len(str(num_atom))
    for index,line in enumerate(lines[start_bond:-1]):
        if line.split()[2]!='0':
            bonds.append(line.split()[0:3])
        else:
            bond=[]
            bond.append(line.split()[0][:-m])
            bond.append(line.split()[0][-m:])
            bond.append(line.split()[1])
            bonds.append(bond)
    bond_without_h=[]
    for bond in bonds:
        if not (int(bond[0]) in H_index or int(bond[1])in H_index) :
            bond_without_h.append(bond)
    rotational_bonds=[]
    for bond in bond_without_h:
        if bond[2]=='1':
            rotational_bonds.append(bond)
    text_list=[]
    for bond in rotational_bonds:
        left=get_surround_bond(bond_current=bond,i=0)
        right=get_surround_bond(bond_current=bond,i=1)
        num_same_bonds=len([x for x in left if x in right])
        if num_same_bonds==1:
            for b in bonds: 
                if (bond[0] in b[:-1]) and (b!=bond):
                    another_point1=b[1] if b[0]==bond[0] else b[0]
                    for b2 in bonds:
                        if (bond[1] in b2[:-1]) and (b2!=bond):
                            another_point2=b2[1] if b2[0]==bond[1] else b2[0]
                            text_list.append([another_point1,bond[0],bond[1],another_point2])
                            break
                    break
                  
    return text_list

if __name__=="__main__":
    p=Path.cwd()
    print(p)
    for file in p.glob('in/*.mol'):
        text=rotational_text(file_name=file)
        text1=[]
        for t in text:
            t.append('F\n')
            t.insert(0,'D')
            text1.append(' '.join(t))
        inter_path=file.name.split('.',-1)[0]
        for file1 in p.glob(inter_path+'/RE/*.com'):
            with open(file1,'r') as f:
                lines=f.readlines()
                method=lines[3].split(' ',-1)
                method[1]='opt=modredundant'
                lines[3]=' '.join(method)
                lines.extend(text1)
                lines.append('\n')
                lines.append('\n')
            print('write:'+file1.as_posix()+'\n'+''.join(text1))
            with open(file1,'w') as f:
                f.writelines(lines)
                f.close()


