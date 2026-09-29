# Synthetic Inventory Health

**Simulation date: 2026-09-29**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 83 |
| Lead-time risk | 9 |
| Reorder | 1 |
| Stockout | 19 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 504 | 758 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 28.3 | 104 | 170 | 342 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 700 | 737 | 60 | 45.1 | 397 | 1344 | 1562 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1973 | 0 | 45 | 355.9 | 89 | 345 | 461 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 163 | 0 | 14 | 21.4 | 44 | 159 | 319 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 198 | 0 | 14 | 26.1 | 48 | 162 | 321 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 44 | 198 | 60 | 25.7 | 29 | 134 | 185 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 120 | 410 | 90 | 45.8 | 81 | 320 | 375 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 382 | 0 | 90 | 131.2 | 69 | 334 | 422 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1006 | 0 | 7 | 79.9 | 33 | 134 | 399 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 76 | 196 | 274 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1174 | 0 | 30 | 281.8 | 48 | 178 | 265 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3024 | 0 | 60 | 289.2 | 216 | 854 | 1074 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 282 | 0 | 14 | 34.7 | 50 | 172 | 343 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 571 | 0 | 60 | 431.8 | 23 | 104 | 144 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 614 | 2083 | 2308 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 75.8 | 7 | 27 | 46 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 235 | 0 | 30 | 85.3 | 31 | 117 | 175 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 272 | 960 | 90 | 39.9 | 213 | 834 | 978 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1292 | 0 | 14 | 191.9 | 41 | 142 | 284 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 387 | 0 | 60 | 92.9 | 67 | 322 | 447 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 367 | 0 | 45 | 87.4 | 69 | 263 | 351 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 685 | 0 | 60 | 327.9 | 73 | 201 | 264 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 168 | 245 | 14 | 14.6 | 66 | 240 | 482 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 167 | 0 | 14 | 31.1 | 33 | 114 | 227 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 444 | 0 | 30 | 54.3 | 88 | 342 | 514 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 531 | 290 | 30 | 37.6 | 152 | 590 | 887 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4541 | 0 | 60 | 475.8 | 250 | 833 | 966 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 299 | 465 | 14 | 20.9 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 172 | 0 | 14 | 26.6 | 41 | 138 | 274 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 748 | 0 | 45 | 220.0 | 41 | 198 | 300 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 72 | 175 | 225 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 15 | 80 | 45 | 16.1 | 14 | 57 | 85 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 90 | 218 | 7 | 8.9 | 25 | 106 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 58 | 155 | 7 | 8.0 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4542 | 0 | 60 | 425.4 | 282 | 934 | 1083 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 516 | 0 | 14 | 52.7 | 80 | 227 | 364 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1297 | 1125 | 90 | 71.3 | 687 | 2344 | 2598 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 54.0 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 78 | 294 | 392 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 67 | 110 | 14 | 13.6 | 28 | 102 | 205 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 109 | 0 | 30 | 53.9 | 19 | 82 | 143 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 698 | 0 | 14 | 102.6 | 38 | 140 | 283 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1039 | 0 | 60 | 83.9 | 255 | 1011 | 1270 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 391 | 0 | 45 | 70.9 | 86 | 340 | 456 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 265 | 245 | 14 | 15.9 | 120 | 371 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 456 | 0 | 30 | 77.6 | 68 | 251 | 374 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 70 | 0 | 7 | 24.7 | 6 | 29 | 114 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 9 | 25 | 7 | 11.1 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 226 | 889 | 1118 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3566 | 0 | 90 | 640.6 | 173 | 680 | 797 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 58 | 0 | 14 | 27.6 | 10 | 42 | 105 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 374 | 0 | 7 | 143.8 | 7 | 28 | 106 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 453 | 540 | 45 | 37.5 | 190 | 746 | 999 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 582 | 0 | 45 | 247.1 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 503 | 393 | 90 | 71.5 | 215 | 856 | 1003 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 248 | 0 | 7 | 22.1 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1087 | 0 | 14 | 99.3 | 64 | 229 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 92 | 337 | 60 | 31.0 | 63 | 244 | 307 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 39 | 0 | 14 | 28.8 | 8 | 29 | 69 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Stockout | 0 | 365 | 45 | 0.0 | 52 | 250 | 378 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 297 | 702 | 14 | 21.2 | 373 | 583 | 779 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 72 | 0 | 30 | 48.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 954 | 735 | 90 | 70.8 | 411 | 1637 | 1920 | 0 | 104 |
| ITEM-0093 | B - Core Products | Healthy | 608 | 0 | 7 | 37.0 | 239 | 371 | 715 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 143 | 0 | 7 | 24.1 | 18 | 66 | 191 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7254 | 0 | 90 | 394.7 | 697 | 2370 | 2627 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3986 | 0 | 60 | 293.8 | 350 | 1178 | 1368 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 205 | 0 | 7 | 27.7 | 24 | 84 | 239 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 201 | 0 | 14 | 45.6 | 28 | 95 | 187 | 0 | — |
| ITEM-0101 | A - Top Movers | Reorder | 761 | 420 | 60 | 63.8 | 630 | 1358 | 1525 | 345 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 43 | 210 | 45 | 18.6 | 30 | 137 | 206 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 571 | 0 | 45 | 76.7 | 118 | 461 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1311 | 1041 | 90 | 77.5 | 644 | 2183 | 2420 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 470 | 481 | 60 | 41.8 | 231 | 918 | 1154 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 73 | 1100 | 90 | 8.1 | 276 | 1099 | 1288 | 0 | 9 |
| ITEM-0110 | C - Slow Moving | Healthy | 644 | 0 | 60 | 184.0 | 115 | 329 | 434 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2013 | 0 | 90 | 139.9 | 546 | 1856 | 2057 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 848 | 902 | 60 | 47.5 | 458 | 1548 | 1798 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 23 | 45 | 14 | 15.8 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 52 | 648 | 90 | 9.8 | 164 | 648 | 759 | 0 | 10 |
| ITEM-0119 | B - Core Products | Healthy | 343 | 0 | 30 | 58.6 | 63 | 245 | 368 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 26 | 55 | 30 | 13.1 | 17 | 79 | 138 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 78 | 290 | 7 | 5.7 | 36 | 145 | 431 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 125 | 216 | 14 | 12.4 | 58 | 210 | 422 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 113 | 0 | 7 | 19.0 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 919 | 200 | 30 | 108.3 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 560 | 750 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 698 | 0 | 14 | 119.4 | 33 | 121 | 244 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 377 | 0 | 60 | 84.8 | 72 | 344 | 477 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 113 | 142 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4091 | 0 | 60 | 300.3 | 350 | 1181 | 1372 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 29 | 80 | 112 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 561 | 0 | 14 | 54.6 | 79 | 234 | 378 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 520 | 227 | 30 | 33.5 | 164 | 646 | 972 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1506 | 269 | 60 | 82.0 | 469 | 1589 | 1846 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2404 | 0 | 45 | 241.2 | 156 | 615 | 824 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 334 | 479 | 45 | 30.9 | 170 | 668 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 994 | 0 | 7 | 76.5 | 38 | 142 | 415 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 132 | 517 | 649 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 197 | 636 | 90 | 44.2 | 138 | 544 | 638 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 136.9 | 223 | 381 | 602 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 723 | 0 | 60 | 138.4 | 112 | 431 | 541 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 39 | 200 | 60 | 21.8 | 30 | 140 | 193 | 0 | 22 |
| ITEM-0155 | B - Core Products | Excess | 711 | 0 | 14 | 101.9 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 585 | 259 | 30 | 32.1 | 242 | 808 | 1063 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 26.9 | 301 | 487 | 810 | 0 | — |
