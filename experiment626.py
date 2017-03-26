#! /usr/bin/env python
# -*- encoding: utf8 -*-
#This makes possible to run this program as a script invoking the interpreter

#########################
##     HEADER INFO     ##
#########################

__author__ = "Kike Puma"
__copyright__ = "Copyright 2007, CosasDePuma"
__credits__ = ["KikePuma", "CosasDePuma"]
__license__ = "GNU-3.0"
__version__ = "2.0.1 Travis Build"
__maintainer__ = "KikePuma"
__email__ = "kikefontanlorenzo@gmail.com"
__status__ = "First Travis Build"

########################
##     CHECK ROOT     ##
########################
import os
import sys

if not os.geteuid() == 0:
    sys.exit("\033[0;31mYou need to have root privileges to run this program.\nPlease try again, this time using 'sudo'. Exiting.\033[0m")

########################
##       COLORS       ##
########################

#Color change: "\033[cod_formato;cod_texto;cod_fondom"
ERROR = "\n\033[1;31m" #BOLD RED
POSITIVE = "\033[1;32m" #GREEN
NEUTRAL = "\033[1;37m" #WHITE
NEGATIVE = "\033[1;31m" #RED
STITCH = "\033[1;34m" #BLUE
DEFAULT = "\033[0m" #DEFAULT COLOR
CREDITS = "\033[2;37m" #LIGHT WHITE

#######################
##       BANNER      ##
#######################

banner = STITCH + '''  ______                      _                      _   
 |  ____|                    (_)                    | |  
 | |__  __  ___ __   ___ _ __ _ _ __ ___   ___ _ __ | |_ 
 |  __| \ \/ / '_ \ / _ \ '__| | '_ ` _ \ / _ \ '_ \| __|
 | |____ >  <| |_) |  __/ |  | | | | | | |  __/ | | | |_ 
 |______/_/\_\ .__/ \___|_|_ |_|_| |_| |_|\___|_| |_|\__|
             | |     / /|__ \ / /
             |_|    / /_   ) / /_
                   | '_ \ / / '_ \ 
                   | ( ) / /| ( ) |
                    \___/____\___/

''' + NEUTRAL + '''[TIMELINE]: \n'''

stitch = STITCH + '''                                                      ````   
                                                     ......  
                                                     ........ 
                                                    ......... 
                                                  `......... 
                           -/+::--..`             -......... 
                        /yysssssssyyo:.          :-.......-` 
  ...``               `/ssssyyyyssssy:://-     /y.........  
 `......`           +hysssyhdmmdhyy+:mom//  .oso........   
  ........`        .o/+yysymNNNNmdhy++MMMso+-ysh+/-....     
   `-.......`      //sy++yhhhddhhyhds+mds+ysysysso+:::`     
   ..........-`    /symMd+yddyyyyyNyssssysyyyyhyyyo/.       
   `..........os/- o/dNNmosydmhyhhyyoohsdy+s:---.           
     ........-/syssyso++oyysysyomy/yosmos:.                 
      `......:ossyyyysyyyys::`--:.`.--/:`                   
        `..--/syyyyhsss+//:------::/+ssy+`                  
            ..---..`   `./ssss::/:::+sysss/-                
                      `:sssyys::/::::yyyyyssyo.             
                   `/syssyyyy+:://:+oyysssssssy             
                   osssssssssyo/:::ysssssssssss             
                   :ysssssssssso::yyyyyysssss/`             
                    .oyssssyyyyho:myhyosys-.                
                      `-/ys:yhmoo::/oo+:yy-                 
                       -syo:o+/:::::::::yyso-               
                     -osssy/:::::::::::/ysssso.             
                   .osssssss+:::::::::/sssssssy/            
                   yssssssssyyo+//++osysssssssss:           
                  -hysssssss+--:::::-.-/sssssyyyh:          
                  oMhdysydyy            oymhyhmyy`          
                   .:so/+o-              ./:-.-`            '''

stitchSad = STITCH + '''                                                      ````   
                                                     ......  
                                                     ........ 
                                                    ......... 
                                                  `......... 
                           -/+::--..`             -......... 
                        /yysssssssyyo:.          :-.......-` 
  ...``               `/ssssyyyyssssy:://-     /y.........  
 `......`           +hysssyhdmmdhyy+:mom//  .oso........   
  ........`        .o/+yysymNNNNmdhy++MMMso+-ysh+/-....     
   `-.......`      //sy++yhhhd   yhds+mds+ysysysso+:::`     
   ..........-`    /symMd+ydd     Nyssssysyyyyhyyyo/.       
   `..........os/- o/dNNmosy        yoohsdy+s:--.           
     ........-/syssyso++oyysy      yosmos:.                 
      `......:ossyyyysyyyys::yyyyyy::-/:`                   
        `..--/syyyyhsss+//:------::/+ssy+`                  
            ..---..`   `./ssss::/:::+sysss/-                
                      `:sssyys::/::::yyyyyssyo.             
                   `/syssyyyy+:://:+oyysssssssy             
                   osssssssssyo/:::ysssssssssss             
                   :ysssssssssso::yyyyyysssss/`             
                    .oyssssyyyyho:myhyosys-.                
                      `-/ys:yhmoo::/oo+:yy-                 
                       -syo:o+/:::::::::yyso-               
                     -osssy/:::::::::::/ysssso.             
                   .osssssss+:::::::::/sssssssy/            
                   yssssssssyyo+//++osysssssssss:           
                  -hysssssss+--:::::-.-/sssssyyyh:          
                  oMhdysydyy            oymhyhmyy`          
                   .:so/+o-              ./:-.-`            '''

stitchLove2 = STITCH + '''                                                      ````   
                                                     ......  
                                                     ........ 
''' + NEGATIVE + '''           _ _ ''' + STITCH + '''                                     ......... 
''' + NEGATIVE + '''          ( v )''' + STITCH + '''                                   `......... 
''' + NEGATIVE + '''           \ / ''' + STITCH + '''            -/+::--..`             -......... 
''' + NEGATIVE + '''            '  ''' + STITCH + '''         /yysssssssyyo:.          :-.......-` 
  ...``     ''' + NEGATIVE + '''  ( v )''' + STITCH + '''   `/ssssyyyyssssy:://-     /y.........  
 `......`   ''' + NEGATIVE + '''   \ / ''' + STITCH + ''' +hysssyhdmmdhyy+:mom//  .oso........   
  ........`        .o/+yysymNNNNmdhy++MMMso+-ysh+/-....     
   `-.......`      //sy++yhhhddhhyhds+mds+ysysysso+:::`     
   ..........-`    /symMd+yddyyyyyNyssssysyyyyhyyyo/.       
   `..........os/- o/dNNmosydmhyhhyyoohsdy+s:---.           
     ........-/syssyso++oyysysyomy/yosmos:.                 
      `......:ossyyyysyyyys::`--:.`.--/:`                   
        `..--/syyyyhsss+//:------::/+ssy+`                  
            ..---..`   `./ssss::/:::+sysss/-                
                      `:sssyys::/::::yyyyyssyo.             
                   `/syssyyyy+:://:+oyysssssssy             
                   osssssssssyo/:::ysssssssssss             
                   :ysssssssssso::yyyyyysssss/`             
                    .oyssssyyyyho:myhyosys-.                
                      `-/ys:yhmoo::/oo+:yy-                 
                       -syo:o+/:::::::::yyso-               
                     -osssy/:::::::::::/ysssso.             
                   .osssssss+:::::::::/sssssssy/            
                   yssssssssyyo+//++osysssssssss:           
                  -hysssssss+--:::::-.-/sssssyyyh:          
                  oMhdysydyy            oymhyhmyy`          
                   .:so/+o-              ./:-.-`            '''

stitchLove1 = STITCH + '''                                                      ````   
                                                     ......  
''' + NEGATIVE + '''        _ _ ''' + STITCH + '''                                         ........ 
''' + NEGATIVE + '''       ( v )''' + STITCH + '''                                        ......... 
''' + NEGATIVE + '''        \ / ''' + STITCH + '''                                      `......... 
''' + NEGATIVE + '''         '  ''' + STITCH + '''               -/+::--..`             -......... 
                        /yysssssssyyo:.          :-.......-` 
  ...``               `/ssssyyyyssssy:://-     /y.........  
 `......`           +hysssyhdmmdhyy+:mom//  .oso........   
  ........`        .o/+yysymNNNNmdhy++MMMso+-ysh+/-....     
   `-.......`      //sy++yhhhddhhyhds+mds+ysysysso+:::`     
   ..........-`    /symMd+yddyyyyyNyssssysyyyyhyyyo/.       
   `..........os/- o/dNNmosydmhyhhyyoohsdy+s:---.           
     ........-/syssyso++oyysysyomy/yosmos:.                 
      `......:ossyyyysyyyys::`--:.`.--/:`                   
        `..--/syyyyhsss+//:------::/+ssy+`                  
            ..---..`   `./ssss::/:::+sysss/-                
                      `:sssyys::/::::yyyyyssyo.             
                   `/syssyyyy+:://:+oyysssssssy             
                   osssssssssyo/:::ysssssssssss             
                   :ysssssssssso::yyyyyysssss/`             
                    .oyssssyyyyho:myhyosys-.                
                      `-/ys:yhmoo::/oo+:yy-                 
                       -syo:o+/:::::::::yyso-               
                     -osssy/:::::::::::/ysssso.             
                   .osssssss+:::::::::/sssssssy/            
                   yssssssssyyo+//++osysssssssss:           
                  -hysssssss+--:::::-.-/sssssyyyh:          
                  oMhdysydyy            oymhyhmyy`          
                   .:so/+o-              ./:-.-`            '''

########################
##       PROGRAM      ##
########################

#Libraries and APIs
import time #System Threading
import tweepy #API Twitter
import codecs #Text Encoder
import requests #HTTP Requests
import demjson #JSON Decoder
import argparse #Argument Parser

#Set default encoding UTF-8
reload(sys)
sys.setdefaultencoding('utf8')

#Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("keywords", metavar="keywords", type=str, nargs='+', help="keywords to filter tweets")
parser.add_argument("-c", "--colored", help="color according to the feelings (verbose required)", action="store_true")
parser.add_argument("-d", "--database", help="Connect to MongoDB and store the data in the collection 'experiment626_'") 
parser.add_argument("-l", "--language", choices=('en','es'), default='es', help="set the analyzed text language")
parser.add_argument("-f", "--feelings", help="show the feeling polarity in the text (verbose required)", action="store_true")
parser.add_argument("-i", "--irony", help="indicates the irony of the text (verbose required)", action="store_true")
parser.add_argument("-s", "--subjectivity", help="marks the subjectivity of the text (verbose required)", action="store_true")
parser.add_argument("-p", "--persistence", help="don't delete the MongoDB Collection.", action="store_true")
parser.add_argument("-v", "--verbose", help="verbose, hide the banner", action="store_true")
parser.add_argument("--version", help="show the version", action="store_true")
args = parser.parse_args()

#TwitterApp Keys and Access Tokens
consumerKey = ''
consumerSecret = ''
accessToken = ''
accessSecret = ''

#Show the version
if args.version:
    print STITCH + "Experiment 626\n" + NEUTRAL + __version__ + " " + __status__ + CREDITS + "\nCreated by KikePuma 2017 (https://github.com/KikePuma)" + DEFAULT #Credits
    sys.exit(0)

#MongoDB Connection (MongoLab Used)
if args.database:
    from pymongo import MongoClient #API MongoDB
    try:
        uri = args.database
        client = MongoClient(uri)
        db = client.get_default_database()
        collection_name = 'experiment626_'
        collection = db[collection_name]
    except:
        print ERROR + "[ERROR] Bad MongoDB Config or URI\n"
        sys.exit(0xDEAD)

#MeaningCloud Key & Config
meaningCloudKey = ''
meaningCloudLang = args.language #Default: Spanish

#Extend the class streamListener
class spoutModule(tweepy.StreamListener):
    def on_status(self, status):
        if not hasattr(status, 'retweeted_status'): #Ignore retweets
            meaning = meaningCloud(status.text.encode('utf-8'),'DEBUG') #Meaning Procesing

            #Print Banner if Verbose Mode is off
            if not args.verbose:
                if meaning['score_tag'] == "P+":
                    cls()
                    print stitchLove2 
		elif meaning['score_tag'] == "P":
                    cls()
                    print stitchLove1
                elif meaning['score_tag'] == "NEU" or meaning['score_tag'] == "NONE":
                    cls()
                    print stitch
                elif meaning['score_tag'] == "N" or meaning['score_tag'] == "N+":
                    cls()
                    print stitchSad
            else:
                consoleLine =  status.user.name + " (@" + status.user.screen_name + ") <> " + status.text.encode('utf-8') + DEFAULT
                data = ""
                #MEANING ARGS
                if args.subjectivity:
                    data = "[" + meaning['subjectivity'] + "]" + data
                if args.irony:
        	    data = "[" + meaning['irony'] + "]" + data
                if args.feelings:
                    data = "[" + meaning['score_tag'] + "]" + data
                #SET THE DATA
                if data != "":
                    consoleLine = data + " " + consoleLine
                #COLOR ARGS
                if args.colored:
                    if meaning['score_tag'] == "P+" or meaning['score_tag'] == "P":
                        consoleLine = POSITIVE + consoleLine #Print the tweet in White
                    elif meaning['score_tag'] == "NEU" or meaning['score_tag'] == "NONE":
                        consoleLine = NEUTRAL + consoleLine #Print the Tweet in White
                    elif meaning['score_tag'] == "N" or meaning['score_tag'] == "N+":
                        consoleLine = NEGATIVE + consoleLine #Print the Tweet in Red
                else:
                    consoleLine = DEFAULT + consoleLine #Print the tweet in UTF-8
                print consoleLine

            if args.database:
                #Create Tweet Information in JSON
                tweet = {
                        "feeling": meaning['score_tag'],
                        "irony": meaning['irony'],
                        "subjectivity": meaning['subjectivity'],
                        "tweet":
                        {
                            "text": status.text.encode('utf-8'),
                            "url": "https://twitter.com/" + status.user.screen_name + "/status/" + str(status.id),
                            "user": status.user.name
                        }
                        };
                #Insert the tweet info in the Collection
                collection.insert_one(tweet)

    def on_error(self, status_code):
        if status_code == 420:
            print ERROR + "[ERROR] Connection refused. Max number of tries. Please wait and try again" + DEFAULT
        elif status_code == 401:
            print ERROR + "[ERROR] Wrong credentials" + DEFAULT
        else:
            print ERROR + "[ERROR] Unknown Error" + DEFAULT
        #Return: True dont' stop the program, False stop it
        return False

    def on_timeout(self):
        print ERROR + '[ERROR] Timeout...' + DEFAULT
        return False

#Define a function that make a HTTP request
def meaningCloud(tweet,textMode):
    url = "http://api.meaningcloud.com/sentiment-2.1"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = "key=" + meaningCloudKey + "&lang=" + meaningCloudLang + "&txt=" + tweet + "&model="

    response = requests.request("POST", url, data=payload, headers=headers)
    if textMode == 'JSON': #Return the response in RAW format
        return response

    decoded = demjson.decode(response.text) #Decode from JSON to Python
    if textMode == 'ALL': #Return the full response
        return decoded
    #Debugger
    meaningCloudStatus = decoded['status']['code']; #Get the status response code
    if meaningCloudStatus == '104':
        print ERROR + "[ERROR] You have exceeded the request limit. Waiting 5 seconds ..." + DEFAULT
        time.sleep( 5 )
    elif meaningCloudStatus != '0':
        print ERROR + "[ERROR] MeaningStorm Unknown Error" + DEFAULT
        sys.exit(0xDEAD)
    if textMode == 'DEBUG':
        return decoded
    #Get the feeling
    if textMode == 'FEELING':
        response = decoded['score_tag']
    #Get the irony
    elif textMode == 'IRONY':
        response = decoded['irony']
    else:
        return "[ERROR] ERROR"
    return response

#Clear the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#Init Banner
cls()
if args.verbose:
    print banner
else:
    print stitch

#Catch KeyboardInterrupt (Ctrl + C)
try:
    #Create the authentication
    tauth = tweepy.OAuthHandler(consumerKey,consumerSecret)
    tauth.set_access_token(accessToken,accessSecret)
    #Run the streaming (Sinfonier's Spout)
    spout = spoutModule()
    stream = tweepy.Stream(auth = tauth, listener = spout)
    #Filter the Streaming
    stream.filter(track=args.keywords, async=False)

except KeyboardInterrupt:
    #Catch MongoDB Errors
    try:
        if args.database and not args.persistence:
            db.drop_collection(collection_name) #Delete the collection
        if args.database:
            client.close() #Close the MongoDB connection
    except:
        print ERROR + "[ERROR] Can not close database"
    print CREDITS + "\nCreated by KikePuma 2017 (https://github.com/KikePuma)" + DEFAULT #Credits
    sys.exit(0) #Exit the program


