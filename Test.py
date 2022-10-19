import re
def solution(S, T):
    digits_s = re.findall('\d+',S)
    digits_t = re.findall('\d+',T)
    print(digits_s)
    print(digits_t)
    for i in digits_t:
        T = T.replace(i, int(i)*'?',1)
    print(T)
    for i in digits_s:
        S = S.replace(i,int(i)*'?',1)
    print(S)
    if len(T) != len(S):
        return False
    else:
        for i in range(len(T)):
            letter = T[i]
            letter2 = S[i]
            if letter=='?':
                continue
            else:
                if letter2=='?':
                    continue
                elif letter == letter2:
                    continue
                else:
                    return False
        for i in range(len(S)):
            letter = T[i]
            letter2 = S[i]
            if letter2=='?':
                continue
            else:
                if letter=='?':
                    continue
                elif letter == letter2:
                    continue
                else:
                    return False
        return True

if __name__=='__main__':
    S =input("S: ")
    T = input("T: ")
    results = solution(S,T)
    print(results)