import hashlib,os,re

f_in = open('./uniq_list_of_vars.txt', 'r')
f_out = open('./dictionary.txt', 'r+')
f_out.truncate()
lines = f_in.readlines()
dic = dict();

for line in lines: 
    string = line.strip() + ' : ' + str(line[0].strip()) + \
    str(hashlib.md5(line.strip()).hexdigest()[0:7])
    if f_out.read().find(string.split(':')[-1].strip()) != -1 and \
       f_out.read().find(string.strip()) != -1:
        print "error " + string.split(':')[-1].strip() + " already exists"
    dic[str(line).strip()] = str(line[0].strip()) + \
    str(hashlib.md5(str(line.strip())).hexdigest()[0:7])
    f_out.write(string + '\n')
    

f_in.close()
f_out.close()

with open("./final_code.lindo","w+") as out:
    for line in open("./full_code.lindo","r"):
        for key in dic.keys():
            if key in line:
                line = line.replace(key,dic[key])
        print line,
        out.write(line)







