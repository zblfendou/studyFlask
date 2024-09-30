import dns.resolver

# 禁用全局缓存
dns.resolver.Resolver().cache = None


def get_record(domain: str, type: str) -> list:
    """
       Get DNS records for a domain and record type
       :param domain: Domain name
       :param type: Record type (A, CNAME, or TXT)
       :return: List of DNS records
   """
    dns_data_type = dns.rdatatype.from_text(type.upper())
    try:
        answers = dns.resolver.resolve(domain, dns_data_type)
        return [rdata.to_text().rstrip(".") if dns_data_type == dns.rdatatype.CNAME and rdata.to_text().endswith(
            ".") else rdata.to_text() for rdata in answers]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return []


# 示例
domain = "niujf.top"
print(get_record(domain, 'a'))
