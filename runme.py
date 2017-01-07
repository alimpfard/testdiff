from bs4 import BeautifulSoup
import requests
from hashlib import md5
import re
import difflib

def auth(S, uname, passed):
    m = md5()
    m.update(bytes(str(passed),"utf-8"))
    data = {"UserType": "Student"}
    data["UserCode"] = str(uname)
    data["KeyCode"] = m.hexdigest()
    r = S.post("http://amozesh.tabrizu.ac.ir/samaweb/login.asp", data=data)
    return r
def update(S):
    r = S.get("http://amozesh.tabrizu.ac.ir/samaweb/WorkBookRequest.asp")
    return r

def main():
    S = requests.Session()
    uname = int(re.search(r'([0-9]{9})',input("Username? [0-9]{9}: ")).group(1))
    passwd = int(re.search(r'([0-9]{9})',input("Password? [0-9]{12}: ")).group(1))
    r = auth(S, uname, passwd)
    soup = BeautifulSoup(update(S).text, "html.parser")
    last = soup.get_text()
    while(True):
        a=0
        soup = BeautifulSoup(update(S).text, "html.parser")
        for _,s in enumerate(difflib.ndiff(soup.get_text(), last)):
            if s[0]==' ':
                continue
            elif s[0]=='-':
                print(u'Deleted "{}" from position {}'.format(s[-1],i))
                a+=1
            elif s[0]=='+':
                print(u'Added "{}" to position {}'.format(s[-1],i))
                a+=1
        if a is 0:
            print("No Change detected.")
        else:
            print("\a\a\a\a"*10)
        last = soup.get_text()
        __import__("time").sleep(5*60)
if __name__ == "__main__":
    main()
