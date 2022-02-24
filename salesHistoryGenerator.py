from random import randrange

book = ["Celeste", "Devil May Cry", "Hades", "Why I am gay.", "Beholder", "Beholder 2", "Dyson Sphere Program", "Battlefield", "Return Human", "Paranormal HK"]
people = ["Johnny Silverhand", "Judy Alvarez", "Logan Bamford", "Goro Takemura", "Mica Smith"]

cnt = 1

for i in range (1, 30):
    cnt += randrange(2)
    print(f"\'{book[randrange(10)]}\', 1, \'03/{cnt}/2021\', \'{people[randrange(5)]}\'")