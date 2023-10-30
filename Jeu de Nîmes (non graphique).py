import random
r_player=0
r_bot=0
allumettes=21
perdu = False

player = input("Quel est votre nom?")
if player.lower() == "grail":
    print("Bravo, vous avez débloqué le mod où vous pouvez gagner!!!")
else:
    print(f"Bonne chance {player}")

print(f"Il y a {allumettes} allumettes.")

try:
    while perdu == False:

        print(f"Il reste {allumettes} allumettes.")

        for n in range(1):

            if allumettes >= 3:
                r_player=int(input("Vous pouvez en prendre entre 1 et 3. Combien en prenez vous?"))

                if r_player>3 or r_player<1:
                    print("On avait dit entre 1 et 3!!!")
                    r_player=int(input("ENTRE 1 ET 3:"))

                    if r_player > 3 or r_player < 1:
                        print("Là vous forcez!")
                        perdu = True

            elif allumettes == 2:
                r_player = int(input("Vous pouvez en prendre entre 1 et 2. Combien en prenez vous?"))

                if r_player > 2 or r_player < 1:
                    print("On avait dit entre 1 et 2!!!")
                    r_player = int(input("ENTRE 1 ET 2:"))

                    if r_player > 3 or r_player < 1:
                        print("Là vous forcez!")
                        perdu = True

            elif allumettes == 1:
                r_player = int(input("Vous pouvez en prendre entre 1 et...1, bon bah vous allez perdre. "
                                     "Je vous laisse quand même le chois. "
                                     "Combien en prenez vous?"))

                if r_player > 1 or r_player < 1:
                    print("On avait dit entre 1 et 1!!!")
                    r_player = int(input("ENTRE 1 ET 1:"))

                    if r_player != 1:
                        print("Là vous forcez, "
                              "la seule réponse c'est 1 et vous arrivez même pas à mettre le bon nombre..."
                              "je sais pas quoi faire de vous...")
                        perdu = True

            allumettes = allumettes-r_player

        if allumettes==0:
            print("Vous avez perdu mais moi j'ai gagné!")
            perdu = True


        for n in range(1):
            if player.lower() == "grail":
                if allumettes >= 3:
                    r_bot = random.randint(1, 3)
                    print(f"Je prends {r_bot} allumettes")

                elif allumettes == 2:
                        r_bot = random.randint(1, 2)
                        print(f"Je prends {r_bot} allumettes")

                elif allumettes == 1:
                    r_bot = 1
                    print(f"Je prends {r_bot} allumettes")

                allumettes = allumettes - r_bot

                if allumettes == 0:
                    print("J'ai perdu mais bravo à toi, tu as gagné!")
                    perdu = True

            else:
                if allumettes > 17:
                    r_bot = 21-r_player-17
                    print(f"Je prends {r_bot} allumettes")

                elif allumettes >= 13 and allumettes < 17:
                    r_bot = 17-r_player-13
                    print(f"Je prends {r_bot} allumettes")

                elif allumettes >= 9 and allumettes < 13:
                    r_bot = 13-r_player-9
                    print(f"Je prends {r_bot} allumettes")

                elif allumettes >= 5 and allumettes < 9:
                    r_bot = 9-r_player-5
                    print(f"Je prends {r_bot} allumettes")

                elif allumettes >=1 and allumettes < 5 :
                    r_bot = 5-r_player-1
                    print(f"Je prends {r_bot} allumettes")
                else:
                    print("Au revoir")

                allumettes = allumettes - r_bot
except ValueError:
    print("Nous avons rencontré un problème durant l'éxecution du jeu, relancez le.")