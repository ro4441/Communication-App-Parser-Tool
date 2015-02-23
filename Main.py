#!/usr/bin/python
import sqlite3
import hashlib
import csv
import sys
import argparse
import os
import glob


def menu (menu):
  menu = {}
  menu['1']="Combine database."
  menu['2']="Convert to CSV."
  menu['3']="Parse."
  menu['4']="Hash Checker."
  menu['5']="Exit."
  while True:
    options=list(menu.keys())
    options.sort()
    for entry in options:
        print (entry, menu[entry])
    selection= input("Please Select:")
    if selection =='1':
        print ("\nDatabases combined")
        combine ("1stcall")
    elif selection == '2':
          print ("\nWhich DBs do you want to convert to CSV")
          convert ()
    elif selection == '3':
          print ("\nWhich CSV do you want to Parse")
          Parses()
    elif selection == '4':
          print ("\nWhich Database do you want to check")
          Hashmenu(Hashmenu)
    elif selection == '5':
      break
    else:
        print ("Unknown Option Selected!")

###########################HASH SUB MENU################################
def Hashmenu (Hashmenu):
  Hashmenu = {}
  Hashmenu['1']="Hash Facebook database."
  Hashmenu['2']="Hash Kik messenger database."
  Hashmenu['3']="Hash Sms database."
  Hashmenu['4']="Hash Whatsapp database."
  Hashmenu['5']="Hash All."
  Hashmenu['6']="Back."
  while True:
    options=list(Hashmenu.keys())
    options.sort()
    for entry in options:
        print (entry, Hashmenu[entry])
    selection= input("Please Select:")
    if selection =='1':
         HashFB()
         print ("\n")
    elif selection == '2':
          HashKik ()
          print ("\n")
    elif selection == '3':
          HashSms()
          print ("\n")
    elif selection == '4':
          HashWApp()
          print ("\n")
    elif selection == '5':
          HashFB()
          HashKik ()
          HashSms()
          HashWApp()
          print ("\n")
    elif selection == '6':
          menu (menu)
    else:
        print ("Unknown Option Selected!")
############Hash############
def HashKik():
    try:
        print ('kik database:     ', hashlib.md5(open('kikDatabase.db', 'rb').read()).hexdigest())
    except: print ('Database does not exist')
def HashWApp():
    try:
        print ('Whatsapp database:',hashlib.md5(open('msgstore.db', 'rb').read()).hexdigest())
    except: print ('Database does not exist')
def HashSms():
    try:
        print ('SMS database:     ',hashlib.md5(open('sms.mbp', 'rb').read()).hexdigest())
    except: print ('Database does not exist')
def HashFB():
    try:
        print ('Facebook database:',hashlib.md5(open('threads_db2.db', 'rb').read()).hexdigest())
    except: print ('Database does not exist')

##########################DATABASE CONNECTIONS##################################
def combine(old_db):
#############Whatsapp###############
    combined_db = sqlite3.connect('combined.db') # open combined database
    old_db = sqlite3.connect('msgstore.db') # open whatsapp database
    query = "".join(line for line in old_db.iterdump()) # for every line in whatsapp db
    try:
        combined_db.executescript(query) #try to add Whatsapp db to combined
    except:
        print("Cant connect msgstore.db") #otherwise print cant connect
    combined_db.close() # close db
    old_db.close()

    ##Repeat process for each database to connect##
    ##########KikMessenger##########
    combined_db = sqlite3.connect('combined.db')
    old_db = sqlite3.connect('kikDatabase.db')
    query = "".join(line for line in old_db.iterdump())
    try:
        combined_db.executescript(query)
    except:
        print("Cant connect KikDatabase.db")
    combined_db.close()
    old_db.close()

    ###############Sms##############
    combined_db = sqlite3.connect('combined.db')
    old_db = sqlite3.connect('sms.mbp')
    query = "".join(line for line in old_db.iterdump())
    try:
        combined_db.executescript(query)
    except:
        print("Cant connect sms.mbp")
    combined_db.close()
    old_db.close()

    #######FacebookMessenger########
    combined_db = sqlite3.connect('combined.db')
    old_db = sqlite3.connect('threads_db2.db')
    query = "".join(line for line in old_db.iterdump())
    try:
        combined_db.executescript(query)
    except:
        print("Cant connect Threads_db2.db")
    combined_db.close()
    old_db.close()

############################CONVERT MENU CONVERT#################################
def convert():
  def Cmenu(Cmenu):
     Cmenu = {}
     Cmenu['1']="Convert Combined."
     Cmenu['2']="Convert Facebook Messenger."
     Cmenu['3']="Convert Kik Messenger."
     Cmenu['4']="Convert SMS."
     Cmenu['5']="Convert Whatsapp."
     Cmenu['6']="Convert all."
     Cmenu['7']="CLEAR ALL CSV FILES."
     Cmenu['8']="Back."
     while True:
        options=list(Cmenu.keys())
        options.sort()
        for entry in options:
            print (entry, Cmenu[entry])
        selection=input("Please Select:")
        Cant = ('can not convert\n')
        Can = ("converted \n")
        if selection =='1':
            try:
                cAll()
                print (Can)
            except:
              print (Cant)
        elif selection == '2':
            try:
                cFB()
                print (Can)
            except:
              print (Cant)
        elif selection == '3':
            try:
                cKik()
                print (Can)
            except:
              print (Cant)
        elif selection == '4':
            try:
                cSms()
                print (Can)
            except:
               print (Cant)
        elif selection == '5':
            try:
               cWApp()
               print (Can)
            except:
              print (Cant)
        elif selection == '6':
            try:
              cAll()
              cKik()
              cFB()
              cWApp()
              cSms()
              print ("converted all to CSV \n")
            except:
              print (Cant)
        elif selection == '7':
            try:
              Prompt()
            except:
              print ("Cant clear")
        elif selection == '8':
          print ("\n")
          menu(menu)
          break
        else:
            print ("Unknown Option Selected!")
  #######ClearALL+Prompt########
  def Prompt():
    # http://stackoverflow.com/questions/12277864/python-clear-csv-file
      print ("/nAre you sure? please type either")
      Prompt = {}
      Prompt['y']="= yes"
      Prompt['n']="= no"
      while True:
        options=list(Prompt.keys())
        options.sort()
        for entry in options:
            print (entry, Prompt[entry])
        selection= input("Please Select:")
        if selection =='y':
              C = open("OutSms.csv", "w+")
              C = open("OutFB.csv", "w+")
              C = open("OutKik.csv", "w+")
              C = open("out.csv", "w+")
              C = open("OutWhatsapp.csv", "w+")
              C.close()
              print ("Cleared all CSVs \n")
              Cmenu(Cmenu)
        elif selection == 'n':
              Cmenu(Cmenu)
        else:
            print ("Unknown Option Selected!")
  ###########Convert All###########
  def cAll():
    #create in write 'out.csv' file in utf8 to allow emojis
    with open("out.csv", "w", encoding= 'utf8') as csv_file:
        combined_db = sqlite3.connect('combined.db') # open combined database
        cursor = combined_db.cursor()
        try:  #try and select certain columns from tables in combined.db. cursor parameters
            cursor.execute('select body, messagesTable.timestamp, was_me, data, messages.timestamp, key_from_me from messagesTable, messages')
        except:
            print("No such table")
            sys.exit(-1)
    #split fields with ',' and end of line with new line '\n'
        csv_writer = csv.writer(csv_file,delimiter=',', lineterminator='\n')
        csv_writer.writerow([i[0] for i in cursor.description]) # write header row
        try:
            csv_writer.writerows(cursor) #write rows, parameters of cursor
            print ("\n")
        except:
            print ("unable to convert")
        combined_db.close() #close db
  #########Convert Facebook#########
  def cFB():
    with open("OutFB.csv", "w", encoding= 'utf8') as csv_file:
        FB = sqlite3.connect('threads_db2.db')
        cursor = FB.cursor()
        try:
            cursor.execute('select text, sender, timestamp_ms from messages')
        except:
            print("No such table")
            sys.exit(-1)
        csv_writer = csv.writer(csv_file,delimiter=',', lineterminator='\n')
        csv_writer.writerow([i[0] for i in cursor.description])
        try:
            csv_writer.writerows(cursor)
        except:
            print ("unable to convert")
        FB.close()
  ########Convert Kik Messenger########
  def cKik():
    with open("OutKik.csv", "w", encoding= 'utf8') as csv_file:
        Kik = sqlite3.connect('kikDatabase.db')
        cursor = Kik.cursor()
        try:
            cursor.execute('select partner_jid, was_me, body, timestamp from messagesTable')
        except:
            print("No such table")
            sys.exit(-1)
        csv_writer = csv.writer(csv_file,delimiter=',', lineterminator='\n')
        csv_writer.writerow([i[0] for i in cursor.description])
        try:
            csv_writer.writerows(cursor)
        except:
            print ("unable to convert")
        Kik.close()
  #############Convert Sms#############
  def cSms():
    with open("OutSms.csv", "w", encoding= 'utf8') as csv_file:
        Sms = sqlite3.connect('sms.mbp')
        cursor = Sms.cursor()
        try:
            cursor.execute('select address, body, date from sms')
        except:
            print("No such table")
            sys.exit(-1)
        csv_writer = csv.writer(csv_file,delimiter=',', lineterminator='\n')
        csv_writer.writerow([i[0] for i in cursor.description])
        try:
            csv_writer.writerows(cursor)
        except:
            print ("unable to convert")
        Sms.close()
  #############Convert Whatsapp###########
  def cWApp():
    with open("OutWhatsapp.csv", "w", encoding= 'utf8') as csv_file:
        WApp = sqlite3.connect('msgstore.db')
        cursor = WApp.cursor()
        try:
            cursor.execute('select key_remote_jid, key_from_me, data, timestamp from messages')
        except:
            print("No such table")
            sys.exit(-1)
        csv_writer = csv.writer(csv_file,delimiter=',', lineterminator='\n')
        csv_writer.writerow([i[0] for i in cursor.description])
        try:
            csv_writer.writerows(cursor)
        except:
            print ("unable to convert")
        WApp.close()
  Cmenu("firstCall");
#############################SUB MENU PARSE###############################
def Parses():
    def Submenu (Submenu):
      Submenu = {}
      Submenu['1']="Parse all."
      Submenu['2']="Parse Facebook Messenger."
      Submenu['3']="Parse Kik Messenger."
      Submenu['4']="Parse SMS."
      Submenu['5']="Parse Whatsapp."
      Submenu['6']="Back."
      while True:
        options=list(Submenu.keys())
        options.sort()
        for entry in options:
            print (entry, Submenu[entry])

        selection= input("Please Select:")
        if selection =='1':
            try:
                process_interactive("out.csv")
                Submenu (Submenu)
            except:
                print ("no out.csv\n")
        elif selection == '2':
            try:
                process_interactive("OutFB.csv")
                Submenu (Submenu)
            except:
                print ("no OutFB.csv\n")
        elif selection == '3':
            try:
                process_interactive("OutKik.csv")
                Submenu (Submenu)
            except:
                print ("no outkik.csv\n")
        elif selection == '4':
            try:
                process_interactive("OutSms.csv")
                Submenu (Submenu)
            except:
              print ("no Sms.csv\n")
        elif selection == '5':
            try:
                process_interactive("OutWhatsapp.csv")
                Submenu (Submenu)
            except:
              print ("no OutWhatsapp.csv\n")
        elif selection == '6':
          print ("\n")
          menu(menu)
          break
        else:
            print ("Unknown Option Selected!")

###############################PARSE CSV###################################
    #############Open CSVs############
    # expand each directory using generator into list of *.csv files inside of it
    # return index of file and it's path
    def get_files(args):
        index = 0
        for path in args.files:
            if os.path.isdir(path):
                # if the file is an existing directory
                # try to exapnd all *.csv files inside of it
                for f in glob.glob(os.path.join(path, "*.csv")):
                    yield index,f
                    index += 1
            else:
                # regular file just return the path
                yield index,path
                index += 1

    #########Timestamp Arguments########
    def get_timestamp_range(args):
        # timestamp could be specified using the following string
        # xxx-yyy xxx- -yyy
        # extract xxx and yyy parts of the string
        start, end = args.timestamp.split("-")[:2]
        def convert(s):
            if s == "":
                return None
            else:
                return int(s)
       # convert xxx and yyy parts into int or None in case
        # of xxx- or -yyy
        return (convert(start), convert(end))
    #########################
    # process single csv file
    def process_csv(index, path, data, timestamp):
        with open(path) as f:
            csv_reader = csv.reader(f, delimiter=',', quotechar='"')
            csv_writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')
            # read the headers first line
            headers = csv_reader.__next__()
            if index == 0:
                # for the first file write the headers
                csv_writer.writerow(headers)
            # read the second line
            test_line = csv_reader.__next__()
            if index == 0:
                # for the first file print the second line
                csv_writer.writerow(test_line)
            # find the index of timestamp and data inside the
            # headers array
            timestamp_index = -1
            try:
                timestamp_index = headers.index("timestamp")
            except:
                pass
            data_index = -1
            try:
                data_index = headers.index("data")
            except:
                pass
            for d in csv_reader:
                if data != None:
                    if data_index != -1 and data not in d[data_index]:
                        # if we have data filter specified and the data field
                        # doesn't contain the requested string continue 
                        continue
                    else:
                        # if we have data filter specified and filter word not in fields continue
                        if not any(data in e for e in d):
                            continue
 ###############                         
                # if timestamp is specified and timestamp field is before the start timestamp continue
                if data_index != -1 and timestamp[0] is not None and int(d[timestamp_index]) < timestamp[0]:
                    continue
                # if end timestamp is specified and timestamp field is after the end timestamp continue
                if data_index != -1 and timestamp[1] is not None and int(d[timestamp_index]) > timestamp[1]:
                    continue
                # if we didn't filter the line write it
                csv_writer.writerow(d)
    #############Input Arguments############
    def process_interactive(file_path):
        try:
            while True:
                data = input("Enter data to search [Enter to leave it blank]: ").strip()
                if data == "":
                    data = None
                timestamp = input("Enter Unix timestamp to search in the format of xxx-yyy or xxx- [Enter to leave it blank]: ").strip()
                if timestamp == "":
                    timestamp = "-"
                try:
                    class DummyArgs(object):
                        pass
                    args = DummyArgs()
                    args.timestamp = timestamp
                    timestamp = get_timestamp_range(args)
                except:
                    print ("Error: invalid timestamp range %s, should be xxx-yyy or xxx- or yyy-" % timestamp)
                    continue
                
###############
                try:
                    process_csv(0, file_path, data, timestamp)
                except:
                    import traceback
                    traceback.print_exc()
                    raise
################                  
                if timestamp[0] != None or timestamp[1] != None:
                    print ("\n\nTIMESTAMP RANGE %s-%s" % (timestamp[0] if timestamp[0] != None else "",
                                                         timestamp[1] if timestamp[1] != None else ""))
                print ("\n")
                Submenu (Submenu)
        except KeyboardInterrupt:
            pass
    Submenu ("1st call");
menu ("1st call");
