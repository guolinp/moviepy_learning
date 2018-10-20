#!/usr/bin/python3

from moviepy.editor import *

input_mp4_files=[
    "20180915_165944_001.mp4",
    "20180915_170035_001.mp4",
    # more mp4s
]

output_videoclip="output.mp4"

input_videoclips=[]

for f in input_mp4_files:
    input_videoclips.append(VideoFileClip(f))

final_clip = concatenate_videoclips(input_videoclips)

final_clip.to_videofile(output_videoclip, fps=24, remove_temp=False) 
