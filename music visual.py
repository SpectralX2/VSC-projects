import pygame
import numpy as np
import scipy.io.wavfile as wav
import time
import sys
import random

# === CONFIG ===
AUDIO_FILE = "C:\Users\Tian\Downloads\FX_8BarsRiser2.wav"  # Replace this with your .wav path
WIDTH, HEIGHT = 1280, 720
FPS = 60
NUM_BARS = 100
PARTICLE_COUNT = 100
WAVE_RESOLUTION = 2  # Lower = more detailed waveform
BEAT_THRESHOLD = 1.8  # Increase if too sensitive

# === INIT ===
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Music Visualizer")
clock = pygame.time.Clock()

# === AUDIO ===
rate, data = wav.read(AUDIO_FILE)
if data.ndim == 2:
    data = data.mean(axis=1)
data = data / np.max(np.abs(data))  # Normalize to -1..1

audio_pos = 0
samples_per_frame = int(rate / FPS)

# === PARTICLES ===
particles = []

def spawn_particle():
    return {
        "x": random.uniform(0, WIDTH),
        "y": HEIGHT,
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(-5, -2),
        "radius": random.uniform(2, 5),
        "life": random.uniform(1.0, 2.0),
        "color": pygame.Color(255, 255, 255)
    }

for _ in range(PARTICLE_COUNT):
    particles.append(spawn_particle())

# === FUNCTIONS ===
def get_fft(samples):
    window = np.hanning(len(samples))
    fft_result = np.abs(np.fft.rfft(samples * window))
    fft_result = fft_result[:NUM_BARS]
    fft_result = np.log1p(fft_result)
    return fft_result / np.max(fft_result)

def get_waveform(samples):
    samples = samples[::WAVE_RESOLUTION]
    return samples * (HEIGHT // 3)

def draw_bars(magnitudes, time_offset):
    bar_width = WIDTH / NUM_BARS
    for i, magnitude in enumerate(magnitudes):
        color = pygame.Color(0)
        hue = int((i * 3 + time_offset * 60) % 360)
        color.hsva = (hue, 100, 100, 100)
        bar_height = magnitude * HEIGHT * 0.7
        x = i * bar_width
        y = HEIGHT - bar_height
        pygame.draw.rect(screen, color, (x, y, bar_width - 2, bar_height))

def draw_waveform(waveform):
    mid = HEIGHT // 2
    points = []
    for i, val in enumerate(waveform):
        x = i * (WIDTH / len(waveform))
        y = mid + val
        points.append((x, y))
    if len(points) > 1:
        pygame.draw.lines(screen, (0, 255, 255), False, points, 2)

def update_particles(dt, intensity):
    for p in particles:
        p["x"] += p["vx"] * dt * 60
        p["y"] += p["vy"] * dt * 60
        p["life"] -= dt
        if p["life"] <= 0 or p["y"] < 0:
            new_p = spawn_particle()
            new_p["radius"] *= intensity * 1.5
            particles[particles.index(p)] = new_p

def draw_particles():
    for p in particles:
        alpha = max(0, min(255, int(p["life"] * 255)))
        surf = pygame.Surface((p["radius"]*2, p["radius"]*2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*p["color"][:3], alpha), (p["radius"], p["radius"]), p["radius"])
        screen.blit(surf, (p["x"], p["y"]))

# === MAIN LOOP ===
running = True
start_time = time.time()

while running and audio_pos + samples_per_frame < len(data):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # AUDIO FRAME
    samples = data[audio_pos:audio_pos + samples_per_frame]
    audio_pos += samples_per_frame
    fft_magnitudes = get_fft(samples)
    waveform = get_waveform(samples)
    avg_energy = np.mean(fft_magnitudes)
    beat_detected = avg_energy > BEAT_THRESHOLD

    # UPDATE
    dt = clock.get_time() / 1000.0
    update_particles(dt, avg_energy)

    # DRAW
    screen.fill((0, 0, 0))
    draw_bars(fft_magnitudes, time.time() - start_time)
    draw_waveform(waveform)
    draw_particles()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()