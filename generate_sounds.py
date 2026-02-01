import wave
import math
import struct
import random
import os

def save_wav(filename, samples, sample_rate=44100):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with wave.open(filename, 'w') as obj:
        obj.setnchannels(1) # mono
        obj.setsampwidth(2) # 2 bytes (16 bit)
        obj.setframerate(sample_rate)
        
        # Convert floats (-1.0 to 1.0) to integers
        raw_data = bytearray()
        for s in samples:
            # Clip between -1 and 1
            s = max(-1.0, min(1.0, s))
            # Scale to 16-bit integer range
            int_val = int(s * 32767)
            raw_data.extend(struct.pack('<h', int_val))
            
        obj.writeframes(raw_data)
    print(f"Generated {filename}")

def generate_jump(duration=0.3, sample_rate=44100):
    samples = []
    # Slide frequency up
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        freq = 300 + (t / duration) * 600 # 300Hz to 900Hz
        sample = 0.5 * math.sin(2 * math.pi * freq * t)
        samples.append(sample)
    return samples

def generate_coin(duration=0.1, sample_rate=44100):
    samples = []
    # High pitched ping (two tones)
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        freq = 1200 if t < duration/2 else 1800
        # Decay volume
        vol = 0.5 * (1 - (t / duration))
        sample = vol * math.sin(2 * math.pi * freq * t)
        samples.append(sample)
    return samples

def generate_hit(duration=0.3, sample_rate=44100):
    samples = []
    # Noise / Low frequency crash
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        # White noise + decay
        vol = 0.5 * (1 - (t / duration))
        sample = vol * (random.random() * 2 - 1)
        samples.append(sample)
    return samples

# Generate sounds
save_wav("assets/sounds/jump.wav", generate_jump())
save_wav("assets/sounds/coin.wav", generate_coin(0.2))
save_wav("assets/sounds/hit.wav", generate_hit())
