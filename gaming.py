class Gaming:
    
    def __init__(self):
        user_name = input("Enter User Name : ")
        while True:
            print (f''' Heloo Mr : {user_name} Enter your Number :
        1.numper sherts Alhilal player.
        2.name Alhilal Player.
        3.your berhtday for Alhilal.
        4. you want Exsit Enter X''')
            gaming  = input("Enter Numper for gaming : ")
            if gaming == "1" :
                sherts = int(input("Enter numper shirts : "))
                self.sherts_Alhilal(sherts)
            elif gaming == "2":
                name = int(input("Enter name player : "))
                self.name_player(name)
            elif gaming == "3":
                birthday = int(input("Enter your Birthday:")) 
                self.birthday_player(birthday)
            elif gaming == "x":
                print("Good luke")
                break
            
            print ("---------------------")
    def sherts_Alhilal(self,sherts):
        if sherts == 1:
            print ("ALMUAIOUF, ABDULLAH IBRAHIM A")
        elif sherts == 9:
            print ("IGHALO ODION JUDE")
        elif sherts == 7:
            print ("ALFARAJ, SALMAN MOHAMMED M")
        elif sherts == 5:
            print ("AL BULAYHI, ALI HADI M")
        elif sherts == 70:
            print ("JAHFALI, MOHAMMED YAHYA S")
        elif sherts == 17:
            print ("MAREGA MOUSSA")
        elif sherts == 19:
            print ("CARRILLO DIAZ ANDRE MARTIN")
        elif sherts == 29:
            print ("LDAWSARI, SALEM MOHAMMED S")
        elif sherts == 20:
            print ("JANG HYUNSOO")
        elif sherts == 33:
            print ("ALJADANI, ABDULLAH SHAMLAH O")
        elif sherts == 21:
            print ("ALOWAIS, MOHAMMED KHALIL I")
        elif sherts == 12:
            print ("ALSHAHRANI, YASIR GHARSAN S")
        elif sherts == 8:
            print ("OTAYF, ABDULLAH IBRAHIM Y")
        elif sherts == 2:
            print ("ALBURAYK, MOHAMMED IBRAHIM M")
        elif sherts == 6:
            print ("CUELLAR GALLEGO GUSTAVO LEONARDO")
        elif sherts == 11:
            print ("ALSHEHRI, SALEH KHALID M")
        elif sherts == 28:
            print ("KANNO. MOHAMED IBRAHIM A")
        elif sherts == 15:
            print ("COSTA PEREIRA MATHEUS FELLIPE")
        elif sherts == 32:
            print ("ALMUFARRIJ, MUTEB ABDULLAH A")
        elif sherts == 16:
            print ("ALDAWSARI, NASSER ESSA S")
        elif sherts == 88:
            print ("ALTUHAYFAN, HAMAD TURKI H")
        elif sherts == 66:
            print ("ABDULHAMID, SAUD ABDULLAH S")
        elif sherts == 14:
            print ("AALHAMDDAN, ABDULLAH ABDULRAHMAN A")
        elif sherts == 44:
            print ("ALNASSER. SAAD FAHAD S")
        elif sherts == 69:
            print ("ALKHAIBARI, MOHAMMED NAIF A")
        elif sherts == 56:
            print ("ALQAHTANI, MOHAMMED HAMAD D")
        elif sherts == 49:
            print ("RADIF, ABDULLAH HADI J")
        elif sherts == 43:
            print ("ALJUWAYR, MUSAB FAHAD Z")
        elif sherts == 96:
            print ("DELGADO ED OLIVEIRA MICHAEL RICHARD")
        else:
            print ("dont have player")
    def name_player(self,name):
        if name == 1:
            print ("  ALMUAIOUF ,Goals: 1 ,Asisst: 1 , Goalkeeper")
        elif name == 9:
            print (" IGHALO, Goals: 24 ,Asisst: 9 , Attacker")
        elif name == 7:
            print ("ALFARAJ , Goals: 2 ,Asisst: 5 , Midfielder")
        elif name == 5:
            print ("Goals: 3 ,Asisst: 2 , Difender")
        elif name == 70:
            print ("JAHFALI , Goals: 1 ,Asisst: 0 , Difender")
        elif name == 17:
            print ("MAREGA , Goals: 10 ,Asisst: 5 , Attacker")
        elif name == 19:
            print ("CARRILLO,Goals: 4 ,Asisst: 15 , Midfielder")
        elif name == 29:
            print ("SALEM , Goals: 12 ,Asisst: 8 , Midfielder")
        elif name == 20:
            print ("JANG , Goals: 2 ,Asisst: 0 , Difender")
        elif name == 33:
            print ("ALJADANI , Goals: 0 ,Asisst: 0 , Goalkeeper")
        elif name == 21:
            print ("ALOWAIS , Goals: 0 ,Asisst: 0 , Goalkeeper")
        elif name == 12:
            print ("ALSHAHRANI , Goals: 1 ,Asisst: 6 , Difender")
        elif name == 8:
            print ("OTAYF , Goals: 0 ,Asisst: 1 , Midfielder")
        elif name == 2:
            print ("ALBURAYK , Goals: 0 ,Asisst: 5 , Difender")
        elif name == 6:
            print ("CUELLAR ,Goals: 0 ,Asisst: 0 , Midfielder")
        elif name == 11:
            print ("ALSHEHRI ,Goals: 1 ,Asisst: 2 , Attacker")
        elif name == 28:
            print ("KANNO , Goals: 0 ,Asisst: 0 , Midfielder")
        elif name == 15:
            print ("PEREIRA ,Goals: 3 ,Asisst: 15 , Midfielder")
        elif name == 32:
            print ("ALMUFARRIJ , Goals: 0 ,Asisst: 0 , Difender")
        elif name == 16:
            print ("ALDAWSARI , Goals: 2 ,Asisst: 4 , Midfielder")
        elif name == 88:
            print ("ALTUHAYFAN , Goals: 0 ,Asisst: 5 , Difender")
        elif name == 66:
            print ("ABDULHAMID , Goals: 0 ,Asisst: 10 , Difender")
        elif name == 14:
            print ("AALHAMDDAN , Goals: 3 ,Asisst: 2 , Attacker")
        elif name == 44:
            print ("ALNASSER , Goals: 0 ,Asisst: 0 , Difender")
        elif name == 69:
            print ("ALKHAIBARI , Goals: 0 ,Asisst: 0 , Difender")
        elif name == 56:
            print ("ALQAHTANI , Goals: 0 ,Asisst: 0 , Midfielder")
        elif name == 49:
            print ("RADIF , Goals: 0 ,Asisst: 0 , Midfielder")
        elif name == 43:
            print ("ALJUWAYR , Goals: 0 ,Asisst: 2 , Midfielder")
        elif name == 96:
            print ("MICHAEL , Goals: 7 ,Asisst: 7 , Midfielder")
        else:print ("dont have player")
    def birthday_player(self,birthday):
        print (2022 - birthday)
g1  =  Gaming()
    
