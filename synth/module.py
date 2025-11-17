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