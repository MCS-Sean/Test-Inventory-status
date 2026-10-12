# Synthetic Inventory Health

**Simulation date: 2026-10-12**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 84 |
| Lead-time risk | 8 |
| Reorder | 4 |
| Stockout | 13 |

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
| ITEM-0001 | B - Core Products | Healthy | 548 | 0 | 30 | 42.7 | 136 | 534 | 804 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 36.2 | 91 | 143 | 277 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 485 | 968 | 60 | 31.0 | 401 | 1355 | 1574 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1925 | 0 | 45 | 385.0 | 81 | 311 | 416 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 226 | 0 | 14 | 29.8 | 44 | 158 | 317 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 134 | 0 | 45 | 84.3 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 132 | 145 | 14 | 19.7 | 41 | 142 | 282 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 29 | 198 | 60 | 20.2 | 24 | 112 | 155 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 105 | 410 | 90 | 47.5 | 69 | 271 | 317 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 349 | 0 | 90 | 119.9 | 69 | 334 | 422 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 821 | 0 | 7 | 64.2 | 32 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 86.7 | 78 | 203 | 285 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 455 | 0 | 45 | 68.5 | 104 | 410 | 550 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1139 | 0 | 30 | 307.8 | 43 | 158 | 236 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2922 | 0 | 60 | 288.7 | 210 | 828 | 1041 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 232 | 0 | 14 | 34.8 | 40 | 140 | 280 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 562 | 0 | 60 | 495.9 | 20 | 90 | 124 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 602 | 2043 | 2265 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 41 | 0 | 30 | 69.6 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 95.7 | 622 | 1142 | 1262 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 211 | 0 | 30 | 88.7 | 27 | 101 | 151 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 219 | 960 | 90 | 37.4 | 183 | 716 | 839 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 28.6 | 6 | 10 | 25 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1248 | 0 | 14 | 222.9 | 34 | 118 | 236 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 333 | 0 | 60 | 78.0 | 69 | 330 | 458 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 324 | 0 | 45 | 90.6 | 58 | 223 | 298 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 252 | 0 | 14 | 20.9 | 67 | 248 | 501 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 126 | 0 | 14 | 26.9 | 29 | 100 | 198 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 356 | 0 | 30 | 43.9 | 87 | 339 | 509 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 354 | 290 | 30 | 25.0 | 152 | 591 | 889 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4465 | 0 | 60 | 557.4 | 208 | 697 | 809 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 230 | 480 | 14 | 17.4 | 325 | 524 | 710 | 0 | — |
| ITEM-0042 | B - Core Products | Reorder | 114 | 0 | 14 | 20.9 | 33 | 115 | 230 | 116 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 453 | 1160 | 1323 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 707 | 0 | 45 | 207.9 | 42 | 199 | 301 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 315 | 115 | 90 | 101.2 | 131 | 415 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 58 | 760 | 60 | 8.9 | 279 | 677 | 814 | 0 | 9 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.9 | 12 | 49 | 72 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 133 | 338 | 438 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 169 | 0 | 7 | 16.4 | 26 | 109 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 123 | 0 | 7 | 17.4 | 20 | 77 | 226 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4454 | 0 | 60 | 476.1 | 246 | 817 | 948 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 430 | 0 | 14 | 51.5 | 62 | 188 | 305 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1063 | 1390 | 90 | 58.0 | 692 | 2360 | 2616 | 0 | 120 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 67 | 256 | 342 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 123 | 0 | 14 | 25.8 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 94 | 0 | 30 | 55.3 | 16 | 69 | 120 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 620 | 0 | 14 | 92.4 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 890 | 260 | 60 | 73.4 | 251 | 992 | 1246 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 316 | 115 | 45 | 58.3 | 85 | 335 | 449 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 326 | 245 | 14 | 20.2 | 117 | 359 | 585 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 411 | 0 | 30 | 81.3 | 58 | 215 | 321 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 37 | 0 | 7 | 13.4 | 6 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 27 | 0 | 7 | 34.2 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 223 | 880 | 1106 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3522 | 0 | 90 | 713.9 | 152 | 601 | 705 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 34 | 61 | 14 | 16.8 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Reorder | 53 | 0 | 45 | 61.2 | 13 | 53 | 79 | 26 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 354 | 0 | 7 | 151.7 | 6 | 25 | 95 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 322 | 540 | 45 | 26.7 | 189 | 744 | 997 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 558 | 0 | 45 | 253.6 | 27 | 129 | 195 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 402 | 558 | 90 | 56.2 | 220 | 872 | 1022 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 89 | 240 | 7 | 8.1 | 26 | 115 | 346 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 957 | 0 | 14 | 87.4 | 64 | 229 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 64 | 337 | 60 | 24.3 | 56 | 217 | 272 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 27 | 0 | 14 | 22.5 | 7 | 25 | 61 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 311 | 0 | 45 | 72.7 | 52 | 249 | 378 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 50 | 50 | 30 | 33.6 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 801 | 735 | 90 | 62.5 | 391 | 1558 | 1828 | 292 | 97 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 28.2 | 281 | 445 | 874 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 96 | 0 | 7 | 18.9 | 15 | 56 | 163 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7053 | 0 | 90 | 391.1 | 686 | 2328 | 2580 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3791 | 0 | 60 | 271.4 | 359 | 1211 | 1407 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 35.7 | 98 | 146 | 272 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 147 | 0 | 7 | 22.7 | 22 | 74 | 210 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 171 | 0 | 14 | 45.0 | 24 | 81 | 161 | 0 | — |
| ITEM-0101 | A - Top Movers | Reorder | 514 | 1045 | 60 | 35.0 | 697 | 1593 | 1798 | 240 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 22 | 210 | 45 | 10.8 | 26 | 121 | 182 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 81.1 | 388 | 1163 | 1342 | 0 | — |
| ITEM-0105 | B - Core Products | Lead-time risk | 454 | 0 | 45 | 59.6 | 121 | 472 | 631 | 180 | 60 |
| ITEM-0106 | A - Top Movers | Reorder | 1104 | 1041 | 90 | 66.1 | 636 | 2156 | 2390 | 245 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 324 | 740 | 60 | 28.7 | 232 | 920 | 1157 | 0 | 72 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1066 | 1250 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 533 | 0 | 60 | 120.8 | 132 | 402 | 534 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1866 | 0 | 90 | 137.2 | 520 | 1758 | 1948 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 635 | 1161 | 60 | 36.0 | 455 | 1532 | 1779 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 270 | 1395 | 45 | 16.5 | 765 | 1519 | 1749 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 8 | 45 | 14 | 5.8 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 85 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 165 | 653 | 765 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 268 | 0 | 30 | 47.0 | 61 | 238 | 358 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 58 | 59 | 30 | 29.7 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 233 | 0 | 7 | 17.5 | 35 | 142 | 422 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 100 | 92 | 14 | 35.4 | 65 | 108 | 192 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 217 | 0 | 14 | 21.9 | 58 | 207 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 27 | 126 | 7 | 4.5 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 181.1 | 308 | 500 | 586 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 142 | 558 | 748 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 93.5 | 674 | 1786 | 2042 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 612 | 0 | 14 | 101.6 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 327 | 130 | 60 | 75.5 | 70 | 335 | 465 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 128 | 160 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3895 | 0 | 60 | 280.9 | 356 | 1202 | 1396 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 466 | 0 | 14 | 51.3 | 68 | 205 | 332 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 556 | 229 | 30 | 36.1 | 163 | 641 | 964 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1303 | 269 | 60 | 72.3 | 461 | 1561 | 1813 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2277 | 0 | 45 | 236.1 | 152 | 596 | 799 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 449 | 236 | 45 | 41.2 | 171 | 672 | 901 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 873 | 0 | 7 | 70.3 | 37 | 137 | 398 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 115 | 451 | 566 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 164 | 636 | 90 | 43.0 | 117 | 464 | 544 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 581 | 385 | 14 | 32.0 | 439 | 711 | 965 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 680 | 0 | 60 | 154.5 | 93 | 362 | 454 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 25 | 200 | 60 | 16.1 | 26 | 121 | 168 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 602 | 0 | 14 | 82.8 | 43 | 152 | 305 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 623 | 266 | 30 | 34.4 | 239 | 801 | 1055 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
