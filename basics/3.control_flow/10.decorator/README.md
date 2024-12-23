#### デコレーター
```python
def print_info(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

f = add_num(10, 20)
"""
(10, 20) {}
START
END
30
"""
print(f)
```

#### 自分なりやってみよう（ロガー）
```python
from typing import Callable

User = dict[str, str | int]

def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Elements: {args}")
        print(f"Dict Elements: {kwargs}")

        return func(*args, **kwargs)
    return wrapper

@logger
def create_user(id: int | None, name: str | None, age: int | None, gender: str | None) -> User | None:
    if id is None or name is None or age is None or gender is None:
        return None
    
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    return {"id": id, "name": name, "age": age, "gender": gender}

func = create_user(1, "Alice", 20, "female")
print(func)

"""
Elements: (1, 'Alice', 20, 'female')
Dict Elements: {}
{'id': 1, 'name': 'Alice', 'age': 20, 'gender': 'female'}
"""
```

#### loggingを使用したログデコレーター
```python
import logging
from typing import Callable, Optional

User = dict[str, Optional[str | int]]

def setup_logger(name: str, log_file: Optional[str] = None, level: int = logging.DEBUG) -> logging.Logger:
    """
    ログメッセージの設定およびコンソール・ファイルへの出力設定

    引数:
    - name (str):               ロガー名
    - log_file (Optional[str]): ログファイルのパス
    - level (int):              ログレベル

    戻り値:
    - logging.Logger: ロガーオブジェクト
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # コンソールへの出力設定
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # ログファイルの出力設定
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

def logger(func: Callable) -> Callable:
    """
    結果をログに記録するデコレーター

    引数:
    - func (Callable): デコレーターでラップする関数

    戻り値:
    - Callable: ログ出力機能を追加したラップされた関数
    """
    def wrapper(*args, **kwargs):
        # 2024-12-23 01:26:08,391 - user_creation - DEBUG - Called with arguments: (1, 'Alice', 25, 'female'), {}
        logger.debug(f"Called with arguments: {args}, {kwargs}")
        try:
            result = func(*args, **kwargs)
            # 2024-12-23 01:26:08,391 - user_creation - DEBUG - Result: {'id': 1, 'name': 'Alice', 'age': 25, 'gender': 'female'}
            logger.debug(f"Result: {result}")
        except Exception as e:
            logger.error(f"Error in function '{func.__name__}': {e}")
        return result
    return wrapper

@logger
def create_user(id: Optional[int], name: Optional[str], age: Optional[int], gender: Optional[str]) -> Optional[User]:
    """
    ユーザーを作成し、辞書型で返す

    引数:
    - id (Optional[int]):     ユーザーID
    - name (Optional[str]):   ユーザー名
    - age (Optional[int]):    年齢
    - gender (Optional[str]): 性別

    戻り値
    - Optional[User]: ユーザー情報を含む辞書、無効な場合は None を返す

    例外:
    - ValueError: 必須フィールドが欠けている、または無効な値が渡された場合に発生する
    """
    if id is None or name is None or age is None or gender is None:
        raise ValueError("All fields are required.")
    
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer.")
    
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'.")
    
    return {"id": id, "name": name, "age": age, "gender": gender}

mock_database = {}

def save_user(user: User) -> None:
    """
    ユーザー情報を仮のデータベースに保存する

    引数:
    - user (User): 保存するユーザー情報を含む辞書
    """
    mock_database[user["id"]] = user

# ロガーのセットアップ
logger = setup_logger("user_creation", log_file="user_creation.log")

try:
    user = create_user(1, "Alice", 25, "female")
    save_user(user)

    # 2024-12-23 01:26:08,391 - user_creation - INFO - User created: {'id': 1, 'name': 'Alice', 'age': 25, 'gender': 'female'}
    logger.info(f"User created: {user}")
except Exception as e:
    logger.error(f"Error creating user: {e}")
```