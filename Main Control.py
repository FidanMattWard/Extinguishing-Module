from random import randint
from time import sleep

import paho.mqtt.client as mqtt

ACCESS_TOKENS = {
    'Smoke detector': 'yar6BTNpeURbCLPiGb10',
    'Extinguishing module': 'f6jsiVuPyO38DwhUvMPn',
    'Extract fan': 'VhJ8R25omQOhUid2Tqjx'
}

HOST = 'demo.thingsboard.io'
PORT = 1883


def on_log(client, userdata, level, buf):
    print(f'log: {buf}')


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')


def on_disconnect(client, userdata, flags, rc=0):
    print(f'Disconnected result code - {rc}')


def create_clients():
    clients = {}
    for DEVICE_NAME, TOKEN in ACCESS_TOKENS.items():
        client = mqtt.Client(DEVICE_NAME)
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_log = on_log
        client.username_pw_set(TOKEN)

        clients[DEVICE_NAME] = client
    return clients


CLIENTS = create_clients()


def send_telemetry(concentration, oxygen, flag, delay):
    for DEVICE_NAME, CLIENT in CLIENTS.items():
        CLIENT.connect(HOST, PORT, keepalive=60)
        CLIENT.loop_start()

        if DEVICE_NAME == 'Extinguishing module':
            data = {"concentration": concentration, "flag": flag}
        elif DEVICE_NAME == 'Extract fan':
            data = {"concentration": oxygen}
        else:
            data = {"concentration": concentration}
        data = str(data).lower()
        CLIENT.publish("v1/devices/me/telemetry", data)
        print(f'Publishing {data} to the v1/devices/me/telemetry on the {DEVICE_NAME}.')
        sleep(delay)
        CLIENT.loop_stop()
        CLIENT.disconnect()


def main():
    oxygen = 21
    flag = False
    flag_o = False
    concentration = 5

    while True:
        if flag:
            concentration -= 5
        elif not flag_o:
            concentration = randint(0, 50)

        if flag_o:
            oxygen += 1
            if oxygen >= 21:
                flag_o = False

        if concentration > 30:
            flag = True
        elif concentration <= 5:
            if flag:
                oxygen = 14
                flag_o = True
            flag = False
        print(f'''\033[36m\t\tConcentration of CO is {concentration} ppm
        Oxygen concentration is {oxygen}%
        Extinguishing process is {flag}
        Removal of inergen from the building is {flag_o}\033[0m''')

        try:
            send_telemetry(concentration, oxygen, flag, 5)
        except KeyboardInterrupt:
            print('\n\033[31mManual completion\033[0m')
            send_telemetry(5, 21, False, 5)
            break


if __name__ == "__main__":
    main()
