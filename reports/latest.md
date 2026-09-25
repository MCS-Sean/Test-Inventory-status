# Synthetic Inventory Health

**Simulation date: 2026-09-25**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 71 |
| Lead-time risk | 12 |
| Reorder | 3 |
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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 498 | 748 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 116 | 195 | 7 | 15.8 | 98 | 157 | 311 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 740 | 737 | 60 | 47.4 | 399 | 1352 | 1570 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1984 | 0 | 45 | 338.2 | 95 | 365 | 489 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 202 | 0 | 14 | 26.9 | 43 | 156 | 314 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 214 | 0 | 14 | 27.1 | 50 | 169 | 335 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 46 | 198 | 60 | 25.4 | 31 | 142 | 196 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 127 | 410 | 90 | 46.7 | 85 | 333 | 390 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 8.4 | 755 | 1565 | 1750 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 394 | 0 | 90 | 137.4 | 68 | 329 | 415 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1038 | 0 | 7 | 81.4 | 33 | 136 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 270 | 0 | 7 | 227.1 | 19 | 29 | 65 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 77 | 198 | 277 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 549 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1186 | 0 | 30 | 265.5 | 52 | 191 | 285 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3067 | 0 | 60 | 289.6 | 218 | 864 | 1087 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 303 | 0 | 14 | 35.7 | 52 | 180 | 358 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 577 | 0 | 60 | 436.4 | 23 | 104 | 144 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 627 | 2128 | 2359 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 49 | 0 | 30 | 72.3 | 8 | 30 | 50 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 25 | 113 | 198 | 0 | 1 |
| ITEM-0029 | B - Core Products | Healthy | 286 | 960 | 90 | 40.0 | 222 | 873 | 1023 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1313 | 0 | 14 | 189.1 | 42 | 147 | 292 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 67 | 322 | 447 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 375 | 0 | 45 | 82.5 | 75 | 285 | 380 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 309.7 | 77 | 214 | 282 | 0 | — |
| ITEM-0035 | B - Core Products | Reorder | 226 | 0 | 14 | 20.0 | 64 | 234 | 471 | 245 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 180 | 0 | 14 | 31.2 | 36 | 123 | 244 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 473 | 0 | 30 | 57.7 | 88 | 343 | 515 | 0 | — |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 149 | 576 | 865 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4561 | 0 | 60 | 449.6 | 266 | 885 | 1027 | 0 | — |
| ITEM-0041 | A - Top Movers | Reorder | 299 | 195 | 14 | 20.9 | 344 | 559 | 760 | 270 | — |
| ITEM-0042 | B - Core Products | Healthy | 194 | 0 | 14 | 29.5 | 42 | 141 | 279 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 615 | 1692 | 1941 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 762 | 0 | 45 | 227.8 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 140 | 181 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 16 | 80 | 45 | 16.0 | 14 | 60 | 90 | 0 | 17 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 134 | 0 | 7 | 13.3 | 25 | 106 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 85 | 0 | 7 | 11.7 | 20 | 79 | 232 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4558 | 0 | 60 | 411.0 | 292 | 969 | 1124 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 537 | 0 | 14 | 52.8 | 83 | 236 | 379 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1366 | 1125 | 90 | 75.3 | 686 | 2337 | 2590 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 51.6 | 479 | 961 | 1288 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 82 | 309 | 413 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 84 | 110 | 14 | 16.8 | 29 | 104 | 209 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 111 | 0 | 30 | 51.5 | 20 | 87 | 152 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 725 | 0 | 14 | 107.7 | 38 | 139 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1094 | 0 | 60 | 89.3 | 252 | 999 | 1257 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 406 | 0 | 45 | 72.1 | 88 | 348 | 466 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 326 | 245 | 14 | 19.4 | 121 | 373 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 472 | 0 | 30 | 76.0 | 71 | 264 | 394 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 82 | 0 | 7 | 29.6 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 58 | 193 | 45 | 17.8 | 84 | 234 | 332 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 12 | 0 | 7 | 14.6 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 227 | 893 | 1122 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3579 | 0 | 90 | 591.0 | 188 | 740 | 867 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 67 | 0 | 14 | 32.2 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 53 | 79 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 380 | 0 | 7 | 139.0 | 7 | 29 | 111 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 498 | 275 | 45 | 40.9 | 191 | 751 | 1007 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 589 | 0 | 45 | 245.4 | 29 | 140 | 212 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 524 | 393 | 90 | 73.1 | 219 | 872 | 1022 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 52 | 235 | 7 | 4.6 | 28 | 118 | 353 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1135 | 0 | 14 | 103.7 | 64 | 229 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 99 | 337 | 60 | 31.4 | 67 | 260 | 326 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 43 | 0 | 14 | 30.2 | 8 | 30 | 72 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 264 | 354 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Reorder | 297 | 347 | 14 | 15.7 | 451 | 735 | 999 | 355 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 76 | 0 | 30 | 50.7 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1004 | 735 | 90 | 74.9 | 410 | 1631 | 1913 | 0 | 108 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 50.6 | 231 | 350 | 662 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 157 | 0 | 7 | 24.8 | 19 | 70 | 203 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7339 | 0 | 90 | 409.2 | 682 | 2314 | 2565 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4060 | 0 | 60 | 303.7 | 345 | 1161 | 1348 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 224 | 0 | 7 | 29.0 | 24 | 86 | 249 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 215 | 0 | 14 | 46.6 | 29 | 99 | 195 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 46 | 210 | 45 | 18.7 | 31 | 144 | 218 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 773 | 689 | 90 | 84.3 | 419 | 1254 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 586 | 0 | 45 | 76.5 | 121 | 474 | 634 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1366 | 1041 | 90 | 80.1 | 650 | 2203 | 2441 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 520 | 481 | 60 | 46.6 | 230 | 912 | 1146 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 116 | 1100 | 90 | 13.1 | 270 | 1076 | 1262 | 0 | 14 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2083 | 0 | 90 | 144.0 | 550 | 1867 | 2069 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 929 | 622 | 60 | 53.2 | 448 | 1513 | 1758 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 31 | 0 | 14 | 22.0 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 83 | 125 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 78 | 648 | 90 | 14.7 | 164 | 648 | 759 | 0 | 15 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 250 | 376 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 31 | 55 | 30 | 15.6 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 131 | 290 | 7 | 9.6 | 36 | 146 | 433 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 158 | 216 | 14 | 15.5 | 58 | 211 | 425 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 134 | 0 | 7 | 22.4 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 941 | 200 | 30 | 114.1 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 558 | 747 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 724 | 0 | 14 | 124.8 | 33 | 120 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 385 | 0 | 60 | 84.1 | 73 | 353 | 490 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 114 | 144 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4120 | 0 | 60 | 294.3 | 358 | 1212 | 1408 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 29 | 80 | 112 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 594 | 0 | 14 | 56.3 | 81 | 240 | 388 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 204 | 688 | 906 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1570 | 269 | 60 | 85.2 | 471 | 1596 | 1854 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2442 | 0 | 45 | 247.2 | 155 | 610 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 369 | 479 | 45 | 33.6 | 173 | 678 | 909 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1031 | 0 | 7 | 79.3 | 38 | 142 | 415 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 142 | 553 | 695 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 207 | 636 | 90 | 44.3 | 145 | 571 | 669 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 734 | 0 | 60 | 134.5 | 117 | 450 | 565 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 43 | 200 | 60 | 22.6 | 32 | 148 | 205 | 0 | 23 |
| ITEM-0155 | B - Core Products | Excess | 740 | 0 | 14 | 106.2 | 41 | 146 | 292 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 662 | 259 | 30 | 36.6 | 242 | 804 | 1057 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 23.3 | 325 | 539 | 914 | 0 | — |
