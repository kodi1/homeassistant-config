#! /usr/bin/bash

ssh_opt="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o LogLevel=ERROR"
cat <<EOF | ssh ${ssh_opt} root@192.168.1.1 "cat > /usr/share/rpcd/acl.d/root.json && /etc/init.d/rpcd restart && /etc/init.d/uhttpd restart"
{
  "root": {
    "description": "Access role for OpenWrt ubus integration",
    "read": {
      "ubus": {
        "hostapd.*": ["get_clients"],
        "uci": ["get"]
      },
    },
    "write": {}
  }
}
EOF
