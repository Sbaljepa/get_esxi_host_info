from con_esxi_host import *
from math import pow, ceil
class hardware:
    def get_host_hwinfo(self):
        si = connect_to_host()
        #content = si.RetrieveContent()
        hw = si.content.rootFolder.childEntity[0].hostFolder.childEntity[0].host[0]
        hw1 = si.content.rootFolder.childEntity[0].hostFolder.childEntity[0].datastore[0]
        #hw2 =hw.configManager.storageSystem.storageDeviceInfo.scsiLun[0]
        hw3 = hw.configManager.graphicsManager.graphicsInfo[0]
        #hw4 = hw.configManager.networkSystem.networkInfo.netStackInstance[0]
        lc = hw.configManager.licenseManager.licenses[0]
        hw_info = {}
        #config_hw = {}
        lcs ={}
        cpu = {}
        ram ={}
        strg = {}
        gpu = {}
        #vir ={}
        # More details can be accessed from vm.summary, but these are the most relevant
        #fullname = content.about.fullName
        #build = content.about.build
        #apiVersion = content.about.apiVersion
        #license = content.about.licenseProductVersion
        vendor = hw.summary.hardware.vendor
        model = hw.summary.hardware.model
        uuid = hw.summary.hardware.uuid
        cpuModel = hw.summary.hardware.cpuModel
        cpuMhz = hw.summary.hardware.cpuMhz
        #numCpuPkgs = hw.summary.hardware.numCpuPkgs
        numCpuCores = hw.summary.hardware.numCpuCores
        numCpuThreads = hw.summary.hardware.numCpuThreads
        memorySize = ceil(hw.summary.hardware.memorySize / pow(1024, 3))
        biosInfo = hw.hardware.biosInfo.biosVersion
        capacity = ceil(hw1.summary.capacity / pow(1024, 3))
        storage = hw1.summary.name
        type=  hw1.summary.type
        ssd = hw1.info.vmfs.ssd
        Graphic_device = hw3.deviceName
        GraphicsType = hw3.graphicsType
        vendorName = hw3.vendorName
        license_key =lc.licenseKey
        license_name = lc.name
        try:
            sn = hw.summary.hardware.otherIdentifyingInfo[1].identifierValue
        except:
            sn = "Unknown"
        hw_info['Type'] = "Hardware"
        hw_info['Serial no'] = sn
        hw_info['Bios'] = biosInfo
        hw_info['Vendor'] = vendor
        hw_info['Model'] = model
        hw_info['UUID'] = uuid
        lcs['Type'] = "License"
        lcs['Name'] = license_name
        lcs['Value'] = license_key
        cpu['Type'] = "CPU"
        cpu['Model'] = cpuModel
        cpu['Cores'] = numCpuCores
        cpu['Threads'] = numCpuThreads
        ram['Type'] = "RAM"
        ram['value'] = "Memory"
        ram['Memory'] = memorySize
        strg['Type'] = "storage"
        strg['Name'] = storage
        strg['Size'] = capacity
        strg['SSD'] = ssd
        strg['value'] = type
        #strg['Verzcsion'] = abc
        #strg['vsn'] = hw2
        gpu['Type'] = "GPU"
        gpu['Name'] = vendorName
        gpu['Model'] = Graphic_device
        gpu['Key'] = GraphicsType
        config_hw = lcs,cpu,ram,strg,gpu

        hw_info['configuration'] = config_hw
        return hw_info
    def virt_hw_info(self):
        si = connect_to_host()
        content = si.RetrieveContent()
        hw = si.content.rootFolder.childEntity[0].hostFolder.childEntity[0].host[0]
        nw = {}
        vir ={}
        Host_name = hw.summary.config.name
        numNics = hw.summary.hardware.numNics
        version = content.about.version
        #host = content.about.fullName
        vir['Type'] = "Virtualization"
        vir['Name'] = "VMWare"
        vir['Host_name'] = Host_name
        nw['Name'] = "Network"
        #nw['IP'] = host
        nw['NIC'] = numNics
        vir['version'] = version
        vir['Configuration'] = nw
        return vir