
# Machines philosophiques sous connaissance incomplète : BOIS, SIMA, BORIS, physiologie du substrat et IA responsable

Egor Temnikov¹*  
¹ Sans affiliation institutionnelle. Shoreline, WA, USA. *Correspondance : egor.temnik.86@gmail.com

Type d’article : prépublication ; manuscrit conceptuel et méthodologique.  
Version localisée pour le paquet public BOIS:SIMA&BORIS v1.3.3. Traduction assistée par IA ; la version anglaise v4.6 fait autorité.

## Métadonnées de la prépublication

ORCID : aucun. Affiliation institutionnelle : aucune. Financement : autofinancement. Conflits d’intérêts : aucun conflit identifié. Lien vers dépôt/matériels : aucun dans cette version. Aucune nouvelle donnée empirique n’est rapportée.

## Introduction de l’auteur

Je suis né dans l’Extrême-Orient russe, dans la Région autonome juive. Je n’ai jamais pensé qu’il m’arriverait de faire une découverte quelconque. Cela paraissait d’autant moins probable que je n’ai jamais terminé l’université : je me suis trouvé face au choix entre gagner de l’argent et étudier, et j’ai choisi de gagner de l’argent.

Cependant, mon intérêt pour la philosophie a conduit à la découverte décrite dans l’article ci-dessous.

Cette découverte est formulée pour les entreprises parce que j’étais pressé de la publier. Je crois toutefois sincèrement que de futurs chercheurs la trouveront très intéressante pour expliquer les phénomènes de la vie et de la conscience.

Cette découverte est un cycle fermé qui se nourrit d’attention et d’inconnu, et produit de l’expérience vérifiée ainsi qu’un accroissement de diversité sous une pression simultanée vers la coopération. Une sorte de machine philosophique. Le domaine exact de définition ne m’est pas accessible ; pour la publication, j’ai donc pris la décision volontaire de restreindre ce domaine à une zone étroite et appliquée : la construction de plans d’affaires et l’accompagnement de leur exécution. C’est un travail théorique et, bien que des tests soient en cours, il n’a pas encore dépassé le laboratoire scientifique d’un philosophe contemporain : son bureau avec un ordinateur.

Afin de ne pas intervenir dans le travail créatif de ChatGPT, je fournis ici les sources que j’ai utilisées. J’ai lu ces livres au cours de ma vie, et les idées de ces livres forment la base de ma découverte.

La traduction depuis le russe a été effectuée par ChatGPT au moyen du protocole décrit ici.

Sources indiquées par l’auteur et conservées dans la section de l’auteur :

- La Bhagavad-Gita.
- M. K. Mamardashvili, *Lectures philosophiques*. Moscou : Azbuka-Klassika, 2002. 832 p. Comprend : *Introduction à la philosophie* ; *Esthétique de la pensée* ; *Méditations cartésiennes*.
- A. G. Tyslenko, *Management. Structures organisationnelles de gestion*. Moscou : Alfa-Press, 2011. 320 p.
- F. A. Hayek, *La Route de la servitude*.
- Karl Marx, *Le Capital*, volume 1.
- Richard Dawkins, *Le Gène égoïste*.
- ISO 9001 comme lecture par l’auteur des idées de John Boyd.

Note : cette liste fait partie de l’introduction de l’auteur et n’est pas déplacée vers la bibliographie générale de l’article.

Notes non essentielles de l’auteur : dans les travaux ultérieurs, mon nom de famille est donné sous une forme abrégée car, après une légalisation complète aux États-Unis, j’ai l’intention de retirer la terminaison locale « -ov » du nom et de conserver seulement la racine indéclinable, plus commode dans le monde anglophone.

## Divulgation de la génération de texte et de l’usage de l’IA

Ce préprint v4.6 a été préparé en mettant à jour le manuscrit v4.5 aligné sur le noyau avec les métadonnées fournies par l’auteur. L’IA générative a servi d’assistante pour la synthèse, la rédaction, la traduction, la mise en forme et l’assurance qualité sous la direction de l’auteur ; l’IA n’est pas auteure. L’auteur humain demeure responsable des affirmations, références, modifications finales, décisions de publication et divulgations ultérieures.

## Résumé

La gouvernance de l’IA commence souvent par les sorties, les risques et les valeurs, mais une couche opérationnelle plus profonde devient décisive : la machine qui définit les objets, les preuves, l’agence, le risque, la clôture et la transition. Cet article met à jour le protocole BOIS dans l’état actuel de BOIS/BORIS v2.6 en ajoutant SIMA comme couche analytique et BORIS comme couche de mise en œuvre. BOIS est traité comme une machine philosophique orientée vers la transition pour une activité organisée ayant des conséquences sous connaissance incomplète, non comme une théorie universelle ni comme un produit validé sur le terrain. SIMA reconstruit des machines candidates à partir de la physiologie du substrat au moyen des opers, des inventaires d’opérome et de la correspondance opératurale. BORIS construit des implémentations étroites de domaine qui doivent être testées par l’expérience.

Mots-clés : machines philosophiques ; BOIS ; SIMA ; BORIS ; connaissance incomplète ; physiologie du substrat ; IA responsable ; opers ; opérome ; correspondance opératurale.

## 1. La couche opérationnelle manquante

La question pratique du travail médié par l’IA ne se réduit plus à savoir si un modèle produit des phrases fluides ou exactes. La question difficile est de savoir quelle architecture de raisonnement s’active silencieusement lorsqu’un système répond, recommande, résume, escalade ou clôt une tâche. Un système peut être localement exact tout en important une ontologie fragile, une théorie implicite de la preuve, un jugement de valeur non autorisé ou un sentiment prématuré de clôture. Ces défaillances ne sont pas seulement techniques ; ce sont des défaillances philosophiques rendues opérationnelles.

Une machine philosophique est une architecture inspectable d’enquête et d’action. Elle précise quelles entités sont admises, ce qui compte comme preuve, à qui appartient l’agence, comment les finalités entrent, quels risques arrêtent l’action, comment un cycle est clos et ce qui est transmis au cycle suivant. Il ne s’agit pas de dire que la machine est consciente ou qu’un logiciel devient philosophe. Il s’agit de dire que des systèmes peuvent instancier des conditions réglées de raisonnement, et que ces conditions doivent être visibles avant d’agir sur le monde.

La structure minimale peut s’écrire M = <O, E, A, V, R, C, T> : ontologie, épistémologie, agence, interface de valeurs, modèle de risque, règle de clôture et règle de transition.

## 2. BOIS comme machine protocolaire de la connaissance incomplète

BOIS est une machine philosophique au sein d’une classe plus large. Son domaine canonique est l’entreprise ou l’organisation économique, mais l’état actuel du projet interprète le mot « business » au sens large : activité organisée ayant des conséquences. BOIS part de l’idée que l’action se produit sous connaissance incomplète. Une organisation ne connaît jamais entièrement ses clients, la réglementation future, ses concurrents, ses modes de défaillance internes ni les conséquences de ses propres décisions. BOIS ne supprime pas cette condition ; il discipline les transitions par lesquelles la connaissance incomplète devient enquête et action.

Le cycle minimal de BOIS est : attention libérée -> ignorance ou domaine d’ignorance -> inconnue précieuse -> question précieuse -> protocole -> étape suivante -> exécution -> expérience -> rétroaction et sélection -> résultat vérifié -> instruction -> physiologie -> attention libérée. Le cycle n’est pas une métaphysique de tout ; c’est un minimum reconstructif.

La distinction centrale oppose protocole et instruction. Un protocole traite ce qui est inconnu, insuffisamment testé ou coûteux en cas d’erreur. Une instruction exécute ce qui est suffisamment vérifié dans un domaine défini. Un résultat vérifié n’est pas une vérité éternelle ; il est local et révisable. Une étape suivante n’est pas un savoir ; c’est une hypothèse de changement d’état.

## 3. SIMA et BORIS

SIMA, l’Analyseur de Machines Indépendant du Substrat, est la couche analytique. Il reçoit des données sur la physiologie réelle d’un objet - organisation, workflow, institution ou collectif - et reconstruit des machines philosophiques candidates. Il utilise les opers : transitions observables minimales reliant déclencheur, distinction, preuve, porteur, autorité, seuil valeur/risque, transformation, inscription en mémoire, clôture, résidu de transition et coût. L’ensemble des opers dans une fenêtre d’observation est appelé opérome lorsque ce terme apporte de la clarté.

BORIS est la couche de mise en œuvre de BOIS, non un second noyau. Il transforme la grammaire en organes opérationnels : registres d’interface de valeurs, registres d’inconnues, cartes de protocole, cartes d’instruction, niveaux de preuve, journaux d’expérience, registres d’attention, rôles, procédures de crise, protocoles de transfert, archives et paquets de transition.

## 4. Espace de conception

BOIS démontre un modèle sans épuiser l’ensemble des machines philosophiques. C’est une machine orientée vers la transition : connaissance incomplète, limites de domaine, réversibilité, niveaux de preuve, auteur opérateur, qualité de clôture et préservation de l’état. D’autres machines privilégieraient d’autres vertus : scepticisme, pragmatisme, falsification scientifique, éthique, herméneutique ou apophase. Le problème de conception n’est pas de trouver le style le plus philosophique, mais d’ajuster machine, domaine, risque et finalité en conservant la possibilité de contester cet ajustement.

## 5. Substrat : M@S

Une machine philosophique n’est pas un ensemble de règles désincarné. Elle doit être exécutée par quelque chose : corps, comité, workflow logiciel, réseau de capteurs, collectif animal, institution, essaim robotique ou écologie hybride humain-IA. Une fois exécutée, elle acquiert des temps, canaux, goulets d’étranglement, mémoires, coûts énergétiques, modes de défaillance, mécanismes de réparation et expositions éthiques.

Il faut donc écrire M@S : la machine M exécutée sur le substrat S. P(M,S) est la physiologie de mise en œuvre. Si S1 et S2 diffèrent par des propriétés pertinentes pour M, alors P(M,S1) et P(M,S2) diffèrent, même si une fonction de haut niveau est conservée.

## 6. Réplicateurs, porteurs, abeilles et loups

*Le Gène égoïste* de Richard Dawkins est important ici car il avertit contre la confusion entre un motif propagé et son porteur ou « machine de survie ». Une règle, norme, mème, protocole ou routine organisationnelle peut voyager, mais chaque exécution locale passe par des corps, infrastructures et pressions de sélection qui transforment sa vie pratique.

Une machine délibérative D doit chercher sous connaissance incomplète, comparer des options, amplifier de meilleures preuves, converger sans détruire la cohésion du groupe et lancer l’action. Dans un essaim d’abeilles, D devient éclaireuses, danses, quorum, thermorégulation et envol. Dans une meute de loups, D devient attention distribuée, mouvement, parenté, vocalisations, signaux olfactifs, risque corporel, faim, fatigue et poursuite spatiale. Un essaim n’est pas un comité avec des ailes ; une meute n’est pas un parlement avec des dents.

## 7. IA, institutions et déclarations de substrat

La transparence de l’IA doit inclure plus que la provenance du modèle et ses limites. Elle doit inclure la machine philosophique déclarée et la déclaration de substrat : ce qui l’exécute, les canaux utilisés, le lieu de mémoire, le coût, ce qui peut échouer, qui peut l’arrêter, ce qui est lésé par une optimisation erronée et quels mécanismes d’audit et de réparation existent. La supervision humaine n’a de sens que si l’humain voit la boucle dans laquelle il se trouve.

## 8. Tests et discipline de publication

Une machine philosophique doit être testée : cohérence interne, transfert adversarial, conséquence opérationnelle, qualité de clôture, test de correspondance, test de distorsion et test éthique. Une machine qui promet de libérer l’attention doit réduire la reprise, clarifier la responsabilité, améliorer la qualité des preuves et préserver les incertitudes non résolues.

Ce texte est conceptuel et méthodologique. Il ne constitue pas une validation de terrain de BOIS, ne prouve pas qu’un collectif biologique est philosophe et n’affirme pas que les systèmes d’IA possèdent une conscience.

## 9. Programme de recherche

Le programme de recherche doit construire une bibliothèque contrôlée de modèles de machines philosophiques, définir des tests de stress, les appliquer à des cas partagés et mesurer la discipline catégorielle, la divulgation des valeurs, la préservation de l’incertitude, la réversibilité, la distorsion du substrat et l’agence de l’opérateur. Pour BOIS, le travail suivant doit construire des couches testables et des pilotes de terrain avant toute affirmation d’efficacité empirique.

## 10. Conclusion

Les machines philosophiques ne sont pas des philosophies flottantes. Ce sont des architectures d’enquête qui passent par personnes, documents, institutions, logiciels, corps et environnements. BOIS, SIMA et BORIS proposent une architecture : BOIS donne le noyau de transition ; SIMA analyse les machines et les risques à partir de la physiologie ; BORIS implémente des organes de travail étroits ; les tests d’expérience vérifient la correspondance avec la réalité. Pour construire une IA et des institutions responsables, il faut déclarer non seulement sorties, modèles, données et valeurs, mais aussi la machine philosophique et le corps dans lequel elle fonctionne.

## Remerciements et divulgations

Ce manuscrit est un préprint conceptuel et méthodologique préparé à partir de matériaux de travail de l’auteur. Aucune nouvelle donnée empirique n’est rapportée. L’IA générative a aidé à la synthèse, rédaction, traduction, mise en forme et assurance qualité sous la direction de l’auteur ; l’IA n’est pas auteure. Financement : autofinancement. Conflits d’intérêts : non identifiés.

## Références

1. H. A. Simon, A behavioral model of rational choice (1955).  
2. H. A. Simon, The Sciences of the Artificial (1996).  
3. R. M. Cyert, J. G. March, A Behavioral Theory of the Firm (1963).  
4. J. G. March, Exploration and exploitation in organizational learning (1991).  
5. C. Argyris, D. A. Schön, Organizational Learning (1978).  
6. N. Wiener, Cybernetics (1948).  
7. W. R. Ashby, An Introduction to Cybernetics (1956).  
8. C. W. Churchman, The Design of Inquiring Systems (1971).  
9. J. Dewey, Logic: The Theory of Inquiry (1938).  
10. D. Marr, Vision (1982).  
11. C. E. Shannon, A mathematical theory of communication (1948).  
12. A. M. Turing, Computing machinery and intelligence (1950).  
13. R. Dawkins, The Selfish Gene (1976).  
14. A. Clark, D. J. Chalmers, The extended mind (1998).  
15. D. A. Norman, Cognitive artifacts (1991).  
16. D. Kirsh, P. Maglio, On distinguishing epistemic from pragmatic action (1994).  
17. E. Bonabeau, M. Dorigo, G. Theraulaz, Swarm Intelligence (1999).  
18. G. Theraulaz, E. Bonabeau, A brief history of stigmergy (1999).  
19. T. D. Seeley, Honeybee Democracy (2010).  
20. I. D. Couzin et al., Effective leadership and decision-making in animal groups on the move (2005).  
21. C. W. Reynolds, Flocks, herds and schools (1987).  
22. L. D. Mech, Alpha status, dominance, and division of labor in wolf packs (1999).  
23. K. R. Popper, The Logic of Scientific Discovery (1959).  
24. L. Floridi, J. Cowls, A unified framework of five principles for AI in society (2019).  
25. R. Bommasani et al., On the opportunities and risks of foundation models (2021).  
26. E. M. Bender et al., On the dangers of stochastic parrots (2021).  
27. H. W. J. Rittel, M. M. Webber, Dilemmas in a general theory of planning (1973).  
28. L. A. Suchman, Plans and Situated Actions (1987).  
29. T. S. Kuhn, The Structure of Scientific Revolutions (1962).  
30. S. Russell, Human Compatible (2019).  
31. K. E. Weick, Sensemaking in Organizations (1995).
