#
#    EETCC Python3
#
 
import socket
import time
import datetime
import subprocess
import threading
import signal
import logging
import sys
import csv
import queue
import echonet_lite

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(module)]s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

udp_queue = queue.Queue()
sock = None # udp socket



def signal_handler(sig, frame):
    global sock
    ECHONET_MSG_SET_AIRCOND[14] = 0x31
    ECHONET_MSG_ENCODED = bytearray(ECHONET_MSG_SET_AIRCOND)
    sock.sendto(ECHONET_MSG_ENCODED, (ECHONET_iHouse_174, 3610))
    print("Aircond OFF! Exiting...")
    sys.exit(0)

def udp_receiver():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("192.168.3.234", ECHONET_PORT))
    while True:
        try:
            received_udp_packet, received_addr = sock.recvfrom(4096)
            udp_queue.put((list(received_udp_packet), received_addr))
            logging.debug("Received {} bytes from {}.".format(len(received_udp_packet), received_addr))
        except Exception as e:
            logging.exception("udp_receiver() exception occurred.")

def echonet_parser():
    global udp_queue
    while True:
        try:
            udp_queue = get()
            if ord(received_udp_packet[4]) == echonet_lite.CGC_SENSOR_RELATED:
                if ord(received_udp_packet[5]) == echonet_lite.CC_TEMPERTURE_SENSOR:
                    # check ip and instance for which sensor probe is this
                    #if received_addr
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_AIR_CONDITIONER_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_HOUSING_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_COOKING_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_HEALTH_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_MANAGEMENT_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_AV_RELATED:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_PROFILE_CLASS:
                print()
            elif ord(received_udp_packet[4]) == echonet_lite.CGC_USER_DEFINITION_CLASS:
                print()
        except Exception as e:
            logging.exception("echonet_parser() exception occurred.")


def echonet_poller():
    while True:
        try:
            print()
        except Exception as e:
            logging.exception("echonet_poller() exception occurred.")

thread_list = []
thread_list.append(threading.Thread(target=udp_receiver, args=[]))
thread_list.append(threading.Thread(target=echonet_parser, args=[]))
for thread in thread_list:
    thread.daemon = True
    thread.start()

signal.signal(signal.SIGINT, signal_handler)
logging.info("...")
