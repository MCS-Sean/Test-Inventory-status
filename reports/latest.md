# Synthetic Inventory Health

**Simulation date: 2026-09-10**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 65 |
| Lead-time risk | 19 |
| Reorder | 1 |
| Stockout | 25 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 506 | 760 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 293 | 0 | 7 | 47.9 | 89 | 138 | 267 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 996 | 517 | 60 | 66.2 | 385 | 1304 | 1515 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2036 | 0 | 45 | 295.5 | 111 | 428 | 573 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 296 | 0 | 14 | 39.2 | 43 | 157 | 315 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 293 | 0 | 14 | 31.5 | 59 | 199 | 394 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 64 | 198 | 60 | 28.8 | 37 | 173 | 240 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 154 | 410 | 90 | 45.4 | 106 | 415 | 486 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 435 | 0 | 90 | 153.5 | 68 | 326 | 411 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1242 | 0 | 7 | 98.0 | 33 | 135 | 401 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 78 | 235 | 45 | 30.3 | 77 | 196 | 273 | 0 | — |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 106 | 419 | 561 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1224 | 0 | 30 | 228.5 | 61 | 228 | 340 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3234 | 0 | 60 | 312.0 | 214 | 847 | 1065 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 384 | 0 | 14 | 39.0 | 59 | 207 | 414 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 590 | 0 | 60 | 384.8 | 26 | 120 | 166 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 642 | 2182 | 2419 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 18.9 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1046 | 717 | 60 | 84.4 | 803 | 1559 | 1733 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 132 | 231 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 347 | 960 | 90 | 41.3 | 261 | 1027 | 1204 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 24 | 0 | 7 | 47.0 | 7 | 12 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1361 | 0 | 14 | 160.3 | 50 | 178 | 356 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 309 | 428 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 413 | 0 | 45 | 74.5 | 91 | 347 | 463 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 272.0 | 82 | 238 | 315 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 411 | 0 | 14 | 37.9 | 62 | 225 | 452 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 221 | 0 | 14 | 31.1 | 42 | 149 | 298 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 333 | 500 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 32 | 575 | 30 | 2.3 | 148 | 573 | 860 | 0 | 3 |
| ITEM-0040 | A - Top Movers | Excess | 4654 | 0 | 60 | 368.1 | 332 | 1104 | 1281 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 41.4 | 276 | 498 | 807 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 262 | 0 | 14 | 32.3 | 52 | 174 | 345 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 562 | 1496 | 1711 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 813 | 0 | 45 | 236.0 | 42 | 201 | 304 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 192 | 60 | 0.0 | 85 | 211 | 273 | 81 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 352 | 175 | 60 | 74.2 | 175 | 465 | 607 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 28 | 80 | 45 | 25.0 | 16 | 68 | 102 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 290 | 60 | 0.0 | 132 | 297 | 378 | 88 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 286 | 0 | 7 | 28.5 | 27 | 108 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 205 | 0 | 7 | 28.1 | 20 | 79 | 232 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4666 | 0 | 60 | 351.1 | 351 | 1162 | 1348 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 627 | 0 | 14 | 51.2 | 97 | 281 | 453 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1649 | 580 | 90 | 93.8 | 666 | 2266 | 2512 | 285 | 94 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 100 | 378 | 505 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 29 | 102 | 204 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 133 | 0 | 30 | 52.0 | 23 | 103 | 179 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 821 | 0 | 14 | 121.3 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1282 | 0 | 60 | 106.1 | 249 | 986 | 1240 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 481 | 0 | 45 | 81.5 | 92 | 364 | 488 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 589 | 0 | 14 | 35.0 | 121 | 374 | 609 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 135 | 390 | 30 | 17.8 | 85 | 320 | 480 | 0 | — |
| ITEM-0069 | C - Slow Moving | Reorder | 29 | 0 | 7 | 10.1 | 7 | 31 | 117 | 90 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 26 | 0 | 7 | 30.8 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 239 | 945 | 1188 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3629 | 0 | 90 | 500.9 | 225 | 885 | 1037 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 96 | 0 | 14 | 45.0 | 10 | 42 | 106 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 76 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 405 | 0 | 7 | 126.6 | 8 | 34 | 130 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 169 | 170 | 90 | 80.5 | 105 | 297 | 360 | 0 | 81 |
| ITEM-0079 | B - Core Products | Healthy | 656 | 275 | 45 | 51.4 | 200 | 787 | 1055 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 621 | 0 | 45 | 252.9 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 633 | 235 | 90 | 90.4 | 214 | 851 | 998 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 229 | 0 | 7 | 20.8 | 29 | 117 | 348 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1318 | 0 | 14 | 125.5 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 126 | 337 | 60 | 32.1 | 83 | 323 | 405 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 55 | 0 | 14 | 32.6 | 9 | 35 | 85 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 93 | 0 | 30 | 59.8 | 14 | 63 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1207 | 436 | 90 | 90.7 | 408 | 1620 | 1899 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.5 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 221 | 0 | 7 | 30.4 | 22 | 81 | 234 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7617 | 0 | 90 | 423.7 | 683 | 2319 | 2571 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4296 | 0 | 60 | 326.0 | 340 | 1144 | 1329 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 289 | 0 | 7 | 31.0 | 31 | 106 | 302 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 35 | 118 | 235 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 94.8 | 507 | 1206 | 1447 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 67 | 210 | 45 | 22.9 | 37 | 172 | 260 | 0 | 23 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 112.0 | 395 | 1173 | 1352 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 683 | 0 | 45 | 85.7 | 125 | 492 | 659 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1606 | 773 | 90 | 94.0 | 651 | 2207 | 2446 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 675 | 241 | 60 | 61.0 | 228 | 904 | 1136 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 593 | 0 | 30 | 216.1 | 61 | 147 | 229 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 249 | 915 | 90 | 27.4 | 277 | 1105 | 1295 | 0 | 28 |
| ITEM-0110 | C - Slow Moving | Excess | 711 | 0 | 60 | 258.0 | 103 | 272 | 354 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2262 | 0 | 90 | 148.5 | 577 | 1964 | 2177 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1202 | 360 | 60 | 67.8 | 456 | 1538 | 1786 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 50 | 0 | 14 | 34.9 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 59.3 | 298 | 552 | 908 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 160 | 530 | 90 | 29.5 | 166 | 660 | 774 | 0 | 30 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 255 | 384 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 70 | 55 | 30 | 38.2 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 323 | 0 | 7 | 23.8 | 36 | 145 | 431 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 233 | 0 | 14 | 80.0 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 9 | 292 | 14 | 0.9 | 59 | 215 | 432 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 96 | 0 | 7 | 15.7 | 17 | 67 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 551 | 739 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 803 | 0 | 14 | 129.3 | 35 | 129 | 259 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 461 | 0 | 60 | 106.7 | 70 | 334 | 464 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 109 | 137 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4327 | 0 | 60 | 316.9 | 350 | 1183 | 1375 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 0.9 | 27 | 77 | 109 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 696 | 0 | 14 | 56.9 | 92 | 276 | 447 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 81 | 787 | 30 | 5.4 | 198 | 662 | 871 | 0 | 6 |
| ITEM-0140 | A - Top Movers | Healthy | 1846 | 0 | 60 | 101.1 | 467 | 1582 | 1837 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2585 | 0 | 45 | 265.9 | 153 | 601 | 805 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 585 | 1380 | 1653 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 533 | 243 | 45 | 49.5 | 168 | 664 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1264 | 0 | 7 | 99.4 | 37 | 139 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 165 | 641 | 805 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 248 | 636 | 90 | 43.3 | 177 | 698 | 818 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 417 | 705 | 974 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 119.2 | 254 | 445 | 713 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 602 | 178 | 60 | 90.6 | 141 | 547 | 686 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 63 | 200 | 60 | 28.1 | 37 | 174 | 242 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 852 | 0 | 14 | 123.5 | 41 | 145 | 290 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 35 | 930 | 30 | 1.9 | 242 | 807 | 1062 | 0 | 2 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 383 | 418 | 7 | 16.9 | 304 | 485 | 802 | 0 | — |
