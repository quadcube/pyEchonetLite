#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Static Echonet Lite definitions
 | EHD1 1byte | EHD2 1byte | TID 2byte | EOJ_CGC&CC 2byte | IC 1byte | ESV 1byte | DATA |
"""
# Echonet Lite Header 1 (EHD1)
EHD1_ECHONET = 0x10

# Echonet Lite Header 2 (EHD2)
EHD2_FORMAT1 = 0x81
EHD2_FORMAT2 = 0x82

def code_to_desc(code_dict):
    desc_dict = {}
    for key in code_dict:
        desc_dict[code_dict[key]] = key
    return desc_dict

ESV_CODE = {
    'ESV_SetI_SNA':   0x50,
    'ESV_SetC_SNA':   0x51,
    'ESV_Get_SNA':    0x52,
    'ESV_INF_SNA':    0x53,
    'ESV_SetGet_SNA': 0x5e,
    'ESV_SetI':       0x60,
    'ESV_SetC':       0x61,
    'ESV_Get':        0x62,
    'ESV_INF_REQ':    0x63,
    'ESV_SetGet':     0x6e,
    'ESV_Set_Res':    0x71,
    'ESV_Get_Res':    0x72,
    'ESV_INF':        0x73,
    'ESV_INFC':       0x74,
    'ESV_INFC_Res':   0x7a,
    'ESV_SetGet_Res': 0x7e,
}
ESV_DESC = code_to_desc(ESV_CODE)
ESV_REQUEST_CODES = (
    ESV_CODE['ESV_SetI'],
    ESV_CODE['ESV_SetC'],
    ESV_CODE['ESV_Get'],
    ESV_CODE['ESV_INF_REQ'],
    ESV_CODE['ESV_SetGet'],
    ESV_CODE['ESV_INF'],
)
ESV_RESPONSE_CODES = (
    ESV_CODE['ESV_Set_Res'],
    ESV_CODE['ESV_Get_Res'],
    ESV_CODE['ESV_INF'],
    ESV_CODE['ESV_INFC_Res'],
    ESV_CODE['ESV_SetGet_Res'],
)
ESV_ERROR_CODES = (
    ESV_CODE['ESV_SetI_SNA'],
    ESV_CODE['ESV_SetC_SNA'],
    ESV_CODE['ESV_Get_SNA'],
    ESV_CODE['ESV_INF_SNA'],
    ESV_CODE['ESV_SetGet_SNA'],
)
CLSGRP_CODE = {
