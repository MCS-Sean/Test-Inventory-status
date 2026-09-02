# Synthetic Inventory Health

**Simulation date: 2026-09-02**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 55 |
| Lead-time risk | 39 |
| Reorder | 1 |
| Stockout | 16 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 131 | 510 | 767 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1112 | 294 | 60 | 75.1 | 378 | 1282 | 1489 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2070 | 0 | 45 | 281.4 | 119 | 458 | 612 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 357 | 0 | 14 | 46.9 | 44 | 159 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 2 | 142 | 45 | 1.2 | 21 | 98 | 148 | 0 | 2 |
| ITEM-0008 | B - Core Products | Healthy | 339 | 0 | 14 | 33.6 | 63 | 215 | 426 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 77 | 198 | 60 | 31.9 | 41 | 189 | 261 | 0 | 32 |
| ITEM-0010 | B - Core Products | Lead-time risk | 165 | 410 | 90 | 42.7 | 120 | 472 | 554 | 0 | 43 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2128 | 0 | 7 | 127.9 | 306 | 440 | 673 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 460 | 0 | 90 | 165.6 | 66 | 319 | 403 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1356 | 0 | 7 | 105.5 | 34 | 137 | 407 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 106 | 419 | 562 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1241 | 0 | 30 | 211.5 | 66 | 248 | 372 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3326 | 0 | 60 | 326.1 | 211 | 834 | 1048 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 108 | 323 | 14 | 10.2 | 63 | 222 | 445 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 596 | 0 | 60 | 350.6 | 29 | 133 | 184 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 96 | 2305 | 90 | 5.6 | 652 | 2218 | 2458 | 0 | 6 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.7 | 8 | 31 | 53 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 87.4 | 685 | 1496 | 1775 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 3 | 243 | 30 | 0.8 | 32 | 142 | 248 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 384 | 960 | 90 | 41.9 | 283 | 1117 | 1309 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 2 | 35 | 7 | 4.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1407 | 0 | 14 | 150.9 | 56 | 196 | 392 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 2 | 395 | 60 | 0.5 | 64 | 305 | 423 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 436 | 0 | 45 | 68.4 | 105 | 399 | 533 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 485 | 0 | 14 | 43.1 | 64 | 233 | 470 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 254 | 0 | 14 | 33.1 | 45 | 161 | 322 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 335 | 503 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 138 | 575 | 30 | 10.0 | 149 | 579 | 870 | 0 | 10 |
| ITEM-0040 | A - Top Movers | Excess | 4716 | 0 | 60 | 345.1 | 356 | 1190 | 1381 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 41.7 | 351 | 589 | 810 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 296 | 0 | 14 | 33.5 | 56 | 189 | 375 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 845 | 0 | 45 | 250.2 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 154.9 | 122 | 380 | 465 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 11.1 | 83 | 205 | 264 | 0 | 12 |
| ITEM-0047 | C - Slow Moving | Reorder | 405 | 0 | 60 | 91.4 | 173 | 444 | 577 | 175 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 31 | 80 | 45 | 24.9 | 17 | 75 | 112 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 12 | 290 | 60 | 5.9 | 116 | 241 | 302 | 0 | 6 |
| ITEM-0052 | B - Core Products | Healthy | 371 | 0 | 7 | 36.5 | 28 | 110 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 249 | 0 | 7 | 33.3 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4733 | 0 | 60 | 332.0 | 374 | 1244 | 1444 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 691 | 0 | 14 | 53.5 | 101 | 295 | 476 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1821 | 580 | 90 | 106.0 | 651 | 2215 | 2455 | 0 | 107 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 379 | 765 | 1027 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 23 | 564 | 45 | 3.4 | 112 | 423 | 565 | 0 | 4 |
| ITEM-0061 | B - Core Products | Lead-time risk | 36 | 145 | 14 | 7.4 | 29 | 103 | 205 | 0 | 8 |
| ITEM-0062 | C - Slow Moving | Healthy | 148 | 0 | 30 | 52.0 | 25 | 114 | 199 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 868 | 0 | 14 | 127.6 | 38 | 140 | 283 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 82.3 | 272 | 714 | 866 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1398 | 0 | 60 | 118.3 | 244 | 966 | 1214 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 539 | 0 | 45 | 94.2 | 90 | 354 | 474 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 745 | 0 | 14 | 44.7 | 121 | 371 | 605 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 161 | 390 | 30 | 19.3 | 93 | 353 | 528 | 0 | 20 |
| ITEM-0069 | C - Slow Moving | Healthy | 55 | 0 | 7 | 19.0 | 7 | 31 | 118 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 31 | 0 | 7 | 35.8 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 14 | 1070 | 60 | 1.2 | 236 | 931 | 1170 | 0 | 2 |
| ITEM-0073 | B - Core Products | Excess | 3662 | 0 | 90 | 479.7 | 236 | 931 | 1091 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 42 | 106 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 11 | 47 | 71 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 417 | 0 | 7 | 115.5 | 9 | 38 | 147 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 758 | 275 | 45 | 60.7 | 195 | 769 | 1032 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 639 | 0 | 45 | 257.9 | 30 | 144 | 219 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 711 | 235 | 90 | 107.2 | 203 | 807 | 946 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 113 | 335 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1412 | 0 | 14 | 135.6 | 61 | 218 | 436 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 141 | 337 | 60 | 31.8 | 94 | 365 | 458 | 0 | 32 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 329 | 483 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 61 | 0 | 14 | 33.5 | 9 | 37 | 91 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 7 | 365 | 45 | 1.5 | 71 | 280 | 374 | 0 | 2 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 105 | 0 | 30 | 66.1 | 14 | 64 | 111 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1304 | 436 | 90 | 99.7 | 402 | 1593 | 1867 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 31.3 | 241 | 368 | 700 | 0 | — |
| ITEM-0094 | B - Core Products | Stockout | 0 | 262 | 7 | 0.0 | 27 | 92 | 262 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7753 | 0 | 90 | 435.3 | 678 | 2299 | 2549 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4393 | 0 | 60 | 325.4 | 349 | 1173 | 1362 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 13.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 320 | 0 | 7 | 31.5 | 32 | 114 | 327 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 38 | 131 | 260 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1129 | 420 | 60 | 77.8 | 579 | 1465 | 1769 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 78 | 210 | 45 | 24.5 | 40 | 187 | 282 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 748 | 0 | 45 | 92.7 | 125 | 497 | 666 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1794 | 524 | 90 | 106.5 | 643 | 2176 | 2412 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 787 | 241 | 60 | 73.5 | 222 | 876 | 1101 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 200.3 | 66 | 159 | 249 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 319 | 915 | 90 | 34.5 | 282 | 1124 | 1318 | 0 | 35 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 315.2 | 96 | 241 | 312 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2389 | 0 | 90 | 161.9 | 559 | 1902 | 2109 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1368 | 360 | 60 | 77.8 | 451 | 1524 | 1770 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 623 | 1100 | 45 | 33.1 | 886 | 1751 | 2014 | 295 | 34 |
| ITEM-0114 | C - Slow Moving | Healthy | 9 | 55 | 14 | 6.1 | 8 | 31 | 75 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1014 | 0 | 14 | 60.3 | 298 | 551 | 904 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 202 | 530 | 90 | 37.4 | 165 | 657 | 770 | 0 | 38 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 255 | 383 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 85 | 0 | 30 | 45.8 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 448 | 0 | 7 | 34.4 | 36 | 141 | 414 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | 6 |
| ITEM-0124 | B - Core Products | Lead-time risk | 62 | 292 | 14 | 5.9 | 60 | 218 | 440 | 0 | 6 |
| ITEM-0125 | B - Core Products | Healthy | 136 | 0 | 7 | 21.7 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 548 | 735 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 850 | 0 | 14 | 134.9 | 35 | 130 | 262 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 497 | 0 | 60 | 118.3 | 68 | 325 | 451 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 7 | 135 | 90 | 7.5 | 24 | 109 | 137 | 0 | 8 |
| ITEM-0135 | A - Top Movers | Excess | 4436 | 0 | 60 | 323.5 | 352 | 1189 | 1381 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 742 | 0 | 14 | 52.6 | 107 | 319 | 516 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 210 | 560 | 30 | 14.3 | 195 | 652 | 858 | 0 | 15 |
| ITEM-0140 | A - Top Movers | Healthy | 2015 | 0 | 60 | 112.9 | 457 | 1547 | 1797 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2660 | 0 | 45 | 270.8 | 155 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 547 | 1246 | 1486 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 626 | 243 | 45 | 58.1 | 168 | 664 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1361 | 0 | 7 | 107.5 | 37 | 139 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 31 | 888 | 60 | 3.6 | 181 | 705 | 885 | 0 | 4 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 272 | 636 | 90 | 44.0 | 190 | 753 | 882 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 422 | 705 | 968 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 635 | 178 | 60 | 85.9 | 157 | 608 | 763 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 75 | 200 | 60 | 30.5 | 41 | 191 | 265 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 913 | 0 | 14 | 130.8 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 241 | 671 | 30 | 13.9 | 231 | 768 | 1010 | 0 | 14 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
