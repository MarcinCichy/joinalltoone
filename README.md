The program was written for the "Za Rączkę" mentoring program.

The instructor (mentor) asked us to create a program that would combine all the files of our project into one file, named "full.cr.txt.
This single file should look like:

==================== 
FILE: file name

    file content

==================== 
FILE: name of the next file

    content of the next file


This program was written using the PyQt5 module.


Using this program, you can combine selected files into the required format.

Files are loaded using the "Select Files" button.
When their names appear in the right window ("Files to Select"), choose the files you intend to combine into one.

Upon clicking the file name, the icon next to it changes from red to green, and the content of the selected file(s) appears in the required format in the "Joined All Files" window.

In the "Joined All Files" window, you can also edit the files.

Before combining the files into one, you should select a relative path and specify the main project folder using the "Main Folder" button.

After pressing the "JOIN" button, a text file with the user-provided name is saved, which contains the content of all selected files in the required format.

Additionally, when you select the "with layout" option, a file is created that stores information about the read file names and which of them were selected.

Such a file (with the ".layout" extension) can be loaded later and recreate the point when the work of combining files was saved. You can then continue working from that point.