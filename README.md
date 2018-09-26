# mining-ansible
Ansible playbooks for eth mining autoconfiguration
## Features
* Overclocking of AMD Radeon Cards without bios modifications.
* Monitoring of temp, fan, hashrate. 
## Approach
* ohgodatool is used for amd overclocking.
* Zabbix based monitoring.
* Systemd services used for scheduling and autostart.
## Prerequirments
* Python3, aptitude for rigs.
* Claymore installation is not included, it should be installed or preinstalled to /opt/mine/clay.
* Install Claymore for zcash to /opt/mine/zclay (optional)
* Install XMR to /opt/mine/xmr-stak(optional)
* For amd GPU install [AMDGPU-PRO Beta Mining Driver 17.40](https://support.amd.com/en-us/kb-articles/Pages/AMDGPU-Pro-Beta-Mining-Driver-for-Linux-Release-Notes.aspx)
### Host groups
* miners - meta group for all mining devices.
* amd, nv - Monitoring scripts installation is based on this groups. Add mining device directly or through children groups. Rigs should not be in both groups simultaneously. 
* rx470 - Children group for Sapphire RX470 GPU based rigs.
### Roles
* common - does not have any tasks. Planned for general tasks required for all rigs.
* mine-update - updates configuration files of zabbix and miners.
* monitor-nv, monitor-amd - install scripts for gpu monitoring.
* reboot-soft - gently restarts.
* tune-rx470 - installs ohgodatool and configures it.
* test - used for test. Some tasks that were used for experiments

## Troubleshooting
This repo is a copy of ansible playbooks which were succesfully used. But I had to remove some private data, files, configs and it might have become broken. Playbooks may contain errors and do not work. This repo have not been tested. 
