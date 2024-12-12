import qrcode

myqr = qrcode.make("https://youtu.be/IUQVO97zcE0?si=j-L6LQQoQQLNjKDi")
myqr.save(myqr.png)