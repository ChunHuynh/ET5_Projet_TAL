# TP2 - Analyse linguistique avec le framework NLTK

## I - Installation de la plateforme d’analyse linguistique NLTK

### 1. Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK
#### 1.1. Ecrire un programme Python utilisant le package pos_tag pour désambiguïser morphosyntaxiquement le texte du fichier wsj_0010_sample.txt.
```bash
python3 src/nltk_pos_tagger.py data/wsj_0010_sample.txt data/wsj_0010_sample.txt.pos.nltk
```

#### 1.2. Utiliser le programme Python « evaluate.py » pour évaluer l’analyseur morpho-syntaxique de la plateforme NLTK.
On formatte d'abord le fichier référence en format ligne:
```bash
python3 src/column_to_line.py data/wsj_0010_sample.pos.ref data/wsj_0010_sample.pos.ref.line
```
On peut ensuite évaluer l'analyseur NLTK au fichier référence:
```bash
python src/evaluate.py data/wsj_0010_sample.txt.pos.nltk  data/wsj_0010_sample.pos.ref.line
```
Résultat:  
Word precision: 0.990909090909  
Word recall: 0.990909090909  
Tag precision: 0.936363636364  
Tag recall: 0.936363636364  
Word F-measure: 0.990909090909  
Tag F-measure: 0.936363636364  

#### 1.3. Evaluation à l’aide des étiquettes universelles
##### a. Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers « wsj_0010_sample.txt.pos.nltk » et « wsj_0010_sample.txt.pos.ref » par les étiquettes universelles en utilisant la table de correspondance « POSTags_PTB_Universal.txt ».
```bash
python3 src/PTB_to_universal.py data/wsj_0010_sample.txt.pos.nltk data/wsj_0010_sample.txt.pos.univ.nltk data/POSTags_PTB_Universal_Linux.txt
```
```bash
python3 src/PTB_to_universal.py data/wsj_0010_sample.pos.ref.line data/wsj_0010_sample.txt.pos.univ.ref data/POSTags_PTB_Universal_Linux.txt
```

##### b. Utiliser le programme Python « evaluate.py » pour évaluer l’analyseur morphosyntaxique de la plateforme NLTK selon les étiquettes universelles.
```bash
python src/evaluate.py data/wsj_0010_sample.txt.pos.univ.nltk data/wsj_0010_sample.txt.pos.univ.ref
```
Résultat:  
Word precision: 0.990909090909  
Word recall: 0.990909090909  
Tag precision: 0.954545454545  
Tag recall: 0.954545454545  
Word F-measure: 0.990909090909  
Tag F-measure: 0.954545454545  

##### c. Quelles conclusions peut-on avoir à partir de ces deux évaluations ?
On peut dire que l'analyseur de NLTK est assez précis sur l'analyse morpho-syntaxique. Le passage aux étiquettes universelles montre bien que NLTK a des étiquettes propres à lui-même mais qu'il arrive à bien faire correspondre la nature du mot.

### 2. Utilisation de la plateforme NLTK pour l’analyse syntaxique

#### 2.1. Ecrire un programme Python utilisant le package parse pour extraire les mots composés (chunks) ayant la structure syntaxique Déterminant-Adjectif-Nom (grammar = "Compound: {\<DT>?\<JJ>*\<NN>}") présents dans le texte du fichier wsj_0010_sample.txt.  
#### 2.2. Généraliser le programme Python précédent pour extraire les mots composés (chunks) compatibles avec les structures syntaxiques ci-dessous:
Adjectif-Nom  
Nom-Nom  
Adjectif-Nom-Nom  
Adjectif-Adjectif-Nom  

On utilise un fichier déclaratif nommé `grammars.txt` qui contiendra ces structures syntaxiques:  
```bash
python3 src/nltk_parser.py data/wsj_0010_sample.txt data/wsj_0010_sample.txt.chk.nltk data/grammars.txt
```

### 3. Utilisation de la plateforme NLTK pour l’extraction d’entités nommées

#### 3.1.Ecrire un programme Python utilisant le package ne_chunk pour extraire les entités nommées présentes dans le texte du fichier wsj_0010_sample.txt.
```bash
python3 src/nltk_ne_recognizer.py data/wsj_0010_sample.txt data/wsj_0010_sample.txt.ne.nltk
```

#### 3.2. Ecrire un programme Python permettant de convertir les étiquettes des entités nommées produites. (voir sujet de TP pour plus d'info)
```bash
python3 src/nltk_to_std.py data/wsj_0010_sample.txt.ne.nltk data/wsj_0010_sample.txt.std.ne.nltk data/labels_NLTK_Standard.txt
```



