# WebLED
Playing arond with a webservice running on a RasberryPi controlling some LEDs.

## Web Sever
`webled.py` is a little [Flask]([http://flask.pocoo.org) script that starts a web service that serves the routes `/white`, `/green`, `/red`, `/blue`. Each route serves a `plain/text` value between 0 and 255 that corresponds with the brightness level of its color. Clients can use `PUT` to change the value. The server also serves a static `index.html` which contains a little [jQuery UI](https://jqueryui.com) app using sliders to control the values.

### Starting the web server as a service
Raspbian uses systemctl to run daemons. Assuming the server script is located at `/home/pi/webled/webled.py` we create the following service script `/lib/systemd/system/webled.service`
```
Description=Web LED Flask Web Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/home/pi/webled/webled.py > /home/pi/webled/webled.log 2>&1

[Install]
WantedBy=multi-user.target
```
Enable starting the service with system start:
```
> sudo systemctl enable webled
Created symlink from /etc/systemd/system/multi-user.target.wants/webled.service to /lib/systemd/system/webled.service.
```

## Hardware
As hardware setup the solution described by [Popoklopsi](https://www.facebook.com/popoklopsi) in the article [Raspberry Pi & RGB LED-Strips, Controlling a RGB LED-Strip with a Raspberry Pi](http://popoklopsi.github.io/RaspberryPi-LedStrip) is used.

The web service script uses [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) to control the GPIO pins used to control the LED stripes. `test.py` contains a little test script doing some basic GPIO stuff without being a web service.

## Future Plans
* Attach a rotary encoder to the Pi in order to change the brightness level at the hardware as well.
* Use websockets to propagate value changes across multiple clients (and the hardware itself if one is able to change the values directly at the hardware)
* Include [jQuery UI Touch Punch](http://touchpunch.furf.com) for easier touch access of the slider widgets.
* Displaying my current mood and work status through the glass window of my office door using colored light.