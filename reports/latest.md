# Synthetic Inventory Health

**Simulation date: 2026-10-01**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 84 |
| Lead-time risk | 9 |
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
| ITEM-0001 | B - Core Products | Healthy | 720 | 0 | 30 | 58.9 | 130 | 509 | 766 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 657 | 737 | 60 | 42.2 | 399 | 1350 | 1568 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1966 | 0 | 45 | 362.6 | 87 | 337 | 451 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 150 | 160 | 14 | 19.7 | 43 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 189 | 0 | 14 | 25.2 | 48 | 161 | 318 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 42 | 198 | 60 | 24.9 | 29 | 133 | 183 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 117 | 410 | 90 | 45.8 | 79 | 312 | 366 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 378 | 0 | 90 | 129.4 | 69 | 335 | 423 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 982 | 0 | 7 | 78.5 | 33 | 134 | 396 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 76 | 196 | 274 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1168 | 0 | 30 | 286.4 | 47 | 174 | 260 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3010 | 0 | 60 | 289.4 | 215 | 850 | 1068 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 273 | 0 | 14 | 34.1 | 50 | 171 | 339 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 571 | 0 | 60 | 443.0 | 23 | 102 | 141 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 619 | 2101 | 2329 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 81.5 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 231 | 0 | 30 | 85.6 | 31 | 115 | 172 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 264 | 960 | 90 | 39.9 | 206 | 808 | 947 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1282 | 0 | 14 | 195.2 | 40 | 139 | 277 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 374 | 0 | 60 | 88.1 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 361 | 0 | 45 | 86.9 | 69 | 261 | 348 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 685 | 0 | 60 | 342.5 | 73 | 195 | 255 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 145 | 245 | 14 | 12.5 | 66 | 240 | 484 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 159 | 0 | 14 | 30.7 | 31 | 109 | 218 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 422 | 0 | 30 | 51.3 | 88 | 344 | 517 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 496 | 290 | 30 | 34.6 | 154 | 599 | 900 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4533 | 0 | 60 | 484.0 | 246 | 818 | 949 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 494 | 270 | 14 | 34.5 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 165 | 0 | 14 | 26.1 | 40 | 135 | 268 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 743 | 0 | 45 | 220.0 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 66 | 153 | 196 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 13 | 80 | 45 | 14.4 | 13 | 55 | 82 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 70 | 218 | 7 | 6.9 | 26 | 107 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 51 | 155 | 7 | 7.1 | 20 | 78 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4529 | 0 | 60 | 426.8 | 280 | 928 | 1076 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 505 | 0 | 14 | 54.0 | 74 | 215 | 346 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1266 | 1125 | 90 | 69.9 | 685 | 2335 | 2588 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 75 | 284 | 378 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 57 | 110 | 14 | 11.5 | 29 | 104 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 108 | 0 | 30 | 55.2 | 18 | 79 | 138 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 685 | 0 | 14 | 101.4 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Reorder | 1013 | 0 | 60 | 81.6 | 255 | 1013 | 1273 | 260 | — |
| ITEM-0066 | B - Core Products | Healthy | 380 | 0 | 45 | 69.5 | 85 | 337 | 452 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 231 | 245 | 14 | 13.9 | 120 | 370 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 448 | 0 | 30 | 76.9 | 67 | 248 | 370 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 65 | 0 | 7 | 22.9 | 6 | 29 | 115 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 9 | 25 | 7 | 11.2 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 884 | 1110 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3559 | 0 | 90 | 656.4 | 168 | 662 | 776 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 53 | 0 | 14 | 25.1 | 10 | 42 | 105 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 66 | 0 | 45 | 78.2 | 12 | 51 | 77 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 370 | 0 | 7 | 143.5 | 7 | 28 | 105 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 442 | 540 | 45 | 37.0 | 187 | 736 | 987 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 576 | 0 | 45 | 243.4 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 499 | 393 | 90 | 71.9 | 212 | 844 | 990 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 221 | 0 | 7 | 19.6 | 28 | 119 | 356 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1062 | 0 | 14 | 96.1 | 64 | 230 | 462 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 88 | 337 | 60 | 30.6 | 61 | 237 | 297 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 63.7 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 37 | 0 | 14 | 27.8 | 8 | 28 | 68 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 358 | 0 | 45 | 83.9 | 52 | 249 | 377 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 113 | 702 | 14 | 7.7 | 391 | 612 | 819 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 68 | 0 | 30 | 44.7 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 916 | 735 | 90 | 68.8 | 406 | 1618 | 1897 | 0 | 102 |
| ITEM-0093 | B - Core Products | Healthy | 608 | 0 | 7 | 37.0 | 239 | 371 | 715 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 139 | 0 | 7 | 24.2 | 18 | 65 | 185 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7230 | 0 | 90 | 394.8 | 694 | 2361 | 2617 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3953 | 0 | 60 | 289.0 | 352 | 1187 | 1378 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 198 | 0 | 7 | 27.5 | 23 | 81 | 232 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 197 | 0 | 14 | 44.9 | 28 | 94 | 186 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 40 | 210 | 45 | 17.3 | 30 | 137 | 206 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 554 | 0 | 45 | 74.1 | 119 | 463 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1286 | 1041 | 90 | 76.0 | 644 | 2183 | 2420 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 448 | 481 | 60 | 40.0 | 230 | 914 | 1149 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 60 | 1100 | 90 | 6.7 | 274 | 1090 | 1279 | 0 | 7 |
| ITEM-0110 | C - Slow Moving | Excess | 644 | 0 | 60 | 198.5 | 112 | 310 | 408 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1994 | 0 | 90 | 139.5 | 543 | 1844 | 2044 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 835 | 902 | 60 | 48.0 | 447 | 1509 | 1752 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 21 | 45 | 14 | 14.4 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.7 | 263 | 455 | 723 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 36 | 648 | 90 | 6.7 | 166 | 657 | 770 | 0 | 7 |
| ITEM-0119 | B - Core Products | Healthy | 330 | 0 | 30 | 56.6 | 63 | 244 | 367 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 21 | 114 | 30 | 10.5 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 356 | 0 | 7 | 26.3 | 35 | 144 | 428 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 113 | 216 | 14 | 11.4 | 57 | 207 | 415 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 101 | 0 | 7 | 17.1 | 16 | 64 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 919 | 200 | 30 | 108.3 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 558 | 747 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1284 | 697 | 90 | 95.1 | 717 | 1946 | 2229 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 691 | 0 | 14 | 118.5 | 33 | 121 | 243 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 372 | 0 | 60 | 85.6 | 70 | 336 | 466 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 115 | 145 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4051 | 0 | 60 | 295.9 | 352 | 1188 | 1379 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 552 | 0 | 14 | 55.3 | 77 | 227 | 367 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 492 | 227 | 30 | 31.5 | 165 | 649 | 977 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1478 | 269 | 60 | 81.5 | 464 | 1571 | 1825 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2383 | 0 | 45 | 242.1 | 154 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 552 | 1320 | 1584 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 315 | 479 | 45 | 29.0 | 171 | 671 | 899 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 969 | 0 | 7 | 75.1 | 38 | 142 | 413 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 129 | 504 | 633 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 196 | 636 | 90 | 44.9 | 135 | 533 | 625 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 44.3 | 338 | 610 | 990 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 147.4 | 218 | 365 | 570 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 716 | 0 | 60 | 139.8 | 110 | 423 | 531 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 38 | 200 | 60 | 21.8 | 29 | 136 | 188 | 0 | 22 |
| ITEM-0155 | B - Core Products | Excess | 694 | 0 | 14 | 98.8 | 41 | 147 | 294 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 556 | 259 | 30 | 30.7 | 240 | 802 | 1055 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 26.9 | 301 | 487 | 810 | 0 | — |
