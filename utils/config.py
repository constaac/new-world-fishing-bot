from yaml import safe_load, dump
from tkinter import IntVar, StringVar, DoubleVar
from utils.global_variables import CONFIG_PATH
from numpy import random


config = safe_load(open(CONFIG_PATH))

dict = {
    'fishing':{
      'x': IntVar(value=config['fishing']['x']),
      'y': IntVar(value=config['fishing']['y']),
      'width': IntVar(value=config['fishing']['width']),
      'height': IntVar(value=config['fishing']['height']),
      'cast_strength': IntVar(value=config['fishing']['cast_strength']),
      'timeouts':{
        'loop': {
          'min': config['fishing']['timeouts']['loop']['min'],
          'max': config['fishing']['timeouts']['loop']['max']
        },
        'notice': {
          'min': config['fishing']['timeouts']['notice']['min'],
          'max': config['fishing']['timeouts']['notice']['max']
        },
        'reeling': {
          'min': config['fishing']['timeouts']['reeling']['min'],
          'max': config['fishing']['timeouts']['reeling']['max']
        },
        'pause': {
          'min': config['fishing']['timeouts']['pause']['min'],
          'max': config['fishing']['timeouts']['pause']['max']
        },
        'cast_min': {
          'min': config['fishing']['timeouts']['cast_min']['min'],
          'max': config['fishing']['timeouts']['cast_min']['max']
        },
        'cast_shallow': {
          'min': config['fishing']['timeouts']['cast_shallow']['min'],
          'max': config['fishing']['timeouts']['cast_shallow']['max']
        },
        'cast_deep': {
          'min': config['fishing']['timeouts']['cast_deep']['min'],
          'max': config['fishing']['timeouts']['cast_deep']['max']
        },
        'cast_max': {
          'min': config['fishing']['timeouts']['cast_max']['min'],
          'max': config['fishing']['timeouts']['cast_max']['max']
        },
        "afk": {
          'min': config['fishing']['timeouts']['afk']['min'],
          'max': config['fishing']['timeouts']['afk']['max']
        },
        "afk_strafe_return": {
          'min': config['fishing']['timeouts']['afk']['min'],
          'max': config['fishing']['timeouts']['afk']['max']
        }
      }
    },
    'repairing':{
      'x': IntVar(value=config['repairing']['x']),
      'y': IntVar(value=config['repairing']['y']),
      'length': IntVar(value=config['repairing']['length']),
      'every': IntVar(value=config['repairing']['every']),
      'enable': IntVar(value=config['repairing']['enable']),
      'enable_afk_break': IntVar(value=config['repairing']['enable_afk_break']),
      'timeouts': {
        'arm_disarm': {
          'min': config['repairing']['timeouts']['arm_disarm']['min'],
          'max': config['repairing']['timeouts']['arm_disarm']['max']
        },
        'inventory': {
          'min': config['repairing']['timeouts']['inventory']['min'],
          'max': config['repairing']['timeouts']['inventory']['max']
        },
        'repair': {
          'min': config['repairing']['timeouts']['repair']['min'],
          'max': config['repairing']['timeouts']['repair']['max']
        },
        'confirm': {
          'min': config['repairing']['timeouts']['confirm']['min'],
          'max': config['repairing']['timeouts']['confirm']['max']
        }
      }
    },
    'bait':{
      'bait_x': IntVar(value=config['bait']['bait_x']),
      'bait_y': IntVar(value=config['bait']['bait_y']),
      'equip_button_x': IntVar(value=config['bait']['equip_button_x']),
      'equip_button_y': IntVar(value=config['bait']['equip_button_y']),
      'length': IntVar(value=config['bait']['length']),
      'enable': IntVar(value=config['bait']['enable']),
      'timeouts': {
        'select': {
          'min': config['bait']['timeouts']['select']['min'],
          'max': config['bait']['timeouts']['select']['max']
        },
        'confirm': {
          'min': config['bait']['timeouts']['confirm']['min'],
          'max': config['bait']['timeouts']['confirm']['max']
        }
      }
    },
    'keybinds':{
      'forward': StringVar(value=config['keybinds']['forward']),
      'backward': StringVar(value=config['keybinds']['backward']),
      'strafe_left': StringVar(value=config['keybinds']['strafe_left']),
      'strafe_right': StringVar(value=config['keybinds']['strafe_right']),
      'free_look': StringVar(value=config['keybinds']['free_look']),
      'jump': StringVar(value=config['keybinds']['jump']),
      'interact': StringVar(value=config['keybinds']['interact']),
      'arm_disarm_fishing_rod': StringVar(value=config['keybinds']['arm_disarm_fishing_rod']),
      'open_inventory': StringVar(value=config['keybinds']['open_inventory']),
      'bait': StringVar(value=config['keybinds']['bait'])
    },
    'colors':{
      'green': (config['colors']['green']['r'], config['colors']['green']['g'], config['colors']['green']['b']),
      'brown': (config['colors']['brown']['r'], config['colors']['brown']['g'], config['colors']['brown']['b']),
      'red': (config['colors']['red']['r'], config['colors']['red']['g'], config['colors']['red']['b'])
    },
    'resolution':{
      'x': config['resolution']['x'],
      'y': config['resolution']['y']
    },
    'log_lvl': config['log_lvl']
  }

def save_data():
    d = {
    'fishing':{
      'x': dict['fishing']['x'].get(),
      'y': dict['fishing']['y'].get(),
      'width': dict['fishing']['width'].get(),
      'height': dict['fishing']['height'].get(),
      'cast_strength': dict['fishing']['cast_strength'].get(),
      'timeouts':{
        'loop': {
          'min': dict['fishing']['timeouts']['loop']['min'],
          'max': dict['fishing']['timeouts']['loop']['max']
        },
        'notice': {
          'min': dict['fishing']['timeouts']['notice']['min'],
          'max': dict['fishing']['timeouts']['notice']['max']
        },
        'reeling': {
          'min': dict['fishing']['timeouts']['reeling']['min'],
          'max': dict['fishing']['timeouts']['reeling']['max']
        },
        'pause': {
          'min': dict['fishing']['timeouts']['pause']['min'],
          'max': dict['fishing']['timeouts']['pause']['max']
        },
        'cast_min': {
          'min': dict['fishing']['timeouts']['cast_min']['min'],
          'max': dict['fishing']['timeouts']['cast_min']['max']
        },
        'cast_shallow': {
          'min': dict['fishing']['timeouts']['cast_max']['min'],
          'max': dict['fishing']['timeouts']['cast_max']['max']
        },
        'cast_deep': {
          'min': dict['fishing']['timeouts']['cast_deep']['min'],
          'max': dict['fishing']['timeouts']['cast_deep']['max']
        },
        'cast_max': {
          'min': dict['fishing']['timeouts']['cast_max']['min'],
          'max': dict['fishing']['timeouts']['cast_max']['max']
        },
        'afk': {
          'min': dict['fishing']['timeouts']['afk']['min'],
          'max': dict['fishing']['timeouts']['afk']['max']
        },
        'afk_strafe_return': {
          'min': dict['fishing']['timeouts']['afk']['min'],
          'max': dict['fishing']['timeouts']['afk']['max']
        }
      }
    },
    'repairing':{
      'x': dict['repairing']['x'].get(),
      'y': dict['repairing']['y'].get(),
      'length': dict['repairing']['length'].get(),
      'every': dict['repairing']['every'].get(),
      'enable': dict['repairing']['enable'].get(),
      'enable_afk_break': dict['repairing']['enable_afk_break'].get(),
      'timeouts': {
        'arm_disarm': {
          'min': dict['repairing']['timeouts']['arm_disarm']['min'],
          'max': dict['repairing']['timeouts']['arm_disarm']['max']
        },
        'inventory': {
          'min': dict['repairing']['timeouts']['inventory']['min'],
          'max': dict['repairing']['timeouts']['inventory']['max']
        },
        'repair': {
          'min': dict['repairing']['timeouts']['repair']['min'],
          'max': dict['repairing']['timeouts']['repair']['max']
        },
        'confirm': {
          'min': dict['repairing']['timeouts']['confirm']['min'],
          'max': dict['repairing']['timeouts']['confirm']['max']
        }
      }
    },
    'bait':{
      'bait_x': dict['bait']['bait_x'].get(),
      'bait_y': dict['bait']['bait_y'].get(),
      'equip_button_x': dict['bait']['equip_button_x'].get(),
      'equip_button_y': dict['bait']['equip_button_y'].get(),
      'length': dict['bait']['length'].get(),
      'enable': dict['bait']['enable'].get(),
      'timeouts': {
        'select': {
          'min': dict['bait']['timeouts']['select']['min'],
          'max': dict['bait']['timeouts']['select']['max']
        },
        'confirm': {
          'min': dict['bait']['timeouts']['confirm']['min'],
          'max': dict['bait']['timeouts']['confirm']['max']
        }
      }
    },
    'keybinds':{
      'forward': config['keybinds']['forward'],
      'backward': config['keybinds']['backward'],
      'strafe_left': config['keybinds']['strafe_left'],
      'strafe_right': config['keybinds']['strafe_right'],
      'free_look': config['keybinds']['free_look'],
      'jump': config['keybinds']['jump'],
      'interact': config['keybinds']['interact'],
      'arm_disarm_fishing_rod': config['keybinds']['arm_disarm_fishing_rod'],
      'open_inventory': config['keybinds']['open_inventory'],
      'bait': config['keybinds']['bait']
    },
    'colors':{
      'green': {
        'r': dict['colors']['green'][0],
        'g': dict['colors']['green'][1],
        'b': dict['colors']['green'][2]
      },
      'brown': {
        'r': dict['colors']['brown'][0],
        'g': dict['colors']['brown'][1],
        'b': dict['colors']['brown'][2]
      },
      'red': {
        'r': dict['colors']['red'][0],
        'g': dict['colors']['red'][1],
        'b': dict['colors']['red'][2]
      }
    },
    'resolution':{
      'x': dict['resolution']['x'],
      'y': dict['resolution']['y']
    },
    'log_lvl': dict['log_lvl']
    }
    with open(CONFIG_PATH, 'w') as yaml_file:
        dump(d, yaml_file, sort_keys=False)

def random_timeout(key):
    upper_limit = float(key['max'])
    lower_limit = float(key['min'])

    loc = (upper_limit + lower_limit) / 2
    scale = (upper_limit - lower_limit) / 4

    sample = random.normal(loc, scale)

    return round(min(max(sample, lower_limit), upper_limit),2)
