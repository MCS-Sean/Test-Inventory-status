# Synthetic Inventory Health

**Simulation date: 2026-09-26**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 73 |
| Lead-time risk | 13 |
| Reorder | 2 |
| Stockout | 23 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 501 | 752 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 37 | 195 | 7 | 4.5 | 104 | 170 | 342 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 728 | 737 | 60 | 46.6 | 399 | 1353 | 1572 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1981 | 0 | 45 | 348.9 | 91 | 353 | 472 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 193 | 0 | 14 | 25.4 | 43 | 157 | 317 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 209 | 0 | 14 | 26.8 | 49 | 166 | 330 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 45 | 198 | 60 | 25.6 | 30 | 138 | 190 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 125 | 410 | 90 | 46.1 | 84 | 331 | 388 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.5 | 705 | 1417 | 1580 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 392 | 0 | 90 | 136.7 | 68 | 329 | 415 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1027 | 0 | 7 | 80.5 | 33 | 136 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 270 | 0 | 7 | 227.1 | 19 | 29 | 65 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 77 | 198 | 277 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 411 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1182 | 0 | 30 | 270.0 | 51 | 187 | 279 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3054 | 0 | 60 | 288.4 | 218 | 864 | 1087 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 299 | 0 | 14 | 35.7 | 52 | 178 | 354 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 576 | 0 | 60 | 435.6 | 23 | 104 | 144 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 613 | 2081 | 2306 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 49 | 0 | 30 | 73.5 | 8 | 29 | 49 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 25 | 112 | 196 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 282 | 960 | 90 | 40.1 | 219 | 860 | 1007 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1308 | 0 | 14 | 190.2 | 42 | 146 | 290 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 67 | 322 | 447 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 371 | 0 | 45 | 84.3 | 72 | 275 | 367 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 351.4 | 72 | 193 | 252 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 200 | 245 | 14 | 17.4 | 65 | 237 | 478 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 177 | 0 | 14 | 31.1 | 35 | 121 | 241 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 468 | 0 | 30 | 57.4 | 87 | 340 | 512 | 0 | — |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 151 | 583 | 876 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4554 | 0 | 60 | 457.9 | 260 | 867 | 1006 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 299 | 465 | 14 | 20.9 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 190 | 0 | 14 | 28.7 | 42 | 142 | 280 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 633 | 1776 | 2040 | 295 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 760 | 0 | 45 | 227.2 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 140 | 181 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 16 | 80 | 45 | 16.2 | 14 | 60 | 90 | 0 | 17 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 119 | 0 | 7 | 11.8 | 26 | 107 | 320 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 82 | 0 | 7 | 11.4 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4556 | 0 | 60 | 410.0 | 292 | 970 | 1126 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 534 | 0 | 14 | 54.2 | 80 | 228 | 366 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1349 | 1125 | 90 | 74.5 | 685 | 2334 | 2587 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 54.0 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 81 | 305 | 408 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 79 | 110 | 14 | 15.9 | 29 | 104 | 209 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 109 | 0 | 30 | 50.8 | 19 | 86 | 150 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 723 | 0 | 14 | 107.2 | 38 | 140 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1080 | 0 | 60 | 87.8 | 253 | 1004 | 1262 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 399 | 0 | 45 | 70.8 | 88 | 348 | 466 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 306 | 245 | 14 | 18.3 | 121 | 372 | 605 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 468 | 0 | 30 | 76.9 | 70 | 259 | 387 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 80 | 0 | 7 | 28.8 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Lead-time risk | 26 | 193 | 45 | 7.2 | 90 | 257 | 365 | 146 | 8 |
| ITEM-0071 | C - Slow Moving | Reorder | 10 | 0 | 7 | 12.2 | 3 | 10 | 35 | 25 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 228 | 896 | 1126 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3577 | 0 | 90 | 602.9 | 185 | 725 | 850 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 65 | 0 | 14 | 31.3 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 53 | 79 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 378 | 0 | 7 | 137.2 | 7 | 30 | 112 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 485 | 275 | 45 | 40.0 | 190 | 749 | 1003 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 586 | 0 | 45 | 244.2 | 29 | 140 | 212 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 517 | 393 | 90 | 72.4 | 218 | 869 | 1019 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 281 | 0 | 7 | 25.1 | 28 | 118 | 353 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1123 | 0 | 14 | 103.1 | 63 | 227 | 455 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 97 | 337 | 60 | 31.1 | 67 | 258 | 324 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 42 | 0 | 14 | 29.8 | 8 | 30 | 72 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 265 | 356 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 297 | 702 | 14 | 18.0 | 417 | 665 | 897 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 75 | 0 | 30 | 49.6 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 987 | 735 | 90 | 72.9 | 413 | 1645 | 1929 | 0 | 106 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 50.6 | 231 | 350 | 662 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 154 | 0 | 7 | 24.6 | 19 | 70 | 201 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7316 | 0 | 90 | 404.4 | 687 | 2334 | 2587 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4034 | 0 | 60 | 300.0 | 347 | 1168 | 1356 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 220 | 0 | 7 | 28.7 | 24 | 86 | 247 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 212 | 0 | 14 | 46.7 | 29 | 98 | 193 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 45 | 210 | 45 | 18.8 | 30 | 140 | 212 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 584 | 0 | 45 | 76.7 | 120 | 471 | 630 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1343 | 1041 | 90 | 77.6 | 658 | 2234 | 2476 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 505 | 481 | 60 | 45.3 | 230 | 911 | 1145 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 104 | 1100 | 90 | 11.7 | 272 | 1082 | 1269 | 0 | 12 |
| ITEM-0110 | C - Slow Moving | Healthy | 644 | 0 | 60 | 184.0 | 115 | 329 | 434 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2060 | 0 | 90 | 141.9 | 553 | 1875 | 2078 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 907 | 622 | 60 | 51.6 | 450 | 1522 | 1768 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Reorder | 28 | 0 | 14 | 19.7 | 7 | 29 | 71 | 45 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 83 | 125 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 72 | 648 | 90 | 13.5 | 164 | 650 | 762 | 0 | 14 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 248 | 373 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 29 | 55 | 30 | 14.6 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 118 | 290 | 7 | 8.6 | 36 | 146 | 433 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 149 | 216 | 14 | 14.6 | 58 | 212 | 426 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 131 | 0 | 7 | 22.0 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 941 | 200 | 30 | 114.1 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 559 | 750 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 719 | 0 | 14 | 124.0 | 33 | 120 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 382 | 0 | 60 | 83.2 | 74 | 354 | 492 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 114 | 144 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4109 | 0 | 60 | 294.2 | 358 | 1210 | 1406 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 29 | 80 | 112 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 588 | 0 | 14 | 55.9 | 81 | 239 | 387 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 548 | 227 | 30 | 35.2 | 204 | 688 | 906 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1560 | 269 | 60 | 85.9 | 464 | 1573 | 1827 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2431 | 0 | 45 | 244.2 | 156 | 614 | 824 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 360 | 479 | 45 | 32.7 | 173 | 680 | 911 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1024 | 0 | 7 | 79.3 | 38 | 142 | 413 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 137 | 535 | 672 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 204 | 636 | 90 | 44.7 | 141 | 557 | 653 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 730 | 0 | 60 | 136.3 | 114 | 441 | 554 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 43 | 200 | 60 | 23.0 | 31 | 145 | 201 | 0 | 24 |
| ITEM-0155 | B - Core Products | Excess | 732 | 0 | 14 | 105.1 | 41 | 146 | 292 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 647 | 259 | 30 | 35.7 | 242 | 804 | 1057 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 25.3 | 309 | 507 | 851 | 0 | — |
