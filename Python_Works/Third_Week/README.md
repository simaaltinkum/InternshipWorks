#Explanation
*	It provides follow your employees entering and exit times.
Firstly i imported datetime, timedelta and random. I created lastTime and firstTime variable for buffering beginning and end date. "c" variable calculates the difference between last date and beginning date.
*	"time" function buffers dataArr for adding new entering and exit times "c.days" times. Also if it is weekend time it prints it. If it is not weekend random assigns hour and minute for per section of a day. End of this function i return dataArr string form because write it txt folder. Lists are not valid for txt write operation.
*	Finally i created a txt folder for recording datas. I write it write() method. Then, i used read() method to open it python for read.
