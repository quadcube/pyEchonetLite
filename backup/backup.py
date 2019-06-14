#
# Random snippet
#

{
    'CGC_SENSOR_RELATED':           0x00,
    'CGC_AIR_CONDITIONER_RELATED':  0x01,
    'CGC_HOUSING_RELATED':          0x02,
    'CGC_COOKING_RELATED':          0x03,
    'CGC_HEALTH_RELATED':           0x04,
    'CGC_MANAGEMENT_RELATED':       0x05,
    'CGC_AV_RELATED':               0x06,
    'CGC_PROFILE_CLASS':            0x0E,
    'CGC_USER_DEFINITION_CLASS':    0x0F,
}

CGC_SENSOR_RELATED                          = 0x00
CGC_AIR_CONDITIONER_RELATED                 = 0x01
CGC_HOUSING_RELATED                         = 0x02
CGC_COOKING_RELATED                         = 0x03
CGC_HEALTH_RELATED                          = 0x04
CGC_MANAGEMENT_RELATED                      = 0x05
CGC_AV_RELATED                              = 0x06
CGC_PROFILE_CLASS                           = 0x0E
CGC_USER_DEFINITION_CLASS                   = 0x0F

# Echonet Lite Class Group Code (EOJ)
{
    "CGC_SENSOR_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x00
        # Note: Sensor related device class group
        'CC_GAS_LEAK_SENSOR':               0x01,
        'CC_CRIME_PREVENTION_SENSOR':       0x02,
        'CC_EMERGENCY_BUTTON':              0x03,
        'CC_FIRST_AID_SENSOR':              0x04,
        'CC_EARTHQUAKE_SENSOR':             0x05,
        'CC_ELECTRIC_LEAK_SENSOR':          0x06,
        'CC_HUMAN_DETECTION_SENSOR':        0x07,
        'CC_VISITOR_SENSOR':                0x08,
        'CC_CALL_SENSOR':                   0x09,
        'CC_CONDENSATION_SENSOR':           0x0A,
        'CC_AIR_POLLUTION_SENSOR':          0x0B,
        'CC_OXYGEN_SENSOR':                 0x0C,
        'CC_ILLUMINANCE_SENSOR':            0x0D,
        'CC_SOUND_SENSOR':                  0x0E,
        'CC_MAILING_SENSOR':                0x0F,
        'CC_WEIGHT_SENSOR':                 0x10,
        'CC_TEMPERTURE_SENSOR':             0x11,
        'CC_HUMIDITY_SENSOR':               0x12,
        'CC_RAIN_SENSOR':                   0x13,
        'CC_WATER_LEVEL_SENSOR':            0x14,
        'CC_BATH_WATER_LEVEL_SENSOR':       0x15,
        'CC_BATH_HEATING_STATUS_SENSOR':    0x16,
        'CC_WATER_LEAK_SENSOR':             0x17,
        'CC_WATER_OVERFLOW_SENSOR':         0x18,
        'CC_FIRE_SENSOR':                   0x19,
        'CC_CIGARETTE_SMOKE_SENSOR':        0x1A,
        'CC_CO2_SENSOR':                    0x1B,
        'CC_GAS_SENSOR':                    0x1C,
        'CC_VOC_SENSOR':                    0x1D,
        'CC_DIFFERENTIAL_PRESSURE_SENSOR':  0x1E,
        'CC_AIR_SPEED_SENSOR':              0x1F,
        'CC_ODOR_SENSOR':                   0x20,
        'CC_FLAME_SENSOR':                  0x21,
        'CC_ELECTRIC_ENERGY_SENSOR':        0x22,
        'CC_CURRENT_VALUE_SENSOR':          0x23,
        'CC_DAYLIGHT_SENSOR':               0x24,
        'CC_WATER_FLOW_RATE_SENSOR':        0x25,
        'CC_MICROMOTION_SENSOR':            0x26,
        'CC_PASSAGE_SENSOR':                0x27,
        'CC_BED_PRESENCE_SENSOR':           0x28,
        'CC_OPEN_CLOSE_SENSOR':             0x29,
        'CC_ACTIVITY_AMOUNT_SENSOR':        0x2A,
        'CC_HUMAN_BODY_LOCATION_SENSOR':    0x2B,
        'CC_SNOW_SENSOR':                   0x2C,
        'CC_AIR_PRESSURE_SENSOR':           0x2D,
    },
    "CGC_AIR_CONDITIONER_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x01
        # Note: Air-conditional device class group
        'CC_HOME_AIR_CONDITIONER':                      0x30,
        'CC_COLD_BLASTER':                              0x31,
        'CC_ELECTRIC_FAN':                              0x32,
        'CC_VENTILATION_FAN':                           0x33,
        'CC_AIR_CONDITIONER_VENTILATION_FAN':           0x34,
        'CC_AIR_CLEANER':                               0x35,
        'CC_COLD_BLAST_FAN':                            0x36,
        'CC_CIRCULATOR':                                0x37,
        'CC_DEHUMIDIFIER':                              0x38,
        'CC_HUMIDIFIER':                                0x39,
        'CC_CEILING_FAN':                               0x3A,
        'CC_ELECTRIC_KOTATSU':                          0x3B,
        'CC_ELECTRIC_HEATING_PAD':                      0x3C,
        'CC_ELECTRIC_BLANKET':                          0x3D,
        'CC_SPACE_HEATER':                              0x3E,
        'CC_PANEL_HEATER':                              0x3F,
        'CC_ELECTRIC_CARPET':                           0x40,
        'CC_FLOOR_HEATER_0x01':                         0x41,
        'CC_ELECTRIC_HEATER':                           0x42,
        'CC_FAN_HEATER':                                0x43,
        'CC_BATTERY_CHARGER':                           0x44,
        'CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_INDOOR':    0x45,
        'CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_OUTDOOR':   0x46,
        'CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_THERMAL':   0x47,
        'CC_COMMERCIAL_FAN_COIL_UNIT':                  0x48,
        'CC_COMMERCIAL_AIRCOND_COLD_SOURCE_CHILLER':    0x49,
        'CC_COMMERCIAL_AIRCOND_HOT_SOURCE_BOILER':      0x50,
        'CC_AIRCOND_VAV_FOR_COMMERCIAL_APPLICATIONS':   0x51,
        'CC_AIRCOND_FOR_COMMERCIAL_APPLICATIONS':       0x52,
        'CC_UNIT_COOLER':                               0x53,
        'CC_CONDENSING_UNIT_FOR_COMMERCIAL_APP':        0x54,
        'CC_ELECTRIC_STORAGE_HEATER':                   0x55,
},
    "CGC_HOUSING_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x02
        # Note: Housing/facility device class group
        'CC_ELECTRICALLY_OPERATED_BLIND':               0x60,
        'CC_ELECTRICALLY_OPERATED_SHUTTER':             0x61,
        'CC_ELECTRICALLY_OPERATED_CURTAIN':             0x62,
        'CC_ELECTRICALLY_OPERATED_RAIN_SLIDING_DOOR':   0x63,
        'CC_ELECTRICALLY_OPERATED_GATE':                0x64,
        'CC_ELECTRICALLY_OPERATED_WINDOW':              0x65,
        'CC_AUTOMATICALLY_OPERATED_ENTRANCE_DOOR':      0x66,
        'CC_GARDEN_SPRINKLER':                          0x67,
        'CC_FIRE_SPRINKLER':                            0x68,
        'CC_FOUNTAIN':                                  0x69,
        'CC_INSTANTANEOUS_WATER_HEATER':                0x6A,
        'CC_ELECTRIC_WATER_HEATER':                     0x6B,
        'CC_SOLAR_WATER_HEATER':                        0x6C,
        'CC_CIRCULATION_PUMP':                          0x6D,
        'CC_BIDET_EQUIPPED_TOILET':                     0x6E,
        'CC_ELECTRIC_LOCK':                             0x6F,
        'CC_GAS_LINE_VALVE':                            0x70,
        'CC_HOME_SAUNA':                                0x71,
        'CC_HOT_WATER_GENERATOR':                       0x72,
        'CC_BATHROOM_DRYER':                            0x73,
        'CC_HOME_ELEVATOR':                             0x74,
        'CC_ELECTRICALLY_OPERATED_ROOM_DIVIDER':        0x75,
        'CC_HORIZONTAL_TRANSFER':                       0x76,
        'CC_ELECTRICALLY_OPERATED_CLOTH_DRYING_POLE':   0x77,
        'CC_SEPTIC_TANK':                               0x78,
        'CC_HOME_SOLAR_POWER_GENERATION':               0x79,
        'CC_COLD_HOT_WATER_HEAT_SOURCE_EQUIPMENT':      0x7A,
        'CC_FLOOR_HEATER_0x02':                         0x7B,
        'CC_FUEL_CELL':                                 0x7C,
        'CC_STORAGE_BATTERY':                           0x7D,
        'CC_ELECTRIC_VEHICLE_CHARGER_DISCHARGER':       0x7E,
        'CC_ENGINE_COGENERATION':                       0x7F,
        'CC_ELECTRIC_ENERGY_METER':                     0x80,
        'CC_WATER_FLOW_METER':                          0x81,
        'CC_GAS_METER':                                 0x82,
        'CC_LP_GAS_METER':                              0x83,
        'CC_CLOCK':                                     0x84,
        'CC_AUTOMATIC_DOOR':                            0x85,
        'CC_COMMERCIAL_ELEVATOR':                       0x86,
        'CC_DISTRIBUTION_PANEL_METERING':               0x87,
        'CC_LOW_VOLTAGE_SMART_ELECTRIC_ENERGY_METER':   0x88,
        'CC_SMART_GAS_METER':                           0x89,
        'CC_HIGH_VOLTAGE_SMART_ELECTRIC_ENERGY_METER':  0x8A,
        'CC_GENERAL_LIGHTING_CLASS':                    0x90,
        'CC_SINGLE_FUNCTION_LIGHTING':                  0x91,
        'CC_EMERGENCY_LIGHTING':                        0x99,
        'CC_EQUIPMENT_LIGHT':                           0x9D,
        'CC_BUZZER':                                    0xA0,
    },
    "CGC_COOKING_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x03
        # Note: Cooking/Household-related device class group
        'CC_COFFEE_MACHINE':                    0xB0,
        'CC_COFFEE_MILL':                       0xB1,
        'CC_ELECTRIC_HOT_WATER_POT':            0xB2,
        'CC_ELECTRIC_STOVE':                    0xB3,
        'CC_TOASTER':                           0xB4,
        'CC_JUICER_FOOD_MIXER':                 0xB5,
        'CC_FOOD_PROCESSOR':                    0xB6,
        'CC_REFRIGERATOR':                      0xB7,
        'CC_COMBINATION_MICROWAVE_OVEN':        0xB8,
        'CC_COOKING_HEATER':                    0xB9,
        'CC_OVEN':                              0xBA,
        'CC_RICE_COOKER':                       0xBB,
        'CC_ELECTRONIC_JAR':                    0xBC,
        'CC_DISH_WASHER':                       0xBD,
        'CC_DISH_DRYER':                        0xBE,
        'CC_ELECTRIC_RICE_CARD_COOKER':         0xBF,
        'CC_KEEP_WARM_MACHINE':                 0xC0,
        'CC_RICE_MILL':                         0xC1,
        'CC_AUTOMATIC_BREAD_COOKER':            0xC2,
        'CC_SLOW_COOKER':                       0xC3,
        'CC_ELECTRIC_PICKLES_COOKER':           0xC4,
        'CC_WASHING_MACHINE':                   0xC5,
        'CC_CLOTHES_DRYER':                     0xC6,
        'CC_ELECTRIC_IRON':                     0xC7,
        'CC_TROUSER_PRESS':                     0xC8,
        'CC_FUTON_DRYER':                       0xC9,
        'CC_SMALL_ARTICLE_SHOES_DRYER':         0xCA,
        'CC_ELECTRIC_VACUUM_CLEANER':           0xCB,
        'CC_DISPOSER':                          0xCC,
        'CC_ELECTRIC_MOSQUITO_CATCHER':         0xCD,
        'CC_COMMERCIAL_SHOW_CASE':              0xCE,
        'CC_COMMERCIAL_REFRIGERATOR':           0xCF,
        'CC_COMMERCIAL_HOT_CASE':               0xD0,
        'CC_COMMERCIAL_FRYER':                  0xD1,
        'CC_COMMERCIAL_MICROWAVE_OVEN':         0xD2,
        'CC_WASHER_AND_DRYER':                  0xD3,
        'CC_COMMERCIAL_SHOW_CASE_OUTDOOR_UNIT': 0xD4,
},
    "CGC_HEALTH_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x04
        # Note: Health-related device class group
        'CC_WEIGHTING_MACHINE':     0x01,
        'CC_CLINICAL_THERMOMETER':  0x02,
        'CC_BLOOD_PRESSURE_METER':  0x03,
        'CC_BLOOD_SUGAR_METER':     0x04,
        'CC_BODY_FAT_METER':        0x05,
    },
    "CGC_MANAGEMENT_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x05
        # Note: Management/operation-related device class group
        'CC_SECURE_COMM_SHARED_KEY_SETUP_NODE': 0xFC,
        'CC_SWITCH':                            0xFD,
        'CC_PORTABLE_TERMINAL':                 0xFE,
        'CC_CONTROLLER':                        0xFF,
},
    "CGC_AV_RELATED": {
        # Echonet Lite Class Code (EOJ)
        # Class Group Code = 0x06
        # Note: Audiovisual-related device class group
        'CC_DISPLAY':           0x01,
        'CC_TELEVISION':        0x02,
        'CC_AUDIO':             0x03,
        'CC_NETWORK_CAMERA':    0x04,
    },
    "CGC_PROFILE_CLASS": {
        # Echonet Lite Class Code (EOJ)
        # Note: Class Group Code = 0x0E
        'CC_NODE_PROFILE':      0xF0,
},
    "CGC_USER_DEFINITION_CLASS": {
        # Echonet Lite Instance Code (EOJ)
        # Note: 1. Only for Class Code = Profile Class (0x0E)
        #       2. only for Class Group Code = Node Profile Class (0xF0)
        'IC_GENERAL_NODE':              0x01,
        'IC_TRANSMISSION_ONLY_NODE':    0x02,
    },
}

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x00
# Note: Sensor related device class group
CC_GAS_LEAK_SENSOR                          = 0x01
CC_CRIME_PREVENTION_SENSOR                  = 0x02
CC_EMERGENCY_BUTTON                         = 0x03
CC_FIRST_AID_SENSOR                         = 0x04
CC_EARTHQUAKE_SENSOR                        = 0x05
CC_ELECTRIC_LEAK_SENSOR                     = 0x06
CC_HUMAN_DETECTION_SENSOR                   = 0x07
CC_VISITOR_SENSOR                           = 0x08
CC_CALL_SENSOR                              = 0x09
CC_CONDENSATION_SENSOR                      = 0x0A
CC_AIR_POLLUTION_SENSOR                     = 0x0B
CC_OXYGEN_SENSOR                            = 0x0C
CC_ILLUMINANCE_SENSOR                       = 0x0D
CC_SOUND_SENSOR                             = 0x0E
CC_MAILING_SENSOR                           = 0x0F
CC_WEIGHT_SENSOR                            = 0x10
CC_TEMPERTURE_SENSOR                        = 0x11
CC_HUMIDITY_SENSOR                          = 0x12
CC_RAIN_SENSOR                              = 0x13
CC_WATER_LEVEL_SENSOR                       = 0x14
CC_BATH_WATER_LEVEL_SENSOR                  = 0x15
CC_BATH_HEATING_STATUS_SENSOR               = 0x16
CC_WATER_LEAK_SENSOR                        = 0x17
CC_WATER_OVERFLOW_SENSOR                    = 0x18
CC_FIRE_SENSOR                              = 0x19
CC_CIGARETTE_SMOKE_SENSOR                   = 0x1A
CC_CO2_SENSOR                               = 0x1B
CC_GAS_SENSOR                               = 0x1C
CC_VOC_SENSOR                               = 0x1D
CC_DIFFERENTIAL_PRESSURE_SENSOR             = 0x1E
CC_AIR_SPEED_SENSOR                         = 0x1F
CC_ODOR_SENSOR                              = 0x20
CC_FLAME_SENSOR                             = 0x21
CC_ELECTRIC_ENERGY_SENSOR                   = 0x22
CC_CURRENT_VALUE_SENSOR                     = 0x23
CC_DAYLIGHT_SENSOR                          = 0x24
CC_WATER_FLOW_RATE_SENSOR                   = 0x25
CC_MICROMOTION_SENSOR                       = 0x26
CC_PASSAGE_SENSOR                           = 0x27
CC_BED_PRESENCE_SENSOR                      = 0x28
CC_OPEN_CLOSE_SENSOR                        = 0x29
CC_ACTIVITY_AMOUNT_SENSOR                   = 0x2A
CC_HUMAN_BODY_LOCATION_SENSOR               = 0x2B
CC_SNOW_SENSOR                              = 0x2C
CC_AIR_PRESSURE_SENSOR                      = 0x2D

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x01
# Note: Air-conditional device class group
CC_HOME_AIR_CONDITIONER                     = 0x30
CC_COLD_BLASTER                             = 0x31
CC_ELECTRIC_FAN                             = 0x32
CC_VENTILATION_FAN                          = 0x33
CC_AIR_CONDITIONER_VENTILATION_FAN          = 0x34
CC_AIR_CLEANER                              = 0x35
CC_COLD_BLAST_FAN                           = 0x36
CC_CIRCULATOR                               = 0x37
CC_DEHUMIDIFIER                             = 0x38
CC_HUMIDIFIER                               = 0x39
CC_CEILING_FAN                              = 0x3A
CC_ELECTRIC_KOTATSU                         = 0x3B
CC_ELECTRIC_HEATING_PAD                     = 0x3C
CC_ELECTRIC_BLANKET                         = 0x3D
CC_SPACE_HEATER                             = 0x3E
CC_PANEL_HEATER                             = 0x3F
CC_ELECTRIC_CARPET                          = 0x40
CC_FLOOR_HEATER_0x01                        = 0x41
CC_ELECTRIC_HEATER                          = 0x42
CC_FAN_HEATER                               = 0x43
CC_BATTERY_CHARGER                          = 0x44
CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_INDOOR   = 0x45
CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_OUTDOOR  = 0x46
CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_THERMAL  = 0x47
CC_COMMERCIAL_FAN_COIL_UNIT                 = 0x48
CC_COMMERCIAL_AIRCOND_COLD_SOURCE_CHILLER   = 0x49
CC_COMMERCIAL_AIRCOND_HOT_SOURCE_BOILER     = 0x50
CC_AIRCOND_VAV_FOR_COMMERCIAL_APPLICATIONS  = 0x51
CC_AIRCOND_FOR_COMMERCIAL_APPLICATIONS      = 0x52
CC_UNIT_COOLER                              = 0x53
CC_CONDENSING_UNIT_FOR_COMMERCIAL_APP       = 0x54
CC_ELECTRIC_STORAGE_HEATER                  = 0x55

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x02
# Note: Housing/facility device class group
CC_ELECTRICALLY_OPERATED_BLIND              = 0x60
CC_ELECTRICALLY_OPERATED_SHUTTER            = 0x61
CC_ELECTRICALLY_OPERATED_CURTAIN            = 0x62
CC_ELECTRICALLY_OPERATED_RAIN_SLIDING_DOOR  = 0x63
CC_ELECTRICALLY_OPERATED_GATE               = 0x64
CC_ELECTRICALLY_OPERATED_WINDOW             = 0x65
CC_AUTOMATICALLY_OPERATED_ENTRANCE_DOOR     = 0x66
CC_GARDEN_SPRINKLER                         = 0x67
CC_FIRE_SPRINKLER                           = 0x68
CC_FOUNTAIN                                 = 0x69
CC_INSTANTANEOUS_WATER_HEATER               = 0x6A
CC_ELECTRIC_WATER_HEATER                    = 0x6B
CC_SOLAR_WATER_HEATER                       = 0x6C
CC_CIRCULATION_PUMP                         = 0x6D
CC_BIDET_EQUIPPED_TOILET                    = 0x6E
CC_ELECTRIC_LOCK                            = 0x6F
CC_GAS_LINE_VALVE                           = 0x70
CC_HOME_SAUNA                               = 0x71
CC_HOT_WATER_GENERATOR                      = 0x72
CC_BATHROOM_DRYER                           = 0x73
CC_HOME_ELEVATOR                            = 0x74
CC_ELECTRICALLY_OPERATED_ROOM_DIVIDER       = 0x75
CC_HORIZONTAL_TRANSFER                      = 0x76
CC_ELECTRICALLY_OPERATED_CLOTH_DRYING_POLE  = 0x77
CC_SEPTIC_TANK                              = 0x78
CC_HOME_SOLAR_POWER_GENERATION              = 0x79
CC_COLD_HOT_WATER_HEAT_SOURCE_EQUIPMENT     = 0x7A
CC_FLOOR_HEATER_0x02                        = 0x7B
CC_FUEL_CELL                                = 0x7C
CC_STORAGE_BATTERY                          = 0x7D
CC_ELECTRIC_VEHICLE_CHARGER_DISCHARGER      = 0x7E
CC_ENGINE_COGENERATION                      = 0x7F
CC_ELECTRIC_ENERGY_METER                    = 0x80
CC_WATER_FLOW_METER                         = 0x81
CC_GAS_METER                                = 0x82
CC_LP_GAS_METER                             = 0x83
CC_CLOCK                                    = 0x84
CC_AUTOMATIC_DOOR                           = 0x85
CC_COMMERCIAL_ELEVATOR                      = 0x86
CC_DISTRIBUTION_PANEL_METERING              = 0x87
CC_LOW_VOLTAGE_SMART_ELECTRIC_ENERGY_METER  = 0x88
CC_SMART_GAS_METER                          = 0x89
CC_HIGH_VOLTAGE_SMART_ELECTRIC_ENERGY_METER = 0x8A
CC_GENERAL_LIGHTING_CLASS                   = 0x90
CC_SINGLE_FUNCTION_LIGHTING                 = 0x91
CC_EMERGENCY_LIGHTING                       = 0x99
CC_EQUIPMENT_LIGHT                          = 0x9D
CC_BUZZER                                   = 0xA0

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x03
# Note: Cooking/Household-related device class group
CC_COFFEE_MACHINE                           = 0xB0
CC_COFFEE_MILL                              = 0xB1
CC_ELECTRIC_HOT_WATER_POT                   = 0xB2
CC_ELECTRIC_STOVE                           = 0xB3
CC_TOASTER                                  = 0xB4
CC_JUICER_FOOD_MIXER                        = 0xB5
CC_FOOD_PROCESSOR                           = 0xB6
CC_REFRIGERATOR                             = 0xB7
CC_COMBINATION_MICROWAVE_OVEN               = 0xB8
CC_COOKING_HEATER                           = 0xB9
CC_OVEN                                     = 0xBA
CC_RICE_COOKER                              = 0xBB
CC_ELECTRONIC_JAR                           = 0xBC
CC_DISH_WASHER                              = 0xBD
CC_DISH_DRYER                               = 0xBE
CC_ELECTRIC_RICE_CARD_COOKER                = 0xBF
CC_KEEP_WARM_MACHINE                        = 0xC0
CC_RICE_MILL                                = 0xC1
CC_AUTOMATIC_BREAD_COOKER                   = 0xC2
CC_SLOW_COOKER                              = 0xC3
CC_ELECTRIC_PICKLES_COOKER                  = 0xC4
CC_WASHING_MACHINE                          = 0xC5
CC_CLOTHES_DRYER                            = 0xC6
CC_ELECTRIC_IRON                            = 0xC7
CC_TROUSER_PRESS                            = 0xC8
CC_FUTON_DRYER                              = 0xC9
CC_SMALL_ARTICLE_SHOES_DRYER                = 0xCA
CC_ELECTRIC_VACUUM_CLEANER                  = 0xCB
CC_DISPOSER                                 = 0xCC
CC_ELECTRIC_MOSQUITO_CATCHER                = 0xCD
CC_COMMERCIAL_SHOW_CASE                     = 0xCE
CC_COMMERCIAL_REFRIGERATOR                  = 0xCF
CC_COMMERCIAL_HOT_CASE                      = 0xD0
CC_COMMERCIAL_FRYER                         = 0xD1
CC_COMMERCIAL_MICROWAVE_OVEN                = 0xD2
CC_WASHER_AND_DRYER                         = 0xD3
CC_COMMERCIAL_SHOW_CASE_OUTDOOR_UNIT        = 0xD4

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x04
# Note: Health-related device class group
CC_WEIGHTING_MACHINE                        = 0x01
CC_CLINICAL_THERMOMETER                     = 0x02
CC_BLOOD_PRESSURE_METER                     = 0x03
CC_BLOOD_SUGAR_METER                        = 0x04
CC_BODY_FAT_METER                           = 0x05

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x05
# Note: Management/operation-related device class group
CC_SECURE_COMM_SHARED_KEY_SETUP_NODE        = 0xFC
CC_SWITCH                                   = 0xFD
CC_PORTABLE_TERMINAL                        = 0xFE
CC_CONTROLLER                               = 0xFF

# Echonet Lite Class Code (EOJ)
# Class Group Code = 0x06
# Note: Audiovisual-related device class group
CC_DISPLAY                                  = 0x01
CC_TELEVISION                               = 0x02
CC_AUDIO                                    = 0x03
CC_NETWORK_CAMERA                           = 0x04

# Echonet Lite Class Code (EOJ)
# Note: Class Group Code = 0x0E
CC_NODE_PROFILE                             = 0xF0

# Echonet Lite Instance Code (EOJ)
# Note: 1. Only for Class Code = Profile Class (0x0E)
#       2. only for Class Group Code = Node Profile Class (0xF0)
IC_GENERAL_NODE                             = 0x01
IC_TRANSMISSION_ONLY_NODE                   = 0x02

{
    'ESV_SetI':         0x60,
    'ESV_SetC':         0x61,
    'ESV_Get':          0x62,
    'ESV_INF_REQ':      0x63,
    'ESV_SetGet':       0x6E,
    'ESV_Set_Res':      0x71,
    'ESV_Get_Res':      0x72,
    'ESV_INF':          0x73,
    'ESV_INFC':         0x74,
    'ESV_INFC_Res':     0x7A,
    'ESV_SetGet_Res':   0x7E,
    'ESV_SetI_SNA':     0x50,
    'ESV_SetC_SNA':     0x51,
    'ESV_Get_SNA':      0x52,
    'ESV_INF_SNA':      0x53,
    'ESV_SetGet_SNA':   0x5E,
}

# Echonet Lite Service (ESV)
# Note: Service codes for request
ESV_SetI                                    = 0x60
ESV_SetC                                    = 0x61
ESV_Get                                     = 0x62
ESV_INF_REQ                                 = 0x63
ESV_SetGet                                  = 0x6E

# Echonet Lite Service (ESV)
# Note: Service codes for response/notification
ESV_Set_Res                                 = 0x71
ESV_Get_Res                                 = 0x72
ESV_INF                                     = 0x73
ESV_INFC                                    = 0x74
ESV_INFC_Res                                = 0x7A
ESV_SetGet_Res                              = 0x7E

# Echonet Lite Service (ESV)
# Note: Service codes for response not possible
ESV_SetI_SNA                                = 0x50
ESV_SetC_SNA                                = 0x51
ESV_Get_SNA                                 = 0x52
ESV_INF_SNA                                 = 0x53
ESV_SetGet_SNA                              = 0x5E

# Echonet Lite Processing Target Property Counters (OPC)





    "CC_GAS_LEAK_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_GAS_LEAK_OCCURRENCE_STATUS":               "0xB1",
            "EPC_GAS_LEAK_OCCURRENCE_STATUS_RESET":         "0xBF"
        },
        "CC_CRIME_PREVENTION_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_INVASION_OCCURRENCE_STATUS":               "0xB1",
            "EPC_INVASION_OCCURRENCE_STATUS_RESET":         "0xBF"
    },
        "CC_EMERGENCY_BUTTON": {
            "EPC_EMERGENCY_OCCURRENCE_STATUS":              "0xB1",
            "EPC_EMERGENCY_OCCURRENCE_STATUS_RESET":        "0xBF"
},
    "CC_FIRST_AID_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_FIRST_AID_OCCURRENCE_STATUS":              "0xB1",
            "EPC_FIRST_AID_OCCURRENCE_STATUS_RESET":        "0xBF"
        },
        "CC_EARTHQUAKE_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_EARTHQUAKE_OCCURRENCE_STATUS":             "0xB1",
            "EPC_EARTHQUAKE_OCCURRENCE_STATUS_RESET":       "0xBF"
    },
        "CC_ELECTRIC_LEAK_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_ELECTRIC_LEAK_OCCURRENCE_STATUS":          "0xB1",
            "EPC_ELECTRIC_LEAK_OCCURRENCE_STATUS_RESET":    "0xBF"
},
    "CC_HUMAN_DETECTION_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_HUMAN_DETECTION_STATUS":                   "0xB1"
        },
        "CC_VISITOR_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_VISITOR_DETECTION_STATUS":                 "0xB1",
            "EPC_VISITOR_DETECTION_HOLDING_TIME":           "0xBE"
    },
        "CC_CALL_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_CALL_STATUS":                              "0xB1",
            "EPC_CALL_HOLDING_TIME":                        "0xBE"
},
    "CC_CONDENSATION_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_CONDENSATION_DETECTION_STATUS":            "0xB1"
        },
        "CC_AIR_POLLUTION_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL":                "0xB0",
            "EPC_AIR_POLLUTION_DETECTION_STATUS":           "0xB1"
    },
        "CC_OXYGEN_SENSOR": {
            "EPC_MEASURE_OXYGEN_CONCENTRATION_VALUE":       "0xE0"
},
    "CC_ILLUMINANCE_SENSOR": {
        "EPC_MEASURE_ILLUMINANCE_LUX_VALUE": "0xE0",
            "EPC_MEASURE_ILLUMINANCE_KILOLUX_VALUE": "0xE1"
        },
        "CC_SOUND_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_SOUND_DETECTION_STATUS": "0xB1",
            "EPC_SOUND_DETECTION_HOLDING_TIME": "0xBE"
    },
        "CC_MAILING_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_MAILING_DETECTION_STATUS": "0xB1"
},
    "CC_WEIGHT_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_WEIGHT_DETECTION_STATUS": "0xB1"
        },
        "CC_TEMPERTURE_SENSOR": {
            "EPC_MEASURE_TEMPERATURE_VALUE": "0xE0"
    },
        "CC_HUMIDITY_SENSOR": {
            "EPC_MEASURE_HUMIDITY_VALUE": "0xE0"
},
    "CC_RAIN_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_RAIN_DETECTION_STATUS": "0xB1"
        
        },
        "CC_WATER_LEVEL_SENSOR": {
            "EPC_WATER_LEVEL_OVER_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_WATER_LEVEL_OVER_DETECTION_STATUS": "0xB1",
            "EPC_MEASURE_WATER_LEVEL_VALUE": "0xE0"
    },
        "CC_BATH_WATER_LEVEL_SENSOR": {
            "EPC_BATH_WATER_LEVEL_OVER_DETECTION_THRESHOLD_LEVEL":  "0xB0",
            "EPC_BATH_WATER_LEVEL_OVER_DETECTION_STATUS":           "0xB1",
            "EPC_MEASURE_BATH_WATER_LEVEL_VALUE":                   "0xE0"
},
    "CC_BATH_HEATING_STATUS_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL":                        "0xB0",
            "EPC_BATH_HEATING_DETECTION_STATUS":                    "0xB1"
        },
        "CC_WATER_LEAK_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_WATER_LEAK_DETECTION_STATUS": "0xB1"
    },
        "CC_WATER_OVERFLOW_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_WATER_OVERFLOW_DETECTION_STATUS": "0xB1"
},
    "CC_FIRE_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_FIRE_OCCURRENCE_DETECTION_STATUS": "0xB1",
            "EPC_FIRE_OCCURRENCE_DETECTION_STATUS_RESET": "0xBF"
        },
        "CC_CIGARETTE_SMOKE_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_SMOKE_DETECTION_STATUS": "0xB1"
    },
        "CC_CO2_SENSOR": {
            "EPC_MEASURE_CO2_CONCENTRATION_VALUE": "0xE0"
},
    "CC_GAS_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_GAS_DETECTION_STATUS": "0xB1",
            "EPC_MEASURE_GAS_CONCENTRATION_VALUE": "0xE0"
        },
        "CC_VOC_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_VOC_DETECTION_STATUS": "0xB1",
            "EPC_MEASURE_VOC_CONCENTRATION_VALUE": "0xE0"
    },
        "CC_DIFFERENTIAL_PRESSURE_SENSOR": {
            "EPC_MEASURE_DIFFERENTIAL_PRESSURE_VALUE": "0xE0"
},
    "CC_AIR_SPEED_SENSOR": {
        "EPC_MEASURE_AIR_SPEED_VALUE": "0xE0",
            "EPC_AIR_FLOW_DIRECTION": "0xE1"
        },
        "CC_ODOR_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_ODOR_DETECTION_STATUS": "0xB1",
            "EPC_MEASURE_ODOR_VALUE": "0xE0"
    },
        "CC_FLAME_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_FLAME_DETECTION_STATUS": "0xB1",
            "EPC_FLAME_DETECTION_STATUS_RESET": "0xBF"
},
    "CC_ELECTRIC_ENERGY_SENSOR": {
        "EPC_CUMULATIVE_AMOUNT_ELECTRIC_ENERGY":                    "0xE0",
            "EPC_MEDIUM_CAPACITY_SENSOR_INSTANTANEOUS_ELECTRIC_ENERGY": "0xE1",
            "EPC_SMALL_CAPACITY_SENSOR_INSTATANEOUS_ELECTRIC_ENERGY":   "0xE2",
            "EPC_LARGE_CAPACITY_SENSOR_INSTATANEOUS_ELECTRIC_ENERGY":   "0xE3",
            "EPC_CUMULATIVE_AMOUNT_ELECTRIC_ENERGY_MEASUREMENT_LOG":    "0xE4",
            "EPC_EFFECTIVE_VOLTAGE_VALUE":                              "0xE5"
        },
        "CC_CURRENT_VALUE_SENSOR": {
            "EPC_MEASURE_CURRENT_VALUE_1": "0xE0",
            "EPC_RATED_VOLTAGE_TO_BE_MEASURED": "0xE1",
            "EPC_MEASURE_CURRENT_VALUE_2": "0xE2"
    },
        "CC_DAYLIGHT_SENSOR": {
        
        },
        "CC_WATER_FLOW_RATE_SENSOR": {
            "EPC_CUMULATIVE_FLOW_RATE": "0xE0",
            "EPC_FLOW_RATE": "0xE2"
},
    "CC_MICROMOTION_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_MICROMOTION_DETECTION_STATUS": "0xB1",
            "EPC_DETECTION_COUNTER": "0xB2",
            "EPC_SAMPLING_COUNT": "0xBC",
            "EPC_SAMPLING_CYCLE": "0xBD"
        },
        "CC_PASSAGE_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_PASSAGE_DETECTION_HOLD_TIME": "0xBE",
            "EPC_PASSAGE_DETECTION_DIRECTION": "0xE0"
    },
        "CC_BED_PRESENCE_SENSOR": {
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_BED_PRESENCE_DETECTION_STATUS": "0xB1"
},
    "CC_OPEN_CLOSE_SENSOR": {
        "EPC_DEGREE_OF_OPENING_DETECTION_STATUS_1": "0xE0",
            "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_DEGREE_OF_OPENING_DETECTION_STATIS_2": "0xB1"
        },
        "CC_ACTIVITY_AMOUNT_SENSOR": {
            "EPC_ACTIVITY_AMOUNT_LEVEL_1": "0xE0",
            "EPC_MAXIMUM_NUMBER_OF_HUMAN_BODY_ID": "0xE1",
            "EPC_ACTIVITY_AMOUNT_LEVEL_2": "0xE2",
            "EPC_HUMAN_BODY_EXISTENCE_INFORMATION": "0xE3"
    },
        "CC_HUMAN_BODY_LOCATION_SENSOR": {
            "EPC_HUMAN_BODY_DETECTION_LOCATION_1": "0xE0",
            "EPC_MAXIMUM_NUMBER_OF_HUMAN_BODY_ID": "0xE1",
            "EPC_HUMAN_BODY_DETECTION_LOCATION_2": "0xE2",
            "EPC_HUMAN_BODY_EXISTENCE_INFORMATION": "0xE3"
},
    "CC_SNOW_SENSOR": {
        "EPC_DETECTION_THRESHOLD_LEVEL": "0xB0",
            "EPC_SNOW_DETECTION_STATUS": "0xB1"
        },
        "CC_AIR_PRESSURE_SENSOR": {
            "EPC_AIR_PRESSURE_MEASUREMENT": "0xE0"
}
    },
    "CGC_AIR_CONDITIONER_RELATED": {
        "CC_HOME_AIR_CONDITIONER": {
            "EPC_OPERATION_POWER_SAVING":                       "0x8F",
            "EPC_OPERATION_MODE_SETTING":                       "0xB0",
            "EPC_AUTOMATIC_TEMPERATURE_CONTROL_SETTING":        "0xB1",
            "EPC_NORMAL_HIGHSPEED_SILENT_OPERATION_SETTING":    "0xB2",
            "EPC_SET_TEMPERATURE_VALUE":                        "0xB3",
            "EPC_SET_RELATIVE_HUMIDITY_IN_DEHUMIDIFYING_MODE":  "0xB4",
            "EPC_SET_TEMPERATURE_IN_COOLING_MODE":              "0xB5",
            "EPC_SET_TEMPERATURE_IN_HEATING_MODE":              "0xB6",
            "EPC_SET_TEMPERATURE_IN_DEHUMIDIFYING_MODE":        "0xB7",
            "EPC_RATED_POWER_CONSUMPTION":                      "0xB8",
            "EPC_MEASURED_VALUE_OF_CURRENT_CONSUMPTION":        "0xB9",
            "EPC_MEASURED_VALUE_OF_ROOM_RELATIVE_HUMIDITY":     "0xBA",
            "EPC_MEASURED_VALUE_OF_ROOM_TEMPERATURE":           "0xBB",
            "EPC_SET_TEMPERATURE_OF_USER_REMOTE_CONTROL":       "0xBC",
            "EPC_MEASURED_COOLED_AIR_TEMPERATURE":              "0xBD",
            "EPC_MEASURED_OUTDOOR_AIR_TEMPERATURE":             "0xBE",
            "EPC_RELATIVE_TEMPERATURE_SETTING":                 "0xBF",
            "EPC_AIRFLOW_RATE_SETTING":                         "0xA0",
            "EPC_AUTOMATIC_CONTROL_AIRFLOW_DIRECTION_SETTING":  "0xA1",
            "EPC_AUTOMATIC_SWING_AIRFLOW_SETTING":              "0xA3",
            "EPC_AIRFLOW_DIRECTION_VERTICAL_SETTING":           "0xA4",
            "EPC_AIRFLOW_DIRECTION_HORIZONTAL_SETTING":         "0xA5",
            "EPC_SPECIAL_STATE":                                "0xAA",
            "EPC_NON_PRIORITY_STATE":                           "0xAB",
            "EPC_VENTILATION_FUNCTION_SETTING":                 "0xC0",
            "EPC_HUMIDIFIER_FUNCTION_SETTING":                  "0xC1",
            "EPC_VENTILATION_AIR_FLOW_RATE_SETTING":            "0xC2",
            "EPC_DEGREE_OF_HUMIDIFICATION_SETTING":             "0xC4",
            "EPC_MOUNTED_AIR_CLEANING_METHOD":                  "0xC6",
            "EPC_AIR_PURIFIER_FUNCTION_SETTING":                "0xC7",
            "EPC_MOUNTED_AIR_REFRESH_METHOD":                   "0xC8",
            "EPC_AIR_REFRESHER_FUNCTION_SETTING":               "0xC9",
            "EPC_MOUNTED_SELF_CLEANING_METHOD":                 "0xCA",
            "EPC_SELF_CLEANING_FUNCTION_SETTING":               "0xCB",
            "EPC_SPECIAL_FUNCTION_SETTING":                     "0xCC",
            "EPC_OPERATION_STATUS_OF_COMPONENTS":               "0xCD",
            "EPC_THERMOSTAT_SETTING_OVERRIDE_FUNCTION":         "0xCE",
            "EPC_AIR_PURIFICATION_MODE_SETTING":                "0xCF",
            "EPC_ON_TIMER_BASED_RESERVATION_SETTING":           "0x90",
            "EPC_ON_TIMER_SETTING_TIME":                        "0x91",
            "EPC_ON_TIMER_SETTING_RELATIVE_TIME":               "0x92",
            "EPC_OFF_TIMER_BASED_RESERVATION_SETTING":          "0x94",
            "EPC_OFF_TIMER_SETTING_TIME":                       "0x95",
            "EPC_OFF_TIMER_SETTING_RELATIVE_TIME":              "0x96"
        },
        "CC_COLD_BLASTER": {
        
        },
        "CC_ELECTRIC_FAN": {
        
        },
        "CC_VENTILATION_FAN": {
            "EPC_SET_ROOM_RELATIVE_HUMIDITY_VALUE":             "0xB4"
},
    "CC_AIR_CONDITIONER_VENTILATION_FAN": {
        
        },
        "CC_AIR_CLEANER": {
        
        },
        "CC_COLD_BLAST_FAN": {
        
        },
        "CC_CIRCULATOR": {
        
        },
        "CC_DEHUMIDIFIER": {
        
        },
        "CC_HUMIDIFIER": {
        
        },
        "CC_CEILING_FAN": {
        
        },
        "CC_ELECTRIC_KOTATSU": {
        
        },
        "CC_ELECTRIC_HEATING_PAD": {
        
        },
        "CC_ELECTRIC_BLANKET": {
        
        },
        "CC_SPACE_HEATER": {
        
        },
        "CC_PANEL_HEATER": {
        
        },
        "CC_ELECTRIC_CARPET": {
        
        },
        "CC_FLOOR_HEATER_0x01": {
        
        },
        "CC_ELECTRIC_HEATER": {
        
        },
        "CC_FAN_HEATER": {
        
        },
        "CC_BATTERY_CHARGER": {
        
        },
        "CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_INDOOR": {
        
        },
        "CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_OUTDOOR": {
        
        },
        "CC_PACKAGE_TYPE_COMMERCIAL_AIRCOND_THERMAL": {
        
        },
        "CC_COMMERCIAL_FAN_COIL_UNIT": {
        
        },
        "CC_COMMERCIAL_AIRCOND_COLD_SOURCE_CHILLER": {
        
        },
        "CC_COMMERCIAL_AIRCOND_HOT_SOURCE_BOILER": {
        
        },
        "CC_AIRCOND_VAV_FOR_COMMERCIAL_APPLICATIONS": {
        
        },
        "CC_AIRCOND_FOR_COMMERCIAL_APPLICATIONS": {
        
        },
        "CC_UNIT_COOLER": {
        
        },
        "CC_CONDENSING_UNIT_FOR_COMMERCIAL_APP": {
        
        },
        "CC_ELECTRIC_STORAGE_HEATER": {

    }

    },
    "CGC_HOUSING_RELATED": {
        "CC_ELECTRICALLY_OPERATED_BLIND": {
        
        },
        "CC_ELECTRICALLY_OPERATED_SHUTTER": {
        
        },
        "CC_ELECTRICALLY_OPERATED_CURTAIN": {
        
        },
        "CC_ELECTRICALLY_OPERATED_RAIN_SLIDING_DOOR": {
        
        },
        "CC_ELECTRICALLY_OPERATED_GATE": {
        
        },
        "CC_ELECTRICALLY_OPERATED_WINDOW": {
        
        },
        "CC_AUTOMATICALLY_OPERATED_ENTRANCE_DOOR": {
        
        },
        "CC_GARDEN_SPRINKLER": {
        
        },
        "CC_FIRE_SPRINKLER": {
        
        },
        "CC_FOUNTAIN": {
        
        },
        "CC_INSTANTANEOUS_WATER_HEATER": {
        
        },
        "CC_ELECTRIC_WATER_HEATER": {
        
        },
        "CC_SOLAR_WATER_HEATER": {
        
        },
        "CC_CIRCULATION_PUMP": {
        
        },
        "CC_BIDET_EQUIPPED_TOILET": {
        
        },
        "CC_ELECTRIC_LOCK": {
        
        },
        "CC_GAS_LINE_VALVE": {
        
        },
        "CC_HOME_SAUNA": {
        
        },
        "CC_HOT_WATER_GENERATOR": {
        
        },
        "CC_BATHROOM_DRYER": {
        
        },
        "CC_HOME_ELEVATOR": {
        
        },
        "CC_ELECTRICALLY_OPERATED_ROOM_DIVIDER": {
        
        },
        "CC_HORIZONTAL_TRANSFER": {
        
        },
        "CC_ELECTRICALLY_OPERATED_CLOTH_DRYING_POLE": {
        
        },
        "CC_SEPTIC_TANK": {
        
        },
        "CC_HOME_SOLAR_POWER_GENERATION": {
        
        },
        "CC_COLD_HOT_WATER_HEAT_SOURCE_EQUIPMENT": {
        
        },
        "CC_FLOOR_HEATER_0x02": {
        
        },
        "CC_FUEL_CELL": {
        
        },
        "CC_STORAGE_BATTERY": {
        
        },
        "CC_ELECTRIC_VEHICLE_CHARGER_DISCHARGER": {
        
        },
        "CC_ENGINE_COGENERATION": {
        
        },
        "CC_ELECTRIC_ENERGY_METER": {
        
        },
        "CC_WATER_FLOW_METER": {
        
        },
        "CC_GAS_METER": {
        
        },
        "CC_LP_GAS_METER": {
        
        },
        "CC_CLOCK": {
        
        },
        "CC_AUTOMATIC_DOOR": {
        
        },
        "CC_COMMERCIAL_ELEVATOR": {
        
        },
        "CC_DISTRIBUTION_PANEL_METERING": {
        
        },
        "CC_LOW_VOLTAGE_SMART_ELECTRIC_ENERGY_METER": {
        
        },
        "CC_SMART_GAS_METER": {
        
        },
        "CC_HIGH_VOLTAGE_SMART_ELECTRIC_ENERGY_METER": {
        
        },
        "CC_GENERAL_LIGHTING_CLASS": {
        
        },
        "CC_SINGLE_FUNCTION_LIGHTING": {
        
        },
        "CC_EMERGENCY_LIGHTING": {
        
        },
        "CC_EQUIPMENT_LIGHT": {
        
        },
        "CC_BUZZER": {

    }
},
    "CGC_COOKING_RELATED": {
        "CC_COFFEE_MACHINE": {
        
        },
        "CC_COFFEE_MILL": {
        
        },
        "CC_ELECTRIC_HOT_WATER_POT": {
        
        },
        "CC_ELECTRIC_STOVE": {
        
        },
        "CC_TOASTER": {
        
        },
        "CC_JUICER_FOOD_MIXER": {
        
        },
        "CC_FOOD_PROCESSOR": {
        
        },
        "CC_REFRIGERATOR": {
        
        },
        "CC_COMBINATION_MICROWAVE_OVEN": {
        
        },
        "CC_COOKING_HEATER": {
        
        },
        "CC_OVEN": {
        
        },
        "CC_RICE_COOKER": {
        
        },
        "CC_ELECTRONIC_JAR": {
        
        },
        "CC_DISH_WASHER": {
        
        },
        "CC_DISH_DRYER": {
        
        },
        "CC_ELECTRIC_RICE_CARD_COOKER": {
        
        },
        "CC_KEEP_WARM_MACHINE": {
        
        },
        "CC_RICE_MILL": {
        
        },
        "CC_AUTOMATIC_BREAD_COOKER": {
        
        },
        "CC_SLOW_COOKER": {
        
        },
        "CC_ELECTRIC_PICKLES_COOKER": {
        
        },
        "CC_WASHING_MACHINE": {
        
        },
        "CC_CLOTHES_DRYER": {
        
        },
        "CC_ELECTRIC_IRON": {
        
        },
        "CC_TROUSER_PRESS": {
        
        },
        "CC_FUTON_DRYER": {
        
        },
        "CC_SMALL_ARTICLE_SHOES_DRYER": {
        
        },
        "CC_ELECTRIC_VACUUM_CLEANER": {
        
        },
        "CC_DISPOSER": {
        
        },
        "CC_ELECTRIC_MOSQUITO_CATCHER": {
        
        },
        "CC_COMMERCIAL_SHOW_CASE": {
        
        },
        "CC_COMMERCIAL_REFRIGERATOR": {
        
        },
        "CC_COMMERCIAL_HOT_CASE": {
        
        },
        "CC_COMMERCIAL_FRYER": {
        
        },
        "CC_COMMERCIAL_MICROWAVE_OVEN": {
        
        },
        "CC_WASHER_AND_DRYER": {
        
        },
        "CC_COMMERCIAL_SHOW_CASE_OUTDOOR_UNIT": {

    }
    },
    "CGC_HEALTH_RELATED": {
        "CC_WEIGHTING_MACHINE": {
        
        },
        "CC_CLINICAL_THERMOMETER": {
        
        },
        "CC_BLOOD_PRESSURE_METER": {
        
        },
        "CC_BLOOD_SUGAR_METER": {
        
        },
        "CC_BODY_FAT_METER": {

    }
},
    "CGC_MANAGEMENT_RELATED": {
        "CC_SECURE_COMM_SHARED_KEY_SETUP_NODE": {
        
        },
        "CC_SWITCH": {
        
        },
        "CC_PORTABLE_TERMINAL": {
        
        },
        "CC_CONTROLLER": {

    }
    },
    "CGC_AV_RELATED": {
        "CC_DISPLAY": {
        
        },
        "CC_TELEVISION": {
        
        },
        "CC_AUDIO": {
        
        },
        "CC_NETWORK_CAMERA": {

    }
},
    "CGC_PROFILE_CLASS": {
        "CC_NODE_PROFILE": {
            "EPC_UNIQUE_IDENTIFIER_DATA":           "0xBF",
            "EPC_NUMBER_OF_SELF_NODE_INSTANCES":    "0xD3",
            "EPC_NUMBER_OF_SELF_NODE_CLASSES":      "0xD4",
            "EPC_INSTANCE_LIST_NOTIFICATION":       "0xD5",
            "EPC_SELF_NODE_INSTANCE_LIST_S":        "0xD6",
            "EPC_SELF_NODE_CLASS_LIST_S":           "0xD7"
    }
    },
    "CGC_USER_DEFINITION_CLASS": {
        "IC_GENERAL_NODE": {
        
        },
        "IC_TRANSMISSION_ONLY_NODE": {

    }
}
}


# Echonet Lite Property (EPC)
# Note: Super class
EPC_OPERATIONAL_STATUS                      = 0x80
EPC_INSTALLATION_LOCATION                   = 0x81
EPC_STANDARD_VERSION_INFORMATION            = 0x82
EPC_IDENTIFICATION_NUMBER                   = 0x83
EPC_MEASURE_INSTANTANEOUS_POWER_CONSUMPTION = 0x84
EPC_MEASURE_CUMULATIVE_POWER_CONSUMPTION    = 0x85
EPC_MANUFACTURER_FAULT_CODE                 = 0x86
EPC_CURRENT_LIMIT_SETTING                   = 0x87
EPC_FAULT_STATUS                            = 0x88
EPC_FAULT_DESCRIPTION                       = 0x89
EPC_MANUFACTURER_CODE                       = 0x8A
EPC_BUSINESS_FACILITY_CODE                  = 0x8B
EPC_PRODUCT_CODE                            = 0x8C
EPC_PRODUCTION_NUMBER                       = 0x8D
EPC_PRODUCTION_DATE                         = 0x8E
EPC_POWER_SAVING_OPERATIONAL_SETTING        = 0x8F
EPC_REMOTE_CONTROL_SETTING                  = 0x93
EPC_CURRENT_TIME_SETTING                    = 0x97
EPC_CURRENT_DATE_SETTING                    = 0x98
EPC_POWER_LIMIT_SETTING                     = 0x99
EPC_CUMULATIVE_OPERATING_TIME               = 0x9A
EPC_SET_M_PROPERTY_MAP                      = 0x9B
EPC_GET_M_PROPERTY_MAP                      = 0x9C
EPC_STATUS_CHANGE_ANNOUCEMENT_PROPERTY_MAP  = 0x9D
EPC_SET_PROPERTY_MAP                        = 0x9E
EPC_GET_PROPERTY_MAP                        = 0x9F

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Gas Leak Sensor (0x01)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_GAS_LEAK_OCCURRENCE_STATUS              = 0xB1
EPC_GAS_LEAK_OCCURRENCE_STATUS_RESET        = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Crime Prevention Sensor (0x02)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_INVASION_OCCURRENCE_STATUS              = 0xB1
EPC_INVASION_OCCURRENCE_STATUS_RESET        = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Emergency Button (0x03)
EPC_EMERGENCY_OCCURRENCE_STATUS             = 0xB1
EPC_EMERGENCY_OCCURRENCE_STATUS_RESET       = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), First-aid Sensor (0x04)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_FIRST_AID_OCCURRENCE_STATUS             = 0xB1
EPC_FIRST_AID_OCCURRENCE_STATUS_RESET       = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Earthquake Sensor (0x05)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_EARTHQUAKE_OCCURRENCE_STATUS            = 0xB1
EPC_EARTHQUAKE_OCCURRENCE_STATUS_RESET      = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Electric Leak Sensor (0x06)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_ELECTRIC_LEAK_OCCURRENCE_STATUS         = 0xB1
EPC_ELECTRIC_LEAK_OCCURRENCE_STATUS_RESET   = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Human Detection Sensor (0x07)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_HUMAN_DETECTION_STATUS                  = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Visitor Sensor (0x08)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_VISITOR_DETECTION_STATUS                = 0xB1
EPC_VISITOR_DETECTION_HOLDING_TIME          = 0xBE

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Call Sensor (0x09)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_CALL_STATUS                             = 0xB1
EPC_CALL_HOLDING_TIME                       = 0xBE

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Condensation Sensor (0x0A)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_CONDENSATION_DETECTION_STATUS           = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Air Pollution Sensor (0x0B)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_AIR_POLLUTION_DETECTION_STATUS          = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Oxygen Sensor (0x0C)
EPC_MEASURE_OXYGEN_CONCENTRATION_VALUE      = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Illuminance Sensor (0x0D)
EPC_MEASURE_ILLUMINANCE_LUX_VALUE           = 0xE0
EPC_MEASURE_ILLUMINANCE_KILOLUX_VALUE       = 0xE1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Sound Sensor (0x0E)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_SOUND_DETECTION_STATUS                  = 0xB1
EPC_SOUND_DETECTION_HOLDING_TIME            = 0xBE

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Mailing Sensor (0x0F)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_MAILING_DETECTION_STATUS                = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Weight Sensor (0x10)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_WEIGHT_DETECTION_STATUS                 = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Temperature Sensor (0x11)
EPC_MEASURE_TEMPERATURE_VALUE               = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Temperature Sensor (0x12)
EPC_MEASURE_HUMIDITY_VALUE                  = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Rain Sensor (0x13)
EPC_DETECTION_THRESHOLD_LEVEL               = 0xB0
EPC_RAIN_DETECTION_STATUS                   = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Water Level Sensor (0x14)
EPC_WATER_LEVEL_OVER_DETECTION_THRESHOLD_LEVEL              = 0xB0
EPC_WATER_LEVEL_OVER_DETECTION_STATUS                       = 0xB1
EPC_MEASURE_WATER_LEVEL_VALUE                               = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Bath Water Level Sensor (0x15)
EPC_BATH_WATER_LEVEL_OVER_DETECTION_THRESHOLD_LEVEL         = 0xB0
EPC_BATH_WATER_LEVEL_OVER_DETECTION_STATUS                  = 0xB1
EPC_MEASURE_BATH_WATER_LEVEL_VALUE                          = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Bath Heating Status Sensor (0x16)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_BATH_HEATING_DETECTION_STATUS                           = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Water Leak Sensor (0x17)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_WATER_LEAK_DETECTION_STATUS                             = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Water Overflow Sensor (0x18)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_WATER_OVERFLOW_DETECTION_STATUS                         = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Fire Sensor (0x19)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_FIRE_OCCURRENCE_DETECTION_STATUS                        = 0xB1
EPC_FIRE_OCCURRENCE_DETECTION_STATUS_RESET                  = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Cigarette Smoke Sensor (0x1A)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_SMOKE_DETECTION_STATUS                                  = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), CO2 Sensor (0x1B)
EPC_MEASURE_CO2_CONCENTRATION_VALUE                         = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Gas Sensor (0x1C)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_GAS_DETECTION_STATUS                                    = 0xB1
EPC_MEASURE_GAS_CONCENTRATION_VALUE                         = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), VOC Sensor (0x1D)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_VOC_DETECTION_STATUS                                    = 0xB1
EPC_MEASURE_VOC_CONCENTRATION_VALUE                         = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Differential Pressure Sensor (0x1E)
EPC_MEASURE_DIFFERENTIAL_PRESSURE_VALUE                     = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Air Speed Sensor (0x1F)
EPC_MEASURE_AIR_SPEED_VALUE                                 = 0xE0
EPC_AIR_FLOW_DIRECTION                                      = 0xE1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Odor Sensor (0x20)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_ODOR_DETECTION_STATUS                                   = 0xB1
EPC_MEASURE_ODOR_VALUE                                      = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Flame Sensor (0x21)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_FLAME_DETECTION_STATUS                                  = 0xB1
EPC_FLAME_DETECTION_STATUS_RESET                            = 0xBF

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Electric Energy Sensor (0x22)
EPC_CUMULATIVE_AMOUNT_ELECTRIC_ENERGY                       = 0xE0
EPC_MEDIUM_CAPACITY_SENSOR_INSTANTANEOUS_ELECTRIC_ENERGY    = 0xE1
EPC_SMALL_CAPACITY_SENSOR_INSTATANEOUS_ELECTRIC_ENERGY      = 0xE2
EPC_LARGE_CAPACITY_SENSOR_INSTATANEOUS_ELECTRIC_ENERGY      = 0xE3
EPC_CUMULATIVE_AMOUNT_ELECTRIC_ENERGY_MEASUREMENT_LOG       = 0xE4
EPC_EFFECTIVE_VOLTAGE_VALUE                                 = 0xE5

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Current Value Sensor (0x23)
EPC_MEASURE_CURRENT_VALUE_1                                 = 0xE0
EPC_RATED_VOLTAGE_TO_BE_MEASURED                            = 0xE1
EPC_MEASURE_CURRENT_VALUE_2                                 = 0xE2

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Water Flow Rate Sensor (0x25)
EPC_CUMULATIVE_FLOW_RATE                                    = 0xE0
EPC_FLOW_RATE                                               = 0xE2

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Micromotion Sensor (0x26)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_MICROMOTION_DETECTION_STATUS                            = 0xB1
EPC_DETECTION_COUNTER                                       = 0xB2
EPC_SAMPLING_COUNT                                          = 0xBC
EPC_SAMPLING_CYCLE                                          = 0xBD

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Passage Sensor (0x27)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_PASSAGE_DETECTION_HOLD_TIME                             = 0xBE
EPC_PASSAGE_DETECTION_DIRECTION                             = 0xE0

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Bed Presence Sensor (0x28)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_BED_PRESENCE_DETECTION_STATUS                           = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Open/Close Sensor (0x29)
EPC_DEGREE_OF_OPENING_DETECTION_STATUS_1                    = 0xE0
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_DEGREE_OF_OPENING_DETECTION_STATIS_2                    = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Activity Amount Sensor (0x2A)
EPC_ACTIVITY_AMOUNT_LEVEL_1                                 = 0xE0
EPC_MAXIMUM_NUMBER_OF_HUMAN_BODY_ID                         = 0xE1
EPC_ACTIVITY_AMOUNT_LEVEL_2                                 = 0xE2
EPC_HUMAN_BODY_EXISTENCE_INFORMATION                        = 0xE3

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Human Body Location Sensor (0x2B)
EPC_HUMAN_BODY_DETECTION_LOCATION_1                         = 0xE0
EPC_MAXIMUM_NUMBER_OF_HUMAN_BODY_ID                         = 0xE1
EPC_HUMAN_BODY_DETECTION_LOCATION_2                         = 0xE2
EPC_HUMAN_BODY_EXISTENCE_INFORMATION                        = 0xE3

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Snow Sensor (0x2C)
EPC_DETECTION_THRESHOLD_LEVEL                               = 0xB0
EPC_SNOW_DETECTION_STATUS                                   = 0xB1

# Echonet Lite Property (EPC)
# Note: Sensor Class (0x00), Air Pressure Sensor (0x2D)
EPC_AIR_PRESSURE_MEASUREMENT                                = 0xE0

# Echonet Lite Property (EPC)
# Note: Node profile class
EPC_UNIQUE_IDENTIFIER_DATA                                  = 0xBF

# Echonet Lite Property (EPC)
# Note: Node profile class
EPC_NUMBER_OF_SELF_NODE_INSTANCES                           = 0xD3
EPC_NUMBER_OF_SELF_NODE_CLASSES                             = 0xD4
EPC_INSTANCE_LIST_NOTIFICATION                              = 0xD5
EPC_SELF_NODE_INSTANCE_LIST_S                               = 0xD6
EPC_SELF_NODE_CLASS_LIST_S                                  = 0xD7

# Echonet Lite Property (EPC)
# Note: Air Conditioner Related Class (0x01), Home Air Conditioner (0x30)
EPC_AIRCOND_OPERATION_POWER_SAVING                          = 0x8F
EPC_AIRCOND_OPERATION_MODE_SETTING                          = 0xB0
EPC_AIRCOND_AUTOMATIC_TEMPERATURE_CONTROL_SETTING           = 0xB1
EPC_AIRCOND_NORMAL_HIGHSPEED_SILENT_OPERATION_SETTING       = 0xB2
EPC_AIRCOND_SET_TEMPERATURE_VALUE                           = 0xB3
EPC_AIRCOND_SET_RELATIVE_HUMIDITY_IN_DEHUMIDIFYING_MODE     = 0xB4
EPC_AIRCOND_SET_TEMPERATURE_IN_COOLING_MODE                 = 0xB5
EPC_AIRCOND_SET_TEMPERATURE_IN_HEATING_MODE                 = 0xB6
EPC_AIRCOND_SET_TEMPERATURE_IN_DEHUMIDIFYING_MODE           = 0xB7
EPC_AIRCOND_RATED_POWER_CONSUMPTION                         = 0xB8
EPC_AIRCOND_MEASURED_VALUE_OF_CURRENT_CONSUMPTION           = 0xB9
EPC_AIRCOND_MEASURED_VALUE_OF_ROOM_RELATIVE_HUMIDITY        = 0xBA
EPC_AIRCOND_MEASURED_VALUE_OF_ROOM_TEMPERATURE              = 0xBB
EPC_AIRCOND_SET_TEMPERATURE_OF_USER_REMOTE_CONTROL          = 0xBC
EPC_AIRCOND_MEASURED_COOLED_AIR_TEMPERATURE                 = 0xBD
EPC_AIRCOND_MEASURED_OUTDOOR_AIR_TEMPERATURE                = 0xBE
EPC_AIRCOND_RELATIVE_TEMPERATURE_SETTING                    = 0xBF
EPC_AIRCOND_AIRFLOW_RATE_SETTING                            = 0xA0
EPC_AIRCOND_AUTOMATIC_CONTROL_AIRFLOW_DIRECTION_SETTING     = 0xA1
EPC_AIRCOND_AUTOMATIC_SWING_AIRFLOW_SETTING                 = 0xA3
EPC_AIRCOND_AIRFLOW_DIRECTION_VERTICAL_SETTING              = 0xA4
EPC_AIRCOND_AIRFLOW_DIRECTION_HORIZONTAL_SETTING            = 0xA5
EPC_AIRCOND_SPECIAL_STATE                                   = 0xAA
EPC_AIRCOND_NON_PRIORITY_STATE                              = 0xAB
EPC_AIRCOND_VENTILATION_FUNCTION_SETTING                    = 0xC0
EPC_AIRCOND_HUMIDIFIER_FUNCTION_SETTING                     = 0xC1
EPC_AIRCOND_VENTILATION_AIR_FLOW_RATE_SETTING               = 0xC2
EPC_AIRCOND_DEGREE_OF_HUMIDIFICATION_SETTING                = 0xC4
EPC_AIRCOND_MOUNTED_AIR_CLEANING_METHOD                     = 0xC6
EPC_AIRCOND_AIR_PURIFIER_FUNCTION_SETTING                   = 0xC7
EPC_AIRCOND_MOUNTED_AIR_REFRESH_METHOD                      = 0xC8
EPC_AIRCOND_AIR_REFRESHER_FUNCTION_SETTING                  = 0xC9
EPC_AIRCOND_MOUNTED_SELF_CLEANING_METHOD                    = 0xCA
EPC_AIRCOND_SELF_CLEANING_FUNCTION_SETTING                  = 0xCB
EPC_AIRCOND_SPECIAL_FUNCTION_SETTING                        = 0xCC
EPC_AIRCOND_OPERATION_STATUS_OF_COMPONENTS                  = 0xCD
EPC_AIRCOND_THERMOSTAT_SETTING_OVERRIDE_FUNCTION            = 0xCE
EPC_AIRCOND_AIR_PURIFICATION_MODE_SETTING                   = 0xCF
EPC_AIRCOND_ON_TIMER_BASED_RESERVATION_SETTING              = 0x90
EPC_AIRCOND_ON_TIMER_SETTING_TIME                           = 0x91
EPC_AIRCOND_ON_TIMER_SETTING_RELATIVE_TIME                  = 0x92
EPC_AIRCOND_OFF_TIMER_BASED_RESERVATION_SETTING             = 0x94
EPC_AIRCOND_OFF_TIMER_SETTING_TIME                          = 0x95
EPC_AIRCOND_OFF_TIMER_SETTING_RELATIVE_TIME                 = 0x96
