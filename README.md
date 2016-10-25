**Translate-Skill**
===================


An skill to use with Mycroft which allow to translate phrases into other languages

----------


Installation
-------------------

Download mtranslate and install:

    wget https://pypi.python.org/packages/b6/48/aae48178d4205eeda8186a402827b7fb113e05958b14d697b17a33752715/mtranslate-1.4.tar.gz
    tar -xvzf mtranslate-1.4.tar.gz
    cd mtranslate-1.4
 
    sudo /home/pi/.virtualenvs/mycroft/local/bin/python setup.py install
	

> **Note:**
> - /home/pi or your directory containing  /.virtualenvs/mycroft/local/bin/ 


Now go to Mycroft third party skill directory

    cd  /opt/mycroft/third_party/

    git clone  https://github.com/jcasoft/Translate-Skill.git mycroft-translate-skill




Restart Skills

    ./start.sh skills

----------


Features
--------------------

Currently this skill can do the following things (with some variation):

- translate to spanish good night
- say in french good morning
- translate good morning my dear friends to italian
- translate good morning my dear friends to spanish
- translate good morning my dear friends to french
- translate good morning my dear friends to duth
- translate good morning my dear friends to german
- translate good morning my dear friends to portuguese


> **Note:**

> - You can toggle language key word with:
> - spanish, italian, french, dutch, german, portuguese



**Enjoy !**
--------