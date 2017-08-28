# PDF-Downloader
This project is a PDF Downloader I wrote - it lets you automatically download all of the PDF's from a website. I use it to download material from college courses; for example, I might want to save some sample tests from an MIT Classical Mechanics course without saving all the tests by hand. The downloader will work no matter what type of PDF you want, so feel free to be creative!

There are three main parameters, as follows.

1. You will be prompted for the URL - simply enter the URL containing the desired PDF's.
2. You will be prompted for the folder location - enter the entire path of the desired directory.
3. You will be prompted for a character, either 'y' or 'n'. If 'y' is entered, the names of the files saved will be the hyperlinks featured on the website. For example, if the website has a PDF with a link called "Practice Problems," then your saved file will be called "Practice Problems.pdf." If you select 'n', then the default file name will be saved; it could be something like "MIT_Notes_12404.pdf." Depending on the situation, either parameter could be the more useful; you might want to choose 'n' if all of the website links say "PDF", for example.

After the parameters are entered, the code will do its magic!

You can run this code in a Python IDE (This code is written for Python 3), but I find it conveninent to run directly from termial/command prompt. To run it from command line, use "python PDF_Downloader" and you will be able to enter the parameters directly from command line.

If you find any problems with the code, please email me, comment, or make a pull request, and I'll try to fix it ASAP. Enjoy!
