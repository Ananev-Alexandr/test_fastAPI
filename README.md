# 'Echo'

A small site that has an external html page with an input form and a list of messages.
<br>

The user can enter a message and send it.
<br>
<br>
Script on web socket sends text from input field to backend in JSON format, backend receives message and sends to frontend echoing this message and giving number of this message during session, message to frontend is sent in JSON format.
The frontend script reacts to the event in the web socket connection and receives the message sent from the backend and adds a record to the message table.
<br>
<br>
When the page reloads, the messages disappear and the message numbering starts from 1 again.


## Start-up tips

Python version __python3.10__ is required for a stable program launch, operation on versions less than 3.10 is possible, but has not been tested

To install the dependencies, run the following command:

<code>pip install -r requirements.txt</code>

After installing the dependencies, you can start the project with the command
<code>uvicorn main:app --reload</code>

After executing the start command, go to the local address to see the front page:
<code>http://127.0.0.1:8000/</code>