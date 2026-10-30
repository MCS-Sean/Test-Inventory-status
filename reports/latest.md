# Synthetic Inventory Health

**Simulation date: 2026-10-30**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 95 |
| Lead-time risk | 2 |
| Reorder | 1 |
| Stockout | 10 |

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
| ITEM-0001 | B - Core Products | Healthy | 302 | 291 | 30 | 22.9 | 139 | 548 | 825 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 286 | 0 | 7 | 43.9 | 92 | 145 | 281 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 474 | 890 | 60 | 30.6 | 397 | 1343 | 1560 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1860 | 0 | 45 | 452.4 | 66 | 256 | 342 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 112 | 155 | 14 | 15.8 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 109 | 0 | 45 | 71.6 | 19 | 90 | 135 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 177 | 0 | 14 | 30.6 | 34 | 121 | 242 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 199 | 0 | 60 | 155.7 | 22 | 100 | 139 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 71 | 410 | 90 | 38.0 | 58 | 228 | 268 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 300 | 90 | 90 | 105.5 | 68 | 327 | 413 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 568 | 0 | 7 | 43.0 | 34 | 140 | 418 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 343 | 155 | 45 | 51.2 | 105 | 414 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1095 | 0 | 30 | 366.4 | 34 | 127 | 190 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2727 | 0 | 60 | 262.5 | 215 | 849 | 1067 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 137 | 0 | 14 | 23.7 | 34 | 121 | 243 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 550 | 0 | 60 | 575.6 | 18 | 77 | 105 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 586 | 1986 | 2201 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 29 | 0 | 30 | 51.2 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 411 | 1169 | 60 | 39.3 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 180 | 0 | 30 | 87.1 | 18 | 83 | 145 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 128 | 960 | 90 | 26.1 | 150 | 597 | 701 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1170 | 0 | 14 | 243.8 | 29 | 101 | 202 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 250 | 135 | 60 | 58.3 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 274 | 0 | 45 | 87.4 | 50 | 195 | 260 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 677 | 0 | 60 | 662.3 | 49 | 112 | 143 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 338 | 0 | 14 | 29.1 | 67 | 242 | 485 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 32.8 | 116 | 176 | 333 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 58 | 95 | 14 | 14.4 | 25 | 86 | 171 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 202 | 172 | 30 | 24.0 | 90 | 352 | 528 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 361 | 315 | 30 | 24.4 | 157 | 616 | 927 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4338 | 0 | 60 | 606.2 | 184 | 621 | 721 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 50.4 | 251 | 433 | 686 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 165 | 0 | 14 | 35.9 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 651 | 0 | 45 | 195.3 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 287 | 220 | 90 | 91.6 | 130 | 416 | 510 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Stockout | 0 | 965 | 60 | 0.0 | 242 | 755 | 1007 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 72 | 0 | 45 | 101.2 | 11 | 44 | 66 | 0 | — |
| ITEM-0051 | B - Core Products | Reorder | 185 | 263 | 60 | 33.7 | 236 | 571 | 687 | 239 | — |
| ITEM-0052 | B - Core Products | Healthy | 221 | 0 | 7 | 21.4 | 23 | 106 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 137 | 0 | 7 | 18.5 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4322 | 0 | 60 | 558.1 | 201 | 674 | 782 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 309 | 0 | 14 | 42.7 | 53 | 162 | 264 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 742 | 1680 | 90 | 40.6 | 690 | 2353 | 2608 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 505 | 0 | 45 | 138.1 | 58 | 227 | 303 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 16 | 110 | 14 | 3.2 | 28 | 103 | 208 | 0 | 4 |
| ITEM-0062 | C - Slow Moving | Healthy | 69 | 0 | 30 | 47.4 | 13 | 59 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 517 | 0 | 14 | 79.5 | 37 | 135 | 271 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 312 | 310 | 60 | 53.2 | 235 | 593 | 717 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 681 | 525 | 60 | 56.9 | 248 | 979 | 1231 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 205 | 246 | 45 | 36.8 | 88 | 345 | 462 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 266 | 245 | 14 | 16.3 | 119 | 364 | 593 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 343 | 0 | 30 | 81.7 | 47 | 178 | 266 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 76 | 0 | 7 | 27.1 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 206 | 146 | 45 | 58.3 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 19 | 0 | 7 | 26.3 | 3 | 9 | 31 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 229 | 903 | 1134 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3449 | 0 | 90 | 810.5 | 130 | 518 | 607 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 58 | 0 | 14 | 28.4 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 34 | 26 | 45 | 37.8 | 13 | 55 | 82 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 323 | 0 | 7 | 165.2 | 5 | 21 | 80 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 108 | 290 | 90 | 58.9 | 94 | 261 | 316 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 386 | 515 | 45 | 33.7 | 179 | 706 | 946 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 513 | 0 | 45 | 229.7 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 299 | 558 | 90 | 43.2 | 213 | 843 | 989 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 137 | 0 | 7 | 11.9 | 28 | 120 | 362 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 746 | 0 | 14 | 66.6 | 65 | 233 | 469 | 0 | — |
| ITEM-0084 | B - Core Products | Excess | 359 | 0 | 60 | 156.1 | 49 | 190 | 238 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 12 | 35 | 14 | 11.7 | 6 | 22 | 52 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 224 | 135 | 45 | 50.8 | 54 | 257 | 390 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 24 | 50 | 30 | 16.4 | 13 | 59 | 103 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 604 | 1027 | 90 | 48.9 | 376 | 1500 | 1759 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 113 | 485 | 7 | 6.2 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 113 | 0 | 7 | 23.8 | 13 | 52 | 151 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6714 | 0 | 90 | 366.4 | 694 | 2362 | 2618 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3566 | 0 | 60 | 259.0 | 353 | 1193 | 1386 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 56.0 | 96 | 139 | 251 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 68 | 0 | 7 | 13.0 | 16 | 58 | 168 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 115 | 0 | 14 | 35.3 | 19 | 68 | 137 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 66.3 | 642 | 1428 | 1608 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 198 | 0 | 45 | 106.7 | 23 | 109 | 165 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 86.6 | 362 | 1054 | 1214 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 324 | 180 | 45 | 43.5 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 825 | 1542 | 90 | 48.9 | 642 | 2178 | 2415 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 371 | 738 | 60 | 33.4 | 228 | 906 | 1139 | 0 | 56 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1067 | 1252 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 151.4 | 106 | 311 | 412 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1526 | 445 | 90 | 108.7 | 539 | 1818 | 2014 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 298 | 1407 | 60 | 17.0 | 450 | 1520 | 1766 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 27 | 45 | 14 | 18.8 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 833 | 0 | 14 | 84.3 | 239 | 388 | 595 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 109 | 0 | 45 | 74.3 | 18 | 86 | 130 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 176 | 697 | 817 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 158 | 135 | 30 | 26.7 | 63 | 247 | 371 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 31 | 59 | 30 | 16.5 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 349 | 0 | 7 | 27.6 | 34 | 136 | 402 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 49 | 146 | 14 | 13.3 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 29 | 216 | 14 | 2.9 | 57 | 205 | 413 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 44 | 132 | 7 | 7.5 | 16 | 63 | 186 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 525 | 191 | 45 | 59.1 | 139 | 548 | 734 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 496 | 0 | 14 | 81.8 | 35 | 126 | 254 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 253 | 130 | 60 | 60.7 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 30 | 139 | 174 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3629 | 0 | 60 | 262.1 | 357 | 1202 | 1396 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 357 | 0 | 14 | 47.3 | 55 | 169 | 274 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 287 | 474 | 30 | 18.8 | 202 | 675 | 889 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 959 | 799 | 60 | 52.2 | 469 | 1591 | 1848 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2091 | 0 | 45 | 214.6 | 154 | 603 | 807 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 81.8 | 630 | 1509 | 1811 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 251 | 470 | 45 | 23.3 | 170 | 666 | 892 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 623 | 0 | 7 | 49.7 | 38 | 139 | 402 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 95 | 375 | 472 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 121 | 636 | 90 | 38.3 | 97 | 385 | 451 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 36.7 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 623 | 0 | 60 | 165.4 | 79 | 309 | 388 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 799 | 400 | 90 | 350.8 | 215 | 423 | 471 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 203 | 0 | 60 | 146.2 | 24 | 109 | 151 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 475 | 0 | 14 | 64.8 | 43 | 153 | 307 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 603 | 274 | 30 | 34.5 | 231 | 774 | 1019 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 17.2 | 286 | 436 | 699 | 0 | — |
