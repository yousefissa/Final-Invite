import requests
from random import getrandbits

def main():
    share_hash = input('Input your entire referral URL: ').split('=', 1)  
    
    for i in range(1, 1000):
        email = 'test+{}@gmail.com'.format(getrandbits(40))
        payload = {"signup[email]": email, "signup[share_hash": share_hash, "subscribe": ""}
        response = requests.post('https://apply.getfinal.com/signups', data=payload)
        print('{}/1000: Created an account. '.format(i))

if __name__ == "__main__":
    main()
