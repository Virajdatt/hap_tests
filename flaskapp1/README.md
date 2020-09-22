Simple docker image for running a Flask App

The flask server serves a static html, which asks for an input sentece. The input sentence is then posted to the flask server and it creates a TextBlob object, of the input sentence and returns the sentiment polarity based on the words in the input sentence. 

The implementation can be seen in the New.py script.


We can create a docker image out of it using the command :
$docker build -t <name_of_image> . 

We can run the so created image using the command:
$docker run -d -P <name_of_image>

We can then check the mapping of port from host to container by running the command(under PORTS):
$docker ps 


                                                                                  
