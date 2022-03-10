from con_esxi_host import *
from math import pow, ceil
class vmware:
    def get_vm_info(self):
        si = connect_to_host()
        #global virtual
        inv = si.RetrieveContent()
        dc1 = inv.rootFolder.childEntity[0]
        vmList = dc1.vmFolder.childEntity
        virtual = []
        for vm in vmList:
            name = vm.summary.config.name
            guestFullName = vm.summary.config.guestFullName
            # powerState = vm.summary.runtime.powerState
            bootTime = str(vm.summary.runtime.bootTime)
            # overallCPUUsage = vm.summary.quickStats.overallCpuUsage
            # maxCpuUsage = vm.summary.runtime.maxCpuUsage / 1024
            cpuUtilization = vm.summary.quickStats.overallCpuUsage * 100 / vm.summary.runtime.maxCpuUsage;
            # paused = vm.summary.runtime.paused
            # snapshotInBackground = vm.summary.runtime.snapshotInBackground
            # toolsStatus = vm.summary.guest.toolsStatus
            hostName = vm.summary.guest.hostName
            ipAddress = vm.summary.guest.ipAddress
            # vmPathName = vm.summary.config.vmPathName
            memorySizeMB = ceil(vm.summary.config.memorySizeMB / 1024);
            numEthernetCards = vm.summary.config.numEthernetCards
            numVirtualDisks = vm.summary.config.numVirtualDisks
            # guestId = vm.summary.config.guestId
            annotation = vm.summary.config.annotation
            unshared = ceil(vm.summary.storage.unshared / pow(1024, 3))
            uncommitted = ceil(vm.summary.storage.uncommitted / pow(1024, 3))
            committed = uncommitted + unshared
            numCpu = vm.summary.config.numCpu

            vm_info = {}
            #config_vm = {}
            vm_kernal = {}
            vm_strg = {}
            vm_mem = {}
            vm_cpu = {}
            vm_nw = {}

            vm_info['Type'] = "Virtual Machine"
            vm_info['Name'] = name
           # vm_info['host'] = host
            vm_info['HostName'] = hostName
            vm_kernal['Type'] = "Kernal"
            vm_kernal['OS'] = guestFullName
            vm_kernal['Boot Time'] = bootTime
            vm_nw['Type'] = "Network"
            vm_nw['IP'] = ipAddress
            vm_nw['EthernetCards'] = numEthernetCards
            vm_strg['Type'] = "Storage"
            vm_strg['Storage'] = committed
            vm_strg['Disks'] = numVirtualDisks
            vm_mem['Type'] = "RAM"
            vm_mem['Name'] = "Memory"
            vm_mem['Memory'] = memorySizeMB
            vm_cpu['Type'] = "CPU"
            vm_cpu['Name'] = "Cores"
            vm_cpu['Capacity'] = numCpu
            #vm_cpu['git'] = git.read()
            config_vm = vm_kernal, vm_cpu,vm_mem,vm_strg, vm_nw
            vm_info['configuration'] = config_vm
            virtual.append(vm_info)
        #print(virtual)
        return virtual