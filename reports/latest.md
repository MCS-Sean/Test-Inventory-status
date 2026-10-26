# Synthetic Inventory Health

**Simulation date: 2026-10-26**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 90 |
| Lead-time risk | 4 |
| Reorder | 2 |
| Stockout | 12 |

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
| ITEM-0001 | B - Core Products | Healthy | 346 | 291 | 30 | 26.3 | 139 | 548 | 825 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 313 | 0 | 7 | 50.4 | 91 | 141 | 272 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 530 | 890 | 60 | 33.5 | 405 | 1371 | 1592 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1876 | 0 | 45 | 442.0 | 68 | 264 | 353 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 141 | 155 | 14 | 20.0 | 41 | 147 | 295 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 114 | 0 | 45 | 73.8 | 20 | 92 | 138 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 198 | 0 | 14 | 33.7 | 34 | 123 | 246 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 205 | 0 | 60 | 156.4 | 22 | 102 | 142 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 77 | 410 | 90 | 39.6 | 61 | 238 | 279 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 2145 | 0 | 60 | 131.1 | 866 | 1865 | 2094 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 313 | 90 | 90 | 111.3 | 67 | 323 | 408 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 618 | 0 | 7 | 47.9 | 35 | 139 | 410 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 365 | 155 | 45 | 54.2 | 105 | 415 | 557 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1110 | 0 | 30 | 353.0 | 37 | 135 | 201 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2777 | 0 | 60 | 271.4 | 212 | 837 | 1052 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 164 | 0 | 14 | 27.6 | 35 | 124 | 249 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 556 | 0 | 60 | 602.9 | 17 | 74 | 101 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 599 | 2034 | 2255 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 31 | 0 | 30 | 54.7 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 500 | 1169 | 60 | 50.8 | 545 | 1146 | 1353 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 189 | 0 | 30 | 90.0 | 18 | 84 | 147 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 154 | 960 | 90 | 30.8 | 153 | 608 | 713 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1187 | 0 | 14 | 240.6 | 30 | 104 | 208 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 265 | 135 | 60 | 60.8 | 70 | 336 | 467 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 285 | 0 | 45 | 87.5 | 52 | 202 | 271 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 105 | 265 | 14 | 8.8 | 67 | 246 | 496 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 75 | 95 | 14 | 18.0 | 25 | 88 | 175 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 230 | 172 | 30 | 27.5 | 89 | 349 | 524 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 413 | 315 | 30 | 28.2 | 156 | 611 | 919 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4369 | 0 | 60 | 607.7 | 185 | 624 | 725 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 45.6 | 242 | 407 | 637 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 65 | 116 | 14 | 13.9 | 28 | 99 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 665 | 0 | 45 | 200.2 | 41 | 194 | 294 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 760 | 60 | 0.0 | 306 | 795 | 963 | 205 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 74 | 0 | 45 | 102.5 | 11 | 45 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 201 | 351 | 60 | 46.4 | 157 | 422 | 552 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 31 | 231 | 7 | 3.0 | 25 | 109 | 328 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 159 | 0 | 7 | 21.4 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4350 | 0 | 60 | 535.6 | 212 | 708 | 822 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 335 | 0 | 14 | 44.7 | 55 | 168 | 273 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 804 | 1680 | 90 | 44.1 | 689 | 2347 | 2602 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 100.5 | 429 | 781 | 1019 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 521 | 0 | 45 | 144.3 | 58 | 225 | 300 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 43 | 110 | 14 | 8.7 | 28 | 103 | 206 | 0 | 9 |
| ITEM-0062 | C - Slow Moving | Healthy | 76 | 0 | 30 | 51.4 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 543 | 0 | 14 | 84.1 | 37 | 134 | 270 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 312 | 310 | 60 | 53.2 | 235 | 593 | 717 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 715 | 525 | 60 | 59.3 | 249 | 985 | 1238 | 0 | — |
| ITEM-0066 | B - Core Products | Lead-time risk | 222 | 115 | 45 | 39.3 | 89 | 349 | 468 | 131 | 60 |
| ITEM-0067 | A - Top Movers | Healthy | 328 | 245 | 14 | 20.3 | 118 | 361 | 587 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 356 | 0 | 30 | 81.5 | 49 | 185 | 277 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 85 | 0 | 7 | 31.1 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 29.6 | 3 | 9 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 227 | 895 | 1125 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3467 | 0 | 90 | 802.1 | 132 | 526 | 617 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 65 | 0 | 14 | 31.1 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 36 | 26 | 45 | 38.6 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 334 | 0 | 7 | 167.9 | 5 | 21 | 81 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 447 | 265 | 45 | 39.2 | 179 | 704 | 944 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 523 | 0 | 45 | 234.2 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 315 | 558 | 90 | 45.3 | 214 | 847 | 994 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 189 | 0 | 7 | 16.8 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 790 | 0 | 14 | 70.9 | 64 | 232 | 466 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 30 | 337 | 60 | 12.7 | 50 | 194 | 244 | 0 | — |
| ITEM-0085 | B - Core Products | Stockout | 0 | 605 | 14 | 0.0 | 243 | 414 | 652 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 16 | 35 | 14 | 15.5 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 244 | 135 | 45 | 56.0 | 53 | 254 | 385 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 523 | 468 | 14 | 28.4 | 368 | 645 | 1031 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 29 | 50 | 30 | 19.2 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 637 | 1027 | 90 | 50.7 | 382 | 1525 | 1789 | 0 | 86 |
| ITEM-0093 | A - Top Movers | Reorder | 307 | 0 | 7 | 14.9 | 336 | 501 | 789 | 485 | — |
| ITEM-0094 | B - Core Products | Healthy | 30 | 104 | 7 | 6.1 | 14 | 54 | 157 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6790 | 0 | 90 | 377.2 | 684 | 2322 | 2574 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3591 | 0 | 60 | 254.1 | 361 | 1224 | 1421 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 47.6 | 104 | 155 | 286 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 88 | 0 | 7 | 16.4 | 16 | 60 | 172 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 130 | 0 | 14 | 39.8 | 19 | 68 | 137 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 66.3 | 642 | 1428 | 1608 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 206 | 0 | 45 | 108.4 | 24 | 112 | 169 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 359 | 180 | 45 | 48.4 | 118 | 459 | 615 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 871 | 1542 | 90 | 50.9 | 649 | 2207 | 2446 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 421 | 499 | 60 | 38.3 | 226 | 897 | 1128 | 0 | 61 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 267 | 1062 | 1246 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1584 | 220 | 90 | 113.8 | 534 | 1801 | 1996 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 370 | 1161 | 60 | 21.1 | 451 | 1522 | 1767 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 108.1 | 665 | 1289 | 1479 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 33 | 0 | 14 | 23.4 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 908 | 0 | 14 | 94.0 | 236 | 381 | 584 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 173 | 683 | 801 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 176 | 135 | 30 | 29.4 | 64 | 250 | 375 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 39 | 59 | 30 | 20.9 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 95 | 285 | 7 | 7.4 | 34 | 138 | 409 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 49 | 146 | 14 | 13.1 | 105 | 162 | 240 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 81 | 216 | 14 | 8.1 | 58 | 209 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 71 | 0 | 7 | 12.2 | 16 | 63 | 185 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 561 | 0 | 45 | 62.5 | 141 | 554 | 743 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 955 | 1320 | 90 | 67.8 | 740 | 2022 | 2317 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 516 | 0 | 14 | 84.6 | 35 | 127 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 272 | 130 | 60 | 65.3 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 137 | 172 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3695 | 0 | 60 | 263.7 | 361 | 1216 | 1412 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 76 | 0 | 45 | 81.4 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 381 | 0 | 14 | 48.0 | 58 | 177 | 289 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 328 | 474 | 30 | 21.2 | 204 | 685 | 902 | 0 | — |
| ITEM-0140 | A - Top Movers | Reorder | 1044 | 539 | 60 | 57.0 | 468 | 1586 | 1843 | 260 | — |
| ITEM-0141 | B - Core Products | Excess | 2122 | 0 | 45 | 212.2 | 158 | 618 | 828 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1360 | 320 | 60 | 109.9 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 303 | 470 | 45 | 28.4 | 168 | 660 | 884 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 705 | 0 | 7 | 57.4 | 37 | 136 | 394 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 99 | 389 | 489 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 129 | 636 | 90 | 39.0 | 102 | 404 | 473 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 16.4 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 637 | 0 | 60 | 167.1 | 81 | 314 | 394 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 207 | 0 | 60 | 143.3 | 24 | 113 | 156 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 495 | 0 | 14 | 66.2 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 667 | 274 | 30 | 38.1 | 231 | 775 | 1020 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 15.6 | 300 | 465 | 753 | 0 | — |
