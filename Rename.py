import os
import zipfile
from time import gmtime, strftime, sleep
from shutil import move

#py -3.4 -m py2exe.build_exe myscript.py
f = open("Config.txt", "r+")
siteid = f.read(4)


def prev_day(hour):

    if hour[2:] == '00':
        pd = str(int(hour[:2])-1) + '12'
    if hour[2:] == '12':
        pd = hour[:2] + '00'
    return pd

def clean():
    if not (hour[2:] == '00' or hour[2:] == '12'):
        print('Cleaning not complete because this is a non-synoptic flight.  The files will have to be manually organized.')
        return
    pd = prev_day(hour)
    prev_flight = int(flightnum)-1
    prev_flight = str(prev_flight)
    if not os.path.exists("C:\Win9000 Messages\Ascensions/"+str(prev_flight)):
        os.makedirs("C:\Win9000 Messages\Ascensions/"+str(prev_flight))
    
    print("Cleaning previous entries...")
    
    for i in os.listdir(os.getcwd()):
        if prev_flight in i:
            try:
                move(i, "C:\Win9000 Messages\Ascensions/"+str(prev_flight)+"/"+i)
            except:
                print('Error occured in moving ABV, MAN, SGL, or FZL to Ascensions folder')
                pass
        if pd in i:
            try:
                move(i, "C:\Win9000 Messages\Ascensions/"+str(prev_flight)+"/"+i)
            except:
                print('Error occured in moving archive to Ascensions folder')
                pass
        else:
            continue
    sleep(5)
    print("Cleaning Complete.")


def clean2():
    if not (hour[2:] == '00' or hour[2:] == '12'):
        print('Cleaning not complete because this is a non-synoptic flight.  The files will have to be manually organized.')
        return
    pd = prev_day(hour)
    for i in os.listdir(os.getcwd()):
        print(i)
        if flightnum not in i and i[:3] == "RRS":
            A = i[7:10]
            if not os.path.exists("C:\Win9000 Messages\Ascensions/" + str(A)):
                os.makedirs("C:\Win9000 Messages\Ascensions/" + str(A))
            try:
                move(i, "C:\Win9000 Messages\Ascensions/" + str(A) + "/" + i)
            except:
                print('Error occured in moving ABV, MAN, SGL, or FZL to Ascensions folder')
                pass
        if flightnum not in i and i[4:7] == "RWS":
            A = i[:3]
            if not os.path.exists("C:\Win9000 Messages\Ascensions/" + str(A)):
                os.makedirs("C:\Win9000 Messages\Ascensions/" + str(A))
            try:
                move(i, "C:\Win9000 Messages\Ascensions/" + str(A) + "/" + i)
            except:
                print('Error occured in moving ABV, MAN, SGL, or FZL to Ascensions folder')
                pass
        if flightnum not in i and (i[:1]=="H" or i[:1]=="T"):
            A = i[1:4]
            try:
                move(i, "C:\Win9000 Messages\Ascensions/" + str(A) + "/" + i)
            except:
                print('Error occured in moving ABV, MAN, SGL, or FZL to Ascensions folder')
                pass
        if pd in i:
            try:
                move(i, "C:\Win9000 Messages\Ascensions/" + str(A) + "/" + i)
            except:
                print('Error occured in moving archive to Ascensions folder')
                pass
        else:
            continue
    sleep(5)
    print("Cleaning Complete.")

def NCEI_Archive(Zip):
    os.chdir("C:\Win9000 Messages\Archive")
    b = strftime(siteid+ "%y%m", gmtime())
    if not os.path.isfile("C:\Win9000 Messages\Ascensions/Archive/"+b+".zip"):
        mz = zipfile.ZipFile(b+".zip", "w")
        os.chdir("C:\Win9000 Messages")
        mz.write(Zip)
        mz.close()
    else:
        mz = zipfile.ZipFile(b+".zip", "a")
        os.chdir("C:\Win9000 Messages")
        mz.write(Zip)
        mz.close()
    os.chdir("C:\Win9000 Messages")

def NCEI_Archive2(data):
    os.chdir("C:\Win9000 Messages\Archive")
    b = strftime(siteid+ "%y%m", gmtime())
    if not os.path.isfile("C:\Win9000 Messages\Archive/"+b+".zip"):
        mz = zipfile.ZipFile(b+".zip", "w")
        os.chdir("C:\Win9000 Messages")
        try:
            mz.write(data)
        except:
            pass
        mz.close()
        print("Creating Zip archive file.")
    else:
        mz = zipfile.ZipFile(b+".zip", "a")
        os.chdir("C:\Win9000 Messages")
        try:
            mz.write(data)
        except:
            pass
        mz.close()
        print("Appending archive data to the monthly zip file.") 
    os.chdir("C:\Win9000 Messages")


print("This program renames and organizes TROS files for tranmission to NCEP and NCEI.  Type help for help.")
flightnum = input("What ascension number would you like to transmit?")
ascnum = input("What release number would you like to transmit?")
hour = input("What is the date and synoptic hour of the flight (Format DDHH)")



if not os.path.exists("C:\Win9000 Messages\Ascensions/"+flightnum):
    os.makedirs("C:\Win9000 Messages\Ascensions/"+flightnum)

if not os.path.exists("C:\Win9000 Messages\Archive"):
    os.makedirs("C:\Win9000 Messages\Archive")

if flightnum == "help":
    f = open("C:/Win9000_TROS_Install/TROS_FileName_V1.07/NCEI Rename Readme.txt", 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

os.chdir("C:\Win9000 Messages")

a = strftime(siteid+ "%y%m", gmtime())
a = a+hour+".zip"
z = zipfile.ZipFile(a, "w")

clean2()

for i in os.listdir(os.getcwd()):
    if (flightnum+"_H") in i:
        try:
            print("Identified H File, renaming..."+i)
            data = "H"+flightnum
            os.rename(i,data)
            z.write(data)
            NCEI_Archive2(data)
            print(data)
        except:
            print("Encountered an Error While Zipping H file")
            pass

for i in os.listdir(os.getcwd()):
    if (flightnum+"_T") in i:
        try:
            print("Identified T File, renaming..."+i)
            data="T"+flightnum
            os.rename(i,data)
            z.write(data)
            z.close
            NCEI_Archive2(data)
            print(data)
        except:
            print("Encountered an Error While Zipping T file")
            pass


msglist = ["SGL","MAN","RADAT","ABV"]
regenlist = ["A.", "B.", "C.", "D.", "E."]
for k in msglist:
    c = 0
    for i in os.listdir(os.getcwd()):
        if "RRS" in i and k in i and flightnum in i:
            c = c + 1
            print("Identified previously generated messages for the " + k + " level")
            print("The next generation will have a " + regenlist[c]+" in the filename.")
            sleep(0.5)
    for i in os.listdir(os.getcwd()):
        if flightnum in i and ("_"+k) in i:
            print("Identified "+k+ " File, renaming..."+i)
            sleep(0.5)
            move(i,"RRS"+siteid[1:4]+ascnum+flightnum+regenlist[c]+k)

for i in os.listdir(os.getcwd()):
    if flightnum in i and '.RADAT' in i:
        print(i)
        move(i, i[:-6]+".FZL")
        continue
    else:
        continue

z.close()
f.close
print('All requested operations have been completed, please proceed by transmitting the files via SFTP\
.  You may now close the program.')
sleep(15)
# def upload(FNum):
#     host = ""
#     port = 22
#     transport = paramiko.Transport((host, port))
#     msglist = ["ABV","MAN","FZL","SGL"]
#     password=""
#     username=""
#     transport.connect(username = username, password = password)
#
#     sftp = paramiko.SFTPClient.from_transport(transport)
#
#
#     for i in msglist:
#         YoN = input("Would you like to transmit the " + i + " message? (Y or N)")
#         if YoN == "Y":
#             for filenames in os.listdir("C:\Win9000 Messages"):
#                 if flightnum in filenames and i in filenames:
#                     filepath = 'C:\Win9000 Messages/'+filenames
#                     localpath = '/home/RRS/data/Incoming/'+filenames
#                     print(filepath)
#                     print(localpath)
#                     sftp.put(filepath, localpath)
#                     print("Successfully uploaded file " + filenames + " to " + host)
#         else:
#             continue
#
#
#     sftp.close()
#     transport.close()
#
#
# TransmitQ = input("Would you like to transmit messages now? Y/N")
# if TransmitQ == "Y":
#     upload(flightnum)
