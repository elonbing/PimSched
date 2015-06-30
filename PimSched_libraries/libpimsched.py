try: #If pydub is installed on this machine, use that library
    from pydub import AudioSegment
except ImportError: #If not, use the included one
    from ..included_libraries.pydub import AudioSegment
    
import tts
from collections import namedtuple
import tempfile

pimsleur_intervals=(0, 2, 8, 33, 154)
two_second_silence=AudioSegment.silent(duration=2000)
five_second_silence=AudioSegment.silent(duration=5000)

def intervals_generator(intervals):
    intervals_seen = set()
    index = -1
    while True:
        index += 1
        intervals_values = set([ index + i for i in intervals ])
        if intervals_seen.isdisjoint(intervals_values):
            intervals_seen |= intervals_values
            yield intervals_values

IdiomTuple = namedtuple('IdiomTuple', ['language','idiom'])

class Lesson(object):

    def __init__(self, engine=tts.GoogleEngine, intervals=pimsleur_intervals, shortsilence=two_second_silence, longsilence=five_second_silence):
        self.intervals = intervals
        self.igenerator = intervals_generator(intervals)
        self.lessondict={}
        self.idiomcount=0

        self.speaker=engine()
        self.shortsilence=shortsilence
        self.longsilence=longsilence

    def speakidiompair(self, idiompair):
        spokenidiompair = self.speaker.speak(idiompair[0].idiom, idiompair[0].language) + self.shortsilence + self.speaker.speak(idiompair[1].idiom, idiompair[1].language)
        return spokenidiompair+AudioSegment.silent(duration=5000-len(spokenidiompair))

    def add(self, idiompair):
        spokenidiompair = self.speakidiompair(idiompair)
        self.addspoken(spokenidiompair)

    def addspoken(self, spokenidiompair):
        intervals = self.igenerator.next()
        for i in intervals:
            self.lessondict[i] = spokenidiompair

    def makeaudio(self):
        audio=AudioSegment.empty()
        for i in range(max(self.lessondict)+1):
            audio+=self.lessondict.get(i,self.longsilence)
        return audio

    def exportaudio(self, path):
        return self.makeaudio().export(path)
