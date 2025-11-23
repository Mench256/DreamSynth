'''
What is a Module?

A module is one building block of the 
synthesizer. It either generates or modifies
sound data.

What Methods must it have?

init(sample_rate, block_size)-> called once playback starts
process(num_frames)-> produces or modifies that many samples

What rules must every module follow?

keep samples betweem -1.0 and +1.0
must be deterministic(same input = same output)
must not modify its input in place
'''

from abc import ABC, abstractmethod

class Module(ABC):

    @abstractmethod
    def generate(self, time_array):
        pass


class OscillatorModule(Module):
    def __init__(self, wave, amp = 0.5):
        self.wave = wave
        self.amp = amp

    def generate(self, time_array):
        signal = self.amp * self.wave.generate(time_array)

        return signal
    

    ## Having all files imported to a test script for the next testing run.
    # personal note: make sure you understand every piece of code inside and out