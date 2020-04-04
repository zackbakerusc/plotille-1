<<<<<<< HEAD
=======
import plotille

>>>>>>> 73f2412a36b1a2e71058b80ae893ac9de35eb2ae
from plotille import Canvas

c = Canvas(width=40, height=20)
c.rect(0.1, 0.1, 0.6, 0.6)
c.line(0.1, 0.1, 0.6, 0.6)
c.line(0.1, 0.6, 0.6, 0.1)
c.line(0.1, 0.6, 0.35, 0.8)
c.line(0.35, 0.8, 0.6, 0.6)
print(c.plot())
<<<<<<< HEAD
=======

import paho.mqtt.publish as publish
publish.single("PDB", c.plot(), hostname="localhost")
>>>>>>> 73f2412a36b1a2e71058b80ae893ac9de35eb2ae
