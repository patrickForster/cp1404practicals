"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_achievement(score))


def determine_achievement(score):
    if score < 0 or score > 100:
        achievement = "Invalid Score!"
    elif score >= 90:
        achievement = "Excellent"
    elif score >= 50:
        achievement = "Pass"
    else:
        achievement = "Bad"
    return achievement


main()
