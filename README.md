# Dice Sound Checker
This repository is a test and simulation for 2 DF player minis playing sound files.
The DFPlayer mini is a simple .mp3/.wav audio player. It does not support simultaneous playback of audio-files, thus making dice shaking simulations hard to achieve. Whenever play has been invoked on the DFPlayer mini, the currently playing file will be stopped and replaced by a new file, making hard audio cut-offs hearable.

This repository will be a testing ground that helps with generating suitable dice shaking audio files. Furthermore it simulates 2 DFPplayer mini playing after each other on their own speakers.

Simply drop and replace the audio files in sounds folder. Audio format must be .wav

# How to setup
- Have python 3.7+ installed
- Clone this repository
- Create a virtual environment if needed `python3 -m venv venv`
- If on linux, activate the venv with command `source venv/bin/activate`
- Select python3 venv interpreter in your chosen IDE. <br>
On VSCode go `ctrl + shift + P` -> `Python: Select Interpreter`
- Intall requirements; `pip3 install requirements.txt`
- Start main
