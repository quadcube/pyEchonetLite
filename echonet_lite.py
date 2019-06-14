#
#    Echonet Lite Python 3
#
import logging
import unittest

"""
    Echonet Lite Functions
    Note: 1. functions are similar to the C version Echonet Lite library, removed some of the simpler functions such as echonet_setEHD1(), etc. and changed the return failed response to -1 for get() functions
          2. functions that deals directly with echonet_packet (global variable) must be executed in sequence (e.g.: setPacket -> setnEPC -> setnPDC -> setnEDT)
          3. functions are thread safe as long as functions in each instances (classes) are sequentially called
"""
class EchonetLite:
    def __init__(self):
        MAX_ECHONET_PACKET_LEN = 64
        self.echonet_packet = [0] * MAX_ECHONET_PACKET_LEN # pre-allocate echonet lite packet structure
    
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
    # Note: 1. property_data_list must be a list
    def setnEDT(self, n, property_data_list):
        j, k = 0, 0
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

    # Set Echonet Lite Packet (without Echonet Lite Property Setting and Data: EPC,PDC,EDT)
    # Note: 1. tid16 can accept both single 16 bit integer and two 8 bit integer list
    def setPacket(self, ehd1, ehd2, tid16, seoj_cgc, seoj_cc, seoj_ic, deoj_cgc, deoj_cc, deoj_ic, esv, opc):
        if type(tid16) is not list:
            tid16 = [tid16 >> 8, tid16 & 0x00ff]
        self.echonet_packet[:12] = [ehd1, ehd2, tid16[0], tid16[1], seoj_cgc, seoj_cc, seoj_ic, deoj_cgc, deoj_cc, deoj_ic, esv, opc]

# def getOperationalStatus(ip_addr, )


"""
    Echonet Lite Function Test Units
    Note: 1. covers all functions that deals directly with echonet_packet (global variable)
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
    
    def test_setPacket(self):
        self.obj.setPacket(0x10, 0x81, [0x00, 0x01], 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test list tid16, tid16 = [0x00, 0x01]
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.setPacket(0x10, 0x81, 0x01, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0x01
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.setPacket(0x10, 0x81, 0x01FF, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0x01FF
        self.sample[2:4] = [0x01, 0xFF] # tid16 = 0x01FF
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)
        self.obj.setPacket(0x10, 0x81, 0xF103, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0xF103
        self.sample[2:4] = [0xF1, 0x03] # tid16 = 0xF103
        self.assertEqual(self.obj.echonet_packet[:len(self.sample)], self.sample)






















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
