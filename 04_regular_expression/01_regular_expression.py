import re

# 1. '.'
r = re.compile("a.c")

print(r.search("kkk"))
print(r.search("abc"))
print(r.search("abcdabc"))

# 2. '?'
r = re.compile("ab?c")

print(r.search("abbc"))
print(r.search("abc"))
print(r.search("ac"))

# 3. '*'
r = re.compile("ab*c")

# None
print(r.search("a"))

# 0 Letter - <re.Match object; span=(0, 2), match='ac'>
print(r.search("ac"))

# 1 Letter - <re.Match object; span=(0, 3), match='abc'>
print(r.search("abc"))

# Above 1 letters - <re.Match object; span=(0, 6), match='abbbbc'>
print(r.search("abbbbc"))

# 4. '+'
r = re.compile("ab+c")

# 0 letter - None
print(r.search("ac"))

# 1 letter - <re.Match object; span=(0, 3), match='abc'>
print(r.search("abc"))

# 4 letters - <re.Match object; span=(0, 6), match='abbbbc'>
print(r.search("abbbbc"))

# 5. '^'

r = re.compile("^ab")

# None
print(r.search("bbc"))
print(r.search("zab"))

# Starting with regular expresison - <re.Match object; span=(0, 2), match='ab'>
print(r.search("abz"))
print(r.search("abzasdasdasdab"))
print(r.search("ababababab"))

r = re.compile("ad^ab")

# None
print(r.search("adab"))
print(r.search("adabz"))
print(r.search("adbbc"))

# 6. {Number}
r = re.compile("ab{2}c")

# None
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbbbc"))

print(r.search("abbc"))


# 7. {Number1, Number2}

r = re.compile("ab{2,8}c")

# None
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbbbbbbbc"))

print(r.search("abbc"))
print(r.search("abbbbc"))
print(r.search("abbbbbbbbc"))


# 8. {Number, }

r = re.compile("a{2,}bc")

print(r.search("bc"))
print(r.search("aa"))
print(r.search("abc"))

print(r.search("aabc"))

print(r.search("aaaaaaaabc"))


# 9. []

r = re.compile("[abc]") # same as [a-c]
print(r.search("zzz"))

print(r.search("a"))

print(r.search("aaaaaa"))

print(r.search("baac"))

r = re.compile("[a-z]")

print(r.search("AAA"))
print(r.search("111"))

print(r.search("aBC"))
print(r.search("aaBC"))


# 10. [^letter]

r = re.compile("[^abc]")

print(r.search("a"))
print(r.search("ab"))
print(r.search("b"))

print(r.search("d"))
print(r.search("1"))