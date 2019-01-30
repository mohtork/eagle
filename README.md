# Eagle
- Monitor your server resources (cpu , memory , disks and swap)<br/>
- Monitor your domains uptime<br/> 
- Monitor ssl expire dates<br/>
- Send alerts to slack<br/>
![ScreenShot](https://s3-us-west-2.amazonaws.com/linuxdirection-github/memory.png)<br/>
![ScreenShot](https://s3-us-west-2.amazonaws.com/linuxdirection-github/ssl.png)<br/>
![ScreenShot](https://s3-us-west-2.amazonaws.com/linuxdirection-github/swap.png)<br/>
![ScreenShot](https://s3-us-west-2.amazonaws.com/linuxdirection-github/uptime.png)<br/>

# Installation
1. git clone https://github.com/mohtork/eagle.git
2. pip install -r requirements.txt

# Eagle in action
- Set your slack credentials from main.yaml file<br/>
- Set your rules from yaml files inside rules directory<br/>
- Add eagle to the running crons<br/>
"* * * * *" cd /path-to/eagle/ && python eagle.py > /tmp/eagle.log 2>&1

