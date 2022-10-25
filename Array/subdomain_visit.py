class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def get_all_domains(full_domain):
            subdomains = full_domain.split('.')
            subdomains = subdomains[::-1]
            all_domains = []
            
            curr_domain = subdomains[0]
            for i in range(1, len(subdomains)):
                all_domains.append(curr_domain)
                curr_domain = subdomains[i] + '.' + curr_domain
            all_domains.append(curr_domain)  
            return all_domains

        domain_to_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, full_domain = cpdomain.split()
            count = int(count)
            
            domains = get_all_domains(full_domain)
            print(domains)
            
            for domain in domains:
                domain_to_count[domain] += count
        res = []
        
        for domain, count in domain_to_count.items():
            string = str(count) + ' ' + domain
            res.append(string)
        return res
