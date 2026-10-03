# Synthetic Inventory Health

**Simulation date: 2026-10-03**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 86 |
| Lead-time risk | 9 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Healthy | 682 | 0 | 30 | 54.5 | 133 | 522 | 785 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 637 | 737 | 60 | 40.8 | 399 | 1351 | 1569 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1960 | 0 | 45 | 372.2 | 85 | 328 | 438 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 137 | 160 | 14 | 18.1 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 176 | 0 | 14 | 23.6 | 47 | 159 | 316 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 40 | 198 | 60 | 24.5 | 28 | 128 | 177 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 117 | 410 | 90 | 47.9 | 76 | 299 | 350 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 92.1 | 324 | 466 | 714 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 373 | 0 | 90 | 127.6 | 69 | 335 | 423 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 959 | 0 | 7 | 76.4 | 33 | 134 | 398 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 409 | 548 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1163 | 0 | 30 | 294.8 | 46 | 169 | 252 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2984 | 0 | 60 | 285.7 | 215 | 853 | 1072 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 265 | 0 | 14 | 34.2 | 48 | 165 | 328 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 568 | 0 | 60 | 452.4 | 22 | 99 | 137 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 620 | 2106 | 2334 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 46 | 0 | 30 | 79.6 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 227 | 0 | 30 | 86.6 | 29 | 111 | 166 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 256 | 960 | 90 | 39.8 | 200 | 786 | 921 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1275 | 0 | 14 | 200.3 | 39 | 135 | 269 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 367 | 0 | 60 | 86.5 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 355 | 0 | 45 | 88.3 | 66 | 252 | 336 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 130 | 245 | 14 | 11.1 | 66 | 242 | 487 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 153 | 0 | 14 | 30.3 | 31 | 107 | 213 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 409 | 0 | 30 | 50.0 | 88 | 342 | 514 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 488 | 290 | 30 | 34.6 | 153 | 591 | 888 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4521 | 0 | 60 | 498.6 | 238 | 792 | 918 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 24.4 | 334 | 545 | 741 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 158 | 0 | 14 | 25.4 | 39 | 133 | 263 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 738 | 0 | 45 | 217.8 | 41 | 197 | 299 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 72 | 175 | 225 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 9 | 80 | 45 | 10.3 | 12 | 53 | 79 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 271 | 0 | 7 | 27.0 | 26 | 107 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 189 | 0 | 7 | 26.8 | 20 | 77 | 225 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4513 | 0 | 60 | 435.3 | 274 | 907 | 1052 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 491 | 0 | 14 | 54.3 | 71 | 207 | 334 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1209 | 1390 | 90 | 65.8 | 695 | 2368 | 2625 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 74 | 279 | 373 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 49 | 110 | 14 | 10.0 | 28 | 102 | 204 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 107 | 0 | 30 | 57.0 | 17 | 76 | 132 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 676 | 0 | 14 | 101.9 | 37 | 137 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 995 | 260 | 60 | 80.8 | 254 | 1005 | 1264 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 369 | 0 | 45 | 67.6 | 85 | 336 | 451 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 218 | 245 | 14 | 13.4 | 119 | 364 | 592 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 442 | 0 | 30 | 79.2 | 64 | 237 | 355 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 62 | 0 | 7 | 22.1 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 7 | 25 | 7 | 8.9 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 884 | 1111 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3551 | 0 | 90 | 667.2 | 165 | 650 | 762 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 50 | 0 | 14 | 24.2 | 10 | 41 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 63 | 0 | 45 | 73.6 | 12 | 52 | 78 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 367 | 0 | 7 | 142.4 | 7 | 28 | 105 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 412 | 540 | 45 | 34.3 | 189 | 743 | 995 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 571 | 0 | 45 | 243.6 | 29 | 137 | 208 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 488 | 393 | 90 | 70.8 | 211 | 838 | 983 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 199 | 0 | 7 | 17.7 | 28 | 119 | 355 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1045 | 0 | 14 | 95.4 | 64 | 229 | 459 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 84 | 337 | 60 | 29.1 | 61 | 238 | 298 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 64.1 | 215 | 334 | 499 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 37 | 0 | 14 | 29.0 | 7 | 27 | 65 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 355 | 0 | 45 | 84.1 | 52 | 247 | 373 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 113 | 702 | 14 | 7.7 | 315 | 536 | 846 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 64 | 0 | 30 | 41.7 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 895 | 735 | 90 | 67.6 | 403 | 1608 | 1886 | 0 | 101 |
| ITEM-0093 | B - Core Products | Healthy | 378 | 435 | 7 | 19.9 | 261 | 413 | 812 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 133 | 0 | 7 | 23.9 | 17 | 62 | 179 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7209 | 0 | 90 | 399.0 | 686 | 2331 | 2583 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3921 | 0 | 60 | 289.0 | 349 | 1177 | 1367 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 183 | 0 | 7 | 25.5 | 23 | 81 | 232 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 192 | 0 | 14 | 45.5 | 26 | 90 | 178 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 37 | 210 | 45 | 16.4 | 29 | 133 | 201 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 537 | 0 | 45 | 71.8 | 119 | 463 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1246 | 1041 | 90 | 74.1 | 640 | 2170 | 2406 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 422 | 481 | 60 | 37.3 | 233 | 924 | 1162 | 259 | 80 |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 42 | 1100 | 90 | 4.7 | 273 | 1087 | 1275 | 0 | 5 |
| ITEM-0110 | C - Slow Moving | Healthy | 622 | 0 | 60 | 181.8 | 115 | 324 | 427 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1969 | 0 | 90 | 138.3 | 541 | 1837 | 2036 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 792 | 902 | 60 | 44.9 | 453 | 1530 | 1777 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 18 | 45 | 14 | 12.3 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 30 | 648 | 90 | 5.6 | 165 | 652 | 764 | 0 | 6 |
| ITEM-0119 | B - Core Products | Healthy | 316 | 0 | 30 | 54.0 | 63 | 245 | 368 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 75 | 59 | 30 | 38.4 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 326 | 0 | 7 | 24.1 | 36 | 145 | 429 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 60.1 | 226 | 445 | 544 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 303 | 0 | 14 | 30.5 | 57 | 206 | 415 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 87 | 0 | 7 | 14.5 | 16 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 131.8 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 554 | 743 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1284 | 697 | 90 | 95.1 | 717 | 1946 | 2229 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 679 | 0 | 14 | 116.2 | 33 | 121 | 244 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 363 | 0 | 60 | 82.7 | 71 | 339 | 471 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 116 | 146 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4026 | 0 | 60 | 294.1 | 352 | 1188 | 1379 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 532 | 0 | 14 | 53.9 | 75 | 224 | 362 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 458 | 227 | 30 | 29.6 | 203 | 683 | 899 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1451 | 269 | 60 | 80.7 | 459 | 1556 | 1808 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2359 | 0 | 45 | 238.8 | 155 | 610 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 552 | 1320 | 1584 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 296 | 479 | 45 | 27.0 | 172 | 677 | 907 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 955 | 0 | 7 | 74.7 | 38 | 141 | 409 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 125 | 488 | 613 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 187 | 636 | 90 | 43.6 | 132 | 523 | 613 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 44.3 | 338 | 610 | 990 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 708 | 0 | 60 | 141.0 | 107 | 414 | 519 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 36 | 200 | 60 | 21.6 | 28 | 130 | 180 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 681 | 0 | 14 | 98.4 | 41 | 145 | 291 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Reorder | 522 | 259 | 30 | 29.0 | 238 | 796 | 1047 | 266 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 26.6 | 301 | 487 | 812 | 0 | — |
