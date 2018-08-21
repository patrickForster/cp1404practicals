"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(level_of_achievement(score))


def level_of_achievement(score):
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
