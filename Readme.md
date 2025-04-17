On va s'attacker les arnaqueor sur internet

In Terminal:
python -m venv .venv

.venv/bin/activate
si no..
dans .venv\Sripts ./Activate.ps1

pip install huggingface_hub

https://studio.nebius.com/settings/api-keys

https://huggingface.co

pip install --upgrade google-cloud-texttospeech

(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe

## La base
* Commencer par faire un prompt systeme
    - Donner le contexte general
    - Donner la description de l'arnaque
    - Donner une personalite (nom, age, etc.)
    - Donner des instructions sur ce que l'on cherche a faire (faire perdre du temp, format des reponces; etc)
    - Donner des instructions negative (ne pas dire que l'on est un IA, etc.)

* Recupere ce que dit l'arnaqeur et l'envoyer comm prompte utilisateur.
* Recuperer le sortie en stream

## Voix
* Reconnaisanse vocale
* TTS (Text to speach) pour parler a l'arnaqeur

## Plus avance
* Reconaissance du ton / emotion
* Indication de ton pour la voix
* Faire varier la longeur des reponces
* Detection du silence
* Ajouter des hesitations
* Ajouter des lapsus (changer de mots)
* Reformation pour clarifier
* Respirations

