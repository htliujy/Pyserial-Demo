import serial, time
s = serial.Serial('/dev/ttys008',baudrate=9600,timeout=0)
while True:
   time.sleep(1)
   s.write("I'm MASTER!".encode())
   resp = s.read(100)
   if resp: 
      print(resp)
