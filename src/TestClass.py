class TestClass:
    age = 16
    name = "Hoge"
    __function_call_count = 0

    def __init__(self):
        self.__text = "Good morning."
        print("TestClass is created.")

    def greet(self):
        print(f"{self.__text} I am {self.name} and {self.age} years old.")
        self.__increment_function_call_count()

    def want(self, name):
        print(f"I want {name}.")
        self.__increment_function_call_count()

    def get_function_call_count(self):
        print(f"function call count is {self.__function_call_count}")

    def __increment_function_call_count(self):
        self.__function_call_count += 1