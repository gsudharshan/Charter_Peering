
# Template for generating Peering configs for AS20115 for both IOS-XR and Junos by updating the generate_peering_config.yml

!!!!!!! usage $ansible-playbook -i router_list.yml generate_peering_config.yml !!!!!!!!!!!!!!!!

router_list.yml contains all the AS20115 router names you are generating the config file for. The file you are creating will be placed in the peering_config/ folder.

Junos routers go under the Junos section on router_list.yml\IOS-XR routers go under the IOS-XR section. This will determine the correct Jinja Template to be used.


SAMPLE YAML INPUT

 pr3.dfw10:
    name: akamai
    type: PEER
    jira: CIOPS-18380
    lag_id_1: 1018
    lag_id_1_link_bw: 100
    lag_bw_1: 300
    lag_grnt_1: chn00499491
    lag_local_ipv4_1: "209.85.168.185/31"
    lag_local_ipv6_1: "2001:4860:1:1::16cf/127"
    lag_id_1_links:
                 Hu0/0/0/7: { int_grnt: chn00499492, ccid: 21373149-Z, pcid: 179119 }
                 Hu0/0/0/6: { int_grnt: chn00499492, ccid: 21373149-Z, pcid: 179119 }
                 Hu0/0/0/5: { int_grnt: chn00499492, ccid: 21373149-Z, pcid: 179119 }


    lag_id_2: 1584
    lag_id_2_link_bw: 100
    lag_bw_2: 100
    lag_grnt_2: chn00499493
    lag_local_ipv4_2: "96.34.3.1/31"
    lag_local_ipv6_2: "2001:2234:0:2::2/127"
    lag_id_2_links:
                 Hu0/1/2/0: { int_grnt: chn00499492, ccid: 21373150-Z, pcid: 179545 }

    bgp:
       group_md5:
       ipv4_md5: jutran7dEbUwr6c9
       ipv6_md5: jutran7dEbUwr6c9
       ipv4_prefix_limit: 15000
       ipv4_prefix_limit_teardown: 90
       ipv6_prefix_limit: 10000
       ipv6_prefix_limit_teardown: 90
       timers_keep: 60
       timers_hold: 180
       timers_min_hold: 45 
       peer_ipv4_1: 209.85.168.184
       peer_ipv6_1: "2001:4860:2:1::16ce"
       peer_ipv4_2: 96.34.3.2
       peer_ipv6_2: "2001:2234:0:2::3"

       peer_ipv4_multihop_1: 1.1.1.1        
       peer_ipv6_multihop_1: "2001::1"
       peer_multihop_1_ttl: 4
       peer_ipv4_multihop_2: 2.2.2.2
       peer_ipv6_multihop_2: "2002::2"       
       peer_multihop_2_ttl: 4
       local_as: 20115
       remote_as: 20940    
