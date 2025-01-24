#!/usr/bin/env python
import vlc
import pathlib
import RPi.GPIO as GPIO

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__file__)

# Setup the raspberry pi pins
BUTTON_PIN_1 = 40
BUTTON_PIN_2 = 38
BUTTON_PIN_3 = 36
BUTTON_PIN_4 = 32

HOME = pathlib.Path().resolve()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def play_video(player, media):
    """
    Play the selected video
    :param player: vlc player instance
    :param media: video to play
    :return:
    """
    # You need to call "set_media()" to (re)load a video before playing it
    player.set_media(media)
    player.play()

def main():
    """
    Main loop to play each video
    :return: Never
    """
    # Set up a player instance. Suppress lots of log messages
    instance = vlc.Instance("--verbose=-1")
    player = instance.media_player_new()

    # Create libVLC objects representing each video
    video1 = vlc.Media(os.path.join(HOME,"videos/big_buck_bunny_480p_10mb.mp4"))
    video2 = vlc.Media(os.path.join(HOME,"videos/Caminandes_Trailer-1080p.mp4"))
    video3 = vlc.Media(os.path.join(HOME,"videos/The_End.mp4"))
    video4 = vlc.Media(os.path.join(HOME,"videos/andre_wally.mp4"))

    # Start the player for the first time
    play_video(player, video1)
    current_video = video1

    # TODO: Add some error handling or at least a proper Ctrl-C handler
    while True:

        # See which button was pressed and the right video
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