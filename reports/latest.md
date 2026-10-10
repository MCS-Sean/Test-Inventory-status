# Synthetic Inventory Health

**Simulation date: 2026-10-10**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 82 |
| Lead-time risk | 7 |
| Reorder | 7 |
| Stockout | 13 |

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
| ITEM-0001 | B - Core Products | Healthy | 572 | 0 | 30 | 44.7 | 135 | 532 | 801 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 509 | 968 | 60 | 32.3 | 404 | 1366 | 1586 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1932 | 0 | 45 | 381.3 | 82 | 316 | 422 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 76 | 160 | 14 | 10.0 | 44 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 138 | 0 | 45 | 86.9 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Reorder | 141 | 0 | 14 | 20.9 | 41 | 143 | 284 | 145 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 32 | 198 | 60 | 21.8 | 25 | 115 | 159 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 109 | 410 | 90 | 49.0 | 69 | 272 | 318 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 355 | 0 | 90 | 121.9 | 69 | 334 | 422 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 850 | 0 | 7 | 67.3 | 33 | 135 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 86.7 | 78 | 203 | 285 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 469 | 0 | 45 | 70.3 | 104 | 411 | 551 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1143 | 0 | 30 | 299.0 | 44 | 163 | 243 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2934 | 0 | 60 | 288.0 | 211 | 833 | 1047 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 239 | 0 | 14 | 35.1 | 41 | 143 | 286 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 563 | 0 | 60 | 482.6 | 21 | 93 | 128 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 598 | 2027 | 2247 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 43 | 0 | 30 | 73.0 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 95.7 | 622 | 1142 | 1262 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 216 | 0 | 30 | 89.6 | 27 | 102 | 153 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 224 | 960 | 90 | 36.9 | 189 | 742 | 869 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 28.6 | 6 | 10 | 25 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1252 | 0 | 14 | 219.6 | 34 | 120 | 240 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 337 | 0 | 60 | 78.6 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 333 | 0 | 45 | 93.1 | 58 | 223 | 298 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 274 | 0 | 14 | 23.0 | 67 | 246 | 497 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 133 | 0 | 14 | 28.0 | 30 | 102 | 201 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 365 | 0 | 30 | 44.7 | 87 | 341 | 512 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 376 | 290 | 30 | 26.6 | 152 | 590 | 886 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4476 | 0 | 60 | 542.2 | 215 | 719 | 835 | 0 | — |
| ITEM-0041 | A - Top Movers | Reorder | 230 | 270 | 14 | 17.4 | 325 | 524 | 710 | 210 | — |
| ITEM-0042 | B - Core Products | Healthy | 122 | 0 | 14 | 21.8 | 34 | 118 | 236 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 498 | 1312 | 1500 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 717 | 0 | 45 | 210.9 | 42 | 199 | 301 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 315 | 115 | 90 | 101.2 | 131 | 415 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 56 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 62.2 | 159 | 288 | 467 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.8 | 12 | 49 | 73 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 133 | 338 | 438 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 189 | 0 | 7 | 18.3 | 26 | 109 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 139 | 0 | 7 | 19.8 | 20 | 77 | 224 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4462 | 0 | 60 | 455.8 | 258 | 856 | 993 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 449 | 0 | 14 | 53.2 | 63 | 190 | 308 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1094 | 1390 | 90 | 60.1 | 688 | 2346 | 2601 | 0 | 122 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 68 | 260 | 347 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 132 | 0 | 14 | 27.8 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 97 | 0 | 30 | 56.3 | 16 | 70 | 122 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 634 | 0 | 14 | 94.9 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 905 | 260 | 60 | 74.6 | 251 | 992 | 1246 | 0 | — |
| ITEM-0066 | B - Core Products | Reorder | 330 | 0 | 45 | 61.4 | 84 | 332 | 445 | 115 | — |
| ITEM-0067 | A - Top Movers | Reorder | 346 | 0 | 14 | 21.3 | 117 | 361 | 588 | 245 | — |
| ITEM-0068 | B - Core Products | Healthy | 418 | 0 | 30 | 80.2 | 60 | 222 | 331 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 42 | 0 | 7 | 15.2 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 27 | 0 | 7 | 33.8 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 221 | 871 | 1095 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3530 | 0 | 90 | 706.0 | 154 | 609 | 714 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 37 | 61 | 14 | 18.2 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 55 | 0 | 45 | 62.7 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | B - Core Products | Excess | 358 | 0 | 7 | 149.2 | 8 | 28 | 78 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 346 | 540 | 45 | 29.1 | 187 | 734 | 983 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 560 | 0 | 45 | 252.0 | 27 | 130 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 421 | 558 | 90 | 59.0 | 219 | 869 | 1018 | 0 | — |
| ITEM-0082 | B - Core Products | Reorder | 112 | 0 | 7 | 10.1 | 27 | 116 | 350 | 240 | — |
| ITEM-0083 | B - Core Products | Excess | 976 | 0 | 14 | 89.3 | 64 | 228 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 68 | 337 | 60 | 25.2 | 57 | 222 | 279 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 30 | 0 | 14 | 24.8 | 7 | 26 | 62 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 319 | 0 | 45 | 75.2 | 52 | 248 | 375 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 54 | 50 | 30 | 36.3 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 825 | 735 | 90 | 64.6 | 389 | 1552 | 1821 | 0 | 99 |
| ITEM-0093 | B - Core Products | Healthy | 141 | 435 | 7 | 6.6 | 283 | 455 | 905 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 103 | 0 | 7 | 19.6 | 16 | 58 | 169 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7095 | 0 | 90 | 393.4 | 686 | 2328 | 2580 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3847 | 0 | 60 | 282.4 | 350 | 1181 | 1372 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 32.8 | 100 | 153 | 290 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 155 | 0 | 7 | 23.5 | 22 | 75 | 214 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 176 | 0 | 14 | 44.9 | 25 | 84 | 167 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 626 | 1045 | 60 | 46.6 | 661 | 1481 | 1669 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 25 | 210 | 45 | 11.9 | 27 | 124 | 187 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 74.1 | 417 | 1265 | 1460 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 480 | 0 | 45 | 64.0 | 119 | 464 | 622 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1142 | 1041 | 90 | 68.6 | 634 | 2149 | 2382 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 338 | 740 | 60 | 29.9 | 232 | 922 | 1160 | 0 | 73 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 269 | 1070 | 1255 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1873 | 0 | 90 | 134.4 | 531 | 1799 | 1994 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 661 | 902 | 60 | 37.1 | 458 | 1545 | 1794 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 470 | 1395 | 45 | 33.2 | 719 | 1371 | 1569 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 9 | 45 | 14 | 6.3 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 85 | 128 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 168 | 664 | 778 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 280 | 0 | 30 | 49.1 | 61 | 238 | 358 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 64 | 59 | 30 | 33.3 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 262 | 0 | 7 | 19.5 | 35 | 143 | 425 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 97.2 | 157 | 292 | 354 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 182 | 0 | 14 | 95.2 | 49 | 78 | 135 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 231 | 0 | 14 | 23.3 | 58 | 207 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 42 | 126 | 7 | 7.0 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 181.1 | 308 | 500 | 586 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 555 | 744 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 84.9 | 713 | 1937 | 2219 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 629 | 0 | 14 | 105.8 | 33 | 123 | 247 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Reorder | 336 | 0 | 60 | 77.3 | 70 | 336 | 466 | 130 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 27 | 124 | 155 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3924 | 0 | 60 | 280.7 | 359 | 1212 | 1408 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 93.0 | 28 | 74 | 104 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 481 | 0 | 14 | 53.0 | 68 | 205 | 332 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 586 | 229 | 30 | 38.0 | 163 | 641 | 965 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1326 | 269 | 60 | 73.7 | 460 | 1558 | 1810 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2294 | 0 | 45 | 236.2 | 153 | 600 | 804 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 455 | 236 | 45 | 41.0 | 174 | 686 | 919 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 897 | 0 | 7 | 72.1 | 37 | 137 | 398 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 117 | 458 | 575 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 168 | 636 | 90 | 42.5 | 122 | 482 | 566 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Reorder | 581 | 0 | 14 | 32.0 | 439 | 711 | 965 | 385 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 687 | 0 | 60 | 152.7 | 95 | 370 | 464 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 28 | 200 | 60 | 17.6 | 27 | 124 | 172 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 623 | 0 | 14 | 86.8 | 42 | 150 | 301 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 669 | 266 | 30 | 37.3 | 237 | 793 | 1044 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
