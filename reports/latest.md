# Synthetic Inventory Health

**Simulation date: 2026-09-19**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 68 |
| Lead-time risk | 14 |
| Reorder | 2 |
| Stockout | 26 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 499 | 750 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 175 | 0 | 7 | 26.2 | 95 | 149 | 289 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 865 | 517 | 60 | 56.5 | 391 | 1325 | 1540 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2005 | 0 | 45 | 319.9 | 102 | 391 | 522 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 240 | 0 | 14 | 32.1 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 248 | 0 | 14 | 31.0 | 50 | 170 | 338 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 52 | 198 | 60 | 26.1 | 34 | 156 | 215 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 138 | 410 | 90 | 47.4 | 91 | 356 | 418 | 0 | 48 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 10.6 | 774 | 1624 | 1819 | 0 | 11 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 94.6 | 337 | 495 | 770 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 408 | 0 | 90 | 144.6 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1122 | 0 | 7 | 88.4 | 33 | 135 | 401 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 234.0 | 20 | 30 | 67 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 11 | 235 | 45 | 4.0 | 80 | 208 | 292 | 0 | 4 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 412 | 553 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1203 | 0 | 30 | 251.2 | 56 | 205 | 306 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3120 | 0 | 60 | 292.8 | 219 | 869 | 1093 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 333 | 0 | 14 | 36.3 | 56 | 194 | 387 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 583 | 0 | 60 | 416.4 | 24 | 110 | 152 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 626 | 2127 | 2358 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 8 | 45 | 30 | 11.6 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 27 | 121 | 212 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 304 | 960 | 90 | 38.9 | 242 | 953 | 1117 | 0 | 39 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1333 | 0 | 14 | 181.8 | 44 | 154 | 308 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 317 | 440 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 389 | 0 | 45 | 77.5 | 83 | 315 | 420 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 290.9 | 79 | 225 | 297 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 310 | 0 | 14 | 28.3 | 62 | 227 | 457 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 15.5 | 127 | 197 | 378 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 203 | 0 | 14 | 32.8 | 38 | 131 | 261 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 87 | 341 | 513 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 150 | 581 | 873 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4594 | 0 | 60 | 417.6 | 287 | 958 | 1112 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 386 | 195 | 14 | 27.3 | 341 | 553 | 751 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 215 | 0 | 14 | 30.1 | 45 | 153 | 303 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 785 | 0 | 45 | 233.9 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 143 | 185 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 296 | 175 | 60 | 64.5 | 166 | 446 | 584 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 384 | 0 | 14 | 34.3 | 190 | 358 | 593 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 20 | 80 | 45 | 19.4 | 15 | 63 | 94 | 0 | 20 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 132 | 316 | 407 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 192 | 0 | 7 | 19.1 | 26 | 107 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 134 | 0 | 7 | 18.7 | 20 | 78 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4600 | 0 | 60 | 390.9 | 310 | 1028 | 1193 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 572 | 0 | 14 | 52.5 | 88 | 252 | 405 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1466 | 865 | 90 | 81.4 | 682 | 2322 | 2574 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 459 | 946 | 1275 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 91 | 341 | 456 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 116 | 0 | 14 | 23.6 | 29 | 103 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 122 | 0 | 30 | 53.6 | 21 | 92 | 160 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 768 | 0 | 14 | 116.2 | 37 | 137 | 275 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 518 | 310 | 60 | 73.1 | 272 | 705 | 854 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1177 | 0 | 60 | 98.1 | 248 | 980 | 1232 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 440 | 0 | 45 | 77.8 | 88 | 349 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 419 | 0 | 14 | 24.3 | 123 | 382 | 623 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 106 | 390 | 30 | 15.8 | 77 | 286 | 426 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 100 | 0 | 7 | 36.4 | 7 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Reorder | 98 | 104 | 45 | 34.9 | 77 | 207 | 291 | 89 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 18.7 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 231 | 908 | 1141 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3602 | 0 | 90 | 570.7 | 196 | 771 | 903 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 78 | 0 | 14 | 36.4 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 52 | 78 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 387 | 0 | 7 | 132.9 | 7 | 31 | 118 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 559 | 275 | 45 | 45.3 | 194 | 762 | 1022 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 602 | 0 | 45 | 250.8 | 29 | 140 | 212 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 560 | 393 | 90 | 78.5 | 218 | 868 | 1017 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 126 | 0 | 7 | 11.4 | 29 | 118 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1199 | 0 | 14 | 110.8 | 63 | 226 | 453 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 107 | 337 | 60 | 30.7 | 74 | 287 | 361 | 0 | 31 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 45 | 0 | 14 | 28.9 | 8 | 32 | 78 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 271 | 363 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 83 | 0 | 30 | 54.1 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1090 | 735 | 90 | 81.3 | 410 | 1631 | 1913 | 0 | 114 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 186 | 0 | 7 | 28.1 | 20 | 73 | 212 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7426 | 0 | 90 | 410.0 | 687 | 2336 | 2589 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4151 | 0 | 60 | 312.4 | 342 | 1153 | 1339 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 246 | 0 | 7 | 28.8 | 28 | 97 | 277 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 233 | 0 | 14 | 46.0 | 32 | 108 | 215 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 55 | 210 | 45 | 21.0 | 33 | 154 | 233 | 0 | 21 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Reorder | 809 | 422 | 90 | 84.8 | 429 | 1298 | 1498 | 267 | — |
| ITEM-0105 | B - Core Products | Healthy | 628 | 0 | 45 | 81.3 | 121 | 477 | 639 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1460 | 773 | 90 | 84.7 | 656 | 2225 | 2466 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 575 | 481 | 60 | 51.7 | 229 | 908 | 1142 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 177 | 915 | 90 | 20.0 | 271 | 1077 | 1263 | 0 | 20 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2170 | 0 | 90 | 147.5 | 559 | 1898 | 2104 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1033 | 622 | 60 | 59.2 | 448 | 1513 | 1757 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 29.6 | 829 | 1635 | 1880 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 37 | 0 | 14 | 25.6 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 72.5 | 267 | 475 | 766 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 83 | 125 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 108 | 648 | 90 | 19.9 | 167 | 661 | 775 | 0 | 20 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 249 | 375 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 48 | 55 | 30 | 25.1 | 16 | 76 | 133 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 214 | 0 | 7 | 15.8 | 36 | 145 | 429 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 285 | 45 | 0.0 | 224 | 429 | 523 | 238 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 63.6 | 94 | 139 | 202 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 216 | 0 | 14 | 21.3 | 58 | 210 | 423 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 30 | 134 | 7 | 4.8 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 18.3 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 138 | 546 | 733 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 128.0 | 655 | 1711 | 1955 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 749 | 0 | 14 | 123.7 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 416 | 0 | 60 | 93.1 | 72 | 345 | 479 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4217 | 0 | 60 | 311.1 | 348 | 1175 | 1365 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 28 | 79 | 111 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 640 | 0 | 14 | 56.5 | 88 | 258 | 417 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 202 | 681 | 896 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1674 | 0 | 60 | 90.9 | 469 | 1593 | 1850 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2506 | 0 | 45 | 255.4 | 154 | 606 | 812 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 628 | 1542 | 1857 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 408 | 479 | 45 | 36.1 | 177 | 698 | 935 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1111 | 0 | 7 | 85.0 | 39 | 144 | 418 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 152 | 589 | 739 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 222 | 636 | 90 | 43.5 | 158 | 623 | 730 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 37.6 | 358 | 679 | 1127 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 576 | 178 | 60 | 100.3 | 122 | 473 | 594 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 55 | 200 | 60 | 28.1 | 33 | 153 | 211 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 790 | 0 | 14 | 115.6 | 41 | 144 | 287 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 243 | 807 | 1062 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 481 | 367 | 7 | 19.9 | 315 | 509 | 848 | 0 | — |
