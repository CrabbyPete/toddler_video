import vlc
import RPi.GPIO as GPIO

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__file__)

BUTTON_PIN_1 = 40
BUTTON_PIN_2 = 38
BUTTON_PIN_3 = 36
BUTTON_PIN_4 = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def play_video(player, media):
    # You need to call "set_media()" to (re)load a video before playing it
    player.set_media(media)
    player.play()

def main():
    instance = vlc.Instance()
    player = instance.media_player_new()

    # Create libVLC objects representing the two videos
    video1 = vlc.Media("./videos/big_buck_bunny_480p_10mb.mp4")
    video2 = vlc.Media("./videos/Caminandes_Trailer-1080p.mp4")
    video3 = vlc.Media("./videos/The_End.mp4")
    video4 = vlc.Media("./videos/andre_wally.mp4")

    # Start the player for the first time
    play_video(player, video1)
    current_video = video1

    # TODO: Add some error handling or at least a proper Ctrl-C handler
    while True:
        if not GPIO.input(BUTTON_PIN_1):
            if not current_video == video1:
                current_video = video1
                play_video(player, current_video)

        elif not GPIO.input(BUTTON_PIN_2):
            if not current_video == video2:
                current_video = video2
                play_video(player, current_video)

        elif not GPIO.input(BUTTON_PIN_3):
            if not current_video == video3:
                current_video = video3
                play_video(player, current_video)

        elif not GPIO.input(BUTTON_PIN_4):
            if not current_video == video4:
                current_video = video4
                play_video(player, current_video)

        # Loop video if playback is ended
        if player.get_state() == vlc.State.Ended:
            play_video(player, current_video)

if __name__ == '__main__':
    main()