import argparse
from soundcontrol import SoundControl


parser = argparse.ArgumentParser(description='Controla el sonido del ordena')
parser.add_argument('-v', '--volume',
                    type=str,
                    help="el volumen que queremos: 40%% o 20%%+, por ejemplo")
parser.add_argument('-s', '--show',
                    action="store_true",
                    help="Muestra estado actual")
group = parser.add_mutually_exclusive_group()
group.add_argument('-u', '--unmute',
                   action="store_true",
                   help="activa el sonido")
group.add_argument('-m', '--mute',
                   action="store_true",
                   help="silencia el sonido")

if __name__ == '__main__':
    args = parser.parse_args()
    control = SoundControl()
    if args.mute:
        control.mute()
    if args.unmute:
        control.unmute()
    if args.volume is not None:
        control.volume(args.volume)
    if args.show:
        print "Volumen: %(volume)s  Estado: %(active)s" % control.get_status()
