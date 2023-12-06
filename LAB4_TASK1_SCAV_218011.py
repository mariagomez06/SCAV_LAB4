#!/usr/bin/env python
# coding: utf-8

# # Task 1

# Maria Gómez - 218011

# In[ ]:


import subprocess

class VideoConverter:
    def __init__(self, input_path):
        self.input_path = input_path

    def convert_to_vp8(self, output_path):
        self._convert_video("libvpx", output_path)

    def convert_to_vp9(self, output_path):
        self._convert_video("libvpx-vp9", output_path)

    def convert_to_h265(self, output_path):
        self._convert_video("libx265", output_path)

    def convert_to_av1(self, output_path):
        self._convert_video("libaom-av1", output_path)

    def _convert_video(self, codec, output_path):
        command = [
            "ffmpeg",
            "-i", self.input_path,
            "-c:v", codec,
            "-b:v", "1M",  
            output_path
        ]

        subprocess.run(command)

if __name__ == "__main__":
    
    input_video_path = r"C:\Users\MARIA\Downloads\BBB_9sec.mp4"
    
    print("A qué formato quieres convertir el video: VP8, VP9, H265 o AV1?")
    R = input()
    
    if (R == 'VP8'):
        converter = VideoConverter(input_video_path)
        output_vp8_path = r"C:\Users\MARIA\Downloads\output_video_vp8.webm"
        converter.convert_to_vp8(output_vp8_path)
        
    elif (R == 'VP9'):
        converter = VideoConverter(input_video_path)
        output_vp9_path = r"C:\Users\MARIA\Downloads\output_video_vp9.webm"
        converter.convert_to_vp9(output_vp9_path)
    
    elif (R == 'H265'):
        converter = VideoConverter(input_video_path)
        output_h265_path = r"C:\Users\MARIA\Downloads\output_video_h265.mp4"
        converter.convert_to_h265(output_h265_path)

    elif (R == 'AV1'):
        converter = VideoConverter(input_video_path)
        output_av1_path = r"C:\Users\MARIA\Downloads\output_video_av1.mp4"
        converter.convert_to_av1(output_av1_path)
        
    else:
        print('invalid input')

