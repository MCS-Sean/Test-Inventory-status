# Synthetic Inventory Health

**Simulation date: 2026-11-02**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 97 |
| Lead-time risk | 2 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Healthy | 279 | 291 | 30 | 21.4 | 138 | 544 | 818 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 34.4 | 94 | 151 | 298 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 441 | 1107 | 60 | 28.9 | 391 | 1322 | 1536 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1847 | 0 | 45 | 460.5 | 64 | 249 | 333 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 87 | 155 | 14 | 12.3 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 106 | 0 | 45 | 71.2 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 158 | 0 | 14 | 28.1 | 32 | 117 | 235 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 197 | 0 | 60 | 155.5 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 67 | 410 | 90 | 36.8 | 57 | 223 | 262 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 294 | 90 | 90 | 105.0 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 525 | 0 | 7 | 39.9 | 34 | 140 | 416 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 320 | 155 | 45 | 48.2 | 104 | 410 | 549 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1084 | 0 | 30 | 369.5 | 33 | 124 | 186 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2693 | 0 | 60 | 253.5 | 219 | 867 | 1091 | 0 | — |
| ITEM-0020 | B - Core Products | Reorder | 119 | 0 | 14 | 20.9 | 33 | 119 | 239 | 120 | — |
| ITEM-0021 | C - Slow Moving | Excess | 547 | 0 | 60 | 600.4 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 598 | 2025 | 2245 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 27 | 0 | 30 | 46.7 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 1128 | 452 | 60 | 107.9 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 177 | 0 | 30 | 88.5 | 17 | 79 | 139 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1074 | 0 | 90 | 216.2 | 151 | 603 | 708 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 38.1 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1159 | 0 | 14 | 247.2 | 28 | 99 | 197 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 237 | 135 | 60 | 54.7 | 69 | 334 | 464 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 270 | 0 | 45 | 90.3 | 48 | 186 | 249 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 677 | 0 | 60 | 846.2 | 44 | 93 | 117 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 294 | 0 | 14 | 25.1 | 67 | 243 | 490 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 33.5 | 116 | 175 | 329 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 43 | 95 | 14 | 11.0 | 23 | 82 | 165 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 184 | 172 | 30 | 22.4 | 88 | 343 | 516 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 649 | 0 | 30 | 44.1 | 157 | 614 | 922 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4310 | 0 | 60 | 606.1 | 182 | 616 | 716 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 51.0 | 251 | 430 | 681 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 153 | 0 | 14 | 33.6 | 27 | 96 | 191 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 643 | 0 | 45 | 192.3 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 280 | 220 | 90 | 87.2 | 131 | 424 | 520 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 315 | 844 | 1026 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 70 | 0 | 45 | 98.4 | 11 | 44 | 66 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 194 | 0 | 7 | 19.1 | 23 | 105 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 115 | 0 | 7 | 15.4 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4292 | 0 | 60 | 556.6 | 198 | 669 | 777 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 293 | 0 | 14 | 41.2 | 52 | 159 | 259 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 675 | 1950 | 90 | 36.6 | 697 | 2377 | 2635 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 495 | 0 | 45 | 137.5 | 58 | 224 | 300 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 3 | 110 | 14 | 0.6 | 29 | 104 | 209 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 66 | 0 | 30 | 47.1 | 13 | 57 | 99 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 496 | 0 | 14 | 76.0 | 37 | 135 | 272 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 281 | 470 | 60 | 45.2 | 241 | 620 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 644 | 525 | 60 | 53.6 | 248 | 981 | 1233 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 181 | 246 | 45 | 32.1 | 89 | 349 | 468 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 451 | 0 | 14 | 27.2 | 120 | 369 | 601 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 328 | 0 | 30 | 79.1 | 46 | 175 | 262 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 69 | 0 | 7 | 24.9 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 352 | 0 | 45 | 105.6 | 88 | 242 | 342 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 17 | 0 | 7 | 24.3 | 3 | 9 | 30 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 1018 | 0 | 60 | 89.6 | 235 | 929 | 1168 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3442 | 0 | 90 | 841.8 | 125 | 498 | 583 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 54 | 0 | 14 | 27.2 | 9 | 39 | 99 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 32 | 26 | 45 | 36.5 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 320 | 0 | 7 | 175.6 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 108 | 290 | 90 | 58.9 | 94 | 261 | 316 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 365 | 515 | 45 | 32.9 | 174 | 685 | 918 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 505 | 0 | 45 | 228.4 | 27 | 129 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 276 | 705 | 90 | 39.9 | 213 | 842 | 988 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 106 | 250 | 7 | 9.2 | 28 | 121 | 363 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 724 | 0 | 14 | 65.1 | 65 | 232 | 466 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 350 | 0 | 60 | 153.7 | 48 | 187 | 235 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 44 | 0 | 14 | 45.0 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 214 | 135 | 45 | 49.3 | 54 | 254 | 385 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 21 | 50 | 30 | 14.3 | 13 | 59 | 103 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 566 | 1027 | 90 | 45.2 | 380 | 1519 | 1782 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 113 | 485 | 7 | 6.2 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 96 | 0 | 7 | 20.5 | 13 | 51 | 149 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6667 | 0 | 90 | 370.4 | 681 | 2319 | 2571 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3513 | 0 | 60 | 254.4 | 354 | 1197 | 1390 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 56.0 | 96 | 139 | 251 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Reorder | 55 | 0 | 7 | 10.6 | 15 | 57 | 166 | 115 | — |
| ITEM-0100 | B - Core Products | Healthy | 107 | 0 | 14 | 33.6 | 19 | 67 | 134 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 40.2 | 718 | 1662 | 1878 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 192 | 0 | 45 | 104.7 | 23 | 108 | 163 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 74.4 | 357 | 1061 | 1224 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 296 | 180 | 45 | 39.5 | 119 | 464 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 759 | 1542 | 90 | 44.7 | 648 | 2194 | 2432 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 351 | 738 | 60 | 32.4 | 222 | 883 | 1111 | 0 | 55 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 261 | 1038 | 1217 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1490 | 445 | 90 | 104.5 | 545 | 1843 | 2042 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 242 | 1407 | 60 | 13.8 | 449 | 1518 | 1763 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 22 | 45 | 14 | 15.1 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 833 | 0 | 14 | 106.0 | 206 | 324 | 489 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 104 | 0 | 45 | 69.9 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 175 | 692 | 811 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 140 | 135 | 30 | 23.5 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 25 | 59 | 30 | 13.3 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 327 | 0 | 7 | 26.3 | 34 | 134 | 395 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 211 | 0 | 14 | 21.1 | 57 | 207 | 417 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 15 | 132 | 7 | 2.5 | 17 | 65 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 168.8 | 306 | 479 | 556 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 499 | 191 | 45 | 56.1 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 480 | 0 | 14 | 80.0 | 34 | 124 | 250 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 247 | 130 | 60 | 59.9 | 67 | 319 | 443 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 135 | 169 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3592 | 0 | 60 | 260.1 | 356 | 1199 | 1392 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 329 | 0 | 14 | 44.5 | 54 | 165 | 269 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 246 | 474 | 30 | 16.3 | 201 | 671 | 882 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 879 | 799 | 60 | 46.8 | 479 | 1626 | 1889 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2057 | 0 | 45 | 210.6 | 154 | 604 | 809 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 86.3 | 619 | 1452 | 1738 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 452 | 234 | 45 | 41.6 | 171 | 672 | 900 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 578 | 0 | 7 | 45.5 | 38 | 140 | 407 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 92 | 364 | 457 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 110 | 636 | 90 | 35.5 | 96 | 379 | 444 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 39.3 | 430 | 696 | 945 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 911 | 0 | 14 | 84.8 | 235 | 397 | 622 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 609 | 0 | 60 | 162.6 | 78 | 307 | 386 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 739 | 400 | 90 | 251.0 | 241 | 509 | 571 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 200 | 0 | 60 | 146.3 | 23 | 107 | 148 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 459 | 0 | 14 | 63.9 | 42 | 150 | 301 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 532 | 274 | 30 | 30.3 | 232 | 776 | 1022 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 521 | 0 | 7 | 24.2 | 308 | 481 | 782 | 0 | — |
