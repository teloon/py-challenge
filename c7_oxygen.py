import Image
import urllib
import StringIO

URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"

img_f = StringIO.StringIO(urllib.urlopen(URL).read())
im = Image.open(img_f)
w, h = im.size

res = []
pixels = im.load()
for x in range(0, w, 7):
    print pixels[x, h // 2]
    res.append(chr(pixels[x, h // 2][0]))
print "".join(res)

print "next level:"
next_clue = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(map(chr, next_clue))
