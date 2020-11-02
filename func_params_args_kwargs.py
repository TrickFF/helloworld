def printScores(student, *scores):
    print(f"Student Name: {student}")
    for score in scores:
        print(score)


printScores("Leo", 100, 95, 88, 92, 99)


def printPetNames(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


printPetNames("Leo", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
