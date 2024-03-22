# fw
finnegans wake

1) Obtain audio
https://ubu.com/sound/joyce_fw.html

2) Obtain text
https://archive.org/stream/in.ernet.dli.2015.207614/2015.207614.Finnegans-Wake_djvu.txt

3) Segment text into reasonable chunks for YouTube
Maybe do that with AI?
Or just sentences?

4) Find the audio that matches that text

5) Put an image in the background

6) Put the text on top

7) Make a video



mp3splt -s -p th=-30,min=0.3 fw.mp3\n

for i in fw_si*mp3 && ffprobe -i $i -show_entries format=duration -v quiet -of csv="p=0"

