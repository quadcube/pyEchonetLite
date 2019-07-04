# pyEchonetLite: Echonet Lite for Human
Too lazy to search specification documents for mundane stuffs like Class Code (CC), Class Group Code (CGC), source EOJ, ESV, etc.? 
pyEchonetLite was created to make interfacing with Echonet Lite devices a breeze.
Written in Python 3, require no external dependencies, pure Python!


#### Wanna create an Echonet Lite packet?
```
createPacket("CC_TEMPERATURE_SENSOR")
createPacket("temperature sensor", EPC=["operational status", "temperature value"])
```
Search **echonet_lite_EOJ_CC.json** in **json** folder for more details about various Echonet Lite device name/class code.
Information about Echonet Lite properties (EPC) can be found in **echonet_lite_EPC_EDT.json** in **json** folder.
#### Parsing an Echonet Lite packet?
```
parsePacket(echonetlite_packet)
```


#### Simple as that. All you need is 3 lines to get going:
```
obj = EchonetLite()
echonetlite_packet = obj.createPacket(arg)
value = obj.parsePacket(echonetlite_packet)
```


Check test unit in echonet_lite.py for various possible use cases.
