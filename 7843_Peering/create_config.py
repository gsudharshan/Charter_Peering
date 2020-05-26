import os
import sys

cmd1 = 'ansible-playbook -i router_list.yml generate_peering_config.yml'
os.system(cmd1)
