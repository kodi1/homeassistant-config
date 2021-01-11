# INN-FR-B32
from pymodbus.client import ModbusTcpClient
import ctypes

read_regs = {
    0 : {
            'name': 'T1',
            'desc': 'Air temperature',
            'miltiplyer': 0.1,
        },
    1 : {
            'name': 'T2',
            'desc': 'Hot water temperature H2',
            'miltiplyer': 0.1,
        },
    8 : {
            'name': 'SP',
            'desc': 'Real setpoint',
            'miltiplyer': 0.1,
        },
    15 : {
            'name': 'MOT_SET',
            'desc': 'Motor speed (set)',
            'miltiplyer': 1,
        },
    202 : {
            'name': 'SPL',
            'desc': 'Minimum setpoint',
            'miltiplyer': 0.1,
        },
    203 : {
            'name': 'SPH',
            'desc': 'Maximum setpoint',
            'miltiplyer': 0.1,
        },
    210 : {
            'name': 'MVV5',
            'desc': 'Minimum speed in MIN and Night mode',
            'miltiplyer': 1,
        },
    211 : {
            'name': 'MVV4',
            'desc': 'Maximum speed in Night Mode and Minimum in AUTO',
            'miltiplyer': 1,
        },
    212 : {
            'name': 'MVV3',
            'desc': 'Maximum speed in MIN and Minimum in MAX',
            'miltiplyer': 1,
        },
    230 : {
            'name': 'MVVP3',
            'desc': 'Maximum speed in MIN and Minimum in MAX with Performance enabled',
            'miltiplyer': 1,
        },
    213 : {
            'name': 'MVV2',
            'desc': 'Maximum speed in AUTO',
            'miltiplyer': 1,
        },
    234 : {
            'name': 'MVVP2',
            'desc': 'Maximum speed in AUTO with Performance enabled',
            'miltiplyer': 1,
        },
    214 : {
            'name': 'MVV1',
            'desc': 'Maximum speed in MAX',
            'miltiplyer': 1,
        },
    215 : {
            'name': 'MVVP1',
            'desc': 'Maximum speed in MAX with Performance enabled',
            'miltiplyer': 1,
        },
    218 : {
            'name': 'LLO',
            'desc': 'Minimum water for heating',
            'miltiplyer': 0.1,
        },
    219 : {
            'name': 'LHI',
            'desc': 'Maximum water for cooling',
            'miltiplyer': 0.1,
        },
    231 : {
            'name': 'SP',
            'desc': 'Absolute setpoint value (Note 2)',
            'miltiplyer': 0.1,
        },
    242 : {
            'name': 'OS1',
            'desc': 'T1 air probe offset',
            'miltiplyer': 0.1,
        },
    243 : {
            'name': 'OS2',
            'desc': 'H2 water probe offset',
            'miltiplyer': 0.1,
        },
}

fan_coils_read = {
    'living': {
        'slave': 10,
        'regs': read_regs,
    },
    'bed': {
        'slave': 20,
        'regs': read_regs,
    },
    'office': {
        'slave': 30,
        'regs': read_regs,
    },
}

default_regs = {
    202 : {
            'val': 16,
            'miltiplyer': 0.1,
        },
    203 : {
            'val': 28,
            'miltiplyer': 0.1,
        },
    210 : {
            'val': 400,
            'miltiplyer': 1,
        },
    211 : {
            'val': 550,
            'miltiplyer': 1,
        },
    212 : {
            'val': 680,
            'miltiplyer': 1,
        },
    230 : {
            'val': 920,
            'miltiplyer': 1,
        },
    213 : {
            'val': 1100,
            'miltiplyer': 1,
        },
    234 : {
            'val': 1220,
            'miltiplyer': 1,
        },
    214 : {
            'val': 1500,
            'miltiplyer': 1,
        },
    215 : {
            'val': 1700,
            'miltiplyer': 1,
        },
    218 : {
            'val': 30,
            'miltiplyer': 0.1,
        },
    219 : {
            'val': 20,
            'miltiplyer': 0.1,
        },
    242 : {
            'val': 0,
            'miltiplyer': 0.1,
        },
    243 : {
            'val': 0,
            'miltiplyer': 0.1,
        },
}

fan_coils_write_default = {
    'living': {
        'slave': 10,
        'regs': default_regs,
    },
    'bed': {
        'slave': 20,
        'regs': default_regs,
    },
    'office': {
        'slave': 30,
        'regs': default_regs,
    },
}


fan_coils_write = {
    'living': {
        'slave': 10,
        'regs': {
            242: {
                'val': 0,
                'miltiplyer': 0.1,
            },
        },
    },
    'bed': {
        'slave': 20,
        'regs': {
            242: {
                'val': 0,
                'miltiplyer': 0.1,
            },
        },
    },
    'office': {
        'slave': 30,
        'regs':  {
            242: {
                'val': 0,
                'miltiplyer': 0.1,
            },
        },
    },
}

def read_config():
    for k in fan_coils_read.keys():
        slave = fan_coils_read.get(k).get('slave')
        print('read from %s\tslave %d' % (k, slave))

        for reg, data in fan_coils_read.get(k).get('regs').items():
            result = client.read_input_registers(reg, 1, slave)
            value = int(result.registers[0])
            value = ctypes.c_int16(value).value
            value *= data.get('miltiplyer')
            print('%.1f\t\t%s\t%s' % (value, data.get('name'), data.get('desc')))

        print('')

def write_config(settings):
    for k in settings.keys():
        slave = fan_coils_write.get(k).get('slave')
        print('write to %s\tslave %d' % (k, slave))

        for reg, data in settings.get(k).get('regs').items():
            value = data.get('val')
            value /= data.get('miltiplyer')
            value = int(round(value))
            value = ctypes.c_uint16(value).value

            print('reg %d val %d' % (reg, value))
            client.write_register(reg, value, slave)
        print()

client = ModbusTcpClient('gw_rs485', port=8899, method='rtu')
client.connect()

# write_config(fan_coils_write_default)
# write_config(fan_coils_write)
read_config()

client.close()
