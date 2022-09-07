class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # extract user and domain name
            user, domain = email.split('@')
            user = user.split('+')[0].replace('.','')
            cleaned_email = user + '@' + domain
            unique_emails.add(cleaned_email)
        
        print(unique_emails)
        return len(unique_emails)