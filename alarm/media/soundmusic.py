from playsound import playsound

class MusicPlayer:
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self):
        # Reproduce el archivo de audio
        playsound(self.file_path)

# Uso del objeto
player = MusicPlayer("alarmaGorilas.mp3")
player.play()
