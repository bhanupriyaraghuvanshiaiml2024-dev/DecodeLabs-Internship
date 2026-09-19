print("............ AI Rule Based CHATBOT ............")
print("If you want to exit, say -> bye or thankyou")


# Function to take input
def get_input():
    answer = input().lower().strip()

    if answer in ["bye", "thankyou"]:
        return None

    return answer


while True:

    print("Hello, what's your name?")
    a = get_input()
    if a is None:
        print("Okayy, bye!")
        break

    print("Where are you from? (city or state)")
    b = get_input()
    if b is None:
        print("Okayy, bye!")
        break

    print("What do you do?")
    c = get_input()
    if c is None:
        print("Okayy, bye!")
        break

    print("What are you feeling today?? (good or bad)")
    d = get_input()
    if d is None:
        print("Okayy, bye!")
        break

    if d == "good":
        print("Good to hear that, thank you for letting me know!")
    else:
        print("I am so sorry to hear that! Can I do anything? (yes or no)")
        e = get_input()

        if e is None:
            print("Okayy, bye!")
            break

        if e == "yes":
            print("Sorry to hear that.")
        else:
            print("It's okayy!! Take your time.")

    print("What do you want to become?\n"
          "1. Government servant\n"
          "2. Corporate\n"
          "3. CEO\n"
          "4. Business\n"
          "5. Doctor\n"
          "6. Engineer")

    print("If the answer is none of these, say - nothing")

    f = get_input()
    if f is None:
        print("Okayy, bye!")
        break

    if f == "nothing":
        print("No worries, take your timee!")
    else:
        print("Hope you can become that.")

    print("What are your interests?\n"
          "1. Dancing\n"
          "2. Poetry\n"
          "3. Singing\n"
          "4. Coding\n"
          "5. Sports")

    print("If the answer is none of these, say - nothing")

    g = get_input()
    if g is None:
        print("Okayy, bye!")
        break

    if g == "nothing":
        print("It's okayyy!")
    else:
        print("Love to know thatt!!")

    print("How well do you know AI??")
    print("Want to play a quiz? (yes or no)")

    h = get_input()
    if h is None:
        print("Okayy, bye!")
        break

    if h == "yes":

        print("What is AI?")
        print("1. Artificial Intelligence\n"
              "2. Artificial Integration\n"
              "3. Artificial Internet\n"
              "4. Artificial Information")

        ans = get_input()
        if ans is None:
            print("Okayy, bye!")
            break

        if ans == "artificial intelligence":
            print("Correctt!")
        else:
            print("The answer is Artificial Intelligence, nice try!")

        print("What is an example of AI?")
        print("1. Calculator\n"
              "2. Voice Assistant\n"
              "3. Keyboard\n"
              "4. USB Cable")

        ans1 = get_input()
        if ans1 is None:
            print("Okayy, bye!")
            break

        if ans1 == "voice assistant":
            print("Righhttt!")
        else:
            print("The answer is Voice Assistant, nice try!")

        print("What is the common use of AI?")
        print("1. Face Recognition\n"
              "2. Printing a paper\n"
              "3. Charging a phone\n"
              "4. Connecting a cable")

        ans3 = get_input()
        if ans3 is None:
            print("Okayy, bye!")
            break

        if ans3 == "face recognition":
            print("You got it!")
        else:
            print("The right answer is Face Recognition.")

    else:
        print("Okayy! No issueeee.")

    print("Do you want to know how I work?")
    j = get_input()
    if j is None:
        print("Okayy, bye!")
        break

    if j == "yes":
        print("Well, this program works using if-else and while-loop logic.")
        print("Want to know where my program is written? (yes/no)")

        ans5 = get_input()
        if ans5 is None:
            print("Okayy, bye!")
            break

        if ans5 == "yes":
            print("Well, I work on online Python compilers or VS Code.")
        else:
            print("Okayy, no issuee.")

    else:
        print("No issuess!")