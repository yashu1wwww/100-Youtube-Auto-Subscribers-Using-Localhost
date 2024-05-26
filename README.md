# 100-Youtube-Auto-Subscribers-Using-Localhost

100+ Youtube Non Stop Auto Subscribers using selenium with python on localhost

## "If you know proxy rotation, then please fork it".

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

## Watch up to 3 minutes and 46 seconds, and then remain in the remaining part in the code

First, open Chrome file location and bypass the location restriction using an extension such as Touch VPN. In my case, the Chrome location(use start in: path) is

C:\Users\Hp\AppData\Local\Google\Chrome\Application

click window button and search cmd and enter

cd C:\Users\Hp\AppData\Local\Google\Chrome\Application (1st line in cmd)

in line enter

chrome.exe --remote-debugging-port=9222 --user-data-dir=""(in "enter your localhost path here")

Next, enter this command into the terminal, replacing "enter your localhost path here" with your localhost path:

For example, in my case it is:

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost" (2nd line in cmd make sure you replace the localhost path)

# then again open new terminal in that folder enter

 pip install selenium==4.2.0 

after enter  subscribe.py or double click on subscribe.py

After opening Chrome, paste the following two lines of code from the script into the command prompt and hit enter. This will open the YouTube channel url in Chrome, automatically hit subscribe, and switch between accounts to hit the auto subscribe.

"You must login with your 10+ accounts, and each account must have 10+ brand accounts to hit auto-subscribe. replace the URL with the youtube channel url in 18th line...


---------------------------------------------------------------------------------------------------------------------------------------------

## 👉 Note:Every time YouTube updates the code, it varies. So, open the YouTube video, press 'Ctrl+Shift+C' to open the developer tools,

## then copy the 'subcribe' button's XPath, CSS, or JavaScript path. Replace it in the code and press 'Ctrl+H' to find and replace the same element in the code.

---------------------------------------------------------------------------------------------------------------------------------------------

# 👉Note:-

👉If you have the latest version of Selenium, the code may not run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
