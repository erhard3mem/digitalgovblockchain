# digitalgovblockchain

This app symoblizes a virtual voting chamber for governments and is due to the simplest version of "blockchain" proof-secure. 

Every vote has a unique 'fingerprint' within the md5-blockchain. 

You can vote as often you want, but if you share the link to your fingerprint-URL, somebody else can attach to the position of your votings and vote.

For example:

0. #start: 00001
1. vote 'No' = 00002 = hash(hash(00001)+'No')
2. vote 'Yes' = shareLink(hash(hash(00002)+'Yes'))
3. link shared to another participant

## start it

> python web.py
