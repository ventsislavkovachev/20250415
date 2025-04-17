Vous devez faire une IA capable de faire perdre du temps à des arnaqueurs téléphonique. Le but est d'être le plus convainquant possible pour garder l'escroc au téléphone.

Pour cela vous utiliserez de la reconnaissance vocale ainsi qu'un LLM (Large Language Model) puis un TTS (Text To Speech).

Vous devez rendre un dépôt Github avec un fichier README.md qui fait office de rapport ainsi que tout le code et instructions d'installation nécessaire au fonctionnement de l'outils. Vous ajouterez vos noms dans le rapport.

On vous fournis une base d'exemple avec les éléments suivants :

Commencer par faire un prompt système
Donner le contexte général
Donner la description de l'arnaque
Donner une personalité (nom, age, etc)
Donner des instructions sur ce que l'on cherche à faire (faire perdre le temps, format des réponse, etc)
Donner des instructions négative (ne pas dire que l'on est une IA, etc)
Récupérer ce que dit l'arnaqueur et l'envoyer comme prompt utilisateur.
Récupérer la sortie en stream.
Vous commencerez par ajouter la partie voix :

Reconnaisance vocale de l'arnaqueur
TTS (Text to speach) Pour parler à l'arnaqueur.
Vous devez ajouter tout ce qu'il faut pour rendre l'IA plus convaincante. Par exemple :

Reconnaissance de ton / emotion
Indication de ton pour la voix
Faire varier la longueur des réponses
Detection de silence
Ajouter des hésitations
Ajouter des lapsus (changer de mot)
Reformulation pour clarifier.
Respirations
etc