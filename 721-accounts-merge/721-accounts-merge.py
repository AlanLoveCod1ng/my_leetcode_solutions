class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(index):
            if account_rep[index] == index:
                return index
            account_rep[index] = find(account_rep[index])
            return account_rep[index]
            
        def combine(a1,a2):
            re1 = find(a1)
            re2 = find(a2)
            if size[re1] > size[re2]:
                account_rep[re2] = re1
                size[re1] += size[re2]
            else:
                account_rep[re1] = re2
                size[re2] += size[re1]
        
        
        mail_account = {}
        # account_rep[i] is the index of representative account of the account with index i
        account_rep = [i for i in range(len(accounts))]
        account_name = ["" for _ in range(len(accounts))]
        size = [1]*len(accounts)
        for account_index in range(len(accounts)):
            account_name[account_index] = accounts[account_index][0]
            for email_index in range(1,len(accounts[account_index])):
                current_email = accounts[account_index][email_index]
                if not current_email in mail_account:
                    mail_account[current_email] = account_index
                else:
                    combine(account_index, mail_account[current_email])
        
        # representative : [list of email in its set]
        hashtable = {}
        for email in mail_account:
            rep = find(mail_account[email])
            temp_list = hashtable.get(rep,[])
            temp_list.append(email)
            hashtable[rep] = temp_list
        res = []
        for rep in hashtable:
            list_email = hashtable[rep]
            res.append([account_name[rep]]+sorted(list_email))
        return res
        