# Basic-InfixtoPostfix-and-Operation
Convert infix to postfix and do math

#### Input: 
{<br/>
(((20+5)x2)/6)x(10+8x(3+10)-9)<br/>
}<br/>
#### Output: 

{<br/>
Operation:  (((20+5)x2)/6)x(10+8x(3+10)-9)<br/>
Postfix:  20|5+|2x|6/|10|8|3|10+|x9-+x<br/>
Result:  875.0000000000001<br/>
}<br/>

#### Input: 
{<br/>
(2x(5+3)<br/>
}<br/>
#### Output: 

{<br/>
Wrong Operation<br/>
}<br/>

#### Input: 
{<br/>
(2x(5+3))<br/>
}<br/>
#### Output: 

{<br/>
Operation:  (2x(5+3))<br/>
Postfix:  2|5|3+x<br/>
Result:  16.0<br/>
}<br/>

- - - - - - - - - - - 
"x" is actually "*"!
- - - - - - - - - - -

