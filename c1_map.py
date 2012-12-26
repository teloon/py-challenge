
def naive(code):
    msg_lst = []
    for c in code:
        o_n = ord(c)
        if  ord('a') <= o_n <= ord('z'):
            msg_lst.append(chr((o_n - ord('a') + 2) % 26 + ord('a')))
        else:
            msg_lst.append(c)

    return ''.join(msg_lst)

def use_table(code):
    import string
    from_s = "".join([chr(i+ord('a')) for i in range(26)])
    to_s = from_s[2:] + from_s[:2]
    table = string.maketrans(from_s, to_s)
    return code.translate(table)

if __name__ == '__main__':
    #code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    code = "map"
    print use_table(code)
