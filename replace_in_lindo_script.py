# replace the file
with open("lindo_script.lindo", "wt") as out:
    for line in open("orig_script.lindo"):
        out.write(line.replace('A', 'Orange'))

