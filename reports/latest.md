# Synthetic Inventory Health

**Simulation date: 2026-10-05**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 85 |
| Lead-time risk | 11 |
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
| ITEM-0001 | B - Core Products | Healthy | 654 | 0 | 30 | 52.2 | 133 | 522 | 785 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 601 | 968 | 60 | 38.6 | 399 | 1350 | 1569 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1951 | 0 | 45 | 372.0 | 85 | 327 | 437 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 117 | 160 | 14 | 15.4 | 43 | 157 | 317 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 161 | 0 | 14 | 22.6 | 43 | 150 | 299 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 37 | 198 | 60 | 23.3 | 27 | 124 | 172 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 114 | 410 | 90 | 47.9 | 74 | 291 | 341 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 10.8 | 670 | 1295 | 1439 | 0 | 11 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 369 | 0 | 90 | 127.7 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 919 | 0 | 7 | 72.2 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Healthy | 497 | 0 | 45 | 74.3 | 105 | 413 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1157 | 0 | 30 | 296.7 | 45 | 166 | 248 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2978 | 0 | 60 | 289.8 | 213 | 840 | 1056 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 258 | 0 | 14 | 34.3 | 46 | 159 | 317 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 566 | 0 | 60 | 463.1 | 21 | 96 | 133 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 611 | 2071 | 2295 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 46 | 0 | 30 | 81.2 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 223 | 0 | 30 | 86.5 | 29 | 109 | 164 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 249 | 960 | 90 | 39.7 | 196 | 768 | 900 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1266 | 0 | 14 | 205.3 | 37 | 130 | 259 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 355 | 0 | 60 | 82.8 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 350 | 0 | 45 | 89.5 | 64 | 244 | 327 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 103 | 245 | 14 | 8.7 | 66 | 243 | 491 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 144 | 0 | 14 | 28.7 | 31 | 107 | 212 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 391 | 0 | 30 | 47.6 | 88 | 343 | 515 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 451 | 290 | 30 | 31.3 | 155 | 603 | 905 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4502 | 0 | 60 | 510.9 | 230 | 768 | 891 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 25.2 | 333 | 537 | 727 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 151 | 0 | 14 | 24.8 | 39 | 131 | 258 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 731 | 0 | 45 | 213.6 | 42 | 200 | 303 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 365 | 115 | 90 | 131.9 | 120 | 372 | 455 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 25 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 55.0 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 9 | 80 | 45 | 10.5 | 12 | 52 | 78 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 113 | 275 | 354 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 253 | 0 | 7 | 25.1 | 25 | 106 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 177 | 0 | 7 | 25.3 | 20 | 76 | 223 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4498 | 0 | 60 | 445.3 | 266 | 883 | 1024 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 476 | 0 | 14 | 51.9 | 71 | 209 | 338 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1163 | 1390 | 90 | 62.2 | 707 | 2410 | 2672 | 0 | 123 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 74 | 278 | 372 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 38 | 110 | 14 | 7.8 | 28 | 102 | 204 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 106 | 0 | 30 | 58.5 | 17 | 74 | 128 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 660 | 0 | 14 | 98.8 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 948 | 260 | 60 | 75.6 | 259 | 1024 | 1287 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 359 | 0 | 45 | 66.2 | 85 | 335 | 449 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 443 | 0 | 14 | 27.7 | 117 | 358 | 582 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 436 | 0 | 30 | 79.0 | 64 | 236 | 352 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 55 | 0 | 7 | 19.6 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 31 | 0 | 7 | 39.9 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 221 | 871 | 1094 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3544 | 0 | 90 | 675.8 | 162 | 640 | 750 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 45 | 0 | 14 | 21.8 | 10 | 41 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 61 | 0 | 45 | 70.4 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 364 | 0 | 7 | 141.2 | 7 | 28 | 105 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 398 | 540 | 45 | 33.3 | 188 | 738 | 989 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 568 | 0 | 45 | 248.2 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 473 | 393 | 90 | 68.7 | 211 | 838 | 983 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 168 | 0 | 7 | 15.1 | 27 | 117 | 351 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1030 | 0 | 14 | 94.4 | 64 | 228 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 79 | 337 | 60 | 28.0 | 60 | 233 | 292 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 64.1 | 215 | 334 | 499 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 35 | 0 | 14 | 28.4 | 7 | 26 | 63 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 350 | 0 | 45 | 83.8 | 51 | 244 | 369 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 113 | 702 | 14 | 7.7 | 315 | 536 | 846 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 62 | 0 | 30 | 41.0 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 873 | 735 | 90 | 66.1 | 402 | 1604 | 1881 | 0 | 100 |
| ITEM-0093 | B - Core Products | Healthy | 378 | 435 | 7 | 19.9 | 261 | 413 | 812 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 123 | 0 | 7 | 22.4 | 17 | 61 | 177 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7161 | 0 | 90 | 391.1 | 695 | 2362 | 2618 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3902 | 0 | 60 | 284.1 | 352 | 1190 | 1382 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 172 | 0 | 7 | 24.5 | 22 | 79 | 226 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 188 | 0 | 14 | 45.4 | 26 | 89 | 176 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 34 | 210 | 45 | 15.4 | 28 | 130 | 197 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 522 | 0 | 45 | 69.9 | 118 | 462 | 619 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1221 | 1041 | 90 | 72.6 | 639 | 2169 | 2405 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 402 | 740 | 60 | 35.8 | 231 | 916 | 1152 | 0 | 79 |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 25 | 1100 | 90 | 2.8 | 272 | 1084 | 1272 | 0 | 3 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1954 | 0 | 90 | 139.9 | 532 | 1803 | 1999 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 745 | 902 | 60 | 41.7 | 459 | 1549 | 1799 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 17 | 45 | 14 | 11.9 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 130 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 16 | 648 | 90 | 3.0 | 167 | 658 | 771 | 0 | 3 |
| ITEM-0119 | B - Core Products | Healthy | 311 | 0 | 30 | 53.7 | 62 | 242 | 364 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 73 | 59 | 30 | 37.3 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 313 | 0 | 7 | 23.3 | 36 | 144 | 427 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 86.4 | 163 | 315 | 385 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 295 | 0 | 14 | 29.9 | 57 | 205 | 412 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 75 | 0 | 7 | 12.5 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 131.8 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 138 | 548 | 735 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Reorder | 1142 | 697 | 90 | 75.7 | 773 | 2146 | 2462 | 623 | — |
| ITEM-0131 | B - Core Products | Excess | 661 | 0 | 14 | 111.2 | 34 | 124 | 248 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 351 | 0 | 60 | 79.2 | 71 | 342 | 475 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 26 | 119 | 149 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4005 | 0 | 60 | 294.2 | 350 | 1181 | 1371 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 513 | 0 | 14 | 52.5 | 75 | 222 | 359 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 430 | 456 | 30 | 27.8 | 203 | 682 | 898 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1429 | 269 | 60 | 80.6 | 454 | 1536 | 1784 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2336 | 0 | 45 | 235.4 | 155 | 612 | 820 | 0 | — |
| ITEM-0142 | B - Core Products | Lead-time risk | 180 | 1680 | 60 | 14.3 | 552 | 1320 | 1584 | 0 | 15 |
| ITEM-0143 | B - Core Products | Healthy | 512 | 236 | 45 | 46.6 | 172 | 678 | 909 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 947 | 0 | 7 | 74.8 | 38 | 140 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 123 | 480 | 603 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 181 | 636 | 90 | 43.3 | 129 | 510 | 597 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 46.9 | 333 | 590 | 949 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 703 | 0 | 60 | 145.1 | 103 | 399 | 501 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 367.1 | 229 | 460 | 513 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 33 | 200 | 60 | 20.1 | 28 | 129 | 178 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 662 | 0 | 14 | 95.0 | 41 | 146 | 292 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 757 | 266 | 30 | 42.1 | 237 | 794 | 1046 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 26.6 | 301 | 487 | 812 | 0 | — |
