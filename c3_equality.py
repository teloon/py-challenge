
def solve():
    fn = "c3_equality.txt"
    cnt_lst = [0, 0, 0]
    bnd_lst = [3, 1, 3]
    #0 for in prev, 1 for in mid, 2 for in latt
    state = -1
    res_lst = []
    for ln in open(fn, "r"):
        for i, s in enumerate(ln.strip()):
            if not s.isalpha():
                continue
            if state == -1:
                if s.isupper():
                    state = 0
            if state == 0:
                if s.isupper():
                    cnt_lst[0] += 1
                elif cnt_lst[0] == bnd_lst[0]:
                    state = 1
                else:
                    state = -1
                    cnt_lst = [0, 0, 0]
            if state == 1:
                if s.lower() and cnt_lst[1] < bnd_lst[1]:
                        cnt_lst[1] += 1
                        state = 2
                        continue
                else:
                    state = -1
                    cnt_lst = [0, 0, 0]
            if state == 2:
                if s.isupper():
                    cnt_lst[2] += 1
                elif cnt_lst[2] == bnd_lst[2]:
                    res_lst.append(ln[i-7:i])
                    state = 0
                    cnt_lst = [bnd_lst[0], 0, 0]
                else:
                    state = -1
                    cnt_lst = [0, 0, 0]
    for s in res_lst:
        print s

if __name__ == '__main__':
    solve()
