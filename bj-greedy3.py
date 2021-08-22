# 1. 동전의 종류개수 N
# 2. 동전을 사용한 가치의 합 K
# 3. 동전의 가치 djgc
# 3. 필요한 동전 개수의 최솟값을 구하자
# 4. djgc을 리스트화 해서 리스트 끝에서부터 pop을 이용해 숫자를 뽑아냄.
# 5. 뽑아낸 숫자를 K로 나눠봄. 몫이 0이면 다음 팝한 숫자로 나눠봄
# 6. 몫이 1이상이면서 나머지가 0이면 그 몫을 djs에 추가하고 출력
# 7. 몫이 1이상이면서 나머지가 0이 아니면 그 몫을 djs에 추가하고 pop새로 해서 그 숫자로 나머지를 나눠봄
# 8. 반복해서 나머지가 0일 때 끝
# <풀이1>
n, k = map(int, input().split())
djgc = [int(input()) for _ in range(n)]
djs = 0
for i in range(1, n + 1):
    coin = djgc.pop()

    if k >= coin:
        mok = k // coin
        k -= coin * mok
        djs += mok
print(djs)
# <풀이2>
n,k = map(int,input().split())
money = [int(input()) for _ in range(n)]
cnt = 0
while k > 0:
    cnt += k // money[n-1]
    k = k % money[n-1]
    n -= 1

print(cnt)