# 설탕배달

n = int(input())

def question(N):
    bjs = 0
    while N >= 0:
        if N % 5 == 0:
            bjs += N // 5
            #print(bjs)
            ans = bjs
            return ans
        N -= 3
        bjs += 1

    else:
        ans = -1
        return ans

print(question(n))



