# Synthetic Inventory Health

**Simulation date: 2026-11-08**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 97 |
| Lead-time risk | 3 |
| Reorder | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 486 | 302 | 30 | 37.1 | 139 | 546 | 821 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 357 | 1107 | 60 | 23.5 | 390 | 1317 | 1530 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1825 | 0 | 45 | 470.6 | 62 | 241 | 322 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 213 | 0 | 14 | 31.0 | 41 | 144 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 97 | 0 | 45 | 65.1 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 112 | 125 | 14 | 20.1 | 32 | 116 | 233 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 190 | 0 | 60 | 150.0 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 56 | 410 | 90 | 30.9 | 56 | 221 | 259 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1824 | 0 | 60 | 130.7 | 793 | 1645 | 1840 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 277 | 90 | 90 | 100.9 | 65 | 315 | 398 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 458 | 0 | 7 | 35.3 | 34 | 138 | 411 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 279 | 155 | 45 | 42.5 | 103 | 406 | 543 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1065 | 0 | 30 | 374.4 | 32 | 121 | 180 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2641 | 0 | 60 | 253.9 | 215 | 850 | 1068 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 89 | 120 | 14 | 16.4 | 32 | 114 | 227 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 540 | 0 | 60 | 607.5 | 16 | 71 | 97 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 590 | 1993 | 2209 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 23 | 20 | 30 | 41.4 | 7 | 25 | 41 | 0 | — |
| ITEM-0027 | A - Top Movers | Reorder | 763 | 626 | 60 | 52.9 | 851 | 1731 | 1932 | 543 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 166 | 0 | 30 | 86.9 | 16 | 76 | 133 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1039 | 0 | 90 | 212.5 | 148 | 593 | 696 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 44.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1117 | 0 | 14 | 241.1 | 27 | 97 | 194 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 222 | 135 | 60 | 52.9 | 67 | 324 | 450 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 249 | 0 | 45 | 85.2 | 47 | 182 | 243 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 234 | 245 | 14 | 20.2 | 66 | 240 | 483 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 41.4 | 100 | 148 | 272 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 121 | 0 | 14 | 32.2 | 23 | 80 | 159 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 131 | 355 | 30 | 15.7 | 89 | 348 | 523 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 572 | 315 | 30 | 38.7 | 156 | 615 | 925 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4266 | 0 | 60 | 618.3 | 176 | 597 | 694 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 61.2 | 221 | 371 | 579 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 121 | 0 | 14 | 26.2 | 27 | 97 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 499 | 1324 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 624 | 0 | 45 | 190.4 | 40 | 191 | 290 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 192 | 179 | 60 | 67.8 | 113 | 286 | 371 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 790 | 60 | 3.8 | 325 | 891 | 1085 | 260 | 4 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 185.3 | 84 | 127 | 186 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 67 | 0 | 45 | 102.2 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 153 | 0 | 7 | 15.6 | 22 | 101 | 308 | 0 | — |
| ITEM-0053 | B - Core Products | Reorder | 79 | 0 | 7 | 10.8 | 20 | 79 | 233 | 155 | — |
| ITEM-0054 | A - Top Movers | Excess | 4226 | 0 | 60 | 538.7 | 201 | 680 | 790 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 240 | 0 | 14 | 33.5 | 52 | 160 | 260 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 605 | 1950 | 90 | 33.7 | 680 | 2315 | 2567 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 468 | 0 | 45 | 132.0 | 56 | 220 | 294 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 101 | 105 | 14 | 20.5 | 28 | 102 | 206 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 55 | 43 | 30 | 38.7 | 13 | 58 | 100 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 455 | 0 | 14 | 70.7 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 52.9 | 210 | 524 | 632 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 544 | 525 | 60 | 44.4 | 253 | 1001 | 1258 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 141 | 246 | 45 | 25.1 | 89 | 348 | 466 | 0 | — |
| ITEM-0067 | A - Top Movers | Reorder | 356 | 0 | 14 | 21.6 | 119 | 367 | 598 | 245 | — |
| ITEM-0068 | B - Core Products | Healthy | 301 | 0 | 30 | 74.6 | 44 | 170 | 254 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 55 | 0 | 7 | 20.0 | 7 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 106.7 | 82 | 220 | 310 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 15 | 0 | 7 | 22.5 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 958 | 0 | 60 | 85.3 | 233 | 919 | 1155 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3421 | 0 | 90 | 882.2 | 118 | 471 | 553 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 40 | 0 | 14 | 20.2 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 26 | 54 | 45 | 29.6 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 964 | 1090 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 306 | 0 | 7 | 172.1 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 25.3 | 107 | 295 | 356 | 0 | 26 |
| ITEM-0079 | B - Core Products | Healthy | 279 | 515 | 45 | 25.1 | 175 | 687 | 921 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 489 | 0 | 45 | 219.0 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 386 | 547 | 90 | 54.7 | 218 | 861 | 1009 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 41 | 250 | 7 | 3.5 | 29 | 122 | 366 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 652 | 0 | 14 | 58.4 | 65 | 233 | 467 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 335 | 0 | 60 | 151.5 | 46 | 181 | 228 | 0 | — |
| ITEM-0085 | B - Core Products | Reorder | 242 | 0 | 14 | 19.2 | 253 | 442 | 707 | 465 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 37 | 0 | 14 | 38.7 | 6 | 21 | 49 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 186 | 135 | 45 | 42.8 | 54 | 254 | 385 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 688 | 369 | 14 | 34.2 | 473 | 775 | 1057 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 12 | 50 | 30 | 8.2 | 13 | 59 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 501 | 1027 | 90 | 40.0 | 381 | 1522 | 1785 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 32.9 | 256 | 402 | 784 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 66 | 0 | 7 | 14.1 | 12 | 50 | 148 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6536 | 0 | 90 | 361.5 | 685 | 2331 | 2584 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3466 | 0 | 60 | 256.1 | 348 | 1174 | 1363 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 41.7 | 89 | 130 | 236 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 22 | 115 | 7 | 4.4 | 14 | 54 | 159 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 93 | 0 | 14 | 30.2 | 18 | 65 | 129 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 621 | 1260 | 60 | 41.3 | 573 | 1491 | 1807 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 179 | 0 | 45 | 98.8 | 23 | 107 | 161 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 83.5 | 332 | 959 | 1104 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 251 | 340 | 45 | 33.3 | 120 | 468 | 626 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 652 | 1789 | 90 | 38.4 | 648 | 2194 | 2432 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 518 | 498 | 60 | 46.3 | 228 | 911 | 1146 | 0 | 47 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 260 | 1034 | 1212 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1384 | 665 | 90 | 94.9 | 558 | 1885 | 2089 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 513 | 1047 | 60 | 29.9 | 441 | 1489 | 1730 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 15 | 45 | 14 | 10.5 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 94 | 0 | 45 | 63.1 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 178 | 705 | 827 | 0 | 1 |
| ITEM-0119 | B - Core Products | Reorder | 109 | 135 | 30 | 18.7 | 63 | 245 | 367 | 125 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 70 | 58 | 30 | 36.4 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 252 | 0 | 7 | 20.7 | 32 | 130 | 386 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 168 | 211 | 14 | 17.2 | 56 | 203 | 407 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 111 | 0 | 7 | 18.4 | 17 | 66 | 192 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 452 | 191 | 45 | 51.4 | 138 | 543 | 727 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 444 | 0 | 14 | 72.3 | 35 | 128 | 257 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 220 | 130 | 60 | 53.7 | 67 | 318 | 441 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3532 | 0 | 60 | 261.6 | 347 | 1171 | 1360 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 278 | 0 | 14 | 38.3 | 52 | 161 | 263 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 415 | 245 | 30 | 28.0 | 198 | 658 | 866 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 744 | 1068 | 60 | 40.0 | 474 | 1610 | 1871 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1983 | 0 | 45 | 200.3 | 156 | 612 | 820 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 389 | 463 | 45 | 36.4 | 169 | 661 | 886 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 523 | 0 | 7 | 41.5 | 38 | 139 | 404 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 866 | 0 | 60 | 195.3 | 92 | 363 | 456 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 94 | 636 | 90 | 31.2 | 93 | 368 | 431 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 67.3 | 406 | 645 | 868 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 590 | 0 | 60 | 169.1 | 73 | 286 | 360 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 189 | 0 | 60 | 140.6 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 414 | 0 | 14 | 57.9 | 42 | 150 | 300 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 447 | 533 | 30 | 25.6 | 231 | 773 | 1017 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 314 | 498 | 7 | 15.0 | 318 | 486 | 779 | 0 | — |
