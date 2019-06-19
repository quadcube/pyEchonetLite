#
#    Echonet Lite Python 3
#
import logging
import unittest
import json

ehd = None
eoj_cgc = None
eoj_cc = None
esv = None
epc = None
epc_edt = None
il = None
fd = None

"""
    Echonet Lite Functions
    Note: 1. functions are similar to the C version Echonet Lite library, removed some of the simpler functions such as echonet_setEHD1(), etc. and changed the return failed response to -1 for get() functions
          2. functions that deals directly with echonet_packet (global variable) must be executed in sequence (e.g.: setPacket -> setnEPC -> setnPDC -> setnEDT)
          3. functions are thread safe as long as functions in each instances (classes) are sequentially called
    
    Echonet Lite Packet Structure
    |   EHD1   |   EHD2   |   TID   |   EDATA (SEOJ,DEOJ,ESV,OPC,EPC1,PDC1,EDT1,...)   |
"""
class EchonetLite():
    def __init__(self):
        global ehd, eoj_cgc, eoj_cc, esv, epc, epc_edt, il, fd
        MAX_ECHONET_PACKET_LEN = 64
        self.current_echonet_packet_len = 0
        self.echonet_packet = [0] * MAX_ECHONET_PACKET_LEN # pre-allocate echonet lite packet structure
        if ehd == None: self.initEchonetLite()
    
    # Initialize Echonet Lite Library
    # Note: 1. Require JSON Echonet Lite property files
    def initEchonetLite(self):
        global ehd, eoj_cgc, eoj_cc, esv, epc, epc_edt, il, fd
        try:
            with open('json/echonet_lite_EHD.json') as json_file:
                ehd = json.load(json_file)
                ehd = self.dictTraverse(ehd, path=None, convert=True)
            with open('json/echonet_lite_EOJ_CGC.json') as json_file:
                eoj_cgc = json.load(json_file)
                eoj_cgc = self.dictTraverse(eoj_cgc, convert=True)
            with open('json/echonet_lite_EOJ_CC.json') as json_file:
                eoj_cc = json.load(json_file)
                eoj_cc = self.dictTraverse(eoj_cc, convert=True)
            with open('json/echonet_lite_ESV.json') as json_file:
                esv = json.load(json_file)
                esv = self.dictTraverse(esv, convert=True)
            with open('json/echonet_lite_EPC.json') as json_file:
                epc = json.load(json_file)
                epc = self.dictTraverse(epc, convert=True)
            with open('json/echonet_lite_EPC_EDT.json') as json_file:
                epc_edt = json.load(json_file)
                epc_edt = self.dictTraverse(epc_edt, convert=True)
            with open('json/echonet_lite_IL.json') as json_file:
                il = json.load(json_file)
                il = self.dictTraverse(il, convert=True)
            with open('json/echonet_lite_FD.json') as json_file:
                fd = json.load(json_file)
                fd = self.dictTraverse(fd, convert=True)
        except Exception as e:
            logging.exception("initEchonetLite() exception occurred.")

    # Helper: Python Dictionary Traversal
    # Note: 1.
    #       2. key search useful for both epc and eoj_cc json
    def dictTraverse(self, obj, path=None, callback=None, convert=False, search=None, key=False):
        search_value = None
        # Dictionary Traversal (recursive function)
        def _inner_traversal(obj, path=None, callback=None, convert=False, search=None, target=None, key=False):
            nonlocal search_value
            if path is None: path = []
            if isinstance(obj, dict):
                value = {} #value = {k: self.dictTraverse(v, path + [k], callback, convert, search) for k, v in obj.items()}
                for k, v in obj.items():
                    #print(f"dict() path {path}, key {k}, value {v}\n\n")
                    if search is not None: # search for value
                        if all(elem in path for elem in search) and k == target and key == False:
                            search_value = v
                            raise StopIteration # break all iteration
                        elif key == True:
                            if k == search[0]:
                                search_value = path[0]
                                raise StopIteration # break all iteration
                            elif v == search[0]:
                                search_value = k
                                raise StopIteration # break all iteration
                    value.update({k: _inner_traversal(v, path + [k], callback, convert, search, target, key)})
            elif isinstance(obj, list):
                value = [] #value = [self.dictTraverse(elem, path + [[]], callback, convert, search) for elem in obj]
                for elem in obj:
                    #print(f"list() path {path}, elem {elem}\n\n")
                    value.append(_inner_traversal(elem, path + [[]], callback, convert, search, target, key))
            else:
                #print(f"scalar path {path} value {obj}\n\n")
                if search is not None: # search for value
                    if all(elem in path for elem in search):
                        search_value = obj
                        raise StopIteration # break all iteration
                value = obj
            if convert == True: # convert dict hex, bin strings to int
                try:
                    value = int(value,0)
                except:
                    pass
            if callback is None:
                return value
            else:
                return callback(path, value)
                
        if search is not None:
            try:
                if not isinstance(search, list): search = [search] # make sure that search variable is a list
                try:
                    target = [elem for elem in search if not any(elem1 in elem for elem1 in ['CGC_', 'CC_', 'EPC_'])] # filter off some Echonet Lite constant headers
                    target = 'value' if not target else target[0] # provide default target and ensure it's a single target
                    search_only = [elem for elem in search if any(elem1 in elem for elem1 in ['CGC_', 'CC_', 'EPC_'])] # filter off some Echonet Lite constant
                except TypeError:
                    target = None
                    search_only = search # non-iterable objects are directly passed into search_only (e.g.: int)
                if not search_only: search_only = search # ensure search is not empty
                _inner_traversal(obj, path, callback, convert, search_only, target, key)
            except StopIteration:
                return search_value
        else:
            return _inner_traversal(obj, path, callback, convert)
                
    # Helper: Echonet Lite Property Finder
    #def getEPC():
    
    # Set Echonet Lite Property
    # Note: 1. 1 byte (X1-class group code,X2-class code)
    #       2. Refer to Table 3.12 EPC Code Allocation Table
    #       3. Value n>0,n<=OPC value (Request 1,2,3,...,n)
    #       4. echonet_setnEPC(OPC limited n,EPC_xx)
    def setnEPC(self, n, epc_code):
        j, k = 0, 0
        if n <= self.echonet_packet[11] and n > 0: # check n with OPC
            if n == 1:
                self.echonet_packet[12] = epc_code
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                self.echonet_packet[12+k+(i*2)] = epc_code
            self.current_echonet_packet_len += 1
        else:
            logging.error("setnEPC() invalid n.")

    # Get Echonet Lite Property
    # Note: 1. Error,return -1
    def getnEPC(self, n):
        j, k = 0, 0
        if n <= self.echonet_packet[11] and n > 0: # check n with OPC
            if n == 1:
                return self.echonet_packet[12]
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                return self.echonet_packet[12+k+(i*2)]
        else:
            logging.error("setnEPC() invalid n.")
            return -1

    # Set Echonet Lite Property Data Counter
    # Note: 1. Value n>0,n<=OPC value (Request 1,2,3,...,n)
    #       2. echonet_setnPDC(OPC limited n,value)
    def setnPDC(self, n, value):
        j, k = 0, 0
        if n <= self.echonet_packet[11] and n > 0: # check n with OPC
            if n == 1:
                self.echonet_packet[13] = value
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                self.echonet_packet[13+k+(i*2)] = value
            self.current_echonet_packet_len += 1
        else:
            logging.error("setnPDC() invalid n.")

    # Get Echonet Lite Property Data Counter
    # Note: 1. Error,return -1
    def getnPDC(self, n):
        j, k = 0, 0
        if n <= self.echonet_packet[11] and n > 0: # check n with OPC
            if n == 1:
                return self.echonet_packet[13]
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                return self.echonet_packet[13+k+(i*2)]
        else:
            logging.error("getnPDC() invalid n.")
            return -1

    # Set Echonet Lite Property Value
    # Note: 1. property_data_list can be any data type or list
    def setnEDT(self, n, property_data_list):
        j, k = 0, 0
        if not isinstance(property_data_list, list): property_data_list = [property_data_list]  # make sure property_data_list is a list
        if n <= self.echonet_packet[11] and n > 0 and len(property_data_list) == self.getnPDC(n): # check n with OPC & input list is equal to nPDC
            if n == 1:
                for i in range(self.getnPDC(n)):
                    self.echonet_packet[14+i] = property_data_list[i]
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                for j in range(self.getnPDC(n)):
                    self.echonet_packet[14+j+k+(i*2)] = property_data_list[j]
            self.current_echonet_packet_len += len(property_data_list)
        else:
            logging.error("setnEDT() invalid n and/or length of input list is not equal to nPDC.")

    # Get Echonet Lite Property Value
    # Note: 1. Error,return -1
    #       2. returns EDT list
    def getnEDT(self, n):
        EDT_list = []
        j, k = 0, 0
        if n <= self.echonet_packet[11] and n > 0: # check n with OPC
            if n == 1:
                for i in range(self.getnPDC(n)):
                    EDT_list.append(self.echonet_packet[14+i])
            else:
                for i in range(1, n):
                    k += self.echonet_packet[12+i+j+k]
                    j += 1
                for j in range(self.getnPDC(n)):
                    EDT_list.append(self.echonet_packet[14+j+k+(i*2)])
            return EDT_list
        else:
            logging.error("setnEDT() invalid n")
            return -1
        
    # Create Echonet Lite Packet
    # Note: 1. TID can accept both single 16 bit integer and two 8 bit integer list
    def createPacket(self, DEOJ_CC, TID=0x00, SEOJ_CC='CC_NODE_PROFILE', SEOJ_IC=0x01, DEOJ_IC=0x01, EPC="EPC_OPERATIONAL_STATUS", ESV='ESV_Get', EPC_EDT=()):
        global ehd, eoj_cgc, eoj_cc, esv, epc, epc_edt, il, fd
        if not isinstance(TID, list): TID = [TID >> 8, TID & 0x00ff] # convert TID to list
        if not isinstance(EPC, list): EPC = [EPC]  # make sure EPC is a list
        if not isinstance(EPC_EDT, list): EPC_EDT = [EPC_EDT]  # make sure EPC_EDT is a list
        OPC = len(EPC) if EPC_EDT == [()] else len(EPC_EDT) # calculate OPC
        self.echonet_packet[:] = [0 for _ in self.echonet_packet[:]] # reset global var
        scgc_key = self.dictTraverse(eoj_cc, search=SEOJ_CC, key=True)
        dcgc_key = self.dictTraverse(eoj_cc, search=DEOJ_CC, key=True)
        self.echonet_packet[:12] = [ehd['EHD1_ECHONET'], ehd['EHD2_FORMAT1'], TID[0], TID[1], eoj_cgc[scgc_key], eoj_cc[scgc_key][SEOJ_CC], SEOJ_IC, eoj_cgc[dcgc_key], eoj_cc[dcgc_key][DEOJ_CC], DEOJ_IC, esv[ESV], OPC]
        self.current_echonet_packet_len = 12 # reset current Echonet packet length
        for i in range(OPC):
            if EPC_EDT == [()]:
                target_epc = EPC[i]
                target_pdc = 0
            else:
                target_epc = EPC_EDT[i][0]
                target_pdc = len(EPC_EDT[i][1])
            self.setnEPC(i+1, self.dictTraverse(epc_edt, search=target_epc))
            self.setnPDC(i+1, target_pdc)
            if not EPC_EDT == [()]:
                self.setnEDT(i+1, EPC_EDT[i][1])
        return self.echonet_packet[:self.current_echonet_packet_len]

"""
    Echonet Lite Function Test Units
    Note: 1. covers all functions that deals directly with echonet_packet (global variable)
          2.
"""
class testEchonetLite(unittest.TestCase):
    def setUp(self): # populate global var with sample header, OPC = 3
        self.obj = EchonetLite()
        self.obj.echonet_packet[:] = [0 for _ in self.obj.echonet_packet[:]] # reset global var
        self.sample = [0x10, 0x81, 0x00, 0x01, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3]
        self.obj.echonet_packet[:len(self.sample)] = self.sample[:]

    def test_setnEPC(self):
        self.obj.setnEPC(1, 0x01) # n = 1, EPC = 0x01
        self.sample.append(0x01) # n = 1, EPC = 0x01
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0xFF] # n = 1, PDC = 0x01, EDT = 0xFF
        self.obj.setnEPC(2, 0x01) # n = 2, EPC = 0x01
        self.sample.extend([0x01, 0xFF, 0x01]) # n = 2, EPC = 0x01
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+4] = [0x03, 0xFF, 0xFF, 0xFF] # n = 2, PDC = 0x03, EDT = 0xFF * 3
        self.obj.setnEPC(3, 0x01) # n = 3, EPC = 0x01
        self.sample.extend([0x03, 0xFF, 0xFF, 0xFF, 0x01]) # n = 3, EPC = 0x01
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)

    def test_getnEPC(self):
        self.obj.echonet_packet[12] = 0x01 # n = 1, EPC = 0x01
        self.sample.append(0x01) # n = 1, EPC = 0x01
        self.assertEqual(self.obj.getnEPC(1), self.sample[len(self.sample)-1])
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2]  = [0xFF, 0x01] # EDT = 0xFF, n = 2, EPC = 0x01
        self.sample.extend([0xFF, 0x01]) # EDT = 0xFF, n = 2, EPC = 0x01
        self.assertEqual(self.obj.getnEPC(1), self.sample[len(self.sample)-1])
    
    def test_setnPDC(self):
        self.obj.echonet_packet[12] = 0x01 # n = 1, EPC = 0x01
        self.obj.setnPDC(1, 0x01) # n = 1, value = 1
        self.sample.extend([0x01, 0x01]) # n = 1, EPC = 0x01, PDC = 0x01
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2]  = [0xFF, 0x01] # EDT = 0xFF, n = 2, EPC = 0x01
        self.obj.setnPDC(2, 0x03)
        self.sample.extend([0xFF, 0x01, 0x03]) # n = 1, EPC = 0x01, PDC = 0x03
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+4]  = [0xFF, 0xFF, 0xFF, 0x01] # EDT = 0xFF * 3, n = 3, EPC = 0x01
        self.obj.setnPDC(3, 0x02)
        self.sample.extend([0xFF, 0xFF, 0xFF, 0x01, 0x02]) # n = 2, EPC = 0x01, PDC = 0x02
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)

    def test_getnPDC(self):
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x01]  # n = 1, EPC = 0x01, PDC = 0x01
        self.sample.extend([0x01, 0x01]) # n = 1, EPC = 0x01, PDC = 0x01
        self.assertEqual(self.obj.getnPDC(1), self.sample[len(self.sample)-1])
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0xFF, 0x01, 0x03]  # EDT = 0xFF, n = 2, EPC = 0x01, PDC = 0x03
        self.sample.extend([0xFF, 0x01, 0x03]) # EDT 0xFF, n = 2, EPC = 0x01, PDC = 0x03
        self.assertEqual(self.obj.getnPDC(2), self.sample[len(self.sample)-1])
        self.obj.echonet_packet[len(self.sample):len(self.sample)+5] = [0xFF, 0xFF, 0xFF, 0x01, 0x02] # EDT = 0xFF * 3, n = 3, EPC = 0x01, PDC = 0x02
        self.sample.extend([0xFF, 0xFF, 0xFF, 0x01, 0x02]) # EDT 0xFF * 3, n = 3, EPC = 0x01, PDC = 0x02
        self.assertEqual(self.obj.getnPDC(3), self.sample[len(self.sample)-1])
    
    def test_setnEDT(self):
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x01] # n = 1, EPC = 0x01, PDC = 0x01
        self.obj.setnEDT(1, [0xFF]) # input EDT must be a list
        self.sample.extend([0x01, 0x01, 0xFF]) # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x03] # n = 2, EPC = 0x01, PDC = 0x03
        self.obj.setnEDT(2, [0xFF, 0xFF, 0xFF])
        self.sample.extend([0x01, 0x03, 0xFF, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x02] # n = 1, EPC = 0x01, PDC = 0x02
        self.obj.setnEDT(3, [0xFF, 0xFF])
        self.sample.extend([0x01, 0x02, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x02, EDT = 0xFF * 2
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)

    def test_getnEDT(self):
        self.obj.echonet_packet[len(self.sample):len(self.sample)+3] = [0x01, 0x01, 0xFF] # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.sample.extend([0x01, 0x01, 0xFF]) # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.assertEqual(self.obj.getnEDT(1), [self.sample[len(self.sample)-1]])
        self.obj.echonet_packet[len(self.sample):len(self.sample)+5] = [0x01, 0x03, 0xFF, 0xFF, 0xFF] # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.sample.extend([0x01, 0x03, 0xFF, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.assertEqual(self.obj.getnEDT(2), self.sample[len(self.sample)-3:len(self.sample)])

    def test_dictTraverse(self):
        self.assertEqual(self.obj.dictTraverse(epc_edt, search=["CC_TEMPERATURE_SENSOR"]), 0xE0)
        self.assertEqual(self.obj.dictTraverse(epc_edt, search=["CC_ELECTRIC_ENERGY_SENSOR", "EPC_SMALL_CAPACITY_SENSOR_INSTATANEOUS_ELECTRIC_ENERGY"]), 0xE2)
        self.assertEqual(self.obj.dictTraverse(eoj_cc, search="CC_ELECTRIC_ENERGY_SENSOR"), 0x22) # test non-'value' key dict
        self.assertEqual(self.obj.dictTraverse(ehd, search="EHD2_FORMAT1"), 0x81) # test single level dict without Echonet Lite constant header
        self.assertEqual(self.obj.dictTraverse(epc_edt, search="EPC_OPERATIONAL_STATUS"), 0x80)
        self.assertEqual(self.obj.dictTraverse(eoj_cc, search=0x0B, key=True), "CC_AIR_POLLUTION_SENSOR") # search for key
        self.assertEqual(self.obj.dictTraverse(eoj_cc, search="CC_AIR_POLLUTION_SENSOR", key=True), "CGC_SENSOR_RELATED")
        self.assertEqual(self.obj.dictTraverse(eoj_cgc, search=0x05, key=True), "CGC_MANAGEMENT_RELATED")

    def test_createPacket(self):
        self.assertEqual(self.obj.createPacket("CC_TEMPERATURE_SENSOR"), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x01, 0x80, 0x00])
        self.assertEqual(self.obj.createPacket("CC_TEMPERATURE_SENSOR", EPC=["EPC_OPERATIONAL_STATUS", "EPC_TEMPERATURE_VALUE"]), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x02, 0x80, 0, 0xE0, 0])
        #print(self.obj.createPacket("CC_HOME_AIR_CONDITIONER", ESV='ESV_SetC', EPC_EDT=[("EPC_OPERATIONAL_STATUS",0x30), ("EPC_OPERATION_MODE_SETTING", 0x41)]))











#                         ehd1  ehd2  tid   tid   seoj  seoj  seoj  deoj  deoj  deoj  esv  opc epc  pdc edt
ECHONET_MSG_SET_WINDOW = [0x10, 0x81, 0x00, 0xFF, 0x0E, 0xF0, 0x01, 0x05, 0xFD, 0x01, 0x61, 1, 0x80, 1, 0x30]
# tid 0x00 and 0x01 reserved for indoor n outdoor temp
ECHONET_MSG_TEMPERATURE = [0x10, 0x81, 0x00, 0x01, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 1, 0xE0, 0]
ECHONET_MSG_AIRSPEED = [0x10, 0x81, 0x00, 0x02, 0x0E, 0xF0, 0x01, 0x00, 0x1F, 0x01, 0x62, 1, 0xE0, 0]
ECHONET_MSG_GET_AIRCOND = [0x10, 0x81, 0x00, 0x03, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x62, 1, 0x80, 0] # EPC_OPERATIONAL_STATUS=0x80
ECHONET_MSG_SET_AIRCOND = [0x10, 0x81, 0x00, 0x04, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x61, 1, 0x80, 1, 0x31] # 0x31 OFF
ECHONET_MSG_AIRCOND_HEAT = [0x10, 0x81, 0x00, 0x05, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x61, 1, 0xB0, 1, 0x41] # EPC_MODE = 0xB0 ESV_SetC = 0x61, Aircond mode: 0x41 (auto)
ECHONET_MSG_AIRCOND_SET_TEMP = [0x10, 0x81, 0x00, 0x06, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x61, 1, 0xB3, 1, 0x19] # EPC_TEMP = 0xB3 ESV_SetC = 0x61, Temp range: 0x00 - 0x32 (0x19 : 25 Celsius)
ECHONET_MSG_AIRCOND_GET_TEMP = [0x10, 0x81, 0x00, 0x07, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x62, 1, 0xB3, 0]
#                            ehd1  ehd2  tid   tid   seoj  seoj  seoj  deoj  deoj  deoj  esv  opc epc
ECHONET_MSG_POWERMETER_D1 = [0x10, 0x81, 0x00, 0x08, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD1, 0]
ECHONET_MSG_POWERMETER_D2 = [0x10, 0x81, 0x00, 0x09, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD2, 0]
ECHONET_MSG_POWERMETER_D3 = [0x10, 0x81, 0x00, 0x0A, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD3, 0]
ECHONET_MSG_POWERMETER_D4 = [0x10, 0x81, 0x00, 0x0B, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD4, 0]
ECHONET_MSG_POWERMETER_D5 = [0x10, 0x81, 0x00, 0x0C, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD5, 0]
ECHONET_MSG_POWERMETER_D6 = [0x10, 0x81, 0x00, 0x0D, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD6, 0]
ECHONET_MSG_POWERMETER_D7 = [0x10, 0x81, 0x00, 0x0E, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD7, 0]
ECHONET_MSG_POWERMETER_D8 = [0x10, 0x81, 0x00, 0x0F, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD8, 0]
ECHONET_MSG_POWERMETER_D9 = [0x10, 0x81, 0x00, 0x10, 0x0E, 0xF0, 0x01, 0x02, 0x87, 0x01, 0x62, 1, 0xD9, 0]
ECHONET_MSG_AIRCOND_GET_SENSETEMP = [0x10, 0x81, 0x00, 0x11, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x62, 1, 0xBB, 0]


if __name__ == '__main__':
    unittest.main()
