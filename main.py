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

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(module)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
import echonet_lite

udp_queue = queue.Queue()
sock = None # udp socket
echolite_obj = []

def udp_receiver():
    global sock, udp_queue
    while True:
        try:
            received_udp_packet, received_addr = sock.recvfrom(1500)
            udp_queue.put((list(received_udp_packet), received_addr)) # tuple
            logging.debug("Received {} bytes from {}.".format(len(received_udp_packet), received_addr))
        except Exception as e:
            logging.exception("udp_receiver() exception occurred.")

def echonet_parser():
    global udp_queue, echolite_obj
    while True:
        try:
            received_udp_packet, _ = udp_queue.get()
            echolite_obj[0].parsePacket(received_udp_packet)
            udp_queue.task_done() # useful if .join() is implemented
        except Exception as e:
            logging.exception("echonet_parser() exception occurred.")


def echonet_poller():
    global sock, echolite_obj
    while True:
        try:
            sock.sendto(bytes(echolite_obj[0].createPacket("CC_TEMPERATURE_SENSOR", EPC=["EPC_OPERATIONAL_STATUS", "EPC_TEMPERATURE_VALUE"])), ("192.168.2.145", 3610))
            time.sleep(20)
        
        except Exception as e:
            logging.exception("echonet_poller() exception occurred.")

def main():
    global sock, echolite_obj
    try:
        socket.if_nametoindex('ppp0') # check whether the machine is connected to VPN, exception thrown if it's
        ip_addr = (subprocess.check_output(['ifconfig', 'ppp0'])).decode("utf-8").split("inet ")[1].split(" -->")[0]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((ip_addr, 3610))
        print(f"main() IP: {ip_addr}, Port: 3610")
    except OSError as e:
        logging.critical("main() VPN interface not found.")
        sys.exit(0)
    echolite_obj.append(echonet_lite.EchonetLite())
    thread_list = []
    thread_list.append(threading.Thread(target=udp_receiver, args=[]))
    thread_list.append(threading.Thread(target=echonet_parser, args=[]))
    thread_list.append(threading.Thread(target=echonet_poller, args=[]))
    for thread in thread_list:
        thread.daemon = True
        thread.start()
    signal.signal(signal.SIGINT, signal.default_int_handler) # catch SIGINT
    try:
        while True:
            try:
                socket.if_nametoindex('ppp0') # check status of VPN every 10 sec
                time.sleep(10)
            except OSError as e:
                logging.critical("main() VPN disconnected.")
    except KeyboardInterrupt:
        logging.info("main() Ctrl-C received.")
    finally:
        logging.info("main() exiting.")
        sys.exit(0)


if __name__ == '__main__':
    main()
