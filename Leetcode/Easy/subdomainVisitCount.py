# https://leetcode.com/problems/subdomain-visit-count/

# Easy

# Time: O(N^3) | Space: O(N)
def subdomainVisits(self, cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    dict_domain_count = {}
    
    for domain in cpdomains:
        count_fullEmail = domain.split(" ")
        count = int(count_fullEmail[0])
        full_email = count_fullEmail[1]
        full_email_array = full_email.split(".")
        for i in range(len(full_email_array)):
            domain = ".".join(full_email_array[i:])
            if domain in dict_domain_count:
                dict_domain_count[domain] += count
            else:
                dict_domain_count[domain] = count
    
    result = []
    
    for domain in dict_domain_count:
        
        result.append(str(dict_domain_count[domain]) + " " + domain)
        
    return result