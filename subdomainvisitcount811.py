class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_domain = dict()
        def input_dict(domain, visit):
            if domain in dict_domain:
                dict_domain[domain] += visit
            else:
                dict_domain[domain] = visit
        for visit_domain in cpdomains:
            visit, domain = visit_domain.split(" ")
            while domain:
                input_dict(domain, int(visit))
                dot = domain.find(".")
                if dot == -1:
                    break
                domain = domain[dot+1:]
        ans = [str(dict_domain[domain])+" "+domain for domain in dict_domain]
        return ans
            
            