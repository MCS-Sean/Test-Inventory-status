# Synthetic Inventory Health

**Simulation date: 2026-11-10**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 100 |
| Lead-time risk | 3 |
| Reorder | 2 |
| Stockout | 7 |

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
| ITEM-0001 | B - Core Products | Healthy | 482 | 302 | 30 | 37.4 | 137 | 537 | 808 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 167 | 0 | 7 | 26.2 | 91 | 142 | 276 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 536 | 884 | 60 | 35.0 | 392 | 1326 | 1540 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1818 | 0 | 45 | 478.4 | 60 | 235 | 315 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 200 | 0 | 14 | 29.1 | 41 | 144 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 92 | 0 | 45 | 61.3 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 101 | 125 | 14 | 18.1 | 32 | 116 | 233 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 186 | 0 | 60 | 145.6 | 22 | 100 | 139 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 51 | 410 | 90 | 27.8 | 57 | 224 | 263 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1564 | 515 | 60 | 92.8 | 895 | 1923 | 2159 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 271 | 90 | 90 | 99.6 | 65 | 313 | 395 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 426 | 0 | 7 | 32.9 | 33 | 137 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 268 | 155 | 45 | 40.9 | 103 | 405 | 543 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1057 | 0 | 30 | 374.5 | 32 | 120 | 179 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2615 | 0 | 60 | 250.1 | 217 | 855 | 1075 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 73 | 120 | 14 | 13.5 | 31 | 113 | 226 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 538 | 0 | 60 | 597.8 | 17 | 72 | 99 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 588 | 1987 | 2202 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 22 | 20 | 30 | 40.4 | 7 | 24 | 41 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 763 | 1169 | 60 | 53.2 | 850 | 1726 | 1926 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 163 | 0 | 30 | 85.3 | 16 | 76 | 133 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1028 | 0 | 90 | 209.3 | 149 | 596 | 700 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 15 | 0 | 7 | 26.0 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1106 | 0 | 14 | 239.9 | 27 | 97 | 193 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 215 | 135 | 60 | 51.6 | 67 | 322 | 447 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 246 | 0 | 45 | 85.5 | 46 | 179 | 239 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 218 | 245 | 14 | 19.1 | 66 | 238 | 477 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 20.6 | 110 | 167 | 314 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 115 | 0 | 14 | 31.1 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 118 | 355 | 30 | 14.3 | 88 | 345 | 519 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 540 | 315 | 30 | 36.4 | 157 | 618 | 930 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4255 | 0 | 60 | 619.7 | 176 | 595 | 691 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 503 | 0 | 14 | 45.2 | 232 | 399 | 633 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 108 | 0 | 14 | 22.9 | 27 | 98 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 499 | 1324 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 621 | 0 | 45 | 191.4 | 40 | 190 | 287 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 191 | 179 | 60 | 67.1 | 113 | 287 | 372 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 3.8 | 325 | 891 | 1085 | 0 | 4 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 185.3 | 84 | 127 | 186 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 66 | 0 | 45 | 100.7 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 185 | 502 | 60 | 33.7 | 183 | 518 | 683 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 134 | 0 | 7 | 13.7 | 22 | 101 | 307 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 64 | 155 | 7 | 8.8 | 20 | 79 | 232 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4201 | 0 | 60 | 539.4 | 199 | 675 | 784 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 222 | 0 | 14 | 31.2 | 52 | 159 | 259 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 582 | 1950 | 90 | 32.4 | 679 | 2312 | 2564 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 458 | 0 | 45 | 128.8 | 57 | 221 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 90 | 105 | 14 | 18.2 | 28 | 102 | 206 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 51 | 43 | 30 | 35.6 | 13 | 58 | 101 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 449 | 0 | 14 | 70.3 | 37 | 133 | 267 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 60.3 | 191 | 467 | 561 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 525 | 525 | 60 | 43.4 | 249 | 987 | 1241 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 134 | 246 | 45 | 24.1 | 88 | 344 | 461 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 300 | 245 | 14 | 17.8 | 122 | 376 | 613 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 282 | 0 | 30 | 68.4 | 45 | 173 | 260 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 50 | 0 | 7 | 18.3 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 106.7 | 82 | 220 | 310 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 14 | 0 | 7 | 21.4 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Reorder | 918 | 0 | 60 | 80.9 | 236 | 929 | 1167 | 249 | — |
| ITEM-0073 | B - Core Products | Excess | 3414 | 0 | 90 | 877.9 | 119 | 473 | 555 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 37 | 60 | 14 | 18.8 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 25 | 54 | 45 | 28.8 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 958 | 1084 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 305 | 0 | 7 | 172.6 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 25.3 | 107 | 295 | 356 | 0 | 26 |
| ITEM-0079 | B - Core Products | Healthy | 256 | 515 | 45 | 23.1 | 174 | 684 | 917 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 483 | 0 | 45 | 216.3 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 367 | 547 | 90 | 51.8 | 219 | 865 | 1013 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 267 | 0 | 7 | 23.0 | 29 | 122 | 366 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 644 | 0 | 14 | 59.9 | 62 | 224 | 450 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 330 | 0 | 60 | 150.8 | 46 | 180 | 226 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 34 | 0 | 14 | 35.2 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 174 | 135 | 45 | 39.7 | 54 | 256 | 387 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 31.6 | 457 | 745 | 1013 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 60 | 0 | 30 | 40.9 | 13 | 59 | 103 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 488 | 1027 | 90 | 39.9 | 372 | 1486 | 1743 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 32.9 | 256 | 402 | 784 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 57 | 0 | 7 | 12.4 | 12 | 49 | 146 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6504 | 0 | 90 | 356.5 | 690 | 2351 | 2606 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3433 | 0 | 60 | 252.8 | 349 | 1178 | 1368 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 126 | 0 | 7 | 26.0 | 13 | 52 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 87 | 0 | 14 | 28.9 | 18 | 64 | 127 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 621 | 1260 | 60 | 41.3 | 573 | 1491 | 1807 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 176 | 0 | 45 | 99.0 | 22 | 104 | 158 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 84.9 | 317 | 911 | 1048 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 231 | 340 | 45 | 30.5 | 120 | 469 | 628 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 616 | 1789 | 90 | 36.2 | 647 | 2196 | 2434 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 512 | 498 | 60 | 46.5 | 225 | 897 | 1128 | 0 | 47 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 260 | 1034 | 1212 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1360 | 665 | 90 | 92.7 | 561 | 1897 | 2103 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 488 | 1047 | 60 | 28.7 | 437 | 1474 | 1712 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 14 | 45 | 14 | 10.1 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Reorder | 89 | 0 | 45 | 58.0 | 19 | 90 | 136 | 50 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 180 | 714 | 838 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 86 | 260 | 30 | 14.4 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 66 | 58 | 30 | 34.3 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 233 | 0 | 7 | 19.1 | 32 | 130 | 386 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 195 | 0 | 14 | 52.9 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 153 | 211 | 14 | 15.8 | 56 | 202 | 406 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 106 | 0 | 7 | 17.9 | 17 | 65 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 424 | 191 | 45 | 48.0 | 138 | 545 | 730 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 432 | 0 | 14 | 70.1 | 35 | 128 | 257 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 213 | 130 | 60 | 52.2 | 66 | 315 | 438 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3508 | 0 | 60 | 259.6 | 347 | 1172 | 1361 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 263 | 0 | 14 | 36.8 | 52 | 160 | 260 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 628 | 238 | 30 | 42.0 | 199 | 663 | 872 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 706 | 1068 | 60 | 37.8 | 475 | 1616 | 1877 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1974 | 0 | 45 | 199.4 | 156 | 612 | 820 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 375 | 463 | 45 | 35.6 | 166 | 651 | 871 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 490 | 0 | 7 | 39.0 | 37 | 138 | 402 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 856 | 0 | 60 | 194.5 | 91 | 360 | 452 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 84 | 636 | 90 | 27.9 | 93 | 368 | 431 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 67.3 | 406 | 645 | 868 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 584 | 0 | 60 | 168.5 | 72 | 284 | 357 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 186 | 0 | 60 | 138.3 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 398 | 0 | 14 | 56.1 | 41 | 148 | 297 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 698 | 259 | 30 | 40.7 | 227 | 759 | 999 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 311 | 498 | 7 | 14.8 | 318 | 486 | 780 | 0 | — |
