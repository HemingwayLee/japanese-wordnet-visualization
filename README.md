# japanese-wordnet-visualization
* This project visualizes the [Japanese Wordnet](https://bond-lab.github.io/wnja/) (日本語ワードネット) with web application built by Django
* The demo page is [here](http://35.78.115.229:8000/)

## How to run this project
### Locally
* git clone this project
* download Japanese Wordnet sqlite3 database from [official webstie](https://bond-lab.github.io/wnja/jpn/downloads.html)
* uncompress sqlite3 database and move the file into `japanese-wordnet-visualization/jpwordnet` folder like below:
```
~/wordnet/japanese-wordnet-visualization/jpwordnet$ ls
jpwordnet  manage.py  myapp  wnjpn.db
```
* create a `.env` file in `~/japanese-wordnet-visualization/jpwordnet/jpwordnet/` folder, and put the following content into `.env` file
```
WEBAPP_ADDRESS=127.0.0.1
```

* run the following commands to start the web application
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt 
cd jpwordnet/
python3 manage.py migrate
python3 manage.py runserver
```

* Access the web application `http://127.0.0.1:8000/`
  * Type Japanese word in the textbox
  * You can click red dots on the visualization if you want to search for the words
![jp_wordnet_demo](https://github.com/HemingwayLee/japanese-wordnet-visualization/blob/master/img/demo.png?raw=true)

## Use command-line `sqlite3` to see the data
### Open `wnjpn.db` database
```
sqlite3 wnjpn.db 
```

### Explore the `wnjpn.db` database
* show the database
```
sqlite> .database
main: /path/to/project/japanese-wordnet-visualization/jpwordnet/wnjpn.db
```

* show all tables
```
sqlite> .table
ancestor    pos_def     synlink     synset_def  variant     xlink     
link_def    sense       synset      synset_ex   word    
```

* show rows in a table 
```
sqlite> select * from word limit 3;
1|eng|expletive||n
2|eng|measles||n
3|eng|contras||n
sqlite> select * from word where lang='jpn' limit 3;
155288|jpn|頭金||n
155289|jpn|どうにかこうにか||r
155290|jpn|大砲||n
```

* show the table schema
```
sqlite> .schema word
CREATE TABLE word (wordid integer primary key,
                          lang text,
                          lemma text,
                          pron text,
                          pos text);
CREATE INDEX word_id_idx ON word (wordid);
CREATE INDEX word_lemma_idx ON word (lemma);  
sqlite> .exit
```

## Use [sqleton](https://github.com/inukshuk/sqleton) to see the table schema
```
npm install -g sqleton
sqleton -o wnjpn.png wnjpn.db 
```

![wnjpn_diagram](https://raw.githubusercontent.com/HemingwayLee/japanese-wordnet-visualization/master/img/wnjpn.png)

