# Written by Alan Chung, https://achungweb.wordpress.com/
# Feel free to use this code, but please keep these comments if sharing this code :)

# I wrote this program using BeautifulSoup, which is a popular HTML parser/processor
# Some more information about it can be found here:
#       https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# I also referred to this site for tips on how to do this
# https://null-byte.wonderhowto.com/how-to/download-all-pdfs-webpage-with-python-script-0163031/
# Definitely check them out

import urllib
import urllib.parse
import urllib.request
import os
import sys
import requests
from bs4 import BeautifulSoup

############ INSERT URL HERE BETWEEN QUOTES. EXAMPLE: 'google.com' ############
url = input("Enter the URL: ")
###############################################################################

############ INSERT PATH TO THE DESIRED FOLDER HERE ###########################
PATH = input("Enter the path: ")
###############################################################################

############ CHOOSE THE NAME OF THE FILE TO BE SAVED ##########################
############ 'n' WILL SAVE THE DEFAULT FILE NAME ##############################
############ 'y' WILL SAVE THE NAME OF THE LINK FEATURED ON THE WEBSITE #######
############ For example, if the website says "Practice Problems", ############
############ 'y' will save "Practice Problems.pdf" ############################
############ while 'n' might save something like MIT_fall_124.pdf #############

param = 'random'
while param != 'y' and param != 'n':
    param = input("Enter y to save the name of the hyperlink on the website; n to save the default file name (y/n): ")
###############################################################################

# Takes the HTML from the url and turns it into 'soup.'
request = urllib.request.urlopen(url).read()
soup = BeautifulSoup(request, "lxml")

# Helper method to determine if a file already if exists. If so, then the program will append the smallest unused
# integer to the end. For example, if there are three instances of 'example.pdf' on a website, the program will
# save them as 'example.pdf', 'example_001', and 'example_002' in the order in which they appear. The program
# can save up to 1000 pdfs of the same name from a site, but this most likely will not happen
# The helper method will then save the file to the despired path.

# Please note that if you try to download the same file twice under the same name, the new version will not save
# as a pdf.

def exists(curUrl, current, strName):
    randomVariable  = True
    tempIndex = os.path.basename(curUrl).index('.pdf')
    count = 0
    while count <= 1000:
        if count == 0:
            if param == 'y':
                if (os.path.isfile(PATH + '/' + strName + ".pdf")):
                    count = count + 1
                    continue
                else:
                    try:
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl), PATH + '/' + strName + ".pdf")
                        print(strName)
                        return
                    except:
                        return
            else:
                if (os.path.isfile(PATH + '/' + os.path.basename(curUrl))):
                    count = count + 1
                    continue
                else:
                    try:
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        return
                    except:
                        return
        elif count >= 1 and count <= 9:
            if param == 'y':
                if os.path.isfile(PATH + '/' + strName + '_00' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl), PATH + '/' + strName + '_00' + str(count) + ".pdf")
                        print(strName + '_00' + str(count))
                        return
                    except:
                        return
            else:
                if os.path.isfile(PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_00' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        os.rename(PATH + '/' + os.path.basename(curUrl), PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf")
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl), PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_00' + str(count) + '.pdf')
                        os.rename(PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf",PATH + '/' + os.path.basename(curUrl))
                        return
                    except:
                        return
        elif count >= 10 and count <= 99:
            if param == 'y':
                if os.path.isfile(PATH + '/' + strName + '_0' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        file = open(PATH + '/' + os.path.basename(curUrl),'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl),PATH + '/' + strName + '_0' + str(count) + ".pdf")
                        print(strName + '_0' + str(count))
                        return
                    except:
                        return
            else:
                if os.path.isfile(PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_0' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        os.rename(PATH + '/' + os.path.basename(curUrl),
                                  PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf")
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl),
                                  PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_0' + str(count) + '.pdf')
                        os.rename(PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf",
                                  PATH + '/' + os.path.basename(curUrl))
                        return
                    except:
                        return
        elif count >= 100 and count <= 999:
            tempIndex = os.path.basename(curUrl).index('.pdf')
            if param == 'y':
                if os.path.isfile(PATH + '/' + strName + '_' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        file = open(PATH + '/' + os.path.basename(curUrl),'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl), PATH + '/' + strName + '_' + str(count) + ".pdf")
                        print(strName + '_' + str(count))
                        return
                    except:
                        return
            else:
                if os.path.isfile(PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_' + str(count) + ".pdf"):
                    count = count + 1
                    continue
                else:
                    try:
                        os.rename(PATH + '/' + os.path.basename(curUrl),
                                  PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf")
                        file = open(PATH + '/' + os.path.basename(curUrl), 'wb')
                        file.write(current.read())
                        file.close()
                        os.rename(PATH + '/' + os.path.basename(curUrl),
                                  PATH + '/' + os.path.basename(curUrl)[0:tempIndex] + '_' + str(count) + '.pdf')
                        os.rename(PATH + '/' + "temp_afl2382fa98fhlap1r0912eg23.pdf",
                                  PATH + '/' + os.path.basename(curUrl))
                        return
                    except:
                        return
        else:
            print('Too many files of the same name!')
            print('If this is a problem and you need for the downloader to download more than 1000 files of the same name,')
            print('you can email me at alanchung2000@gmail.com and I\'ll help you resolve the issue.' )
            return

# Find all hyper-references, and run the helper method on these links (pdf's)
for tag in soup.findAll('a', href = True):
    curUrl = urllib.parse.urljoin(url, tag['href']).strip()
    # Check the hyper-reference is a pdf file
    try:
        if os.path.splitext(os.path.basename(curUrl))[1] == '.pdf':
            print(curUrl)
            cur = urllib.request.urlopen(curUrl)
            print("\n[*] Downloading: %s" %(os.path.basename(curUrl)))
            temp = tag.findAll(text=True)[0]
            exists(curUrl, cur, temp)
    except:
        continue