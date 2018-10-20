#!/usr/bin/python3

from moviepy.editor import *

input_mp4='f489336da1dc023b3fed821609f7147b.mp4'

output_videoclip='xxxx.mp4'

content = VideoFileClip(input_mp4)
# cut the range: 0 min 5 sec, 0 min 10 sec
# can call resize
sub_videoclip = content.subclip(5,10)#.resize((480,320))

final_clip = concatenate_videoclips([sub_videoclip])

final_clip.to_videofile(output_videoclip, fps=24, remove_temp=False)
