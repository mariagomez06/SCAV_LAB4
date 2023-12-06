#!/usr/bin/env python
# coding: utf-8

# # TASK 2
# 

# Maria Gómez - 218011

# In[ ]:


import subprocess

def export_video_comparison(input_video_vp8, input_video_vp9, output_comparison):
    # Set the width and height of the output video
    width = 640
    height = 360

    # Use ffmpeg to overlay the two videos side by side
    command = [
        "ffmpeg",
        "-i", input_video_vp8,
        "-i", input_video_vp9,
        "-filter_complex", f"[0:v]scale={width}:-1[p0];[1:v]scale={width}:-1[p1];[p0][p1]hstack=inputs=2",
        "-c:v", "libx264",
        "-crf", "23",  # Adjust the CRF value as needed
        "-preset", "medium",  # Adjust the preset as needed
        "-tune", "zerolatency",
        "-strict", "experimental",
        output_comparison
    ]

    subprocess.run(command)

if __name__ == "__main__":
    input_video_vp8 = r"C:\Users\MARIA\Downloads\output_video_vp8.webm"
    input_video_vp9 = r"C:\Users\MARIA\Downloads\output_video_vp9.webm"
    output_comparison = r"C:\Users\MARIA\Downloads\video_comparison.mp4"

    export_video_comparison(input_video_vp8, input_video_vp9, output_comparison)

