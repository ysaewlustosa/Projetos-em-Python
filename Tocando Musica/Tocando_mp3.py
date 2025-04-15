import pygame   
pygame.init()  # Initialize the mixer module
pygame.mixer.music.load("Tocando.mp3")  # Load the music file
pygame.mixer.music.play()  # Play the music     
pygame.event.wait()  # Wait for the music to finish playing