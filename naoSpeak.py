import time
from coppeliaSimZMQRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Get NAO's speaker
speaker = sim.getObject('/NAO/Speaker')

sim.startSimulation()
time.sleep(2)

# Make NAO speak (Text-to-Speech)
sim.callScriptFunction('saySomething', speaker, 'Hello, I am NAO!')

time.sleep(2)
sim.stopSimulation()

