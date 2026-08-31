# Synthetic Inventory Health

**Simulation date: 2026-08-31**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 56 |
| Lead-time risk | 48 |
| Stockout | 7 |

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
| ITEM-0001 | B - Core Products | Lead-time risk | 4 | 728 | 30 | 0.3 | 130 | 507 | 763 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1147 | 294 | 60 | 77.5 | 378 | 1281 | 1488 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2077 | 0 | 45 | 272.5 | 123 | 474 | 634 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 375 | 0 | 14 | 50.1 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 4 | 142 | 45 | 2.4 | 21 | 99 | 149 | 0 | 3 |
| ITEM-0008 | B - Core Products | Healthy | 351 | 0 | 14 | 33.7 | 66 | 223 | 442 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 77 | 198 | 60 | 30.4 | 42 | 197 | 273 | 0 | 31 |
| ITEM-0010 | B - Core Products | Lead-time risk | 169 | 410 | 90 | 43.2 | 121 | 477 | 560 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2206 | 0 | 7 | 139.8 | 303 | 430 | 651 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 462 | 0 | 90 | 163.7 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1380 | 0 | 7 | 106.9 | 34 | 138 | 409 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 118.1 | 28 | 48 | 121 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 9 | 510 | 45 | 1.3 | 106 | 420 | 563 | 0 | 2 |
| ITEM-0018 | B - Core Products | Excess | 1249 | 0 | 30 | 209.7 | 66 | 251 | 376 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3347 | 0 | 60 | 327.1 | 212 | 837 | 1052 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 114 | 323 | 14 | 10.5 | 65 | 229 | 457 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 597 | 0 | 60 | 342.2 | 29 | 136 | 188 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 122 | 2305 | 90 | 7.1 | 654 | 2224 | 2465 | 0 | 8 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.5 | 8 | 32 | 54 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 87.4 | 685 | 1496 | 1775 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 7 | 243 | 30 | 1.9 | 33 | 147 | 256 | 0 | 2 |
| ITEM-0029 | B - Core Products | Lead-time risk | 399 | 960 | 90 | 43.1 | 286 | 1129 | 1323 | 0 | 44 |
| ITEM-0030 | C - Slow Moving | Healthy | 2 | 35 | 7 | 3.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1418 | 0 | 14 | 146.0 | 59 | 205 | 409 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 12 | 395 | 60 | 3.1 | 64 | 304 | 422 | 0 | 4 |
| ITEM-0033 | B - Core Products | Healthy | 444 | 0 | 45 | 69.3 | 105 | 400 | 535 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 511 | 0 | 14 | 45.6 | 64 | 232 | 468 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 267 | 0 | 14 | 34.0 | 46 | 164 | 329 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 87 | 341 | 513 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 184 | 575 | 30 | 13.6 | 146 | 565 | 848 | 0 | 14 |
| ITEM-0040 | A - Top Movers | Excess | 4731 | 0 | 60 | 345.3 | 356 | 1192 | 1384 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 41.7 | 351 | 589 | 810 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 304 | 0 | 14 | 33.7 | 57 | 193 | 382 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 853 | 0 | 45 | 255.9 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 148.5 | 124 | 393 | 482 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 45 | 192 | 60 | 26.0 | 79 | 185 | 237 | 0 | 26 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 34 | 80 | 45 | 27.6 | 17 | 74 | 111 | 0 | 28 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 62 | 224 | 60 | 42.0 | 102 | 193 | 237 | 0 | 42 |
| ITEM-0052 | B - Core Products | Healthy | 391 | 0 | 7 | 38.5 | 28 | 110 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 261 | 0 | 7 | 34.9 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4743 | 0 | 60 | 328.4 | 378 | 1260 | 1462 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 714 | 0 | 14 | 55.1 | 102 | 297 | 478 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1856 | 580 | 90 | 108.3 | 650 | 2210 | 2449 | 0 | 109 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 379 | 765 | 1027 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 30 | 564 | 45 | 4.3 | 116 | 438 | 585 | 0 | 5 |
| ITEM-0061 | B - Core Products | Lead-time risk | 49 | 145 | 14 | 10.2 | 29 | 102 | 203 | 0 | 11 |
| ITEM-0062 | C - Slow Moving | Healthy | 150 | 0 | 30 | 51.1 | 26 | 117 | 205 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 886 | 0 | 14 | 132.0 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 82.3 | 272 | 714 | 866 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1415 | 0 | 60 | 118.9 | 246 | 972 | 1222 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 552 | 0 | 45 | 96.7 | 89 | 352 | 472 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 779 | 0 | 14 | 46.5 | 122 | 374 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 168 | 390 | 30 | 19.4 | 96 | 364 | 546 | 0 | 20 |
| ITEM-0069 | C - Slow Moving | Healthy | 61 | 0 | 7 | 21.2 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 154 | 104 | 45 | 55.2 | 81 | 210 | 293 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 33 | 0 | 7 | 39.1 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 31 | 1070 | 60 | 2.7 | 236 | 929 | 1167 | 0 | 3 |
| ITEM-0073 | B - Core Products | Excess | 3670 | 0 | 90 | 473.2 | 240 | 946 | 1109 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 1 | 99 | 14 | 0.5 | 10 | 42 | 106 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 2 | 66 | 45 | 2.6 | 11 | 47 | 71 | 0 | 3 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 61.4 | 214 | 412 | 457 | 0 | 62 |
| ITEM-0077 | C - Slow Moving | Excess | 421 | 0 | 7 | 114.8 | 9 | 39 | 149 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 777 | 0 | 45 | 62.3 | 195 | 769 | 1031 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 643 | 0 | 45 | 261.9 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 715 | 235 | 90 | 106.0 | 205 | 819 | 961 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 111 | 328 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1425 | 0 | 14 | 134.7 | 62 | 221 | 443 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 145 | 337 | 60 | 31.7 | 97 | 377 | 473 | 0 | 32 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 329 | 483 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 62 | 0 | 14 | 32.6 | 10 | 39 | 96 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 12 | 365 | 45 | 2.6 | 72 | 284 | 380 | 0 | 3 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 108 | 0 | 30 | 68.0 | 14 | 64 | 111 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1336 | 436 | 90 | 102.9 | 399 | 1581 | 1854 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 31.3 | 241 | 368 | 700 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 6 | 262 | 7 | 0.7 | 28 | 95 | 271 | 0 | 1 |
| ITEM-0095 | A - Top Movers | Excess | 7796 | 0 | 90 | 439.1 | 676 | 2292 | 2541 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4421 | 0 | 60 | 324.5 | 352 | 1183 | 1374 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 11.2 | 110 | 169 | 323 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 4 | 330 | 7 | 0.4 | 33 | 116 | 333 | 0 | 1 |
| ITEM-0100 | B - Core Products | Lead-time risk | 7 | 256 | 14 | 1.1 | 38 | 132 | 263 | 0 | 2 |
| ITEM-0101 | B - Core Products | Healthy | 1204 | 420 | 60 | 85.0 | 571 | 1436 | 1733 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 82 | 210 | 45 | 25.3 | 41 | 191 | 288 | 0 | 26 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 760 | 0 | 45 | 93.8 | 126 | 499 | 669 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1833 | 524 | 90 | 108.4 | 646 | 2185 | 2422 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 806 | 241 | 60 | 74.5 | 224 | 885 | 1112 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 187.2 | 67 | 167 | 263 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 336 | 915 | 90 | 36.6 | 280 | 1116 | 1308 | 0 | 37 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 305.2 | 97 | 247 | 320 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2407 | 0 | 90 | 161.8 | 563 | 1917 | 2126 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1393 | 360 | 60 | 78.5 | 455 | 1538 | 1786 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 863 | 1100 | 45 | 47.9 | 878 | 1708 | 1960 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 13 | 55 | 14 | 8.9 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1023 | 0 | 14 | 55.5 | 314 | 591 | 978 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 3 | 115 | 45 | 2.2 | 17 | 79 | 120 | 0 | 3 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 211 | 530 | 90 | 39.2 | 165 | 656 | 769 | 0 | 40 |
| ITEM-0119 | B - Core Products | Lead-time risk | 11 | 355 | 30 | 1.8 | 65 | 253 | 380 | 0 | 2 |
| ITEM-0120 | C - Slow Moving | Healthy | 87 | 0 | 30 | 46.6 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 469 | 0 | 7 | 36.2 | 37 | 141 | 413 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 4.1 | 102 | 157 | 233 | 0 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 86 | 292 | 14 | 8.2 | 60 | 217 | 437 | 0 | 9 |
| ITEM-0125 | B - Core Products | Healthy | 149 | 0 | 7 | 23.8 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 790 | 30 | 11.1 | 526 | 947 | 1137 | 200 | 12 |
| ITEM-0128 | B - Core Products | Lead-time risk | 20 | 698 | 45 | 2.2 | 139 | 549 | 737 | 0 | 3 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 863 | 0 | 14 | 136.7 | 35 | 130 | 263 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 504 | 0 | 60 | 119.7 | 68 | 325 | 452 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 7 | 135 | 90 | 7.4 | 24 | 110 | 139 | 0 | 8 |
| ITEM-0135 | A - Top Movers | Excess | 4462 | 0 | 60 | 322.8 | 355 | 1199 | 1392 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 756 | 0 | 14 | 52.8 | 107 | 322 | 523 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 242 | 560 | 30 | 16.4 | 195 | 653 | 859 | 0 | 17 |
| ITEM-0140 | A - Top Movers | Healthy | 2052 | 0 | 60 | 114.6 | 458 | 1550 | 1801 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2662 | 0 | 45 | 264.1 | 158 | 622 | 834 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 547 | 1246 | 1486 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 649 | 243 | 45 | 60.0 | 168 | 666 | 893 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1378 | 0 | 7 | 107.3 | 37 | 140 | 410 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 41 | 888 | 60 | 4.6 | 189 | 734 | 922 | 0 | 5 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 277 | 636 | 90 | 44.9 | 190 | 752 | 881 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 431 | 721 | 991 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 640 | 178 | 60 | 83.7 | 162 | 629 | 789 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 76 | 200 | 60 | 30.3 | 42 | 196 | 271 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 933 | 0 | 14 | 136.3 | 40 | 143 | 287 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 278 | 671 | 30 | 16.1 | 230 | 765 | 1007 | 0 | 17 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
