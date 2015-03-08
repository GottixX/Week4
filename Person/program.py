person = {
    }

person["first_name"] = input("Enter first name: ")
person["second_name"] = input("Enter second name: ")
person["third_name"] = input("Enter third name: ")
person["birth_year"] = input("Enter birth year: ")
person["curent_age"] = 2015 - int(person["birth_year"])

print(person)
