import ipaddress

def hitung_prefix(ip):
    first_octet = int(str(ip).split('.')[0])
    if 1 <= first_octet <= 126:
        return 8
    elif 128 <= first_octet <= 191:
        return 16
    elif 192 <= first_octet <= 223:
        return 24
    return None


def kalkulator_subnet(ip_input, target_prefix=None):
    ip_obj = ipaddress.ip_interface(ip_input)
    jaringan = ip_obj.network
    ip = ip_obj.ip

    hasil = {
        "ip": str(ip),
        "prefix": jaringan.prefixlen,
        "netmask": str(jaringan.netmask),
        "network": str(jaringan.network_address),
        "broadcast": str(jaringan.broadcast_address),
        "total_ip": jaringan.num_addresses,
    }

    if jaringan.num_addresses > 2:
        hosts = list(jaringan.hosts())
        hasil["usable_host"] = jaringan.num_addresses - 2
        hasil["host_range"] = f"{hosts[0]} - {hosts[-1]}"
    else:
        hasil["usable_host"] = 0
        hasil["host_range"] = "Tidak ada"

    if ip == jaringan.network_address:
        hasil["status_ip"] = "Network"
    elif ip == jaringan.broadcast_address:
        hasil["status_ip"] = "Broadcast"
    else:
        hasil["status_ip"] = "Host"

    default = hitung_prefix(jaringan.network_address)
    if default:
        hasil["default_class_prefix"] = default
        if jaringan.prefixlen > default:
            hasil["jumlah_subnet"] = 2 ** (jaringan.prefixlen - default)

    if target_prefix:
        if target_prefix >= jaringan.prefixlen:
            hasil["total_subnet_target"] = 2 ** (target_prefix - jaringan.prefixlen)
        else:
            hasil["total_subnet_target"] = "Prefix tidak valid"

    return hasil
