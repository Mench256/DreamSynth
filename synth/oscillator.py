'''
An oscillator is a module that generates a continuous waveform — basically, it creates a raw sound.
It doesn’t need an input because it produces the signal itself.

init(sample_rate, block_size) → called when playback starts
(store the sample rate and reset its internal position in the wave)

process(num_frames) → returns a list/array of samples that form the waveform for that short time chunk


List these clearly:

frequency (Hz) — how many times per second the waveform repeats (e.g., 440 Hz = A4)

amplitude (0–1) — how loud the wave is

internal phase — keeps track of where in the waveform the oscillator currently is
(so each block continues smoothly into the next)

waveform type — for now, just “sine”, but can later be “square”, “saw”, etc.

Rules:

Output values stay within –1.0 to +1.0

Must be deterministic (same settings → same sound)

Must update phase continuously (no jumps at block boundaries)
'''