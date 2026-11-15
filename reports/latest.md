# Synthetic Inventory Health

**Simulation date: 2026-11-15**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 97 |
| Lead-time risk | 5 |
| Reorder | 2 |
| Stockout | 8 |

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
| ITEM-0001 | B - Core Products | Healthy | 422 | 302 | 30 | 32.5 | 137 | 540 | 812 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 107 | 190 | 7 | 15.5 | 94 | 150 | 294 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 482 | 884 | 60 | 31.7 | 390 | 1319 | 1532 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1796 | 0 | 45 | 471.3 | 60 | 236 | 316 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 167 | 0 | 14 | 24.8 | 40 | 141 | 283 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 84 | 46 | 45 | 56.8 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 63 | 125 | 14 | 11.1 | 41 | 127 | 206 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 178 | 0 | 60 | 138.1 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 446 | 0 | 90 | 238.9 | 58 | 228 | 268 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1308 | 0 | 7 | 131.1 | 261 | 341 | 481 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 260 | 90 | 90 | 97.9 | 63 | 305 | 385 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 363 | 0 | 7 | 28.0 | 33 | 137 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 232 | 300 | 45 | 35.4 | 103 | 405 | 542 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1040 | 0 | 30 | 374.4 | 32 | 119 | 177 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2569 | 0 | 60 | 245.7 | 217 | 855 | 1075 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 31 | 120 | 14 | 5.6 | 32 | 115 | 232 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 531 | 0 | 60 | 582.8 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 594 | 2004 | 2221 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 20 | 20 | 30 | 38.3 | 6 | 23 | 38 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 153 | 0 | 30 | 82.0 | 16 | 74 | 130 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1005 | 0 | 90 | 206.0 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 4 | 30 | 7 | 6.3 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1077 | 0 | 14 | 229.7 | 28 | 99 | 197 | 0 | — |
| ITEM-0032 | C - Slow Moving | Reorder | 190 | 135 | 60 | 45.0 | 68 | 326 | 453 | 130 | — |
| ITEM-0033 | B - Core Products | Healthy | 225 | 0 | 45 | 76.1 | 48 | 184 | 247 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 155 | 245 | 14 | 13.5 | 66 | 239 | 481 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 21.2 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 89 | 0 | 14 | 23.8 | 22 | 79 | 157 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 53 | 355 | 30 | 6.2 | 91 | 356 | 535 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 471 | 315 | 30 | 31.7 | 157 | 619 | 931 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4219 | 0 | 60 | 621.5 | 174 | 589 | 684 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 351 | 335 | 14 | 27.4 | 313 | 506 | 685 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 84 | 100 | 14 | 18.0 | 27 | 97 | 195 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 605 | 0 | 45 | 187.8 | 40 | 189 | 285 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 57.8 | 138 | 452 | 555 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 63 | 0 | 45 | 96.1 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 150 | 502 | 60 | 25.5 | 242 | 601 | 724 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 84 | 210 | 7 | 8.5 | 23 | 102 | 310 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 183 | 0 | 7 | 25.3 | 19 | 77 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4148 | 0 | 60 | 528.0 | 201 | 681 | 791 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 190 | 0 | 14 | 27.9 | 50 | 153 | 248 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 507 | 1950 | 90 | 29.0 | 664 | 2255 | 2500 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1018 | 0 | 30 | 80.2 | 439 | 833 | 1100 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 437 | 0 | 45 | 123.3 | 56 | 220 | 294 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 58 | 105 | 14 | 11.4 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 40 | 43 | 30 | 27.3 | 14 | 60 | 104 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 427 | 0 | 14 | 69.0 | 36 | 129 | 259 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 67.4 | 179 | 426 | 510 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 441 | 790 | 60 | 36.0 | 253 | 1001 | 1258 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 109 | 246 | 45 | 19.6 | 88 | 345 | 461 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 248 | 245 | 14 | 15.0 | 121 | 370 | 601 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 257 | 0 | 30 | 62.2 | 45 | 174 | 260 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 37 | 0 | 7 | 13.8 | 6 | 28 | 108 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 10 | 0 | 7 | 15.0 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 865 | 249 | 60 | 76.9 | 234 | 920 | 1157 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3383 | 0 | 90 | 862.5 | 120 | 477 | 560 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 25 | 60 | 14 | 12.6 | 9 | 39 | 99 | 0 | 13 |
| ITEM-0075 | C - Slow Moving | Healthy | 22 | 54 | 45 | 25.1 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 477 | 1186 | 1350 | 260 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 291 | 0 | 7 | 161.7 | 5 | 20 | 74 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 140 | 430 | 525 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 212 | 515 | 45 | 19.3 | 172 | 677 | 907 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 469 | 0 | 45 | 204.9 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 339 | 547 | 90 | 48.7 | 215 | 848 | 995 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 208 | 0 | 7 | 18.4 | 29 | 120 | 358 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 616 | 0 | 14 | 58.7 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 307 | 0 | 60 | 129.1 | 50 | 196 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 27 | 0 | 14 | 27.6 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 136 | 135 | 45 | 30.3 | 56 | 263 | 398 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 974 | 0 | 14 | 52.4 | 367 | 646 | 1037 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 51 | 45 | 30 | 34.3 | 13 | 60 | 104 | 0 | 35 |
| ITEM-0092 | B - Core Products | Healthy | 424 | 1289 | 90 | 34.2 | 377 | 1506 | 1766 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 743 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 38 | 99 | 7 | 8.5 | 12 | 48 | 142 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6436 | 0 | 90 | 356.2 | 683 | 2328 | 2580 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3335 | 0 | 60 | 240.9 | 356 | 1201 | 1395 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 96 | 0 | 7 | 19.9 | 13 | 52 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 73 | 0 | 14 | 24.7 | 17 | 62 | 124 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 161 | 0 | 45 | 91.1 | 22 | 104 | 157 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 87.0 | 314 | 894 | 1028 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 201 | 340 | 45 | 27.2 | 117 | 457 | 612 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1098 | 1265 | 90 | 66.5 | 631 | 2135 | 2366 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 451 | 498 | 60 | 40.7 | 227 | 903 | 1136 | 0 | 41 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 225.2 | 56 | 122 | 186 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 260 | 1036 | 1215 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 184.4 | 93 | 262 | 344 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1292 | 665 | 90 | 87.8 | 561 | 1901 | 2107 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 384 | 1292 | 60 | 22.4 | 440 | 1487 | 1727 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 53 | 0 | 14 | 38.8 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 153.6 | 144 | 218 | 320 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 84 | 50 | 45 | 55.2 | 19 | 90 | 135 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 178 | 705 | 827 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 185 | 125 | 30 | 30.8 | 65 | 252 | 378 | 0 | 31 |
| ITEM-0120 | C - Slow Moving | Healthy | 55 | 58 | 30 | 28.4 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 160 | 0 | 7 | 13.4 | 31 | 127 | 379 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 41.8 | 82 | 142 | 262 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 314 | 0 | 14 | 33.0 | 55 | 198 | 398 | 0 | — |
| ITEM-0125 | B - Core Products | Reorder | 63 | 0 | 7 | 10.2 | 17 | 67 | 196 | 133 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 211.2 | 275 | 408 | 467 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 397 | 191 | 45 | 44.9 | 138 | 545 | 730 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 118.4 | 618 | 1566 | 1785 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 407 | 0 | 14 | 67.3 | 35 | 126 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 196 | 130 | 60 | 48.2 | 66 | 315 | 437 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3439 | 0 | 60 | 252.9 | 349 | 1179 | 1369 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 54.2 | 28 | 76 | 107 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 206 | 0 | 14 | 28.9 | 51 | 158 | 258 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 549 | 238 | 30 | 36.1 | 202 | 674 | 887 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 883 | 799 | 60 | 47.1 | 477 | 1621 | 1883 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1910 | 0 | 45 | 191.2 | 157 | 617 | 827 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 320 | 463 | 45 | 30.3 | 167 | 653 | 875 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 440 | 0 | 7 | 35.6 | 36 | 135 | 394 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 825 | 0 | 60 | 187.0 | 91 | 361 | 453 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 75 | 636 | 90 | 26.3 | 88 | 348 | 408 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 776 | 0 | 14 | 63.4 | 242 | 426 | 683 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 561 | 0 | 60 | 161.3 | 73 | 286 | 359 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 176 | 0 | 60 | 129.8 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 357 | 0 | 14 | 49.1 | 42 | 152 | 304 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 589 | 259 | 30 | 33.4 | 233 | 779 | 1026 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 701 | 0 | 7 | 31.6 | 322 | 500 | 810 | 0 | — |
