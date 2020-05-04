# Calclib
### Thư viện tính toán cho python. Giúp các phép tính đi xa hơn, dễ sử dụng hơn
* Build v0.0.1
  * Cập nhật '^' và 'sqrt' cho việc tính căn thức

***
* ## Cách sử dụng
```python
from calclib.Lexer import Lexer
from calclib.Parser import Parser

lexer = Lexer('1^2+sqrt(20+20)*1+2')
parser = Parser()
tokens = lexer.GetTokens()
kq = parser.TryParse(tokens)
print(kq)
```
Output sẽ là:
```
9.3245553203
```