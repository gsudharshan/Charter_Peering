
# Template for generating configs for both IOS-XR and Junos by updating the generate_peering_config.yml

!!!!!!! usage $ansible-playbook -i router_list.yml generate_peering_config.yml

For now edit the router_list.yml will contain the hosts you are generating the config file for. That file will be created in the peer_config folder.

Junos routers go under the Junos section on inventory.yml\IOS-XR routers go under the IOS-XR section. This will determine the correct Jinja Template to be used.
