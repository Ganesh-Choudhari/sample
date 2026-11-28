class Student:
    def __init__(self,name : str, number : int, marks : float):
        self.name = name
        self.number = number
        self.marks = marks

s = Student(44,"abc",True)

print(s.name,s.number,s.marks)

from pydantic import BaseModel

class Employee(BaseModel):
    name : str
    age : int
    salary : float

e = Employee(name="abc",age="36",salary=False)

print(e)

raw_data1 = {
    "name" : "abc",
    "age" : 55,
    "salary" : 56.66
}

e1 = Employee(**raw_data1)
print(e1)


raw_data2 = {
    "name" : "abc",
    "age" : "55",
    "salary" : "56.66"
}

e1 = Employee(**raw_data2)
print(e1)

print("-"*100)
from pydantic import ValidationError
raw_data3 = {
    "name" : 1234,
    "age" : "Twentyyy"
}
try:
    e3 = Employee(**raw_data3)
except ValidationError as e:
    print(f"Total Number of Validation Error is {e.error_count()}")
    for err in e.errors():
        print(f"Field = {err['loc']}, Type = {err['type']}, Message = {err['msg']}")

print("*" * 100)
from pydantic import BaseModel,ValidationError

class Product(BaseModel):
    product_id : int
    name : str
    price : float
    in_stock : bool

abc = {
    "product_id" : "50",
    "price" : "199.90",
    "in_stock" : "1"
}

try:
    p = Product(**abc)
except ValidationError as e:
    print(f"Total Error Occurs = {e.error_count()}")
    for err in e.errors():
        print(f"Field = {err['loc']} , Type = {err['type']} , Message = {err['msg']}")
print("**  "  * 10)

from pydantic import BaseModel,ValidationError
class College(BaseModel):
    name : str
    year : int | None = None

value = {
    "name" : "abc",
    "year" : None

}

try:
    c = College(**value)
    print(c)
except ValidationError as e:
    print(f"Total No of Error = {e.error_count()}")
    for err in e.errors():
        print(f"Field = {err['loc']} , Type = {err['type']} , Message = {err['msg']}")

print()

print()

print()

print()


from datetime import datetime, UTC
from pydantic import BaseModel

class BadExample(BaseModel):
    created_dt : datetime = datetime.now(UTC)

b1 = BadExample()
b2 = BadExample()

print(b1)
print(b2)


print()
print()

from uuid import UUID,uuid4
from pydantic import BaseModel, Field
import time
class GoodExample(BaseModel):
    created_at : datetime = Field(default_factory=lambda : datetime.now(UTC))
    request_id : UUID = Field(default_factory=uuid4)

g1 = GoodExample()
#time.sleep(30)
g2 = GoodExample()

print(g1)
print(g2)


print("**--** " * 15)