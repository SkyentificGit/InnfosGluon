import time
import sys
sys.path.append('home/pi/')

import innfos

actuID = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]
#actuID = innfos.queryID(6)

innfos.enableact(actuID)

innfos.trapposmode(actuID)
time.sleep(0.5)

innfos.trapposset(actuID, [1.5, 1.5, 1.5, 1.5, 1.5, 1.5], [0.75, 0.75, 0.75, 0.75, 0.75, 0.75], [-0.75, -0.75, -0.75, -0.75, -0.75, -0.75])
time.sleep(0.5)

innfos.setpos(actuID, [0.0, -6.34, -15.0, -15.0, 15.0, 0.0])
time.sleep(0.5)

print(innfos.readacttemp(actuID))

innfos.setpos(actuID, [5.0, -1.0, -8.0, -10.0, 10.0, 0.0])
time.sleep(2)
innfos.setpos(actuID, [5.0, 6.0, 8.0, 4.0, 10.0, 0.0])
time.sleep(2)
innfos.setpos(actuID, [10.0, 0.0, 12.0, 6.0, 5.0, 0.0])
time.sleep(2)
innfos.setpos(actuID, [10.0, -2.0, 8.0, 4.0, 9.0, 0.0])
time.sleep(4)
print(innfos.readpos(actuID))
time.sleep(1)
innfos.setpos(actuID, [10.0, 0.0, 12.0, 6.0, 5.0, 0.0])
time.sleep(2)
innfos.setpos(actuID, [5.0, 6.0, 8.0, 4.0, 10.0, 0.0])
time.sleep(2)



innfos.setpos(actuID, [0.0, -6.34, -15.0, -15.0, 15.0, 0.0])
time.sleep(4)

time.sleep(10)
innfos.disableact(actuID)
time.sleep(0.5)
