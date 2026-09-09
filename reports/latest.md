# Synthetic Inventory Health

**Simulation date: 2026-09-09**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 63 |
| Lead-time risk | 23 |
| Reorder | 2 |
| Stockout | 22 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 506 | 761 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 307 | 0 | 7 | 51.5 | 89 | 137 | 262 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 1004 | 294 | 60 | 66.3 | 386 | 1310 | 1521 | 223 | — |
| ITEM-0005 | B - Core Products | Excess | 2040 | 0 | 45 | 297.6 | 110 | 426 | 570 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 307 | 0 | 14 | 40.7 | 43 | 157 | 315 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 301 | 0 | 14 | 32.1 | 60 | 201 | 398 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 65 | 198 | 60 | 28.7 | 38 | 177 | 245 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 155 | 410 | 90 | 45.1 | 107 | 420 | 492 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 438 | 0 | 90 | 154.6 | 68 | 326 | 411 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1257 | 0 | 7 | 98.7 | 33 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 78 | 235 | 45 | 30.3 | 77 | 196 | 273 | 0 | — |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 106 | 419 | 562 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1227 | 0 | 30 | 226.3 | 62 | 231 | 344 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3239 | 0 | 60 | 312.8 | 214 | 846 | 1064 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 68 | 323 | 14 | 6.9 | 59 | 208 | 416 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 591 | 0 | 60 | 385.4 | 26 | 120 | 166 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 646 | 2196 | 2434 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 18.9 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1161 | 717 | 60 | 104.5 | 773 | 1451 | 1607 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 30 | 135 | 236 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 350 | 960 | 90 | 40.9 | 266 | 1045 | 1225 | 0 | 41 |
| ITEM-0030 | C - Slow Moving | Healthy | 24 | 0 | 7 | 47.0 | 7 | 12 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1364 | 0 | 14 | 156.4 | 52 | 183 | 366 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 309 | 429 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 417 | 0 | 45 | 73.0 | 95 | 358 | 478 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 722 | 0 | 60 | 320.1 | 75 | 213 | 281 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 421 | 0 | 14 | 38.8 | 62 | 225 | 453 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 225 | 0 | 14 | 31.5 | 42 | 149 | 299 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 333 | 501 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 51 | 575 | 30 | 3.8 | 147 | 569 | 855 | 0 | 4 |
| ITEM-0040 | A - Top Movers | Excess | 4658 | 0 | 60 | 363.9 | 335 | 1116 | 1295 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 38.5 | 283 | 521 | 855 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 266 | 0 | 14 | 32.4 | 53 | 177 | 349 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 521 | 1350 | 1541 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 818 | 0 | 45 | 239.0 | 42 | 200 | 303 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 352 | 175 | 60 | 74.2 | 175 | 465 | 607 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 28 | 80 | 45 | 24.5 | 16 | 69 | 103 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 297 | 0 | 7 | 29.5 | 27 | 108 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 215 | 0 | 7 | 29.6 | 20 | 79 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4673 | 0 | 60 | 349.0 | 353 | 1170 | 1358 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 634 | 0 | 14 | 51.7 | 97 | 281 | 453 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1670 | 580 | 90 | 96.0 | 660 | 2244 | 2487 | 0 | 96 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 101 | 382 | 510 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 29 | 103 | 206 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 134 | 0 | 30 | 51.3 | 23 | 104 | 183 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 827 | 0 | 14 | 122.8 | 38 | 139 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1298 | 0 | 60 | 108.1 | 248 | 981 | 1233 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 486 | 0 | 45 | 82.7 | 92 | 363 | 486 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 611 | 0 | 14 | 36.6 | 121 | 372 | 606 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 138 | 390 | 30 | 18.0 | 86 | 324 | 485 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 32 | 0 | 7 | 11.1 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 27 | 0 | 7 | 32.0 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 240 | 948 | 1192 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3633 | 0 | 90 | 496.9 | 227 | 893 | 1046 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 96 | 0 | 14 | 44.3 | 10 | 43 | 108 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 50 | 75 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 406 | 0 | 7 | 124.3 | 8 | 35 | 133 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 169 | 170 | 90 | 80.5 | 105 | 297 | 360 | 0 | 81 |
| ITEM-0079 | B - Core Products | Healthy | 660 | 275 | 45 | 51.3 | 201 | 793 | 1063 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 624 | 0 | 45 | 254.1 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 640 | 235 | 90 | 91.4 | 214 | 851 | 998 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 246 | 0 | 7 | 22.5 | 28 | 116 | 345 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1338 | 0 | 14 | 128.4 | 61 | 218 | 437 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 130 | 337 | 60 | 33.0 | 84 | 325 | 408 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 56 | 0 | 14 | 32.9 | 9 | 35 | 86 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 93 | 0 | 30 | 59.8 | 14 | 63 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1220 | 436 | 90 | 91.6 | 408 | 1621 | 1901 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.5 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 227 | 0 | 7 | 31.3 | 22 | 81 | 233 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7638 | 0 | 90 | 422.5 | 687 | 2333 | 2586 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4308 | 0 | 60 | 329.4 | 338 | 1136 | 1319 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 293 | 0 | 7 | 30.9 | 31 | 107 | 307 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 35 | 120 | 238 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 84.9 | 539 | 1320 | 1588 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 69 | 210 | 45 | 23.4 | 37 | 173 | 261 | 0 | 24 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 103.3 | 420 | 1264 | 1458 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 694 | 0 | 45 | 87.4 | 124 | 490 | 657 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1627 | 773 | 90 | 94.9 | 653 | 2214 | 2454 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 687 | 241 | 60 | 62.3 | 227 | 900 | 1131 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 593 | 0 | 30 | 216.1 | 61 | 147 | 229 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 257 | 915 | 90 | 28.1 | 279 | 1111 | 1302 | 0 | 29 |
| ITEM-0110 | C - Slow Moving | Excess | 711 | 0 | 60 | 258.0 | 103 | 272 | 354 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2268 | 0 | 90 | 148.0 | 580 | 1975 | 2189 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1232 | 360 | 60 | 70.4 | 450 | 1519 | 1764 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 52 | 0 | 14 | 36.0 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 59.3 | 298 | 552 | 908 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 123 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 163 | 530 | 90 | 29.9 | 167 | 664 | 779 | 0 | 30 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 255 | 383 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Reorder | 73 | 0 | 30 | 39.8 | 16 | 73 | 128 | 55 | — |
| ITEM-0121 | B - Core Products | Healthy | 339 | 0 | 7 | 25.2 | 36 | 144 | 427 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 233 | 0 | 14 | 80.0 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 12 | 292 | 14 | 1.2 | 59 | 215 | 434 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 103 | 0 | 7 | 16.8 | 17 | 66 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 550 | 737 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 812 | 0 | 14 | 131.0 | 34 | 127 | 258 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 465 | 0 | 60 | 108.7 | 69 | 330 | 459 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 108 | 136 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4342 | 0 | 60 | 318.7 | 349 | 1180 | 1371 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 0.9 | 27 | 77 | 109 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 706 | 0 | 14 | 56.1 | 97 | 286 | 462 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 91 | 560 | 30 | 6.0 | 199 | 667 | 878 | 227 | 7 |
| ITEM-0140 | A - Top Movers | Healthy | 1870 | 0 | 60 | 102.4 | 467 | 1581 | 1837 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2591 | 0 | 45 | 265.6 | 154 | 603 | 808 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 585 | 1380 | 1653 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 539 | 243 | 45 | 49.7 | 169 | 669 | 897 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1273 | 0 | 7 | 100.7 | 38 | 140 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 5 | 888 | 60 | 0.6 | 166 | 644 | 809 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 252 | 636 | 90 | 43.9 | 177 | 700 | 821 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 417 | 705 | 974 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 119.2 | 254 | 445 | 713 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 606 | 178 | 60 | 90.9 | 141 | 548 | 688 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 65 | 200 | 60 | 28.5 | 38 | 177 | 246 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 863 | 0 | 14 | 126.1 | 40 | 143 | 287 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 66 | 930 | 30 | 3.7 | 239 | 799 | 1051 | 0 | 4 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 383 | 418 | 7 | 16.9 | 304 | 485 | 802 | 0 | — |
