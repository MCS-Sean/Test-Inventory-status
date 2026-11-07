# Synthetic Inventory Health

**Simulation date: 2026-11-07**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 95 |
| Lead-time risk | 3 |
| Reorder | 6 |
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
| ITEM-0001 | B - Core Products | Healthy | 497 | 302 | 30 | 37.7 | 139 | 548 | 824 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 376 | 1107 | 60 | 24.8 | 389 | 1314 | 1526 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1829 | 0 | 45 | 474.4 | 61 | 239 | 320 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 213 | 0 | 14 | 30.8 | 41 | 145 | 291 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 98 | 0 | 45 | 65.8 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Reorder | 116 | 0 | 14 | 20.4 | 33 | 119 | 238 | 125 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 191 | 0 | 60 | 152.1 | 21 | 98 | 136 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 60 | 410 | 90 | 34.0 | 55 | 216 | 253 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 145.2 | 780 | 1618 | 1810 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 281 | 90 | 90 | 102.8 | 65 | 314 | 396 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 469 | 0 | 7 | 36.2 | 34 | 138 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 288 | 155 | 45 | 43.9 | 103 | 405 | 543 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1070 | 0 | 30 | 373.3 | 33 | 122 | 183 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2641 | 0 | 60 | 252.6 | 216 | 854 | 1074 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 92 | 120 | 14 | 16.8 | 32 | 114 | 229 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 542 | 0 | 60 | 609.8 | 16 | 71 | 97 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 580 | 1961 | 2173 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 24 | 20 | 30 | 43.2 | 7 | 25 | 41 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 1000 | 626 | 60 | 84.9 | 591 | 1310 | 1557 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 169 | 0 | 30 | 89.5 | 16 | 75 | 132 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1045 | 0 | 90 | 214.2 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 44.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1126 | 0 | 14 | 245.4 | 27 | 96 | 193 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 226 | 135 | 60 | 53.1 | 68 | 328 | 456 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 254 | 0 | 45 | 87.6 | 47 | 181 | 242 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Reorder | 239 | 0 | 14 | 20.6 | 66 | 240 | 484 | 245 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 41.4 | 100 | 148 | 272 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 121 | 0 | 14 | 31.7 | 23 | 81 | 161 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 141 | 355 | 30 | 17.0 | 89 | 347 | 521 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 583 | 315 | 30 | 39.1 | 158 | 620 | 933 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4273 | 0 | 60 | 612.4 | 179 | 605 | 703 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 61.2 | 221 | 371 | 579 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 125 | 0 | 14 | 26.9 | 27 | 97 | 195 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 626 | 0 | 45 | 190.3 | 40 | 192 | 290 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 62.7 | 141 | 462 | 568 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 192 | 179 | 60 | 67.8 | 113 | 286 | 371 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 113 | 790 | 60 | 13.5 | 302 | 815 | 991 | 0 | 14 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 141.0 | 99 | 155 | 233 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 67 | 0 | 45 | 100.5 | 10 | 41 | 61 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 164 | 0 | 7 | 16.6 | 23 | 103 | 310 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 83 | 0 | 7 | 11.3 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4241 | 0 | 60 | 540.6 | 201 | 680 | 790 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 252 | 0 | 14 | 35.3 | 52 | 159 | 259 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 614 | 1950 | 90 | 33.8 | 687 | 2341 | 2595 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 474 | 0 | 45 | 132.9 | 57 | 222 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Reorder | 104 | 0 | 14 | 20.9 | 29 | 104 | 209 | 105 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 57 | 43 | 30 | 40.4 | 13 | 57 | 100 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 463 | 0 | 14 | 72.1 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 52.9 | 210 | 524 | 632 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 559 | 525 | 60 | 45.6 | 253 | 1002 | 1259 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 147 | 246 | 45 | 26.3 | 88 | 346 | 463 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 378 | 0 | 14 | 23.1 | 118 | 363 | 592 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 307 | 0 | 30 | 75.1 | 45 | 172 | 258 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 57 | 0 | 7 | 20.9 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 106.7 | 82 | 220 | 310 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 15 | 0 | 7 | 22.5 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 968 | 0 | 60 | 86.3 | 233 | 918 | 1154 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3427 | 0 | 90 | 881.2 | 119 | 473 | 555 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 44 | 0 | 14 | 22.5 | 9 | 39 | 97 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 27 | 54 | 45 | 31.2 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 964 | 1090 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 309 | 0 | 7 | 173.8 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 25.3 | 107 | 295 | 356 | 0 | 26 |
| ITEM-0079 | B - Core Products | Healthy | 288 | 515 | 45 | 26.0 | 174 | 684 | 917 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 492 | 0 | 45 | 220.3 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 236 | 705 | 90 | 33.7 | 216 | 853 | 1000 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 44 | 250 | 7 | 3.8 | 29 | 122 | 366 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 666 | 0 | 14 | 60.1 | 64 | 231 | 464 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 337 | 0 | 60 | 153.2 | 46 | 181 | 227 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 422 | 0 | 14 | 37.0 | 229 | 401 | 640 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 37 | 0 | 14 | 38.3 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 193 | 135 | 45 | 45.0 | 53 | 251 | 379 | 0 | — |
| ITEM-0089 | A - Top Movers | Reorder | 688 | 0 | 14 | 34.2 | 473 | 775 | 1057 | 369 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 15 | 50 | 30 | 10.4 | 13 | 58 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 504 | 1027 | 90 | 40.1 | 382 | 1526 | 1790 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 32.9 | 256 | 402 | 784 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 72 | 0 | 7 | 15.4 | 12 | 50 | 148 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6559 | 0 | 90 | 364.6 | 682 | 2319 | 2571 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3476 | 0 | 60 | 257.5 | 347 | 1171 | 1360 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 41.7 | 89 | 130 | 236 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 25 | 115 | 7 | 4.9 | 15 | 56 | 163 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 94 | 0 | 14 | 30.0 | 18 | 65 | 131 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 41.3 | 711 | 1629 | 1840 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 182 | 0 | 45 | 100.5 | 23 | 107 | 161 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 76.8 | 352 | 1034 | 1191 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 263 | 340 | 45 | 35.1 | 119 | 464 | 622 | 0 | — |
| ITEM-0106 | A - Top Movers | Reorder | 660 | 1542 | 90 | 38.6 | 652 | 2210 | 2449 | 247 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 532 | 498 | 60 | 48.2 | 226 | 900 | 1131 | 0 | 49 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1044 | 1224 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1405 | 665 | 90 | 97.0 | 554 | 1873 | 2076 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 526 | 1047 | 60 | 30.5 | 443 | 1495 | 1737 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 15 | 45 | 14 | 10.4 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 128.3 | 182 | 276 | 407 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 96 | 0 | 45 | 64.5 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 178 | 703 | 824 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 113 | 135 | 30 | 19.3 | 63 | 245 | 368 | 0 | — |
| ITEM-0120 | C - Slow Moving | Reorder | 74 | 0 | 30 | 38.9 | 16 | 75 | 132 | 58 | — |
| ITEM-0121 | B - Core Products | Healthy | 266 | 0 | 7 | 22.1 | 33 | 130 | 382 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 591 | 45 | 0.0 | 313 | 644 | 794 | 203 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 179 | 211 | 14 | 18.4 | 56 | 202 | 406 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 117 | 0 | 7 | 19.5 | 17 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 214.3 | 278 | 414 | 475 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 455 | 191 | 45 | 51.2 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 453 | 0 | 14 | 74.5 | 35 | 127 | 254 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 230 | 130 | 60 | 56.6 | 66 | 315 | 437 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3537 | 0 | 60 | 256.1 | 356 | 1199 | 1392 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 281 | 0 | 14 | 38.1 | 53 | 164 | 267 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 430 | 245 | 30 | 28.9 | 199 | 661 | 870 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 758 | 1068 | 60 | 40.3 | 478 | 1625 | 1888 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1993 | 0 | 45 | 203.6 | 155 | 606 | 811 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 85.3 | 620 | 1458 | 1746 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 398 | 463 | 45 | 37.0 | 170 | 665 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 532 | 0 | 7 | 42.6 | 38 | 138 | 401 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 874 | 0 | 60 | 199.1 | 91 | 359 | 451 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 94 | 636 | 90 | 30.7 | 95 | 375 | 439 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 60.0 | 430 | 698 | 948 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 592 | 0 | 60 | 167.5 | 73 | 289 | 363 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 191 | 0 | 60 | 142.1 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 416 | 0 | 14 | 57.2 | 42 | 152 | 304 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 463 | 533 | 30 | 26.7 | 230 | 768 | 1011 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 314 | 498 | 7 | 14.3 | 321 | 497 | 805 | 0 | — |
