Study Reference : https://wikidocs.net/217240

# Regular Expression

## Regular Expression Grammar & Module Function

### 1. Grammar

| Grammar | Meaning |
| ----- | ----- |
| . | One random letter. Except '\n' |
| ? | 0 or 1 letter |
| * | letters over 0 |
| + | letters over 1 |
| ^ | letters continue |
| $ | letters end |
| {number} | repeat for number times|
| {number1, number2} | repeat for over number1 and under number2 times |
| {number, } | repeat for over number times |
| [ ] | match with one of the letters in the brackets. [amk] - match among a, m, k. Range can be set like [a-z]. [a-zA-Z] means total alphabet. |
| [^letter] | match letter except the given letter |
| l | Used like 'AlB' meaning A or B |

* Rules used with '\\'

| Grammar | Meaning |
| ----- | ----- |
| \\\\\ | Back slash |
| \\\\d | All numbers. Same as [0-9] |
| \\\\D | All letters except numbers. Same as [^0-9] |
| \\\\s | Blank space. Same as [ \t\n\r\f\v] |
| \\\\S | All letters except blank space. Same as [^ \t\n\r\f\v] |
| \\\\w | Alphabet or number. Same as [a-zA-Z0-9] |
| \\\\W | All letters except alphabet or numbers. Same as [^a-zA-Z0-9] |

### 2. Module Function
| Function | Description |
| re.compile() | Compile regular expression. Send it to python. For the frequently used pattern, compiling beforehand is good in speed and convenience. |
| re.search() | Search in the total sentence whether the expression matches. | 
| re.match() | Check if the start of the sentence matches the expression. |
| re.split() | Split the sentence using the expression. Return in list. |
| re.findall() | Return all the matching expressions in list. If none, void list. |
| re.finditer() | Return all the matching expressions in iterator object |
| re.sub() | Substitute all the matching expressions with another expression |

# Use Caes

## 1. '.'
* Represent single random letter
* ex) 'a.c'
	* Any letter between 'a', 'c' can come
	* akc, azc, avc, a5c, a!c, ...
	* Find only one first matching expression

## 2. '?'
* Former letter might exist or not.
* ex) 'ab?c'
	* Matching with or without 'b'
	* abc, ac

## 3. '\*'
* Former letters over 0
* Might exist, not exist, many letters may exist.
* ex) 'ab\*c'
	* ac, abc, abbc, abbc

## 4. '+'
* Similar as '\*'
* Former letters over 1
* ex) 'ab+c'
	* ac - X
	* abc, abbc, abbbc - O 

## 5. '^'
* Matches expression starting with regular expression
* ex) ^ab
	* bbc, zab - X
	* abz - O

## 6. {Number}
* The letter repeats for the 'number' times

## 7. {Number1, Number2}
* The letter repeats for over 'number1' and under 'number2' times
* ex) ab{2,8}c
	* ac, abc, abbbbbbbbbc - X
	* abbc, abbbbc, abbbbbbbbc - O

## 8. {Number, }
* The letter repeats for over 'number' times

## 9. []
* Match with one of the letters
* ex) [abc]
	* a, b, c

## 10. [^letter]
* Match if not included