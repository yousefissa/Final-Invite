import requests, threading, random

# It looks like the signup endpoint is down right now so don't expect this to work until that endpoint is back up
# I also didn't test this at all so it might be buggy

# Actually make the signup request
def signup(email, share_hash):
    payload = {
        "signup[email]": email,
        "signup[share_hash]": share_hash,
        "subscribe": ""
    }
    response = requests.post("https://apply.getfinal.com/signups", data=payload) # Do something with the response if you want

# Create a thread for each signup we need so we can basically do them all at once
# There's a better way to do this than with threading, but this is cheap and less complicated
def run(share_hash, signup_count):
    for i in range(0, signup_count):
        email = ("dummy+{}@gmail.com").format(random.getrandbits(128)) # Format our dummy email with some random bits so final recognizes it as a new email
        thread = threading.Thread(target=signup, args=(share_hash, email)) # Do something with this thread if you want
        thread.start()

def main():
    share_hash = "NgL_o4vA" # Replace this with your own referral hash (the stuff at the end of your referral link)
    signup_count = 1000 # How many referral signups you want, 1000 is safe
    run(share_hash, signup_count)

if __name__ == "__main__":
    main()