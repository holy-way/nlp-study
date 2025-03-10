Study Reference : https://wikidocs.net/217240

# Regular Expression

## Regular Expression Grammar & Module Function

1. Grammar

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

* Rules used with '\'

| Grammar | Meaning |
| ----- | ----- |
| \\\\\ | Back slash |
| \\\\d | All numbers. Same as [0-9] |
| \\\\D | All letters except numbers. Same as [^0-9] |
| \\\\s | Blank space. Same as [ \t\n\r\f\v] |
| \\\\S | All letters except blank space. Same as [^ \t\n\r\f\v] |
| \\\\w | Alphabet or number. Same as [a-zA-Z0-9] |
| \\\\W | All letters except alphabet or numbers. Same as [^a-zA-Z0-9] |

