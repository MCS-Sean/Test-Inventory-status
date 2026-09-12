# Synthetic Inventory Health

**Simulation date: 2026-09-12**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 68 |
| Lead-time risk | 18 |
| Stockout | 24 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 498 | 749 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 293 | 0 | 7 | 47.9 | 89 | 138 | 267 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 953 | 517 | 60 | 62.4 | 389 | 1321 | 1534 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2028 | 0 | 45 | 302.2 | 108 | 417 | 558 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 284 | 0 | 14 | 37.5 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 279 | 0 | 14 | 31.2 | 56 | 191 | 379 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 62 | 198 | 60 | 28.3 | 37 | 171 | 237 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 151 | 410 | 90 | 45.6 | 104 | 406 | 475 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 430 | 0 | 90 | 153.6 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1218 | 0 | 7 | 95.3 | 33 | 136 | 404 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 78 | 235 | 45 | 30.3 | 77 | 196 | 273 | 0 | — |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 105 | 415 | 557 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1219 | 0 | 30 | 234.4 | 60 | 222 | 331 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3207 | 0 | 60 | 308.0 | 215 | 851 | 1069 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 365 | 0 | 14 | 37.3 | 58 | 205 | 410 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 589 | 0 | 60 | 389.8 | 26 | 119 | 164 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 643 | 2185 | 2423 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 11 | 45 | 30 | 15.5 | 8 | 31 | 52 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1046 | 717 | 60 | 105.2 | 699 | 1306 | 1445 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 130 | 228 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 337 | 960 | 90 | 41.1 | 255 | 1002 | 1174 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1353 | 0 | 14 | 165.9 | 48 | 171 | 342 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 315 | 437 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 408 | 0 | 45 | 75.9 | 89 | 337 | 450 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 272.0 | 82 | 238 | 315 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 395 | 0 | 14 | 37.0 | 62 | 223 | 447 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 218 | 0 | 14 | 31.2 | 42 | 147 | 294 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 86 | 338 | 508 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 1 | 575 | 30 | 0.1 | 149 | 576 | 865 | 290 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4639 | 0 | 60 | 376.1 | 322 | 1075 | 1247 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 46.1 | 262 | 461 | 740 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 251 | 0 | 14 | 32.1 | 50 | 168 | 332 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1524 | 1745 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 804 | 0 | 45 | 233.4 | 42 | 201 | 304 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 85 | 211 | 273 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 26 | 80 | 45 | 23.9 | 15 | 66 | 98 | 0 | 24 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 132 | 297 | 378 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 267 | 0 | 7 | 26.8 | 27 | 107 | 317 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 188 | 0 | 7 | 25.6 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4651 | 0 | 60 | 356.2 | 345 | 1142 | 1325 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 612 | 0 | 14 | 50.5 | 96 | 278 | 448 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1605 | 865 | 90 | 90.6 | 671 | 2284 | 2532 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 98 | 370 | 495 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 28 | 100 | 199 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 131 | 0 | 30 | 52.4 | 22 | 100 | 175 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 810 | 0 | 14 | 120.5 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1262 | 0 | 60 | 105.6 | 247 | 977 | 1228 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 474 | 0 | 45 | 80.8 | 91 | 361 | 485 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 558 | 0 | 14 | 32.9 | 122 | 377 | 615 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 132 | 390 | 30 | 17.9 | 83 | 312 | 466 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 25 | 90 | 7 | 8.8 | 7 | 30 | 115 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 124 | 104 | 45 | 42.0 | 83 | 219 | 308 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 23 | 0 | 7 | 26.9 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 236 | 931 | 1170 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3622 | 0 | 90 | 514.2 | 219 | 861 | 1008 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 89 | 0 | 14 | 41.3 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 400 | 0 | 7 | 127.2 | 8 | 34 | 128 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 637 | 275 | 45 | 50.7 | 197 | 776 | 1039 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 617 | 0 | 45 | 254.7 | 30 | 142 | 215 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 623 | 235 | 90 | 90.0 | 211 | 841 | 987 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 200 | 0 | 7 | 18.2 | 29 | 118 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1299 | 0 | 14 | 123.8 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 120 | 337 | 60 | 30.9 | 82 | 319 | 400 | 0 | 31 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 54 | 0 | 14 | 32.6 | 9 | 34 | 84 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 271 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 91 | 0 | 30 | 59.3 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1170 | 735 | 90 | 86.6 | 414 | 1644 | 1928 | 0 | 119 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 209 | 0 | 7 | 28.7 | 22 | 81 | 234 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7590 | 0 | 90 | 426.4 | 676 | 2296 | 2545 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4267 | 0 | 60 | 325.7 | 338 | 1138 | 1321 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 280 | 0 | 7 | 30.5 | 30 | 104 | 296 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 254 | 0 | 14 | 46.5 | 35 | 117 | 232 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 1009 | 420 | 60 | 88.5 | 505 | 1201 | 1440 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 64 | 210 | 45 | 22.3 | 36 | 168 | 254 | 0 | 23 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 112.0 | 395 | 1173 | 1352 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 665 | 0 | 45 | 82.3 | 126 | 498 | 668 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1579 | 773 | 90 | 92.0 | 653 | 2215 | 2455 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 653 | 481 | 60 | 58.2 | 231 | 915 | 1151 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 181.9 | 66 | 162 | 255 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 236 | 915 | 90 | 26.3 | 274 | 1090 | 1279 | 0 | 27 |
| ITEM-0110 | C - Slow Moving | Excess | 702 | 0 | 60 | 245.8 | 104 | 279 | 364 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2242 | 0 | 90 | 147.9 | 575 | 1955 | 2167 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1170 | 360 | 60 | 66.5 | 452 | 1526 | 1772 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 26.0 | 897 | 1815 | 2095 | 0 | 27 |
| ITEM-0114 | C - Slow Moving | Healthy | 45 | 0 | 14 | 31.2 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 67.1 | 274 | 499 | 813 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 151 | 530 | 90 | 28.2 | 164 | 652 | 764 | 0 | 29 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 67 | 262 | 393 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 66 | 55 | 30 | 36.0 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 311 | 0 | 7 | 23.2 | 36 | 144 | 426 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 233 | 0 | 14 | 80.0 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 283 | 0 | 14 | 27.6 | 59 | 213 | 429 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 82 | 0 | 7 | 13.6 | 17 | 66 | 193 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 556 | 745 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 791 | 0 | 14 | 129.0 | 34 | 126 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 452 | 0 | 60 | 103.5 | 70 | 337 | 468 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 113 | 142 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4297 | 0 | 60 | 314.4 | 350 | 1184 | 1375 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 1.0 | 26 | 72 | 102 | 0 | 2 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 685 | 0 | 14 | 57.2 | 91 | 271 | 439 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 40 | 787 | 30 | 2.6 | 200 | 672 | 885 | 0 | 3 |
| ITEM-0140 | A - Top Movers | Healthy | 1807 | 0 | 60 | 98.7 | 468 | 1585 | 1842 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2565 | 0 | 45 | 261.1 | 154 | 606 | 813 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 589 | 1407 | 1688 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 501 | 243 | 45 | 45.7 | 171 | 675 | 906 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1223 | 0 | 7 | 94.4 | 38 | 142 | 414 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 163 | 636 | 799 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 242 | 636 | 90 | 43.7 | 171 | 675 | 791 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 995 | 0 | 14 | 51.8 | 417 | 705 | 974 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 139.4 | 230 | 394 | 622 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 593 | 178 | 60 | 92.0 | 136 | 530 | 665 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 61 | 200 | 60 | 27.4 | 37 | 173 | 240 | 0 | 28 |
| ITEM-0155 | B - Core Products | Excess | 839 | 0 | 14 | 121.4 | 41 | 145 | 290 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 243 | 812 | 1068 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 383 | 418 | 7 | 16.9 | 304 | 485 | 802 | 0 | — |
