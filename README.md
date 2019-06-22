# pyEchonetLite: Echonet Lite for Human
Too lazy to search specification documents for mundane stuffs like Class Group Code, source EOJ, ESV, etc.? 
pyEchonetLite was created to make interfacing with Echonet Lite devices a breeze. No need to 
Written in Python 3, require no external dependencies, pure Python!


#### Wanna create an Echonet Lite packet?
```
createPacket("CC_TEMPERATURE_SENSOR")
```


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


Check test unit in echonet_lite.py for various use cases.
