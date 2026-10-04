# Sweet_Control : APK avec notifications Android

Dépôt GitHub (privé) = uniquement ces 3 fichiers :
- www/index.html
- capacitor.config.json
- .github/workflows/apk.yml

Construire l'APK : onglet Actions > "Construire l'APK" > Run workflow (5 à 10 min).
Récupérer l'APK : page principale du dépôt > Releases > "Sweet_Control (dernier APK)" > app-debug.apk.
(Ou dans l'exécution du workflow, section Artifacts > sweet-control-apk, c'est un zip.)

Supprime de l'ancien dépôt : .github/workflows/main.yml, server/ et google-services.json.
