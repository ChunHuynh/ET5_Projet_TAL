# Projet TAL

## Notes
Les commandes suivantes sont à exécuter à la racine du projet ```../ET5_Projet_TAL/```

Les fichiers nécessaires sont passés en paramètre de la commande d'exécution du script python. Le premier paramètre est en général le fichier dont on lit les données, le deuxième le fichier résultat à créer après traitement des données du premier fichier.

Certains fichiers qui excèdent 50 MB n'ont pas pu être ajoutés. Ces fichiers concernent les dossiers stanford-ner et stanford-postagger.<br>
Voici les liens pour télécharger de nouveau et les remplacer:<br>
[Stanford POS Tagger](https://nlp.stanford.edu/software/tagger.shtml#Download)<br>
[Stanford NER](https://nlp.stanford.edu/software/CRF-NER.html#Download)


## I - Evaluation de l’analyse morpho-syntaxique
### 1. Utiliser le corpus annoté « pos_reference.txt.lima » pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier « pos_test.txt ».
```bash
python3 src/extractCorpus.py data/pos_reference.txt.lima data/pos_test.txt
```

### 2. Convertir les tags du corpus annoté « pos_reference.txt.lima » en tags universels et sauvegarder le résultat dans le fichier « pos_reference.txt.univ ».
Nous avons d'abord besoin de convertir les tags lima en tags Penn Tree Bank:<br>
```bash 
python3 src/translateLabel.py data/pos_reference.txt.lima data/pos_reference.txt.ptb data/POSTags_LIMA_PTB_Linux.txt
```

Ensuite on peut convertir les tags PTB en tags universels:<br>
```bash
python3 src/translateLabel.py data/pos_reference.txt.ptb data/pos_reference.txt.univ data/POSTags_PTB_Universal_Linux.txt
```

### 3. Lancer les deux POS taggers sur le fichier « pos_test.txt ».
#### Stanford:

On lance le POS tagger de Stanford:<br>
```bash
cd stanford-postagger-full-2020-11-17
```
```bash
./stanford-postagger.sh models/english-left3words-distsim.tagger ../data/pos_test.txt > ../data/temp_pos.txt.stanford
```

On formatte le résultat obtenu en 2 colonnes:<br>
```bash
python3 src/formatStanford.py data/temp_pos.txt.stanford data/pos_test.txt.pos.stanford
```

#### nltk:
On lance le POS tagger de nltk<br>
```bash
python3 src/nltkPOSTagger.py data/pos_test.txt data/pos_test.txt.pos.nltk
```

### 4. Convertir les résultats des deux POS taggers en utilisant les étiquettes universelles.

#### Stanford:
```bash
python3 src/labelTranslatePOS.py data/pos_test.txt.pos.stanford data/pos_test.txt.pos.stanford.univ data/POSTags_PTB_Universal_Linux.txt
```

#### nltk:
```bash
python3 src/labelTranslatePOS.py data/pos_test.txt.pos.nltk data/pos_test.txt.pos.nltk.univ data/POSTags_PTB_Universal_Linux.txt
```

### 5. Lancer l’évaluation des deux POS taggers
#### Stanford:
```bash
python src/evaluate.py data/pos_test.txt.pos.stanford.univ data/pos_reference.txt.univ
```

#### nltk:
```bash
python src/evaluate.py data/pos_test.txt.pos.nltk.univ data/pos_reference.txt.univ
```

Pour améliorer la qualité de l'évaluation, on peut convertir le format colonne en format ligne des fichiers à évaluer:<br>
```bash
python3 src/column_to_line.py data/pos_test.txt.pos.stanford.univ data/pos_test.txt.pos.stanford.univ.line
```
```bash
python3 src/column_to_line.py data/pos_test.txt.pos.nltk.univ data/pos_test.txt.pos.nltk.univ.line
```
```bash
python3 src/column_to_line.py data/pos_reference.txt.univ data/pos_reference.txt.univ.line
```

On re-évalue avec le format ligne:
#### Stanford:
```bash
python src/evaluate.py data/pos_test.txt.pos.stanford.univ.line data/pos_reference.txt.univ.line
```

#### nltk:
```bash
python src/evaluate.py data/pos_test.txt.pos.nltk.univ.line data/pos_reference.txt.univ.line
```

## II - Evaluation de la reconnaissance d’entités nommées
### 1. Utiliser le corpus annoté « ne_reference.txt.conll » pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier « ne_test.txt ».
```bash
python3 src/extractCorpus.py data/ne_reference.txt.conll_update.txt data/ne_test.txt
```

### 2. Lancer les deux NE recognizers sur le fichier « ne_test.txt ».

#### Stanford:
On lance le NER de Stanford:<br>
```bash
cd stanford-ner-2020-11-17
```

```bash
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../data/ne/ne_test.txt > ../data/ne/ne_test.txt.ne.stanford.temp
```  

On formatte en colonne:<br>
```bash
python3 src/format_NE.py data/ne/ne_test.txt.ne.stanford.temp data/ne/ne_test.txt.ne.stanford
```

#### nltk:
```bash
python3 src/nltk_ne_recognizer.py data/ne/ne_test.txt data/ne/ne_test.txt.ne.nltk
```  

### 3. Convertir les résultats des deux NE recognizers en utilisant les étiquettes CoNLL-2003.

#### Stanford:
```bash
python3 src/ne_to_conll.py data/ne/ne_test.txt.ne.stanford data/ne/ne_test.txt.ne.stanford.conll
```

#### nltk:
```bash
python3 src/ne_to_conll.py data/ne/ne_test.txt.ne.nltk data/ne/ne_test.txt.ne.nltk.conll
```
 
### 4. Lancer l’évaluation des deux NE recognizers.

#### Stanford:
```bash
python src/evaluate.py data/ne/ne_test.txt.ne.stanford.conll data/ne/ne_reference.txt.conll
```

#### nltk:
```bash
python src/evaluate.py data/ne/ne_test.txt.ne.nltk.conll data/ne/ne_reference.txt.conll
```

On peut améliorer l'évaluation en formattant en ligne:  
```bash
python3 src/column_to_line.py data/ne/ne_test.txt.ne.stanford.conll data/ne/ne_test.txt.ne.stanford.conll.line
```  
```bash
python3 src/column_to_line.py data/ne/ne_test.txt.ne.nltk.conll data/ne/ne_test.txt.ne.nltk.conll.line
```  
```bash
python3 src/column_to_line.py data/ne/ne_reference.txt.conll_update.txt data/ne/ne_reference.txt.conll.line
```

On peut ensuite enlever les lignes vides du fichier de référence:<br>
```bash
python3 src/noEmptyLine.py data/ne/ne_reference.txt.conll.line data/ne/ne_reference.txt.conll.line.noblank
```

On re-évalue avec le format ligne:

#### Stanford:
```bash
python src/evaluate.py data/ne/ne_test.txt.ne.stanford.conll.line data/ne/ne_reference.txt.conll.line.noblank
```

#### nltk:
```bash
python src/evaluate.py data/ne/ne_test.txt.ne.nltk.conll.line data/ne/ne_reference.txt.conll.line.noblank
```
