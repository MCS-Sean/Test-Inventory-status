# Synthetic Inventory Health

**Simulation date: 2026-09-11**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 66 |
| Lead-time risk | 18 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 505 | 758 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 293 | 0 | 7 | 47.9 | 89 | 138 | 267 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 973 | 517 | 60 | 63.7 | 389 | 1321 | 1534 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2032 | 0 | 45 | 298.3 | 109 | 423 | 566 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 289 | 0 | 14 | 37.9 | 43 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 285 | 0 | 14 | 30.9 | 59 | 198 | 391 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 63 | 198 | 60 | 28.3 | 37 | 173 | 240 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 153 | 410 | 90 | 45.7 | 104 | 409 | 479 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 433 | 0 | 90 | 154.0 | 67 | 323 | 408 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1228 | 0 | 7 | 96.3 | 33 | 136 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 78 | 235 | 45 | 30.3 | 77 | 196 | 273 | 0 | — |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 106 | 420 | 563 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1223 | 0 | 30 | 232.7 | 60 | 223 | 334 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3217 | 0 | 60 | 309.3 | 215 | 850 | 1068 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 375 | 0 | 14 | 38.1 | 59 | 207 | 413 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 589 | 0 | 60 | 384.1 | 26 | 120 | 166 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 647 | 2202 | 2441 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 12 | 45 | 30 | 17.1 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1046 | 717 | 60 | 84.4 | 803 | 1559 | 1733 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 130 | 228 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 342 | 960 | 90 | 41.4 | 256 | 1008 | 1181 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1357 | 0 | 14 | 163.5 | 49 | 174 | 348 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 311 | 432 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 411 | 0 | 45 | 75.6 | 89 | 339 | 454 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 272.0 | 82 | 238 | 315 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 401 | 0 | 14 | 37.2 | 62 | 224 | 450 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 221 | 0 | 14 | 31.6 | 42 | 147 | 294 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 86 | 338 | 508 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 17 | 575 | 30 | 1.2 | 148 | 573 | 860 | 0 | 2 |
| ITEM-0040 | A - Top Movers | Excess | 4647 | 0 | 60 | 368.2 | 331 | 1101 | 1278 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 46.1 | 262 | 461 | 740 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 259 | 0 | 14 | 32.3 | 52 | 173 | 341 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 566 | 1524 | 1745 | 230 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 810 | 0 | 45 | 236.7 | 42 | 200 | 303 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 85 | 211 | 273 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 27 | 80 | 45 | 24.5 | 15 | 66 | 99 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 132 | 297 | 378 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 277 | 0 | 7 | 27.7 | 27 | 107 | 317 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 193 | 0 | 7 | 26.3 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4656 | 0 | 60 | 355.4 | 346 | 1146 | 1329 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 618 | 0 | 14 | 50.4 | 97 | 281 | 453 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1629 | 865 | 90 | 92.3 | 668 | 2274 | 2521 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 98 | 370 | 495 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 28 | 100 | 200 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 132 | 0 | 30 | 52.6 | 22 | 100 | 176 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 817 | 0 | 14 | 120.7 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1267 | 0 | 60 | 104.8 | 249 | 987 | 1241 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 479 | 0 | 45 | 81.6 | 91 | 361 | 485 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 582 | 0 | 14 | 34.7 | 121 | 373 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 135 | 390 | 30 | 18.2 | 84 | 314 | 469 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 28 | 90 | 7 | 9.8 | 7 | 30 | 116 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 29.6 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 238 | 940 | 1181 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3628 | 0 | 90 | 510.2 | 221 | 869 | 1018 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 92 | 0 | 14 | 42.9 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 402 | 0 | 7 | 126.9 | 8 | 34 | 129 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 168 | 170 | 90 | 79.6 | 105 | 298 | 361 | 0 | 80 |
| ITEM-0079 | B - Core Products | Healthy | 648 | 275 | 45 | 51.2 | 198 | 781 | 1046 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 619 | 0 | 45 | 253.2 | 30 | 143 | 216 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 626 | 235 | 90 | 89.7 | 213 | 848 | 995 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 213 | 0 | 7 | 19.4 | 29 | 117 | 348 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1310 | 0 | 14 | 125.2 | 61 | 218 | 438 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 123 | 337 | 60 | 31.3 | 83 | 323 | 406 | 0 | 32 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 54 | 0 | 14 | 32.0 | 9 | 35 | 85 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 273 | 366 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 93 | 0 | 30 | 61.1 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Reorder | 1187 | 436 | 90 | 88.1 | 413 | 1639 | 1922 | 299 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.5 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 213 | 0 | 7 | 29.4 | 22 | 81 | 233 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7611 | 0 | 90 | 424.1 | 682 | 2315 | 2567 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4283 | 0 | 60 | 324.2 | 341 | 1147 | 1332 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 285 | 0 | 7 | 30.6 | 31 | 106 | 302 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 35 | 118 | 234 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 94.8 | 507 | 1206 | 1447 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 66 | 210 | 45 | 22.9 | 36 | 169 | 255 | 0 | 23 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 112.0 | 395 | 1173 | 1352 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 673 | 0 | 45 | 84.2 | 125 | 493 | 661 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1598 | 773 | 90 | 93.8 | 649 | 2201 | 2439 | 0 | — |
| ITEM-0107 | B - Core Products | Reorder | 661 | 241 | 60 | 59.4 | 229 | 908 | 1142 | 240 | — |
| ITEM-0108 | C - Slow Moving | Excess | 593 | 0 | 30 | 216.1 | 61 | 147 | 229 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 238 | 915 | 90 | 26.2 | 278 | 1107 | 1298 | 0 | 27 |
| ITEM-0110 | C - Slow Moving | Excess | 711 | 0 | 60 | 258.0 | 103 | 272 | 354 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2252 | 0 | 90 | 148.4 | 575 | 1957 | 2169 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1186 | 360 | 60 | 67.5 | 451 | 1523 | 1769 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 26.0 | 897 | 1815 | 2095 | 0 | 27 |
| ITEM-0114 | C - Slow Moving | Healthy | 48 | 0 | 14 | 33.5 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 59.3 | 298 | 552 | 908 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 159 | 530 | 90 | 29.9 | 163 | 647 | 758 | 0 | 30 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 66 | 258 | 388 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 68 | 55 | 30 | 37.1 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 315 | 0 | 7 | 23.2 | 36 | 145 | 430 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 233 | 0 | 14 | 80.0 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 293 | 0 | 14 | 28.4 | 59 | 214 | 431 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 88 | 0 | 7 | 14.5 | 17 | 66 | 194 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 554 | 743 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 800 | 0 | 14 | 129.7 | 34 | 127 | 256 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 456 | 0 | 60 | 104.7 | 70 | 336 | 467 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 110 | 139 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4312 | 0 | 60 | 315.3 | 351 | 1186 | 1377 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 0.9 | 27 | 77 | 109 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 687 | 0 | 14 | 56.7 | 91 | 273 | 443 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 66 | 787 | 30 | 4.4 | 198 | 662 | 872 | 0 | 5 |
| ITEM-0140 | A - Top Movers | Healthy | 1827 | 0 | 60 | 100.4 | 465 | 1575 | 1830 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2575 | 0 | 45 | 264.6 | 153 | 601 | 806 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 585 | 1380 | 1653 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 515 | 243 | 45 | 47.2 | 170 | 672 | 902 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1242 | 0 | 7 | 96.6 | 38 | 141 | 411 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 162 | 631 | 792 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 246 | 636 | 90 | 43.6 | 174 | 688 | 807 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 995 | 0 | 14 | 51.8 | 417 | 705 | 974 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 139.4 | 230 | 394 | 622 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 599 | 178 | 60 | 91.1 | 140 | 542 | 680 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 61 | 200 | 60 | 27.2 | 37 | 174 | 242 | 0 | 28 |
| ITEM-0155 | B - Core Products | Excess | 848 | 0 | 14 | 123.9 | 40 | 143 | 287 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 10 | 930 | 30 | 0.5 | 243 | 811 | 1067 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 383 | 418 | 7 | 16.9 | 304 | 485 | 802 | 0 | — |
