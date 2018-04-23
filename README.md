# Movie Trailer Website

This program takes a list of movies, provided in a .txt document, and then converts them into a website that shows the title of the movie, the poster art for that movie, and if you click on the movie you will be shown a trailer for that movie. This product uses the TMDb API but is not endorsed or certified by TMDb.

# Installation:

Python Version: 3.6.5 <br>
Open the terminal on MacOS or Linux, or the command prompt on Windows and type in 'python' and 'python3' to see if you have that version of Python or later. Simply entering 'python' may return the version of Python 2 on your system, in that case try Python3. <br>

If you do not have Python on your system, then follow this guide: http://docs.python-guide.org/en/latest/starting/installation/
<br>
<br>

Pipenv Installation:

While you can just grab pip and install the necessary requirements for this program, it's better to use a virtual environment to better organize everything. Pipenv is a great tool for this and instructions for downloading and setting it up can be found here: <br>http://docs.python-guide.org/en/latest/dev/virtualenvs/
<br>
<br>

After both Python and Pipenv are on your system, do the following:
<ol>
<li>Open a terminal or command prompt in the folder of this program</li>
<li>Enter 'pipenv install' to install all dependencies from the Pipfile</li>
<li>After it's finished running, enter 'pipenv shell' to enter the virtual environment</li>
</ol>

# Usage
Using the program is relatively straightforward. Edit the 'input.txt' file included with the program with a list of movie names, each movie on a different line, that you wish to create a movie trailer website out of. In theory, you can put as many movies as you'd like. Some example movies are provided for your convenience.
<br>
<br>
After you are satisifed with the input file, simply enter 'python media_center.py' into the terminal or command prompt in which you ran 'pipenv shell'. This will run the file in the virtual environment, ensuring it has access to all dependencies. If you do not do this, it probably will not work.
<br>
<br>
After the program is finished running, an html file labeled 'fresh_tomatoes.html' will appear in the same folder of the program. Open this file in your preferred browser to view the website.