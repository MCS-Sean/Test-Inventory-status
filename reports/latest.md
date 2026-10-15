# Synthetic Inventory Health

**Simulation date: 2026-10-15**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 87 |
| Lead-time risk | 6 |
| Reorder | 4 |
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
| ITEM-0001 | B - Core Products | Healthy | 499 | 291 | 30 | 38.3 | 138 | 542 | 816 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 36.2 | 91 | 143 | 277 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 441 | 968 | 60 | 28.5 | 398 | 1344 | 1561 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1915 | 0 | 45 | 395.3 | 79 | 302 | 404 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 218 | 0 | 14 | 29.8 | 43 | 153 | 307 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 129 | 0 | 45 | 81.2 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 114 | 145 | 14 | 17.3 | 40 | 139 | 278 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 23 | 198 | 60 | 15.9 | 25 | 114 | 157 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 98 | 410 | 90 | 44.8 | 68 | 268 | 314 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 134.4 | 267 | 365 | 535 | 0 | — |
| ITEM-0013 | C - Slow Moving | Reorder | 339 | 0 | 90 | 114.7 | 70 | 339 | 428 | 90 | — |
| ITEM-0014 | B - Core Products | Excess | 788 | 0 | 7 | 61.8 | 33 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 211 | 0 | 7 | 163.7 | 21 | 32 | 70 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 97.9 | 74 | 185 | 257 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 433 | 0 | 45 | 64.5 | 105 | 414 | 555 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1134 | 0 | 30 | 319.9 | 41 | 151 | 226 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2882 | 0 | 60 | 281.9 | 212 | 836 | 1051 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 219 | 0 | 14 | 33.6 | 39 | 137 | 274 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 561 | 0 | 60 | 525.9 | 19 | 85 | 117 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 598 | 2029 | 2249 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 40 | 0 | 30 | 69.2 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 732 | 915 | 60 | 77.4 | 518 | 1095 | 1294 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 205 | 0 | 30 | 89.1 | 26 | 98 | 146 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 204 | 960 | 90 | 36.6 | 172 | 680 | 797 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1240 | 0 | 14 | 228.7 | 33 | 115 | 229 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 321 | 135 | 60 | 74.8 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 315 | 0 | 45 | 89.4 | 57 | 220 | 293 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 225 | 265 | 14 | 19.0 | 67 | 245 | 494 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 115 | 0 | 14 | 25.6 | 28 | 96 | 190 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 324 | 172 | 30 | 39.4 | 88 | 344 | 517 | 0 | — |
| ITEM-0039 | B - Core Products | Reorder | 301 | 290 | 30 | 20.9 | 155 | 603 | 905 | 315 | — |
| ITEM-0040 | A - Top Movers | Excess | 4438 | 0 | 60 | 568.2 | 201 | 678 | 787 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 230 | 480 | 14 | 19.6 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 102 | 116 | 14 | 19.6 | 31 | 109 | 219 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 453 | 1160 | 1323 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 700 | 0 | 45 | 207.2 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Reorder | 305 | 115 | 90 | 94.7 | 133 | 427 | 523 | 105 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 42 | 760 | 60 | 6.3 | 281 | 690 | 831 | 0 | 7 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 86 | 0 | 45 | 115.5 | 11 | 46 | 68 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 224 | 154 | 60 | 67.0 | 133 | 338 | 438 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 147 | 0 | 7 | 14.5 | 25 | 107 | 320 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 102 | 0 | 7 | 14.3 | 20 | 77 | 227 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4437 | 0 | 60 | 493.6 | 237 | 786 | 912 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 405 | 0 | 14 | 49.6 | 61 | 184 | 298 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 988 | 1390 | 90 | 53.0 | 705 | 2403 | 2664 | 290 | 114 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 78.2 | 471 | 923 | 1230 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 65 | 247 | 331 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 110 | 0 | 14 | 23.0 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 92 | 0 | 30 | 57.9 | 15 | 65 | 112 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 597 | 0 | 14 | 88.8 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 847 | 260 | 60 | 70.6 | 248 | 980 | 1232 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 302 | 115 | 45 | 56.2 | 84 | 332 | 445 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 270 | 245 | 14 | 16.9 | 117 | 357 | 581 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 399 | 0 | 30 | 80.3 | 57 | 211 | 316 | 0 | — |
| ITEM-0069 | C - Slow Moving | Reorder | 29 | 0 | 7 | 10.5 | 6 | 29 | 111 | 85 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 26 | 0 | 7 | 33.4 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 229 | 906 | 1139 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3509 | 0 | 90 | 739.6 | 146 | 578 | 678 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 30 | 61 | 14 | 14.9 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 50 | 26 | 45 | 57.0 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 547 | 90 | 0.0 | 288 | 644 | 727 | 180 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 349 | 0 | 7 | 153.2 | 6 | 25 | 93 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 304 | 540 | 45 | 25.7 | 186 | 731 | 980 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 549 | 0 | 45 | 245.8 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 387 | 558 | 90 | 54.9 | 217 | 860 | 1008 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 68 | 240 | 7 | 6.2 | 26 | 114 | 345 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 923 | 0 | 14 | 83.4 | 64 | 230 | 463 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 56 | 337 | 60 | 22.1 | 54 | 209 | 262 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 346 | 0 | 14 | 46.0 | 203 | 316 | 474 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 26 | 0 | 14 | 22.9 | 7 | 24 | 58 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 298 | 0 | 45 | 69.5 | 53 | 251 | 379 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 45 | 50 | 30 | 29.8 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 770 | 1027 | 90 | 60.6 | 388 | 1545 | 1812 | 0 | 95 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 28.2 | 281 | 445 | 874 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 78 | 0 | 7 | 15.5 | 15 | 56 | 161 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6997 | 0 | 90 | 390.4 | 681 | 2312 | 2563 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3747 | 0 | 60 | 268.3 | 359 | 1211 | 1407 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 39.5 | 95 | 139 | 253 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 135 | 0 | 7 | 22.1 | 20 | 69 | 197 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 164 | 0 | 14 | 44.6 | 23 | 79 | 156 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 55.8 | 707 | 1641 | 1856 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 227 | 0 | 45 | 112.9 | 26 | 119 | 179 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 80.6 | 388 | 1165 | 1344 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 437 | 180 | 45 | 58.5 | 119 | 463 | 620 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1057 | 1286 | 90 | 62.8 | 640 | 2171 | 2407 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 302 | 740 | 60 | 27.5 | 226 | 897 | 1128 | 0 | 72 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 271 | 1078 | 1265 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1809 | 0 | 90 | 134.4 | 514 | 1739 | 1927 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 576 | 1161 | 60 | 33.0 | 450 | 1514 | 1758 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 270 | 1395 | 45 | 16.5 | 765 | 1519 | 1749 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 49 | 0 | 14 | 35.9 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 165 | 653 | 765 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 245 | 0 | 30 | 42.0 | 63 | 244 | 367 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 55 | 59 | 30 | 28.4 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 205 | 0 | 7 | 15.4 | 35 | 142 | 421 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 100 | 92 | 14 | 35.4 | 65 | 108 | 192 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 185 | 216 | 14 | 18.4 | 58 | 209 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 5 | 126 | 7 | 0.8 | 16 | 64 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 214.3 | 290 | 452 | 525 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 673 | 0 | 45 | 74.5 | 141 | 557 | 747 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 593 | 0 | 14 | 98.5 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 315 | 130 | 60 | 74.0 | 69 | 329 | 457 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3857 | 0 | 60 | 280.6 | 353 | 1192 | 1384 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 446 | 0 | 14 | 50.6 | 65 | 198 | 321 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 509 | 229 | 30 | 33.0 | 204 | 682 | 898 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1254 | 539 | 60 | 69.5 | 461 | 1563 | 1816 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2258 | 0 | 45 | 238.2 | 150 | 586 | 786 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 605 | 1433 | 1718 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 417 | 470 | 45 | 38.5 | 170 | 668 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 841 | 0 | 7 | 68.5 | 37 | 136 | 394 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 110 | 432 | 542 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 156 | 636 | 90 | 42.3 | 114 | 450 | 528 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Healthy | 416 | 385 | 14 | 20.8 | 458 | 758 | 1038 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 676 | 0 | 60 | 157.6 | 91 | 353 | 443 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 22 | 200 | 60 | 14.5 | 26 | 119 | 165 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 576 | 0 | 14 | 78.9 | 43 | 153 | 306 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 556 | 266 | 30 | 30.0 | 242 | 816 | 1075 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 24.9 | 288 | 459 | 758 | 0 | — |
