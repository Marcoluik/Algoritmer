#Positivt heltal større end 0
#Finder hvad der går op i tæller og nævner
def Euklid(A,B):  # Tager parametrene A og B
    if A > 0 and B > 0:    #Tjekker om A og B er positivt
        int(A) , int(B)    #Konvertere til heltal
        while B != 0:      #Imens B ikke er 0
            if A > B:      #Hvis A er større end B, så A-b
                A = A-B
            else:          #Ellers B = B-A
                B = B-A
        return A           #Først når While er færdig, returenere den A, som er det mindste den går op i.

#Printer med 2 eksempler
print(Euklid(198,78))
print(Euklid(200,100))

