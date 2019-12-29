class Solution:
    def numUniqueEmails(self, emails):
        #use set. set will eliminate duplicate items.
        dictofemails=set()
        for email in emails:
            localdomain=email.split("@")
            local=localdomain[0]
            domain=localdomain[1]
            parsedlocalplus=local.split("+")[0]
            parsedlocalplusdot=parsedlocalplus.replace(".","")
            final=parsedlocalplusdot+"@"+domain
            dictofemails.add(final)
        
        return len(dictofemails)


            