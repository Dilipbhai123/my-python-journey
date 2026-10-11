import random

#યુઝર કયા નંબર થી સુ પસંદ કરી સકે તે માટે નું અને ઈનપુટ આપી સકે
print("Rock : 4 , Paper : 8 , Scissors : 12")
user = int(input("Entar Your first Number :"))

#પહેલા વેલ્યુ ચેક થાય અને જો તે 4, 8, 12 સિવાય હોય તો કોડ આટલેથી બ્રેક થસે 
if user == 4 or user == 8 or user == 12:

     # રેન્ડમ ફૂંકસન થી કોમ્પ્યુટર ચોઇસે પસંદ કરાવવી 
     choise = [4, 8, 12]
     computar = random.choice(choise)
     
     #રોક પેપર સીસેર ગેમ માટેનો ઇમ્પોર્ટેંટ કોડ
     if user == 4 and computar == 12:
         print("user is win is Rock")
     
     elif user == 8 and computar == 12:
         print("computar is win is Scissors")
     
     elif user == 12 and computar == 4:
         print("computar is win is Rock")
     
     elif user == 12 and computar == 8:
         print("user is win is Scissors")
     
     elif user == 8 and computar == 4:
         print("user is win is Paper")
     
     elif user == 4 and computar == 8:
         print("computar is win is Paper")
     
     elif user == computar:
         print("Not For The Win Game IS Drow")

else:
    print("your choice value is wrong")