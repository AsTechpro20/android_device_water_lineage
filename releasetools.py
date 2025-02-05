#
# Copyright (C) 2022 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import common
import re

def FullOTA_Assertions(info, metadata):
    pre_timestamp = GetBuildProp("ro.build.date.utc", OPTIONS.source_info_dict)
    info.script.Print("========================================")
    info.script.Print("Testing build")
    info.script.Print("Dont use for daily")
    info.script.Print("Build Date: " + pre_timestamp)
    info.script.Print("========================================")
    return

def FullOTA_InstallBegin():
    return

def FullOTA_InstallEnd():
    OTA_InstallEnd()
    return

def IncrementalOTA_Assertions():
    return

def IncrementalOTA_VerifyBegin():
    return

def IncrementalOTA_VerifyEnd():
    return

def IncrementalOTA_InstallBegin():
    return

def IncrementalOTA_InstallEnd():
    OTA_InstallEnd()
    return

def AddImage(info, basename, dest):
    name = basename
    data = info.input_zip.read("IMAGES/" + basename)
    common.ZipWriteStr(info.output_zip, name, data)
    info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info):
    info.script.Print("Installing dtbo image...")
    AddImage(info, "dtbo.img", "/dev/block/platform/bootdevice/by-name/dtbo")

    info.script.Print("Patching vbmeta image...")
    AddImage(info, "vbmeta.img", "/dev/block/platform/bootdevice/by-name/vbmeta")

    info.script.Print("Patching vbmeta system image...")
    AddImage(info, "vbmeta_system.img", "/dev/block/platform/bootdevice/by-name/vbmeta_system")

    info.script.Print("Patching vbmeta vendor image...")
    AddImage(info, "vbmeta_vendor.img", "/dev/block/platform/bootdevice/by-name/vbmeta_vendor")
    return