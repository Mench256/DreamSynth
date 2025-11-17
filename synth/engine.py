'''
The Engine is the controller of the synthesizer.
It tells each module when to start, how many samples to generate, and combines the results into a final sound buffer.
It also decides how long to run and what sample rate to use.



Setup

Decide on sample_rate (e.g., 48,000 samples/sec)

Decide on block_size (e.g., 512 samples per chunk)

Create an empty “output buffer” to hold the entire sound

Initialize modules

Tell each module its sample_rate and block_size (using their init())

Render loop

Decide how long the sound should be (e.g., 2 seconds)

Calculate total samples = duration × sample rate

Ask each module for one block at a time (call process(num_frames))

Add each block’s samples to the output buffer until done

Write output

Once all samples are ready, save the sound to a .wav file in output/renders/


Rules:
Must process audio in blocks (to simulate real-time playback 512 samples at a time)

Must keep timing consistent (each block advances time correctly)

Must handle clipping (values outside –1.0…+1.0 should be limited)

Must produce a WAV file that’s playable in any audio program

Deterministic — same input/patch = same sound file
'''

import numpy as np

class TimeBase:
    #Sample rate is going to be a fixed value
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate


    def time_func(self, duration):
        #Calculating the sample_rate per duration
        num_samples = int(duration * self.sample_rate)

        #array of samples
        index_array = np.arange(num_samples)
        #
        #time array is the time for each sample
        time_array = index_array / self.sample_rate

        return time_array
