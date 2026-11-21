# Synthetic Inventory Health

**Simulation date: 2026-11-21**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 25 |
| Healthy | 98 |
| Lead-time risk | 6 |
| Reorder | 3 |
| Stockout | 6 |

## Movement classes

| Class | Items |
|---|---:|
| A - Top Movers | 25 |
| B - Core Products | 75 |
| C - Slow Moving | 38 |
| Dead Inv | 22 |

## Stocking detail

Longer lead times increase demand exposure and stock targets. Incoming orders count toward inventory position, but late receipts can still create a stockout risk.

| Item | Class | Health | On hand | On order | Lead days | Cover days | Safety | Reorder | Target | New order | Gap in days |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ITEM-0001 | B - Core Products | Healthy | 343 | 302 | 30 | 26.3 | 139 | 544 | 818 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 258 | 0 | 7 | 35.2 | 96 | 155 | 309 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 382 | 1107 | 60 | 24.9 | 393 | 1328 | 1543 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1765 | 0 | 45 | 460.4 | 61 | 238 | 318 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 115 | 150 | 14 | 16.8 | 41 | 144 | 288 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 74 | 46 | 45 | 50.5 | 19 | 87 | 131 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 21 | 125 | 14 | 3.6 | 42 | 129 | 210 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 169 | 0 | 60 | 130.0 | 22 | 102 | 141 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 431 | 0 | 90 | 225.5 | 60 | 234 | 275 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 103.8 | 798 | 1659 | 1856 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 247 | 90 | 90 | 95.4 | 62 | 298 | 376 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 270 | 0 | 7 | 20.1 | 34 | 142 | 423 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 200 | 300 | 45 | 31.0 | 101 | 398 | 534 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1018 | 0 | 30 | 351.0 | 33 | 123 | 184 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2507 | 0 | 60 | 242.4 | 214 | 846 | 1063 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 116 | 0 | 14 | 21.0 | 32 | 115 | 231 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 524 | 0 | 60 | 548.4 | 17 | 76 | 104 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2248 | 0 | 90 | 144.5 | 597 | 2013 | 2231 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 16 | 20 | 30 | 31.3 | 7 | 23 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 77.6 | 632 | 1388 | 1648 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 135 | 0 | 30 | 69.8 | 17 | 77 | 135 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 973 | 0 | 90 | 199.5 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 34 | 0 | 7 | 57.7 | 8 | 13 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1052 | 0 | 14 | 233.8 | 27 | 95 | 189 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 164 | 265 | 60 | 38.2 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 199 | 0 | 45 | 66.3 | 48 | 186 | 249 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 349 | 0 | 14 | 31.0 | 65 | 234 | 471 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 63 | 90 | 14 | 17.0 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 180 | 183 | 30 | 21.4 | 90 | 352 | 528 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 383 | 315 | 30 | 25.5 | 159 | 625 | 940 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4159 | 0 | 60 | 601.8 | 177 | 599 | 696 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 686 | 0 | 14 | 53.5 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 57 | 100 | 14 | 12.5 | 27 | 96 | 191 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 511 | 1357 | 1552 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 587 | 0 | 45 | 183.4 | 39 | 187 | 283 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 65.1 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 59 | 0 | 45 | 93.2 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 243 | 0 | 7 | 24.8 | 23 | 102 | 308 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 133 | 0 | 7 | 17.9 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4099 | 0 | 60 | 509.5 | 205 | 696 | 809 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 138 | 100 | 14 | 19.9 | 51 | 156 | 253 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 396 | 1950 | 90 | 22.9 | 656 | 2227 | 2468 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1010 | 0 | 30 | 86.3 | 428 | 791 | 1037 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 415 | 0 | 45 | 116.0 | 57 | 222 | 297 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 27 | 105 | 14 | 5.3 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 26 | 43 | 30 | 17.6 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 392 | 0 | 14 | 63.6 | 36 | 129 | 258 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 471 | 160 | 60 | 89.4 | 215 | 537 | 647 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 354 | 790 | 60 | 28.0 | 261 | 1033 | 1299 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 71 | 367 | 45 | 12.5 | 89 | 350 | 469 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 164 | 245 | 14 | 10.0 | 121 | 366 | 595 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 232 | 0 | 30 | 58.5 | 44 | 167 | 251 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 22 | 85 | 7 | 8.2 | 6 | 28 | 108 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 7 | 25 | 7 | 11.2 | 3 | 8 | 27 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 784 | 249 | 60 | 68.1 | 238 | 941 | 1182 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3355 | 0 | 90 | 867.7 | 118 | 470 | 552 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 11 | 60 | 14 | 5.5 | 9 | 39 | 99 | 0 | 6 |
| ITEM-0075 | C - Slow Moving | Healthy | 43 | 28 | 45 | 47.2 | 13 | 55 | 83 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 523 | 1342 | 1531 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 279 | 0 | 7 | 156.9 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 144 | 454 | 556 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 406 | 495 | 45 | 36.9 | 173 | 679 | 910 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 451 | 0 | 45 | 193.3 | 29 | 137 | 207 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 304 | 699 | 90 | 43.4 | 216 | 855 | 1002 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 133 | 0 | 7 | 11.5 | 29 | 122 | 365 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 571 | 0 | 14 | 55.0 | 61 | 217 | 435 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 290 | 0 | 60 | 123.7 | 49 | 193 | 242 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 19 | 30 | 14 | 19.4 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 246 | 137 | 45 | 54.7 | 56 | 263 | 398 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 46.3 | 460 | 752 | 1023 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 42 | 45 | 30 | 29.1 | 13 | 58 | 102 | 0 | 30 |
| ITEM-0092 | B - Core Products | Healthy | 777 | 853 | 90 | 63.5 | 373 | 1488 | 1745 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 204 | 475 | 7 | 11.5 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 104 | 0 | 7 | 23.1 | 12 | 48 | 143 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6325 | 0 | 90 | 346.5 | 690 | 2352 | 2607 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3269 | 0 | 60 | 239.8 | 351 | 1183 | 1374 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 62 | 0 | 7 | 12.9 | 14 | 53 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 47 | 65 | 14 | 15.8 | 17 | 62 | 125 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 77.9 | 641 | 1503 | 1701 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 147 | 0 | 45 | 82.2 | 22 | 105 | 158 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 174 | 340 | 45 | 24.5 | 114 | 442 | 591 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1033 | 1265 | 90 | 64.2 | 616 | 2082 | 2307 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 393 | 498 | 60 | 36.0 | 223 | 889 | 1118 | 0 | 37 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 265 | 1056 | 1239 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1204 | 890 | 90 | 81.9 | 561 | 1899 | 2105 | 0 | — |
| ITEM-0112 | A - Top Movers | Reorder | 255 | 1292 | 60 | 14.1 | 461 | 1565 | 1818 | 271 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 45 | 0 | 14 | 32.1 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 614 | 0 | 14 | 135.1 | 129 | 198 | 293 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 76 | 50 | 45 | 49.2 | 19 | 91 | 137 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 502 | 242 | 90 | 86.2 | 179 | 709 | 832 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 151 | 125 | 30 | 25.2 | 65 | 251 | 377 | 0 | 26 |
| ITEM-0120 | C - Slow Moving | Healthy | 45 | 58 | 30 | 23.7 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 82 | 255 | 7 | 6.9 | 30 | 126 | 375 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 1000 | 45 | 0.0 | 362 | 800 | 1000 | 0 | 26 |
| ITEM-0123 | B - Core Products | Lead-time risk | 63 | 0 | 14 | 13.9 | 121 | 189 | 285 | 222 | 14 |
| ITEM-0124 | B - Core Products | Healthy | 259 | 0 | 14 | 27.5 | 55 | 197 | 394 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 31 | 133 | 7 | 4.9 | 18 | 69 | 201 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Reorder | 349 | 191 | 45 | 39.9 | 137 | 540 | 723 | 183 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 150.7 | 623 | 1602 | 1828 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 385 | 0 | 14 | 66.8 | 34 | 121 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 175 | 255 | 60 | 43.0 | 66 | 315 | 437 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3341 | 0 | 60 | 247.5 | 346 | 1170 | 1359 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 171 | 0 | 14 | 24.2 | 51 | 158 | 257 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 449 | 238 | 30 | 30.3 | 196 | 655 | 862 | 0 | — |
| ITEM-0140 | A - Top Movers | Reorder | 796 | 799 | 60 | 42.5 | 477 | 1621 | 1883 | 288 | — |
| ITEM-0141 | B - Core Products | Excess | 1838 | 0 | 45 | 182.0 | 158 | 623 | 835 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 939 | 635 | 60 | 63.6 | 650 | 1551 | 1860 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 262 | 463 | 45 | 24.6 | 167 | 657 | 881 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 373 | 0 | 7 | 30.8 | 33 | 130 | 384 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 784 | 0 | 60 | 170.4 | 95 | 376 | 473 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 51 | 636 | 90 | 18.2 | 86 | 341 | 400 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 73.8 | 310 | 525 | 825 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 522 | 0 | 60 | 147.3 | 74 | 291 | 365 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 166 | 0 | 60 | 122.5 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 306 | 0 | 14 | 40.7 | 43 | 156 | 314 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 462 | 514 | 30 | 26.2 | 234 | 782 | 1029 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
