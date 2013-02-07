import zipfile
import re

#download "http://www.pythonchallenge.com/pc/def/channel.zip"

zipfile_obj = zipfile.ZipFile("channel.zip")
"""
zipfile_obj.namelist()
print zipfile_obj.read("readme.txt")

"""

fid, patt = "90052", r"Next nothing is (\d+)"
comments = []
while True:
    cont = zipfile_obj.read("%s.txt" % fid)
    mat_obj = re.match(patt, cont)
    if mat_obj:
        fid = mat_obj.group(1)
        comments.append(zipfile_obj.getinfo("%s.txt" % fid).comment)
    else:
        print cont
        break
print "".join(comments)
