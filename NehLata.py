#########remove duplicate values
def remove_duplicate(list):
    uniq_list=[]
    for i in list:
        if i not in uniq_list:
            uniq_list.append(i)
    print(uniq_list)        
list=input("enter list element ").split()
remove_duplicate(list)


#########complicated dictionary
dict={'a':'apple','1':10000,3:"flag",'age':23}
print(dict)
print(dict['a'])
print(dict['1'])
print(dict[3])
print(dict)



###########occurence count
def count_occur(string):
    counter={}
    for i in string:
        if i in counter:
            counter[i]+=1
        else:
            counter[i]=1
    return counter
str=input("enter a string ")
print(count_occur(str))


#########largest substring
st=input("enter string with 0 and 1 ")
lst0=st.split("0")
lst1=st.split("1")
max0=max(lst0)
index0=lst0.index(max0)
max1=max(lst1)
index1=lst1.index(max1)
if len(max0)>len(max1):
    print(max0)
else:
    print(max1)




