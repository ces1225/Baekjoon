ans=[]
rate=0
scoresum=0
rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, 
          "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, 
          "F": 0.0}

for _ in range(20):
    grade = input()
    for i in range(len(grade)):
        if grade[i] == " ":
            ans.append(grade[(i+1):].split())
            break
for i in range(20):
    if ans[i][1] == "P":
        continue
    rate += float(ans[i][0])*rating[ans[i][1]]
    scoresum += float(ans[i][0])
print(rate/scoresum)

'''
입력까지는 했으나 if else문으로 하기 귀찮았따 그리고 해도 틀렸음
알았던 사실
"dictionay는 저렇게 선언 후, 변수[]으로 꺼내올수 있다" 상당히 중요한 부분
또한 정수가 아닌 3.0와 같은 유리수가 나왔기 때문에 float 함수를 사용하여 계산하였다.
성적 P의 경우 계산하지 않고 넘어가기 때문에 if pass문을 사용하여 for문 자체를 생략하였다.

for i in range(20):
    subject, score, grade = input().split()
print(subject)
print(score)
print(grade)
이런 식으로 해도 선언이 되더라 공백으로 해서 나뉘는듯?

'''
    
    
    
