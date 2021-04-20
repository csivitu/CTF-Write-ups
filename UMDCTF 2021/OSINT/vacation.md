# Vacation - OSINT

Author - [BlackJack](http://github.com/Mannan-Goyal)

Requirements : Know how to google

* * *

When we start to solve the challenge we are faced with a pretty elaborate hint which says -

> My mom told me she went to this amazing brewing company in the Carribbean and when I asked her the name of the place, she sent me a picture of her ship. Can you help me find the name of this brewing company?

This already narrows our search in the Carribbean...

After this we move on to inspect the picture provided as a google drive link

![Challenge Image](https://lh3.googleusercontent.com/fife/ABSRlIoJz8F6GMMjVYrLh7-cfEAqrRP6IBO8BT0_U-KpvWxdHAdDinNBRhC6vyk6AvFPF_AG5XxRx1UqPOfLnTxNlEWSP16vLl2on5H5a20zpxfAkr6R8KvjLCQtLr2jJ9lbcg3Xz7tW9MU_ncKpKPImg4EVMETes96kX8uglzjz6NWm7XhpbXQenkFUDeyQOMuqFlArBeQCiAgNQ7RuQ55Tx-vWivYd-P1hnseWg1Xo_xhXBQ_XHKBqTUtchoOfG48wh3rQFcBVA2f7unJjI2bih2wk9CcicvOTKdKAT1Yfwzy_N-XzylVUxLm5ebZA8RlcU0m_Z6FRMNswDlQLt5I3OjSboiRkMwjqN1CKzUpzwO-pWZ0G9Pe_w7wmJpxv5lJ9228EdSPDNnZ-aWMfkGe0RaT94LY8AIUzMEX8PpCbk8zN6Cu9p4fRJbCus5DBw4jB6CNwL03pvFqnelgoBTKD82QKro07VmJ6Zg7NFjFBL_Iao7HsKYEZQcqdv23SZNEU1mTYbJfx8i8Lxv4KHuLMUftpJaTRR3lAMF-2lPVlml_yGxLvE7DE-OAti1y33-L5TPyYOwYPgpFDNYfHpbw21mENVC2r2eYnd27sL22-YkQycieXSlQANXJJX6Rqj8b0RpLy9NYd8qyKZ0SbY78-MVa2MapCyAhpTntsa3OArE2QDAM_CDHniZ9iK94NONdl0M0FGRKgSfseiaIlXYJL2oRiLNoz1W9OZ9A=w1346-h647-ft)

From this we can gather 3 hints-
![Challenge_Image_Hints](https://i.imgur.com/eqi0WFe.png)

1.  Name of the Ship - Freedom of Seas
2.  Name of the ship owning company - RoyalCalCarribbean
3.  Name of the bar - Rum Therapy

After this I immediately went on to look up the route that this particular ship usually takes, with a simple google search I found this - [Route](https://www.cruisemapper.com/ships/Freedom-Of-The-Seas-654)

This didn't help much so I went on to search the bar on google, since the top searches were mostly promotional I thought it would be better to just move to the map view where I saw
![Map View](https://i.imgur.com/m8dafEg.png)

Since there were only 2 results I changed to 3d satellite view by dropping the marker on the bottom left near both locations, when I saw the 1st location

![Sat View](https://i.imgur.com/MseMAjY.png)
the scene seemed very familiar to the original picture and if you zoom in a bit you'd see Antillia Brewing Company. Couldn't be a coincidence now...

So I went on to submit the flag and I wrote this
`UMDCTF-{Stlucia_Antillia}`

Which was ofcourse incorrect, it was later after a lot of frustration I realised that Instead of St. Lucia I had to write the name of the city

So finally the flag is
`UMDCTF-{Castries_Antillia}`

(This city name was also mentioned on the top left in the satellite view image that I included above)
