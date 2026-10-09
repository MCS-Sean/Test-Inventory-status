# Synthetic Inventory Health

**Simulation date: 2026-10-09**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 88 |
| Lead-time risk | 8 |
| Reorder | 1 |
| Stockout | 13 |

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
| ITEM-0001 | B - Core Products | Healthy | 590 | 0 | 30 | 46.5 | 134 | 528 | 794 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 540 | 968 | 60 | 34.9 | 397 | 1341 | 1557 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1937 | 0 | 45 | 377.3 | 83 | 320 | 427 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 78 | 160 | 14 | 10.2 | 44 | 159 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 138 | 0 | 45 | 85.7 | 20 | 95 | 143 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 145 | 0 | 14 | 21.3 | 41 | 144 | 287 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 33 | 198 | 60 | 22.2 | 25 | 116 | 161 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 110 | 410 | 90 | 48.5 | 71 | 278 | 325 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 58 | 2145 | 60 | 5.4 | 679 | 1340 | 1492 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 358 | 0 | 90 | 123.4 | 69 | 333 | 420 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 868 | 0 | 7 | 68.8 | 33 | 134 | 399 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 78 | 203 | 285 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 478 | 0 | 45 | 71.5 | 105 | 413 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1148 | 0 | 30 | 302.1 | 44 | 162 | 242 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2937 | 0 | 60 | 284.2 | 214 | 845 | 1062 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 241 | 0 | 14 | 34.5 | 42 | 147 | 294 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 564 | 0 | 60 | 478.9 | 21 | 93 | 129 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 602 | 2041 | 2263 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 43 | 0 | 30 | 73.0 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 72.1 | 767 | 1458 | 1617 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 217 | 0 | 30 | 89.2 | 27 | 103 | 154 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 231 | 960 | 90 | 38.2 | 189 | 740 | 866 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 23.3 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1253 | 0 | 14 | 216.9 | 35 | 122 | 243 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 341 | 0 | 60 | 79.7 | 69 | 330 | 459 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 334 | 0 | 45 | 90.0 | 60 | 231 | 309 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 286 | 0 | 14 | 24.0 | 67 | 246 | 497 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 134 | 0 | 14 | 27.9 | 30 | 103 | 204 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 368 | 0 | 30 | 45.2 | 87 | 340 | 511 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 392 | 290 | 30 | 27.7 | 152 | 592 | 889 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4488 | 0 | 60 | 534.3 | 220 | 733 | 850 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 28.5 | 313 | 494 | 662 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 126 | 0 | 14 | 21.9 | 36 | 123 | 244 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 498 | 1312 | 1500 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 718 | 0 | 45 | 209.8 | 42 | 200 | 303 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 353 | 115 | 90 | 131.3 | 118 | 363 | 444 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 25 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 61.6 | 159 | 289 | 470 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.5 | 12 | 50 | 75 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 133 | 338 | 438 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 196 | 0 | 7 | 19.0 | 26 | 109 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 147 | 0 | 7 | 20.8 | 20 | 77 | 225 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4470 | 0 | 60 | 451.5 | 261 | 865 | 1004 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 449 | 0 | 14 | 51.2 | 67 | 199 | 322 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1111 | 1390 | 90 | 60.9 | 689 | 2349 | 2604 | 0 | 123 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 71 | 267 | 357 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 136 | 0 | 14 | 28.7 | 27 | 98 | 198 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 98 | 0 | 30 | 56.2 | 16 | 71 | 123 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 641 | 0 | 14 | 96.6 | 37 | 137 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 916 | 260 | 60 | 74.8 | 253 | 1000 | 1258 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 335 | 0 | 45 | 62.0 | 85 | 334 | 447 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 366 | 0 | 14 | 22.7 | 117 | 359 | 585 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 421 | 0 | 30 | 79.9 | 60 | 224 | 334 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 45 | 0 | 7 | 16.4 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 28 | 0 | 7 | 35.0 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 220 | 866 | 1088 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3533 | 0 | 90 | 705.0 | 155 | 612 | 717 | 0 | — |
| ITEM-0074 | C - Slow Moving | Reorder | 40 | 0 | 14 | 19.8 | 10 | 41 | 101 | 61 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 56 | 0 | 45 | 63.8 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 360 | 0 | 7 | 147.3 | 7 | 27 | 100 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 364 | 540 | 45 | 30.8 | 186 | 730 | 978 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 562 | 0 | 45 | 251.6 | 27 | 130 | 197 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 429 | 558 | 90 | 60.4 | 218 | 865 | 1014 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 121 | 0 | 7 | 10.8 | 27 | 117 | 351 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 987 | 0 | 14 | 90.1 | 64 | 229 | 459 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 68 | 337 | 60 | 24.6 | 59 | 228 | 286 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 32 | 0 | 14 | 26.4 | 7 | 26 | 62 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 324 | 0 | 45 | 76.7 | 52 | 247 | 373 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 40.2 | 354 | 616 | 983 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 56 | 50 | 30 | 37.3 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 833 | 735 | 90 | 65.0 | 390 | 1556 | 1825 | 0 | 100 |
| ITEM-0093 | B - Core Products | Healthy | 141 | 435 | 7 | 6.6 | 283 | 455 | 905 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 109 | 0 | 7 | 20.8 | 16 | 58 | 169 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7105 | 0 | 90 | 393.0 | 687 | 2333 | 2586 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3862 | 0 | 60 | 281.4 | 353 | 1191 | 1383 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 32.8 | 100 | 153 | 290 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 160 | 0 | 7 | 24.0 | 22 | 76 | 216 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 178 | 0 | 14 | 45.3 | 25 | 84 | 167 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 626 | 1045 | 60 | 46.6 | 661 | 1481 | 1669 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 26 | 210 | 45 | 12.2 | 27 | 126 | 190 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 74.1 | 417 | 1265 | 1460 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 483 | 0 | 45 | 63.4 | 120 | 471 | 631 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1166 | 1041 | 90 | 69.8 | 637 | 2158 | 2392 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 353 | 740 | 60 | 31.3 | 232 | 920 | 1156 | 0 | 75 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 1 | 1100 | 90 | 0.1 | 271 | 1078 | 1265 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1896 | 0 | 90 | 136.6 | 528 | 1791 | 1986 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 691 | 902 | 60 | 39.2 | 453 | 1530 | 1777 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 470 | 1395 | 45 | 33.2 | 719 | 1371 | 1569 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 11 | 45 | 14 | 7.7 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 87 | 131 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 169 | 667 | 782 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 282 | 0 | 30 | 48.5 | 63 | 244 | 366 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 66 | 59 | 30 | 34.5 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 273 | 0 | 7 | 20.3 | 35 | 143 | 425 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 86.4 | 163 | 315 | 385 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 182 | 0 | 14 | 95.2 | 63 | 92 | 132 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 247 | 0 | 14 | 24.8 | 58 | 208 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 48 | 126 | 7 | 8.1 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 132.7 | 394 | 656 | 774 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 142 | 560 | 750 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 84.9 | 713 | 1937 | 2219 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 637 | 0 | 14 | 107.2 | 33 | 123 | 247 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 340 | 0 | 60 | 78.9 | 69 | 332 | 462 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 27 | 124 | 155 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3933 | 0 | 60 | 282.7 | 358 | 1207 | 1402 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 102 | 0 | 45 | 116.2 | 26 | 67 | 93 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 488 | 0 | 14 | 53.2 | 69 | 207 | 336 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 597 | 229 | 30 | 38.7 | 203 | 682 | 898 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1354 | 269 | 60 | 75.5 | 458 | 1552 | 1803 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2309 | 0 | 45 | 237.5 | 153 | 601 | 805 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 466 | 236 | 45 | 42.4 | 173 | 679 | 910 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 911 | 0 | 7 | 73.4 | 37 | 137 | 397 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 119 | 467 | 587 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 171 | 636 | 90 | 42.6 | 124 | 490 | 574 | 0 | 43 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 51.2 | 323 | 559 | 888 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 689 | 0 | 60 | 152.4 | 96 | 372 | 467 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 30 | 200 | 60 | 19.0 | 27 | 124 | 171 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 636 | 0 | 14 | 90.4 | 42 | 148 | 296 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 688 | 266 | 30 | 38.2 | 238 | 798 | 1050 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
