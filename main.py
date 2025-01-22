name = input('Hello, Whats your name? ')
print('Hey', name, 'lets figure out which love languae fits you best')

ready = input('Are you ready? y/n ').lower()


if ready == "y":
    print('Lets Begin')

    alone_time = input('When you are alone do you, (a) like to listen to relaxing to upbeat music or (b)finishing a task? ')
    if alone_time == "a":
        print("me too")
    elif alone_time == "b":
        print('very productive')

elif ready == "n":
    print('See ya next time')
else:
    print('type y or n')

