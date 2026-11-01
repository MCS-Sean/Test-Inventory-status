# Synthetic Inventory Health

**Simulation date: 2026-11-01**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 94 |
| Lead-time risk | 2 |
| Reorder | 4 |
| Stockout | 9 |

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
| ITEM-0001 | B - Core Products | Healthy | 285 | 291 | 30 | 21.8 | 138 | 543 | 817 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 286 | 0 | 7 | 43.9 | 92 | 145 | 281 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 445 | 890 | 60 | 28.9 | 395 | 1336 | 1552 | 217 | — |
| ITEM-0005 | B - Core Products | Excess | 1855 | 0 | 45 | 463.8 | 64 | 248 | 332 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 96 | 155 | 14 | 13.5 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 106 | 0 | 45 | 70.1 | 19 | 89 | 134 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 165 | 0 | 14 | 29.0 | 33 | 119 | 238 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 198 | 0 | 60 | 156.3 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 69 | 410 | 90 | 37.6 | 57 | 224 | 263 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 296 | 90 | 90 | 104.9 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 547 | 0 | 7 | 41.9 | 34 | 139 | 413 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 75.3 | 24 | 40 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 324 | 155 | 45 | 48.3 | 105 | 414 | 555 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1089 | 0 | 30 | 369.8 | 33 | 125 | 187 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2706 | 0 | 60 | 255.6 | 218 | 864 | 1087 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 128 | 0 | 14 | 22.4 | 33 | 119 | 239 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 548 | 0 | 60 | 587.1 | 17 | 74 | 102 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 596 | 2018 | 2237 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 27 | 0 | 30 | 46.7 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 411 | 1169 | 60 | 39.3 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 177 | 0 | 30 | 86.6 | 18 | 82 | 143 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1079 | 0 | 90 | 218.7 | 150 | 599 | 703 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 38.1 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1159 | 0 | 14 | 246.6 | 28 | 99 | 198 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 241 | 135 | 60 | 55.3 | 70 | 336 | 467 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 271 | 0 | 45 | 89.3 | 49 | 189 | 253 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 677 | 0 | 60 | 662.3 | 49 | 112 | 143 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 304 | 0 | 14 | 25.9 | 67 | 243 | 490 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 33.5 | 116 | 175 | 329 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 49 | 95 | 14 | 12.5 | 23 | 82 | 164 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 197 | 172 | 30 | 23.9 | 88 | 344 | 517 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 349 | 315 | 30 | 23.8 | 156 | 612 | 920 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4318 | 0 | 60 | 610.1 | 182 | 614 | 713 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 51.0 | 251 | 430 | 681 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 156 | 0 | 14 | 33.6 | 27 | 97 | 195 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 647 | 0 | 45 | 194.1 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 280 | 220 | 90 | 87.2 | 131 | 424 | 520 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 315 | 844 | 1026 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 70 | 0 | 45 | 96.9 | 11 | 45 | 66 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 203 | 0 | 7 | 20.0 | 23 | 105 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 124 | 0 | 7 | 16.7 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4301 | 0 | 60 | 565.1 | 196 | 661 | 767 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 305 | 0 | 14 | 43.6 | 51 | 156 | 254 | 0 | — |
| ITEM-0056 | A - Top Movers | Reorder | 693 | 1680 | 90 | 37.5 | 698 | 2381 | 2640 | 270 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 497 | 0 | 45 | 136.8 | 58 | 226 | 302 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 9 | 110 | 14 | 1.8 | 28 | 103 | 207 | 0 | 2 |
| ITEM-0062 | C - Slow Moving | Healthy | 67 | 0 | 30 | 47.1 | 13 | 58 | 100 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 505 | 0 | 14 | 78.0 | 37 | 135 | 271 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 281 | 470 | 60 | 45.2 | 241 | 620 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 654 | 525 | 60 | 54.7 | 247 | 977 | 1229 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 188 | 246 | 45 | 33.3 | 89 | 349 | 468 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 477 | 0 | 14 | 29.1 | 119 | 365 | 595 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 334 | 0 | 30 | 79.7 | 46 | 176 | 264 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 70 | 0 | 7 | 25.1 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 352 | 0 | 45 | 105.6 | 88 | 242 | 342 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 18 | 0 | 7 | 25.7 | 3 | 9 | 30 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 1039 | 0 | 60 | 93.3 | 231 | 911 | 1144 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3443 | 0 | 90 | 826.3 | 127 | 507 | 594 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 54 | 0 | 14 | 26.7 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 34 | 26 | 45 | 39.2 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 322 | 0 | 7 | 172.5 | 5 | 20 | 76 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 108 | 290 | 90 | 58.9 | 94 | 261 | 316 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 372 | 515 | 45 | 33.1 | 176 | 693 | 928 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 507 | 0 | 45 | 227.0 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 281 | 705 | 90 | 40.5 | 214 | 846 | 992 | 0 | — |
| ITEM-0082 | B - Core Products | Reorder | 116 | 0 | 7 | 10.0 | 28 | 121 | 364 | 250 | — |
| ITEM-0083 | B - Core Products | Excess | 726 | 0 | 14 | 65.0 | 65 | 233 | 468 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 352 | 0 | 60 | 154.5 | 48 | 187 | 235 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 45 | 0 | 14 | 45.0 | 6 | 21 | 51 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 214 | 135 | 45 | 48.3 | 54 | 258 | 391 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 22 | 50 | 30 | 14.9 | 13 | 59 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 577 | 1027 | 90 | 46.2 | 380 | 1516 | 1778 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 113 | 485 | 7 | 6.2 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 101 | 0 | 7 | 21.3 | 13 | 51 | 151 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6677 | 0 | 90 | 366.6 | 689 | 2347 | 2602 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3530 | 0 | 60 | 254.8 | 355 | 1201 | 1395 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 56.0 | 96 | 139 | 251 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 61 | 0 | 7 | 11.8 | 15 | 57 | 165 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 110 | 0 | 14 | 34.5 | 19 | 67 | 134 | 0 | — |
| ITEM-0101 | A - Top Movers | Reorder | 621 | 865 | 60 | 40.2 | 718 | 1662 | 1878 | 395 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 193 | 0 | 45 | 104.6 | 23 | 108 | 164 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 67.5 | 387 | 1163 | 1342 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 309 | 180 | 45 | 41.4 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 773 | 1542 | 90 | 45.5 | 647 | 2192 | 2430 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 357 | 738 | 60 | 32.9 | 223 | 886 | 1115 | 0 | 55 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1044 | 1224 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1499 | 445 | 90 | 105.2 | 545 | 1843 | 2042 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 259 | 1407 | 60 | 14.8 | 449 | 1516 | 1761 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 24 | 45 | 14 | 16.6 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 833 | 0 | 14 | 106.0 | 206 | 324 | 489 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 105 | 0 | 45 | 70.5 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 176 | 696 | 816 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 149 | 135 | 30 | 25.2 | 64 | 248 | 372 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 27 | 59 | 30 | 14.4 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 341 | 0 | 7 | 27.5 | 34 | 134 | 395 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 226 | 0 | 14 | 22.7 | 57 | 207 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 23 | 132 | 7 | 3.9 | 17 | 65 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 168.8 | 306 | 479 | 556 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 506 | 191 | 45 | 56.7 | 139 | 550 | 737 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 480 | 0 | 14 | 79.1 | 34 | 125 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 248 | 130 | 60 | 59.2 | 68 | 324 | 450 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 136 | 171 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3605 | 0 | 60 | 262.3 | 355 | 1194 | 1386 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 343 | 0 | 14 | 46.3 | 54 | 166 | 269 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 267 | 474 | 30 | 17.7 | 200 | 668 | 879 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 905 | 799 | 60 | 48.3 | 478 | 1622 | 1884 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2072 | 0 | 45 | 212.6 | 154 | 603 | 807 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 81.8 | 630 | 1509 | 1811 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 232 | 470 | 45 | 21.6 | 170 | 665 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 595 | 0 | 7 | 47.0 | 38 | 140 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 94 | 371 | 466 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 114 | 636 | 90 | 36.5 | 96 | 381 | 446 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 39.3 | 430 | 696 | 945 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 911 | 0 | 14 | 84.8 | 235 | 397 | 622 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 615 | 0 | 60 | 164.2 | 78 | 307 | 386 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 799 | 400 | 90 | 350.8 | 215 | 423 | 471 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 201 | 0 | 60 | 144.7 | 24 | 109 | 151 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 464 | 0 | 14 | 63.9 | 42 | 151 | 304 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 556 | 274 | 30 | 31.7 | 233 | 778 | 1024 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 562 | 0 | 7 | 26.7 | 308 | 477 | 772 | 0 | — |
