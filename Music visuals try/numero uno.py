import pygame
import numpy as np
import wave
import math

# Load audio
audio_file = "FX_8BarsRiser2.wav"
wav = wave.open(audio_file, 'rb')

n_channels = wav.getnchannels()
sample_width = wav.getsampwidth()
frame_rate = wav.getframerate()
chunk_size = 1024

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Xtrullor-Style Visualizer")
clock = pygame.time.Clock()

center = (400, 400)
radius = 200
bar_count = 180  # More bars = smoother ring
angle_step = 360 / bar_count

# Main loop
running = True
data = wav.readframes(chunk_size)

def get_magnitudes(audio_data):
    samples = np.frombuffer(audio_data, dtype=np.int16)
    if n_channels == 2:
        samples = samples[::2]
    fft = np.abs(np.fft.fft(samples))[:bar_count]
    fft = fft / np.max(fft)
    return fft

while running and data:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    magnitudes = get_magnitudes(data)

    # Draw circular bars
    for i in range(bar_count):
        angle_deg = i * angle_step
        angle_rad = math.radians(angle_deg)

        x1 = center[0] + radius * math.cos(angle_rad)
        y1 = center[1] + radius * math.sin(angle_rad)

        bar_length = magnitudes[i] * 100
        x2 = center[0] + (radius + bar_length) * math.cos(angle_rad)
        y2 = center[1] + (radius + bar_length) * math.sin(angle_rad)

        color = (int(255 * magnitudes[i]), 100, 255)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

    pygame.display.flip()
    clock.tick(60)

    data = wav.readframes(chunk_size)

pygame.quit()
