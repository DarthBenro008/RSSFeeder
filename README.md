# RSSFeeder
This is a RSS Feeder , that is ,it will broadcast an RSS feed if you have some kind of compilation and it fails , it can be used with:
<ul>
<li>Android ROM</li>
<li>Custom Kernel</li>
<li>Any make job</li>
</ul>
You can use this feeder with your make command with the ||, 
<b> Eg: make -j32 || . feeder </b>
<br>
<br>
<b>You just need to modify line 10 , 25 & 28 to your website's link in "check.py" file </b>

All your job status will be stored in jobstatus file.

<b><I>Application:</I></b>
I personally use it to check if my android build fails , this script braodcasts this using RSS , and with a simple applet in IFTTT , i get notified to my phone if my build fails.
You can use all your creativity too use this tool.

<b>Make sure all files are in the same directories!</b>
