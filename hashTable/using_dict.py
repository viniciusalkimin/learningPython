voted = dict()


def voting_check(name):
    if voted.get(name):
        print("Send away!")
    else:
        voted[name] = True
        print("Allow to vote!")


voting_check("Vinicius")
voting_check("Davi")
voting_check("Vinicius")

