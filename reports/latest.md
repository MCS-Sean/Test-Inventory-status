# Synthetic Inventory Health

**Simulation date: 2026-10-31**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 96 |
| Lead-time risk | 2 |
| Reorder | 2 |
| Stockout | 9 |

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
| ITEM-0001 | B - Core Products | Healthy | 294 | 291 | 30 | 22.3 | 139 | 547 | 824 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 286 | 0 | 7 | 43.9 | 92 | 145 | 281 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 459 | 890 | 60 | 29.6 | 397 | 1344 | 1561 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1860 | 0 | 45 | 459.9 | 65 | 252 | 336 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 106 | 155 | 14 | 15.0 | 41 | 148 | 296 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 108 | 0 | 45 | 72.0 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 169 | 0 | 14 | 29.5 | 33 | 119 | 240 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 199 | 0 | 60 | 157.1 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 70 | 410 | 90 | 37.7 | 58 | 227 | 266 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 297 | 90 | 90 | 104.4 | 68 | 327 | 413 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 567 | 0 | 7 | 43.6 | 34 | 138 | 411 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 331 | 155 | 45 | 49.2 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1094 | 0 | 30 | 375.8 | 33 | 124 | 185 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2717 | 0 | 60 | 258.8 | 217 | 858 | 1078 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 136 | 0 | 14 | 24.0 | 33 | 118 | 237 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 549 | 0 | 60 | 581.3 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 590 | 1999 | 2216 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 27 | 0 | 30 | 46.7 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 411 | 1169 | 60 | 39.3 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 179 | 0 | 30 | 87.1 | 18 | 82 | 144 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 123 | 960 | 90 | 24.9 | 151 | 601 | 705 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 38.1 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1164 | 0 | 14 | 245.3 | 28 | 100 | 199 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 244 | 135 | 60 | 56.5 | 69 | 333 | 463 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 272 | 0 | 45 | 88.1 | 50 | 193 | 257 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 677 | 0 | 60 | 662.3 | 49 | 112 | 143 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 320 | 0 | 14 | 27.3 | 67 | 243 | 490 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 32.8 | 116 | 176 | 333 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 55 | 95 | 14 | 13.8 | 24 | 84 | 168 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 197 | 172 | 30 | 23.6 | 89 | 348 | 523 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 350 | 315 | 30 | 23.6 | 157 | 617 | 928 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4329 | 0 | 60 | 606.9 | 183 | 619 | 718 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 50.4 | 251 | 433 | 686 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 162 | 0 | 14 | 35.4 | 27 | 96 | 192 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 648 | 0 | 45 | 193.1 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 287 | 220 | 90 | 91.6 | 130 | 416 | 510 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Stockout | 0 | 965 | 60 | 0.0 | 242 | 755 | 1007 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 71 | 0 | 45 | 99.8 | 11 | 44 | 66 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 212 | 0 | 7 | 20.7 | 23 | 105 | 320 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 133 | 0 | 7 | 17.9 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4309 | 0 | 60 | 564.5 | 197 | 663 | 770 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 309 | 0 | 14 | 43.5 | 52 | 159 | 259 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 720 | 1680 | 90 | 39.4 | 691 | 2356 | 2612 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 501 | 0 | 45 | 136.6 | 59 | 228 | 305 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 9 | 110 | 14 | 1.8 | 28 | 103 | 208 | 0 | 2 |
| ITEM-0062 | C - Slow Moving | Healthy | 68 | 0 | 30 | 47.1 | 13 | 58 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 514 | 0 | 14 | 79.9 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Reorder | 281 | 310 | 60 | 45.2 | 241 | 620 | 751 | 160 | — |
| ITEM-0065 | B - Core Products | Healthy | 663 | 525 | 60 | 55.4 | 248 | 979 | 1231 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 194 | 246 | 45 | 34.5 | 89 | 348 | 466 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 252 | 245 | 14 | 15.4 | 119 | 366 | 595 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 338 | 0 | 30 | 81.3 | 46 | 175 | 263 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 72 | 0 | 7 | 25.6 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 206 | 146 | 45 | 61.8 | 88 | 242 | 342 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 19 | 0 | 7 | 26.7 | 3 | 9 | 31 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 1053 | 0 | 60 | 94.5 | 231 | 911 | 1145 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3446 | 0 | 90 | 818.3 | 128 | 512 | 600 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 55 | 0 | 14 | 26.8 | 10 | 41 | 103 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 34 | 26 | 45 | 38.7 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 322 | 0 | 7 | 167.5 | 5 | 21 | 79 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 108 | 290 | 90 | 58.9 | 94 | 261 | 316 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 378 | 515 | 45 | 33.3 | 178 | 701 | 939 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 510 | 0 | 45 | 228.4 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Reorder | 287 | 558 | 90 | 41.3 | 214 | 846 | 992 | 147 | — |
| ITEM-0082 | B - Core Products | Healthy | 131 | 0 | 7 | 11.4 | 28 | 120 | 361 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 738 | 0 | 14 | 66.2 | 64 | 232 | 466 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 355 | 0 | 60 | 154.3 | 49 | 190 | 238 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 11 | 35 | 14 | 10.8 | 6 | 22 | 52 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 217 | 135 | 45 | 48.6 | 55 | 261 | 395 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 23 | 50 | 30 | 15.6 | 13 | 59 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 591 | 1027 | 90 | 47.8 | 376 | 1501 | 1760 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 113 | 485 | 7 | 6.2 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 108 | 0 | 7 | 22.8 | 13 | 51 | 151 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6690 | 0 | 90 | 367.8 | 689 | 2345 | 2599 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3548 | 0 | 60 | 255.7 | 356 | 1203 | 1397 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 56.0 | 96 | 139 | 251 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 64 | 0 | 7 | 12.3 | 15 | 57 | 166 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 111 | 0 | 14 | 34.4 | 19 | 68 | 135 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 743 | 865 | 60 | 52.7 | 677 | 1538 | 1736 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 196 | 0 | 45 | 106.3 | 23 | 108 | 164 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 618 | 689 | 90 | 76.8 | 374 | 1107 | 1275 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 318 | 180 | 45 | 42.8 | 118 | 460 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 813 | 1542 | 90 | 48.4 | 640 | 2170 | 2406 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 365 | 738 | 60 | 33.2 | 226 | 897 | 1128 | 0 | 56 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 267 | 1062 | 1246 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1509 | 445 | 90 | 106.0 | 545 | 1841 | 2040 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 282 | 1407 | 60 | 16.2 | 446 | 1508 | 1751 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 25 | 45 | 14 | 17.3 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 833 | 0 | 14 | 84.3 | 239 | 388 | 595 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 107 | 0 | 45 | 72.4 | 19 | 87 | 132 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 176 | 697 | 817 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 152 | 135 | 30 | 25.6 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 30 | 59 | 30 | 16.1 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 346 | 0 | 7 | 27.8 | 34 | 134 | 395 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 195 | 0 | 14 | 52.9 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 236 | 0 | 14 | 23.8 | 57 | 206 | 414 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 33 | 132 | 7 | 5.6 | 17 | 65 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 168.8 | 306 | 479 | 556 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 517 | 191 | 45 | 58.2 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 489 | 0 | 14 | 81.2 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 249 | 130 | 60 | 59.4 | 68 | 324 | 450 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 30 | 138 | 173 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3616 | 0 | 60 | 262.0 | 356 | 1198 | 1391 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 351 | 0 | 14 | 46.8 | 55 | 168 | 273 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 275 | 474 | 30 | 18.1 | 201 | 673 | 885 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 935 | 799 | 60 | 50.6 | 471 | 1599 | 1858 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2080 | 0 | 45 | 213.7 | 154 | 602 | 807 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 81.8 | 630 | 1509 | 1811 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 239 | 470 | 45 | 22.1 | 170 | 668 | 895 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 611 | 0 | 7 | 48.6 | 38 | 139 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 94 | 371 | 466 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 116 | 636 | 90 | 37.0 | 97 | 383 | 448 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 36.7 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 619 | 0 | 60 | 166.8 | 78 | 305 | 383 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 799 | 400 | 90 | 350.8 | 215 | 423 | 471 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 202 | 0 | 60 | 145.4 | 24 | 109 | 151 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 470 | 0 | 14 | 64.4 | 43 | 153 | 306 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 591 | 274 | 30 | 34.0 | 230 | 770 | 1013 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 562 | 0 | 7 | 26.7 | 308 | 477 | 772 | 0 | — |
