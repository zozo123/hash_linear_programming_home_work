import hashlib,os

f_in = open('./inputfile.txt', 'r')
f_out = open('./outputfile.txt', 'r+')
f_out.truncate()
lines = f_in.readlines()
dic = dict();
for line in lines: 
    string = str(line).strip() + ' : ' + str(line[0].strip()) + \
    str(hashlib.md5(str(line.strip())).hexdigest()[0:7])
    #print f_out.read().find(string.split(':')[-1].strip())
    if f_out.read().find(string.split(':')[-1].strip()) != -1:
        print "error " + string.split(':')[-1].strip() + " already exists"
    dic[str(line).strip()] = str(line[0].strip()) + \
    str(hashlib.md5(str(line.strip())).hexdigest()[0:7])
    f_out.write(string + '\n')
    

f_in.close()
f_out.close()

for key in dic.keys():
    #print key , dic[key]
    with open("out.txt", "wt") as out:
        for line in open("./outputfile.txt"):
            print line
            out.write(line.replace(dic[key] , key))
            line1 =line.replace(str(dic[key]).strip() , key.strip())
            print str(dic[key]).strip() , key.strip()
    

# replace the file
#with open("out.txt", "wt") as out:
#    for line in open("Stud.txt"):
#        out.write(line.replace('A', 'Orange'))
