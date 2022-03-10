import os
App_det ={}
App_s ={}
class application:
    def get_sdp_verinfo(self):
        sdp = os.popen( "grep 'sdp_version' ~/inventory.json | cut -d ':'-f 2")
        sdp_d = os.popen("grep 'sdp_deploy_type' ~/inventory.json |cut -d ':'-f 2")
        App_s['Type'] = "SDP"
        App_s['Name'] = sdp_d.read()
        App_s['Version'] = sdp.read()
        return App_s
    def get_app_info(self):
        ###############################################
        #git = os.popen("git --version")
        docker = os.popen("docker --version | awk '{print $3}'")
        kubernetes = os.popen("kubectl version |head -1 | awk '{print $5}' | cut -d ':'-f 2")
        helm = os.popen("helm version | head -1 | awk '{ print $2}' | cut -d ':' -f 2")
        helm_apps= os.popen("helm list | awk '{print $1}'| awk 'NR>1'| while read line; do echo $line; helm history $line --output json | awk '{print $line}'|awk '!($1="")'; done")

        #App_s ={}
        App_d ={}
        App_k={}
        App_h ={}
        App_ha ={}
        # sdp_apps ={}
        #App_details ={}

        App_d['Type'] = "Service"
        App_d['Name'] = "Docker"
        App_d['Version'] = docker.read()
        App_k['Type'] = "Service"
        App_k['Name'] = "Kubernetes"
        App_k['Version'] = kubernetes.read()
        App_h['Type'] = "Service"
        App_h['Name'] = "Helm"
        App_h['Version'] = helm.read()
        App_ha['Type'] = "Service"
        App_ha['Name'] = "Helm Apps"
        App_ha['Details'] = helm_apps.read()
        sdp_apps = App_d,App_k,App_h,App_ha
        App_det["Applications"] = sdp_apps
        return App_det
        #print(App_details)
