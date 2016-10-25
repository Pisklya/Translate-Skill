from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3


from os.path import dirname, abspath, join
import requests
import os
import sys

from mtranslate import translate

logger = getLogger(dirname(__name__))
sys.path.append(abspath(dirname(__file__)))

ibm_username = ""
ibm_password = ""

__author__ = 'jcasoft'


class TranslateSkill(MycroftSkill):
    """
    A Skill to translate a phrase with IBM Watson TTS to speak the translation on other languages
    """


    def __init__(self):
        super(TranslateSkill, self).__init__('speech_client')

	# For better quality voices
	global ibm_username, ibm_password
	ibm_username = self.config.get('ibm_username')
	ibm_password = self.config.get('ibm_password')

	
    def initialize(self):
    	"""
	Mycroft Translate Intents
	"""
        self.load_data_files(dirname(__file__))
	self.load_regex_files(join(dirname(__file__), 'regex', 'en-us'))

        intent = IntentBuilder('TranslateIntent')\
            .require('TranslateKeyword') \
            .require('LanguageKeyword') \
            .require('phrase') \
            .build()
        self.register_intent(intent, self.handle_translate)

        intent = IntentBuilder('TranslateToIntent')\
            .require('TranslateKeyword') \
            .require('translate') \
            .require('ToKeyword') \
            .require('LanguageKeyword') \
            .build()
        self.register_intent(intent, self.handle_translate_to)


    def handle_translate(self, message):
	word = message.metadata.get("TranslateKeyword")
	lang = message.metadata.get("LanguageKeyword")
	sentence = message.metadata.get("phrase")

	translated = translate(sentence, lang)

	self.say(translated,lang)

    def handle_translate_to(self, message):
	lang = message.metadata.get("LanguageKeyword")
	sentence = message.metadata.get("translate")
	to = message.metadata.get("ToKeyword")

	translated = translate(sentence, lang)

	self.say(translated,lang)


    def say(self,sentence,lang):
	get_sentence = 'wget -q -U Mozilla -O /tmp/translated.mp3 "https://translate.google.com/translate_tts?tl=' + lang + '&q='+ sentence +'&client=tw-ob'+'"'
	os.system(get_sentence)
	play_mp3("/tmp/translated.mp3")



def create_skill():
    return TranslateSkill()


