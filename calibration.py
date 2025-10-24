import math
import marimo as mo
import pandas as pd
import numpy as np

g = 9.80665

# Hardcoded experiment data
motor_off_1 = [
    {
      "timestamp": 66040,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -693,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66069,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -678,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66084,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66102,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -695,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66157,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -730,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66246,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -759,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66336,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -735,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66425,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -675,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66515,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -715,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66605,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -737,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66694,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -657,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66784,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -673,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66873,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -671,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 66963,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -654,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_2 = [
    {
      "timestamp": 68285,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -605,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68314,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -677,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68328,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68346,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -674,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68396,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -658,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68485,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -641,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68575,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -677,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68665,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -693,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68754,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -616,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68844,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -664,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 68933,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -688,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69023,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -682,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69112,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -635,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69202,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -632,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69291,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -675,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69381,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -677,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69470,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -678,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69560,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -644,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69650,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -639,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69739,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -671,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69829,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -634,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 69918,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -608,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 70008,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -672,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 70097,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -648,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 70187,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -660,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 70277,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -736,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_3 = [
    {
      "timestamp": 71770,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -705,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 71799,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -684,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 71813,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 71832,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -667,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 71889,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -672,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 71978,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -720,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72068,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -773,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72157,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -745,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72247,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -714,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72336,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -719,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72426,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -691,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72515,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -765,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72605,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -796,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72695,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -759,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72784,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -682,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72874,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -673,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 72963,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -685,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73053,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -758,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73142,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -796,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73232,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -761,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73321,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -743,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73411,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -749,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73501,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -766,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73590,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -765,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 73680,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -744,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_1 = [
    {
      "timestamp": 235172,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2228,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235201,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2211,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235280,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2251,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235370,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2262,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235459,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2238,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235549,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2206,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235638,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2248,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235728,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2276,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235817,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2240,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235907,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2265,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 235997,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2241,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236086,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2228,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236176,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2248,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236266,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2257,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236355,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2300,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236445,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2285,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236534,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2257,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236624,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2203,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236713,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2233,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236803,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2249,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236893,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2315,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 236982,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2262,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 237072,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2246,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 237161,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2315,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_2 = [
    {
      "timestamp": 231748,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2216,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 231778,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2183,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 231792,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 231810,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2209,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 231875,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2206,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 231965,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2203,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232054,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2250,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232144,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2248,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232234,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2210,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232323,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2180,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232413,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2229,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232502,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2236,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232592,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2202,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232681,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2175,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232771,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2194,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232861,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2197,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 232950,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2225,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233040,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2221,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233130,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2239,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233219,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2228,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233309,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2210,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233398,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2189,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233488,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2181,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233578,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2214,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 233667,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2177,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_3 = [
    {
      "timestamp": 229470,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2203,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229500,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2202,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229546,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2258,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229635,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2236,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229725,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2228,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229815,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -2193,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229904,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -2195,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 229994,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2174,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 230083,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2162,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 230173,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2175,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 230263,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -2148,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 230352,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2122,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 230441,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -2140,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_plus_weight_1 = [
    {
      "timestamp": 341311,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95811,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341340,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95773,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341358,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341376,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95780,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341452,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95817,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341541,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95733,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341631,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95711,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341720,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95710,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341810,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -95723,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341900,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95734,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 341989,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95725,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342079,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95739,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342168,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95726,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342258,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95742,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342348,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95745,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342437,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95690,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342527,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95745,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342616,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95711,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342706,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95743,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342796,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95714,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342885,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95648,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 342975,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95693,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 343064,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -95709,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 343154,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95681,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 343244,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95661,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_plus_weight_2 = [
    {
      "timestamp": 337842,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -95968,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 337872,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95977,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 337886,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 337904,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95945,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 337957,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95920,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338047,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95918,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338136,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95914,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338226,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95936,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338316,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95876,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338405,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95863,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338495,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95885,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338584,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95926,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338674,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95940,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338763,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95932,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338853,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95917,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 338943,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -95884,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339032,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95890,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339122,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95893,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339211,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95917,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339301,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95938,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339391,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95890,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339480,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95825,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339570,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95860,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339659,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -95917,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339749,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95908,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 339839,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95842,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

motor_off_vertical_plus_weight_3 = [
    {
      "timestamp": 335540,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -96034,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335570,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95961,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335628,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95960,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335717,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -96011,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335807,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -95972,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335896,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95964,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 335986,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -95996,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 336076,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -96015,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 336165,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -96064,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 336255,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -96024,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 336344,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95933,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 336434,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -95939,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_1 = [
    {
      "timestamp": 556763,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76616,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 556792,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76466,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 556806,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 556824,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76564,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 556889,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76831,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 556979,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77088,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557068,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77247,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557158,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77020,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557248,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76692,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557337,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76334,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557427,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76159,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557516,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76383,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557606,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 2.5
      },
      "load_cell": {
        "raw_value": -76637,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557696,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76720,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557785,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76950,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557875,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77053,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 557965,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77044,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558054,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77226,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558144,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77227,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558234,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77045,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558323,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76813,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558413,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76457,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558503,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76270,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558592,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -76303,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 558682,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76551,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_2 = [
    {
      "timestamp": 553304,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -75936,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553333,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -75919,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553393,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -75907,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553483,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -75876,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553572,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76234,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553662,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76743,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553752,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77108,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553841,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77437,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 553931,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77466,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554021,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77320,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554110,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77165,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554200,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77177,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554289,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76868,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554379,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76677,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554469,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76611,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554558,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -76435,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554648,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -76629,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554738,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77333,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554827,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -78307,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 554917,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -78918,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 555006,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -79170,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 555096,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -78876,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 555186,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -78401,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 555275,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77967,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_3 = [
    {
      "timestamp": 551014,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77563,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551042,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77919,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551059,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": 110149,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551077,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -78190,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551153,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77987,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551242,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -78072,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551332,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77770,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551422,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77361,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551511,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -77360,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551601,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -77632,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551691,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77675,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551780,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -77505,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551870,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77360,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 551959,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -77154,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_pm_1 = [
    {
      "timestamp": 653153,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175916,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653183,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175898,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653233,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -175897,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653322,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175921,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653412,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175863,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653502,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175766,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653591,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175776,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653681,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175724,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653771,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175787,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653860,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175883,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 653950,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175841,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654039,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175898,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654129,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175907,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654219,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175860,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654308,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175844,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654398,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175883,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654488,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175849,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654577,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175802,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654667,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175807,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654756,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175729,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654846,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175724,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 654936,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175781,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 655025,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175833,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 655115,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175814,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_pm_2 = [
    {
      "timestamp": 649732,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -2.5
      },
      "load_cell": {
        "raw_value": -176112,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 649761,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176059,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 649827,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176006,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 649917,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -176022,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650007,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175981,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650096,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176031,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650186,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176058,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650275,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -176034,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650365,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176021,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650455,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175997,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650544,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -176058,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650634,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176000,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650724,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175996,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650813,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175922,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650903,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -175855,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 650992,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175912,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651082,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -175921,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651172,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175970,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651261,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176030,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651351,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 1.25
      },
      "load_cell": {
        "raw_value": -176008,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651440,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176008,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651530,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -176016,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651620,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175949,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 651709,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -175905,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

off_200g_pm_3 = [
    {
      "timestamp": 647425,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -176282,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647455,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176307,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647497,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176262,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647587,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176194,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647677,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176206,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647766,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176253,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647856,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176220,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 647946,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176168,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 648035,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176187,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 648125,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176187,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 648214,
      "ina260": {
        "voltage_v": 0,
        "current_ma": 0
      },
      "load_cell": {
        "raw_value": -176210,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 648304,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176295,
        "is_ready": True
      },
      "set_speed": 0
    },
    {
      "timestamp": 648394,
      "ina260": {
        "voltage_v": 0,
        "current_ma": -1.25
      },
      "load_cell": {
        "raw_value": -176252,
        "is_ready": True
      },
      "set_speed": 0
    }
  ]

def flatten_dict(d, parent_key='', sep='__'):
    """
    Recursively flattens a nested dictionary.
    """
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def to_dataframe(data, sep='__'):
    """
    Converts a list of nested dictionaries into a flattened pandas DataFrame.
    """
    flat_data = [flatten_dict(entry, sep=sep) for entry in data]
    return pd.DataFrame(flat_data)

def get_dataframe(file_1, file_2, file_3):
    files_data = file_1 + file_2 + file_3
    df = to_dataframe(files_data)
    df = df.sort_values("timestamp",ascending=True).reset_index(drop=True)
    return df

df_cal_1 = get_dataframe(motor_off_1, motor_off_2, motor_off_3)
df_cal_2 = get_dataframe(motor_off_vertical_3, motor_off_vertical_3, motor_off_vertical_3)
df_cal_3 = get_dataframe(motor_off_vertical_plus_weight_1, motor_off_vertical_plus_weight_2, motor_off_vertical_plus_weight_3)
df_cal_4 = get_dataframe(off_200g_1, off_200g_2, off_200g_3)
df_cal_5 = get_dataframe(off_200g_pm_1, off_200g_pm_2, off_200g_pm_3)

# Calculate conversion factor CF
# value delta attributable to 200g
CF_1 = (float(df_cal_4["load_cell__raw_value"].median()) - float(df_cal_2["load_cell__raw_value"].median()))/(0.2*(-g))
# value delta attributable to 200g
CF_2 = (float(df_cal_5["load_cell__raw_value"].median()) - float(df_cal_3["load_cell__raw_value"].median()))/(0.2*(-g))
# average both factors
CF = float(np.average([CF_1, CF_2]))
print("Calibration Factor", CF, CF_1, CF_2)


# Calculate engine weight
engine_F1 = (float(df_cal_3["load_cell__raw_value"].median()) - float(df_cal_2["load_cell__raw_value"].median()))/CF
engine_w1 = engine_F1/g # Force in Newtons to weight in kgs
print("Engine 1", engine_F1, engine_w1)

# Calculate engine weight
engine_F2 = (float(df_cal_5["load_cell__raw_value"].median()) - float(df_cal_4["load_cell__raw_value"].median()))/CF
engine_w2 = engine_F2/g # Force in Newtons to weight in kgs
print("Engine 2", engine_F2, engine_w2)