# Calclib
### Thư viện tính toán cho python. Giúp các phép tính đi xa hơn, dễ sử dụng hơn
* Build v0.0.1
  * Cập nhật 'sqrt' cho việc tính căn thức
***
* ## Hướng dẫn cài đặt
1. Bạn phải download `setup.py` hoặc source code
```
git clone https://github.com/thang0804/calclib
```
2. Sử dụng `setup.py` để cài đặt
* Windows
```
python setup.py install
```
* Linux
```
python3 setup.py install
```

***
* ## Cách sử dụng
```python
from calclib.Lexer import Lexer
from calclib.Parser import Parser

lexer = Lexer('1^2+sqrt(20+20)*1+2.2') # Đưa phép tính vào lexer và khởi tạo lexer
parser = Parser() # Khởi tạo parser
tokens = lexer.GetTokens() # Lấy tokens của phép tính
kq = parser.TryParse(tokens) # Lấy kết quả của phép tính
print(kq)
```
Output sẽ là:
```
9.5245553203
```
* ## Các phép tính có sẵn
```
Để biểu diễn số thập phân ta sử dụng dấu '.' (Ví dụ: 1.4, 6.8265)
Các phép tính cơ bản: +, -, *, /
Chia lấy phần dư: % (Ví dụ: 3%2 = 1 [1 là số sư của phép tính])
Phép lũy thừa: ^ (Ví dụ: 2^3 = 8)
Phép tính căn bậc 2: sqrt(x) hoặc SQRT(x) (Ví dụ: sqrt(16) = 4)
Biểu thức lượng giác sin, cos, tan: sin(x), cos(x), tan(x)
```

* ## Config đơn vị đo góc
* calclib có 2 đơn vị đo góc là 'degree' (đơn vị đo độ) và 'radian' (đơn vị đo radian)
```python
...
lexer.angle = 'degree'
...
```
Hoặc
```python
...
lexer.angle = 'radian'
...
```

# Lưu ý
* Khi sử dụng calclib nên hạn chế việc sử dụng dấu cách ' '.
```
Ví dụ:
Phép tính: 6^2+8-3 thay vì: 6 ^ 2 + 8 - 3
```