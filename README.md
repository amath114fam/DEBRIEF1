# Projet Orange Money – Simulation en Python
Description
--
Ce projet est une simulation simplifiée du service Orange Money réalisée en Python.
Il fonctionne en mode console et permet à un utilisateur de gérer un compte mobile money : consulter son solde, effectuer des transferts, acheter des forfaits et consulter l’historique des transactions.  

Le programme utilise la persistance des données avec des fichiers JSON, ce qui permet de conserver le solde et les transactions même après la fermeture du programme.
--
## Fonctionnalités principales  

  - Affichage du solde actuel  
  - Transfert d’argent vers un autre numéro  
  - Achat de forfaits internet  
  - Annulation du dernier transfert (une seule fois)  
  - Consultation de l’historique des transactions  
  - Sécurisation des opérations avec un code secret  
  - Sauvegarde automatique des données dans des fichiers JSON  

--
## Gestion des fichiers  

  - solde.json : stocke et met à jour le solde du compte  

  - transac.json : stocke l’historique des transactions effectuées  

  - Ces fichiers sont créés automatiquement s’ils n’existent pas.  
--
## Concepts utilisés  

  - Fonctions en Python  

  - Dictionnaires et listes  

  - Boucles (while)  

  - Conditions (if, match)  

  - Gestion des erreurs avec try / except  

  - Lecture et écriture de fichiers JSON  

  - Validation des saisies utilisateur  

## Lancement du programme

### Exécuter le fichier Python

   Saisir *#144#* pour accéder au menu  

   Naviguer dans le menu en entrant le numéro correspondant à l’action souhaitée  