#!/usr/bin/env python3
import os
from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA


modulus = 0

e = 0

p = 0 
q = 0


phy = (p-1)*(q-1)
d = inverse(e, phy)
 
privkey = RSA.construct((modulus, e, d))
 
with open("privkey.pem", "wb") as fp:
    fp.write(privkey.exportKey())