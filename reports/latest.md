# Synthetic Inventory Health

**Simulation date: 2026-08-28**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 53 |
| Lead-time risk | 54 |
| Reorder | 1 |
| Stockout | 3 |

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
| ITEM-0001 | B - Core Products | Lead-time risk | 34 | 728 | 30 | 2.8 | 130 | 509 | 765 | 0 | 3 |
| ITEM-0002 | B - Core Products | Healthy | 182 | 0 | 7 | 28.0 | 96 | 149 | 285 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1178 | 294 | 60 | 79.3 | 380 | 1287 | 1495 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2091 | 0 | 45 | 268.8 | 126 | 484 | 648 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 393 | 0 | 14 | 52.4 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 7 | 142 | 45 | 4.1 | 21 | 99 | 150 | 0 | 5 |
| ITEM-0008 | B - Core Products | Healthy | 365 | 0 | 14 | 34.0 | 68 | 229 | 454 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 82 | 198 | 60 | 31.9 | 43 | 200 | 277 | 0 | 32 |
| ITEM-0010 | B - Core Products | Lead-time risk | 179 | 410 | 90 | 43.7 | 128 | 502 | 588 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2206 | 0 | 7 | 126.7 | 314 | 454 | 698 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 469 | 0 | 90 | 164.9 | 68 | 327 | 413 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1417 | 0 | 7 | 109.6 | 34 | 138 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 111.9 | 28 | 49 | 126 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 27 | 510 | 45 | 4.0 | 106 | 419 | 561 | 0 | 4 |
| ITEM-0018 | B - Core Products | Excess | 1260 | 0 | 30 | 206.9 | 68 | 257 | 385 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3378 | 0 | 60 | 326.6 | 214 | 846 | 1063 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 136 | 323 | 14 | 12.3 | 66 | 232 | 465 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 602 | 0 | 60 | 328.4 | 31 | 143 | 198 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 169 | 2305 | 90 | 9.7 | 660 | 2244 | 2487 | 0 | 10 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 16 | 45 | 30 | 21.5 | 8 | 32 | 54 | 0 | 22 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 81.0 | 702 | 1577 | 1878 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 15 | 243 | 30 | 4.1 | 33 | 147 | 257 | 0 | 5 |
| ITEM-0029 | B - Core Products | Lead-time risk | 420 | 960 | 90 | 43.5 | 299 | 1178 | 1381 | 0 | 44 |
| ITEM-0030 | C - Slow Moving | Lead-time risk | 2 | 35 | 7 | 3.5 | 7 | 12 | 29 | 0 | 4 |
| ITEM-0031 | B - Core Products | Excess | 1426 | 0 | 14 | 142.9 | 60 | 210 | 420 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 23 | 395 | 60 | 5.8 | 64 | 305 | 423 | 0 | 6 |
| ITEM-0033 | B - Core Products | Healthy | 451 | 0 | 45 | 66.7 | 111 | 423 | 565 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 553 | 0 | 14 | 49.8 | 63 | 230 | 463 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 278 | 0 | 14 | 34.8 | 47 | 167 | 335 | 0 | — |
| ITEM-0038 | B - Core Products | Lead-time risk | 21 | 484 | 30 | 2.6 | 86 | 337 | 507 | 0 | 3 |
| ITEM-0039 | B - Core Products | Lead-time risk | 236 | 575 | 30 | 17.6 | 145 | 561 | 843 | 0 | 18 |
| ITEM-0040 | A - Top Movers | Excess | 4749 | 0 | 60 | 333.9 | 369 | 1237 | 1436 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 37.3 | 376 | 642 | 889 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 323 | 0 | 14 | 34.6 | 58 | 199 | 395 | 0 | — |
| ITEM-0043 | B - Core Products | Lead-time risk | 87 | 1270 | 90 | 11.2 | 480 | 1190 | 1354 | 0 | 12 |
| ITEM-0044 | C - Slow Moving | Excess | 863 | 0 | 45 | 265.1 | 40 | 190 | 288 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 474 | 0 | 90 | 166.6 | 119 | 378 | 464 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 45 | 192 | 60 | 26.0 | 79 | 185 | 237 | 0 | 26 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 34 | 80 | 45 | 26.6 | 17 | 76 | 115 | 0 | 27 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 62 | 224 | 60 | 42.0 | 102 | 193 | 237 | 0 | 42 |
| ITEM-0052 | B - Core Products | Healthy | 417 | 0 | 7 | 41.1 | 28 | 110 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 298 | 0 | 7 | 39.8 | 20 | 80 | 238 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4774 | 0 | 60 | 326.7 | 382 | 1274 | 1478 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 734 | 0 | 14 | 54.4 | 107 | 310 | 499 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1890 | 580 | 90 | 107.5 | 666 | 2267 | 2513 | 0 | 108 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Lead-time risk | 52 | 802 | 30 | 5.1 | 323 | 640 | 854 | 0 | 6 |
| ITEM-0060 | B - Core Products | Lead-time risk | 41 | 564 | 45 | 5.7 | 120 | 454 | 607 | 0 | 6 |
| ITEM-0061 | B - Core Products | Lead-time risk | 61 | 145 | 14 | 12.4 | 29 | 103 | 206 | 0 | 13 |
| ITEM-0062 | C - Slow Moving | Healthy | 153 | 0 | 30 | 50.8 | 27 | 121 | 211 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 909 | 0 | 14 | 137.0 | 37 | 137 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Lead-time risk | 595 | 310 | 60 | 77.9 | 279 | 745 | 905 | 0 | 78 |
| ITEM-0065 | B - Core Products | Healthy | 1453 | 0 | 60 | 122.2 | 246 | 972 | 1221 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 564 | 0 | 45 | 97.4 | 90 | 357 | 478 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 834 | 0 | 14 | 49.7 | 122 | 374 | 609 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 181 | 390 | 30 | 20.4 | 98 | 374 | 561 | 0 | 21 |
| ITEM-0069 | C - Slow Moving | Healthy | 71 | 0 | 7 | 25.2 | 7 | 30 | 115 | 0 | — |
| ITEM-0070 | C - Slow Moving | Reorder | 172 | 0 | 45 | 66.4 | 79 | 199 | 276 | 104 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 36 | 0 | 7 | 42.1 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 71 | 1070 | 60 | 6.4 | 232 | 910 | 1144 | 0 | 7 |
| ITEM-0073 | B - Core Products | Excess | 3680 | 0 | 90 | 447.0 | 255 | 1005 | 1178 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 5 | 99 | 14 | 2.3 | 10 | 43 | 107 | 0 | 3 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 4 | 66 | 45 | 5.3 | 11 | 46 | 69 | 0 | 6 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 52.7 | 223 | 453 | 506 | 0 | 53 |
| ITEM-0077 | C - Slow Moving | Excess | 428 | 0 | 7 | 114.6 | 9 | 39 | 151 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 802 | 0 | 45 | 63.1 | 198 | 783 | 1049 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 649 | 0 | 45 | 260.8 | 31 | 146 | 221 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 733 | 235 | 90 | 107.3 | 208 | 830 | 974 | 0 | — |
| ITEM-0082 | B - Core Products | Lead-time risk | 7 | 305 | 7 | 0.7 | 29 | 112 | 328 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1468 | 0 | 14 | 140.9 | 60 | 217 | 436 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 154 | 337 | 60 | 32.9 | 99 | 385 | 483 | 0 | 33 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 331 | 488 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 67 | 0 | 14 | 34.7 | 10 | 39 | 97 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 22 | 365 | 45 | 4.7 | 74 | 292 | 391 | 0 | 5 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 113 | 0 | 30 | 71.6 | 14 | 63 | 111 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1377 | 436 | 90 | 107.8 | 393 | 1556 | 1825 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 28.0 | 246 | 388 | 759 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 14 | 262 | 7 | 1.6 | 28 | 97 | 277 | 0 | 2 |
| ITEM-0095 | A - Top Movers | Excess | 7859 | 0 | 90 | 442.6 | 676 | 2292 | 2541 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4451 | 0 | 60 | 323.3 | 356 | 1196 | 1389 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 11.2 | 110 | 169 | 323 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 17 | 330 | 7 | 1.6 | 34 | 121 | 347 | 0 | 2 |
| ITEM-0100 | B - Core Products | Lead-time risk | 17 | 256 | 14 | 2.6 | 39 | 136 | 272 | 0 | 3 |
| ITEM-0101 | B - Core Products | Healthy | 1204 | 420 | 60 | 85.0 | 571 | 1436 | 1733 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 88 | 210 | 45 | 26.5 | 41 | 194 | 294 | 0 | 27 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 781 | 0 | 45 | 97.0 | 125 | 496 | 665 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1890 | 524 | 90 | 112.7 | 640 | 2166 | 2401 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 845 | 241 | 60 | 79.5 | 221 | 870 | 1093 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 646 | 0 | 30 | 238.3 | 61 | 146 | 227 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 372 | 915 | 90 | 41.0 | 277 | 1103 | 1293 | 0 | 42 |
| ITEM-0110 | C - Slow Moving | Excess | 756 | 0 | 60 | 324.0 | 96 | 239 | 309 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2454 | 0 | 90 | 167.8 | 555 | 1886 | 2091 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1441 | 360 | 60 | 79.3 | 466 | 1575 | 1830 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1095 | 635 | 45 | 70.8 | 801 | 1512 | 1729 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 18 | 55 | 14 | 12.4 | 8 | 30 | 74 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1023 | 0 | 14 | 54.1 | 315 | 599 | 996 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 7 | 115 | 45 | 5.2 | 18 | 81 | 122 | 0 | 6 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 228 | 530 | 90 | 42.4 | 165 | 655 | 768 | 0 | 43 |
| ITEM-0119 | B - Core Products | Lead-time risk | 26 | 355 | 30 | 4.3 | 65 | 255 | 383 | 0 | 5 |
| ITEM-0120 | C - Slow Moving | Healthy | 92 | 0 | 30 | 49.0 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 510 | 0 | 7 | 39.5 | 37 | 141 | 412 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 4.1 | 102 | 157 | 233 | 0 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 129 | 292 | 14 | 12.5 | 59 | 214 | 430 | 0 | 13 |
| ITEM-0125 | B - Core Products | Healthy | 171 | 0 | 7 | 27.6 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 295 | 790 | 30 | 24.7 | 496 | 867 | 1035 | 0 | 25 |
| ITEM-0128 | B - Core Products | Lead-time risk | 41 | 698 | 45 | 4.6 | 141 | 555 | 744 | 0 | 5 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1828 | 0 | 90 | 166.5 | 638 | 1637 | 1868 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 878 | 0 | 14 | 138.4 | 35 | 131 | 264 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 514 | 0 | 60 | 119.8 | 70 | 332 | 461 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 10 | 135 | 90 | 10.6 | 24 | 110 | 139 | 0 | 11 |
| ITEM-0135 | B - Core Products | Excess | 4487 | 0 | 60 | 321.0 | 288 | 1141 | 1435 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.6 | 27 | 77 | 109 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 776 | 0 | 14 | 52.7 | 110 | 331 | 537 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 282 | 560 | 30 | 18.9 | 197 | 659 | 867 | 0 | 19 |
| ITEM-0140 | A - Top Movers | Healthy | 2096 | 0 | 60 | 115.3 | 465 | 1574 | 1829 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2685 | 0 | 45 | 264.1 | 159 | 627 | 841 | 0 | — |
| ITEM-0142 | A - Top Movers | Stockout | 0 | 1360 | 60 | 0.0 | 679 | 1378 | 1538 | 180 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 684 | 0 | 45 | 62.7 | 171 | 673 | 903 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1413 | 0 | 7 | 111.1 | 38 | 140 | 407 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 59 | 888 | 60 | 6.3 | 197 | 765 | 961 | 0 | 7 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 287 | 636 | 90 | 44.3 | 200 | 790 | 926 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 431 | 721 | 991 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 649 | 178 | 60 | 81.8 | 167 | 651 | 818 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 125.1 | 437 | 1114 | 1270 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 81 | 200 | 60 | 31.3 | 43 | 201 | 279 | 0 | 32 |
| ITEM-0155 | B - Core Products | Excess | 950 | 0 | 14 | 138.1 | 40 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 317 | 671 | 30 | 18.2 | 232 | 771 | 1014 | 0 | 19 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
