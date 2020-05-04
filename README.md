# Calclib
### Thư viện tính toán cho python. Giúp các phép tính đi xa hơn, dễ sử dụng hơn
* Build v0.0.1
  * Cập nhật '^' và 'sqrt' cho việc tính căn thức

***
* ## Cách sử dụng
```python
from calclib.Lexer import Lexer
from calclib.Parser import Parser

lexer = Lexer('1^2+sqrt(20+20)*1+2') # Đưa phép tính vào lexer và khởi tạo lexer
parser = Parser() # Khởi tạo parser
tokens = lexer.GetTokens() # Lấy tokens của phép tính
kq = parser.TryParse(tokens) # Lấy kết quả của phép tính
print(kq)
```
Output sẽ là:
```
9.3245553203
```