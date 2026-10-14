# Synthetic Inventory Health

**Simulation date: 2026-10-14**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 85 |
| Lead-time risk | 7 |
| Reorder | 6 |
| Stockout | 11 |

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
| ITEM-0001 | B - Core Products | Reorder | 521 | 0 | 30 | 40.2 | 137 | 539 | 812 | 291 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 36.2 | 91 | 143 | 277 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 450 | 968 | 60 | 28.8 | 401 | 1354 | 1572 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1915 | 0 | 45 | 388.2 | 80 | 307 | 411 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 221 | 0 | 14 | 29.7 | 43 | 155 | 311 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 131 | 0 | 45 | 83.0 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 120 | 145 | 14 | 18.0 | 40 | 140 | 280 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 25 | 198 | 60 | 17.4 | 25 | 113 | 156 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 101 | 410 | 90 | 46.1 | 68 | 268 | 314 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 342 | 0 | 90 | 115.7 | 70 | 339 | 428 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 805 | 0 | 7 | 63.4 | 32 | 134 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 211 | 0 | 7 | 163.7 | 21 | 32 | 70 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 97.9 | 74 | 185 | 257 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 444 | 0 | 45 | 67.2 | 104 | 409 | 547 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1137 | 0 | 30 | 314.9 | 42 | 154 | 230 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2900 | 0 | 60 | 286.8 | 210 | 827 | 1040 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 223 | 0 | 14 | 33.6 | 40 | 140 | 279 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 561 | 0 | 60 | 510.0 | 20 | 88 | 121 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 598 | 2030 | 2250 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 40 | 0 | 30 | 67.9 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 732 | 915 | 60 | 77.4 | 643 | 1220 | 1353 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 207 | 0 | 30 | 89.1 | 26 | 98 | 147 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 209 | 960 | 90 | 36.2 | 180 | 705 | 826 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1245 | 0 | 14 | 226.8 | 34 | 117 | 232 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 325 | 135 | 60 | 75.6 | 69 | 332 | 461 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 319 | 0 | 45 | 89.7 | 57 | 221 | 296 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Reorder | 232 | 0 | 14 | 19.5 | 67 | 246 | 496 | 265 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 119 | 0 | 14 | 26.2 | 28 | 97 | 192 | 0 | — |
| ITEM-0038 | B - Core Products | Reorder | 338 | 0 | 30 | 41.6 | 87 | 340 | 510 | 172 | — |
| ITEM-0039 | B - Core Products | Healthy | 332 | 290 | 30 | 23.5 | 152 | 591 | 889 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4445 | 0 | 60 | 555.6 | 207 | 695 | 807 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 230 | 480 | 14 | 19.6 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 107 | 116 | 14 | 20.4 | 31 | 110 | 221 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 453 | 1160 | 1323 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 701 | 0 | 45 | 207.5 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 315 | 115 | 90 | 101.2 | 131 | 415 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 42 | 760 | 60 | 6.3 | 281 | 690 | 831 | 0 | 7 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 86 | 0 | 45 | 112.2 | 11 | 47 | 70 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 224 | 154 | 60 | 67.0 | 133 | 338 | 438 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 153 | 0 | 7 | 15.0 | 25 | 107 | 321 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 106 | 0 | 7 | 15.0 | 20 | 77 | 226 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4444 | 0 | 60 | 491.4 | 238 | 790 | 917 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 414 | 0 | 14 | 50.1 | 62 | 186 | 302 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1023 | 1390 | 90 | 55.8 | 693 | 2362 | 2618 | 0 | 118 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 78.2 | 471 | 923 | 1230 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 66 | 250 | 334 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 114 | 0 | 14 | 23.8 | 27 | 99 | 200 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 93 | 0 | 30 | 57.3 | 15 | 66 | 114 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 607 | 0 | 14 | 90.4 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 858 | 260 | 60 | 71.3 | 249 | 984 | 1236 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 305 | 115 | 45 | 56.6 | 85 | 333 | 447 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 296 | 245 | 14 | 18.5 | 117 | 357 | 581 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 403 | 0 | 30 | 80.1 | 58 | 215 | 320 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 33 | 0 | 7 | 12.0 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 26 | 0 | 7 | 33.0 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 227 | 896 | 1127 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3513 | 0 | 90 | 728.5 | 148 | 587 | 689 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 31 | 61 | 14 | 15.3 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 51 | 26 | 45 | 58.1 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 35 | 441 | 90 | 11.7 | 246 | 519 | 582 | 106 | 12 |
| ITEM-0077 | C - Slow Moving | Excess | 351 | 0 | 7 | 153.3 | 6 | 25 | 93 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 312 | 540 | 45 | 26.0 | 189 | 741 | 993 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 551 | 0 | 45 | 247.9 | 27 | 130 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 390 | 558 | 90 | 54.8 | 218 | 866 | 1015 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 71 | 240 | 7 | 6.4 | 26 | 115 | 347 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 932 | 0 | 14 | 84.5 | 64 | 230 | 462 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 58 | 337 | 60 | 22.4 | 55 | 213 | 268 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 26 | 0 | 14 | 22.5 | 7 | 25 | 59 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 301 | 0 | 45 | 70.2 | 53 | 251 | 379 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 46 | 50 | 30 | 30.4 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 774 | 1027 | 90 | 60.2 | 392 | 1562 | 1832 | 0 | 95 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 28.2 | 281 | 445 | 874 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 81 | 0 | 7 | 15.9 | 15 | 56 | 163 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7016 | 0 | 90 | 392.2 | 680 | 2308 | 2559 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3764 | 0 | 60 | 271.2 | 357 | 1204 | 1398 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 35.7 | 98 | 146 | 272 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 137 | 0 | 7 | 22.0 | 20 | 70 | 201 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 165 | 0 | 14 | 44.2 | 23 | 79 | 158 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 434 | 1285 | 60 | 28.3 | 707 | 1641 | 1856 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 230 | 0 | 45 | 114.4 | 26 | 119 | 179 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 80.6 | 388 | 1165 | 1344 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 447 | 180 | 45 | 60.0 | 118 | 461 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1076 | 1286 | 90 | 64.4 | 636 | 2157 | 2391 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 312 | 740 | 60 | 27.9 | 230 | 912 | 1147 | 0 | 71 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 271 | 1079 | 1266 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1828 | 0 | 90 | 135.6 | 515 | 1742 | 1931 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 605 | 1161 | 60 | 34.7 | 449 | 1512 | 1756 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 270 | 1395 | 45 | 16.5 | 765 | 1519 | 1749 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 51 | 0 | 14 | 37.3 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 165 | 651 | 763 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 255 | 0 | 30 | 44.4 | 62 | 241 | 361 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 56 | 59 | 30 | 28.8 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 212 | 0 | 7 | 15.8 | 35 | 143 | 425 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 100 | 92 | 14 | 35.4 | 65 | 108 | 192 | 0 | — |
| ITEM-0124 | B - Core Products | Reorder | 200 | 0 | 14 | 20.1 | 58 | 207 | 416 | 216 | — |
| ITEM-0125 | B - Core Products | Healthy | 17 | 126 | 7 | 2.9 | 15 | 63 | 187 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 214.3 | 290 | 452 | 525 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 684 | 0 | 45 | 75.3 | 142 | 560 | 751 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 600 | 0 | 14 | 99.4 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 323 | 130 | 60 | 76.5 | 68 | 326 | 453 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 130 | 163 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3875 | 0 | 60 | 283.3 | 352 | 1187 | 1378 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 455 | 0 | 14 | 51.0 | 66 | 200 | 325 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 536 | 229 | 30 | 35.1 | 162 | 635 | 956 | 0 | — |
| ITEM-0140 | A - Top Movers | Reorder | 1272 | 269 | 60 | 70.6 | 460 | 1559 | 1811 | 270 | — |
| ITEM-0141 | B - Core Products | Excess | 2258 | 0 | 45 | 234.4 | 152 | 596 | 798 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 605 | 1433 | 1718 | 0 | 1 |
| ITEM-0143 | B - Core Products | Reorder | 425 | 236 | 45 | 39.3 | 170 | 668 | 895 | 234 | — |
| ITEM-0144 | B - Core Products | Excess | 847 | 0 | 7 | 68.5 | 37 | 136 | 396 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 111 | 433 | 544 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 157 | 636 | 90 | 42.1 | 115 | 455 | 534 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Healthy | 581 | 385 | 14 | 32.0 | 439 | 711 | 965 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 680 | 0 | 60 | 157.7 | 92 | 355 | 446 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 23 | 200 | 60 | 14.9 | 26 | 121 | 167 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 584 | 0 | 14 | 79.9 | 43 | 153 | 307 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 584 | 266 | 30 | 31.9 | 240 | 808 | 1064 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 23.0 | 301 | 486 | 810 | 0 | — |
