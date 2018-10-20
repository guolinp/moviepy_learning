#!/usr/bin/python3

import imageio
import ssl

# pip install moviepy
ssl._create_default_https_context = ssl._create_unverified_context

imageio.plugins.ffmpeg.download() 
