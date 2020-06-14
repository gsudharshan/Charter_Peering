import os
import sys

cmd1 = 'ansible-playbook -i router_list.yml generate_peering_config.yml'
cmd2 = 'rm generate_peering_config.retry'
os.system(cmd1)
os.system(cmd2)