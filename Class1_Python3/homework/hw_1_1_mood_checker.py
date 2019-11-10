def mood_checker(mood: str) -> str:
    # add your function here

    if mood == "happy":
       print("It is great to see you happy!")
    elif mood == "nervous":
        print("Take a deep breath 3 times.!")
    else:
        print("I don't recognize this mood")

my_mood = input("Enter your mood: ")



def test_mood_checker():
    assert mood_checker("happy") == "It is great to see you happy!"
    assert mood_checker("nervous") == "Take a deep breath 3 times.!"
    assert mood_checker(12) == "I don't recognize this mood"
    assert mood_checker("12") == "I don't recognize this mood"
    assert mood_checker("") == "I don't recognize this mood"

# guard
if __name__ == '__main__':
    test_mood_checker()