# Synthetic Inventory Health

**Simulation date: 2026-09-17**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 67 |
| Lead-time risk | 16 |
| Reorder | 2 |
| Stockout | 25 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 500 | 751 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 268 | 0 | 7 | 47.6 | 84 | 130 | 248 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 884 | 517 | 60 | 57.2 | 393 | 1336 | 1552 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2011 | 0 | 45 | 315.3 | 103 | 397 | 531 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 258 | 0 | 14 | 34.6 | 43 | 155 | 312 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 258 | 0 | 14 | 30.9 | 53 | 179 | 354 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 55 | 198 | 60 | 26.8 | 35 | 161 | 223 | 0 | 27 |
| ITEM-0010 | B - Core Products | Lead-time risk | 141 | 410 | 90 | 46.3 | 95 | 373 | 436 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 414 | 0 | 90 | 147.9 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1161 | 0 | 7 | 91.9 | 33 | 135 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 234.0 | 20 | 30 | 67 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 35 | 235 | 45 | 11.5 | 85 | 226 | 318 | 0 | 12 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1207 | 0 | 30 | 245.8 | 57 | 210 | 313 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3144 | 0 | 60 | 292.0 | 222 | 879 | 1105 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 347 | 0 | 14 | 37.7 | 56 | 195 | 388 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 584 | 0 | 60 | 410.6 | 24 | 111 | 154 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 635 | 2162 | 2397 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 8 | 45 | 30 | 11.2 | 8 | 31 | 52 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 28 | 124 | 216 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 312 | 960 | 90 | 39.1 | 248 | 975 | 1143 | 0 | 40 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1339 | 0 | 14 | 175.9 | 46 | 161 | 320 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 317 | 441 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 393 | 0 | 45 | 75.4 | 86 | 326 | 436 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 290.9 | 79 | 225 | 297 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 325 | 0 | 14 | 29.6 | 63 | 228 | 459 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 13.3 | 141 | 222 | 434 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 209 | 0 | 14 | 32.7 | 39 | 135 | 270 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 86 | 338 | 508 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 148 | 572 | 859 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4609 | 0 | 60 | 406.7 | 296 | 988 | 1146 | 0 | — |
| ITEM-0041 | A - Top Movers | Reorder | 522 | 0 | 14 | 39.1 | 327 | 527 | 714 | 195 | — |
| ITEM-0042 | B - Core Products | Healthy | 221 | 0 | 14 | 29.6 | 47 | 159 | 316 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 792 | 0 | 45 | 237.6 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 143 | 185 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 23 | 80 | 45 | 22.5 | 14 | 62 | 92 | 0 | 23 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 129 | 290 | 369 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 211 | 0 | 7 | 21.1 | 27 | 108 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 153 | 0 | 7 | 21.4 | 20 | 78 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4613 | 0 | 60 | 379.2 | 321 | 1064 | 1234 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 585 | 0 | 14 | 52.8 | 89 | 256 | 411 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1490 | 865 | 90 | 82.7 | 682 | 2323 | 2575 | 0 | 83 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 459 | 946 | 1275 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 91 | 342 | 457 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 127 | 0 | 14 | 25.6 | 29 | 104 | 208 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 124 | 0 | 30 | 53.1 | 21 | 94 | 164 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 783 | 0 | 14 | 118.4 | 38 | 138 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 518 | 310 | 60 | 73.1 | 272 | 705 | 854 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1203 | 0 | 60 | 100.3 | 248 | 980 | 1232 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 451 | 0 | 45 | 79.3 | 89 | 351 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 446 | 0 | 14 | 25.9 | 123 | 381 | 622 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 117 | 390 | 30 | 17.0 | 79 | 293 | 438 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 106 | 0 | 7 | 38.8 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 105 | 104 | 45 | 38.4 | 77 | 203 | 285 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 18 | 0 | 7 | 21.0 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 232 | 915 | 1150 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3608 | 0 | 90 | 554.1 | 203 | 796 | 933 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 81 | 0 | 14 | 37.6 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 389 | 0 | 7 | 129.7 | 8 | 32 | 122 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 579 | 275 | 45 | 46.7 | 195 | 766 | 1026 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 605 | 0 | 45 | 247.5 | 30 | 143 | 216 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 581 | 393 | 90 | 82.7 | 214 | 854 | 1001 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 141 | 0 | 7 | 12.8 | 29 | 118 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1219 | 0 | 14 | 113.2 | 63 | 225 | 451 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 112 | 337 | 60 | 30.9 | 77 | 298 | 375 | 0 | 31 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 46 | 0 | 14 | 28.8 | 9 | 33 | 81 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 271 | 364 | 0 | 1 |
| ITEM-0089 | B - Core Products | Healthy | 784 | 0 | 14 | 58.2 | 304 | 506 | 789 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 85 | 0 | 30 | 55.8 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1115 | 735 | 90 | 82.4 | 414 | 1646 | 1930 | 0 | 115 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 190 | 0 | 7 | 27.8 | 21 | 76 | 220 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7465 | 0 | 90 | 412.2 | 687 | 2336 | 2589 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4173 | 0 | 60 | 314.8 | 342 | 1151 | 1337 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 256 | 0 | 7 | 29.7 | 28 | 97 | 279 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 239 | 0 | 14 | 45.4 | 34 | 113 | 224 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 58 | 210 | 45 | 21.6 | 34 | 158 | 239 | 0 | 22 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 861 | 422 | 90 | 92.0 | 421 | 1273 | 1469 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 634 | 0 | 45 | 80.9 | 122 | 483 | 647 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1481 | 773 | 90 | 86.2 | 654 | 2219 | 2459 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 595 | 481 | 60 | 53.5 | 229 | 908 | 1142 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 190.9 | 65 | 157 | 245 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 189 | 915 | 90 | 21.1 | 274 | 1091 | 1280 | 0 | 22 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2203 | 0 | 90 | 148.6 | 564 | 1913 | 2121 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1063 | 622 | 60 | 59.9 | 455 | 1537 | 1785 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 29.6 | 829 | 1635 | 1880 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 40 | 0 | 14 | 27.9 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 72.5 | 267 | 475 | 766 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 124 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 119 | 648 | 90 | 22.1 | 166 | 657 | 770 | 0 | 23 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 256 | 385 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 54 | 55 | 30 | 28.8 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 249 | 0 | 7 | 18.8 | 36 | 143 | 421 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 63.6 | 94 | 139 | 202 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 232 | 0 | 14 | 22.7 | 59 | 213 | 427 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 40 | 134 | 7 | 6.4 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 16.1 | 412 | 703 | 833 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 138 | 545 | 730 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 758 | 0 | 14 | 124.5 | 34 | 126 | 254 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 430 | 0 | 60 | 97.7 | 71 | 340 | 472 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4244 | 0 | 60 | 314.4 | 347 | 1171 | 1360 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 28 | 79 | 111 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 656 | 0 | 14 | 57.3 | 89 | 261 | 421 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 201 | 675 | 889 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1707 | 0 | 60 | 93.6 | 466 | 1579 | 1834 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2516 | 0 | 45 | 254.4 | 155 | 610 | 818 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 628 | 1542 | 1857 | 0 | 1 |
| ITEM-0143 | B - Core Products | Reorder | 439 | 243 | 45 | 39.5 | 173 | 685 | 918 | 236 | — |
| ITEM-0144 | B - Core Products | Excess | 1142 | 0 | 7 | 87.5 | 38 | 143 | 417 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 155 | 602 | 756 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 228 | 636 | 90 | 43.4 | 162 | 641 | 751 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 802 | 0 | 14 | 37.6 | 444 | 765 | 1063 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 137.8 | 230 | 395 | 625 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 581 | 178 | 60 | 97.6 | 127 | 491 | 616 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 58 | 200 | 60 | 28.7 | 34 | 158 | 219 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 800 | 0 | 14 | 115.8 | 41 | 145 | 290 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 242 | 805 | 1059 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 597 | 0 | 7 | 24.0 | 324 | 524 | 872 | 0 | — |
