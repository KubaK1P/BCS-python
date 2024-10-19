import numpy as np
import simpleaudio as sa

rhythm = {
    "1": 4,
    "1.": 6,
    "1/2": 2,
    "1/2.": 3,
    "1/4": 1,
    "1/4.": 1.5,
    "1/8": 0.5,
    "1/8.": 0.75,
    "1/16": 0.25,
    "1/16.": 0.375,
    "1/32": 0.125
}

bars = [0 for i in range(9)]

better_call_saul_count = 1

tempo = 160

try:
    for k in rhythm.keys():
        rhythm[k] *= 60 / tempo
except ZeroDivisionError:
    print("Tempo must not be zero")
    tempo = 60

pitch = {
    "C2": 130.81,
    "Cs2": 138.59,
    "Db2": 138.59,
    "D2": 146.83,
    "Ds2": 155.56,
    "Eb2": 155.56,
    "E2": 164.81,
    "F2": 174.61,
    "Fs2": 185,
    "Gb2": 185,
    "G2": 196,
    "Gs2": 207.65,
    "Ab2": 207.65,
    "A2": 220,
    "B2": 233.08,
    "H2": 246.94,
    "C3": 261.63,
    "Cs3": 277.18,
    "Db3": 277.18,
    "D3": 293.66,
    "Ds3": 311.13,
    "Eb3": 311.13,
    "E3": 329.63,
    "F3": 349.23,
    "Fs3": 369.99,
    "Gb3": 369.99,
    "G3": 392,
    "Gs3": 415.3,
    "Ab3": 415.3,
    "A3": 440,
    "B3": 466.16,
    "H3": 493.88
}

sample_rate = 44100


def gen_wave(frequency, duration, waveform="square"):
    lookup_sample_rate = sample_rate
    t = np.linspace(0, duration, int(duration * lookup_sample_rate), False)
    note = (np.sin(frequency * t * 2 * np.pi)) if frequency != None else np.zeros(
        (int(duration * lookup_sample_rate),), dtype=np.int16)
    #note[-100:] = 0
    square = np.array([1 if q > 0 else -1 for q in note], dtype=np.float64)
    return square if waveform == "square" else note


bars[0] = gen_wave(pitch["A3"], rhythm["1"]) + gen_wave(pitch["E3"], rhythm["1"]) + \
    gen_wave(pitch["Cs3"], rhythm["1"]) + \
    gen_wave(pitch["A2"] / 2, rhythm["1"])
bars[1] = np.hstack(((gen_wave(pitch["A3"], rhythm["1/4"]) + gen_wave(pitch["E3"], rhythm["1/4"]) + gen_wave(pitch["Cs3"], rhythm["1/4"]) + gen_wave(pitch["A2"] / 2, rhythm["1/4"])), (gen_wave(pitch["Ds3"], rhythm["1/8"]) + gen_wave(pitch["E2"], rhythm["1/8"])), (gen_wave(pitch["E3"], rhythm["1/8"]) +
                    gen_wave(pitch["E2"], rhythm["1/8"])), (gen_wave(pitch["Cs3"] * 2, rhythm["1/8"]) + gen_wave(pitch["E2"], rhythm["1/8"])), (gen_wave(pitch["Gs3"], rhythm["1/8"]) + gen_wave(pitch["E2"], rhythm["1/8"])), (gen_wave(pitch["E3"], rhythm["1/4"]) + gen_wave(pitch["A2"] / 2, rhythm["1/4"]))))
bars[2] = gen_wave(pitch["C3"] * 2, rhythm["1"]) + gen_wave(pitch["G3"], rhythm["1"]) + \
    gen_wave(pitch["E3"], rhythm["1"]) + gen_wave(pitch["C2"], rhythm["1"])
bars[3] = np.hstack(((gen_wave(pitch["C3"] * 2, rhythm["1/4"]) + gen_wave(pitch["G3"], rhythm["1/4"]) + gen_wave(pitch["E3"], rhythm["1/4"]) + gen_wave(pitch["H2"] / 2, rhythm["1/4"])), (gen_wave(pitch["E3"] * 2, rhythm["1/4"]) + gen_wave(pitch["A3"], rhythm["1/4"]) + gen_wave(pitch["Fs3"], rhythm["1/4"]) +
                    gen_wave(pitch["D2"], rhythm["1/4"])), (gen_wave(pitch["D3"] * 2, rhythm["1/8"]) + gen_wave(pitch["D2"], rhythm["1/8"])), (gen_wave(pitch["C2"] * 2, rhythm["1/8"]) + gen_wave(pitch["D2"], rhythm["1/8"])), (gen_wave(pitch["C2"] * 2, rhythm["1/4"]) + gen_wave(pitch["E2"] / 2, rhythm["1/4"]))))
bars[4] = bars[0]
bars[5] = np.hstack(((gen_wave(pitch["A3"], rhythm["1/4"]) + gen_wave(pitch["E3"], rhythm["1/4"]) + gen_wave(pitch["Cs3"], rhythm["1/4"]) + gen_wave(pitch["A2"] / 2, rhythm["1/4"])), (gen_wave(pitch["D3"], rhythm["1/8"]) + gen_wave(pitch["A2"] / 2, rhythm["1/8"])), (gen_wave(pitch["E3"], rhythm["1/8"]
                                                                                                                                                                                                                                                                                    ) + gen_wave(pitch["A2"] / 2, rhythm["1/8"])), (gen_wave(pitch["Cs3"] * 2, rhythm["1/8"]) + gen_wave(pitch["A2"] / 2, rhythm["1/8"])), (gen_wave(pitch["E3"], rhythm["1/8"]) + gen_wave(pitch["E2"], rhythm["1/8"])), (gen_wave(pitch["G3"], rhythm["1/4"]) + gen_wave(None, rhythm["1/4"]))))
bars[6] = np.hstack(((gen_wave(pitch["E2"] / 2, rhythm["1/2"]) + gen_wave(None, rhythm["1/2"])),
                    (gen_wave(pitch["E2"], rhythm["1/2"]) + gen_wave(pitch["G2"], rhythm["1/2"]))))
bars[7] = np.hstack(((gen_wave(pitch["E3"], rhythm["1/4"]) + gen_wave(pitch["C3"], rhythm["1/4"])), (gen_wave(
    pitch["Eb3"], rhythm["1/4"])), (gen_wave(pitch["D3"], rhythm["1/4"])), (gen_wave(pitch["C3"], rhythm["1/4"]))))
bars[8] = np.hstack(((gen_wave(pitch["Eb2"], rhythm["1/8"])), (gen_wave(pitch["Eb2"], rhythm["1/8"])), (gen_wave(pitch["C3"], rhythm["1/8"])), (gen_wave(
    pitch["D3"], rhythm["1/8"])), (gen_wave(None, rhythm["1/8"])), (gen_wave(pitch["A2"] / 2, rhythm["1/8"])), (gen_wave(pitch["C2"], rhythm["1/4"]))))

audio = np.hstack(tuple(bars) * int(better_call_saul_count))

# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()
