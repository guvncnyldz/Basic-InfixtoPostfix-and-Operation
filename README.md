# Basic Infix to Postfix Conversion and Evaluation

This program converts mathematical expressions from **infix notation** to **postfix notation** and evaluates the result.

## Features
- Converts infix expressions to postfix
- Evaluates the mathematical result
- Detects incorrect expressions

## Input & Output Examples

### ✅ Valid Input & Output
#### Example 1
**Input:**
```plaintext
(((20+5)x2)/6)x(10+8x(3+10)-9)
```

**Output:**
```plaintext
Operation:  (((20+5)x2)/6)x(10+8x(3+10)-9)
Postfix:  20|5+|2x|6/|10|8|3|10+|x9-+x
Result:  875.0000000000001
```

---

#### Example 2
**Input:**
```plaintext
(2x(5+3))
```

**Output:**
```plaintext
Operation:  (2x(5+3))
Postfix:  2|5|3+x
Result:  16.0
```

---

### ❌ Invalid Input
#### Example 3
**Input:**
```plaintext
(2x(5+3)
```

**Output:**
```plaintext
Wrong Operation
```

---

## Important Notes
- The character **'x'** is used for multiplication, but it is actually interpreted as **'*'**.
- Parentheses **must be balanced** for the expression to be valid.
- The program follows the **operator precedence** rules for correct evaluation.
