import dns.resolver

# 禁用全局缓存
dns.resolver.Resolver().cache = None


def get_record(domain, type: dns.rdatatype = dns.rdatatype.CNAME):
    data = []
    try:
        answers = dns.resolver.resolve(domain, type)
        for rdata in answers:
            text = rdata.to_text()
            if dns.rdatatype.CNAME == type and text.endswith("."):
                text = text[:-1]
            data.append(text)
        return data
    except dns.resolver.NXDOMAIN:
        return data
    except dns.resolver.NoAnswer:
        return data


# 示例
domain = "www.xinnet.com"
print(get_record(domain, dns.rdatatype.CNAME))
