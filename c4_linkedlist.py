from urllib import urlopen

def solve(num):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    lst = []
    while True:
        f = urlopen(url % num)
        cont = f.read()
        num = cont.strip().split()[-1]
        if not num.isdigit():
            break
        lst.append(num)
        print num
        f.close()

if __name__ == '__main__':
    #solve("12345")
    solve("8022")
