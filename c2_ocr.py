
def count(fn):
    cnt_dict = {}
    for ln in open(fn, "r"):
        for c in ln.strip():
            if c not in cnt_dict:
                cnt_dict[c] = 0
            cnt_dict[c] += 1
    res = cnt_dict.items()
    res.sort(key=lambda x: x[1])
    return res

if __name__ == '__main__':
    fn = "c3_ocr.txt"
    res = count(fn)
    for k, v in res[:20]:
        print k, v
