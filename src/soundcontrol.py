"""
>>> import soundcontrol
>>> control = soundcontrol.SoundControl()
>>> control.mute()
>>> control.unmute()
>>> control.volume("40%")
>>> control.volume("10%+")
>>> control.get_status()
{'volume': '50%', 'active': 'on'}
>>> control.play("audio.ogg")
"""
import subprocess
import re


class SoundControl(object):
    def __init__(self):
        self.null = open('/dev/null', 'wb')

    def mute(self):
        subprocess.check_call("amixer set Master mute", shell=True, stdout=self.null)

    def unmute(self):
        subprocess.check_call("amixer set Master unmute", shell=True, stdout=self.null)

    def volume(self, value):
        # control.volume("40%")
        # control.volume("40%+")
        subprocess.check_call("amixer set Master %s" % value, shell=True, stdout=self.null)

    def get_status(self):
        output = subprocess.check_output("amixer get Master", shell=True)
        data = re.search("  Front Left: Playback \d+ \[(?P<volume>[^\]]*)\] \[(?P<active>.*)\]", output)
        return data.groupdict()

    def play(self, soundfile):
        subprocess.call(["play", soundfile])


if __name__ == '__main__':
    control = SoundControl()
    control.mute()
    control.unmute()
    control.volume("40%")
    control.volume("10%+")
    control.volume("20%-")
    print(control.get_status())  # {'volume': '30%', 'active': 'on'}
