def insert_patient_data(name: str,age:int):
    if type(name)=='str' and type(age)=='int':
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError("Incorrect data type")

def update_patient_data(name: str,age:int):
    if type(name)=='str' and type(age)=='int':
        print(name)
        print(age)
        print("updated into database")
    else:
        raise TypeError("Incorrect data type")


insert_patient_data("mourya","twenty")
"""
age should be in int, here there is no pipe validation happening.
to solve this we use:
    typing hinting, it works even it's mismatches datatype
    we can use conditions but not scalable
    no type validation and data validation
    multiple function updates 
"""