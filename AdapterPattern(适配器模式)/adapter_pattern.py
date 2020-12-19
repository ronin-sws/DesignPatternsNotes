# coding=utf-8

# 1 接口类
class MediaPlayer():
    """创建媒体播放器接口"""
    def play(self, audioType, fileName):
        pass

class AdvancedMediaPlayer():
    """创建高级的媒体播放器接口"""
    def playVlc(self, fileName):
        pass

    def playMp4(self, fileName):
        pass

# 2 接口实体类
class VlcPlayer(AdvancedMediaPlayer):
    """创建实现AdvancedMediaPlayer接口的实体类VlcPlayer"""

    def playVlc(self, fileName):  # 重写 playVlc 方法
        print("Playing vlc file. Name:{}".format(fileName))

    def playMp4(self, fileName):
        pass

class Mp4Player(AdvancedMediaPlayer):
    """创建实现AdvancedMediaPlayer接口的实体类Mp4Player"""

    # def __init__(self, fileName):
    #     self.fileName = fileName

    def playVlc(self, fileName):
        pass

    def playMp4(self, fileName): # 重写 playMp4 方法
        print("Playing mp4 file. Name:{}".format(fileName))

# 3 适配器类
class MediaAdapter(MediaPlayer):
    """创建实现了 MediaPlayer 接口的适配器类"""
    def __init__(self, advancedMusicPlayer):
        self.advancedMusicPlayer = advancedMusicPlayer

    def MediaAdapter(self, audioType):
        if audioType.lower("vlc"):
            self.advancedMusicPlayer = VlcPlayer()
        elif audioType.lower("mp4"):
            self.advancedMusicPlayer = Mp4Player()

    def play(self,audioType, fileName):
        if audioType.lower("vlc"):
            self.advancedMusicPlayer.playVlc(fileName)
        elif audioType.lower("mp4"):
            self.advancedMusicPlayer.playMp4(fileName)

# 4
class AudioPlayer(MediaPlayer):
    """创建实现了 MediaPlayer 接口的实体类"""

    def play(self, audioType, fileName): # 重写接口类中的play方法
        if audioType.lower()== "mp3":  # 播放 mp3 音乐文件的内置支持
            print("Playing mp3 file. Name:{}".format(fileName))

        elif audioType.lower() == "vlc":  # mediaAdapter 提供了播放其他文件格式的支持
            advancedMusicPlayer = VlcPlayer()
            advancedMusicPlayer.playVlc(fileName)

        elif audioType.lower() == "mp4":
            advancedMusicPlayer = Mp4Player()
            advancedMusicPlayer.playMp4(fileName)

        else:
            print("Invalid media.{}  format not supported".format(audioType))


if __name__ == "__main__":
    audioPlayer = AudioPlayer()
    audioPlayer.play("mp3", "beyond the horizon.mp3")
    audioPlayer.play("mp4", "alone.mp4")
    audioPlayer.play("vlc", "far far away.vlc")
    audioPlayer.play("avi", "mind me.avi")