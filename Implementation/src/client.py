import socket
from socket import *;
import speech_recognition as sr
client_socket = socket(AF_INET, SOCK_STREAM);
client_socket.connect(("127.0.0.1",9999));


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('python_audio.wav') as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Sharing the audio content to server..')
        
     
    except:
         print('Sorry.. run again...')
		 
recordfile=open("recordtext.txt","w")
recordfile.write(text);
recordfile.close();
readByte = open(r"C:\Users\Mahavir\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\\recordtext.txt","rb");
data=readByte.read();
readByte.close()
client_socket.send(data);
client_socket.close();
