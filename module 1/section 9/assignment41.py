import random
print("Press enter to spin dice")
while(True):
    user_input = input()
    if user_input == 'q':
        break;
    print(random.randint(1,6))
