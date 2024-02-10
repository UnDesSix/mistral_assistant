Exercice 1: Manipulation de chaînes de caractères

1. `reverse_string(s)` : Cette fonction prend une chaîne de caractères en entrée et renvoie la chaîne inversée. L'opérateur `[::-1]` est utilisé pour inverser la chaîne sans créer de chaîne supplémentaire.
2. `capitalize_first_letter(s)` : Cette fonction prend une chaîne de caractères en entrée et renvoie la chaîne avec la première lettre en majuscule et le reste en minuscule. `s[0].upper()` convertit le premier caractère en majuscule et `s[1:].lower()` convertit le reste de la chaîne en minuscule.
3. `count_vowels(s)` : Cette fonction prend une chaîne de caractères en entrée et renvoie le nombre de voyelles dans la chaîne. La boucle `for` parcourt chaque caractère de la chaîne en minuscule et vérifie s'il est présent dans la chaîne de voyelles. Si c'est le cas, 1 est ajouté au compteur.

---

Exercice 2: Listes et tuples

1. `common_elements(l1, l2)` : Cette fonction prend deux listes en entrée et renvoie une nouvelle liste contenant les éléments communs aux deux listes d'entrée. La liste de compréhension `[element for element in l1 if element in l2]` parcourt chaque élément de la première liste et vérifie s'il est présent dans la deuxième liste. Si c'est le cas, il est ajouté à la nouvelle liste.
2. `remove_duplicates(l)` : Cette fonction prend une liste en entrée et renvoie une nouvelle liste contenant les mêmes éléments sans répétition. La fonction `set()` est utilisée pour convertir la liste en ensemble, supprimant ainsi les doublons, puis la liste est convertie à nouveau en liste.
3. `list_to_tuple(l)` : Cette fonction prend une liste en entrée et renvoie un tuple contenant les mêmes éléments. La fonction `tuple()` est utilisée pour convertir la liste en tuple.

---

Exercice 3: Dictionnaires

1. `word_count(s)` : Cette fonction prend une chaîne de caractères en entrée et renvoie un dictionnaire avec les mots de la chaîne comme clés et leur nombre d'occurrences comme valeurs. La chaîne est d'abord divisée en mots, puis une boucle parcourt chaque mot et met à jour le dictionnaire.
2. `update_dictionary(d1, d2)` : Cette fonction prend deux dictionnaires en entrée et met à jour le premier dictionnaire avec les paires clé-valeur du deuxième dictionnaire. Une boucle parcourt chaque paire clé-valeur du deuxième dictionnaire et met à jour le premier dictionnaire si la clé est présente, sinon elle ajoute la paire clé-valeur au premier dictionnaire.

---

Exercice 4: Structures de contrôle

1. `factorial(n)` : Cette fonction prend un entier en entrée et renvoie sa factorielle. Une boucle `for` parcourt les entiers de 1 à n et multiplie le résultat par l'entier courant à chaque itération.
2. `fibonacci(n)` : Cette fonction prend un entier en entrée et renvoie le n-ième nombre de la suite de Fibonacci. Une boucle `for` parcourt les entiers de 0 à n-1 et met à jour les variables a et b pour calculer le n-ième nombre de la suite.
3. `is_prime(n)` : Cette fonction prend un entier en entrée et renvoie True si l'entier est premier et False sinon. Une boucle `for` parcourt les entiers de 2 à la racine carrée de n et vérifie si n est divisible par l'entier courant. Si c'est le cas, la fonction renvoie False.

---

Exercice 5: Applications avancées

1. `calculate_average(l)` : Cette fonction prend une liste de nombres en entrée et renvoie la moyenne des nombres de la liste. Si la liste est vide, la fonction renvoie None.
2. `sort_list_of_tuples(l)` : Cette fonction prend une liste de tuples en entrée et renvoie la liste triée par la première valeur de chaque tuple. La fonction `sorted()` est utilisée avec la fonction `lambda` pour trier la liste en fonction de la première valeur de chaque tuple.
3. `reverse_list(l)` : Cette fonction prend une liste en entrée et renvoie la liste inversée. Une boucle `for` parcourt la moitié de la liste et échange les éléments de l'indice courant avec l'élément de l'indice correspondant dans la deuxième moitié de la liste.