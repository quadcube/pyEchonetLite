#
#    Echonet Lite Python 3
#
import logging
import unittest

# Echonet Lite Header 1 (EHD1)
# Note: Conventional Echonet (0b00010000)
EHD1_ECHONET                                = 0x10

# Echonet Lite Header 2 (EHD2)
# Note: Specified message format (FORMAT 1)
# Arbitrary message formar (FORMAT 2)
EHD2_FORMAT1                                = 0x81
EHD2_FORMAT2                                = 0x82

# Echonet Lite Class Group Code (EOJ)
CGC_SENSOR_RELATED                          = 0x00
CGC_AIR_CONDITIONER_RELATED                 = 0x01
CGC_HOUSING_RELATED                         = 0x02
CGC_COOKING_RELATED                         = 0x03
CGC_HEALTH_RELATED                          = 0x04
CGC_MANAGEMENT_RELATED                      = 0x05
CGC_AV_RELATED                              = 0x06
CGC_PROFILE_CLASS                           = 0x0E
CGC_USER_DEFINITION_CLASS                   = 0x0F

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

# Echonet Lite Operation Status (Property)
OS_ON                                       = 0x30
OS_OFF                                      = 0x31

# Echonet Lite Installation Location (Property)
# According to Specification Appendix Table 2-2
# Note: Location number set to 000 (last 3 bit are not specified)
IL_LIVING_ROOM                              = 0b00001000
IL_DINING_ROOM                              = 0b00010000
IL_KITCHEN                                  = 0b00011000
IL_BATHROOM                                 = 0b00100000
IL_LAVATORY                                 = 0b00101000
IL_CHANGING_ROOM                            = 0b00110000
IL_PASSAGEWAY                               = 0b00111000
IL_ROOM                                     = 0b01000000
IL_STAIRWAY                                 = 0b01001000
IL_FRONT_DOOR                               = 0b01010000
IL_STORE_ROOM                               = 0b01011000
IL_GARDEN                                   = 0b01100000
IL_GARAGE                                   = 0b01101000
IL_BALCONY                                  = 0b01110000
IL_OTHERS                                   = 0b01111000
IL_INSTALLATION_LOCATION_NOT_SPECIFIED      = 0b00000000
IL_INSTALLATION_LOCATION_INDEFINITE         = 0b11111111
IL_POSITION_INFORMATION                     = 0b00000001

# Echonet Lite Standard Version Information (Property)


# Echonet Lite Fault Status (Property)
FS_FAULT_OCCURED                            = 0x41
FS_NO_FAULT_OCCURED                         = 0x42

# Echonet Lite Fault Description (Property)
# Note: 2-byte,lower byte specified
FD_NO_FAULT                                 = 0x00
FD_RECOVERABLE_FAULT1                       = 0x01
FD_RECOVERABLE_FAULT2                       = 0x02
FD_RECOVERABLE_FAULT3                       = 0x03
FD_RECOVERABLE_FAULT4                       = 0x04
FD_RECOVERABLE_FAULT5                       = 0x05
FD_RECOVERABLE_FAULT6                       = 0x06
FD_REQUIRE_REPAIR_ABNORMAL_EVENT1           = 0x0A
FD_REQUIRE_REPAIR_ABNORMAL_EVENT2           = 0x0B
FD_REQUIRE_REPAIR_ABNORMAL_EVENT3           = 0x0C
FD_REQUIRE_REPAIR_ABNORMAL_EVENT4           = 0x0D
FD_REQUIRE_REPAIR_ABNORMAL_EVENT5           = 0x0E
FD_REQUIRE_REPAIR_ABNORMAL_EVENT6           = 0x0F
FD_REQUIRE_REPAIR_ABNORMAL_EVENT7           = 0x10
FD_REQUIRE_REPAIR_ABNORMAL_EVENT8           = 0x11
FD_REQUIRE_REPAIR_ABNORMAL_EVENT9           = 0x12
FD_REQUIRE_REPAIR_ABNORMAL_EVENT10          = 0x13
FD_REQUIRE_REPAIR_SWITCH_FAULT1             = 0x14
FD_REQUIRE_REPAIR_SWITCH_FAULT2             = 0x15
FD_REQUIRE_REPAIR_SWITCH_FAULT3             = 0x16
FD_REQUIRE_REPAIR_SWITCH_FAULT4             = 0x17
FD_REQUIRE_REPAIR_SWITCH_FAULT5             = 0x18
FD_REQUIRE_REPAIR_SWITCH_FAULT6             = 0x19
FD_REQUIRE_REPAIR_SWITCH_FAULT7             = 0x1A
FD_REQUIRE_REPAIR_SWITCH_FAULT8             = 0x1B
FD_REQUIRE_REPAIR_SWITCH_FAULT9             = 0x1C
FD_REQUIRE_REPAIR_SWITCH_FAULT10            = 0x1D
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT1      = 0x1E
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT2      = 0x1F
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT3      = 0x20
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT4      = 0x21
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT5      = 0x22
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT6      = 0x23
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT7      = 0x24
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT8      = 0x25
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT9      = 0x26
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT10     = 0x27
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT11     = 0x28
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT12     = 0x29
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT13     = 0x2A
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT14     = 0x2B
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT15     = 0x2C
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT16     = 0x2D
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT17     = 0x2E
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT18     = 0x2F
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT19     = 0x30
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT20     = 0x31
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT21     = 0x32
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT22     = 0x33
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT23     = 0x34
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT24     = 0x35
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT25     = 0x36
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT26     = 0x37
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT27     = 0x38
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT28     = 0x39
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT29     = 0x3A
FD_REQUIRE_REPAIR_SENSOR_SYSTEM_FAULT30     = 0x3B
FD_REQUIRE_REPAIR_COMPONENT_FAULT1          = 0x3C
FD_REQUIRE_REPAIR_COMPONENT_FAULT2          = 0x3D
FD_REQUIRE_REPAIR_COMPONENT_FAULT3          = 0x3E
FD_REQUIRE_REPAIR_COMPONENT_FAULT4          = 0x3F
FD_REQUIRE_REPAIR_COMPONENT_FAULT5          = 0x40
FD_REQUIRE_REPAIR_COMPONENT_FAULT6          = 0x41
FD_REQUIRE_REPAIR_COMPONENT_FAULT7          = 0x42
FD_REQUIRE_REPAIR_COMPONENT_FAULT8          = 0x43
FD_REQUIRE_REPAIR_COMPONENT_FAULT9          = 0x44
FD_REQUIRE_REPAIR_COMPONENT_FAULT10         = 0x45
FD_REQUIRE_REPAIR_COMPONENT_FAULT11         = 0x46
FD_REQUIRE_REPAIR_COMPONENT_FAULT12         = 0x47
FD_REQUIRE_REPAIR_COMPONENT_FAULT13         = 0x48
FD_REQUIRE_REPAIR_COMPONENT_FAULT14         = 0x49
FD_REQUIRE_REPAIR_COMPONENT_FAULT15         = 0x4A
FD_REQUIRE_REPAIR_COMPONENT_FAULT16         = 0x4B
FD_REQUIRE_REPAIR_COMPONENT_FAULT17         = 0x4C
FD_REQUIRE_REPAIR_COMPONENT_FAULT18         = 0x4D
FD_REQUIRE_REPAIR_COMPONENT_FAULT19         = 0x4E
FD_REQUIRE_REPAIR_COMPONENT_FAULT20         = 0x4F
FD_REQUIRE_REPAIR_COMPONENT_FAULT21         = 0x50
FD_REQUIRE_REPAIR_COMPONENT_FAULT22         = 0x51
FD_REQUIRE_REPAIR_COMPONENT_FAULT23         = 0x52
FD_REQUIRE_REPAIR_COMPONENT_FAULT24         = 0x53
FD_REQUIRE_REPAIR_COMPONENT_FAULT25         = 0x54
FD_REQUIRE_REPAIR_COMPONENT_FAULT26         = 0x55
FD_REQUIRE_REPAIR_COMPONENT_FAULT27         = 0x56
FD_REQUIRE_REPAIR_COMPONENT_FAULT28         = 0x57
FD_REQUIRE_REPAIR_COMPONENT_FAULT29         = 0x58
FD_REQUIRE_REPAIR_COMPONENT_FAULT30         = 0x59
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT1      = 0x5A
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT2      = 0x5B
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT3      = 0x5C
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT4      = 0x5D
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT5      = 0x5E
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT6      = 0x5F
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT7      = 0x60
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT8      = 0x61
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT9      = 0x62
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT10     = 0x63
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT11     = 0x64
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT12     = 0x65
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT13     = 0x66
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT14     = 0x67
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT15     = 0x68
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT16     = 0x69
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT17     = 0x6A
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT18     = 0x6B
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT19     = 0x6C
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT20     = 0x6D
FD_REQUIRE_REPAIR_CIRCUIT_BOARD_FAULT21     = 0x6E
FD_FAULT_OCCURED_NOT_ABLE_TO_DETERMINE      = 0x03FF

# Echonet Lite Manufacturer Code (Property)


# Echonet Lite Business Facility Code (Property)


# Echonet Lite Product Code (Property)


# Echonet Lite Production Number (Property)


# Echonet Lite Production Date (Property)


# Echonet Lite Property Map (Property)


# Echonet Lite Identification Number (Property)


# Echonet Lite Manufacturer Fault Code (Property)


# Echonet Lite Current Limit Setting (Property)


# Echonet Lite Power Saving Operation Setting (Property)
PSOS_POWER_SAVING_ON                        = 0x41
PSOS_POWER_SAVING_OFF                       = 0x42

# Echonet Lite Remote Control Setting (Property)
RCS_NOT_THROUGH_PUBLIC_NETWORK              = 0x41
RCS_THROUGH_PUBLIC_NETWORK                  = 0x42

# Echonet Lite Cumulative Operating Time (Property)
COT_SECONDS                                 = 0x41
COT_MINUTES                                 = 0x42
COT_HOURS                                   = 0x43
COT_DAYS                                    = 0x44

# Echonet Lite Current Time Setting (Property)


# Echonet Lite Current Date Setting (Property)


# Echonet Lite Measured Instantaneous Power Consumption (Property)
MIPC_UNDERFLOW                              = 0xFFFE
MIPC_OVERFLOW                               = 0xFFFF

# Echonet Lite Measured Cumulative Power Consumption (Property)


# Echonet Lite Power Limit Setting (Property)

"""
    Echonet Lite Functions
    Note: 1. functions are similar to the C version Echonet Lite library, removed some of the simpler functions such as echonet_setEHD1(), etc. and changed the return failed response to -1 for get() functions
          2. functions that deals directly with echonet_packet (global variable) must be executed in sequence (e.g.: setPacket -> setnEPC -> setnPDC -> setnEDT)
          3. since functions sequentially deals with echonet_packet (global variable), functions are not thread safe (behavior is not guaranteed)
"""
class EchonetLite:
    def __init__(self)
        MAX_ECHONET_PACKET_LEN = 64
        self.echonet_packet = [0] * MAX_ECHONET_PACKET_LEN # pre-allocate echonet lite packet structure
# Set Echonet Lite Property
# Note: 1. 1 byte (X1-class group code,X2-class code)
#       2. Refer to Table 3.12 EPC Code Allocation Table
#       3. Value n>0,n<=OPC value (Request 1,2,3,...,n)
#       4. echonet_setnEPC(OPC limited n,EPC_xx)
def setnEPC(n, epc_code):
    global echonet_packet
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0: # check n with OPC
        if n == 1:
            echonet_packet[12] = epc_code
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            echonet_packet[12+k+(i*2)] = epc_code
    else:
        logging.error("setnEPC() invalid n.")

# Get Echonet Lite Property
# Note: 1. Error,return -1
def getnEPC(n):
    global echonet_packet
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0: # check n with OPC
        if n == 1:
            return echonet_packet[12]
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            return echonet_packet[12+k+(i*2)]
    else:
        logging.error("setnEPC() invalid n.")
        return -1

# Set Echonet Lite Property Data Counter
# Note: 1. Value n>0,n<=OPC value (Request 1,2,3,...,n)
#       2. echonet_setnPDC(OPC limited n,value)
def setnPDC(n, value):
    global echonet_packet
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0: # check n with OPC
        if n == 1:
            echonet_packet[13] = value
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            echonet_packet[13+k+(i*2)] = value
    else:
        logging.error("setnPDC() invalid n.")

# Get Echonet Lite Property Data Counter
# Note: 1. Error,return -1
def getnPDC(n):
    global echonet_packet
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0: # check n with OPC
        if n == 1:
            return echonet_packet[13]
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            return echonet_packet[13+k+(i*2)]
    else:
        logging.error("getnPDC() invalid n.")
        return -1

# Set Echonet Lite Property Value
# Note: 1. property_data_list must be a list
def setnEDT(n, property_data_list):
    global echonet_packet
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0 and len(property_data_list) == getnPDC(n): # check n with OPC & input list is equal to nPDC
        if n == 1:
            for i in range(getnPDC(n)):
                echonet_packet[14+i] = property_data_list[i]
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            for j in range(getnPDC(n)):
                echonet_packet[14+j+k+(i*2)] = property_data_list[j]
    else:
        logging.error("setnEDT() invalid n and/or length of input list is not equal to nPDC.")

# Get Echonet Lite Property Value
# Note: 1. Error,return -1
#       2. returns EDT list
def getnEDT(n):
    global echonet_packet
    EDT_list = []
    j, k = 0, 0
    if n <= echonet_packet[11] and n > 0: # check n with OPC
        if n == 1:
            for i in range(getnPDC(n)):
                EDT_list.append(echonet_packet[14+i])
        else:
            for i in range(1, n):
                k += echonet_packet[12+i+j+k]
                j += 1
            for j in range(getnPDC(n)):
                EDT_list.append(echonet_packet[14+j+k+(i*2)])
        return EDT_list
    else:
        logging.error("setnEDT() invalid n")
        return -1

# Set Echonet Lite Packet (without Echonet Lite Property Setting and Data: EPC,PDC,EDT)
# Note: 1. tid16 can accept both single 16 bit integer and two 8 bit integer list
def setPacket(ehd1, ehd2, tid16, seoj_cgc, seoj_cc, seoj_ic, deoj_cgc, deoj_cc, deoj_ic, esv, opc):
    global echonet_packet
    if type(tid16) is not list:
        tid16 = [tid16 >> 8, tid16 & 0x00ff]
    echonet_packet[:12] = [ehd1, ehd2, tid16[0], tid16[1], seoj_cgc, seoj_cc, seoj_ic, deoj_cgc, deoj_cc, deoj_ic, esv, opc]

def



"""
    Echonet Lite Function Test Units
    Note: 1. covers all functions that deals directly with echonet_packet (global variable)
"""
class testEchonetLite(unittest.TestCase):
    global echonet_packet

    def setUp(self): # populate global var with sample header, OPC = 3
        echonet_packet[:] = [0 for _ in echonet_packet[:]] # reset global var
        self.sample = [0x10, 0x81, 0x00, 0x01, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3]
        echonet_packet[:len(self.sample)] = self.sample[:]

    def test_setnEPC(self):
        setnEPC(1, 0x01) # n = 1, EPC = 0x01
        self.sample.append(0x01) # n = 1, EPC = 0x01
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0xFF] # n = 1, PDC = 0x01, EDT = 0xFF
        setnEPC(2, 0x01) # n = 2, EPC = 0x01
        self.sample.extend([0x01, 0xFF, 0x01]) # n = 2, EPC = 0x01
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+4] = [0x03, 0xFF, 0xFF, 0xFF] # n = 2, PDC = 0x03, EDT = 0xFF * 3
        setnEPC(3, 0x01) # n = 3, EPC = 0x01
        self.sample.extend([0x03, 0xFF, 0xFF, 0xFF, 0x01]) # n = 3, EPC = 0x01
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)

    def test_getnEPC(self):
        echonet_packet[12] = 0x01 # n = 1, EPC = 0x01
        self.sample.append(0x01) # n = 1, EPC = 0x01
        self.assertEqual(getnEPC(1), self.sample[len(self.sample)-1])
        echonet_packet[len(self.sample):len(self.sample)+2]  = [0xFF, 0x01] # EDT = 0xFF, n = 2, EPC = 0x01
        self.sample.extend([0xFF, 0x01]) # EDT = 0xFF, n = 2, EPC = 0x01
        self.assertEqual(getnEPC(1), self.sample[len(self.sample)-1])
    
    def test_setnPDC(self):
        echonet_packet[12] = 0x01 # n = 1, EPC = 0x01
        setnPDC(1, 0x01) # n = 1, value = 1
        self.sample.extend([0x01, 0x01]) # n = 1, EPC = 0x01, PDC = 0x01
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+2]  = [0xFF, 0x01] # EDT = 0xFF, n = 2, EPC = 0x01
        setnPDC(2, 0x03)
        self.sample.extend([0xFF, 0x01, 0x03]) # n = 1, EPC = 0x01, PDC = 0x03
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+4]  = [0xFF, 0xFF, 0xFF, 0x01] # EDT = 0xFF * 3, n = 3, EPC = 0x01
        setnPDC(3, 0x02)
        self.sample.extend([0xFF, 0xFF, 0xFF, 0x01, 0x02]) # n = 2, EPC = 0x01, PDC = 0x02
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)

    def test_getnPDC(self):
        echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x01]  # n = 1, EPC = 0x01, PDC = 0x01
        self.sample.extend([0x01, 0x01]) # n = 1, EPC = 0x01, PDC = 0x01
        self.assertEqual(getnPDC(1), self.sample[len(self.sample)-1])
        echonet_packet[len(self.sample):len(self.sample)+2] = [0xFF, 0x01, 0x03]  # EDT = 0xFF, n = 2, EPC = 0x01, PDC = 0x03
        self.sample.extend([0xFF, 0x01, 0x03]) # EDT 0xFF, n = 2, EPC = 0x01, PDC = 0x03
        self.assertEqual(getnPDC(2), self.sample[len(self.sample)-1])
        echonet_packet[len(self.sample):len(self.sample)+5] = [0xFF, 0xFF, 0xFF, 0x01, 0x02] # EDT = 0xFF * 3, n = 3, EPC = 0x01, PDC = 0x02
        self.sample.extend([0xFF, 0xFF, 0xFF, 0x01, 0x02]) # EDT 0xFF * 3, n = 3, EPC = 0x01, PDC = 0x02
        self.assertEqual(getnPDC(3), self.sample[len(self.sample)-1])
    
    def test_setnEDT(self):
        echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x01] # n = 1, EPC = 0x01, PDC = 0x01
        setnEDT(1, [0xFF]) # input EDT must be a list
        self.sample.extend([0x01, 0x01, 0xFF]) # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x03] # n = 2, EPC = 0x01, PDC = 0x03
        setnEDT(2, [0xFF, 0xFF, 0xFF])
        self.sample.extend([0x01, 0x03, 0xFF, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        echonet_packet[len(self.sample):len(self.sample)+2] = [0x01, 0x02] # n = 1, EPC = 0x01, PDC = 0x02
        setnEDT(3, [0xFF, 0xFF])
        self.sample.extend([0x01, 0x02, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x02, EDT = 0xFF * 2
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)

    def test_getnEDT(self):
        echonet_packet[len(self.sample):len(self.sample)+3] = [0x01, 0x01, 0xFF] # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.sample.extend([0x01, 0x01, 0xFF]) # n = 1, EPC = 0x01, PDC = 0x01, EDT = 0xFF
        self.assertEqual(getnEDT(1), [self.sample[len(self.sample)-1]])
        echonet_packet[len(self.sample):len(self.sample)+5] = [0x01, 0x03, 0xFF, 0xFF, 0xFF] # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.sample.extend([0x01, 0x03, 0xFF, 0xFF, 0xFF]) # n = 2, EPC = 0x01, PDC = 0x03, EDT = 0xFF * 3
        self.assertEqual(getnEDT(2), self.sample[len(self.sample)-3:len(self.sample)])
    
    def test_setPacket(self):
        setPacket(0x10, 0x81, [0x00, 0x01], 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test list tid16, tid16 = [0x00, 0x01]
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        setPacket(0x10, 0x81, 0x01, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0x01
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        setPacket(0x10, 0x81, 0x01FF, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0x01FF
        self.sample[2:4] = [0x01, 0xFF] # tid16 = 0x01FF
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)
        setPacket(0x10, 0x81, 0xF103, 0x0E, 0xF0, 0x01, 0x00, 0x11, 0x01, 0x62, 3) # test int tid16, tid16 = 0xF103
        self.sample[2:4] = [0xF1, 0x03] # tid16 = 0xF103
        self.assertEqual(echonet_packet[:len(self.sample)], self.sample)






















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
