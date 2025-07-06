import ipaddress
from typing import List

class Calculator():
    def max_subnets(self, ip: str, mask: int) -> List:
        """
        Return [total_addresses, usable_addresses, network_address, broadcast_address]
        for the given IPv4 and subnet mask.
        """
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        # for /31 and /32, “usable” hosts differ—here we treat only /30 or larger
        host_bits = 32 - mask
        max_subnets = 2 ** host_bits
        if max_subnets >=30:
            max_addresses = max_subnets - 2  # Subtracting network and broadcast addresses
        else:
            max_addresses = max_subnets

        return [
            max_subnets,
            max_addresses,
            str(network.network_address),
            str(network.broadcast_address),
        ]

# Example:
calc = Calculator()
print(calc.max_subnets("172.8.8.13", 12))
# → ['1048576', '1048574', '172.0.0.0', '172.15.255.255']
   