import os
import sys

filename1 = sys.argv[1]

cmd1 = 'python pp.py ' + filename1
cmd2 = 'ansible-playbook -i router_list.yml generate_peering_config.yml'
cmd3 = 'rm generate_peering_config.retry'
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
