import re
filename = 'UGWSCR_After_CFG.txt'
filename2 = 'testread1.txt'
pattern  = 'user-profile '
new_file = []

size = len(pattern)

with open('UGWSCR_After_CFG.txt','r') as fi:
    id = []
    x = 0
    copy_line = False
    for ln in fi:
        if "user-profile" in ln:
            c = ln[1]
            print(c)
            if c == 'u':
                c = ln[size]
                if c == ' ':
                    copy_line = True
        if copy_line:
            id.append ( ln[:] )
        if " " in ln :
            copy_line = False

    with open ('testing_out.txt', 'a', encoding='utf-8' ) as fo:
        fo.write ("\n".join(id))

#print(id)
