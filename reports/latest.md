# Synthetic Inventory Health

**Simulation date: 2026-10-04**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 86 |
| Lead-time risk | 9 |
| Reorder | 2 |
| Stockout | 14 |

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
| ITEM-0001 | B - Core Products | Healthy | 673 | 0 | 30 | 54.0 | 132 | 519 | 780 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 611 | 737 | 60 | 38.9 | 402 | 1360 | 1579 | 231 | — |
| ITEM-0005 | B - Core Products | Excess | 1954 | 0 | 45 | 370.2 | 85 | 328 | 439 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 129 | 160 | 14 | 17.0 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 169 | 0 | 14 | 23.1 | 46 | 156 | 310 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 38 | 198 | 60 | 23.4 | 28 | 127 | 176 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 115 | 410 | 90 | 47.5 | 75 | 296 | 347 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 95.4 | 323 | 460 | 700 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 371 | 0 | 90 | 127.4 | 69 | 334 | 422 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 939 | 0 | 7 | 74.3 | 33 | 135 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Healthy | 502 | 0 | 45 | 75.2 | 105 | 413 | 553 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1161 | 0 | 30 | 292.7 | 46 | 169 | 253 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2984 | 0 | 60 | 289.7 | 213 | 842 | 1058 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 263 | 0 | 14 | 34.8 | 47 | 161 | 319 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 568 | 0 | 60 | 460.5 | 22 | 98 | 135 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 618 | 2097 | 2324 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 46 | 0 | 30 | 79.6 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 225 | 0 | 30 | 86.2 | 29 | 110 | 165 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 251 | 960 | 90 | 39.4 | 199 | 780 | 914 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1270 | 0 | 14 | 201.6 | 38 | 133 | 265 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 362 | 0 | 60 | 84.8 | 68 | 329 | 457 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 351 | 0 | 45 | 87.0 | 67 | 253 | 338 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 114 | 245 | 14 | 9.7 | 66 | 242 | 488 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 147 | 0 | 14 | 29.2 | 31 | 107 | 213 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 395 | 0 | 30 | 47.8 | 89 | 345 | 519 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 466 | 290 | 30 | 32.4 | 155 | 601 | 903 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4509 | 0 | 60 | 497.3 | 238 | 792 | 918 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 24.4 | 334 | 545 | 741 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 155 | 0 | 14 | 25.4 | 39 | 131 | 259 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 734 | 0 | 45 | 215.2 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 156.7 | 113 | 340 | 415 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 72 | 175 | 225 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 216 | 475 | 60 | 45.3 | 174 | 465 | 608 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 55.0 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 9 | 80 | 45 | 10.4 | 12 | 52 | 78 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 260 | 0 | 7 | 25.9 | 26 | 107 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 177 | 0 | 7 | 24.9 | 20 | 77 | 226 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4505 | 0 | 60 | 443.1 | 268 | 889 | 1031 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 486 | 0 | 14 | 53.6 | 71 | 207 | 334 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1194 | 1390 | 90 | 64.8 | 696 | 2373 | 2631 | 0 | 126 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 74 | 280 | 375 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 44 | 110 | 14 | 9.0 | 28 | 102 | 204 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 107 | 0 | 30 | 58.7 | 17 | 74 | 129 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 667 | 0 | 14 | 100.0 | 38 | 138 | 278 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 978 | 260 | 60 | 79.5 | 253 | 1004 | 1262 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 363 | 0 | 45 | 66.5 | 85 | 336 | 451 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 462 | 0 | 14 | 29.0 | 117 | 357 | 580 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 438 | 0 | 30 | 78.1 | 64 | 238 | 356 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 59 | 0 | 7 | 21.0 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 31 | 0 | 7 | 39.3 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 224 | 881 | 1107 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3549 | 0 | 90 | 672.4 | 163 | 644 | 755 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 47 | 0 | 14 | 22.6 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 62 | 0 | 45 | 72.5 | 12 | 52 | 78 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 366 | 0 | 7 | 142.0 | 7 | 28 | 105 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 406 | 540 | 45 | 33.8 | 189 | 743 | 995 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 571 | 0 | 45 | 248.3 | 28 | 134 | 203 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 479 | 393 | 90 | 69.4 | 211 | 839 | 984 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 182 | 0 | 7 | 16.3 | 27 | 117 | 350 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1040 | 0 | 14 | 95.4 | 64 | 228 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 82 | 337 | 60 | 28.8 | 60 | 234 | 294 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 64.1 | 215 | 334 | 499 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 35 | 0 | 14 | 27.6 | 7 | 26 | 64 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 355 | 0 | 45 | 85.0 | 51 | 244 | 369 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 113 | 702 | 14 | 7.7 | 315 | 536 | 846 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 64 | 0 | 30 | 42.7 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 889 | 735 | 90 | 67.2 | 403 | 1607 | 1884 | 0 | 101 |
| ITEM-0093 | B - Core Products | Healthy | 378 | 435 | 7 | 19.9 | 261 | 413 | 812 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 129 | 0 | 7 | 23.3 | 17 | 62 | 178 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7185 | 0 | 90 | 395.7 | 689 | 2342 | 2596 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3909 | 0 | 60 | 286.3 | 351 | 1184 | 1376 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 177 | 0 | 7 | 25.2 | 22 | 79 | 226 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 190 | 0 | 14 | 45.5 | 26 | 89 | 177 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 36 | 210 | 45 | 16.1 | 29 | 132 | 199 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 530 | 0 | 45 | 70.6 | 119 | 465 | 623 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1237 | 1041 | 90 | 73.2 | 642 | 2179 | 2416 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 414 | 740 | 60 | 36.8 | 231 | 918 | 1154 | 0 | 80 |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 34 | 1100 | 90 | 3.8 | 272 | 1083 | 1271 | 0 | 4 |
| ITEM-0110 | C - Slow Moving | Healthy | 579 | 0 | 60 | 148.5 | 125 | 363 | 480 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1966 | 0 | 90 | 139.3 | 537 | 1822 | 2019 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 775 | 902 | 60 | 43.8 | 454 | 1533 | 1780 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 18 | 45 | 14 | 12.4 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 130 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 19 | 648 | 90 | 3.5 | 168 | 662 | 776 | 0 | 4 |
| ITEM-0119 | B - Core Products | Healthy | 314 | 0 | 30 | 53.8 | 63 | 244 | 367 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 74 | 59 | 30 | 37.8 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 316 | 0 | 7 | 23.4 | 36 | 145 | 429 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 60.1 | 226 | 445 | 544 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 295 | 0 | 14 | 29.6 | 57 | 207 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 82 | 0 | 7 | 13.6 | 16 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 131.8 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 552 | 740 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1284 | 697 | 90 | 95.1 | 717 | 1946 | 2229 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 669 | 0 | 14 | 113.2 | 33 | 122 | 246 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 359 | 0 | 60 | 82.4 | 70 | 336 | 467 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 26 | 119 | 149 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4013 | 0 | 60 | 291.5 | 354 | 1194 | 1387 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 524 | 0 | 14 | 53.3 | 75 | 223 | 361 | 0 | — |
| ITEM-0139 | A - Top Movers | Reorder | 444 | 227 | 30 | 28.7 | 203 | 684 | 900 | 229 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1438 | 269 | 60 | 80.3 | 458 | 1551 | 1802 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2346 | 0 | 45 | 235.9 | 156 | 614 | 823 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 552 | 1320 | 1584 | 0 | 15 |
| ITEM-0143 | B - Core Products | Healthy | 520 | 236 | 45 | 47.3 | 172 | 678 | 909 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 952 | 0 | 7 | 75.0 | 38 | 140 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 124 | 484 | 607 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 184 | 636 | 90 | 43.8 | 129 | 512 | 600 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 44.3 | 338 | 610 | 990 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 705 | 0 | 60 | 144.2 | 104 | 403 | 505 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 34 | 200 | 60 | 20.3 | 28 | 131 | 181 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 673 | 0 | 14 | 96.9 | 41 | 146 | 291 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 770 | 266 | 30 | 42.7 | 238 | 798 | 1050 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 26.6 | 301 | 487 | 812 | 0 | — |
