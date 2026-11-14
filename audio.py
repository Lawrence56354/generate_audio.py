import wave
import struct
import math

SAMPLE_RATE = 48000
FPS = 30
SAMPLES_PER_FRAME = SAMPLE_RATE // FPS  # 1600 samples per frame

# Representative frequencies (Hz) across Bands 1 to 8
BAND_NOTES = [
    261.63, 293.66, 329.63, 349.23,  # Band 1: + - * /
    392.00, 440.00, 493.88, 523.25,  # Band 2-3
    587.33, 659.25, 698.46, 783.99,  # Band 4-5
    880.00, 987.77, 1046.50, 1174.66 # Band 6-8
]

FRAMES_PER_NOTE = 15  # 0.5 seconds per symbol at 30 FPS

with wave.open("math_bands_1_to_8_30fps.wav", "w") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(SAMPLE_RATE)

    for freq in BAND_NOTES:
        total_samples = FRAMES_PER_NOTE * SAMPLES_PER_FRAME
        for s in range(total_samples):
            t = s / SAMPLE_RATE
            envelope = max(0.0, 1.0 - (s / total_samples))
            # Square/sine blend for classic symbol synth tone
            val = math.sin(2 * math.pi * freq * t)
            sample = int(val * envelope * 16000)
            wav_file.writeframes(struct.pack("<h", sample))
