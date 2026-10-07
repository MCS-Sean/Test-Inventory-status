# Synthetic Inventory Health

**Simulation date: 2026-10-07**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 86 |
| Lead-time risk | 11 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Healthy | 623 | 0 | 30 | 49.7 | 133 | 522 | 786 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 559 | 968 | 60 | 35.8 | 400 | 1353 | 1571 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1945 | 0 | 45 | 376.5 | 84 | 322 | 431 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 98 | 160 | 14 | 12.9 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 140 | 0 | 45 | 85.7 | 21 | 97 | 146 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 152 | 0 | 14 | 22.0 | 42 | 146 | 292 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 35 | 198 | 60 | 23.0 | 26 | 119 | 165 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 112 | 410 | 90 | 48.2 | 72 | 284 | 333 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 10.8 | 670 | 1295 | 1439 | 0 | 11 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 365 | 0 | 90 | 126.8 | 68 | 330 | 417 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 889 | 0 | 7 | 69.5 | 33 | 136 | 405 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Healthy | 487 | 0 | 45 | 72.7 | 105 | 414 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1154 | 0 | 30 | 302.8 | 44 | 163 | 243 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2959 | 0 | 60 | 286.7 | 213 | 843 | 1060 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 248 | 0 | 14 | 33.6 | 46 | 157 | 312 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 566 | 0 | 60 | 471.7 | 21 | 95 | 131 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 610 | 2069 | 2293 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 44 | 0 | 30 | 76.2 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 221 | 0 | 30 | 89.6 | 28 | 105 | 157 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 240 | 960 | 90 | 39.4 | 190 | 745 | 872 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1260 | 0 | 14 | 212.4 | 36 | 125 | 250 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 350 | 0 | 60 | 82.5 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 341 | 0 | 45 | 90.0 | 62 | 237 | 316 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 306 | 0 | 14 | 25.5 | 68 | 249 | 501 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 139 | 0 | 14 | 28.3 | 30 | 104 | 207 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 382 | 0 | 30 | 47.4 | 87 | 338 | 507 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 419 | 290 | 30 | 29.3 | 153 | 597 | 898 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4496 | 0 | 60 | 528.9 | 222 | 741 | 860 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 28.5 | 313 | 494 | 662 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 137 | 0 | 14 | 22.7 | 38 | 129 | 256 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 726 | 0 | 45 | 212.8 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 353 | 115 | 90 | 131.3 | 118 | 363 | 444 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 25 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 58.4 | 161 | 298 | 489 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.2 | 12 | 52 | 78 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 113 | 275 | 354 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 229 | 0 | 7 | 22.4 | 25 | 107 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 163 | 0 | 7 | 23.3 | 20 | 76 | 223 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4484 | 0 | 60 | 443.0 | 267 | 885 | 1027 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 459 | 0 | 14 | 51.1 | 70 | 205 | 331 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1137 | 1390 | 90 | 62.0 | 693 | 2363 | 2620 | 0 | 124 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 72 | 272 | 363 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 32 | 110 | 14 | 6.7 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 102 | 0 | 30 | 56.3 | 17 | 74 | 128 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 646 | 0 | 14 | 96.7 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 931 | 260 | 60 | 75.1 | 256 | 1013 | 1273 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 342 | 0 | 45 | 62.4 | 86 | 338 | 454 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 413 | 0 | 14 | 25.7 | 117 | 359 | 584 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 431 | 0 | 30 | 81.3 | 61 | 226 | 337 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 52 | 0 | 7 | 19.0 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 30 | 0 | 7 | 38.6 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 222 | 875 | 1099 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3539 | 0 | 90 | 701.6 | 156 | 616 | 721 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 44 | 0 | 14 | 21.6 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 58 | 0 | 45 | 66.9 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 360 | 0 | 7 | 144.0 | 6 | 26 | 101 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 387 | 540 | 45 | 32.9 | 185 | 727 | 974 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 563 | 0 | 45 | 244.8 | 28 | 134 | 203 | 0 | — |
| ITEM-0081 | B - Core Products | Lead-time risk | 446 | 393 | 90 | 63.4 | 216 | 857 | 1004 | 165 | 120 |
| ITEM-0082 | B - Core Products | Healthy | 139 | 0 | 7 | 12.4 | 27 | 117 | 353 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1006 | 0 | 14 | 92.1 | 64 | 228 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 74 | 337 | 60 | 26.5 | 59 | 230 | 288 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 34 | 0 | 14 | 28.1 | 7 | 26 | 62 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 335 | 0 | 45 | 79.3 | 52 | 247 | 373 | 0 | — |
| ITEM-0089 | B - Core Products | Stockout | 0 | 702 | 14 | 0.0 | 354 | 616 | 983 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 59 | 50 | 30 | 39.6 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 861 | 735 | 90 | 66.2 | 397 | 1580 | 1853 | 0 | 100 |
| ITEM-0093 | B - Core Products | Healthy | 141 | 435 | 7 | 6.5 | 283 | 456 | 910 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 116 | 0 | 7 | 21.6 | 16 | 60 | 172 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7120 | 0 | 90 | 389.8 | 693 | 2356 | 2611 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3894 | 0 | 60 | 284.7 | 351 | 1186 | 1377 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 165 | 0 | 7 | 24.3 | 22 | 77 | 219 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 183 | 0 | 14 | 44.8 | 26 | 88 | 174 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 706 | 765 | 60 | 56.3 | 641 | 1407 | 1582 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 30 | 210 | 45 | 13.9 | 27 | 127 | 191 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 74.1 | 417 | 1265 | 1460 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 502 | 0 | 45 | 66.2 | 120 | 469 | 628 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1182 | 1041 | 90 | 69.7 | 644 | 2187 | 2425 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 381 | 740 | 60 | 34.0 | 230 | 914 | 1150 | 0 | 77 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 7 | 1100 | 90 | 0.8 | 273 | 1088 | 1277 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1917 | 0 | 90 | 136.8 | 533 | 1809 | 2005 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 726 | 902 | 60 | 41.4 | 451 | 1522 | 1767 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 38.1 | 715 | 1342 | 1533 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 13 | 45 | 14 | 9.1 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 87 | 131 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 7 | 648 | 90 | 1.3 | 165 | 652 | 764 | 0 | 2 |
| ITEM-0119 | B - Core Products | Healthy | 297 | 0 | 30 | 51.3 | 62 | 242 | 364 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 70 | 59 | 30 | 36.2 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 294 | 0 | 7 | 21.9 | 35 | 143 | 425 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 86.4 | 163 | 315 | 385 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 182 | 0 | 14 | 95.2 | 63 | 92 | 132 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 271 | 0 | 14 | 27.4 | 58 | 207 | 414 | 0 | — |
| ITEM-0125 | B - Core Products | Reorder | 63 | 0 | 7 | 10.6 | 16 | 64 | 189 | 126 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 132.7 | 394 | 656 | 774 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 554 | 743 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 84.9 | 713 | 1937 | 2219 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 647 | 0 | 14 | 109.0 | 33 | 122 | 247 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 344 | 0 | 60 | 78.4 | 71 | 339 | 471 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 26 | 122 | 153 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3978 | 0 | 60 | 292.0 | 350 | 1181 | 1372 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 102 | 0 | 45 | 108.0 | 27 | 71 | 99 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 504 | 0 | 14 | 54.1 | 70 | 210 | 341 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 397 | 456 | 30 | 25.7 | 203 | 683 | 899 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1400 | 269 | 60 | 78.5 | 456 | 1545 | 1795 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2332 | 0 | 45 | 242.4 | 151 | 594 | 796 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 180 | 1680 | 60 | 14.3 | 552 | 1320 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 490 | 236 | 45 | 44.8 | 172 | 675 | 905 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 927 | 0 | 7 | 73.8 | 38 | 139 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 121 | 472 | 593 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 177 | 636 | 90 | 43.1 | 127 | 502 | 588 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 51.2 | 323 | 559 | 888 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 694 | 0 | 60 | 148.4 | 99 | 385 | 483 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 367.1 | 229 | 460 | 513 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 32 | 200 | 60 | 20.0 | 27 | 125 | 173 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 648 | 0 | 14 | 92.4 | 42 | 148 | 295 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 716 | 266 | 30 | 39.6 | 239 | 801 | 1054 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
