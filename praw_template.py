import praw #PRAW provides Reddit API functionality
import datetime #Provides capability to easily formate timestamps of message postings
import asyncpraw
from aiohttp import ClientSession

session = ClientSession(trust_env=True)
#Reddit API Credentials

reddit = praw.Reddit(user_agent='CIS518',
                     client_id='xRc8Mg2oqNI_Pkeign6TPw',
                     client_secret="5-rUhb9KCdu11JQ87lnFqSAr1Kaegg",
                     username='hardeek24',
                     password='Hardeek@987') 



#Change this variable to indicate what subreddit you want to collect
#Find the subreddit manually on Reddit
#Then change the subreddit name here to be exactly the same
#No white spaces! A multi-word subreddit will have underscores, e.g., "three_word_subreddit"
subreddit = 'StartLink' 

#File gets written to the same directory this Python script is located. The file will be called "output.csv"
f = open('output16.csv','w', encoding='utf8')	
#In this next line we print out column headers
f.write("MsgID, Timestamp,Author,ThreadID,ThreadTitle,MsgBody,ReplyTo,Permalink\n")

#Begin streaming user-generated comments from the focal subreddit specified in the 'subreddit' variable earlier in this code
count = 1

for comment in reddit.subreddit("Star+Link").stream.comments():
  #Refer to the documentation for PRAW to see what API commands are available
    commentID = str(comment.id) #Every Reddit post has an identification number. Here we extract it
    author = str(comment.author).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #Name of message author
    timestamp = str(datetime.datetime.fromtimestamp(comment.created)) #Timestamp of when message was posted
    replyTo = "" #Whether the collected message was a direct reply to another existing message. 
    if not comment.is_root: #If it is indeed a reply, this column contains the message ID of the parent message. If it is not a reply, a '-' is written to this column
          replyTo = str(comment.parent().id)
    else:
        replyTo = "-"
    threadID = str(comment.submission.id) # The ID of the thread the message was posted in
    threadTitle = str(comment.submission.title).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #The title of the thread the message was posted in
    msgBody = str(comment.body).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #The message itself
    permalink = str(comment.permalink).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #A URL you can follow directly to the message

#Print all collected message data to console
    print("-------------------------------------------------------")
    print("Comment ID: " + str(comment.id))
    print("Comment Author: "+ str(comment.author))
    print("Timestamp: "+str(datetime.datetime.fromtimestamp(comment.created)))
    if not comment.is_root:
        print("Comment is a reply to: " + str(comment.parent().id))
    else:
        print("Comment is a reply to: -")
        print("Comment Thread ID: " + str(comment.submission.id))
        print("Comment Thread Title: " + str(comment.submission.title))
        print("Comment Body: " + str(comment.body))
        print("Comment Permalink: " + str(comment.permalink))

#Write everything to a file (outpost.csv specified earlier)
        f.write("'"+commentID+"','"+timestamp+"','"+author+"','"+threadID+"','"+threadTitle+"','"+msgBody+"','"+replyTo+"','"+permalink+"'\n")
        print("Total messages collected from /r/"+subreddit+": " + str(count))
        count += 1
  
