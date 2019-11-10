def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0

    n_games = len(a)

    for i in range(n_games):
        if a[i]>b[i]:
            alice_points+=1
        elif a[i]<b[i]:
            bob_points+=1

    return [alice_points, bob_points]