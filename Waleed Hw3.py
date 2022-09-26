from asyncio.windows_events import NULL

from unicodedata import numeric

contactTable = [{"name": "Ahmed", "Phone": "0551112222"}
                , {"name": "Abdullah", "Phone": "0551116666"},
                {"name": "Morad", "Phone": "0551115555"},
                {"name": "Sultan", "Phone": "0551114444"},
                {"name": "Saad", "Phone": "0551113333"}
                ]

              
              

phoneNumber= (input("phoneNumber:"))



def find (phoneNum):
    
    if phoneNum.__len__()!=10 or phoneNum.isnumeric() ==False:

        print("This is invalid number")

        return


    for user in contactTable:

        if user["Phone"]==phoneNum:

            print(user["name"])
            return

    print("Sorry, the number is not found")

    return


find(phoneNumber)