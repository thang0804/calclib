# Calclib
### Thư viện tính toán cho python
### Bộ công cụ tính toán dễ dàng mà không cần quá nhiều đến thuật toán
* #### Build v0.1.5 (Read changelog [here](https://github.com/thang0804/calclib)):
  * Thay đổi tên phương thức 'GetTokens' thành 'tokenize'
  * Cập nhật tính giá trị tuyệt đối của 1 số hoặc 1 biến
* Build v0.1.4 :
  * Cập nhật tính giai thừa sử dụng '!'. Xem thêm [Các phép tính có sẵn](https://github.com/thang0804/calclib#các-phép-tính-có-sẵn)
* Build v0.1.3 :
  * Cho phép get nhiều tokens
  * Fix 1 số bugs
* Build v0.1.1 :
  * Thêm số lượng biến có thể sử dụng. Xem thêm [Sử dụng biến](https://github.com/thang0804/calclib#sử-dụng-biến)
* Build v0.1.0 :
  * Cập nhật tạo biến và sử dụng biến. Xem thêm [Sử dụng biến](https://github.com/thang0804/calclib#sử-dụng-biến)
* Build v0.0.2 :
  * Cập nhật thêm phần 'sqrt', cho phép sử dụng căn bậc 3, 4 .... Xem thêm [Các phép tính có sẵn](https://github.com/thang0804/calclib#các-phép-tính-có-sẵn)
***
* ## 0.1.5 Changelog
  * #### Thay đổi tên phương thức
    * Bắt đầu từ bản 0.1.5 trở đi, phương thức 'GetTokens' sẽ trở thành phương thức 'tokenize'
  * #### Giá trị tuyệt đối
    * Giá trị tuyệt đối được sử dụng bằng cách sử dụng abs() hoặc 2 dấu ||:
    ```python
    ...
    tokens = lexer.tokenize('|-2|') # Hoặc có thể là lexer.tokenize('abs(-2)')
    ...
    ```
    Lưu ý sử dụng giá trị tuyệt đối
    ```python
    ...
    tokens = lexer.tokenize('abs((1+1)*-2)') # Cách sử dụng này sẽ làm lexer hiểu nhầm và báo lỗi
    ...
    ```
    Thay vào đó ta sử dụng
    ```python
    ...
    tokens = lexer.tokenize('|(1+1)*-2|') # Phép tính này cho ra kết quả là 4
    ...
    ```
***
* ## Hướng dẫn cài đặt
1. Bạn phải clone `setup.py` từ github:
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
from calclib import Lexer, Parser

lexer = Lexer() # Khởi tạo lexer
lexer.angle = 'degree' # set đơn vị đo góc là degree ('degree' là default)
parser = Parser() # Khởi tạo parser
tokens = lexer.tokenize('1^2+sqrt(20+20)*1+2.2-sin(45+45)') # Lấy tokens của phép tính
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
Phép tính căn bậc 2: sqrt(x) (Ví dụ: sqrt(16) = 4)

: v0.0.11
Biểu thức lượng giác sin, cos, tan: sin(x), cos(x), tan(x)

: v.0.14
Sử dụng ngoặc vuông và ngoặc nhọn dể phân biệt ngoặc:
'(((1+2)*3)/4)*5' => '{[(1+2)*3]/4}*5' # Phép tính nhìn dễ dàng hơn

: v0.0.2
Để tính toán căn thức bậc cao hơn sử dụng: <số mũ>sqrt(x) (Ví dụ: 3sqrt(27) = 3, 4sqrt(16) = 2)

: v0.1.4
Để tính toán giai thừa ta dùng: <số giai thừa>! (VD: 8! = 40320)

: v0.1.5
Để tính giá trị tuyệt đối của 1 số ta dùng abs() hoặc ||
abs(-2) = |-2| = 2
LƯU Ý: builtin abs() sẽ không được sử dụng các dấu ngoặc ở trong, nếu muốn dùng các dấu ngoặc ở trong thì phải dùng trong ||
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

* ## Sử dụng biến
  * #### Các biến chỉ mang tính tạm thời, không lưu trữ cho các lần runscript tiếp theo
  * Không được tạo thêm biến cho lexer, chỉ được sử dụng các biến có sẵn như A -> Z :
```python
...
lexer.sto('X', 60) # Gán biến X có giá trị 60
tokens = lexer.GetTokens('sqrt(X+40)') # điều này tương đương với phép tính sqrt(60+40)
...
```
  * Khi print tokens ra ta được
```
[['SQRT', '(60+40)']]
```
  * #### Lưu ý: Khi sử dụng biến chỉ được sử dụng 1 chữ cái duy nhất. VD: XY (sai) -> X hoặc Y

# Lưu ý
* Khi sử dụng calclib nên hạn chế việc sử dụng dấu cách ' '.
```
Ví dụ:
Phép tính: 6^2+8-3 thay vì: 6 ^ 2 + 8 - 3
```
* #### Các bản Build chỉ là các bản thử nghiệm nên còn nhiều bugs, bugs sẽ được fix dần cho đến khi release