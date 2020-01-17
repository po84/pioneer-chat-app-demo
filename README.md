# Chat App Demo

python v3.6.9

tested on chrome v79 and firefox v72

## To Run:

- install dep packages

`~/<project-root>$ pip install -r requirements.txt`

- run the app locally

`~/<project-root>$ python main.py`

- launch in browser

Go to http://localhost:5000 in your browser

App can be launched in multiple browsers to simulate a real chat room scenario

App saves data in memory, every time the server is restarted all questions/answers data from previous session will be gone.

Users are populated on server start, their ids will be different.

## Description:

A Flask chat app utilizing WebSocket.

Beyond the basic functionality of chatting, users can also send a message as a *question*. Questions appear diffrently in the chat window. Other users can click on one to answer it if they feel like helping out. Answers also appear differently in the chat window to indicate some users have helped out others.


## Why?

I think collaboration is a good way for people to bond together. And since Pioneer is used by people from various different backgrounds, it's also a good chance for people to share perspective or experience. A Q&A system gives people a chance to notice when others need help, and also a chance for them to stand out when they do help others.
There are a few ways this feature can be expanded upon. 

1. There should be a list of recently asked questions so users logged in after the questions were asked can have visibility on earlier conversations.
2. A way to show how many questions a user has answered. This could expand into a leaderboard of "most helpful users".

3. A way to categorize questions. Putting questions in buckets like "business ops", "programming", "people skills", and etc could help people get a better idea of what kind of questions they are helping out with. This can be tied into the leaderboard system and have a sub-leaderboard for each category. 

4. Giving people the ability to stay anonymous when asking/answering might be a good idea.

I'm sure there are many other ways this can be improved upon, these are just a few that I can think of right now.
