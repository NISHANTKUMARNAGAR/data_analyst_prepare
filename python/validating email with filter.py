def fun(s):
    if(s.count('@')==1 and s.count('.')==1):
        c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_'
        u=s.split('@')[0]
        w=(s.split('@')[1]).split('.')[0]
        d=(s.split('@')[1]).split('.')[1]
        if(len(u)!=0 and len(w)!=0 and len(d)!=0):
          if (w.isalnum() and d.isalpha() and len(d)<=3):
            for i in u:
              if i in c:
                pass
              else:
                return False
            return True
          else:
            return False
        else:
          return False
    else:
      return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)