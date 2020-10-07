# MATD
#### Requirements
`pip3 install -r requirements.txt`

#### Datasets
[DNA_50MB](http://pizzachili.dcc.uchile.cl/texts/dna/dna.50MB.gz)

#### 1.CV
[DFA_match](https://github.com/pbednar96/MATD/blob/master/DFA_match.py)

>python3 DFA_match.py pattern text

example: 
`python3 DFA_match.py "ahhHooj" "ahhojdasah+5dssahhhoojjaahhhooj"`

Case insensitive pattern matching.

#### 2.CV

[Brute_force](https://github.com/pbednar96/MATD/blob/master/brute_force.py)

>python3 brute_force.py

[KMP_search](https://github.com/pbednar96/MATD/blob/master/KMP.py)

>python3 KMP.py

#### 3.CV

[BMH_search](https://github.com/pbednar96/MATD/blob/master/BMH.py)

>python3 BMH.py

[BM_search](https://github.com/pbednar96/MATD/blob/master/BM.py)

>python3 BM.py

##### Performance

![plot_img](https://github.com/pbednar96/MATD/blob/master/plots/performance_plot.png)


