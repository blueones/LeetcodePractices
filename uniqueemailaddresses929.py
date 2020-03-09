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
class Solution1:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailList = dict()
        for email in emails:
            seperateLocalDomain= email.split('@')
            local = seperateLocalDomain[0]
            domain = seperateLocalDomain[1]
            local = local.replace(".","").split("+")[0]
            finalemail = local+"@"+domain
            # print(emailList, finalemail)
            if finalemail not in emailList:
                
                emailList[finalemail]=1
            else:
                emailList[finalemail]+=1
        return len(emailList)

            