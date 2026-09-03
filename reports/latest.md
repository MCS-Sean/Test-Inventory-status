# Synthetic Inventory Health

**Simulation date: 2026-09-03**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 60 |
| Lead-time risk | 35 |
| Stockout | 16 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 505 | 759 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1108 | 294 | 60 | 75.1 | 377 | 1278 | 1484 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2067 | 0 | 45 | 286.2 | 117 | 450 | 601 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 347 | 0 | 14 | 45.7 | 44 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 1 | 142 | 45 | 0.6 | 21 | 98 | 147 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 337 | 0 | 14 | 34.0 | 62 | 211 | 419 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 75 | 198 | 60 | 31.5 | 40 | 186 | 257 | 0 | 32 |
| ITEM-0010 | B - Core Products | Lead-time risk | 164 | 410 | 90 | 43.4 | 117 | 461 | 541 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2128 | 0 | 7 | 127.9 | 306 | 440 | 673 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 457 | 0 | 90 | 165.2 | 66 | 318 | 401 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1342 | 0 | 7 | 104.8 | 34 | 137 | 406 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 105 | 417 | 559 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1240 | 0 | 30 | 214.2 | 65 | 245 | 367 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3312 | 0 | 60 | 325.8 | 210 | 831 | 1044 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 104 | 323 | 14 | 9.9 | 63 | 220 | 440 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 595 | 0 | 60 | 352.3 | 29 | 133 | 183 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 67 | 2305 | 90 | 3.9 | 658 | 2237 | 2480 | 0 | 4 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.7 | 8 | 31 | 53 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 104.5 | 622 | 1300 | 1534 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 1 | 243 | 30 | 0.3 | 31 | 140 | 244 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 379 | 960 | 90 | 41.8 | 281 | 1108 | 1298 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 37 | 0 | 7 | 74.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1401 | 0 | 14 | 150.5 | 56 | 196 | 392 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 64 | 305 | 423 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 436 | 0 | 45 | 68.8 | 105 | 397 | 530 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 478 | 0 | 14 | 42.7 | 64 | 232 | 467 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 350 | 0 | 7 | 45.5 | 126 | 188 | 349 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 246 | 0 | 14 | 32.4 | 44 | 158 | 318 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 84 | 329 | 494 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 125 | 575 | 30 | 9.0 | 149 | 579 | 869 | 0 | 10 |
| ITEM-0040 | A - Top Movers | Excess | 4711 | 0 | 60 | 346.7 | 354 | 1183 | 1374 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 611 | 0 | 14 | 37.4 | 353 | 599 | 828 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 294 | 0 | 14 | 34.2 | 54 | 183 | 364 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 839 | 0 | 45 | 246.0 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 154.9 | 122 | 380 | 465 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 405 | 175 | 60 | 91.4 | 173 | 444 | 577 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 482 | 0 | 14 | 45.9 | 185 | 343 | 564 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 31 | 80 | 45 | 25.4 | 17 | 74 | 110 | 0 | 26 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 358 | 0 | 7 | 35.1 | 28 | 110 | 325 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 241 | 0 | 7 | 32.2 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4721 | 0 | 60 | 333.0 | 372 | 1237 | 1436 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 682 | 0 | 14 | 53.7 | 99 | 290 | 468 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1792 | 580 | 90 | 103.5 | 657 | 2234 | 2476 | 0 | 104 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 435 | 897 | 1209 | 407 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 17 | 564 | 45 | 2.5 | 111 | 419 | 560 | 0 | 3 |
| ITEM-0061 | B - Core Products | Lead-time risk | 28 | 145 | 14 | 5.7 | 29 | 103 | 205 | 0 | 6 |
| ITEM-0062 | C - Slow Moving | Healthy | 147 | 0 | 30 | 52.1 | 25 | 113 | 198 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 866 | 0 | 14 | 128.4 | 38 | 140 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 84.5 | 270 | 700 | 848 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1390 | 0 | 60 | 118.5 | 243 | 959 | 1206 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 532 | 0 | 45 | 93.3 | 89 | 352 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 726 | 0 | 14 | 43.5 | 122 | 373 | 607 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 159 | 390 | 30 | 19.4 | 91 | 346 | 518 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 53 | 0 | 7 | 18.3 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 30 | 0 | 7 | 34.2 | 3 | 11 | 37 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 1 | 1070 | 60 | 0.1 | 237 | 934 | 1173 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3659 | 0 | 90 | 482.2 | 235 | 926 | 1085 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 107 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 11 | 47 | 71 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 415 | 0 | 7 | 116.4 | 9 | 38 | 145 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 745 | 275 | 45 | 59.4 | 196 | 773 | 1036 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 637 | 0 | 45 | 259.4 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 704 | 235 | 90 | 106.1 | 203 | 807 | 946 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 114 | 340 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1397 | 0 | 14 | 134.2 | 61 | 218 | 436 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 141 | 337 | 60 | 32.5 | 93 | 359 | 450 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 224 | 348 | 520 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 61 | 0 | 14 | 33.7 | 9 | 37 | 91 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 3 | 365 | 45 | 0.7 | 71 | 278 | 373 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 103 | 0 | 30 | 64.8 | 14 | 64 | 111 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1301 | 436 | 90 | 100.5 | 398 | 1576 | 1848 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 31.3 | 241 | 368 | 700 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 255 | 0 | 7 | 32.1 | 27 | 91 | 258 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7732 | 0 | 90 | 428.8 | 685 | 2327 | 2579 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4385 | 0 | 60 | 328.6 | 345 | 1160 | 1346 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 315 | 0 | 7 | 31.1 | 32 | 113 | 326 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 37 | 129 | 256 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1129 | 420 | 60 | 77.8 | 579 | 1465 | 1769 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 76 | 210 | 45 | 24.3 | 39 | 184 | 278 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 741 | 0 | 45 | 92.2 | 125 | 495 | 664 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1766 | 524 | 90 | 103.9 | 649 | 2196 | 2434 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 764 | 241 | 60 | 70.2 | 226 | 890 | 1118 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 226.3 | 61 | 144 | 223 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 303 | 915 | 90 | 32.6 | 284 | 1130 | 1325 | 0 | 33 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 315.2 | 96 | 241 | 312 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2375 | 0 | 90 | 159.8 | 563 | 1916 | 2124 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1352 | 360 | 60 | 77.4 | 449 | 1515 | 1759 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 623 | 1395 | 45 | 33.1 | 886 | 1751 | 2014 | 0 | 34 |
| ITEM-0114 | C - Slow Moving | Healthy | 7 | 55 | 14 | 4.7 | 8 | 31 | 75 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1007 | 0 | 14 | 59.6 | 298 | 552 | 906 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 197 | 530 | 90 | 36.3 | 166 | 660 | 774 | 0 | 37 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 254 | 382 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 83 | 0 | 30 | 44.7 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 435 | 0 | 7 | 33.1 | 36 | 142 | 417 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Lead-time risk | 62 | 292 | 14 | 5.9 | 60 | 217 | 436 | 0 | 6 |
| ITEM-0125 | B - Core Products | Healthy | 135 | 0 | 7 | 21.7 | 17 | 67 | 198 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 548 | 734 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 848 | 0 | 14 | 135.6 | 35 | 129 | 261 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 493 | 0 | 60 | 117.1 | 68 | 325 | 452 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 7 | 135 | 90 | 7.6 | 23 | 107 | 135 | 0 | 8 |
| ITEM-0135 | A - Top Movers | Excess | 4424 | 0 | 60 | 324.8 | 350 | 1181 | 1372 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 735 | 0 | 14 | 53.0 | 105 | 313 | 507 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 191 | 560 | 30 | 13.0 | 194 | 650 | 856 | 0 | 13 |
| ITEM-0140 | A - Top Movers | Healthy | 1991 | 0 | 60 | 110.4 | 461 | 1562 | 1814 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2649 | 0 | 45 | 267.0 | 156 | 613 | 821 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 584 | 1375 | 1647 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 615 | 243 | 45 | 56.6 | 169 | 669 | 898 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1351 | 0 | 7 | 106.2 | 37 | 139 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 26 | 888 | 60 | 3.1 | 178 | 693 | 870 | 0 | 4 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 269 | 636 | 90 | 43.9 | 189 | 748 | 876 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 422 | 705 | 968 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 631 | 178 | 60 | 85.9 | 156 | 605 | 759 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 73 | 200 | 60 | 29.9 | 41 | 191 | 264 | 0 | 30 |
| ITEM-0155 | B - Core Products | Excess | 901 | 0 | 14 | 128.7 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 211 | 671 | 30 | 12.0 | 234 | 779 | 1024 | 0 | 13 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
