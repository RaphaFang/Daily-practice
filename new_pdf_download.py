# pip install zenrows
# from zenrows import ZenRowsClient

# client = ZenRowsClient("89046282b1402b11fe09b238bcb8a580acebe6bf")
# url = "https://www.zeczec.com/users/sign_in"
# params = {"premium_proxy":"true","proxy_country":"tw","antibot":"true", "premium_proxy":"true",  "js_render":"true","autoparse":"true"}

# response = client.get(url, params=params)

# print(response.text)

import subprocess

def reset_network_settings(interface):
    try:
        # Configure the interface to use DHCP to obtain IP address automatically
        subprocess.check_output(f"sudo networksetup -setdhcp {interface}", shell=True)
        print("Network settings reset successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error resetting network settings: {e}")

# Example usage
interface = "Wi-Fi"  # Replace with your interface name, e.g., "Wi-Fi" or "Ethernet"

reset_network_settings(interface)