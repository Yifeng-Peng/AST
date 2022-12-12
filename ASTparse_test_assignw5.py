#from ASTplot import treeplot
import numpy as np
import glob
from graphviz import Digraph
from collections import Counter
import linecache
import shutil, sys, os
import time
import shutil




noneed = ["detailed","SCOPE","TOPSCOPE"]
need1 = ["VAR"]
need2 = ["VARREF"]
stop = ["CSTMT"]   ####################简化AST
need3 = ["VAR","VARREF","AND","OR","XOR","ADD","NOT"]

noneed2 = ["CCAST"]
noneed3 = ["SCOPE"]
noneed4 = ["TOPSCOPE"]
def isInArray(array, line):
    for item in array:
        if item in line:
            return True
    return False


time_start = time.time() #timer
fname = r'Treefiles/Vs38584.txt'#---------------------------------------------------------------------------------------------------改文件名字
fresult = r'Process/Vs38584_1.txt'#---------------------------------------------------------------------------------------------------改文件名字
# open(fname, 'r', encoding='gb2312')
with open(fname, 'r', encoding='UTF-8') as f:
    with open(fresult, 'w', encoding='UTF-8') as g:
        for line in f.readlines():
            if not isInArray(noneed, line):  # 不含noneed里面字符的行 都要
                g.write(line)
            # if not isInArray(noneed2, line):  # 不含noneed里面字符的行 都要
            #     g.write(line)
            # if not isInArray(noneed3, line):  # 不含noneed里面字符的行 都要
            #     g.write(line)
            # if not isInArray(noneed4, line):  # 不含noneed里面字符的行 都要
            #     g.write(line)
# create Node class for features


# create Node class for features

# fname = r'set01.txt'
# fresult = r'set02.txt'
# # open(fname, 'r', encoding='gb2312')
# with open(fname, 'r', encoding='UTF-8') as f:
#     with open(fresult, 'w', encoding='UTF-8') as g:
#         for line in f.readlines():
#             if not isInArray(stop, line):  # 不含noneed里面字符的行 都要
#                 g.write(line)
# create Node class for features



detaset = glob.glob('Process/Vs38584_1.txt')#---------------------------------------------------------------------------------------------------改文件名字
Node = []

for deta in detaset:
    result_name = []
    result_edge = []
    result_const = []
    result_var = []
    result_varref = []
    result_width = []

    with open(deta) as d:
        for line in d:
            #cells = line0.replace('}', '{').split('{')
            #line1= line.replace(':', ' ')
            #detailed
            #line0.replace('}', '{').split('{')

            name = line.split()[1]
            result_name.append(name)
        result_name = np.array(result_name)
        result_name = result_name[2:]


    with open(deta) as d:
        for line in d:
            #line1 = line.replace(':','')
            #line = line.replace('detailed', '')
            line1 = line.replace(':', '')
            position = line1.split()[0]
            result_edge.append(position)
        result_edge = np.array(result_edge)
        result_edge = result_edge[2:]


    with open(deta) as d:
        for line in d:
            const = line.split()[-1]
            result_const.append(const)
        result_const = np.array(result_const)
        result_const = result_const[2:]


    with open(deta) as d:
        for line in d:
            if isInArray(need1, line):
                var = line.split()[6]
                result_var.append(var)

            else:
                result_var.append(1)
        result_var = np.array(result_var)
        result_var = result_var[2:]


    with open(deta) as d:
        for line in d:
            if isInArray(need2, line):
                varref = line.split()[6]
                result_varref.append(varref)

            else:
                result_varref.append(1)
        result_varref = np.array(result_varref)
        result_varref = result_varref[2:]

    with open(deta) as d:
        for line in d:
            if isInArray(need3, line):
                width = line.split()[5]
                result_width.append(width)

            else:
                result_width.append(0)
        result_width = np.array(result_width)
        result_width = result_width[2:]


loop = len(result_name)
names = globals()

print(result_edge)
print(result_name)
print(result_const)
print(result_var)
print(result_varref)
print(result_width)



print(len(result_name))
print(len(result_edge))
print(len(result_const))
print(len(result_var))
print(len(result_varref))
print(len(result_width))

class Node:
    name = ''
    edge = ''
    const = ''

    def __init__(self, n, e, c):
        self.name = n
        self.edge = e
        self.const = c


names = globals()
# Nodeset = []
# Node = Node(result_name[1], result_edge[1], result_const[1])
# Nodeset.append(Node)
# Nodeset = np.array(Nodeset)
# print(Nodeset[0])
k = 0
while k < loop:
    if "CONST" == result_name[k]:
        # Node = Node(result_name[k], result_edge[k], result_const[k])
        names['Node%s' % k] = Node(result_name[k], result_edge[k], result_const[k])
        k = k + 1
    # if result_name[k] == "VAR":
    #     # Node = Node(result_name[k], result_edge[k], result_const[k])
    #     names['Node%s' % k] = Node(result_name[k], result_edge[k], result_var[k])

    if "VARREF" == result_name[k]:
        # Node = Node(result_name[k], result_edge[k], result_const[k])
        names['Node%s' % k] = Node(result_name[k], result_edge[k], result_varref[k])
        k = k +1

    else:
        names['Node%s' % k] = Node(result_name[k], result_edge[k], '')
        k = k + 1


print("********************************************************")

#     example
print('Testing')
print('Const:',Node3.const)
print('Name:',Node3.name)
print('Edge:',Node3.edge)
print('LENGTH:',len(result_edge[2]))
print('End')
print("**********************-----CREATE AST-----**************************")
# Create part

dot = Digraph(comment='The Test Table')

parts = locals()
j = 0
while j < len(result_name):
    # a = parts['Node%s' % j]
    if result_name[j]=='CCAST':
        j = j + 1
    if result_name[j] == 'VAR':
        j = j + 1

    else:
        dot.node('{}'.format(j), '{}'.format(result_name[j]))
        if result_name[j]=='CONST':
        # dot.node('{}'.format(j), '{}'.format(result_name[j]))
            dot.node('{}'.format(j), '{} {}'.format(result_name[j],result_const[j]))
        if result_var[j]!='1':
        # dot.node('{}'.format(j), '{}'.format(result_name[j]))
            dot.node('{}'.format(j), '{} {}'.format(result_name[j],result_var[j]))
        if result_varref[j]!='1':
        # dot.node('{}'.format(j), '{}'.format(result_name[j]))
            dot.node('{}'.format(j), '{} {}'.format(result_name[j],result_varref[j]))
        if result_name[j] == 'CSTMT':  ##简化 AST 只取需要的部分
            break

        j = j+1



#### edge features
###dot.edge('1', '15')
l = 0
n = 0
m = 0
o = 0
f = 0
z = 0
x = 0
y = 0
z = 0
a = 0
b = 0
p = 0
CASE2 = []
CASE3 = []
CASE4 = []
CASE5 = []
CASE6 = []
CASE7 = []
CASE8 = []
CASE9 = []
CASE10 = []
CASE11 = []
CASE12 = []
CASE13 = []
CASE14 = []


while l < len(result_edge)-2:

    # if len(result_edge[l]) == 2:
    #     z = 0
    #     while z <= l:
    #
    #         if len(result_edge[z]) == len(result_edge[l]) - 1:
    #             CASE9.append(z)
    #             z = z + 1
    #         else:
    #             z = z + 1
    #     print('case00')
    #     l = l + 1

    # if len(result_edge[l]) == 1:
    #     print('case0')
    #     l = l + 1

    #dot.node('{}'.format(j)

    if result_name[l] == "CCAST":
        print("IGNORE")
        l = l + 1

    if result_name[l] == "VAR":
        print("IGNORE1")
        l = l + 1

    if len(result_edge[l]) > len(result_edge[l - 1]) :

        if result_name[l] == "VAR":
            print("IGNORE1")
            l = l + 1

        if result_name[l] == "CCAST":
            print("IGNORE")
            l = l + 1

        if result_name[l-1] == 'CSTMT':  ##简化 AST 只取需要的部分
            print('END')
            break


        # if result_name[l] == '{}'.format(l):
        #     l = l + 1

        if len(result_edge[l]) == 1 :
            print('case1')
            l = l + 1


        if result_name[l-1] == "CCAST":
            p  = 0
            while p <= l:
                if len(result_edge[p]) == len(result_edge[l]) - 2:
                    CASE14.append(p)
                    p = p + 1
                else:
                    p = p + 1
            dot.edge('{}'.format(CASE14[-1]), '{}'.format(l))
            print('case1.1')
            l = l + 1

        else:
            if l < len(result_edge) - 2:
                dot.edge('{}'.format(l-1), '{}'.format(l))
        # dot.edges(['{}{}'.format(l - 1, l)])
        # print(['{}{}'.format(l - 1, l)])
                print('case1.2')
                l = l + 1

    # if len(result_edge[l]) == len(result_edge[l - 1]):
    #     #如果是4出现的话应该是前三个，这个要根据后面的大量数据来改，没有4出现的话暂时不用改
    #     #dot.edges(['{}{}'.format(l - 2, l)])
    #     # if result_name[l] == result_name[l-1]:
    #     #  dot.edge('{}'.format(0), '{}'.format(l))
    #     #  print('case2.1')
    #     #  l = l + 1
    #     if result_name[l] == result_name[l-1]:##length 相等，但是大于前一个， 连接自己本来退一位的最近一个node
    #
    #         while n <= l:
    #             if len(result_edge[n]) == len(result_edge[l])-1:
    #                 CASE2.append(n)
    #                 n = n + 1
    #             else:
    #                 n = n + 1
    #         dot.edge('{}'.format(CASE2[-1]), '{}'.format(l))
    #         print('case2.1')
    #         l = l + 1
    #
    #
    #     if result_name[l] > result_name[l-1]:
    #         dot.edge('{}'.format(l-1), '{}'.format(l))
    #         print('case2.2')
    #         l = l + 1
    #
    #
    #
    #     else :
    #         dot.edge('{}'.format(0 ), '{}'.format(l))
    #         print('case2.3')
    #         l = l + 1

    if len(result_edge[l]) == len(result_edge[l - 1]) :
        # 如果是4出现的话应该是前三个，这个要根据后面的大量数据来改，没有4出现的话暂时不用改
        # dot.edges(['{}{}'.format(l - 2, l)])
        # if result_name[l] == result_name[l-1]:
        #  dot.edge('{}'.format(0), '{}'.format(l))
        #  print('case2.1')
        #  l = l + 1

        if result_name[l] == "VAR":
            print("IGNORE1")
            l = l + 1


        if result_name[l] == "CCAST":
            print("IGNORE")
            l = l + 1


        if result_name[l] == 'CSTMT':  ##简化 AST 只取需要的部分
            print('END')
            break


        # if result_name[l] == '{}'.format(l):
        #     l = l +1

        if len(result_edge[l]) == 1 :

            print('case2.1')

            l = l + 1

        # if len(result_edge[l])== 2:
        #     dot.edge('{}'.format(1), '{}'.format(l))
        #     l = l + 1




        if len(result_edge[l]) > 2 :
            if result_name[l-1] == "CCAST":
                n  = 0
                while n <= l:
                    if len(result_edge[n]) == len(result_edge[l]) - 2 :
                        CASE2.append(n)
                        n = n + 1
                    else:
                        n = n + 1

                if l < len(result_edge) - 2 :
                    dot.edge('{}'.format(CASE2[-1]), '{}'.format(l))
                    print('case2.2')
                    l = l + 1
            else:
                a = 0
                while a <= l:
                    if len(result_edge[a]) == len(result_edge[l]) - 1 :
                        CASE12.append(a)
                        a = a + 1
                    else:
                        a = a + 1
                if l < len(result_edge) - 2:
                    dot.edge('{}'.format(CASE12[-1]), '{}'.format(l))
                    print('case2.3')
                    l = l + 1
        else:
            dot.edge('{}'.format(0), '{}'.format(l))
            print('case2.4')
            l = l + 1




    if len(result_edge[l]) < len(result_edge[l - 1])  :
        # 这里的-4取决于前面的数量的多少，还需要继续修改，再分成多个case
        #dot.edges(['{}{}'.format(l - 4, l)])
        #dot.edge('{}'.format(l - 4), '{}'.format(l))

        # if len(result_edge[l])== 2:
        #     dot.edge('{}'.format(1), '{}'.format(l))
        #     l =  l + 1

        if result_name[l] == "VAR":
            print("IGNORE1")
            l = l + 1


        if result_name[l] == "CCAST":
            print("IGNORE")
            l = l + 1


        if result_name[l] == 'CSTMT':  ##简化 AST 只取需要的部分
            print('END')
            break




        # if result_name[l] == '{}'.format(l):
        #     l = l + 1

        if len(result_edge[l])== 2:
            y = 0
            while y <= l:
                if len(result_edge[y]) == 1 :
                    CASE8.append(y)
                    y = y + 1

                else:
                    y = y + 1
            if l < len(result_edge) - 2:
                dot.edge('{}'.format(CASE8[-1]), '{}'.format(l))
                print('case3.1')
                l = l + 1

        if len(result_edge[l]) == 1 :
            print('case3.2')
            l = l + 1


        if result_name[l - 1] == "CCAST":
            if len(result_edge[l]) > 2:
                m = 0
                while m <= l:
                    if len(result_edge[m]) == len(result_edge[l]) - 2  :

                        CASE3.append(m)

                        m = m + 1
                    else:
                        m = m + 1
                if l < len(result_edge) - 2:
                    dot.edge('{}'.format(CASE3[-1]), '{}'.format(l))

                    print('case3.3')
                    l = l + 1
            else:
                dot.edge('{}'.format(0), '{}'.format(l))
                print("case3.4")
                l  = l + 1
        else:
            b = 0
            while b <= l:
                if len(result_edge[b]) == len(result_edge[l]) - 1:
                    CASE13.append(b)
                    b = b + 1
                else:
                    b = b + 1
            if l < len(result_edge) - 2:
                dot.edge('{}'.format(CASE13[-1]), '{}'.format(l))
                print('case3.5')
                l = l + 1





print(dot.source)
#dot.view()
#                                                 处理宽度数据切片
result_w = []
xy = 0
while xy < loop:
    if result_width[xy] !='0':
        str1 = result_width[xy]
        re1 = str1.split('/')
        re1 = str1.replace(')','')
        print(re1)
        re2 = re1[-1]
        result_w.append(re2)
        xy = xy +1
    else:
        result_w.append('')
        xy = xy +1
# result_var = result_var[2:]
print("----------------------------------WIDTH----------------------------------------------")
#result_w = result_w.replace(')', '')
print(result_w)

loop = len(result_name)
w =0
reline= ''
print('-------------------------------------CREATE RELOAD TXT---------------------------------------------------------')
#f = open('create.txt',mode='{}.txt'.format(result_name[0]))   tracing003
f = open('Process/Vs38584_re.txt', mode='w')#---------------------------------------------------------------------------------------------------改文件名字
while w < loop:
    print('$$$$$$$$$$$$$$$$$$')
    #a = 'Node{}'.format(w)
    #print(a.const)
    print("NODE: ", w,"CONST OR VAR: " ,vars()['Node{}'.format(w)].const)
    #f.write("NODE: ", w,"CONST: " ,vars()['Node{}'.format(w)].const)
    # b = 'Node{}'.format(w)
    # print(b.name)
    print("NODE: ",w , "NAME: ", vars()['Node{}'.format(w)].name)
    # c = 'Node{}'.format(w)
    # print(c.edge)
    #f.write("NODE: ",w , "NAME: ", vars()['Node{}'.format(w)].name)

    print("NODE:",w , "EDGE； " , vars()['Node{}'.format(w)].edge)
    #f.write("NODE:",w , "EDGE； " , vars()['Node{}'.format(w)].edge)
    if result_name[w] == 'CSTMT':
        print('END')
        break
    else:
        reline = '{} {} {} {} '.format(w,vars()['Node{}'.format(w)].edge,vars()['Node{}'.format(w)].name,vars()['Node{}'.format(w)].const)
        f.writelines(reline)
    #f.write(reline)
        f.write('\n')
        w = w + 1
f.close()



wl =0
reline= ''
print('------------------------------CREATE FEATURE---------------------------------------')
#f = open('create.txt',mode='{}.txt'.format(result_name[0]))   tracing003
fl = open('Process/Vs38584_f.txt', mode='w')#---------------------------------------------------------------------------------------------------改文件名字
while wl < loop:
    if result_name[wl] == 'CSTMT':
        print('END')
        break
    if result_name[wl] == 'CONST':
        reline = '{} {}'.format(vars()['Node{}'.format(wl)].name, result_const[wl])
        fl.writelines(reline)
        # f.write(reline)
        fl.write('\n')
        wl = wl + 1
    else:
        reline = '{} {}'.format(vars()['Node{}'.format(wl)].name , result_w[wl])
        fl.writelines(reline)
    #f.write(reline)
        fl.write('\n')
        wl = wl + 1

# reline2 = 'Total bits =  '.format(vars()['Node{}'.format(5)].const)
# fl.writelines(reline)
# fl.write('\n')
fl.close()


flname = r'Process/Vs38584_f.txt'#---------------------------------------------------------------------------------------------------改文件名字
flresult = r'Process/Vs38584_feature.txt'#---------------------------------------------------------------------------------------------------改文件名字
delete=["CSTMT","CFUNC","ASSIGN","CCAST","CALL","VAR","COMMENT","SHIFTR","MODULE","IF"]
GET1=["ASSIGNDLY","ASSIGNW"]
# open(fname, 'r', encoding='gb2312')
with open(flname, 'r', encoding='UTF-8') as fl:
    with open(flresult, 'w', encoding='UTF-8') as k:
        for line in fl.readlines():
            if isInArray(GET1, line):  # 不含noneed里面字符的行 都要
                 k.write(line)
            if not isInArray(delete, line):  # 不含noneed里面字符的行 都要
                k.write(line)

        # reline2 = 'Total bits =  '.format(vars()['Node{}'.format(5)].const)
        # k.writelines(reline)
        # k.write('\n')

#----------------------------------计算bits mux等

detaset2 = glob.glob('Process/Vs38584_feature.txt')#---------------------------------------------------------------------------------------------------改文件名字

for deta in detaset2:
    width0 = []
    name2 = []
    with open(deta) as d:
        for line in d:
            #cells = line0.replace('}', '{').split('{')
            #line1= line.replace(':', ' ')
            #detailed
            #line0.replace('}', '{').split('{')

            name = line.split()[0]
            name2.append(name)
        name2 = np.array(name2)
    with open(deta) as d:
        for line in d:
            # cells = line0.replace('}', '{').split('{')
            # line1= line.replace(':', ' ')
            # detailed
            # line0.replace('}', '{').split('{')

            wid = line.split()[-1]
            width0.append(wid)
        width0 = np.array(width0)




print("--------------------------------BITS COUNTING-------------------------------")
print('name2')
print(name2)
print('width0')
print(width0)
k1 = len(name2)
k2 = 0
k22 = 0
k222 = 0
k33 = 0
while k33 < k1:
    if name2[k33] == "COND":
        # name2[k2].replace("COND","MUX")
        width0[k33]= 1
        k33 = k33 +1
    if name2[k33] == "ASSIGNDLY":
        # name2[k2].replace("COND","MUX")
        name2[k33] = "Flip-Flop"                                   #------------------------------根据assigndly的数量来找ff的数量
        width0[k33]= 1
        k33 = k33 +1
    if name2[k33] == "ASSIGNW":
        # name2[k2].replace("COND","MUX")
        width0[k33] = 1
        k33 = k33 + 1
    else:
        k33 = k33 +1
print('更新后的WIDTH0')
print(width0)

#------------------------------------------------------------处理DFF-------------------------
# if "ASSIGNDLY" in name2:



while k2 < k1:
    if name2[k2] == "COND":
        # name2[k2].replace("COND","MUX")
        name2[k2]="MUX"
        k2 = k2 +1
    # if name2[k2] == "ASSIGNDLY":
    #     name2[k2] = "Flip-Flop"
    #     k2 = k2 + 1
    else:
        k2 = k2 +1
print('Name2')
print(name2)
#------------------------------------------------------------删除不需要的AND----------------------------------
while k222 < k1:
    if k222 == len(name2)-1:
        break
    if name2[k222] == "AND":#------------------------------------暂时定为如果AND没用，CONST会马上跟在后面，可能还要继续改
        if name2[k222+1] == "CONST":
            #b = np.delete(a, index)
            name2=np.delete(name2,k222)
            width0=np.delete(width0,k222)
        else:
            k222 = k222 + 1
    else:
        k222 = k222 + 1


k223= 0
if 'Flip-Flop' in name2:
    name2 = name2
    width0 = width0
    print('有DFF')
    print(name2)
    print(width0)
else:
    while k223 < k1:
        if k223 == len(name2)-1:
            break
        if name2[k223] == "ASSIGNW":
            name2 = np.delete(name2, k223)
            width0 = np.delete(width0, k223)
            k223 = k223 + 1
        else:
            k223 = k223 + 1
    print('无DFF')
    print(name2)
    print(width0)



k1 = len(name2)


while k22 < k1:
    if name2[k22] == "MUX":
        # name2[k2].replace("COND","MUX")
        width0[k22]= 0
        k22 = k22 +1
    else:
        k22 = k22 +1
print('先处理MUX的位数之后的width0')
print(width0)

k23 = 0
bit2 = []
while k23 < k1:
    if name2[k23] == "Flip-Flop":
        # name2[k2].replace("COND","MUX")
        k23 = k23 +1
        bit2.append(k23)
    else:
        k23 = k23 +1
print('FF的位置')
print(bit2)

k3 = 0
k4 = 1
while k3 < k1:
    if name2[0] == "CONST":
        if name2[k3] == "CONST":
            if k3 == k1 -1:
                break
            if name2[k3+1] == "CONST":
                k3 = k3 + 1
                k4 = k4 + 1
            if name2[k3-1] == "CONST":
                k3 = k3 + 1
                k4 = k4 + 1
            else:
                while k4 < k1:
                    if name2[k4]== "CONST":
                        break
                    width0[k3+1]=width0[k3]
                    k3 = k3 + 1
                    k4 = k4 + 1
        else:
            k3 = k3 + 1
            k4 = k4 + 1

    if name2[0] != "CONST":
        if name2[k3] == "CONST":
            if k3 == k1 - 1:
                break
            if name2[k3 + 1] == "CONST":
                k3 = k3 + 1
                k4 = k4 + 1
            if name2[k3 - 1] == "CONST":
                k3 = k3 + 1
                k4 = k4 + 1
            else:
                while k4 < k1:
                    if name2[k4] == "CONST":
                        break
                    width0[k3 - 1] = width0[k3]
                    k3 = k3 + 1
                    k4 = k4 + 1
        else:
            k3 = k3 + 1
            k4 = k4 + 1
    else:
        k3 = k3 + 1
        k4 = k4 + 1

print('处理CONST和AND之后的width0')
print(width0)


#--------------------------------------------------------十六进制转换器----------------------------------------------






def change_chars(a):#a 是初始的十六进制的所有数组，就是 width
    """将十六进制中的字符转化为十进制的字符"""
    hex_list = a
    # print(hex_list)
    for u in hex_list:
        if u == 'a':
            i = hex_list.index('a')
            hex_list[i] = '10'
        elif u == 'b':
            i = hex_list.index('b')
            hex_list[i] = '11'
        elif u == 'c':
            i = hex_list.index('c')
            hex_list[i] = '12'
        elif u == 'd':
            i = hex_list.index('d')
            hex_list[i] = '13'
        elif u == 'e':
            i = hex_list.index('e')
            hex_list[i] = '14'
        elif u == 'f':
            i = hex_list.index('f')
            hex_list[i] = '15'
        else:
            pass
    return hex_list

width2 = []


width3 = []###########十进制
k5  =  0
while k5 < k1:

    str2 = width0[k5]
    re3 = str2.split('h')
    re4 = re3[-1]
    width2.append(re4)
    k5 = k5 +1

print('width2')
print(width2)


k55 = 0
while k55 < k1:
    if width2[k55] == "ASSIGNDLY":
        width2[k55] = 1
        k55 = k55 + 1
    else:
        k55 =  k55 +1

"""将十六进制转成十进制"""
k11 = 0
while k11 < k1:
    #'Node{}'.format(wl)
    j = '0x{}'.format(width2[k11])
    num = eval(j)
    width3.append(num)
    k11 = k11 +1

print("width3,转换后的十进制数组是 ： ",width3)

# number = int(input())
# binnum = bin(number)
# print(binnum)

k6= 0
#"""将十六进制转成二进制，不足四位补零"""

"""将十进制转成二进制"""

width4 = []
while k6 < k1:
    if k6 == k1 :
        break
    if name2[k6]=="CONST"or name2[k6]=="MUX":
        j = int(width3[k6])
        num = bin(j)
        width4.append(num)
        k6 = k6 + 1
    else:
        width4.append(width3[k6])
        k6 = k6 + 1

print("width4,转换后的二进制数组是 ： ",width4)
print(name2)


k7 = 0
width5 =[]
while k7 < k1:
    if k7 == k1 :
        break
    if name2[k7] == "CONST" or name2[k7]=="MUX":
        str2 = width4[k7]
        re3 = str2.split('b')
        re4 = re3[-1]
        width5.append(re4)
        k7 = k7 +1
    else:
        width5.append(width3[k7])
        k7 = k7 + 1
print("width5,转换后的二进制数组表示是 ： ",width5)
print(name2)


def int_Conter(n):
    bin_n = n
    dict_bin = Counter(bin_n)
    for k, v in dict_bin.items():
        if k == '1':
            return v


k71 = 0
while k71 < k1 :
    if k71== k1:
        break
    if name2[k71] == "CONST":
        #width5[k71]= int_Conter(width5[k71])
        a = int_Conter(width5[k71])
        if a == None:
            width5[k71] = width5[k71]
            k71 = k71 + 1
        else:
            width5[k71] = a
            k71 = k71 + 1
    else:
        k71 = k71 +1

print("width5,MUX的真实bits 数组：",width5)
print(name2)


k8 = 0
width6  = []
while k8 < k1:
    if k8 == k1 :
        break
    if name2[k8] == "CONST":
        if width5[k8]==1:
            width6.append(1)
            k8 = k8 + 1

        else:
            num = len(width5[k8])
            width6.append(num)
            k8 = k8 + 1
    if k8 == k1:
        break
    if name2[k8] == "MUX":
        width6.append(width5[k8])
        k8 = k8 + 1
    else:
        width6.append(width3[k8])
        k8 = k8 + 1
print("width6,转换后的二进制数组相对应的位数是 ： ",width6)
print(name2)


kl = 0
OUTposition = []
while kl < len(result_name):
    if "OUTPUT" in linecache.getline('Process/Vs38584_1.txt', kl) and len(result_edge[kl]) == 2:#-------------------------------------------------------------改文件名字
        OUTposition.append(kl)
        kl = kl + 1
    else:
        kl = kl + 1


print("OUTPUT的原始行数位置")
print(OUTposition)


klc = 0
CFUNCposition = []
while klc < len(result_name):
    if "CFUNC" in linecache.getline('Process/Vs38584_1.txt', klc):#-------------------------------------------------------------改文件名字
        CFUNCposition.append(klc)
        klc = klc + 1
    else:
        klc = klc + 1

print("CFUNC的原始行数位置")
print(CFUNCposition)


kla = 0
DLYposition = []
while kla < len(result_name):
    if "ASSIGNDLY" in linecache.getline('Process/Vs38584_1.txt', kla):#-------------------------------------------------------------改文件名字
        DLYposition.append(kla)
        kla = kla + 1
    else:
        kla = kla + 1

print("ASSIGNDLY的原始行数位置")
print(DLYposition)


klw = 0
AWposition = []
while klw < len(result_name):
    if "ASSIGNW" in linecache.getline('Process/Vs38584_1.txt', klw):#-------------------------------------------------------------改文件名字
        AWposition.append(klw)
        klw = klw + 1
    else:
        klw = klw + 1

print("ASSIGNW的原始行数位置")
print(AWposition)



E1 = DLYposition[0]
i14 = 0
CFUNC2 = 0
while i14 < len(CFUNCposition):
    if CFUNCposition[i14] > E1:                # DLY 出现之后的 第一个CFUNC 的行数位置
        CFUNC2 = CFUNCposition[i14+1]                     # 这个CFUNC2 就不应该继续打开了
        i14 = i14 +1
        break
    else:
        i14 = i14 + 1

print("Parser应该结束的CFUNC的位置", CFUNC2)




ENDD2 = 0
i15 = 0

while i15 < len(AWposition):
    if AWposition[i15] > CFUNC2:                                 #       DLY出现后的第一个CFUNC结束的assignw的行数位置
        ENDD2 = i15
        i15 = i15 +1
        break
    else:
        i15 = i15 + 1

    if i15 == len(AWposition)-1:
        ENDD2 = i15

ENDD3 = ENDD2+1
print("DLY的CFUNC结束，第一个ASSIGNW的位置", ENDD2)                    #ENDD2表示一个结束的时候的ASSIGNW的个数，第ENDD2个ASSIGNW应该结束
print("DLY的CFUNC结束后，第一个ASSIGNW的个数", ENDD3)                     #              第 ENDD3个assigndw应该结束

i16 = 0
ENDD4 = 0
while i16 < len(AWposition):
    if AWposition[i16] > DLYposition[-1]:
        ENDD4 = i16
        i16 = i16 + 1
        break
    else:
        i16 = i16 +1

print("ASSIGNDLY结束之后的第一个Assignw的位置", ENDD4)

E_condition =  ENDD3 - ENDD4                                         #           应该计算的ASSIGNDLY 之后ASSIGNW的个数
print("AST PARSER 的结束条件是， Assignw只取  ",E_condition)

TEE = 0
FFPOSI = []
while TEE < len(name2):
    if name2[TEE]== "Flip-Flop":
        FFPOSI.append(TEE)
        TEE = TEE +1
    else:
        TEE = TEE + 1

print("FF在数组中的位置")
print(FFPOSI)
print(len(FFPOSI))


AEE = 0
ASSIGNPOSI = []
while AEE < len(name2):
    if name2[AEE]== "ASSIGNW":
        ASSIGNPOSI.append(AEE)
        AEE = AEE +1
    else:
        AEE = AEE + 1

print("ASSIGNW在数组中的位置")
print(ASSIGNPOSI)
print(len(ASSIGNPOSI))



wl = 0                        #确认ASSIGNW从哪里开始取值，这里是从第一个开始取值
reline= ''
WLL=0
kk = 0
START = 0
print('------------------------------CREATE FEATURE BITS---------------------------------------')
#f = open('create.txt',mode='{}.txt'.format(result_name[0]))   tracing003
fl = open('Process/Vs38584_T.txt', mode='w')#---------------------------------------------------------------------------------------------------改文件名字


while wl < k1:
    if name2[wl] == 'CONST':
        wl = wl + 1
    else:
        reline = '{} {}'.format(name2[wl], width6[wl])
        fl.writelines(reline)
    # f.write(reline)
        fl.write('\n')
        wl = wl + 1

    if wl == k1:
        break

    if name2[wl] == 'ASSIGNW':
        reline = '{} {}'.format(name2[wl],0)
        fl.writelines(reline)
        fl.write('\n')
        wl = wl + 1

    if name2[wl] == 'Flip-Flop':
        reline = '{} {}'.format(name2[wl], width6[wl])
        fl.writelines(reline)
        # f.write(reline)
        fl.write('\n')
        wl = wl + 1
        kk = kk +1
    #if kk == len(FFPOSI)-1:




    # while qq < len(name2):
    #     if qq + wl == len(name2) - 1:
    #         break
    #     if name2[wl + qq] == 'Flip-Flop':
    #         break
    #     if name2[wl + qq] == 'NOT':
    #         qq = qq + 1
    #     else:
    #         reline = '{} {}{}'.format(name2[wl + qq], width6[wl + qq], "-bit")
    #         fl.writelines(reline)
    #         fl.write('\n')
    #         qq = qq + 1
    # wl = wl + 1


fl.close()

k33 = 0
i = 1
ff = 0
ii = 0
FFposition = []

while k33 < k1:
    if "Flip-Flop" in linecache.getline('Process/Vs38584_T.txt', i):#---------------------------------------------------------------------------------------------------改文件名字
        FFposition.append(i)
        i = i + 1
        k33 = k33 +1
        ff = ff +1

    if "ASSIGNW" in linecache.getline('Process/Vs38584_T.txt', i):#---------------------------------------------------------------------------------------------------改文件名字
        FFposition.append(i)
        i = i + 1
        k33 = k33 +1


    else:
        i = i + 1
        k33 = k33 + 1
print("FF和ASSIGNW的位置行数:")
print(FFposition)



k331 = 0
i1 = 0
AAposition = []
DFposition = []
while k331 < k1:
    if "ASSIGNW" in linecache.getline('Process/Vs38584_T.txt', i1):#---------------------------------------------------------------------------------------------------改文件名字
        AAposition.append(i1)
        i1 = i1 + 1
        k331 = k331 +1

    if "Flip-Flop" in linecache.getline('Process/Vs38584_T.txt', i1):#---------------------------------------------------------------------------------------------------改文件名字
        DFposition.append(i1)
        i1 = i1 + 1
        k331 = k331 +1
    else:
        i1 = i1 + 1
        k331 = k331 + 1

print("ASSIGNW的行数位置：")
print(AAposition)

print("ASSIGNW的行数位置的长度：")
print(len(AAposition))



print("DFF的行数位置：")
print(DFposition)





if ff == 0:
    shutil.copy("Process/Vs38584_T.txt", "Process/Vs38584_TFF.txt")# ---------------------------------------------------------------------------------------------------改文件名字
    print("NO FF IN THE DESIGN")
else:
    if len(FFposition) == 0:
        print("NO FF IN THE DESIGN")
    if len(FFposition) == 1:
        count = len(open("Process/Vs38584_T.txt").readlines())  # ---------------------------------------------------------------------------------------------------改文件名字
        flname = r'Process/Vs38584_T.txt'  # ---------------------------------------------------------------------------------------------------改文件名字
        flresult = r'Process/Vs38584_TFF.txt'  # ---------------------------------------------------------------------------------------------------改文件名字
        # open(fname, 'r', encoding='gb2312')
        GET2 = ["Flip-Flop"]
        print("Only one FF IN THE DESIGN")
        with open(flname, 'r', encoding='UTF-8') as fll:
            with open(flresult, 'w', encoding='UTF-8') as kl:
                for line in fll.readlines():
                    if isInArray(GET2, line):  # 含noneed里面字符的行 都要
                         kl.write(line)

                a = FFposition[0] + 1
                print(a)
                print(linecache.getline('Process/Vs38584_T.txt', a))#---------------------------------------------------------------------------------------------------改文件名字
                while a < FFposition[-1]:
                    aaa= '{}'.format(linecache.getline('Process/Vs38584_T.txt', a))#---------------------------------------------------------------------------------------------------改文件名字
                    kl.writelines(aaa)
                    a = a + 1
                print("END")
    else:
        count = len(open("Process/Vs38584_T.txt").readlines())#---------------------------------------------------------------------------------------------------改文件名字
        flname = r'Process/Vs38584_T.txt'#---------------------------------------------------------------------------------------------------改文件名字
        flresult = r'Process/Vs38584_TFF.txt'#---------------------------------------------------------------------------------------------------改文件名字
        # open(fname, 'r', encoding='gb2312')
        #GET3 = ["ASSIGNW"]
        #GET2=["Flip-Flop"]
        #text = linecache.getline(filename, 50000000)
        # open(fname, 'r', encoding='gb2312')
        with open(flname, 'r', encoding='UTF-8') as fll:
            with open(flresult, 'w', encoding='UTF-8') as kl:
                #for line in fll.readlines():
                    # if isInArray(GET2, line):  # 含noneed里面字符的行 都要
                    #      kl.write(line)
                # b = DFposition[-1]#           最后一个FF的位置行数
                # c = DFposition[0]#             第一个FF的位置行数
                # cc = 1
                cc1 = 0#             第一个FF的位置行数
                END = 0
                A = 0
                a2 = 0
                a3 = 0
                EDD = 0
                test = 0
                LeftAA = []
                while a2 < len(AAposition):
                    if a2 == len(AAposition):
                        break
                    if AAposition[a2] > DFposition[-1] :
                        LeftAA.append(a2)
                        a2 = a2 +1
                    else:
                        a2 = a2 +1

                while a3 < len(AAposition):
                    if a3 == len(AAposition):
                        break
                    if AAposition[a3] > DFposition[-1]:
                        A = a3
                        break
                    else:
                        a3 = a3 + 1
                print(LeftAA)
                #AAposition[A + int(len(LeftAA) / 2)]

                while cc1 < AAposition[-1]:                  # 这里应该是用CFUNC来计算，到底在哪里停止，FF可以先不打开计算
                    if "ASSIGNW" in linecache.getline('Process/Vs38584_T.txt', cc1) :
                        cc1 = cc1 + 1
                        EDD = test*(EDD+1)

                    if EDD == E_condition:         # 这里应该是用CFUNC来计算，到底在哪里停止，FF可以先不打开计算
                        break

                    if "Flip-Flop" in linecache.getline('Process/Vs38584_T.txt', cc1) :
                        ccc = '{}'.format(linecache.getline('Process/Vs38584_T.txt', cc1))
                        kl.writelines(ccc)
                        # if a < len(DFposition):
                        #     cc1 = DFposition[a]
                        #     a = a + 1
                        # else:
                        #     cc1 = cc1 + 1
                        if a < len(DFposition):
                            cc1 = cc1 + 1
                            a = a + 1
                        else:
                            cc1 = cc1 + 1
                            test = 1

                    else:
                        ccc = '{}'.format(linecache.getline('Process/Vs38584_T.txt', cc1))
                        kl.writelines(ccc)
                        cc1 = cc1 + 1

print("AREA Counting Starts")

#这个算法计算了最后的有关output的点的gate信息

result = glob.glob('Process/Vs38584_TFF.txt')#---------------------------------------------------------------------------------------------------改文件名字
Node = []

for deta in result:
    AST_name = []
    AST_width = []

    with open(deta) as d:
        for line in d:
            #cells = line0.replace('}', '{').split('{')
            #line1= line.replace(':', ' ')
            #detailed
            #line0.replace('}', '{').split('{')

            name = line.split()[0]
            AST_name.append(name)
        AST_name = np.array(AST_name)

    with open(deta) as d:
        for line in d:
            wi = line.split()[1]
            AST_width.append(wi)
        AST_width = np.array(AST_width)

print("---------------------------------------------WIDTH PREDICTION-----------------------------------------------")
print(AST_name)
print(AST_width)



AST_width2 = []

ij = len(AST_name)
#print(AST_width[2])
ii = 0


while ii < ij:

    if ii == len(AST_name) :
        break

    if AST_name[ii] == "NOT":

        notw = float(AST_width[ii]) * 0.532
        AST_width2.append(notw)
        ii = ii +1

    if ii == len(AST_name) :
        break

    if AST_name[ii] == "OR":
        orw = float(AST_width[ii]) * 1.064

        AST_width2.append(orw)
        ii = ii + 1


    if ii == len(AST_name) :
        break

    if AST_name[ii] == "AND":

        andw = int(AST_width[ii]) * 1.064

        AST_width2.append(andw)
        ii = ii + 1

    if ii == len(AST_name) :
        break

    if AST_name[ii] == "XOR":
        xorw = int(AST_width[ii]) * 1.596

        AST_width2.append(xorw)
        ii = ii + 1

    if ii == len(AST_name) :
        break

    if AST_name[ii] == "XNOR":
        xnorw = int(AST_width[ii]) * 1.596

        AST_width2.append(xnorw)
        ii = ii + 1


    if ii == len(AST_name) :
        break

    if AST_name[ii] == "Flip-Flop":
        ffw = int(AST_width[ii]) * 4.522

        AST_width2.append(ffw)

        ii = ii + 1

    if ii == len(AST_name) :
        break

    if AST_name[ii] == "ASSIGNW":
        AST_width2.append(0)
        ii = ii + 1


print(AST_width2)
print(len(AST_width2))
print(AST_name)
print(len(AST_name))

astresult = r'results/Area/Vs38584_AST.txt'
with open(astresult, 'w', encoding='UTF-8') as astr:
    iii = 0
    jjj = 0
    kkk = 0
    seqn = 0
    comn = 0
    while iii < len(AST_width2):
        ast = '{} {} {}'.format(AST_name[iii],AST_width2[iii],"um2")
        astr.writelines(ast)
        astr.write('\n')
        iii = iii +1

    ttwidth = 0
    sqwidth = 0
    cbwidth = 0

    for i in range(0, len(AST_width2)):
        ttwidth += AST_width2[i]

    while jjj  < len(AST_width2):

        if jjj == len(AST_width2):
            break

        if AST_name[jjj] == "Flip-Flop":
            sqwidth+=AST_width2[jjj]
            jjj = jjj + 1

        else:
            jjj = jjj +1

        if jjj == len(AST_width2):
            break

        if AST_name[jjj] == "ASSIGNW":
            jjj = jjj + 1

    while kkk < len(AST_width2):

        if kkk == len(AST_width2) :
            break

        if AST_name[kkk] == "Flip-Flop":
            kkk = kkk + 1
            seqn = seqn + 1

        else:
            cbwidth += AST_width2[kkk]
            kkk = kkk + 1
            comn = comn +1

        if kkk == len(AST_width2):
            break

        if AST_name[kkk] == "ASSIGNW":
            kkk = kkk + 1

    comn = comn - seqn*2
    cbwidth = cbwidth - 1.596*seqn
    ttwidth = ttwidth - 1.596*seqn
    sqwidthbit = '{} {} {} {} {}'.format("Sequential area are", sqwidth, "um2","Numbers are ",seqn)
    cmwidthbit = '{} {} {} {} {}'.format("Combinational area are", cbwidth, "um2", "Numbers are ",comn)
    ttwidthbit = '{} {} {}'.format("Total area are",ttwidth, "um2")
    time_end = time.time()
    time_c = time_end - time_start
    tttime = '{} {} {}'.format(" AST parser cost",time_c,"seconds")
    ASTver = '{} '.format(" AST parser version is ASTparser_test_assignw5，DLY打开，Assignw的个数还是在DLY结束后的CFUNC2那里结束,从一开始的ASSIGNW开始计算")
    astr.writelines(sqwidthbit)
    astr.write('\n')
    astr.writelines(cmwidthbit)
    astr.write('\n')
    astr.writelines(ttwidthbit)
    astr.write('\n')
    astr.writelines(tttime)
    astr.write('\n')
    astr.writelines(ASTver)


print(" AST PARSER END PROCESS")

#dot.render('{}.gv'.format(result_name[0]), view=True)#####可自动根据文件名来保存
#dot.render('{}.gv'.format('results/tree/Vs38584_ast'), view=True)#---------------------------------------------------------------------------------------------------改文件名字


    # parts['Partedge%s' % j]
    # a1 = len(str(a.edge))
    # b1 = len(str(b.edge))
    # if b1 > a1:



#treeplot(result_name, result_edge)