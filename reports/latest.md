# Synthetic Inventory Health

**Simulation date: 2026-08-27**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 38 |
| Lead-time risk | 64 |
| Reorder | 6 |
| Stockout | 3 |

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
| ITEM-0001 | B - Core Products | Lead-time risk | 45 | 0 | 30 | 3.7 | 132 | 514 | 773 | 728 | 4 |
| ITEM-0002 | B - Core Products | Healthy | 182 | 0 | 7 | 28.0 | 96 | 149 | 285 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Lead-time risk | 1198 | 0 | 60 | 80.8 | 379 | 1284 | 1492 | 294 | 81 |
| ITEM-0005 | B - Core Products | Excess | 2095 | 0 | 45 | 266.7 | 127 | 489 | 654 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 397 | 0 | 14 | 52.7 | 43 | 156 | 315 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 9 | 0 | 45 | 5.3 | 21 | 100 | 151 | 142 | 6 |
| ITEM-0008 | B - Core Products | Healthy | 375 | 0 | 14 | 35.2 | 68 | 228 | 452 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 84 | 0 | 60 | 32.2 | 44 | 204 | 282 | 198 | 33 |
| ITEM-0010 | B - Core Products | Lead-time risk | 183 | 0 | 90 | 44.3 | 129 | 506 | 592 | 410 | 45 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 0 | 60 | 8.1 | 927 | 2036 | 2291 | 2145 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2206 | 0 | 7 | 126.7 | 314 | 454 | 698 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 471 | 0 | 90 | 164.9 | 68 | 328 | 414 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1428 | 0 | 7 | 110.3 | 34 | 138 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 111.9 | 28 | 49 | 126 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 0 | 45 | 26.3 | 84 | 221 | 310 | 235 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 41 | 0 | 45 | 6.1 | 104 | 411 | 551 | 510 | 7 |
| ITEM-0018 | B - Core Products | Excess | 1261 | 0 | 30 | 203.8 | 69 | 261 | 391 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3385 | 0 | 60 | 321.7 | 218 | 860 | 1081 | 0 | — |
| ITEM-0020 | B - Core Products | Lead-time risk | 146 | 0 | 14 | 13.1 | 67 | 235 | 469 | 323 | 14 |
| ITEM-0021 | C - Slow Moving | Excess | 602 | 0 | 60 | 322.5 | 32 | 146 | 202 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 182 | 0 | 90 | 10.5 | 660 | 2244 | 2487 | 2305 | 11 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 16 | 0 | 30 | 20.6 | 9 | 34 | 57 | 45 | 21 |
| ITEM-0027 | B - Core Products | Reorder | 1161 | 0 | 60 | 81.0 | 702 | 1577 | 1878 | 717 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 18 | 0 | 30 | 4.8 | 33 | 149 | 261 | 243 | 5 |
| ITEM-0029 | B - Core Products | Lead-time risk | 426 | 0 | 90 | 44.0 | 300 | 1181 | 1384 | 960 | 45 |
| ITEM-0030 | C - Slow Moving | Lead-time risk | 2 | 0 | 7 | 3.0 | 8 | 14 | 34 | 35 | 3 |
| ITEM-0031 | B - Core Products | Excess | 1431 | 0 | 14 | 141.2 | 61 | 213 | 426 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 27 | 0 | 60 | 6.9 | 63 | 301 | 418 | 395 | 7 |
| ITEM-0033 | B - Core Products | Healthy | 452 | 0 | 45 | 66.5 | 112 | 425 | 568 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 565 | 0 | 14 | 50.4 | 64 | 233 | 468 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 0 | 7 | 0.0 | 126 | 188 | 349 | 350 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 281 | 0 | 14 | 34.6 | 48 | 170 | 341 | 0 | — |
| ITEM-0038 | B - Core Products | Lead-time risk | 25 | 0 | 30 | 3.1 | 87 | 339 | 509 | 484 | 4 |
| ITEM-0039 | B - Core Products | Lead-time risk | 261 | 0 | 30 | 19.7 | 143 | 554 | 833 | 575 | 20 |
| ITEM-0040 | A - Top Movers | Excess | 4752 | 0 | 60 | 328.5 | 375 | 1258 | 1460 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 829 | 0 | 14 | 52.5 | 282 | 519 | 851 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 326 | 0 | 14 | 34.6 | 59 | 201 | 398 | 0 | — |
| ITEM-0043 | B - Core Products | Lead-time risk | 87 | 0 | 90 | 11.2 | 480 | 1190 | 1354 | 1270 | 12 |
| ITEM-0044 | C - Slow Moving | Excess | 868 | 0 | 45 | 267.5 | 40 | 190 | 287 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 474 | 0 | 90 | 166.6 | 119 | 378 | 464 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 45 | 0 | 60 | 26.0 | 79 | 185 | 237 | 192 | 26 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 35 | 0 | 45 | 27.2 | 17 | 77 | 115 | 80 | 28 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 62 | 0 | 60 | 32.3 | 111 | 229 | 286 | 224 | 33 |
| ITEM-0052 | B - Core Products | Healthy | 425 | 0 | 7 | 41.7 | 28 | 110 | 324 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 307 | 0 | 7 | 41.3 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4781 | 0 | 60 | 321.4 | 389 | 1297 | 1505 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 740 | 0 | 14 | 53.8 | 109 | 316 | 508 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1909 | 0 | 90 | 109.7 | 660 | 2244 | 2487 | 580 | 110 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Lead-time risk | 52 | 0 | 30 | 5.1 | 323 | 640 | 854 | 802 | 6 |
| ITEM-0060 | B - Core Products | Lead-time risk | 46 | 0 | 45 | 6.3 | 120 | 457 | 610 | 564 | 7 |
| ITEM-0061 | B - Core Products | Lead-time risk | 65 | 0 | 14 | 13.2 | 29 | 103 | 207 | 145 | 14 |
| ITEM-0062 | C - Slow Moving | Healthy | 156 | 0 | 30 | 52.4 | 26 | 119 | 208 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 918 | 0 | 14 | 139.3 | 37 | 136 | 275 | 0 | — |
| ITEM-0064 | B - Core Products | Lead-time risk | 595 | 0 | 60 | 77.9 | 279 | 745 | 905 | 310 | 78 |
| ITEM-0065 | B - Core Products | Healthy | 1463 | 0 | 60 | 122.1 | 248 | 979 | 1231 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 568 | 0 | 45 | 98.9 | 90 | 355 | 475 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 865 | 0 | 14 | 52.0 | 121 | 371 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 182 | 0 | 30 | 20.2 | 99 | 379 | 568 | 390 | 21 |
| ITEM-0069 | C - Slow Moving | Healthy | 76 | 0 | 7 | 27.3 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 212 | 0 | 45 | 98.9 | 70 | 169 | 233 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 36 | 0 | 7 | 41.5 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 80 | 0 | 60 | 7.2 | 233 | 915 | 1150 | 1070 | 8 |
| ITEM-0073 | B - Core Products | Excess | 3684 | 0 | 90 | 440.3 | 259 | 1021 | 1197 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 7 | 0 | 14 | 3.3 | 10 | 42 | 106 | 99 | 4 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 4 | 0 | 45 | 5.2 | 11 | 47 | 70 | 66 | 6 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 0 | 90 | 44.3 | 238 | 511 | 574 | 441 | 45 |
| ITEM-0077 | C - Slow Moving | Excess | 432 | 0 | 7 | 114.0 | 10 | 41 | 154 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 0 | 90 | 90.0 | 104 | 288 | 348 | 170 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 820 | 0 | 45 | 65.4 | 196 | 774 | 1037 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 651 | 0 | 45 | 260.4 | 31 | 146 | 221 | 0 | — |
| ITEM-0081 | B - Core Products | Lead-time risk | 738 | 0 | 90 | 108.2 | 208 | 829 | 973 | 235 | 109 |
| ITEM-0082 | B - Core Products | Lead-time risk | 22 | 0 | 7 | 2.1 | 28 | 111 | 326 | 305 | 3 |
| ITEM-0083 | B - Core Products | Excess | 1474 | 0 | 14 | 140.8 | 61 | 218 | 438 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 155 | 0 | 60 | 32.5 | 101 | 392 | 492 | 337 | 33 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 0 | 14 | 3.5 | 218 | 331 | 488 | 465 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 69 | 0 | 14 | 35.3 | 10 | 40 | 98 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 27 | 0 | 45 | 5.7 | 74 | 292 | 392 | 365 | 6 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 0 | 14 | 3.5 | 379 | 588 | 784 | 735 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 115 | 0 | 30 | 73.9 | 14 | 63 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1386 | 0 | 90 | 108.7 | 393 | 1554 | 1822 | 436 | 109 |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 28.0 | 246 | 388 | 759 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 20 | 0 | 7 | 2.3 | 29 | 99 | 282 | 262 | 3 |
| ITEM-0095 | A - Top Movers | Excess | 7881 | 0 | 90 | 441.4 | 680 | 2305 | 2555 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4454 | 0 | 60 | 319.9 | 359 | 1209 | 1404 | 0 | — |
| ITEM-0097 | B - Core Products | Reorder | 82 | 0 | 7 | 11.2 | 110 | 169 | 323 | 245 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 24 | 0 | 7 | 2.2 | 34 | 122 | 351 | 330 | 3 |
| ITEM-0100 | B - Core Products | Lead-time risk | 19 | 0 | 14 | 2.9 | 39 | 138 | 275 | 256 | 3 |
| ITEM-0101 | B - Core Products | Reorder | 1257 | 0 | 60 | 92.6 | 563 | 1392 | 1677 | 420 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 90 | 0 | 45 | 26.6 | 42 | 198 | 300 | 210 | 27 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Lead-time risk | 1024 | 0 | 90 | 111.0 | 413 | 1253 | 1446 | 422 | 112 |
| ITEM-0105 | B - Core Products | Healthy | 788 | 0 | 45 | 97.7 | 125 | 497 | 666 | 0 | — |
| ITEM-0106 | A - Top Movers | Lead-time risk | 1900 | 0 | 90 | 112.2 | 646 | 2187 | 2424 | 524 | 113 |
| ITEM-0107 | B - Core Products | Reorder | 856 | 0 | 60 | 80.2 | 222 | 873 | 1097 | 241 | — |
| ITEM-0108 | C - Slow Moving | Excess | 646 | 0 | 30 | 205.4 | 68 | 166 | 260 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 383 | 0 | 90 | 42.1 | 277 | 1105 | 1295 | 915 | 43 |
| ITEM-0110 | C - Slow Moving | Excess | 756 | 0 | 60 | 324.0 | 96 | 239 | 309 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2468 | 0 | 90 | 167.8 | 558 | 1897 | 2103 | 0 | — |
| ITEM-0112 | A - Top Movers | Lead-time risk | 1468 | 0 | 60 | 80.9 | 466 | 1574 | 1828 | 360 | 81 |
| ITEM-0113 | A - Top Movers | Reorder | 1095 | 0 | 45 | 70.8 | 801 | 1512 | 1729 | 635 | — |
| ITEM-0114 | C - Slow Moving | Lead-time risk | 19 | 0 | 14 | 13.0 | 8 | 30 | 74 | 55 | 13 |
| ITEM-0115 | B - Core Products | Healthy | 1023 | 0 | 14 | 54.1 | 315 | 599 | 996 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 9 | 0 | 45 | 6.6 | 18 | 81 | 122 | 115 | 7 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 237 | 0 | 90 | 44.2 | 165 | 654 | 767 | 530 | 45 |
| ITEM-0119 | B - Core Products | Lead-time risk | 30 | 0 | 30 | 4.9 | 65 | 256 | 384 | 355 | 5 |
| ITEM-0120 | C - Slow Moving | Healthy | 95 | 0 | 30 | 50.9 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 525 | 0 | 7 | 40.8 | 37 | 140 | 410 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 113 | 0 | 45 | 36.2 | 188 | 332 | 398 | 285 | 37 |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 0 | 14 | 4.1 | 102 | 157 | 233 | 218 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 138 | 0 | 14 | 13.4 | 59 | 214 | 430 | 292 | 14 |
| ITEM-0125 | B - Core Products | Healthy | 173 | 0 | 7 | 27.9 | 17 | 67 | 198 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 295 | 0 | 30 | 23.0 | 505 | 904 | 1083 | 790 | 23 |
| ITEM-0128 | B - Core Products | Lead-time risk | 47 | 0 | 45 | 5.2 | 141 | 556 | 745 | 698 | 6 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1828 | 0 | 90 | 166.5 | 638 | 1637 | 1868 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 882 | 0 | 14 | 139.0 | 35 | 131 | 264 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 522 | 0 | 60 | 122.3 | 69 | 330 | 458 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 10 | 0 | 90 | 10.3 | 24 | 112 | 141 | 135 | 11 |
| ITEM-0135 | A - Top Movers | Excess | 4497 | 0 | 60 | 320.5 | 359 | 1216 | 1412 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 0 | 45 | 6.6 | 27 | 77 | 109 | 102 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 782 | 0 | 14 | 52.8 | 110 | 333 | 540 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 303 | 0 | 30 | 20.5 | 196 | 656 | 863 | 560 | 21 |
| ITEM-0140 | A - Top Movers | Healthy | 2112 | 0 | 60 | 116.7 | 463 | 1568 | 1821 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2690 | 0 | 45 | 262.6 | 160 | 632 | 847 | 0 | — |
| ITEM-0142 | A - Top Movers | Stockout | 0 | 0 | 60 | 0.0 | 621 | 1219 | 1356 | 1360 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 694 | 0 | 45 | 64.0 | 170 | 669 | 897 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1425 | 0 | 7 | 112.3 | 38 | 140 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 67 | 0 | 60 | 7.2 | 196 | 761 | 955 | 888 | 8 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 292 | 0 | 90 | 44.9 | 200 | 792 | 928 | 636 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 0 | 14 | 0.0 | 431 | 721 | 991 | 995 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Reorder | 650 | 0 | 60 | 80.9 | 169 | 660 | 828 | 178 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Lead-time risk | 930 | 0 | 90 | 118.2 | 447 | 1163 | 1329 | 400 | 119 |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 83 | 0 | 60 | 31.9 | 43 | 202 | 280 | 200 | 32 |
| ITEM-0155 | B - Core Products | Excess | 958 | 0 | 14 | 139.3 | 40 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 339 | 0 | 30 | 19.6 | 231 | 768 | 1010 | 671 | 20 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 847 | 0 | 7 | 42.0 | 278 | 440 | 722 | 0 | — |
