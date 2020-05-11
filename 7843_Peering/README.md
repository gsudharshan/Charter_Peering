
# Template for generating Peering configs for AS20115 for both IOS-XR and Junos by updating the generate_peering_config.yml

!!!!!!! usage $ansible-playbook -i router_list.yml generate_peering_config.yml !!!!!!!!!!!!!!!!

router_list.yml contains all the AS20115 router names you are generating the config file for. The file you are creating will be placed in the peering_config/ folder.

Junos routers go under the Junos section on router_list.yml\IOS-XR routers go under the IOS-XR section. This will determine the correct Jinja Template to be used.
