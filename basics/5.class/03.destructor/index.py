class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __del__(self):
        print("Deleted Person Instance")

person = Person("Jim", 24)

# Deleted Person Instance
del person

class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file
    
    # エラーや例外が発生しても __exit__ は必ず実行されるため、安全にリソース解放ができる
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()

with FileManager('test.txt', 'w') as file:
    file.write("Implement RAII in Python")