| ID	|    Description |	Precondition |	Excepted input |	Expected output |	Actual output |
|-----|----------------|---------------|-----------------|------------------|---------------
| TC_1 | Check the Python installation in the local machine | Downloaded the python ver. 3.8.0 | Pyhton.exe | Launch the python | Launching the python |
| TC_2 | Check the python path is set in the environment variables | Set required environment variables and path. | Check the python path in the command prompt | Display the installed path for python |	Display the installed path for python |
| TC_3 |	Check the notepad++ IDE is installed and has the Python language support | Python language support |	Program execution on the command prompt  | Launching the programs with ‘.py’ extensions |	Launching the programs with ‘.py’ extensions |
|TC_4 |	Check whether the server is launched |	Open the command prompt    |	server.py  | Launching the server  |	Launching the server  |
|TC_5 |	Check the audio file is ready to load at the client |	Audio file with .wav format  |	File path to the audio file  |	Launching the audio file at the client|	Launching the audio file at the client|
TC_6 	Check whether the server is running in the background 	Opened server in the command prompt 	Opened server and running	Running server in the background	Running server in the background|
TC_6 	Check whether the client is launched 	Open the command prompt 	Client.py	Launching the client 	Launching the client
TC7	Check the audio file is launched and sent to the server	Server running in the background 	Audio file sent from the client 	Displaying the text on the server	Displaying the text on the server
TC_8	Check if the text is displayed on the server	Successfully launched the audio file from the client 	Audio file from the client 	Text output for the audio input	Text output for the audio input
TC_9	Check the text displayed is written to a text file	 Opened the text file to write 
 	Text displayed on the server	Text written to the text file 
	Text written to the text file 

TC_10	 No audio file launched at the client 	Server running	Client program launched without the audio file 	No output to display the text	Shall not write the text to the file (text file empty) 
