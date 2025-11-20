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
from abc import ABC, abstractmethod

import numpy as np, math
from engine import TimeBase


class Wave(ABC):

    def __init__(self, frequency):
        self.frequency = frequency

    #Making abstract method so subclasses
    #must implement generate()
    @abstractmethod
    def generate(self, time_array):
        raise NotImplementedError
    
#inhereting from Wave for time array and frequency
class SineWave(Wave):

    def __init__(self, frequency): # not necessay for now but good practice
         super().__init__(frequency)
        
    def generate(self, time_array):
            phase = 2 * math.pi * self.frequency * time_array

            wave = np.sin(phase)

            return wave