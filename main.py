import json
def afficher_menu(): 
    """la fonction pour afficher le menu"""
    print("-" * 30)
    print(f"Solde actuel : {mon_compte["solde"]}")
    print("-" * 30)
    print("1. Acheter un forfait")
    print("2. Effectuer un transfert")
    print("3. Annuler le dernier transfert")
    print("4. Voir l’historique des transactions")
    print("5. Quitter")

    choix = input("Choisis un numéro : ")
    return choix

#**************le solde initial******************
mon_compte = {"solde" : 1000000}
#***********************************************

#*****************creation du fichier solde.json qui stocke et met à jour le solde**************
fichier = "solde.json"
def save():
    with open(fichier,"w", encoding="UTF8") as f:
        json.dump(mon_compte,f, indent=4)
try:
    with open(fichier,"r") as f:
        mon_compte = json.load(f)
except FileNotFoundError:
    save()
#*********************************************************************************************

#*****************creation du fichier transac.json qui stocke et met à jour le solde**************
listes_transactions = []
fichier1 = "transac.json"
def transaction():
    with open(fichier1,"w", encoding="UTF8") as f:
        json.dump(listes_transactions,f, indent=4)
try:
    with open(fichier1,"r") as f:
        listes_transactions = json.load(f)
except FileNotFoundError:
    transaction()
#************************************************************************************************
code_secret = 2002 #Initialisation du mot de passe Orange Money
#************************************************************************************************

def les_transactions():
    """Les transactions faits"""
    global listes_transactions
    print("-" * 10)
    if listes_transactions:
        print("Les transactions")
        for index, element in enumerate(listes_transactions, start=1) :
            numero = element["numero"]
            montant= element["montant"]
            print(f"{index}. Envoie de {montant}fcf au {numero} statut : {element["statut"]}")
    else:
        print("Aucune transaction disponible")
        print("-" * 10)
    print("-" * 10)
    print("1. Retour au menu")
    print("2. Quitter")
    choix_redirect = input("Choisis : ")
    if choix_redirect == "1":
        return
    elif choix_redirect == "2":
        print("-" * 10)
        exit()
    else:
        print("Saisie incorrecte")
        print("-" * 10)
        exit()
def transfert_argent():
    """Transfert d'argent"""
    global listes_transactions
    global stockage_transaction
    print("Vous voulez faire un transfert d'argent")
    print("-" * 5)
    numero = input("Entrer le numéro du destinataire : ").replace(" ", "")
    while len(numero) != 9 or not numero.isdigit() or not numero.startswith("77"):
        print("Saisie incorrect")
        numero = input("Entrer un numéro 77 ********: ").replace(" ", "")
    montant = input("Entrer le montant : ").replace(" ","")
    while len(montant) > 10 or not montant.isdigit() or int(montant) == 0 :
        print("Saisie incorrect")
        montant = input("Entrer le montant : ").replace(" ","")
    while True:
        code = input("Entrer ton code secret : ")
        try:
            if int(code) == code_secret:
                break
            else: 
                print("Code incorrect")
        except ValueError:
            print("Veuillez entrer un code valide")
    while mon_compte["solde"] < int(montant) : 
        print("Solde insuffisant")
        print(f"Veillez saisir un montant inférieur à {mon_compte["solde"]}")
        montant = input("Entrer le montant : ").replace(" ","")
        while len(montant) > 10 or not montant.isdigit() or int(montant) == 0:
            print("Saisie incorrect")
            montant = input("Entrer le montant : ").replace(" ","")
    mon_compte["solde"] -= int(montant)
    mes_transactions ={
        "numero" : numero,
        "montant" : montant,
        "statut" : "envoyé"
    }
    listes_transactions.append(mes_transactions)
    transaction()
    save()
    print("-" * 30)
    print(f"Vous avez effetué un transfert de {montant}f sur le numéro {numero}")
    print("-" * 30)
    print(f"Solde actuel : {mon_compte["solde"]}")
    print("-" * 30)
    print("1. Retour au menu")
    print("2. Quitter")
    choix_redirect = input("Choisis : ")
    if choix_redirect == "1":
        return
    elif choix_redirect == "2":
        print(".....................")
        exit()
    else:
        print("Saisie incorrecte")
        print(".....................")
        exit()
def forfait():
    """Acheter un forfait"""
    global code_secret
    while True:
        print("Vous voulez acheté un forfait ")
        print("-" * 5)
        print("1. Pass 100 Mo à 500f")
        print("2. Pass 500 Mo à 1000f")
        print("3. Pass 1 Go à 2000f")
        montant_forfait = {
            "forfait1" : 500,
            "forfait2" : 1000,
            "forfait3" : 2000,
        }
        choix_forfait = input("Choisis 1 ou 2 ou 3 : ")
        if choix_forfait == "1":
            numero = input("Entrer le numéro le numéro du destinataire : ").replace(" ", "")
            while len(numero) != 9 or not numero.isdigit() or not numero.startswith("77"):
                print("Saisie incorrect")
                numero = input("Entrer un numéro 77 ********: ").replace(" ", "")
            while True:
                code = input("Entrer ton code secret : ")
                try:
                    if int(code) == code_secret:
                        break
                    else: 
                        print("Code incorrect")
                except ValueError:
                    print("Veuillez entrer un code valide")
            if mon_compte["solde"] < montant_forfait["forfait1"]:
                print("solde insuffisant")
                break
            else:
                print("-" * 30)
                print(f"vous avez activé le pass 500 Mo à 1000f sur le numéro {numero}")
                print("-" * 30)
                mon_compte["solde"] -= montant_forfait["forfait1"]
                save()
        elif choix_forfait == "2":
            numero = input("Entrer le numéro le numéro du destinataire : ").replace(" ", "")
            while len(numero) != 9 or not numero.isdigit() or not numero.startswith("77"):
                print("Saisie incorrect")
                numero = input("Entrer un numéro 77 ********: ").replace(" ", "")
            while True:
                code = input("Entrer ton code secret : ")
                try:
                    if int(code) == code_secret:
                        break
                    else: 
                        print("Code incorrect")
                except ValueError:
                    print("Veuillez entrer un code valide")
            if mon_compte["solde"] < montant_forfait["forfait2"]:
                print("solde insuffisant")
                break
            else:
                print("-" * 30)
                print(f"vous avez activé le pass 500 Mo à 1000f sur le numéro {numero}")
                print("-" * 30)
                mon_compte["solde"] -= montant_forfait["forfait2"]
                save()
        elif choix_forfait == "3":
            numero = input("Entrer le numéro le numéro du destinataire : ").replace(" ", "")
            while len(numero) != 9 or not numero.isdigit() or not numero.startswith("77"):
                print("Saisie incorrect")
                numero = input("Entrer un numéro 77 ********: ").replace(" ", "")
            while True:
                code = input("Entrer ton code secret : ")
                try:
                    if int(code) == code_secret:
                        break
                    else: 
                        print("Code incorrect")
                except ValueError:
                    print("Veuillez entrer un code valide")
            if mon_compte["solde"] < montant_forfait["forfait3"]:
                print("solde insuffisant")
                break
            else:
                print("-" * 30)
                print(f"vous avez activé le pass 1Go Mo à 2000f sur le numéro {numero}")
                print("-" * 30)
                mon_compte["solde"] -= montant_forfait["forfait3"]
                save()
        else :
            print("Choix invalide ")
            print("-" * 30)
            return
        print("-" * 30)
        print(f"Solde actuel : {mon_compte["solde"]}")
        print("-" * 30)
        print("1. Retour au menu")
        print("2. Quitter")
        choix_redirect = input("Choisis 1 ou 2 : ")
        if choix_redirect == "1":
            return
        elif choix_redirect == "2":
            exit()
        else:
            print("Choix invalide ")
            print(".....................")
            return
fichier3 = "last_annulation.json"
nombre_annulation = {"last_delete" : 0} #ça permet de suivre combien de fois on a fait une annulation
def transaction_annulée():
    with open(fichier3,"w") as file:
        json.dump(nombre_annulation,file,indent=4)
try:
    with open(fichier3,"r") as file:
        nombre_annulation = json.load(file)
except FileNotFoundError:
    transaction_annulée()
    
def annuler_transaction():
    # global nombre_annulation
    global listes_transactions
    nombre_annulation["last_delete"] = 1
    transaction_annulée()
    if listes_transactions:
        dernier_transac = listes_transactions[-1]["montant"]
        while True:
            print(dernier_transac)
            print("Vous voulez annuler une transaction ")
            print("-" * 10)
            code = input("Entrer ton code secret : ")
            try :
               if int(code) == code_secret:
                   break
               else:
                print("Code incorrect")
            except ValueError:
               print("Veuillez entrer un nombre valide")
        mon_compte["solde"] += int(dernier_transac)
        save()
        listes_transactions[-1]["statut"] = "annulé"
        transaction()
        print("-" * 10)
        print("Transaction annulée")
        print("-" * 10)
        return
    else:
        print("Aucune transaction disponible")
        print("......")
#***************************l'accueil à chaque fois qu'on lance le programme**************
saisie = input("Veillez entrer le #144# : ")
while saisie != "#144#":
    print("Tu es sur la page Orange money ")
    saisie = input("Veillez saisir #144# pour débuter : ")
#****************************************************************************************

#*****************************affichage du menu *****************************************
while True:
    choix = afficher_menu()
    match choix:
        case "1":
            print("-" * 30)
            forfait()
            print("-" * 30)
        case "2":
            print("-" * 30)
            transfert_argent()
            print("-" * 30)
        case "3":
            if nombre_annulation["last_delete"] < 1:
                annuler_transaction()
            else:
                print("-" * 30)
                print("Impossible d'annuler le dernier transaction")
                print("-" * 30)
        case "4":
            print("-" * 30)
            les_transactions()
            print("-" * 30)
        case "5":
            break
        case _:
            print("Veillez choisir un numéro valide")
            
