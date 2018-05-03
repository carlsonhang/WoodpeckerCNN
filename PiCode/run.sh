#!/bin/bash
/bin/date > /home/pi/Desktop/run.log
export DISPLAY=:0.0
#uncomment the two lines below to enable autostart. dont modify the #!/bin/bash above
/usr/bin/python /home/pi/Desktop/Testcode_v1.py 2>/home/pi/Desktop/testcode_err.log 1>/home/pi/Desktop/testcode_out.log &
/usr/bin/python /home/pi/Desktop/testbutton.py 2>/home/pi/Desktop/button_err.log 1>/home/pi/Desktop/button_out.log &
echo "scripts started" >> /home/pi/Desktop/run.log

