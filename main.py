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
            
            if activity == 'a':
                hug= input('That sound comforting. When someone does something nice for you do you show appreciation by (a) taking them to a nice dinner or (b) return the favor and help them with a task? ').lower()

                if hug == 'a':
                    dinner= input('Sounds delicious!')

                elif hug =='b':
                    favor = input('You are so kind, your love language is acts of service')

            elif activity == 'b':
                talk= input('Love a good fashion heart to heart. Do you (a) love a good compliment or (b) do you get shy ')

                if talk=='a':
                    love = input('Do you want your partnet to (a) stay in contact throughout the day or (b) a quick check in? ')
                    
                    if love == "a":
                        contact = input('YOUR LOVE LANGUAGE IS QUALITY TIME- NOW GO CALL YOUR LOVER AND CUDDLE ON THE COUCH ')
                    elif love =='b':
                        check_in= input('YOUR LOVE LANGUAGE IS WORDS OF AFFIRMATION, NOW CALL YOUR MATE AND TELL THEM TO SHOWER YOU WITH COMPLIMENTS')


                elif talk== 'b':
                    shy = input('Its the weekend, do you (a) want to stay in or (b) have a night out on the town? ').lower()

        elif listen == 'b':
            brunch = input('Love a good Mimosa, ')
        
    elif alone_time =='b':
        task = input('Staying focused, I like it. On your birthday do you like to (a) have a huge celebration or (b) no fuss? ').lower()
        
    else:
        print('select option a or b')

elif ready == "n":
    print('See ya next time')
else:
    print('type y or n')

 