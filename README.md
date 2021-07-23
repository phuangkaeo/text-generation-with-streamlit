# Contexte du projet
La création de contenu est crucial lorsque l'on veut lancer son site. Il est nécéssaire d'identifier les mots clés sur lesquels vous voulez vous positionner et dans un second temps créér le contenu associé à ces mots clés.


La première étape de votre travail constitura la création de la liste des mots clés ainsi que la liste des questions à lesquelles il va falloir répondre à travers les articles à créer.


Etape 1 - Création de la liste de mots clés
Pour cela vous allez créer une fonction utilisant la requête suivante: https://importsem.com/query-google-suggestions-api-with-python/ (paramétrez en anglais). A la sortie de cette fonction vous allez récupérer un liste de mot clés en liens avec le mot clé d'input.

Exemple: get_list_kw("yoga") =>["yoga","yoga with adriene","yoga mat","yoga nidra","yoga poses","yoga pants"] Ici nous prendrons que 5 mots clé en plus de celui envoyé dans la requête.

Etape 2 - Identifier les questions
Dans un second temps vous allez récupérer les questions que les utilisateurs se posent suivants les mots chaque mots clés récupérés avec la library people_also_ask: https://pypi.org/project/people-also-ask/

Etape 3 - Récupérer les réponses aux questions
Toujours avec la library people_also_ask vous aller utiliser la méthode get_answer afin de récupérer la réponse au questions de l'étape 2.

Les 3 premières étapes consistent à créer la data qui va structurer le générateur de texte. Vous trouverez un exemple sur la structure de la donnée attendu dans la partie ressource.

Etape 4 - Génération de texte pour chaque ligne de votre jeu de donnée
Ici vous allez utiliser soit GPT-J, soit GPT-2 Large afin de générer du contenu pour chaque combinaison de question-réponse afin d'obtenir du contenu pour l'ensemble des mots clés. Pour cela vous allez devoir utiliser Google collab qui vous fournira l'environnement de développement adéquat pour cette tâche gourmande en ressource.
