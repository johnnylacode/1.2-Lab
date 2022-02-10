"""Johnny La
1875393 """

menu = {"Oil change":35, "Tire rotation":19, "Car wash":7, "Car wax":12, "No service":0}
print("Davy's auto shop services\n"
      "Oil change -- $35\n"
      "Tire rotation -- $19\n"
      "Car wash -- $7\n"
      "Car wax -- $12")

print()

user_service1 = input("Select first service:\n")
user_service2 = input("Select second service:\n")

if user_service2 == "-":
    user_service2 = "No service"
elif user_service1 == "-":
    user_service1 = "No service"

print()

service1 = menu[user_service1]
service2 = menu[user_service2]
total = service1 + service2

if service2 == 0:
    print("Davy's auto shop invoice\n\n"
          "Service 1: {}, ${}\n"
          "Service 2: {}\n".format(user_service1, service1, user_service2))
    print("Total: ${}".format(total))
elif service1 == 0:
    print("Davy's auto shop invoice\n\n"
          "Service 1: {}\n"
          "Service 2: {}, ${}\n".format(user_service1, user_service2, service2))
    print("Total: ${}".format(total))
else:
    print("Davy's auto shop invoice\n\n"
          "Service 1: {}, ${}\n"
          "Service 2: {}, ${}\n".format(user_service1, service1, user_service2, service2))
    print("Total: ${}".format(total))