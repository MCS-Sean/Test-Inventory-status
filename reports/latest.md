# Synthetic Inventory Health

**Simulation date: 2026-10-13**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 87 |
| Lead-time risk | 7 |
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
| ITEM-0001 | B - Core Products | Healthy | 537 | 0 | 30 | 41.7 | 136 | 536 | 807 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 36.2 | 91 | 143 | 277 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 467 | 968 | 60 | 29.9 | 401 | 1356 | 1575 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1921 | 0 | 45 | 390.3 | 80 | 307 | 410 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 221 | 0 | 14 | 29.4 | 43 | 156 | 314 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 133 | 0 | 45 | 84.3 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 126 | 145 | 14 | 18.9 | 40 | 141 | 281 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 26 | 198 | 60 | 18.0 | 25 | 114 | 157 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 103 | 410 | 90 | 47.1 | 68 | 268 | 314 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 346 | 0 | 90 | 118.4 | 69 | 335 | 423 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 812 | 0 | 7 | 63.7 | 32 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 248.3 | 18 | 26 | 55 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 86.7 | 78 | 203 | 285 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 450 | 0 | 45 | 68.1 | 104 | 409 | 547 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1139 | 0 | 30 | 310.6 | 43 | 157 | 234 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2916 | 0 | 60 | 290.3 | 209 | 822 | 1033 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 227 | 0 | 14 | 33.9 | 40 | 141 | 281 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 562 | 0 | 60 | 505.8 | 20 | 88 | 122 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 594 | 2015 | 2234 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 41 | 0 | 30 | 69.6 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 732 | 915 | 60 | 77.4 | 643 | 1220 | 1353 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 209 | 0 | 30 | 89.1 | 26 | 99 | 148 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 213 | 960 | 90 | 36.2 | 183 | 718 | 842 | 0 | — |
| ITEM-0030 | C - Slow Moving | Reorder | 10 | 0 | 7 | 18.8 | 6 | 11 | 27 | 20 | — |
| ITEM-0031 | B - Core Products | Excess | 1248 | 0 | 14 | 226.0 | 34 | 117 | 233 | 0 | — |
| ITEM-0032 | C - Slow Moving | Reorder | 327 | 0 | 60 | 76.4 | 69 | 330 | 459 | 135 | — |
| ITEM-0033 | B - Core Products | Healthy | 320 | 0 | 45 | 89.7 | 58 | 223 | 297 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 250 | 0 | 14 | 20.9 | 67 | 246 | 497 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 124 | 0 | 14 | 26.8 | 29 | 99 | 196 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 348 | 0 | 30 | 42.8 | 87 | 339 | 510 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 345 | 290 | 30 | 24.5 | 151 | 588 | 883 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4456 | 0 | 60 | 552.4 | 209 | 702 | 814 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 230 | 480 | 14 | 17.4 | 325 | 524 | 710 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 108 | 116 | 14 | 20.0 | 32 | 113 | 227 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 453 | 1160 | 1323 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 704 | 0 | 45 | 208.4 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 315 | 115 | 90 | 101.2 | 131 | 415 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 42 | 760 | 60 | 6.3 | 281 | 690 | 831 | 0 | 7 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 9.1 | 11 | 47 | 70 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 133 | 338 | 438 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 160 | 0 | 7 | 15.5 | 26 | 109 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 111 | 0 | 7 | 15.6 | 20 | 77 | 227 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4453 | 0 | 60 | 486.4 | 242 | 801 | 929 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 420 | 0 | 14 | 50.2 | 63 | 189 | 306 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1049 | 1390 | 90 | 57.4 | 690 | 2353 | 2608 | 0 | 120 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 78.2 | 471 | 923 | 1230 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 67 | 255 | 340 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 118 | 0 | 14 | 24.6 | 27 | 99 | 200 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 93 | 0 | 30 | 55.8 | 15 | 67 | 117 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 610 | 0 | 14 | 90.6 | 38 | 139 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 869 | 260 | 60 | 71.4 | 252 | 995 | 1251 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 315 | 115 | 45 | 58.5 | 85 | 333 | 447 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 324 | 245 | 14 | 20.5 | 116 | 354 | 576 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 407 | 0 | 30 | 80.9 | 58 | 215 | 320 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 35 | 0 | 7 | 12.8 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 27 | 0 | 7 | 34.2 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 888 | 1117 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3517 | 0 | 90 | 716.1 | 151 | 598 | 702 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 33 | 61 | 14 | 16.4 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 52 | 26 | 45 | 60.0 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 352 | 0 | 7 | 150.9 | 6 | 25 | 95 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 313 | 540 | 45 | 25.9 | 190 | 746 | 1000 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 555 | 0 | 45 | 252.3 | 27 | 129 | 195 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 396 | 558 | 90 | 55.5 | 219 | 869 | 1018 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 79 | 240 | 7 | 7.2 | 26 | 114 | 345 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 945 | 0 | 14 | 85.6 | 64 | 230 | 462 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 61 | 337 | 60 | 23.5 | 55 | 214 | 269 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 26 | 0 | 14 | 21.9 | 7 | 25 | 61 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 307 | 0 | 45 | 72.0 | 52 | 249 | 377 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 48 | 50 | 30 | 32.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 786 | 1027 | 90 | 61.3 | 391 | 1558 | 1828 | 0 | 96 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 28.2 | 281 | 445 | 874 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 88 | 0 | 7 | 17.2 | 15 | 56 | 164 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7037 | 0 | 90 | 390.9 | 685 | 2323 | 2575 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3774 | 0 | 60 | 271.5 | 357 | 1205 | 1400 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 35.7 | 98 | 146 | 272 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 141 | 0 | 7 | 22.2 | 21 | 72 | 205 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 168 | 0 | 14 | 44.3 | 24 | 81 | 161 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 480 | 1285 | 60 | 32.4 | 699 | 1602 | 1809 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 231 | 0 | 45 | 113.0 | 26 | 121 | 182 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 80.6 | 388 | 1165 | 1344 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 451 | 180 | 45 | 60.1 | 119 | 464 | 622 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1091 | 1286 | 90 | 65.3 | 636 | 2157 | 2391 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 321 | 740 | 60 | 28.7 | 230 | 912 | 1146 | 0 | 72 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 270 | 1073 | 1259 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1857 | 0 | 90 | 138.4 | 513 | 1735 | 1923 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 616 | 1161 | 60 | 34.9 | 455 | 1532 | 1779 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 270 | 1395 | 45 | 16.5 | 765 | 1519 | 1749 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 7 | 45 | 14 | 5.1 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 163 | 645 | 756 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 264 | 0 | 30 | 46.3 | 61 | 238 | 358 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 56 | 59 | 30 | 28.5 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 226 | 0 | 7 | 16.9 | 35 | 143 | 424 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 100 | 92 | 14 | 35.4 | 65 | 108 | 192 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 209 | 0 | 14 | 21.0 | 58 | 208 | 417 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 21 | 126 | 7 | 3.5 | 15 | 63 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 181.1 | 308 | 500 | 586 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 690 | 0 | 45 | 76.0 | 142 | 560 | 751 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 72.3 | 734 | 1991 | 2281 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 604 | 0 | 14 | 100.1 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 326 | 130 | 60 | 76.2 | 69 | 330 | 459 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 129 | 162 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3889 | 0 | 60 | 283.9 | 352 | 1188 | 1380 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 458 | 0 | 14 | 51.3 | 66 | 200 | 326 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 553 | 229 | 30 | 36.2 | 162 | 635 | 956 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1288 | 269 | 60 | 71.7 | 459 | 1555 | 1806 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2262 | 0 | 45 | 232.9 | 153 | 600 | 804 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 435 | 236 | 45 | 40.2 | 170 | 668 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 858 | 0 | 7 | 68.9 | 37 | 137 | 399 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 113 | 442 | 555 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 160 | 636 | 90 | 42.5 | 116 | 459 | 538 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Healthy | 581 | 385 | 14 | 32.0 | 439 | 711 | 965 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 680 | 0 | 60 | 156.9 | 92 | 357 | 448 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 24 | 200 | 60 | 15.5 | 26 | 121 | 167 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 595 | 0 | 14 | 81.8 | 43 | 153 | 305 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 602 | 266 | 30 | 32.8 | 241 | 811 | 1067 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 23.0 | 301 | 486 | 810 | 0 | — |
