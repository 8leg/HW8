# I did it like a static method instead of instance one because why should I? There is no unique values
# that need to be stored separately and also I wanted to try and play with it all. Also yes, protected
# attribute. How was it? "Але якщо дуже хочеться .... то можна ..."?)))
class Factorial:
    __data={}
    @classmethod
    def calculate(cls, number: int):
        if not isinstance(number, int):
            return None
        elif number in cls.__data:
            return cls.__data[number]
        else:
            result=1
            for i in range(number):
                result*=i+1
            cls.__data[number]=result
            return result
    @classmethod
    def return_cache(cls):
        return cls.__data


if __name__ == "__main__":
    while True:
        num=input("Enter a number to calculate factorial. Enter [D] to view database: ")
        try:
            num=int(num)
        except ValueError:
            if num.upper()=="D":
                for i in Factorial.return_cache().items():
                    print(i)
            else:
                print("Invalid input")
            continue
        print(Factorial.calculate(num))