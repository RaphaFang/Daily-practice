# ------------------------------------------------------------------------------------------------------------------------------
# chacnge back to original
# ------------------------------------------------------------------------------------------------------------------------------
import subprocess

def set_static_ip(interface, ip_address, subnet_mask, router):
    try:
        # Configure the interface with the provided static IP address, subnet mask, and router
        subprocess.check_output(f"sudo networksetup -setmanual {interface} {ip_address} {subnet_mask} {router}", shell=True)
        print("Static IP address configured successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring static IP address: {e}")

# Example usage
interface = "Wi-Fi"  # Replace with your interface name, e.g., "Wi-Fi" or "Ethernet"
ip_address = "192.168.1.100"  # Replace with your desired IP address
subnet_mask = "255.255.255.0"  # Replace with your subnet mask
router = "192.168.1.1"  # Replace with your router IP address

set_static_ip(interface, ip_address, subnet_mask, router)


# ------------------------------------------------------------------------------------------------------------------------------
# chacnge back to original
# ------------------------------------------------------------------------------------------------------------------------------
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