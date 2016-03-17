=========
 Fishnet
=========

A raspberry pi network.  Collecting and serving open data.

Weather data, transport information, culture, music, art and science.

Bermuda
-------


Rasberry Pi
===========

The raspberry pi is a small, low cost, low power, computer.  There are
several different models, ranging in price from $5 to $35.

Playing with these is like playing with lego computers.  You can plug
things into them: sensors, lights, displays and lots more.

There is simple software to work with all these components.  The
software is getting simpler.

Astro pi
========

The Astro Pi or Sense Hat is one component you can plug in.  It has a
pressure sensor, a humidity sensor, a compass and accelerometer.  It
also has an 8x8 colour LED display that is simple to program.  You can
display banner messages or low resolution images.  There is also a
tiny joystick that you can use to give input to the pi.

The Pi 3 has just been announced.  It has built in wifi and a
bluetooth chip too.  I hear it is more powerful than the 2, which is
already a powerful machine for the power consumption.


Getting Started
===============

Install Raspbian
----------------

Download the latest raspbian image and put it on an SD card.

See http://raspbian.org/ for how to do this.

Windows install
'''''''''''''''

https://sourceforge.net/projects/win32diskimager/files/latest/download

Use the disk imager to write the image to the SD card

OK, so hit a few snags, but
---------------------------

It works great from at least one computer in the world :)

Connecting via a network cable to the pi.

Then using ssh:

  ssh -v pi@192.168.1.1

but if this fails check what your dhcp server is doing.
  
When prompted for a pasword, use "raspberry".

I've been thinking about connecting to sites with interesting data or
compute power, open data, and lots more.

Being able to deploy images with good security and repeatable
(automatic) installs would be valuable in lots of directions.  It would
be great for the pi's.

Just a "copy this raspbian, run this install script, by the way you
might be connected to:

  * nothing
  * internet?
  * another computer by ethernet cable?
  * wifi
  * bluetooth
  * sensors

If it found a way to give me a hint where and (when?) it thinks it is
that would helpful,

And it somehow gets me where I can ssh to it or wifi connection and
log on.


Starting the pi
---------------

Once you have raspbian on your SD card you can start up the raspberry
pi.

There are two options.

Connect the pi to a display and keyboard
''''''''''''''''''''''''''''''''''''''''

Network connection from another machine
'''''''''''''''''''''''''''''''''''''''

Windows
+++++++

http://carbonstone.blogspot.com/2014/02/connecting-to-pi-from-laptops-ethernet.html

Add aceboy
----------

Install some extras
-------------------

git

python3
+++++++

Clone fishnet
-------------

pip install -r requirements.txt
-------------------------------

ZeroNet
-------

Sunshine
--------

Jupyter
-------

Ingredients
===========

Raspbian
========

Weather
=======

Zeronet
=======
