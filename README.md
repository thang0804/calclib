# Calclib
### Thư viện tính toán cho python
### Bộ công cụ tính toán dễ dàng mà không cần quá nhiều đến thuật toán
* #### Build v0.0.13
  * Phát hiện và sửa lỗi
  * Cho phép get nhiều tokens
* Build v0.0.11
  * Cập nhật 'sin', 'cos', 'tan' cho việc tính lượng giác
  * Cập nhật chế độ [đơn vị đo góc](https://github.com/thang0804/calclib#đơn-vị-đo-góc) 'degree' (độ) và 'radian' (rad)
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

lexer = Lexer('') # Khởi tạo lexer
lexer.angle = 'degree' # set đơn vị đo góc lad degree
parser = Parser() # Khởi tạo parser
tokens = lexer.GetTokens('1^2+sqrt(20+20)*1+2.2-sin(45+45)') # Lấy tokens của phép tính
result = parser.TryParse(tokens) # Lấy kết quả của phép tính
print(result)
```
Output sẽ là:
```
8.5245553203
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

* ## Đơn vị đo góc
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
* #### Các bản Build chỉ là các bản thử nghiệm nên còn nhiều bugs, bugs sẽ được fix dần cho đến khi release