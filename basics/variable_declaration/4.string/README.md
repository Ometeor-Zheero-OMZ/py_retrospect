### 文字列
```python
# single quote
print('string')

# double quote
print("string")
```

### シングルクォート ('), ダブルクォート (") を含む文字列
```python
# string with 'single quote'
print("string with 'single quote'")

# string with "double quote"
print('string with "double quote"')
```

### Backslash Escape
```python
# string with 'single quote'
print('string with \'single quote\'')
# string with "double quote"
print("string with \"double quote\"")
```

### Raw String
```python
# C:\Users\user\Desktop
print(r'C:\Users\user\Desktop')
```

### Double Backslash Escape
```python
# C:\Users\user\Desktop
print('C:\\Users\\user\\Desktop')
```

### 複数行出力
```python
print("""
　　　　　ト .,__,,.''"´￣￣￣｀ﾞ''　 、　 　 　  ┌─ 【 東風谷　 早苗 】   ────────────────┐
　　　　　｀＞　　　 　 　　　‐- ｒ oヽ.＼　　　  |                                        |
　 　　　.／ ／　　　　 　　  　　 ヽヽo)　ﾊ.　　 |　弱気になってどうするのですか！        |
　　　 ,:'　 ;'　　　/|　,　　/| イ　ﾊ　 Y 　 .!  |　そんな自分が年寄りだと思い込んでるから|
　　  ,'　　|　　‐/-|/| 　/ｧ''lてヽ | 　 |　 |　  |　駄目なんですよ                     　 |
　　  |. 　 |　　/ｧ= ､|／ 　 j__ｒﾉﾊ　　  |　 |　 |　ファイト！                         　 |
 　　 '、 八　 ,ﾊxx　　'　　 　 xx / 　   | 　 ',.└─　l7 /> ───────────────────────────────┘
 　　　 ＼/∨  |　　   l7￣｀ヽ　    r'⌒ヽ!.　　':,　　 　 　 ´＿
　　　 　 　 | 人　　 、　　ﾉ　  /｀ヽ.ノ 、 　 ヽ、 /´!　＼|
　　　　 　 /　 /,＞.､　　　イ;'＼ /　| ハ　　　 ｀|　|
　　　 　 ／　 イ _＿,ｒ｀て__/ﾄ､　）-‐'、　| 　 　　!　ﾄ 、
　　　 /　／ア'!::|,　 | .∧　 {＼ｿ　　/::ヽ{｀ヽ /´￣} 　':,
　  .／ﾚ' 　r/　|:/　 .|/:::/＼|／ヽ.　;:::/　 ＼{´￣　|　　 ',
　  / 　,r‐|＼ ／　　./::::/　 /。。ﾉ}､|:::|　／::|{´￣　}　　 .|
　 | ／ヽ::::::/　　 　 |:::/　　 ｰイ /　∨/::::://しﾍ、 ﾄ､　/
  ／　　　  ヽ{　　　　 |::{　　　　 ﾚ' 　 }ﾚ|:::::|/:::::/ヽ.__!::::Y
　　　  -=‐ｒﾍ、　　　ゝ}＿, 　　 　　ｲ/.|:::::{:::::::{　/::::|:::;ﾊ
　　　　 /::::/｀l　　 ´「|￣｀ﾞ　 　 '"/　'､:::|::::::::∨::::::|/ |
""")
```

### 空行を省いて複数行出力
```python
print("#############################################################################################")
print("""\
　　　　　ト .,__,,.''"´￣￣￣｀ﾞ''　 、　 　 　  ┌─ 【 東風谷　 早苗 】   ────────────────┐
　　　　　｀＞　　　 　 　　　‐- ｒ oヽ.＼　　　  |                                        |
　 　　　.／ ／　　　　 　　  　　 ヽヽo)　ﾊ.　　 |　弱気になってどうするのですか！        |
　　　 ,:'　 ;'　　　/|　,　　/| イ　ﾊ　 Y 　 .!  |　そんな自分が年寄りだと思い込んでるから|
　　  ,'　　|　　‐/-|/| 　/ｧ''lてヽ | 　 |　 |　  |　駄目なんですよ                     　 |
　　  |. 　 |　　/ｧ= ､|／ 　 j__ｒﾉﾊ　　  |　 |　 |　ファイト！                         　 |
 　　 '、 八　 ,ﾊxx　　'　　 　 xx / 　   | 　 ',.└─　l7 /> ───────────────────────────────┘
 　　　 ＼/∨  |　　   l7￣｀ヽ　    r'⌒ヽ!.　　':,　　 　 　 ´＿
　　　 　 　 | 人　　 、　　ﾉ　  /｀ヽ.ノ 、 　 ヽ、 /´!　＼|
　　　　 　 /　 /,＞.､　　　イ;'＼ /　| ハ　　　 ｀|　|
　　　 　 ／　 イ _＿,ｒ｀て__/ﾄ､　）-‐'、　| 　 　　!　ﾄ 、
　　　 /　／ア'!::|,　 | .∧　 {＼ｿ　　/::ヽ{｀ヽ /´￣} 　':,
　  .／ﾚ' 　r/　|:/　 .|/:::/＼|／ヽ.　;:::/　 ＼{´￣　|　　 ',
　  / 　,r‐|＼ ／　　./::::/　 /。。ﾉ}､|:::|　／::|{´￣　}　　 .|
　 | ／ヽ::::::/　　 　 |:::/　　 ｰイ /　∨/::::://しﾍ、 ﾄ､　/
  ／　　　  ヽ{　　　　 |::{　　　　 ﾚ' 　 }ﾚ|:::::|/:::::/ヽ.__!::::Y
　　　  -=‐ｒﾍ、　　　ゝ}＿, 　　 　　ｲ/.|:::::{:::::::{　/::::|:::;ﾊ
　　　　 /::::/｀l　　 ´「|￣｀ﾞ　 　 '"/　'､:::|::::::::∨::::::|/ |\
""")
print("#############################################################################################")
```

### 文字列の複数出力
```python
# しょう HEY! HEY!
print("しょう " + "HEY! " * 2)
```

### 文字列リテラル
```python
long_string = ('This is a long string'
               ' that goes on and on')

other_long_string = 'This is a long string' \
                    ' that goes on and on'

# This is a long string that goes on and on
print(long_string)

# This is a long string that goes on and on
print(other_long_string)
```