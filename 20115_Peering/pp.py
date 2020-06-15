import pandas as pd
import numpy as np
import os,sys

filename1 = sys.argv[1]

df = pd.read_excel(filename1, sheet_name = 0)
df = df.replace(np.nan, '', regex=True)

#Print output to a file named "ciops_input_template.yml"
f = open('ciops_input_template.yml','w')
sys.stdout = f

print("---")
print("\n")
print("nodes: ")
print("\n")
# Generate YAML for Public Peering
def create_single_yaml(i):
    print("  " + df.iloc[i, 0] + ":")
    print("    name: " + df.iloc[i, 1])
    print("    type: " + df.iloc[i, 2])
    print("    jira: " + df.iloc[i, 3])
    print("    lag_local_ipv4_1: " + df.iloc[i, 4])
    print("    lag_local_ipv6_1: " + df.iloc[i, 5])
    print("    bgp: ")
    if df.iloc[i, 6]:
        print("        group_md5: " + str(df.iloc[i, 6]))
    if df.iloc[i, 7]:
        print("        ipv4_md5: " + str(df.iloc[i, 7]))
    if df.iloc[i, 8]:
        print("        ipv6_md5: " + str(df.iloc[i, 8]))
    print("        ipv4_prefix_limit: " + str(int(df.iloc[i, 9])))
    print("        ipv6_prefix_limit: " + str(int(df.iloc[i, 10])))
    print("        peer_ipv4_1: " + (df.iloc[i, 11]))
    print("        peer_ipv6_1: " + (df.iloc[i, 12]))
    print("        local_as: " + str(int(df.iloc[i, 13])))
    print("        remote_as: " + str(int(df.iloc[i, 14])))
for i in range(len(df.index)):
    j = i + 1
    if j >= len(df.index):
        if i == len(df.index):
            create_single_yaml(i)
        continue
    router_check = df.iloc[i, 0] == df.iloc[j, 0]
    router_check1 = df.iloc[i, 0] == df.iloc[i-1, 0]
    if router_check is False:
        if router_check1 is False or (router_check1 is True and i == 0):
            create_single_yaml(i)
        continue
    print("  " + df.iloc[i, 0] + ":")
    print("    name: " + df.iloc[i, 1])
    print("    type: " + df.iloc[i, 2])
    print("    jira: " + df.iloc[i, 3])
    print("    lag_local_ipv4_1: " + df.iloc[i, 4])
    print("    lag_local_ipv6_1: " + df.iloc[i, 5])
    print("    bgp: ")
    if df.iloc[i, 6] and router_check:
        print("        group_md5: " + (df.iloc[i, 6]))
    if df.iloc[i, 7] and router_check:
        print("        ipv4_md5: " + (df.iloc[i, 7]))
    if df.iloc[i, 8] and router_check:
        print("        ipv6_md5: " + (df.iloc[i, 8]))
    print("        ipv4_prefix_limit: " + str(int(df.iloc[i, 9])))
    print("        ipv6_prefix_limit: " + str(int(df.iloc[i, 10])))
    print("        peer_ipv4_1: " + (df.iloc[i, 11]))
    if df.iloc[j, 11] and router_check:
        print("        peer_ipv4_2: " + (df.iloc[j, 11]))
    print("        peer_ipv6_1: " + (df.iloc[i, 12]))
    if df.iloc[j, 12] and router_check:
        print("        peer_ipv6_2: " + (df.iloc[j, 12]))
    print("        local_as: " + str(int(df.iloc[i, 13])))
    print("        remote_as: " + str(int(df.iloc[i, 14])))

