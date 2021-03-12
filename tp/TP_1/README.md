# TP1 Analyse linguistique avec la plateforme Stanford CoreNLP

## I - Installation et évaluation de l’outil de désambiguïsation morphosyntaxique de l’université de Stanford

### 1. Installation
(voir le sujet du TP pour les instructions sur l'installation et l'utilisation de Stanford POSTagger)
### 2. Evaluation
#### a. Lancer le POS tagger sur le fichier « wsj_0010_sample.txt ».
```bash
./stanford-postagger.sh models/english-left3words-distsim.tagger ../data/wsj_0010_sample.txt > ../data/wsj_0010_sample.txt.pos.stanford
```

#### b. Ecrire un programme Python qui permet de convertir le fichier de référence wsj_0010_sample.pos.ref au format de la sortie du Stanford POS tagger.
```bash
python3 src/formatStanford.py data/wsj_0010_sample.pos.ref data/wsj_0010_sample.pos.stanford.ref
```

#### c. Calculer la précision de ce POS tagger en utilisant les étiquettes PTB.
```bash
python src/evaluate.py data/wsj_0010_sample.txt.pos.stanford data/wsj_0010_sample.pos.stanford.ref
```
Résultat:  
Word precision: 1.0  
Word recall: 1.0  
Tag precision: 0.918181818182  
Tag recall: 0.918181818182  
Word F-measure: 1.0  
Tag F-measure: 0.918181818182  

#### d. Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers wsj_0010_sample.txt.pos.stanford et wsj_0010_sample.pos.stanford.ref par les étiquettes universelles en utilisant la table de correspondance « POSTags_PTB_Universal.txt ».
```bash
python3 src/PTB_universal.py data/wsj_0010_sample.txt.pos.stanford data/wsj_0010_sample.txt.pos.univ.stanford data/POSTags_PTB_Universal_Linux.txt
```
```bash
python3 src/PTB_universal.py data/wsj_0010_sample.pos.stanford.ref data/wsj_0010_sample.txt.pos.univ.ref data/POSTags_PTB_Universal_Linux.txt
```

#### e. Calculer la précision de ce POS tagger en utilisant les étiquettes universelles.
```bash
python src/evaluate.py data/wsj_0010_sample.txt.pos.univ.stanford data/wsj_0010_sample.txt.pos.univ.ref
```
Résultat:  
Word precision: 1.0  
Word recall: 1.0  
Tag precision: 0.927272727273  
Tag recall: 0.927272727273  
Word F-measure: 1.0  
Tag F-measure: 0.927272727273

#### d. Quelles conclusions peut-on avoir à partir de ces deux évaluations ?
On peut remarquer que même en convertissant les etiquettes Penn TreeBank en etiquettes universelles il exite en effet des differences de tag sur certains mots.  
On aurait pu croire que la difference du tag F-measure est a cause de la difference des tags entre stanford et reférence mais la difference vient surtout d'une interpretation differente de la nature des mots par les tagger.

## II - Installation et utilisation de l’outil de reconnaissance d’entités nommées de l’université de Stanford

### 1. Installation
(voir le sujet du TP pour les instructions sur l'installation et l'utilisation de Stanford NER)
### 2. Extraction d’entités nommées
A partir du résultat de l’outil de reconnaissance des entités nommées « wsj_0010_sample.txt.ner.stanford », écrire un programme Python permettant de représenter les entités nommées sous le format suivant:  
Entité nommée | Type | Nombre d’occurrences | Proportion dans le texte (%)  
--- | --- | --- | ---
Jonh | PERSON | 1 | 1 (1/1)  

On lance le NER de Stanford sur le fichier de référence:
```bash
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../data/ner/wsj_0010_sample.txt > ../data/ner/wsj_0010_sample.txt.ner.stanford
```
```bash
python3 src/formatNE.py data/ner/wsj_0010_sample.txt.ner.stanford data/ner/wsj_0010_sample.txt.ner.stanford.format
```

