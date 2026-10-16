# Synthetic Inventory Health

**Simulation date: 2026-10-16**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 89 |
| Lead-time risk | 6 |
| Reorder | 2 |
| Stockout | 11 |

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
| ITEM-0001 | B - Core Products | Healthy | 484 | 291 | 30 | 37.3 | 137 | 540 | 812 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 220 | 0 | 7 | 33.6 | 91 | 144 | 281 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 431 | 968 | 60 | 27.9 | 397 | 1339 | 1555 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1909 | 0 | 45 | 399.6 | 77 | 297 | 398 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 207 | 0 | 14 | 28.3 | 43 | 153 | 307 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 127 | 0 | 45 | 79.9 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 106 | 145 | 14 | 16.1 | 40 | 139 | 277 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 221 | 0 | 60 | 157.9 | 24 | 110 | 152 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 96 | 410 | 90 | 44.8 | 67 | 263 | 308 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 144.9 | 264 | 355 | 512 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 335 | 90 | 90 | 112.9 | 70 | 340 | 429 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 778 | 0 | 7 | 61.4 | 32 | 134 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 199 | 0 | 7 | 139.9 | 21 | 33 | 76 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 426 | 0 | 45 | 63.5 | 105 | 414 | 555 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1131 | 0 | 30 | 324.2 | 41 | 150 | 223 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2865 | 0 | 60 | 275.8 | 216 | 850 | 1068 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 212 | 0 | 14 | 32.8 | 39 | 136 | 272 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 561 | 0 | 60 | 531.5 | 19 | 84 | 116 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 604 | 2047 | 2269 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 39 | 0 | 30 | 68.8 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Reorder | 500 | 915 | 60 | 41.6 | 766 | 1501 | 1669 | 254 | — |
| ITEM-0028 | B - Core Products | Healthy | 202 | 0 | 30 | 87.0 | 26 | 98 | 147 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 200 | 960 | 90 | 36.0 | 172 | 678 | 795 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1237 | 0 | 14 | 230.5 | 33 | 114 | 227 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 314 | 135 | 60 | 72.1 | 70 | 336 | 467 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 312 | 0 | 45 | 89.7 | 56 | 216 | 290 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 215 | 265 | 14 | 18.2 | 67 | 245 | 493 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 111 | 0 | 14 | 24.6 | 28 | 96 | 191 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 319 | 172 | 30 | 39.2 | 87 | 340 | 510 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 280 | 605 | 30 | 19.3 | 156 | 607 | 912 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4434 | 0 | 60 | 575.0 | 198 | 669 | 777 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 500 | 210 | 14 | 42.7 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 101 | 116 | 14 | 19.5 | 31 | 109 | 217 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 466 | 1222 | 1396 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 697 | 0 | 45 | 207.0 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 257 | 330 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 42 | 760 | 60 | 6.6 | 276 | 664 | 797 | 0 | 7 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 85 | 0 | 45 | 114.2 | 11 | 46 | 68 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 224 | 154 | 60 | 67.0 | 133 | 338 | 438 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 139 | 0 | 7 | 13.6 | 25 | 107 | 322 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 89 | 0 | 7 | 12.4 | 20 | 78 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4426 | 0 | 60 | 485.8 | 239 | 795 | 923 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 398 | 0 | 14 | 49.1 | 60 | 182 | 295 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 975 | 1680 | 90 | 52.5 | 701 | 2390 | 2650 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 78.2 | 471 | 923 | 1230 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 560 | 0 | 45 | 141.6 | 65 | 247 | 331 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 105 | 0 | 14 | 22.1 | 27 | 99 | 198 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 90 | 0 | 30 | 57.4 | 15 | 64 | 111 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 589 | 0 | 14 | 87.3 | 38 | 140 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 838 | 260 | 60 | 70.4 | 246 | 973 | 1223 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 298 | 115 | 45 | 55.4 | 84 | 332 | 445 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 497 | 0 | 14 | 31.0 | 117 | 358 | 583 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 399 | 0 | 30 | 81.1 | 57 | 210 | 313 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 27 | 85 | 7 | 9.8 | 6 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 26 | 0 | 7 | 34.4 | 3 | 10 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 228 | 900 | 1131 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3505 | 0 | 90 | 751.1 | 143 | 568 | 666 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 27 | 61 | 14 | 13.3 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 48 | 26 | 45 | 54.0 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 727 | 90 | 0.0 | 288 | 644 | 727 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 349 | 0 | 7 | 157.0 | 6 | 24 | 91 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 293 | 540 | 45 | 24.8 | 186 | 731 | 979 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 548 | 0 | 45 | 247.8 | 27 | 129 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 385 | 558 | 90 | 55.2 | 215 | 850 | 997 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 53 | 240 | 7 | 4.8 | 26 | 115 | 347 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 914 | 0 | 14 | 82.3 | 65 | 232 | 465 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 54 | 337 | 60 | 21.5 | 53 | 207 | 259 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 346 | 0 | 14 | 46.0 | 203 | 316 | 474 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 25 | 0 | 14 | 22.1 | 7 | 24 | 58 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 294 | 0 | 45 | 68.7 | 52 | 249 | 378 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 43 | 50 | 30 | 28.5 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 757 | 1027 | 90 | 60.1 | 384 | 1530 | 1794 | 0 | 95 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 32.7 | 255 | 396 | 766 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 74 | 0 | 7 | 14.9 | 15 | 55 | 160 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6988 | 0 | 90 | 393.3 | 676 | 2293 | 2542 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3736 | 0 | 60 | 267.5 | 359 | 1211 | 1407 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 156 | 0 | 7 | 25.7 | 98 | 147 | 274 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 132 | 0 | 7 | 21.8 | 20 | 69 | 196 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 160 | 0 | 14 | 44.0 | 23 | 78 | 154 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 55.8 | 707 | 1641 | 1856 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 225 | 0 | 45 | 111.9 | 26 | 119 | 179 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 80.6 | 388 | 1165 | 1344 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 430 | 180 | 45 | 57.5 | 119 | 463 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1043 | 1286 | 90 | 62.2 | 638 | 2164 | 2399 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 287 | 740 | 60 | 26.2 | 225 | 894 | 1125 | 0 | 71 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1068 | 1253 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1800 | 0 | 90 | 134.0 | 514 | 1737 | 1925 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 559 | 1161 | 60 | 32.3 | 446 | 1502 | 1745 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 270 | 1395 | 45 | 16.6 | 765 | 1516 | 1744 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 46 | 0 | 14 | 33.4 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 96.6 | 241 | 397 | 615 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 167 | 661 | 775 | 0 | 1 |
| ITEM-0119 | B - Core Products | Lead-time risk | 234 | 0 | 30 | 39.9 | 63 | 245 | 369 | 135 | 40 |
| ITEM-0120 | C - Slow Moving | Healthy | 53 | 59 | 30 | 27.6 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 200 | 0 | 7 | 15.0 | 35 | 142 | 422 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 100 | 92 | 14 | 35.4 | 65 | 108 | 192 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 185 | 216 | 14 | 18.6 | 58 | 207 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 122 | 0 | 7 | 20.4 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 214.3 | 290 | 452 | 525 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 666 | 0 | 45 | 74.3 | 140 | 553 | 741 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 584 | 0 | 14 | 96.3 | 34 | 125 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 314 | 130 | 60 | 74.2 | 68 | 327 | 454 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 29 | 133 | 167 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3844 | 0 | 60 | 279.0 | 354 | 1195 | 1388 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 442 | 0 | 14 | 50.8 | 65 | 196 | 318 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 497 | 229 | 30 | 32.3 | 164 | 642 | 965 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1246 | 539 | 60 | 69.4 | 459 | 1555 | 1806 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2237 | 0 | 45 | 231.4 | 153 | 598 | 801 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 605 | 1433 | 1718 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 407 | 470 | 45 | 37.6 | 170 | 669 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 823 | 0 | 7 | 66.0 | 37 | 137 | 399 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 110 | 430 | 540 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 154 | 636 | 90 | 42.0 | 113 | 447 | 524 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Healthy | 416 | 385 | 14 | 20.8 | 458 | 758 | 1038 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 673 | 0 | 60 | 157.3 | 91 | 352 | 442 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 21 | 200 | 60 | 14.0 | 25 | 117 | 162 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 570 | 0 | 14 | 77.7 | 43 | 153 | 307 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Reorder | 537 | 266 | 30 | 29.0 | 243 | 818 | 1077 | 274 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 24.9 | 288 | 459 | 758 | 0 | — |
