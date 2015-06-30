import pydub
import tempfile

class GoogleEngine(object):

    def __init__(self):
        import GoogleTTS
        self.GoogleTTS=GoogleTTS

    def speak(self, text, language):
        t=tempfile.TemporaryFile()
        args=self.GoogleTTS.audio_args(language=language, output=t)
        self.GoogleTTS.audio_extract(text, args)

        t.seek(0)
        return pydub.AudioSegment.from_file(t, 'mp3')
