# Synthetic Inventory Health

**Simulation date: 2026-08-30**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 53 |
| Lead-time risk | 49 |
| Reorder | 2 |
| Stockout | 6 |

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
| ITEM-0001 | B - Core Products | Lead-time risk | 18 | 728 | 30 | 1.5 | 130 | 505 | 759 | 0 | 2 |
| ITEM-0002 | B - Core Products | Reorder | 127 | 0 | 7 | 17.8 | 99 | 156 | 306 | 180 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1157 | 294 | 60 | 78.5 | 377 | 1276 | 1482 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2080 | 0 | 45 | 267.4 | 126 | 484 | 648 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 382 | 0 | 14 | 51.0 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 5 | 142 | 45 | 3.0 | 21 | 99 | 149 | 0 | 3 |
| ITEM-0008 | B - Core Products | Healthy | 353 | 0 | 14 | 32.9 | 68 | 229 | 454 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 79 | 198 | 60 | 30.8 | 43 | 200 | 277 | 0 | 31 |
| ITEM-0010 | B - Core Products | Lead-time risk | 173 | 410 | 90 | 43.9 | 122 | 481 | 564 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2206 | 0 | 7 | 139.8 | 303 | 430 | 651 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 464 | 0 | 90 | 163.1 | 68 | 327 | 413 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1390 | 0 | 7 | 107.8 | 34 | 138 | 408 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 118.1 | 28 | 48 | 121 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 17 | 510 | 45 | 2.5 | 106 | 419 | 561 | 0 | 3 |
| ITEM-0018 | B - Core Products | Excess | 1253 | 0 | 30 | 208.4 | 67 | 254 | 380 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3357 | 0 | 60 | 326.3 | 213 | 841 | 1057 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 123 | 323 | 14 | 11.4 | 64 | 226 | 452 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 598 | 0 | 60 | 340.6 | 30 | 138 | 190 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 142 | 2305 | 90 | 8.2 | 661 | 2247 | 2491 | 0 | 9 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.2 | 8 | 32 | 55 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 87.4 | 685 | 1496 | 1775 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 9 | 243 | 30 | 2.4 | 33 | 148 | 259 | 0 | 3 |
| ITEM-0029 | B - Core Products | Lead-time risk | 406 | 960 | 90 | 43.6 | 288 | 1136 | 1331 | 0 | 44 |
| ITEM-0030 | C - Slow Moving | Healthy | 2 | 35 | 7 | 3.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1420 | 0 | 14 | 142.8 | 60 | 210 | 418 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 18 | 395 | 60 | 4.6 | 64 | 304 | 421 | 0 | 5 |
| ITEM-0033 | B - Core Products | Healthy | 447 | 0 | 45 | 67.8 | 109 | 413 | 551 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 518 | 0 | 14 | 46.2 | 64 | 233 | 468 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 271 | 0 | 14 | 33.8 | 47 | 168 | 336 | 0 | — |
| ITEM-0038 | B - Core Products | Lead-time risk | 1 | 484 | 30 | 0.1 | 87 | 340 | 512 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 207 | 575 | 30 | 15.4 | 145 | 563 | 846 | 0 | 16 |
| ITEM-0040 | A - Top Movers | Excess | 4736 | 0 | 60 | 341.0 | 361 | 1209 | 1403 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 37.3 | 376 | 642 | 889 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 308 | 0 | 14 | 33.6 | 58 | 196 | 389 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1270 | 90 | 0.0 | 518 | 1327 | 1514 | 245 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 856 | 0 | 45 | 256.8 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 474 | 0 | 90 | 184.7 | 112 | 346 | 423 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 45 | 192 | 60 | 26.0 | 79 | 185 | 237 | 0 | 26 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 34 | 80 | 45 | 26.8 | 17 | 76 | 114 | 0 | 27 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 62 | 224 | 60 | 42.0 | 102 | 193 | 237 | 0 | 42 |
| ITEM-0052 | B - Core Products | Healthy | 400 | 0 | 7 | 39.3 | 28 | 110 | 324 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 275 | 0 | 7 | 37.0 | 19 | 79 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4753 | 0 | 60 | 325.8 | 382 | 1272 | 1477 | 0 | — |
| ITEM-0055 | A - Top Movers | Excess | 721 | 0 | 14 | 55.7 | 102 | 297 | 478 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1861 | 580 | 90 | 107.0 | 659 | 2242 | 2485 | 0 | 108 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 379 | 765 | 1027 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 32 | 564 | 45 | 4.5 | 118 | 447 | 597 | 0 | 5 |
| ITEM-0061 | B - Core Products | Lead-time risk | 52 | 145 | 14 | 10.7 | 29 | 102 | 204 | 0 | 11 |
| ITEM-0062 | C - Slow Moving | Healthy | 151 | 0 | 30 | 51.3 | 26 | 118 | 206 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 896 | 0 | 14 | 134.6 | 37 | 137 | 277 | 0 | — |
| ITEM-0064 | B - Core Products | Lead-time risk | 595 | 310 | 60 | 77.9 | 279 | 745 | 905 | 0 | 78 |
| ITEM-0065 | B - Core Products | Healthy | 1423 | 0 | 60 | 119.5 | 246 | 973 | 1223 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 559 | 0 | 45 | 98.1 | 89 | 352 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 805 | 0 | 14 | 48.4 | 121 | 371 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 170 | 390 | 30 | 19.2 | 98 | 372 | 558 | 0 | 20 |
| ITEM-0069 | C - Slow Moving | Healthy | 64 | 0 | 7 | 22.3 | 7 | 30 | 116 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 154 | 104 | 45 | 55.2 | 81 | 210 | 293 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 34 | 0 | 7 | 39.7 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 38 | 1070 | 60 | 3.3 | 237 | 934 | 1173 | 0 | 4 |
| ITEM-0073 | B - Core Products | Excess | 3672 | 0 | 90 | 460.9 | 247 | 972 | 1140 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 2 | 99 | 14 | 0.9 | 10 | 42 | 106 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 3 | 66 | 45 | 3.9 | 11 | 47 | 70 | 0 | 4 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 61.4 | 214 | 412 | 457 | 0 | 62 |
| ITEM-0077 | C - Slow Moving | Excess | 424 | 0 | 7 | 115.3 | 9 | 39 | 149 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 786 | 0 | 45 | 62.7 | 196 | 773 | 1036 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 644 | 0 | 45 | 262.3 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 720 | 235 | 90 | 106.6 | 206 | 821 | 963 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 111 | 327 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1433 | 0 | 14 | 135.3 | 62 | 221 | 444 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 148 | 337 | 60 | 32.3 | 97 | 377 | 473 | 0 | 33 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 331 | 488 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 63 | 0 | 14 | 32.8 | 10 | 39 | 97 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 17 | 365 | 45 | 3.7 | 73 | 287 | 385 | 0 | 4 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 109 | 0 | 30 | 68.1 | 14 | 64 | 112 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1349 | 436 | 90 | 104.7 | 397 | 1570 | 1841 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 29.9 | 242 | 375 | 723 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 9 | 262 | 7 | 1.1 | 28 | 96 | 275 | 0 | 2 |
| ITEM-0095 | A - Top Movers | Excess | 7813 | 0 | 90 | 438.4 | 679 | 2301 | 2551 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4429 | 0 | 60 | 326.2 | 351 | 1180 | 1370 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 11.2 | 110 | 169 | 323 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 4 | 330 | 7 | 0.4 | 34 | 120 | 343 | 0 | 1 |
| ITEM-0100 | B - Core Products | Lead-time risk | 10 | 256 | 14 | 1.6 | 38 | 134 | 267 | 0 | 2 |
| ITEM-0101 | B - Core Products | Healthy | 1204 | 420 | 60 | 85.0 | 571 | 1436 | 1733 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 84 | 210 | 45 | 25.6 | 41 | 192 | 291 | 0 | 26 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 768 | 0 | 45 | 95.2 | 125 | 497 | 666 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1846 | 524 | 90 | 109.2 | 645 | 2183 | 2420 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 818 | 241 | 60 | 75.8 | 224 | 883 | 1109 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 610 | 0 | 30 | 196.1 | 67 | 164 | 257 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 347 | 915 | 90 | 37.9 | 280 | 1115 | 1307 | 0 | 38 |
| ITEM-0110 | C - Slow Moving | Excess | 756 | 0 | 60 | 324.0 | 96 | 239 | 309 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2414 | 0 | 90 | 163.0 | 561 | 1909 | 2117 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1411 | 360 | 60 | 79.0 | 458 | 1548 | 1798 | 0 | — |
| ITEM-0113 | A - Top Movers | Reorder | 863 | 635 | 45 | 47.9 | 878 | 1708 | 1960 | 465 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 15 | 55 | 14 | 10.4 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1023 | 0 | 14 | 55.5 | 314 | 591 | 978 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 4 | 115 | 45 | 3.0 | 18 | 81 | 122 | 0 | 3 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 217 | 530 | 90 | 40.2 | 165 | 657 | 770 | 0 | 41 |
| ITEM-0119 | B - Core Products | Lead-time risk | 17 | 355 | 30 | 2.8 | 65 | 253 | 380 | 0 | 3 |
| ITEM-0120 | C - Slow Moving | Healthy | 89 | 0 | 30 | 47.4 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 477 | 0 | 7 | 36.5 | 37 | 142 | 417 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 4.1 | 102 | 157 | 233 | 0 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 101 | 292 | 14 | 9.7 | 60 | 216 | 435 | 0 | 10 |
| ITEM-0125 | B - Core Products | Healthy | 156 | 0 | 7 | 24.9 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 295 | 790 | 30 | 24.7 | 496 | 867 | 1035 | 0 | — |
| ITEM-0128 | B - Core Products | Lead-time risk | 23 | 698 | 45 | 2.5 | 141 | 558 | 747 | 0 | 3 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 870 | 0 | 14 | 137.4 | 35 | 130 | 263 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 506 | 0 | 60 | 118.9 | 69 | 329 | 457 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 9 | 135 | 90 | 9.8 | 23 | 107 | 135 | 0 | 10 |
| ITEM-0135 | A - Top Movers | Excess | 4473 | 0 | 60 | 323.1 | 355 | 1200 | 1394 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.6 | 27 | 77 | 109 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 761 | 0 | 14 | 53.1 | 107 | 323 | 523 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 254 | 560 | 30 | 17.1 | 197 | 658 | 866 | 0 | 18 |
| ITEM-0140 | A - Top Movers | Healthy | 2074 | 0 | 60 | 115.8 | 458 | 1551 | 1802 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2671 | 0 | 45 | 264.2 | 158 | 624 | 836 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 547 | 1246 | 1486 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 656 | 243 | 45 | 60.1 | 170 | 673 | 902 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1389 | 0 | 7 | 107.5 | 37 | 141 | 412 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 47 | 888 | 60 | 5.2 | 192 | 747 | 938 | 0 | 6 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 280 | 636 | 90 | 44.9 | 192 | 760 | 891 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 431 | 721 | 991 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 640 | 178 | 60 | 82.5 | 164 | 638 | 800 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 78 | 200 | 60 | 31.1 | 42 | 196 | 271 | 0 | 32 |
| ITEM-0155 | B - Core Products | Excess | 941 | 0 | 14 | 138.4 | 40 | 142 | 285 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 301 | 671 | 30 | 17.7 | 228 | 755 | 993 | 0 | 18 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
