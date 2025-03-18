import re

# 1. re.match() vs re.search()
r = re.compile("ab.")

print(r.match("kkkabc"))
print(r.search("kkkabc"))
print(r.match("abckkk"))


# 2. re.split()

text = "사과 딸기 수박 메론 바나나"
print(re.split(" ", text))

text = """사과
딸기
수박
메론
바나나"""

print(re.split("\n", text))

text = "사과+딸기+수박+메론+바나나"

print(re.split("\+", text))

# 3. re.findall()
text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남 """

print(re.findall("\d+", text))

print(re.findall("\d+", "문자열입니다."))

# 4. re.sub()
text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."

preprocessed_text = re.sub('[^a-zA-Z]', ' ', text)
print(preprocessed_text)