## hap_tests with simple github actions

- [Contents](#Contents)
	* [ScreenCaptures](#ScreenCaptures)
	* [setup-instructions](#setup-instructions)
	* [Github-Actions](#The-repo-now-has-github-actions-setup)
	* [TO-DO](#TO-DO)

This repo can be used to learn some basics and test some HAP configs in a dockerized environment.
This esentially tries to elimnate one's need to setup a haproxy on  a vm and servers on multiple vm's to get started with haproxy and here one can learn and do some minimal testing on a local machine with docker and docker-compose installed.


The repo comes with a simple 30 lines of a dockerized flask server, which servers a simple html.


The folders *flaskapp1* and *flaskapp2* contain two slightly different versions of the same flaskapp.
flaskapp2 has an extra line in its html saying :-
I am from FAPP2   
This is just to test that the requests are being routed to 2 different backends.

The changes to hap configurations can be made under hap/haproxy.cfg.


Offical docker image of the HAPROXY and its relevant docs can be found at https://hub.docker.com/_/haproxy
Haproxy doesn't write logs to disks. Hap it's contraized form writes the logs to the stdout so one can check the 
hap logs there. Or one can use a rsyslog container and make it write to a volume.

In its current form, the HAP backends are setup to have a roundrobin for routing the incoming requests.
One can also modify the cookie serverid and see the requests routed to different backends.

The 2 serverids mentioned are in the hap/haproxy.cfg file and they are 
f1 and f2
f1 --> routes the requests to container created using the flaskapp1 Dockerfile
f2 --> routes the requests to container created using the flaskapp2 Dockerfile, which says "I am from FAPP2"

## ScreenCaptures
The below image shows haplog entry and the the container served from the image in flaskapp2
![Front-End and HAP log Image](/images/fapp2.png)

The below image shows the response on explicity changing the serverid cookie to f1,
it gets reflected in the image and 
![cookie change](/images/fapp_cookies.png)

Clear cookies and refresh to see roundrobin in action, the request will be redirected to different backends,
![clear cookies](/images/clear-cookies.png)

## setup-instructions

```
   $git clone https://github.com/Virajdatt/hap_tests.git
   $cd hap_tests
   $docker-compose up
```

In case changes are made to the hap/haproxy.cfg or any other file in general please use the --build argument to rebuild things

<code>$docker-compose up --build</code>

## The-repo-now-has-github-actions-setup
![github actions](/images/github-actions.png)

## TO-DO
<ol>
<li>Include write up for starting up the Haproxy</li>
<li>Add comments in the haproxy.cfg file</li>
</ol>
