name = input('Hello, Whats your name? ')
print('Hey', name, 'lets figure out which love languae fits you best')

ready = input('Are you ready? y/n ').lower()


if ready == "y":
    print('Lets Begin')

    alone_time = input('When you are alone do you, (a) like to relax and listen music or (b) finish up a task? ').lower()
    if alone_time == "a":
        listen = input('Me too! What about when hangin out with friends, Do you prefer (a) doing an activity together or (b) going to brunch and chat? ').lower()
    if listen == 'a':
            activity = input('Nice, Now when you are sad do you (a) need a hug or (b) talk it out?')
    elif alone_time =='b':
        task = input('Staying focused, I like it. On your birthday do you like to (a) have a huge celebration or (b) no fuss? ').lower()
    if activity == 'a':
                hug= input('That sound comforting. When someone does something nice for you do you show appreciation by (a) taking them to a nice dinner or (b) return the favor and help them with a task? ')
                if hug == 'a':
                    dinner = input('sounds delicious.')

    elif alone_time == "b":
        print('very productive')
    else:
        print('select option a or b')

elif ready == "n":
    print('See ya next time')
else:
    print('type y or n')

 