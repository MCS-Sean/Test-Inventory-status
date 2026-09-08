# Synthetic Inventory Health

**Simulation date: 2026-09-08**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 62 |
| Lead-time risk | 26 |
| Reorder | 1 |
| Stockout | 21 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 506 | 760 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 307 | 0 | 7 | 44.1 | 99 | 155 | 301 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1019 | 294 | 60 | 67.2 | 387 | 1312 | 1524 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2044 | 0 | 45 | 293.4 | 112 | 433 | 579 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 315 | 0 | 14 | 41.8 | 43 | 157 | 315 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 306 | 0 | 14 | 32.1 | 60 | 203 | 403 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 65 | 198 | 60 | 28.4 | 38 | 178 | 247 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 156 | 410 | 90 | 45.0 | 108 | 424 | 497 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 442 | 0 | 90 | 157.2 | 67 | 323 | 408 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1269 | 0 | 7 | 99.7 | 33 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 30.3 | 77 | 196 | 273 | 0 | 31 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 413 | 553 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1231 | 0 | 30 | 224.3 | 62 | 233 | 348 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3247 | 0 | 60 | 314.9 | 213 | 842 | 1059 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 74 | 323 | 14 | 7.4 | 59 | 209 | 418 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 592 | 0 | 60 | 383.3 | 26 | 121 | 167 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 652 | 2215 | 2455 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 18.9 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1161 | 717 | 60 | 104.5 | 773 | 1451 | 1607 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 31 | 138 | 240 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 356 | 960 | 90 | 41.3 | 268 | 1053 | 1234 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 32 | 0 | 7 | 75.8 | 6 | 10 | 23 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1369 | 0 | 14 | 154.8 | 53 | 186 | 372 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 308 | 427 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 419 | 0 | 45 | 71.8 | 96 | 365 | 487 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 722 | 0 | 60 | 320.1 | 75 | 213 | 281 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 433 | 0 | 14 | 39.8 | 62 | 226 | 454 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 227 | 0 | 14 | 31.4 | 43 | 152 | 304 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 332 | 500 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 69 | 575 | 30 | 5.1 | 148 | 571 | 858 | 0 | 6 |
| ITEM-0040 | A - Top Movers | Excess | 4667 | 0 | 60 | 361.2 | 338 | 1127 | 1308 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 37.4 | 284 | 530 | 873 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 269 | 0 | 14 | 32.4 | 53 | 178 | 352 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 822 | 0 | 45 | 241.0 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 352 | 175 | 60 | 74.2 | 175 | 465 | 607 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 29 | 80 | 45 | 25.3 | 16 | 69 | 103 | 0 | 26 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 312 | 0 | 7 | 31.1 | 27 | 108 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 222 | 0 | 7 | 30.6 | 20 | 79 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4679 | 0 | 60 | 344.6 | 358 | 1187 | 1377 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 643 | 0 | 14 | 52.9 | 97 | 280 | 450 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1694 | 580 | 90 | 97.0 | 662 | 2251 | 2495 | 0 | 98 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 103 | 390 | 521 | 0 | 1 |
| ITEM-0061 | B - Core Products | Lead-time risk | 1 | 145 | 14 | 0.2 | 29 | 103 | 207 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 137 | 0 | 30 | 52.2 | 23 | 105 | 183 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 836 | 0 | 14 | 124.8 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1320 | 0 | 60 | 110.4 | 247 | 977 | 1228 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 493 | 0 | 45 | 84.8 | 91 | 359 | 481 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 621 | 0 | 14 | 36.6 | 123 | 378 | 616 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 142 | 390 | 30 | 18.5 | 86 | 325 | 486 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 36 | 0 | 7 | 12.5 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 28 | 0 | 7 | 33.6 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 239 | 944 | 1186 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3637 | 0 | 90 | 496.0 | 227 | 895 | 1049 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 108 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 50 | 74 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 406 | 0 | 7 | 121.8 | 8 | 35 | 135 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 179 | 170 | 90 | 88.5 | 104 | 289 | 349 | 0 | 89 |
| ITEM-0079 | B - Core Products | Healthy | 670 | 275 | 45 | 52.2 | 201 | 792 | 1062 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 627 | 0 | 45 | 255.3 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 649 | 235 | 90 | 93.0 | 213 | 848 | 995 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 263 | 0 | 7 | 24.4 | 28 | 115 | 342 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1345 | 0 | 14 | 128.1 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 132 | 337 | 60 | 32.9 | 85 | 330 | 414 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 56 | 0 | 14 | 32.5 | 9 | 35 | 87 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 273 | 367 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 95 | 0 | 30 | 61.5 | 14 | 62 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1228 | 436 | 90 | 91.7 | 410 | 1629 | 1910 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.2 | 248 | 387 | 749 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 231 | 0 | 7 | 31.9 | 22 | 80 | 233 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7654 | 0 | 90 | 423.4 | 687 | 2333 | 2586 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4318 | 0 | 60 | 326.0 | 343 | 1151 | 1337 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 299 | 0 | 7 | 31.2 | 31 | 108 | 309 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 35 | 121 | 240 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 84.9 | 539 | 1320 | 1588 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 71 | 210 | 45 | 24.2 | 37 | 172 | 260 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 103.3 | 420 | 1264 | 1458 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 701 | 0 | 45 | 87.5 | 126 | 495 | 663 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1654 | 773 | 90 | 97.2 | 648 | 2197 | 2435 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 700 | 241 | 60 | 63.6 | 227 | 898 | 1129 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 593 | 0 | 30 | 216.1 | 61 | 147 | 229 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 263 | 915 | 90 | 28.9 | 278 | 1108 | 1299 | 0 | 29 |
| ITEM-0110 | C - Slow Moving | Excess | 711 | 0 | 60 | 258.0 | 103 | 272 | 354 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2279 | 0 | 90 | 148.1 | 583 | 1984 | 2199 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1251 | 360 | 60 | 71.7 | 449 | 1514 | 1758 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 54 | 0 | 14 | 36.8 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | A - Top Movers | Healthy | 1004 | 0 | 14 | 59.3 | 370 | 624 | 861 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 167 | 530 | 90 | 30.6 | 167 | 664 | 779 | 0 | 31 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 254 | 382 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 75 | 0 | 30 | 40.9 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 358 | 0 | 7 | 26.9 | 36 | 143 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 22 | 292 | 14 | 2.1 | 60 | 217 | 437 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 110 | 0 | 7 | 17.9 | 17 | 67 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 549 | 737 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 817 | 0 | 14 | 131.3 | 35 | 129 | 259 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 470 | 0 | 60 | 110.4 | 69 | 329 | 457 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 2 | 135 | 90 | 2.2 | 23 | 106 | 134 | 0 | 3 |
| ITEM-0135 | A - Top Movers | Excess | 4356 | 0 | 60 | 318.2 | 351 | 1187 | 1378 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 0.9 | 27 | 77 | 109 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 714 | 0 | 14 | 55.9 | 99 | 291 | 470 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 110 | 560 | 30 | 7.3 | 198 | 664 | 874 | 0 | 8 |
| ITEM-0140 | A - Top Movers | Healthy | 1895 | 0 | 60 | 103.7 | 467 | 1582 | 1837 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2597 | 0 | 45 | 265.0 | 154 | 605 | 811 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 585 | 1380 | 1653 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 557 | 243 | 45 | 51.6 | 168 | 665 | 892 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1294 | 0 | 7 | 102.3 | 38 | 140 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 11 | 888 | 60 | 1.4 | 169 | 656 | 824 | 0 | 2 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 254 | 636 | 90 | 43.9 | 178 | 705 | 827 | 0 | 44 |
| ITEM-0148 | B - Core Products | Stockout | 0 | 995 | 14 | 0.0 | 327 | 598 | 977 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 119.2 | 254 | 445 | 713 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 611 | 178 | 60 | 89.7 | 145 | 561 | 704 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 149.7 | 389 | 955 | 1085 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 65 | 200 | 60 | 28.1 | 38 | 179 | 249 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 869 | 0 | 14 | 125.7 | 41 | 145 | 290 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 87 | 930 | 30 | 4.8 | 238 | 795 | 1047 | 0 | 5 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Reorder | 406 | 0 | 7 | 17.3 | 308 | 496 | 824 | 418 | — |
