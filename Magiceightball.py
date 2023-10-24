#this is the 'Choice()' function option by creating a list otherwise use radiant.random() to use a numbered list
import random
response_option=['It appears you are blind.',
               'Oops, try again.',
               'Do you so wish your future to be doomed? Perish the thought.',
               'How many times does Life have to tell you No?!',
               'Now now, do not be a sob. Things shall get better.',
               'It is a no. Come now, do not be sad.',
               'Yes, you should be rejoicing, why are you not celebrating this very minute?',
               'Perhaps, perhaps not. The choice is entirley yours.',
               'The dark mists cloud my sight...',
               'Why of course you silly Nincompoop!']
while True:
    question=input("Hello! I am the Magic 8 Ball of the Mystical Lands! Tell me your question and I shall share all. (type 'end' to End.)")
    if question=="end":
        print("I shall await your retrun.")
        break
    # answer_string=random.choice(response_option)
    # print(answer_string)
    print(random.choice(response_option))           
               
"""
In this module, we imported and used random.choice() like this:

     import random
     ...
     print(random.choice(...))
     
Alternate syntax, if we are only using `choice`, and we don't want to write `random.choice` each time:

    from random import choice
    ...
    print(choice(...))

"""
               
"""choice(['Oops, try again', 'Hell naw', 'By the Godess Yes!'])
    print("Hello! I am the Magic 8 Ball of the Mystical Lands! Tell me your question and I shall share all. ")
answer = 0
while magic8 == answer:
    answer = int(input("Tell me your question and I shall share all. "))
    if answer = magic8:
        print("""