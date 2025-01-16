import requests
import hashlib
def request_api(code):
    respond = requests.get("https://api.pwnedpasswords.com/range/" +code )
    if respond.status_code!=200:
        raise RuntimeError(f"error type {respond.status_code}")
    return respond
    
def read_hash(hashs,tail):
    hashs = (x.split(":") for x in hashs.text.splitlines())
    for x,y in hashs:
        if x==tail:
            return y
    return 0 
def pass_check(password):
    a = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5,tail = a[:5],a[5:]
    result = request_api(first5)
    return read_hash(result,tail)
   

import sys
def main(args):

    for counts in args[1:]:
        count = pass_check(counts)
        if count:
            print (f"{counts} code is breakable!!!\nIt was pwned {count} times")
        else:
            print(f"{counts} is good passwords!!!")
main(sys.argv)