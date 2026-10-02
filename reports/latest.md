# Synthetic Inventory Health

**Simulation date: 2026-10-02**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 84 |
| Lead-time risk | 9 |
| Reorder | 2 |
| Stockout | 15 |

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
| ITEM-0001 | B - Core Products | Healthy | 698 | 0 | 30 | 56.3 | 132 | 517 | 777 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 652 | 737 | 60 | 42.1 | 397 | 1342 | 1559 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1962 | 0 | 45 | 364.8 | 87 | 335 | 448 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 142 | 160 | 14 | 18.6 | 43 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 97 | 146 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 182 | 0 | 14 | 24.6 | 47 | 159 | 314 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 41 | 198 | 60 | 24.6 | 28 | 130 | 180 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 117 | 410 | 90 | 46.8 | 78 | 306 | 358 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 92.1 | 324 | 466 | 714 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 375 | 0 | 90 | 127.8 | 70 | 337 | 425 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 968 | 0 | 7 | 77.1 | 33 | 134 | 398 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 409 | 548 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1164 | 0 | 30 | 287.8 | 47 | 173 | 258 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2992 | 0 | 60 | 287.7 | 215 | 850 | 1068 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 268 | 0 | 14 | 33.7 | 49 | 169 | 336 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 570 | 0 | 60 | 446.1 | 22 | 100 | 139 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 619 | 2101 | 2329 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 83.1 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 229 | 0 | 30 | 87.0 | 29 | 111 | 166 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 261 | 960 | 90 | 40.4 | 201 | 789 | 925 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1279 | 0 | 14 | 197.4 | 39 | 137 | 273 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 370 | 0 | 60 | 86.9 | 68 | 328 | 456 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 359 | 0 | 45 | 87.8 | 68 | 257 | 342 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 685 | 0 | 60 | 342.5 | 73 | 195 | 255 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 136 | 245 | 14 | 11.6 | 66 | 242 | 487 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 156 | 0 | 14 | 30.5 | 31 | 108 | 216 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 419 | 0 | 30 | 51.2 | 88 | 342 | 514 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 489 | 290 | 30 | 34.3 | 154 | 596 | 896 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4527 | 0 | 60 | 491.5 | 242 | 804 | 933 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 494 | 270 | 14 | 40.1 | 310 | 495 | 668 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 161 | 0 | 14 | 25.6 | 40 | 135 | 267 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 740 | 0 | 45 | 217.6 | 41 | 198 | 300 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 66 | 153 | 196 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 11 | 80 | 45 | 12.2 | 13 | 55 | 82 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 64 | 218 | 7 | 6.4 | 26 | 107 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 39 | 155 | 7 | 5.5 | 20 | 78 | 227 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4518 | 0 | 60 | 428.0 | 278 | 922 | 1070 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 501 | 0 | 14 | 54.4 | 73 | 212 | 341 | 0 | — |
| ITEM-0056 | A - Top Movers | Reorder | 1231 | 1125 | 90 | 67.2 | 693 | 2361 | 2617 | 265 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 75 | 282 | 377 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 55 | 110 | 14 | 11.4 | 28 | 101 | 203 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 108 | 0 | 30 | 55.9 | 18 | 78 | 136 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 685 | 0 | 14 | 102.9 | 38 | 138 | 278 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1006 | 260 | 60 | 81.3 | 255 | 1010 | 1270 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 376 | 0 | 45 | 69.1 | 85 | 336 | 450 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 220 | 245 | 14 | 13.2 | 120 | 370 | 603 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 446 | 0 | 30 | 78.2 | 66 | 243 | 363 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 65 | 0 | 7 | 23.3 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 7 | 25 | 7 | 8.8 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 226 | 888 | 1116 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3554 | 0 | 90 | 656.8 | 167 | 660 | 774 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 51 | 0 | 14 | 24.4 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 64 | 0 | 45 | 75.8 | 12 | 51 | 77 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 368 | 0 | 7 | 142.1 | 7 | 28 | 106 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 428 | 540 | 45 | 35.8 | 188 | 738 | 990 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 573 | 0 | 45 | 242.1 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 490 | 393 | 90 | 70.6 | 212 | 844 | 990 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 210 | 0 | 7 | 18.7 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1053 | 0 | 14 | 95.9 | 64 | 229 | 460 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 86 | 337 | 60 | 29.7 | 62 | 239 | 300 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 63.7 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 37 | 0 | 14 | 28.2 | 7 | 27 | 66 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 355 | 0 | 45 | 83.4 | 52 | 248 | 376 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 113 | 702 | 14 | 7.7 | 391 | 612 | 819 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 66 | 0 | 30 | 43.0 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 909 | 735 | 90 | 69.2 | 401 | 1598 | 1874 | 0 | 103 |
| ITEM-0093 | B - Core Products | Reorder | 378 | 0 | 7 | 19.9 | 261 | 413 | 812 | 435 | — |
| ITEM-0094 | B - Core Products | Healthy | 136 | 0 | 7 | 23.8 | 18 | 64 | 184 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7213 | 0 | 90 | 395.1 | 692 | 2354 | 2609 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3932 | 0 | 60 | 285.8 | 355 | 1195 | 1387 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 193 | 0 | 7 | 26.9 | 23 | 81 | 232 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 195 | 0 | 14 | 45.6 | 27 | 92 | 181 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 38 | 210 | 45 | 16.4 | 30 | 137 | 206 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 546 | 0 | 45 | 73.2 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1259 | 1041 | 90 | 74.6 | 642 | 2178 | 2415 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 441 | 481 | 60 | 39.4 | 230 | 913 | 1148 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 51 | 1100 | 90 | 5.7 | 274 | 1092 | 1281 | 0 | 6 |
| ITEM-0110 | C - Slow Moving | Excess | 644 | 0 | 60 | 202.7 | 111 | 305 | 401 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1988 | 0 | 90 | 140.2 | 539 | 1830 | 2028 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 822 | 902 | 60 | 47.2 | 447 | 1509 | 1752 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 19 | 45 | 14 | 13.0 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 34 | 648 | 90 | 6.3 | 165 | 653 | 765 | 0 | 7 |
| ITEM-0119 | B - Core Products | Healthy | 323 | 0 | 30 | 55.5 | 63 | 244 | 366 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 20 | 114 | 30 | 10.1 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 344 | 0 | 7 | 25.5 | 35 | 143 | 427 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 60.1 | 226 | 445 | 544 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 101 | 216 | 14 | 10.2 | 57 | 206 | 414 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 97 | 0 | 7 | 16.4 | 16 | 64 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 919 | 200 | 30 | 108.3 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 558 | 748 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1284 | 697 | 90 | 95.1 | 717 | 1946 | 2229 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 686 | 0 | 14 | 118.0 | 33 | 121 | 243 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 369 | 0 | 60 | 84.5 | 70 | 337 | 468 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 116 | 146 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4035 | 0 | 60 | 293.1 | 354 | 1194 | 1387 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 543 | 0 | 14 | 54.2 | 77 | 228 | 368 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 476 | 227 | 30 | 30.7 | 164 | 645 | 970 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1464 | 269 | 60 | 81.4 | 459 | 1556 | 1808 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2377 | 0 | 45 | 242.3 | 154 | 606 | 812 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 552 | 1320 | 1584 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 306 | 479 | 45 | 28.1 | 171 | 673 | 902 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 964 | 0 | 7 | 75.1 | 38 | 141 | 411 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 127 | 497 | 624 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 192 | 636 | 90 | 44.2 | 134 | 530 | 621 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 44.3 | 338 | 610 | 990 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 154.3 | 217 | 357 | 553 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 712 | 0 | 60 | 138.4 | 110 | 424 | 532 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 37 | 200 | 60 | 21.6 | 29 | 134 | 185 | 0 | 22 |
| ITEM-0155 | B - Core Products | Excess | 685 | 0 | 14 | 98.6 | 41 | 146 | 291 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 546 | 259 | 30 | 30.2 | 240 | 802 | 1055 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 26.6 | 301 | 487 | 812 | 0 | — |
