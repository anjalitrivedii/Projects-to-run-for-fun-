import pygame
import os

# Initialize the mixer
pygame.mixer.init()


def play_audio(file_path):
    if not os.path.isfile(file_path):
        print("File not found. Please check the path.")
        return

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print("\nPlaying:", os.path.basename(file_path))
        print("Commands: [p]ause | [r]esume | [s]top")

        while True:
            cmd = input("Enter command: ").lower()
            if cmd == 'p':
                pygame.mixer.music.pause()
            elif cmd == 'r':
                pygame.mixer.music.unpause()
            elif cmd == 's':
                pygame.mixer.music.stop()
                break
    except Exception as e:
        print("Error playing audio:", e)


def main():
    # 🔽 Replace this path with your local audio file path
    file_path = "C:\\Users\\anjal\\Downloads\\timeless-playboi-carti-x-the-weeknd-type-beat-315481.mp3"

    play_audio(file_path)


if __name__ == "__main__":
    main()
