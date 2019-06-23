#
#    Echonet Lite Python 3
#
import logging
import unittest
import json

ehd = None      # stores echonet_lite_EHD.json as dict
eoj_cgc = None  # stores echonet_lite_EOJ_CGC.json as dict
eoj_cc = None   # stores echonet_lite_EOJ_CC.json as dict
esv = None      # stores echonet_lite_ESV.json as dict
epc = None      # stores echonet_lite_EPC.json as dict
epc_edt = None  # stores echonet_lite_EPC_EDT.json as dict
il = None       # stores echonet_lite_IL.json as dict
fd = None       # stores echonet_lite_FD.json as dict

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
    # Note: 1. Used extensively by createPacket() and parsePacket() to generate and parse Echonet Lite packets
    #       2. Key search useful for both epc and eoj_cc json
    #       3. If search argument is 1, function might return wrong value due to return of first value found (e.g. CC_NETWORK_CAMERA == CC_FIRST_AID_SENSOR == CC_BLOOD_SUGAR_METER, CC_FIRST_AID_SENSOR will be returned)
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
                        if all(elem in path for elem in search) and k == target and key == False: # TODO: below all(lists) method might be more versatile for non-key search
                            search_value = v
                            raise StopIteration # break all iteration
                        elif key == True:
                            if len(search) > 1: # this returns more accurate result compared to len(search)==1
                                if all(elem in path + [k] + [v] for elem in search):
                                    search_value = ([elem for elem in path + [k] + [v] if not any(elem in [elem1] for elem1 in search)])[0]
                                    raise StopIteration # break all iteration
                            elif len(search) == 1: # might return wrong value due to return of first value found (e.g. CC_NETWORK_CAMERA == CC_FIRST_AID_SENSOR == CC_BLOOD_SUGAR_METER, CC_FIRST_AID_SENSOR will be returned)
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
    # Note: 1. Error, return -1
    #       2. SEOJ_CC and DEOJ_CC is able to accept both str and int, however if either one or both are int, its respective EOJ_CGC is required
    #       3. ESV is able to accept both str and int. e.g. "ESV_Get" = 0x62
    #       4. EPC and EPC_EDT are both able to accept str and int, e.g. "EPC_OPERATIONAL_STATUS" = 0x80, "on" = 0x41
    #       5. TID can accept both single 16 bit integer and two 8 bit integer list
    def createPacket(self, DEOJ_CC, TID=0x00, SEOJ_CC='CC_NODE_PROFILE', SEOJ_IC=0x01, DEOJ_IC=0x01, EPC="EPC_OPERATIONAL_STATUS", ESV='ESV_Get', EPC_EDT=(), DEOJ_CGC=None, SEOJ_CGC=None):
        global ehd, eoj_cgc, eoj_cc, esv, epc, epc_edt, il, fd
        if not isinstance(TID, list): TID = [TID >> 8, TID & 0x00ff] # convert TID to list
        if not isinstance(EPC, list): EPC = [EPC]  # make sure EPC is a list
        if not isinstance(EPC_EDT, list): EPC_EDT = [EPC_EDT]  # make sure EPC_EDT is a list
        OPC = len(EPC) if EPC_EDT == [()] else len(EPC_EDT) # calculate OPC
        if ESV == 'ESV_Get' and EPC_EDT != [()]: ESV = 'ESV_SetC'
        ESV = esv[ESV] if isinstance(ESV, str) else ESV # check whether ESV is str
        if isinstance(DEOJ_CC, str) and DEOJ_CGC == None:
            dcgc_key = self.dictTraverse(eoj_cc, search=DEOJ_CC, key=True)
            deoj_cgc = eoj_cgc[dcgc_key]
            deoj_cc = eoj_cc[dcgc_key][DEOJ_CC]
        elif isinstance(DEOJ_CC, int) and DEOJ_CGC != None:
            deoj_cgc = DEOJ_CGC if isinstance(DEOJ_CGC, int) else self.dictTraverse(eoj_cgc, search=DEOJ_CGC)
            deoj_cc = DEOJ_CC
        else: return -1 # don't accept int DEOJ_CC without providing DEOJ_CGC
        if isinstance(SEOJ_CC, str) and SEOJ_CGC == None:
            scgc_key = self.dictTraverse(eoj_cc, search=SEOJ_CC, key=True)
            seoj_cgc = eoj_cgc[scgc_key]
            seoj_cc = eoj_cc[scgc_key][SEOJ_CC]
        elif isinstance(SEOJ_CC, int) and SEOJ_CGC != None:
            seoj_cgc = SEOJ_CGC if isinstance(SEOJ_CGC, int) else self.dictTraverse(eoj_cgc, search=SEOJ_CGC)
            seoj_cc = SEOJ_CC
        else: return -1 # don't accept int SEOJ_CC without providing SEOJ_CGC
        self.echonet_packet[:] = [0 for _ in self.echonet_packet[:]] # reset global var
        self.echonet_packet[:12] = [ehd['EHD1_ECHONET'], ehd['EHD2_FORMAT1'], TID[0], TID[1], seoj_cgc, seoj_cc, SEOJ_IC, deoj_cgc, deoj_cc, DEOJ_IC, ESV, OPC]
        self.current_echonet_packet_len = 12 # reset current Echonet packet length
        for i in range(OPC):
            if EPC_EDT == [()]:
                target_epc = EPC[i]
                target_pdc = 0
            else:
                target_epc = EPC_EDT[i][0]
                target_pdc = len([EPC_EDT[i][1]]) if not isinstance(EPC_EDT[i][1], list) else len(EPC_EDT[i][1]) # make sure EPC_EDT[i][1] is a list
            if isinstance(target_epc, str): target_epc = self.dictTraverse(epc_edt, search=target_epc)
            self.setnEPC(i+1, target_epc)
            self.setnPDC(i+1, target_pdc)
            if not EPC_EDT == [()]:
                target_edt = self.dictTraverse(epc_edt, search=EPC_EDT[i][1]) if isinstance(EPC_EDT[i][1], str) else EPC_EDT[i][1]
                self.setnEDT(i+1, target_edt)
        return self.echonet_packet[:self.current_echonet_packet_len]

    # Parse Echonet Lite Packet
    # Note: 1. Error,return -1
    #       2. Return values only if value_only is True, else include EPC and unit as tuple (EPC, "x.xx unit")
    #       3. Return raw value if raw_value is True, else auto convert values according to their respective EPC specification
    #       4. Return CGC and CC class info as a list [CGC, CC, (...)] or [CGC, CC, [...]] if class_info is True
    #       5. Support auto conversion for unsigned char, signed char, unsigned short, signed short, unsigned long, signed long
    #       6. TODO: add EDT range validation
    def parsePacket(self, obj, value_only=True, raw_value=False, class_info=False):
        global ehd, eoj_cgc, eoj_cc, esv, epc, epc_edt, il, fd
        try:
            if len(obj) > 12 and obj[0] == ehd['EHD1_ECHONET'] and obj[1] == ehd['EHD2_FORMAT1']:
                self.echonet_packet[:len(obj)] = obj[:]
                return_value = [] # init return value list for parsePacket()
                cgc_str = self.dictTraverse(eoj_cgc, search=obj[4], key=True) # search key to retrieve CGC str
                cc_str = self.dictTraverse(eoj_cc, search=[cgc_str, obj[5]], key=True) # search key to retrieve CC str
                for i in range(obj[11]): # OPC
                    temp_return_value = [] # specially used internally for OPC > 1
                    epc_num = self.getnEPC(i+1)
                    cgc_epc_str = cc_str
                    epc_cgc_str = self.dictTraverse(epc_edt, search=[cgc_epc_str, epc_num], key=True)
                    if epc_cgc_str == None: # handle cases where CC does not have the target EPC code
                        cgc_epc_str = cgc_str
                        epc_cgc_str = self.dictTraverse(epc_edt, search=[cgc_epc_str, epc_num], key=True) # search CGC class for EPC
                    if epc_cgc_str == None: # handle cases where CGC does not have the target EPC code
                        cgc_epc_str = "CGC_SUPERCLASS"
                        epc_cgc_str = self.dictTraverse(epc_edt, search=[cgc_epc_str, epc_num], key=True) # search CGC super class for EPC
                    epc_str = self.dictTraverse(epc_edt, search=[epc_cgc_str, epc_num], key=True)
                    edt = self.getnEDT(i+1) # get EDT list
                    data_type = epc_edt[cgc_epc_str][epc_cgc_str]["data_type"] # get data type for data concatenate or conversion
                    try: unit = epc_edt[cgc_epc_str][epc_cgc_str]["unit"] # get unit for data conversion
                    except: unit = None
                    if data_type == 'unsigned char': # no conversion needed
                        for j in range(len(edt)):
                            char_value = self.dictTraverse(epc_edt, search=[cgc_epc_str, epc_cgc_str, edt[j]], key=True) if raw_value == False else edt[j]
                            if raw_value == False and char_value == 'EDT': char_value = edt[j] # handle cases where key is EDT, return raw value
                            if unit is not None and value_only == False: char_value = str(char_value) + " " + unit.split()[1] if (unit[0].isdigit() and raw_value == False) else str(char_value) + " " + unit # convert to str + unit
                            if value_only == False: temp_return_value.append((epc_cgc_str, char_value))
                            else: temp_return_value.append(char_value)
                    elif data_type == 'signed char': # convert to signed. no need to convert based on unit as they won't be some float values
                        for j in range(len(edt)):
                            char_value = edt[j]
                            if raw_value == False: char_value = char_value if char_value < (1 << 8-1) else char_value - (1 << 8)
                            if unit is not None and value_only == False: char_value = str(char_value) + " " + unit.split()[1] if (unit[0].isdigit() and raw_value == False) else str(char_value) + " " + unit # convert to str + unit
                            if value_only == False: temp_return_value.append((epc_cgc_str, char_value))
                            else: temp_return_value.append(char_value)
                    elif data_type == 'unsigned short' or data_type == 'signed short': # convert to int or float (list if needed)
                        for j in range(int(len(edt)/2)):
                            short_value = edt[(j*2)] << 8 | edt[(j*2)+1] & 0xFF
                            if data_type == 'signed short' and raw_value == False: short_value = short_value if short_value < (1 << 16-1) else short_value - (1 << 16)
                            if unit is not None and raw_value == False: # if unit property exist in EPC, convert
                                try:
                                    unit_only = float(unit.split()[0]) if '.' in unit else int(unit.split()[0]) # try to find int or float
                                    short_value = float(short_value) * unit_only # apply unit to the value
                                except: pass
                            if unit is not None and value_only == False: short_value = str(short_value) + " " + unit.split()[1] if (unit[0].isdigit() and raw_value == False) else str(short_value) + " " + unit # convert to str + unit
                            if value_only == False: temp_return_value.append((epc_cgc_str, short_value))
                            else: temp_return_value.append(short_value)
                    elif data_type == 'unsigned long' or data_type == 'signed long': # convert to int or float (list if needed)
                        for j in range(int(len(edt)/4)):
                            long_value = edt[(j*4)] << 24 | edt[(j*4)+1] << 16 | edt[(j*4)+2] << 8 | edt[(j*4)+3] & 0xFF
                            if data_type == 'signed long' and raw_value == False: long_value = long_value if long_value < (1 << 32-1) else long_value - (1 << 32)
                            if unit is not None and raw_value == False: # if unit property exist in EPC, convert
                                try:
                                    unit_only = float(unit.split()[0]) if '.' in unit else int(unit.split()[0]) # try to find int or float
                                    long_value = float(long_value) * unit_only # apply unit to the value
                                except: pass
                            if unit is not None and value_only == False: long_value = str(long_value) + " " + unit.split()[1] if (unit[0].isdigit() and raw_value == False) else str(long_value) + " " + unit # convert to str + unit
                            if value_only == False: temp_return_value.append((epc_cgc_str, long_value))
                            else: temp_return_value.append(long_value)
                    else:
                        logging.error("parsePacket() data_type {} undefined in function.".format(data_type))
                        return -1
                    if len(temp_return_value) == 1: return_value.append(temp_return_value[0]) # unpack list
                    else: return_value.append(temp_return_value) # return whole list
                if class_info == False:
                    if len(return_value) == 1: return_value = return_value[0] # finally, unpack list
                    return return_value # finally return the values
                else:
                    if len(return_value) == 1: return_value = [cgc_str, cc_str, return_value[0]] # finally, unpack list
                    return [cgc_str, cc_str, return_value] # finally return the values
            else:
                logging.error("parsePacket() invalid Echonet Lite packet.")
                return -1
        except Exception as e:
            logging.exception("parsePacket() exception occurred.")
            return -1

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
        self.assertEqual(self.obj.dictTraverse(eoj_cc, search=[0x04, "CGC_AV_RELATED"], key=True), "CC_NETWORK_CAMERA") # test multi search values for key
        self.assertEqual(self.obj.dictTraverse(epc_edt, search=["CC_TEMPERATURE_SENSOR", 'value', 0xE0], key=True), "EPC_TEMPERATURE_VALUE")
        self.assertEqual(self.obj.dictTraverse(epc_edt, search=["CC_TEMPERATURE_SENSOR", 0xE0], key=True), "EPC_TEMPERATURE_VALUE") # Note: might be based on assumption!

    def test_createPacket(self):
        self.assertEqual(self.obj.createPacket("CC_TEMPERATURE_SENSOR"), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x01, 0x80, 0x00])
        self.assertEqual(self.obj.createPacket("CC_TEMPERATURE_SENSOR", EPC=["EPC_OPERATIONAL_STATUS", "EPC_TEMPERATURE_VALUE"]), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x02, 0x80, 0, 0xE0, 0])
        self.assertEqual(self.obj.createPacket("CC_HOME_AIR_CONDITIONER", ESV='ESV_SetC', EPC_EDT=[("EPC_OPERATIONAL_STATUS",0x30), ("EPC_OPERATION_MODE_SETTING", 0x41)]), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x61, 0x02, 0x80, 0x01, 0x30, 0xB0, 0x01, 0x41])
        self.assertEqual(self.obj.createPacket("CC_HOME_AIR_CONDITIONER", ESV='ESV_SetC', EPC_EDT=[("EPC_OPERATIONAL_STATUS", "on"), ("EPC_OPERATION_MODE_SETTING", "automatic")]), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x01, 0x30, 0x01, 0x61, 0x02, 0x80, 0x01, 0x30, 0xB0, 0x01, 0x41])
        self.assertEqual(self.obj.createPacket(0x11, DEOJ_CGC=0x00), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x01, 0x80, 0x00]) # test whether input raw EOJ_CC and EOJ_CGC
        self.assertEqual(self.obj.createPacket(0x11, DEOJ_CGC="CGC_SENSOR_RELATED"), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x01, 0x80, 0x00]) # test whether input raw EOJ_CC and str EOJ_CGC
        self.assertEqual(self.obj.createPacket("CC_TEMPERATURE_SENSOR", EPC=[0x80, 0xE0]), [0x10, 0x81, 0x00, 0x00, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 0x02, 0x80, 0, 0xE0, 0])

    def test_parsePacket(self):
        test_packet = [0x10, 0x81, 0x00, 0x00, 0x00, 0x11, 0x01, 0x0E, 0xF0, 0x01, 0x72, 0x02, 0x80, 0x01, 0x30, 0xE0, 0x02, 0x00, 0xEB]
        self.assertEqual(self.obj.parsePacket(test_packet), ['on', 23.5])
        self.assertEqual(self.obj.parsePacket(test_packet, raw_value=True), [0x30, 0xEB])
        self.assertEqual(self.obj.parsePacket(test_packet, value_only=False), [('EPC_OPERATIONAL_STATUS', 'on'), ('EPC_TEMPERATURE_VALUE', '23.5 Celsius')])
        self.assertEqual(self.obj.parsePacket(test_packet, value_only=False, raw_value=True), [('EPC_OPERATIONAL_STATUS', 48), ('EPC_TEMPERATURE_VALUE', '235 0.1 Celsius')])
        self.assertEqual(self.obj.parsePacket(test_packet, class_info=True), ['CGC_SENSOR_RELATED', 'CC_TEMPERATURE_SENSOR', ['on', 23.5]])
        self.assertEqual(self.obj.parsePacket(test_packet, value_only=False, class_info=True), ['CGC_SENSOR_RELATED', 'CC_TEMPERATURE_SENSOR', [('EPC_OPERATIONAL_STATUS', 'on'), ('EPC_TEMPERATURE_VALUE', '23.5 Celsius')]])
        self.assertEqual(self.obj.parsePacket(test_packet, value_only=False, raw_value=True , class_info=True), ['CGC_SENSOR_RELATED', 'CC_TEMPERATURE_SENSOR', [('EPC_OPERATIONAL_STATUS', 48), ('EPC_TEMPERATURE_VALUE', '235 0.1 Celsius')]])
                         
if __name__ == '__main__':
    unittest.main()
