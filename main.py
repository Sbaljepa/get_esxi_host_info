import json
#from credent import *
from hardware import hardware
from vmware import vmware
from application import application
full_json = []
def main():
    hw =hardware()
    vm =vmware()
    apps = application()
    a=hw.get_host_hwinfo()
    b=hw.virt_hw_info()
    c=vm.get_vm_info()
    d=apps.get_app_info()
    e=apps.get_sdp_verinfo()
    sdp_arr = []
    ap =[]
    test = c,d
    comp_section = [a, b]
    comp_section.extend(test)
    sdp_arr.append({'Components': comp_section})
    App_data = e,sdp_arr
    full_json.append({'structure': App_data})
    return full_json
    #To get information on user inputs
    # A = input('Press Enter to get complete machine info, "h" for Hardware, "v" for VM and "a" for Application: ')
    # if A =="h":
    #     comp_section = [a, b]
    #     sdp_arr.append({'Components': comp_section})
    #     full_json.append({'structure': sdp_arr})
    # elif A == "v":
    #     #comp_section.extend
    #     sdp_arr.append({'Components': c})
    #     full_json.append({'structure': sdp_arr})
    # elif A == "a":
    #     ap.append({'Components': d})
    #     sdp_arr = e,ap
    #     full_json.append({'structure': sdp_arr})
    # else:
    #     test = c, d
    #     comp_section = [a, b]
    #     comp_section.extend(test)
    #     sdp_arr.append({'Components': comp_section})
    #     App_data = e,sdp_arr
    #     full_json.append({'structure': App_data})
    # return full_json
if __name__ == '__main__':
    full_json = main()
    with open('SDP_sys_info.json', 'w', encoding='utf-8') as f:
        json.dump(full_json, f, indent=6)


