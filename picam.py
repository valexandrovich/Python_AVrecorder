from AudioRecorder import AudioRecorder
from VideoRecorder import VideoRecorder
import time
from gpiozero import Button
from signal import pause

def start_AVrecording():
    # video_thread.start()
    audio_thread.start()
    time.sleep(10)
    audio_thread.stop()

def test_audio():
    audio_thread.test()

def main():
    global video_thread
    global audio_thread
    
    timestamp = time.time()

    video_thread = VideoRecorder(timestamp)
    audio_thread = AudioRecorder(timestamp)

    # Allows time for camera to boot up
    time.sleep(5)

    button = Button(14)
    button.when_pressed = start_AVrecording
    print("ready for action!")
    pause()

if __name__ == "__main__":
    main()