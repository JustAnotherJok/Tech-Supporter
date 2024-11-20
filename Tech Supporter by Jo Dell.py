import tkinter as tk
from tkinter import messagebox, ttk 
import unicodedata

# Fonction pour normaliser les mots-clés
def normalize_keyword(keyword):
    return ''.join(
        c for c in unicodedata.normalize('NFD', keyword)
        if unicodedata.category(c) != 'Mn'
    ).lower()

# Dictionnaire de problèmes informatiques et des étapes de dépannage correspondantes
troubleshooting_guide = { 
    "l'ordinateur ne démarre pas": [ 
    "Étape 1 : Vérification d'alimentation\n\n"
    "PC de bureau : Demandez au client de vérifier si le câble d'alimentation est bien branché, "
    "si l'interrupteur de l'alimentation (à l'arrière de l'unité centrale) est en position 'ON', "
    "et si la multiprise ou la prise murale fonctionne (en branchant un autre appareil dessus).\n\n"
    "Ordinateur portable : Demandez au client de vérifier que le chargeur est bien connecté. Si la batterie est amovible, "
    "suggérez de la retirer, puis de brancher le chargeur pour voir si l'ordinateur démarre sans la batterie.\n",
    "Étape 2 : Vérification des signes de vie\n\n"
    "Vérifiez s'il y a des bruits (ventilateurs, disques durs) ou des voyants lumineux lorsque le bouton de démarrage est pressé.\n\n"
    "S'il y a des bips sonores, ils peuvent indiquer un problème matériel. Le nombre de bips et leur séquence peuvent parfois fournir des indices.\n",
    "Étape 3 : Réinitialisation matérielle\n\n"
    "PC de bureau : Demandez au client de maintenir le bouton d’alimentation enfoncé pendant environ 10 secondes pour décharger l’électricité résiduelle, puis d’essayer de redémarrer.\n\n"
    "Ordinateur portable : S’il est possible de retirer la batterie, faites-lui débrancher le chargeur et la batterie, "
    "maintenir le bouton d’alimentation enfoncé pendant 30 secondes, puis de rebrancher uniquement le chargeur et essayer de démarrer.\n",
    "Étape 4 : Diagnostic de l’écran\n\n"
    "Vérifiez si l’écran est bien allumé ou si l’ordinateur démarre mais que l’écran reste noir. Parfois, il peut sembler que l’ordinateur ne démarre pas alors qu’il s’agit d’un problème d’affichage.\n",
    "Étape 5 : Vérification des erreurs ou codes affichés\n\n"
    "Si des messages d’erreur apparaissent brièvement (par exemple un logo ou un message d’erreur BIOS), ils peuvent être des indices précieux.\n",
    "Étape 6 : Vérifiez le matériel si possible\n\n"
    "Si le client est à l’aise, il peut ouvrir le boîtier pour vérifier que les composants (RAM, carte graphique, disques durs) sont bien connectés.\n"
    ],
    "périphérique USB non reconnu ou ne s'affiche pas dans l'explorateur de fichiers": [
        "Étape 1 : Vérifiez que le périphérique est correctement connecté à un port USB fonctionnel.\n",
        "Étape 2 : Essayez un autre port USB sur l'ordinateur pour vérifier si le problème vient du port.\n",
        "Étape 3 : Essayer le périphérique sur un autre ordinateur et si le périphérique ne fonctionne pas sur un autre ordinateur, il peut être défectueux.\n",
        "Étape 4 : Ouvrir le gestionnaire de disque pour afficher les lecteurs tels que USB.\n",
        "Étape 5 : Si une partition est déjà visible, assigner une lettre au lecteur.\n",
        "Étape 6 : Si l'espace du disque est non alloué, créer un nouveau volume.\n",
        "Étape 7 : Vérifiez dans le BIOS/UEFI si les ports USB sont activés.\n",
        "Étape 8 : Essayez de démarrer en mode sans échec pour diagnostiquer un conflit logiciel.\n",
        "Étape 9 : Si le périphérique ne fonctionne pas sur un autre ordinateur, il peut être défectueux.\n",
        "Étape 10 : Désactivez et réactivez les contrôleurs USB dans le Gestionnaire de périphériques, puis redémarrez l'ordinateur.\n"
    ],
     "écran noir ou vide": [
        "Étape 1 : Vérifiez que le câble de l'écran est bien connecté à l'ordinateur.\n",
        "Étape 2 : Essayez un autre câble ou un autre écran pour exclure un problème d'écran défectueux.\n",
        "Étape 3 : Vérifiez si l'ordinateur émet des bips au démarrage, ce qui peut indiquer un problème matériel.\n",
        "Étape 4 : Si vous avez un ordinateur portable, essayez de connecter un écran externe.\n",
        "Étape 5 : Si aucune image n'apparait, il pourrait y avoir un problème avec la carte graphique ou la carte mère.\n"
    ],
      "problème de connexion Wi-Fi intermittente": [
        "Étape 1 : Vérifiez si votre routeur est obstrué par des objets ou se trouve dans une zone où le signal est faible.\n",
        "Étape 2 : Changez le canal Wi-Fi de votre routeur pour éviter les interférences avec d'autres réseaux à proximité.\n",
        "Étape 3 : Mettez à jour le firmware de votre routeur pour corriger les éventuels bugs de connectivité.\n",
        "Étape 4 : Testez la connexion avec un autre appareil pour vérifier si le problème vient du périphérique.\n",
        "Étape 5 : Vérifiez les paramètres d'économie d'énergie de votre carte Wi-Fi pour s'assurer qu'elle ne s'éteint pas automatiquement.\n",
        "Étape 6 : Désactivez la fonction d'économie d'énergie du routeur si elle est activée.\n",
        "Étape 7 : Si le problème persiste, essayez de remplacer la carte Wi-Fi de votre ordinateur ou d'utiliser un adaptateur Wi-Fi externe.\n"
    ],
     "imprimante ne répond pas": [
        "Étape 1 : Vérifiez si l'imprimante est allumée et si elle est correctement branchée à l'ordinateur ou au réseau.\n",
        "Étape 2 : Vérifiez si des erreurs ou des messages d'alerte sont affichés sur l'écran de l'imprimante.\n",
        "Étape 3 : Redémarrez l'imprimante et essayez à nouveau.\n",
        "Étape 4 : Vérifiez le statut de l'imprimante dans le panneau de contrôle des périphériques de votre ordinateur.\n",
        "Étape 5 : Si l'imprimante est en mode hors ligne, remettez-la en ligne via les paramètres de l'ordinateur.\n",
        "Étape 6 : Vérifiez si l'imprimante est correctement connectée à un réseau sans fil ou via un câble USB.\n",
        "Étape 7 : Réinstallez ou mettez à jour les pilotes de l'imprimante depuis le site Web du fabricant.\n",
        "Étape 8 : Si le problème persiste, essayez d'imprimer à partir d'un autre ordinateur pour vérifier si l'imprimante fonctionne.\n"
    ],
    "imprimante impression de mauvaise qualité": [
        "Étape 1 : Vérifiez si l'encre ou le toner de l'imprimante est suffisant.\n",
        "Étape 2 : Vérifiez si les cartouches d'encre ou les toners sont correctement installés.\n",
        "Étape 3 : Nettoyez les têtes d'impression via le menu de l'imprimante ou l'outil de nettoyage du logiciel de l'imprimante.\n",
        "Étape 4 : Assurez-vous que le bon type de papier est utilisé et qu'il est chargé correctement dans le bac.\n",
        "Étape 5 : Vérifiez la résolution d'impression dans les paramètres du travail d'impression et ajustez-la si nécessaire.\n",
        "Étape 6 : Réalisez un test d'impression pour vérifier si le problème persiste après les ajustements.\n",
        "Étape 7 : Si l'impression est toujours de mauvaise qualité, remplacez les cartouches d'encre ou le toner.\n"
    ],
    "imprimante ne se connecte pas au réseau": [
        "Étape 1 : Vérifiez si l'imprimante est correctement connectée au réseau sans fil ou au réseau local.\n",
        "Étape 2 : Assurez-vous que l'imprimante et l'ordinateur sont connectés au même réseau Wi-Fi.\n",
        "Étape 3 : Redémarrez l'imprimante et le routeur pour résoudre d'éventuels problèmes de réseau.\n",
        "Étape 4 : Vérifiez si le mot de passe du réseau Wi-Fi est correctement configuré sur l'imprimante.\n",
        "Étape 5 : Si l'imprimante utilise un câble Ethernet, assurez-vous que le câble est bien connecté et en bon état.\n",
        "Étape 6 : Réinitialisez les paramètres réseau de l'imprimante et reconnectez-la au réseau.\n",
        "Étape 7 : Si nécessaire, réinstallez les pilotes de l'imprimante pour corriger les problèmes de connectivité.\n"
    ],
     "imprimante ne repond pas aux commandes impression": [
    "Étape 1 : Vérifiez que l'imprimante est allumée et connectée correctement à l'ordinateur ou au réseau.\n",
    "Étape 2 : Assurez-vous qu'il n'y a pas de messages d'erreur affichés sur l'écran de l'imprimante.\n",
    "Étape 3 : Vérifiez l'état de l'imprimante dans le panneau de configuration pour voir si elle est hors ligne ou en pause.\n",
    "Étape 4 : Redémarrez l'imprimante ainsi que l'ordinateur pour résoudre d'éventuels problèmes de communication.\n",
    "Étape 5 : Assurez-vous que l'imprimante est définie comme l'imprimante par défaut dans les paramètres de l'ordinateur.\n",
    "Étape 6 : Supprimez tous les travaux d'impression en attente et essayez de relancer l'impression.\n",
    "Étape 7 : Mettez à jour ou réinstallez les pilotes de l'imprimante depuis le site du fabricant.\n",
    "Étape 8 : Si le problème persiste, essayez de connecter l'imprimante à un autre ordinateur pour vérifier si elle répond.\n"
    ],
     "aucun son haut parleurs ordinateur": [
    "Étape 1 : Vérifiez que les haut-parleurs sont correctement connectés et allumés (si ce sont des haut-parleurs externes).\n",
    "Étape 2 : Assurez-vous que le volume de l’ordinateur et des haut-parleurs n'est pas coupé ou réglé trop bas.\n",
    "Étape 3 : Vérifiez les paramètres audio de votre système pour vous assurer que les haut-parleurs sont sélectionnés comme périphérique de sortie par défaut.\n",
    "Étape 4 : Redémarrez l'ordinateur pour résoudre d'éventuels conflits logiciels.\n",
    "Étape 5 : Branchez des écouteurs ou un autre périphérique audio pour vérifier si le problème vient des haut-parleurs ou de la carte son.\n",
    "Étape 6 : Mettez à jour ou réinstallez les pilotes audio dans le Gestionnaire de périphériques.\n",
    "Étape 7 : Si aucune des étapes précédentes ne fonctionne, cela peut indiquer un problème matériel avec les haut-parleurs ou la carte son. Consultez un technicien si nécessaire.\n"
    ],
     "aucun son haut parleurs internes ordinateur": [
    "Étape 1 : Assurez-vous que le volume de l’ordinateur n’est pas coupé et qu'il est réglé à un niveau audible.\n",
    "Étape 2 : Vérifiez les paramètres audio de votre système pour vous assurer que les haut-parleurs internes sont sélectionnés comme périphérique de sortie par défaut.\n",
    "Étape 3 : Redémarrez l'ordinateur pour éliminer d'éventuels problèmes logiciels temporaires.\n",
    "Étape 4 : Mettez à jour ou réinstallez les pilotes audio dans le Gestionnaire de périphériques.\n",
    "Étape 5 : Si votre ordinateur est équipé d'un clavier avec touches de contrôle du volume, assurez-vous que le son n'est pas coupé depuis ces touches.\n",
    "Étape 6 : Essayez de démarrer en mode sans échec pour voir si le problème audio est lié à un logiciel tiers.\n",
    "Étape 7 : Si le problème persiste, cela peut être dû à une défaillance matérielle des haut-parleurs internes ou de la carte son. Consultez un technicien si nécessaire.\n"
    ],
     "ordinateurs reseau local ne communiquent pas": [
    "Étape 1 : Vérifiez que tous les ordinateurs sont connectés au même réseau local (vérifiez le nom du réseau Wi-Fi ou le routeur utilisé pour les connexions câblées).\n",
    "Étape 2 : Assurez-vous que chaque ordinateur a une adresse IP unique. Pour ce faire, redémarrez chaque appareil ou utilisez l'option de renouvellement d'adresse IP.\n",
    "Étape 3 : Vérifiez que le partage de fichiers et d'imprimantes est activé dans les paramètres réseau de chaque ordinateur.\n",
    "Étape 4 : Désactivez temporairement les pare-feu sur chaque ordinateur pour voir si cela résout le problème de communication.\n",
    "Étape 5 : Si un VPN est activé sur un ordinateur, désactivez-le temporairement car il peut interférer avec le réseau local.\n",
    "Étape 6 : Redémarrez le routeur et les ordinateurs pour réinitialiser les connexions réseau.\n",
    "Étape 7 : Assurez-vous que tous les ordinateurs sont dans le même groupe de travail (sur les systèmes Windows, vérifiez les paramètres de groupe de travail dans les propriétés système).\n",
    "Étape 8 : Si le problème persiste, il peut être dû à une incompatibilité des paramètres réseau. Essayez de réinitialiser les paramètres réseau de chaque ordinateur.\n"
    ],
     "logiciel ferme de manière inattendue ou ne repond pas": [
    "Étape 1 : Redémarrez le logiciel pour voir s'il s'ouvre normalement après un redémarrage.\n",
    "Étape 2 : Vérifiez si des mises à jour du logiciel sont disponibles et installez-les, car cela peut corriger les bugs.\n",
    "Étape 3 : Fermez les autres applications pour libérer des ressources système (RAM et processeur) qui pourraient être nécessaires.\n",
    "Étape 4 : Redémarrez l'ordinateur pour résoudre d'éventuels conflits logiciels.\n",
    "Étape 5 : Désactivez temporairement votre antivirus ou pare-feu, car ils peuvent parfois bloquer certains logiciels.\n",
    "Étape 6 : Lancez le logiciel en mode administrateur pour voir si le problème est lié aux permissions.\n",
    "Étape 7 : Si le logiciel ne fonctionne toujours pas, réinstallez-le pour remplacer les fichiers corrompus.\n",
    "Étape 8 : Vérifiez les journaux d'événements (sur Windows, via l'Observateur d'événements) pour identifier toute erreur spécifique liée au logiciel.\n",
    "Étape 9 : Si le problème persiste, consultez la documentation officielle du logiciel ou contactez le support technique pour plus d'aide.\n"
    ],
     "sauvegardes automatiques ne se réalisent pas": [
    "Étape 1 : Vérifiez les paramètres de sauvegarde automatique pour vous assurer qu'ils sont correctement configurés.\n",
    "Étape 2 : Assurez-vous que l'espace de stockage disponible sur le disque ou dans le cloud est suffisant pour effectuer la sauvegarde.\n",
    "Étape 3 : Vérifiez que le logiciel de sauvegarde est à jour, et mettez-le à jour si nécessaire.\n",
    "Étape 4 : Vérifiez les horaires de sauvegarde pour vous assurer qu'ils ne sont pas mal configurés ou que le programme ne tente pas de sauvegarder à des moments inappropriés.\n",
    "Étape 5 : Assurez-vous que l'ordinateur est allumé et connecté à Internet (si la sauvegarde se fait dans le cloud).\n",
    "Étape 6 : Redémarrez le logiciel de sauvegarde ou l'ordinateur pour résoudre tout problème temporaire.\n",
    "Étape 7 : Si la sauvegarde est planifiée via un service en ligne, vérifiez les paramètres du service (comme Google Drive, OneDrive, ou autres) pour s'assurer qu'il n'y a pas de problèmes de synchronisation.\n",
    "Étape 8 : Consultez les journaux de sauvegarde du logiciel pour repérer des erreurs éventuelles.\n",
    "Étape 9 : Si le problème persiste, essayez de réinitialiser ou de réinstaller le logiciel de sauvegarde.\n",
    "Étape 10 : Si le problème est lié à un disque dur externe ou un périphérique de stockage, vérifiez s'il est correctement connecté et fonctionne normalement.\n"
    ],
     "connexion ethernet ne fonctionne pas": [
    "Étape 1 : Vérifiez que le câble Ethernet est correctement branché à la fois sur l'ordinateur et le routeur ou le modem.\n",
    "Étape 2 : Essayez un autre câble Ethernet pour vérifier que le câble actuel n'est pas défectueux.\n",
    "Étape 3 : Vérifiez que le port Ethernet de l'ordinateur fonctionne correctement en testant avec un autre appareil.\n",
    "Étape 4 : Redémarrez le routeur et l'ordinateur pour réinitialiser les connexions réseau.\n",
    "Étape 5 : Vérifiez les paramètres IP de l'ordinateur. Assurez-vous que l'adresse IP est attribuée automatiquement (via DHCP).\n",
    "Étape 6 : Vérifiez que la carte réseau Ethernet est activée dans le Gestionnaire de périphériques et que les pilotes sont à jour.\n",
    "Étape 7 : Si l'ordinateur dispose d'une connexion Wi-Fi active, désactivez-la pour éviter tout conflit avec la connexion Ethernet.\n",
    "Étape 8 : Assurez-vous que le routeur/modem est connecté à Internet et qu'aucun problème n'est signalé par le fournisseur d'accès à Internet.\n",
    "Étape 9 : Testez la connexion Ethernet sur un autre appareil pour vérifier si le problème provient du matériel de l'ordinateur ou de la connexion réseau.\n",
    "Étape 10 : Si la connexion reste inactive, essayez de réinitialiser les paramètres réseau de l'ordinateur ou de réinitialiser le routeur aux paramètres d'usine.\n"
    ],
     "ordinateur lent avec des popups publicitaires": [
    "Étape 1 : Vérifiez la présence de logiciels publicitaires ou malveillants en utilisant un programme antivirus ou antimalware comme Malwarebytes ou Windows Defender.\n",
    "Étape 2 : Désinstallez les programmes ou extensions de navigateur inconnus ou suspectés d'être à l'origine des publicités (accédez à 'Panneau de configuration' -> 'Programmes' pour désinstaller).\n",
    "Étape 3 : Supprimez les extensions de navigateur indésirables qui pourraient être responsables des popups (allez dans les paramètres du navigateur et supprimez les extensions non reconnues).\n",
    "Étape 4 : Effectuez un nettoyage de disque pour supprimer les fichiers temporaires et inutiles qui ralentissent l'ordinateur. Utilisez l'outil 'Nettoyage de disque' de Windows ou CCleaner.\n",
    "Étape 5 : Vérifiez les programmes qui démarrent automatiquement avec l'ordinateur et désactivez ceux qui ne sont pas nécessaires (allez dans le Gestionnaire des tâches -> onglet 'Démarrage').\n",
    "Étape 6 : Mettez à jour tous les logiciels, y compris les navigateurs web et les plugins (comme Flash ou Java), car des versions obsolètes peuvent exposer l'ordinateur à des publicités ou des vulnérabilités.\n",
    "Étape 7 : Utilisez un bloqueur de publicités dans votre navigateur, comme AdBlock ou uBlock Origin, pour empêcher les popups publicitaires d'apparaître.\n",
    "Étape 8 : Redémarrez l'ordinateur et vérifiez si le problème persiste après les étapes ci-dessus.\n",
    "Étape 9 : Si le problème persiste, réinitialisez les paramètres du navigateur ou envisagez de réinstaller le système d'exploitation après avoir sauvegardé vos fichiers importants.\n"
    ],
     "jeu lag": [
    "Étape 1 : Vérifiez les spécifications du jeu et comparez-les avec les performances de votre ordinateur. Si votre matériel ne correspond pas aux exigences minimales, cela peut causer des lags.\n",
    "Étape 2 : Assurez-vous que les pilotes de votre carte graphique sont à jour. Vous pouvez télécharger les derniers pilotes depuis le site Web du fabricant de votre carte graphique (NVIDIA, AMD, Intel).\n",
    "Étape 3 : Fermez toutes les applications et programmes inutiles avant de jouer. Ces programmes peuvent consommer des ressources système et réduire les performances du jeu.\n",
    "Étape 4 : Baissez les paramètres graphiques du jeu pour réduire la charge sur votre carte graphique. Réduisez la résolution, les effets graphiques et les détails.\n",
    "Étape 5 : Si vous jouez en ligne, vérifiez votre connexion Internet. Un ping élevé ou des coupures peuvent causer des lags. Utilisez un câble Ethernet plutôt qu'une connexion Wi-Fi pour améliorer la stabilité.\n",
    "Étape 6 : Vérifiez la température de votre matériel, surtout du processeur et de la carte graphique. Un refroidissement insuffisant peut entraîner des baisses de performance. Nettoyez les ventilateurs et remplacez la pâte thermique si nécessaire.\n",
    "Étape 7 : Activez le mode de performance maximale dans les paramètres d'alimentation de votre ordinateur. Cela empêchera l'ordinateur de réduire la vitesse du processeur pendant les sessions de jeu.\n",
    "Étape 8 : Désactivez les logiciels de fond qui peuvent interférer avec les performances du jeu, comme les logiciels de streaming ou de surveillance.\n",
    "Étape 9 : Si vous jouez à un jeu en ligne, assurez-vous que votre serveur ou la plateforme de jeu ne rencontre pas de problèmes de serveur.\n",
    "Étape 10 : Vérifiez l'utilisation de la carte graphique et du processeur pendant que vous jouez à l'aide d'un gestionnaire de tâches ou d'un logiciel de surveillance pour détecter toute utilisation excessive qui pourrait expliquer les lags.\n"
    ],
    "Le client mentionne qu'il n'est pas capable d'imprimer, Il aimerait imprimer dans le local 204": [
    "Élément 1 : Vérifier avec le client s'il voit l'imprimante dans la liste des imprimantes disponibles.\n",
    "Élément 2 : Vérifier avec le client la file d'attente d'impression.\n",
    "Élément 3 : Vérifier avec le client le ping vers l'imprimante (10.40.141.224).\n",
    "Élément 4 : Vérifier les paramètres de l'imprimante (10.40.141.224) avec un navigateur Web.\n",
    "Élément 5 : Vérifier avec le client les paramètres du pare-feu ou de l'antivirus.\n",
    "Hypothèse 1 : L'imprimante n'a pas été déployée correctement à partir du serveur.\n",
    "Hypothèse 2 : L'imprimante n'a pas été partagée correctement à partir du serveur.\n",
    "Hypothèse 3 : L'imprimante a été déplacée dans Active Directory.\n",
    "Hypothèse 4 : L'imprimante n'est pas associée au bon groupe de sécurité.\n",
    "Hypothèse 5 : Le pilote de l'imprimante n'est pas à jour.\n",
    "Solution : Installé l'imprimante manuellement dans les paramètres de Windows.\n",
    "Sélectionné le type d'imprimante : TCP/IP.\n",
    "Installé l'imprimante avec son adresse IP : 10.40.141.224.\n",
    "Demandé au client d'imprimer une page test.\n",
    "La page test a imprimée.\n"
    ],
    "Le client utilise Word et OneDrive version Web (Microsoft 365), Le client mentionne que Word a planté et qu'il souhait récupérer son document rapport (Version ultérieure)": [
    "Élément 1 : Vérifier avec le client les champs du document Word (Modifié, modifié par et partage).\n",
    "Élément 2 : Vérifier avec le client la corbeille primaire et la corbeille secondaire dans OneDrive.\n",
    "Élément 3 : Vérifier l'historique du document Word.\n",
    "Hypothèse 1 : Le document Word est partagé.\n",
    "Hypothèse 2 : Le document Word est effacé.\n",
    "Hypothèse 3 : Le document Word est corrompu.\n",
    "Solution : Récupérer la version 1 du fichier en appuyant sur les 3 ...\n",
    "Sélectionné l'option historique des fichiers.\n",
    "Validé avec le client et celui-ci mentionne que la version 1 est ok.\n"
    ],
    "Le client mentionne qu'il n'a pas accès à Internet, Message d'erreur : La page Web ne peut pas s'afficher. Vérifier le pare-feu ou les configurations du serveur DNS": [
    "Élément 1 : Vérifier avec le client l'adresse IP de son ordinateur (ipconfig).\n",
    "Élément 2 : Vérifier avec le client le ping vers google.com.\n",
    "Élément 3 : Vérifier avec le client le ping de mon ordinateur vers son ordinateur.\n",
    "Élément 4 : Vérifier avec le client l'Internet sur un autre appareil.\n",
    "Élément 5 : Vérifier avec le client l'Internet sur un autre navigateur Web.\n",
    "Élément 6 : Vérifier avec le client la commande PowerShell (Test-NetConnection google.com -p 443).\n",
    "Hypothèse 1 : Un logiciel a modifié ou ajouté une nouvelle règle dans le pare-feu Windows.\n",
    "Hypothèse 2 : L'administrateur du réseau a déployé de nouvelles règles HTTPS dans le pare-feu\n",
    "Solution : Commencé par désactiver le pare-feu du client afin de voir si le problème persiste.\n",
    "Donc, non, le problème est disparu avec la désactivation du pare-feu.\n",
    "Ensuite, Réactiver le pare-feu.\n",
    "Cherché et désactivé les règles entrantes et sortantes HTTPS.\n"
    ],
    "Le client mentionne que lorsqu'il ouvre son rapport.pdf, pleins de caractères bizarres s'affichent.": [
    "Élément 1 : Vérifier avec le client l'extension ou le format de fichier.\n",
    "Élément 2 : Vérifier avec le client s'il peut ouvrir son fichier avec une autre application.\n",
    "Élément 3 : Vérifier avec le client si une application peut lire des fichiers pdf est installée dans les paramètres de Windows ou dans le panneau de configuration (Adobe).\n",
    "Élément 4 : Vérifier avec le client l'association application / extension du fichier dans les paramètres de Windows (Application par défaut).\n",
    "Hypothèse 1 : L'application Adobe Reader a été désinstallée et l'application Bloc-note a été sélectionnée par défaut pour ouvrir les fichiers pdf.\n",
    "Hypothèse 2 : Un problème lors de la conversion entre le fichier original et la version finale du rapport.pdf.\n",
    "Solution : Vérifier et configurer correctement l'association de fichiers/applications.\n",
    "Dans l'utilitaire Application par défaut de Windows, saisir l'extension .pdf et remarqué si les pdf étaient ouvert avec le bloc note.\n",
    "Remplacé le bloc note par Microsoft Edge.\n",
    "Le client confirme que le problème est réglé.\n"
    ],
    "Le client mentionne qu'il n'a pas accès à Internet, Message d'erreur : La page Web ne peut pas s'afficher. Vérifier le pare-feu ou les configurations du serveur DNS.": [
    "Élément 1 : Vérifier avec le client l'adresse IP de son ordinateur (ipconfig).\n",
    "Élément 2 : Vérifier avec le client le ping vers google.com.\n",
    "Élément 3 : Vérifier avec le client le ping de mon ordinateur vers son ordinateur.\n",
    "Élément 4 : Vérifier avec le client l'Internet sur un autre appareil.\n",
    "Élément 5 : Vérifier avec le client l'Internet sur un autre navigateur Web.\n",
    "Élément 6 : Vérifier avec le client la commande PowerShell (Test-NetConnection google.com -p 443).\n",
    "Hypothèse 1 : Un serveur Web (IIS ou Apache) a été installé dans l'ordinateur du client.\n",
    "Hypothèse 2 : Le serveur DHCP n'a pas été configuré correctement (Serveur DNS préféré).\n",
    "Solution : Dans Windows 11, modifié l'adresse IP du serveur DNS préféré.\n",
    "Il était à 127.0.0.1.\n",
    "Remplacé cette adresse par une adresse DHCP.\n",
    "Validé avec le client et l'Internet est fonctionnel.\n"
    ],
    "Le client mentionne qu'il n'est pas capable de se connecter sur son compte clients, Le client ne se souvient plus de son mot de passe.": [
    "Élément 1 : Vérifier avec le client s'il utilise le bon compte.\n",
    "Élément 2 : Vérifier avec le client s'il saisie son mot de passe correctement.\n",
    "Élément 3 : Vérifier avec le client s'il utilise la bonne méthode d'entrée (clavier).\n",
    "Hypothèse 1 : Le compte du client est désactivé.\n",
    "Hypothèse 2 : L'administrateur du domaine ou de l'ordinateur a modifié le mot de passe du client\n",
    "Solution : Se connecté sur le compte Techs.\n",
    "Réinitialiser le mot de passe du client.\n",
    "Validé avec le client. Celui-ci peut se connecter à son compte clients.\n"
    ],
    "Le client mentionne qu'avant, il pouvait accéder au NAS, De plus, avant il pouvait y accéder avec un raccourci.": [
    "Élément 1 : Vérifier avec le client le ping vers le serveur NAS (10.40.210.14).Élément 1 : Vérifier avec le client le ping vers le serveur NAS (10.40.210.14).\n",
    "Élément 2 : Vérifier avec le client l'accès au NAS en utilisant le raccourci clavier WIN+R.\n",
    "Hypothèse 1 : L'ancien raccourci a été effacé.\n",
    "Hypothèse 2 : Le serveur NAS est en panne.\n",
    "Solution : Créé un raccourci sur le bureau vers \\10.40.210.14.\n",
    "Validé avec le client. Celui-ci confirme qu'il peut accéder au NAS.\n"
    ],
    "Le client mentionne qu'il n'est pas capable de se connecter, Le message d'erreur dit : Le nom d'utilisateur ou le mot de passe est incorrect.": [
    "Élément 1 : Vérifier avec le client s'il saisie correctement son mot de passe.\n",
    "Élément 2 : Vérifier avec le client s'il utilise la bonne méthode d'entrée (Clavier).\n",
    "Hypothèse 1 : Le mot de passe n'a pas été saisi correctement.\n",
    "Hypothèse 2 : Pas la bonne méthode d'entrée (Clavier).\n",
    "Solution : Réinitialiser le mot de passe du client dans AD.\n",
    "Validé avec le client. Celui-ci est capable de se connecter au domaine.\n"
    ],
    "Le client mentionne qu'il ne trouve pas son fichier évaluation.txt, Le client mentionne qu'il utilise l'application bloc note, Le client mentionne qu'il ne se souvient pas de l'endroit ou le fichier est sauvegardé.": [
    "Élément 1 : Rechercher les fichiers *.txt dans la barre de recherche de l'explorateur de fichiers.\n",
    "Élément 2 : Vérifier si le fichier est caché.\n",
    "Hypothèse 1 : Le fichier est caché.\n",
    "Hypothèse 2 : Le fichier est effacé.\n"
    "Solution : Aller dans l'application Options d'indexation de Windows.\n",
    "Cliqué sur le bouton avancé.\n",
    "Cliqué sur l'onglet Types de fichiers.\n",
    "Activé les fichiers .txt.\n"
    ],
    "Le client mentionne qu'il a partagé un document Word avec OneDrive, Le client mentionne qu'il n'aurait pas dû partager le document et demande d'arrêter le partage.": [
    "Élément 1 : Vérifier et valider si le fichier est vraiment partagé.\n",
    "Élément 2 : Vérifier avec quelle version de OneDrive : Version Web ou l'application.\n",
    "Hypothèse 1 : Erreur de partage.\n",
    "Hypothèse 2 : Peut avoir partagé son document à partir de l'application.\n",
    "Solution : Dans la version Web, cliqué sur les 3 ...\n",
    "Sélectionner gérer l'accès.\n",
    "Ensuite, arrêté le partage.\n",
    "Vérifié les liens pour être certain qu'il n'y avait pas de lien de partage.\n"
    ],
    "Le client mentionne que lorsqu'il sauvegarde un document Word (Application), il y a un message d'erreur, Word tente de convertir son document en format texte brute.": [
    "Élément 1 : Vérifier lors de la sauvegarde, si le fichier est sauvegardé en format txt.\n",
    "Élément 2 : Vérifier les paramètres dans les options de Word.\n",
    "Hypothèse 1 : Mauvaise configuration dans les paramètres de Word.\n",
    "Hypothèse 2 : Mauvaise configuration dans une GPO.\n",
    "Solution : Modifié la configuration des enregistrement dans Word.\n",
    "Options\Enregistrement\Fichiers par défaut .txt vers docx.\n"
    ],
    "Le client mentionne qu'il aimerait imprimer dans le local 104, Cause : A dû travailler à un autre bureau. Ce bureau est proche du local 104.": [
    "Élément 1 : Ping vers l'imprimante du local 104 (10.40.141.222).\n",
    "Élément 2 : Vérifier dans les paramètres de Windows, si l'imprimante n'est pas déjà installée.\n",
    "Solution : Installé l'imprimante manuellement.\n",
    "TCP/IP et l'adresse IP est 10.40.141.222.\n",
    "Demandé au client d'imprimer une page test.\n",
    "La page test a imprimée.\n"
    ],
    "Le client mentionne que le format de papier n'est pas le bon, Il veut aussi imprimer recto-verso.": [
    "Élément 1 : Vérifier si l'imprimante est affichée dans la liste des imprimantes installées sur le poste du client.\n",
    "Élément 2 : Vérifier les préférences d'impression sur le poste du client.\n",
    "Hypothèse 1 : Mauvaise configuration des paramètres d'impression lors du déploiement d'imprimante.\n",
    "Hypothèse 2 : Le client a peut être déjà utilisé ces paramètres et juste oublier de les remettre.\n",
    "Solution : Accéder aux préférences d'impression de l'imprimante du local 202.\n",
    "Modifié le format de papier de A5 à 8.5 x 11.\n",
    "Modifié le type d'impression en recto-verso.\n",
    "Demandé au client d'imprimer une page test.\n",
    "La page test à réussie.\n"
    ],
    "Le client mentionne qu'une notification à apparue : Windows Defender à détecté une menace, il dit avoir téléchargé Microsoft Edge et lorsqu'il démarre l'installation, une tête de mort apparaît et que son ordinateur est infecté par un virus.": [
    "Élément 1 : Vérifier l'historique de protection dans Windows Defender.\n",
    "Élément 2 : Vérifier si la protection en temps réel est activée.\n",
    "Élément 3 : Vérifier le dossier de téléchargement.\n",
    "Élément 4 : Vérifier les fichiers marqués.\n",
    "Hypothèse 1 : Le fichier d'installation de Microsoft Edge n'a pas été téléchargé d'une source sûre.\n",
    "Hypothèse 2 : Certaines configurations de Windows Defender n'ont pas été activées ou n'ont pas été configurées correctement\n",
    "Solution : Affiché les fichiers masqués dans l'explorateur de fichiers.\n",
    "Éffacé le raccourci et le fichier *.bat : Edge version malveillante.\n",
    "Éffectué une analyse complète avec Windows Defender.\n",
    "Vérifié les paramètres de base : Protection en temps réel, protection applications...\n",
    "Recommandé et démontré à l'utilisateur de télécharger des installateurs d'une source sûre comme sur le site de Microsoft, Google, ou Firefox.\n"
    ],
    "Le client mentionne utiliser Outlook version Web, Le client mentionne qu'il aimerait utiliser Outlook version Web en anglais.": [
    "Élément 1 : Vérifier les paramètres de langue dans Outlook version Web.\n",
    "Élément 2 : Vérifier les paramètres de langue dans son Navigateur Web.\n",
    "Hypothèse 1 : L'administrateur des courriels à sélectionné la langue française et celle-ci est déployée dans toutes les configurations des usagers.\n",
    "Hypothèse 2 : La langue dans Outlook version Web utilise la langue sélectionnée ou la langue par défaut dans le navigateur Web du client.\n",
    "Solution : Sélectionné la langue anglaise dans les paramètres Outlook.\n",
    "Confirmer avec le client que tout est ok.\n"
    ]
}

# Dictionnaire pour les problèmes normalisés
normalized_troubleshooting_guide = {normalize_keyword(k): v for k, v in troubleshooting_guide.items()}

# Fonction pour afficher les étapes de dépannage pour un problème sélectionné
def display_troubleshooting_steps():
    selected_problem = problem_var.get()
    normalized_problem = normalize_keyword(selected_problem)
    steps = normalized_troubleshooting_guide.get(normalized_problem)
    
    if steps:
        # Afficher les étapes dans la zone de texte et ajuster la hauteur
        troubleshooting_text.config(state=tk.NORMAL)
        troubleshooting_text.delete(1.0, tk.END)
        troubleshooting_text.insert(tk.END, '\n'.join(steps))
        troubleshooting_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Erreur", "Problème non trouvé.")

# Interface graphique
root = tk.Tk()
root.title("Guide de Dépannage")
root.geometry("1440x900")  # Largeur et hauteur de la fenêtre

# Etiquette et menu déroulant pour sélectionner un problème
problem_label = tk.Label(root, text="Sélectionnez un problème:", font=("Arial", 12))
problem_label.pack(pady=15)

problem_var = tk.StringVar()
problem_menu = ttk.Combobox(root, textvariable=problem_var, font=("Arial", 12), width=140)
problem_menu['values'] = list(troubleshooting_guide.keys())
problem_menu.pack(pady=15)

# Ouvrir la liste déroulante lorsqu'on clique dans la barre de recherche
problem_menu.bind("<Button-1>", lambda event: problem_menu.event_generate("<Down>"))

# Bouton pour afficher les étapes de dépannage
troubleshoot_button = tk.Button(root, text="Afficher les étapes de dépannage", command=display_troubleshooting_steps, font=("Arial", 12))
troubleshoot_button.pack(pady=15)

# Associer l'appui sur "Entrée" au clic sur le bouton
problem_menu.bind("<Return>", lambda event: troubleshoot_button.invoke())

# Zone de texte pour afficher les étapes de dépannage, désactivée pour éviter les modifications
troubleshooting_text = tk.Text(root, wrap=tk.WORD, width=125, height=75, font=("Arial", 12))
troubleshooting_text.pack(pady=10)
troubleshooting_text.config(state=tk.DISABLED)

root.mainloop()