# Memory_game
This is a game that uses a 320x240 tft screen and 16 mx switches. Its pretty much a meomory games, a 4x4 pattern cann be seen on the screen and some of those squares light up, try to enter them on the mx switches, if you cant do it the game starts again.

# Firmware
Attention! The Firmware was made with Ai!

# PCB

As said the pcb uses a tft 320x240 screen and 16 mx switches, also it uses a rp pico and 16 diodes.

<img width="1010" height="442" alt="memory_gameschematick" src="https://github.com/user-attachments/assets/e371c379-be9b-4d0f-9b1e-a4f0001359cc" />

The tft screen is above the 16 swicthes and the rp pico is on the bottom.

<img width="587" height="566" alt="memory_gamepcb" src="https://github.com/user-attachments/assets/b69319e9-eb19-421f-9703-b8f2e960e375" />

# CAD
I made a pretty simple case to store the pcb in, the screen is completly exposed and the switches are partially covered up (ofcourse there is room for the switches just the spaces in between are covered up)

<img width="584" height="722" alt="image" src="https://github.com/user-attachments/assets/8cc59a21-68f9-47cb-a8f8-42340cbb3d3e" />


<img width="626" height="374" alt="image" src="https://github.com/user-attachments/assets/8e0a9658-1748-4af0-8dd4-2da500414838" />


As you see there are 4 holes to hold the 2 parts togerther, for that I will be using 4 M4 screws, alor 4s am I right?

# BOM
Raspbarry Pi Pico / Required: YES / COST: 17$ / Link: https://www.amazon.de/IBest-Pico-Microcontroller-Board-Pre-Soldered/dp/B091TLCNJD/ref=sr_1_2_sspa?adgrpid=71382112712&dib=eyJ2IjoiMSJ9.JopKME4aoMONkSmgTvmHYcJYrAj8yYsJ_VEZMSbj2CXjeyDCSSqMRD716D8P1oSk5omqCq2T0J1jLe0k4lBnRA2PBEwuPAmWQqQo7iqWOb3jDQgANAbU9OM1e_digfpGrs89UTZCnMAG1oiqk7Ooz7-kHnTkn06KYHjz5siRRHtAzxp7kRb0B7MdAzLZiBDax6lB_sH_eps8aw4h118HPEwZvCOvWspXIRaraquOo7M.ZIpDpwydYrnrK1Vwtn17VzKl7E-J20VRrF9UCYNh1ds&dib_tag=se&hvadid=676492002894&hvdev=c&hvexpln=0&hvlocphy=1000690&hvnetw=g&hvocijid=38328084338439323--&hvqmt=e&hvrand=38328084338439323&hvtargid=kwd-1185628278465&hydadcr=26425_2797057&keywords=raspberry%2Bpi%2Bpico%2Bamazon&mcid=4272132b329935d2aa1093ee1c242b10&qid=1753281278&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1

4x M4 screws / Required: NO / COST: 6$ / Link:  Link: https://de.aliexpress.com/item/1005007159750547.html?src=google&pdp_npi=4%40dis!EUR!5.59!5.47!!!!!%40!12000039655872513!ppc!!!&src=google&albch=shopping&acnt=615-992-9880&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_oFgTQeV&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=de1005007159750547&ds_e_product_merchant_id=654239350&ds_e_product_country=AT&ds_e_product_language=de&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=22482375352&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22482428299&gbraid=0AAAAA_TvRHqbdMdvv4yLgoHxuPzqSRUUz&gclid=Cj0KCQjwkILEBhDeARIsAL--pjx7K9E937sz6-7abxWOtLTGcakH9O7FHxS4DmKv-i_RxzDqIHP1Qo8aAmg6EALw_wcB

16 diodes / Required: YES / COST: 3$ / Link:https://de.aliexpress.com/item/1005005707644429.html?src=google&pdp_npi=4%40dis!EUR!1.57!1.57!!!!!%40!12000034075505703!ppc!!!&src=google&albch=shopping&acnt=615-992-9880&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_oFgTQeV&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=de1005005707644429&ds_e_product_merchant_id=5055919252&ds_e_product_country=AT&ds_e_product_language=de&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=22482375352&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22482428299&gbraid=0AAAAA_TvRHqbdMdvv4yLgoHxuPzqSRUUz&gclid=Cj0KCQjwkILEBhDeARIsAL--pjyyiVILkbUKRgAGii3Gls3qtWBFSL2nvHr4z5c5il5uQQGCqNgchxwaAmU4EALw_wcB

16 mx switches / Required: YES / COST: 6$ / Link: https://de.aliexpress.com/item/1005007503045573.html?src=google&pdp_npi=4%40dis!EUR!0.83!0.49!!!!!%40!12000045838558309!ppc!!!&src=google&albch=shopping&acnt=615-992-9880&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_oFgTQeV&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=de1005007503045573&ds_e_product_merchant_id=109387492&ds_e_product_country=AT&ds_e_product_language=de&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=22482375352&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22482428299&gbraid=0AAAAA_TvRHqbdMdvv4yLgoHxuPzqSRUUz&gclid=Cj0KCQjwkILEBhDeARIsAL--pjzeF16zltABir5Tw_KdGp8of-SdjQHntJ96R5WI48cDXgRDA2FpRs4aAoRnEALw_wcB

Tft screen / Required: YES / COST: 22$ / Link: https://de.aliexpress.com/item/1005007503045573.html?src=google&pdp_npi=4%40dis!EUR!0.83!0.49!!!!!%40!12000045838558309!ppc!!!&src=google&albch=shopping&acnt=615-992-9880&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_oFgTQeV&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=de1005007503045573&ds_e_product_merchant_id=109387492&ds_e_product_country=AT&ds_e_product_language=de&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=22482375352&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22482428299&gbraid=0AAAAA_TvRHqbdMdvv4yLgoHxuPzqSRUUz&gclid=Cj0KCQjwkILEBhDeARIsAL--pjzeF16zltABir5Tw_KdGp8of-SdjQHntJ96R5WI48cDXgRDA2FpRs4aAoRnEALw_wcB

Total cost of BOM: (only needed parts) 48$





