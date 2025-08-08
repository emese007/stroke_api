Stroke data project
===================

Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.


DATA PROCESSING:

1. Verification des data types et les valeurs manquantes

-Verification de doublons -----> pas de doublons dans les données

-Valeurs manquantes: bmi - 201
Traitement: Remplacement des valeurs manquantes en calculant le coefficient multiplicateur trouvé en divisant la médiane de la BMI par la médiane du taux de glucose. 
Formule pour une donnée "d1" : bmi_manquante_d1 = mediane_bmi/mediane_glucose * taux de glucose_d1

- identifier les incohérences éventuelles: 
La colonne 'gender' contient une seule valeur 'Other' - pas de traitement
La colonne 'avg_glucose_level' contient plusieurs valeurs superieurs à 180 (échelle normale: 0,70 – 1,80)jusqu'à 271
La colonne 'bmi' contient plusieurs valeurs supérieurs à 24,9 (échelle normale: 18,5 – 24,9)

Après analyse, ça s'avère que les valeurs si supérieures sont exceptionnelles / hautes mais pas impossibles.

-Identification des data types pour transformation:
Traitement:
gender                object  ----->  category (Female, Male, Other)
age                  float64  ----->  numeric
hypertension           int64  ----->  boolean (0,1)
heart_disease          int64  ----->  boolean (0,1)
ever_married          object  ----->  boolean (Yes,No)
work_type             object  ----->  category (Private, Self-employed, Govt_job, children, Never_worked)
Residence_type        object  ----->  category (Urban, Rural)
avg_glucose_level    float64  correct
bmi                  float64  correct
smoking_status        object  ----->  category (formerly smoked, never smoked, smokes, Unknown)
stroke                 int64  ----->  boolean (0,1)



2. Informations sur le type de fichier "parquet"

- Différence principale avec le format csv ?
Le csv est une format texte simple, sauvegarde les données par ligne, séparation virgule.
Le parquet est une format binaire colonnaire, qui stocke les données colonne par colonne, avec compression et conversation des types de données.
Le parquet est beaucoup plus rapide car il est capable de lire que certain colonnes à la fois sans lire les tout les données. Les fichiers sont beaucoup plus petits (grâce à la compression et au stockage colonnaire). Par contre, un CSV est plus simple à lire et partager, mais plus volumineux et plus lent sur les grand jeux de données.

- Dans quels cas l'utiliser ? 
Quant on travaille avec les données massives (machine learning, data engineering) ou on veut lire que certaines colonnes rapidement, et aussi pour archiver ou transfporter de gros ensembles des données en minimalisant la taille.

- Pourquoi c'est un format adapté aux gros volumes de données ?
Le stockage colonnaire permet de lire uniquement les colonnes nécessaires, donc on gagne le temps et des entrées/sorties disque sont reduit.
Le compression reduit la taille de fichiers (moins de stockage, transfert plus rapide)
Conservation des types : pas besoin de parser/convertir les valeurs (contrairement au CSV), ce qui accélère le traitement.

Sources: 
https://last9.io/blog/parquet-vs-csv/
https://stackoverflow.com/questions/36822224/what-are-the-pros-and-cons-of-the-apache-parquet-format-compared-to-other-format