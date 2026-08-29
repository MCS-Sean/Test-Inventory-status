# Synthetic Inventory Health

**Simulation date: 2026-08-29**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 52 |
| Lead-time risk | 51 |
| Reorder | 2 |
| Stockout | 5 |

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
| ITEM-0001 | B - Core Products | Lead-time risk | 32 | 728 | 30 | 2.7 | 129 | 503 | 755 | 0 | 3 |
| ITEM-0002 | B - Core Products | Healthy | 182 | 0 | 7 | 28.0 | 96 | 149 | 285 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1171 | 294 | 60 | 79.4 | 377 | 1277 | 1483 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2087 | 0 | 45 | 266.8 | 126 | 486 | 651 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 391 | 0 | 14 | 52.6 | 43 | 155 | 311 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 5 | 142 | 45 | 3.0 | 21 | 99 | 150 | 0 | 3 |
| ITEM-0008 | B - Core Products | Healthy | 361 | 0 | 14 | 33.6 | 68 | 230 | 455 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 80 | 198 | 60 | 31.0 | 43 | 201 | 278 | 0 | 32 |
| ITEM-0010 | B - Core Products | Lead-time risk | 176 | 410 | 90 | 43.2 | 128 | 500 | 585 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2206 | 0 | 7 | 139.8 | 303 | 430 | 651 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 464 | 0 | 90 | 161.2 | 68 | 330 | 417 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1401 | 0 | 7 | 108.5 | 34 | 138 | 409 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 111.9 | 28 | 49 | 126 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 23 | 510 | 45 | 3.4 | 106 | 419 | 561 | 0 | 4 |
| ITEM-0018 | B - Core Products | Excess | 1257 | 0 | 30 | 209.1 | 67 | 254 | 380 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3366 | 0 | 60 | 325.7 | 214 | 845 | 1062 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 130 | 323 | 14 | 11.9 | 65 | 229 | 459 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 599 | 0 | 60 | 332.8 | 30 | 140 | 194 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 146 | 2305 | 90 | 8.4 | 663 | 2254 | 2499 | 0 | 9 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 14 | 45 | 30 | 18.8 | 8 | 32 | 54 | 0 | 19 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 87.4 | 685 | 1496 | 1775 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 12 | 243 | 30 | 3.2 | 33 | 148 | 259 | 0 | 4 |
| ITEM-0029 | B - Core Products | Lead-time risk | 414 | 960 | 90 | 43.8 | 292 | 1152 | 1350 | 0 | 44 |
| ITEM-0030 | C - Slow Moving | Lead-time risk | 2 | 35 | 7 | 3.5 | 7 | 12 | 29 | 0 | 4 |
| ITEM-0031 | B - Core Products | Excess | 1423 | 0 | 14 | 142.1 | 60 | 211 | 421 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 21 | 395 | 60 | 5.4 | 64 | 304 | 421 | 0 | 6 |
| ITEM-0033 | B - Core Products | Healthy | 448 | 0 | 45 | 66.4 | 111 | 422 | 563 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 536 | 0 | 14 | 47.9 | 64 | 232 | 467 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 277 | 0 | 14 | 34.8 | 47 | 167 | 334 | 0 | — |
| ITEM-0038 | B - Core Products | Lead-time risk | 10 | 484 | 30 | 1.2 | 87 | 340 | 511 | 0 | 2 |
| ITEM-0039 | B - Core Products | Lead-time risk | 218 | 575 | 30 | 16.3 | 145 | 561 | 842 | 0 | 17 |
| ITEM-0040 | A - Top Movers | Excess | 4741 | 0 | 60 | 339.2 | 362 | 1215 | 1411 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 37.3 | 376 | 642 | 889 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 315 | 0 | 14 | 33.9 | 58 | 198 | 393 | 0 | — |
| ITEM-0043 | B - Core Products | Lead-time risk | 87 | 1270 | 90 | 11.2 | 480 | 1190 | 1354 | 0 | 12 |
| ITEM-0044 | C - Slow Moving | Excess | 860 | 0 | 45 | 261.5 | 40 | 192 | 290 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 474 | 0 | 90 | 166.6 | 119 | 378 | 464 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 45 | 192 | 60 | 26.0 | 79 | 185 | 237 | 0 | 26 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 34 | 80 | 45 | 26.8 | 17 | 76 | 114 | 0 | 27 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 62 | 224 | 60 | 42.0 | 102 | 193 | 237 | 0 | 42 |
| ITEM-0052 | B - Core Products | Healthy | 407 | 0 | 7 | 39.9 | 28 | 110 | 324 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 286 | 0 | 7 | 38.3 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4762 | 0 | 60 | 324.4 | 384 | 1280 | 1485 | 0 | — |
| ITEM-0055 | A - Top Movers | Excess | 725 | 0 | 14 | 55.3 | 102 | 299 | 483 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1877 | 580 | 90 | 107.6 | 661 | 2249 | 2493 | 0 | 108 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 379 | 765 | 1027 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 35 | 564 | 45 | 4.8 | 119 | 452 | 603 | 0 | 5 |
| ITEM-0061 | B - Core Products | Lead-time risk | 58 | 145 | 14 | 12.0 | 29 | 102 | 204 | 0 | 12 |
| ITEM-0062 | C - Slow Moving | Healthy | 153 | 0 | 30 | 51.4 | 26 | 119 | 208 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 901 | 0 | 14 | 135.6 | 37 | 137 | 277 | 0 | — |
| ITEM-0064 | B - Core Products | Lead-time risk | 595 | 310 | 60 | 77.9 | 279 | 745 | 905 | 0 | 78 |
| ITEM-0065 | B - Core Products | Healthy | 1441 | 0 | 60 | 122.0 | 244 | 965 | 1213 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 562 | 0 | 45 | 98.2 | 90 | 354 | 474 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 816 | 0 | 14 | 48.7 | 122 | 374 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 176 | 390 | 30 | 19.9 | 98 | 373 | 559 | 0 | 20 |
| ITEM-0069 | C - Slow Moving | Healthy | 66 | 0 | 7 | 22.9 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 172 | 104 | 45 | 66.4 | 79 | 199 | 276 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 35 | 0 | 7 | 40.9 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 56 | 1070 | 60 | 5.0 | 234 | 921 | 1157 | 0 | 5 |
| ITEM-0073 | B - Core Products | Excess | 3677 | 0 | 90 | 455.8 | 250 | 985 | 1154 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 4 | 99 | 14 | 1.9 | 10 | 42 | 106 | 0 | 2 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 3 | 66 | 45 | 3.9 | 11 | 47 | 70 | 0 | 4 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 52.7 | 223 | 453 | 506 | 0 | 53 |
| ITEM-0077 | C - Slow Moving | Excess | 425 | 0 | 7 | 113.8 | 9 | 39 | 151 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 796 | 0 | 45 | 63.3 | 196 | 775 | 1038 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 647 | 0 | 45 | 261.1 | 31 | 145 | 220 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 726 | 235 | 90 | 107.1 | 206 | 823 | 966 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 29 | 112 | 329 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1444 | 0 | 14 | 136.4 | 62 | 221 | 444 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 151 | 337 | 60 | 32.5 | 99 | 383 | 480 | 0 | 33 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 331 | 488 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 66 | 0 | 14 | 34.3 | 10 | 39 | 97 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 20 | 365 | 45 | 4.3 | 73 | 289 | 388 | 0 | 5 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 110 | 0 | 30 | 68.8 | 14 | 64 | 112 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1357 | 436 | 90 | 105.1 | 397 | 1572 | 1844 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 29.9 | 242 | 375 | 723 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 12 | 262 | 7 | 1.4 | 28 | 96 | 275 | 0 | 2 |
| ITEM-0095 | A - Top Movers | Excess | 7830 | 0 | 90 | 438.0 | 681 | 2308 | 2559 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4443 | 0 | 60 | 327.5 | 351 | 1179 | 1369 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 11.2 | 110 | 169 | 323 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 8 | 330 | 7 | 0.7 | 34 | 121 | 348 | 0 | 1 |
| ITEM-0100 | B - Core Products | Lead-time risk | 14 | 256 | 14 | 2.2 | 39 | 135 | 269 | 0 | 3 |
| ITEM-0101 | B - Core Products | Healthy | 1204 | 420 | 60 | 85.0 | 571 | 1436 | 1733 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 87 | 210 | 45 | 26.5 | 41 | 193 | 291 | 0 | 27 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 772 | 0 | 45 | 96.0 | 125 | 496 | 664 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1863 | 524 | 90 | 110.0 | 647 | 2188 | 2425 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 834 | 241 | 60 | 78.6 | 221 | 869 | 1092 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 610 | 0 | 30 | 196.1 | 67 | 164 | 257 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 356 | 915 | 90 | 38.9 | 280 | 1114 | 1306 | 0 | 39 |
| ITEM-0110 | C - Slow Moving | Excess | 756 | 0 | 60 | 324.0 | 96 | 239 | 309 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2429 | 0 | 90 | 163.6 | 563 | 1914 | 2122 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1434 | 360 | 60 | 79.9 | 461 | 1556 | 1807 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1095 | 635 | 45 | 70.8 | 801 | 1512 | 1729 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 17 | 55 | 14 | 11.7 | 8 | 30 | 74 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1023 | 0 | 14 | 55.5 | 314 | 591 | 978 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 6 | 115 | 45 | 4.5 | 17 | 79 | 120 | 0 | 5 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 224 | 530 | 90 | 42.0 | 164 | 650 | 762 | 0 | 43 |
| ITEM-0119 | B - Core Products | Lead-time risk | 21 | 355 | 30 | 3.5 | 65 | 254 | 382 | 0 | 4 |
| ITEM-0120 | C - Slow Moving | Healthy | 89 | 0 | 30 | 47.1 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 498 | 0 | 7 | 38.2 | 37 | 142 | 415 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 4.1 | 102 | 157 | 233 | 0 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 116 | 292 | 14 | 11.3 | 59 | 214 | 430 | 0 | 12 |
| ITEM-0125 | B - Core Products | Healthy | 165 | 0 | 7 | 26.7 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 295 | 790 | 30 | 24.7 | 496 | 867 | 1035 | 0 | — |
| ITEM-0128 | B - Core Products | Lead-time risk | 34 | 698 | 45 | 3.8 | 141 | 557 | 746 | 0 | 4 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Reorder | 1686 | 0 | 90 | 134.3 | 698 | 1841 | 2105 | 419 | — |
| ITEM-0131 | B - Core Products | Excess | 874 | 0 | 14 | 137.8 | 35 | 131 | 264 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 508 | 0 | 60 | 117.8 | 70 | 333 | 463 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 9 | 135 | 90 | 9.6 | 24 | 109 | 137 | 0 | 10 |
| ITEM-0135 | A - Top Movers | Excess | 4473 | 0 | 60 | 318.0 | 360 | 1219 | 1415 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.6 | 27 | 77 | 109 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 769 | 0 | 14 | 53.2 | 108 | 325 | 527 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 266 | 560 | 30 | 17.9 | 197 | 658 | 866 | 0 | 18 |
| ITEM-0140 | A - Top Movers | Healthy | 2086 | 0 | 60 | 115.5 | 462 | 1565 | 1817 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2681 | 0 | 45 | 265.7 | 158 | 623 | 834 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 547 | 1246 | 1486 | 0 | 1 |
| ITEM-0143 | B - Core Products | Reorder | 669 | 0 | 45 | 60.6 | 172 | 680 | 912 | 243 | — |
| ITEM-0144 | B - Core Products | Excess | 1407 | 0 | 7 | 110.0 | 37 | 140 | 408 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 54 | 888 | 60 | 5.9 | 195 | 757 | 950 | 0 | 6 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 283 | 636 | 90 | 44.2 | 197 | 780 | 914 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 431 | 721 | 991 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 644 | 178 | 60 | 82.3 | 165 | 643 | 807 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 125.1 | 437 | 1114 | 1270 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 79 | 200 | 60 | 31.0 | 42 | 198 | 274 | 0 | 32 |
| ITEM-0155 | B - Core Products | Excess | 941 | 0 | 14 | 136.8 | 40 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 307 | 671 | 30 | 17.9 | 230 | 763 | 1004 | 0 | 18 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
