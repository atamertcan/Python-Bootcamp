import random


print("\n\n\nOyunumuzun dünyaca bilinen taş kağıt makas oyunudur.\nTaş makası yener, kağıda yenilir; kağıt taşı yener, makasa yenilir; makas kağıdı yener, taşa yenilir.")
print("Oyun bilgisayara karşı oynanmaktadır.\nİlk başta iki round kazanan oyunu kazanır.\nİyi eğlenceler!\n\n")


def tas_kagit_makas_ATAMERT_CAN():

    roundCounter = 1
    gameCounter = 1
    computerCounter = 0
    playerCounter = 0

    while True:


        options = ['taş','kağıt','makas']
        computerChoice = ['evet','hayır']

        print(f"##### GAME {gameCounter} ROUND {roundCounter} ####\n")

        player = input("taş, kağıt, makas, exit: ")
        print("")
        if player == "exit":
            break
        player = player.lower()

        if player != "taş" and player != "kağıt" and player != "makas":
            print("Geçerli seçenek giriniz !")
            break
        
        
        computer = options[random.randint(0,2)]


        print(f"Bilgisayarın seçimi: {computer}\nOyuncunun seçimi : {player}\n")


        if  computer == player:
            print("Berabere!")
            roundCounter += 1
            print(f"Bilgisayar {computerCounter}, Oyuncu {playerCounter}\n")

        elif computer == "taş":

            if player == "kağıt":
                playerCounter += 1
                roundCounter += 1
                print("Roundu oyuncu kazandı !")
                print(f"Bilgisayar {computerCounter}, Oyuncu {playerCounter}\n")
            
            else:
                computerCounter += 1
                roundCounter += 1
                print("Roundu bilgisayar kazandı !")
                print(f"Bilgisayar {computerCounter}, oyuncu {playerCounter}\n")

        elif computer == "kağıt":

            if player == "makas":
                playerCounter += 1
                roundCounter += 1
                print("Roundu oyuncu kazandı !")
                print(f"Bilgisayar {computerCounter}, Oyuncu {playerCounter}\n")
            
            else:
                computerCounter += 1
                roundCounter += 1
                print("Roundu bilgisayar kazandı !")
                print(f"Bilgisayar {computerCounter}, oyuncu {playerCounter}\n")

        elif computer == "makas":

            if player == "taş":
                playerCounter += 1
                roundCounter += 1
                print("Roundu oyuncu kazandı !")
                print(f"Bilgisayar {computerCounter}, Oyuncu {playerCounter}\n")
    
            else:
                computerCounter += 1
                roundCounter += 1
                print("Roundu bilgisayar kazandı !")
                print(f"Bilgisayar {computerCounter}, oyuncu {playerCounter}\n")
        


        if computerCounter == 2 or playerCounter == 2:
            print("Oyun bitti !")
            if computerCounter > playerCounter:
                print("Bilgisayar kazandı !")
                repeat = input("Tekrar oynamak ister misin ? Evet/Hayır :")
                repeat = repeat.lower().strip()
                computerChoiceProvider = computerChoice[random.randint(0,1)]
                print(f"Bilgisayarın seçimi: {computerChoiceProvider}")

                if repeat == "evet" and computerChoiceProvider == "evet":
                    gameCounter += 1
                    computerCounter = 0
                    playerCounter = 0
                    roundCounter = 1
                elif repeat == "hayır" or computerChoiceProvider == "hayır":
                    break
                else:
                    print("Geçerli değer giriniz!")
                    break


            elif playerCounter > computerCounter:
                print("Oyuncu kazandı !")
                repeat = input("Tekrar oynamak ister misin ? Evet/Hayır :")
                repeat = repeat.lower().strip()
                computerChoiceProvider = computerChoice[random.randint(0,1)]
                print(f"Bilgisayarın seçimi: {computerChoiceProvider}")
                
                if repeat == "evet" and computerChoiceProvider == "evet":
                    gameCounter += 1
                    computerCounter = 0
                    playerCounter = 0
                    roundCounter = 1
                elif repeat == "hayır" or computerChoiceProvider == "hayır":
                    break
                else:
                    print("Geçerli değer giriniz!")
                    break


tas_kagit_makas_ATAMERT_CAN()
    

        
        


        







    