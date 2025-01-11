sudo apt update
sudo apt upgrade
sudo apt install -y git emacs-nox
sudo apt install -y  vlc-bin  vlc-plugin-base python3-vlc python3-rpi.gpio
git clone https://github.com/CrabbyPete/toddler_video.git
cd toddler_video
chmod +x play.py
sudo cp play.py /usr/local/bin

