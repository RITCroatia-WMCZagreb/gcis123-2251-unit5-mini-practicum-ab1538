'''
@ASSESSME.USERID: ab1538
@ASSESSME.AUTHOR: Andrej Biljaka
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''

# The  thecima values of PI
PI_VALUE = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    exactcount = 0

    for i in range(len(PI_VALUE)):
        digit_number = i + 1
        userinput = input("Enter the " + str(digit_number) + "-th digit of pi: ")

        if userinput == PI_VALUE[i]:
            exactcount = exactcount + 1
        else:
            print("Incorrect digit. The correct digit is:", PI_VALUE[i], ".") 
            break
    return exactcount

def display_score(score):
    print("Number of correct decimal digits", str(score))

    if score >=0 and score <= 4:
        title = "PI Neophyte"
    elif score >= 5 and score <= 9:
        title = "PI Novice"
    elif score >= 10 and score <= 24:
        title = "PI Journeyman"
    elif score >= 25 and score <= 49:
        title = "PI Enthusiast"
    elif score >= 50 and score <= 96:
        title = "PI Connoisseur"
    elif score >= 97 and score <= 100:
        title = "PI Expert"
    else:
        title = "PI Imposter"
    print("Your title:", title)


def main():
    score = pi_tester()
    display_score(score)

if __name__ == "__main__":
    main()