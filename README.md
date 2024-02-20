# Are you here?

This is a very simple python script that checks wether you are in front of your computer or not. This way if you leave unatended your computer it will lock/sleep automaticaly.

## Installation

Just install python, then install the requirements with:

<pre>
    python -m pip install -r requirements.txt
</pre>

## Running

You are now ready to run the script, just open a terminal and run:

<pre>
    python lock_comp.py
</pre>

It could be that you need to change the camera input number in the code `lock_comp.py`. By default it uses `0` but maybe your camera is set in `1` or `2` or ... You can check the amount of video inputs you have using `ffmpeg`. for example in macOs would be:
<pre>
    ffmpeg -f avfoundation -list_devices true -i ""
</pre>
