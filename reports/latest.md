# Synthetic Inventory Health

**Simulation date: 2026-10-06**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 85 |
| Lead-time risk | 11 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Healthy | 639 | 0 | 30 | 50.7 | 134 | 525 | 790 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 582 | 968 | 60 | 37.2 | 401 | 1356 | 1575 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1949 | 0 | 45 | 374.0 | 84 | 324 | 434 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 114 | 160 | 14 | 15.2 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 95 | 143 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 155 | 0 | 14 | 21.9 | 43 | 150 | 298 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 35 | 198 | 60 | 22.2 | 27 | 124 | 171 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 112 | 410 | 90 | 47.1 | 74 | 291 | 341 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 10.8 | 670 | 1295 | 1439 | 0 | 11 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 367 | 0 | 90 | 127.0 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 901 | 0 | 7 | 69.9 | 33 | 137 | 407 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 74 | 186 | 259 | 0 | 1 |
| ITEM-0017 | B - Core Products | Healthy | 494 | 0 | 45 | 73.9 | 105 | 413 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1156 | 0 | 30 | 300.7 | 45 | 165 | 245 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2971 | 0 | 60 | 289.1 | 213 | 840 | 1056 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 253 | 0 | 14 | 33.9 | 46 | 158 | 315 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 566 | 0 | 60 | 467.3 | 21 | 95 | 132 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 610 | 2068 | 2292 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 45 | 0 | 30 | 77.9 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 221 | 0 | 30 | 87.2 | 28 | 107 | 160 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 244 | 960 | 90 | 39.4 | 193 | 757 | 887 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1264 | 0 | 14 | 209.5 | 36 | 127 | 254 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 355 | 0 | 60 | 83.6 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 343 | 0 | 45 | 88.2 | 64 | 243 | 325 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 84 | 245 | 14 | 7.0 | 67 | 247 | 497 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 140 | 0 | 14 | 28.1 | 30 | 105 | 210 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 384 | 0 | 30 | 47.2 | 87 | 340 | 510 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 435 | 290 | 30 | 30.0 | 156 | 605 | 909 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4501 | 0 | 60 | 524.7 | 224 | 748 | 868 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 25.2 | 333 | 537 | 727 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 144 | 0 | 14 | 23.7 | 39 | 131 | 258 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 729 | 0 | 45 | 213.7 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 353 | 115 | 90 | 121.7 | 122 | 386 | 473 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 25 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 55.0 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 8 | 80 | 45 | 9.4 | 12 | 52 | 78 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 113 | 275 | 354 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 240 | 0 | 7 | 23.7 | 26 | 107 | 320 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 170 | 0 | 7 | 24.4 | 20 | 76 | 222 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4493 | 0 | 60 | 445.3 | 266 | 882 | 1023 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 468 | 0 | 14 | 51.4 | 71 | 208 | 336 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1155 | 1390 | 90 | 62.7 | 696 | 2373 | 2631 | 0 | 124 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 73 | 275 | 367 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 36 | 110 | 14 | 7.4 | 28 | 101 | 202 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 105 | 0 | 30 | 58.3 | 17 | 73 | 127 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 654 | 0 | 14 | 97.9 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 941 | 260 | 60 | 75.6 | 257 | 1017 | 1278 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 351 | 0 | 45 | 64.5 | 85 | 336 | 450 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 429 | 0 | 14 | 26.7 | 117 | 359 | 584 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 433 | 0 | 30 | 79.4 | 63 | 233 | 347 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 54 | 0 | 7 | 19.5 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 31 | 0 | 7 | 40.4 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 222 | 875 | 1100 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3541 | 0 | 90 | 682.4 | 161 | 634 | 743 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 44 | 0 | 14 | 21.4 | 10 | 41 | 103 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 58 | 0 | 45 | 66.1 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 362 | 0 | 7 | 142.3 | 7 | 28 | 104 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 395 | 540 | 45 | 33.4 | 186 | 730 | 978 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 565 | 0 | 45 | 245.7 | 28 | 134 | 203 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 461 | 393 | 90 | 66.3 | 213 | 846 | 993 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 151 | 0 | 7 | 13.5 | 27 | 117 | 352 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1021 | 0 | 14 | 93.7 | 64 | 228 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 76 | 337 | 60 | 26.8 | 60 | 233 | 293 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 35 | 0 | 14 | 28.9 | 7 | 26 | 62 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 344 | 0 | 45 | 82.6 | 51 | 243 | 368 | 0 | — |
| ITEM-0089 | B - Core Products | Stockout | 0 | 702 | 14 | 0.0 | 354 | 616 | 983 | 0 | 1 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Reorder | 60 | 0 | 30 | 39.7 | 14 | 61 | 107 | 50 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 868 | 735 | 90 | 66.2 | 400 | 1594 | 1869 | 0 | 100 |
| ITEM-0093 | B - Core Products | Healthy | 141 | 435 | 7 | 6.5 | 283 | 456 | 910 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 120 | 0 | 7 | 22.2 | 16 | 60 | 173 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7142 | 0 | 90 | 391.5 | 692 | 2353 | 2608 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3899 | 0 | 60 | 284.6 | 352 | 1188 | 1380 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 169 | 0 | 7 | 24.6 | 22 | 78 | 222 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 185 | 0 | 14 | 45.1 | 26 | 88 | 174 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 706 | 765 | 60 | 56.3 | 641 | 1407 | 1582 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 33 | 210 | 45 | 15.3 | 27 | 127 | 191 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 515 | 0 | 45 | 68.5 | 119 | 466 | 623 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1210 | 1041 | 90 | 71.8 | 641 | 2175 | 2411 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 391 | 740 | 60 | 34.9 | 230 | 914 | 1150 | 0 | 78 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 186.8 | 63 | 150 | 233 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 20 | 1100 | 90 | 2.2 | 272 | 1082 | 1269 | 0 | 3 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1933 | 0 | 90 | 138.2 | 533 | 1806 | 2002 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 738 | 902 | 60 | 42.0 | 451 | 1522 | 1768 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 38.1 | 715 | 1342 | 1533 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 16 | 45 | 14 | 11.2 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 130 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 11 | 648 | 90 | 2.1 | 165 | 652 | 764 | 0 | 3 |
| ITEM-0119 | B - Core Products | Healthy | 304 | 0 | 30 | 52.2 | 63 | 244 | 366 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 71 | 59 | 30 | 36.5 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 307 | 0 | 7 | 23.1 | 36 | 143 | 422 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 86.4 | 163 | 315 | 385 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 283 | 0 | 14 | 28.7 | 57 | 205 | 412 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 68 | 0 | 7 | 11.3 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 131.8 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 554 | 743 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 75.7 | 773 | 2146 | 2462 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 655 | 0 | 14 | 110.0 | 34 | 124 | 249 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 347 | 0 | 60 | 78.9 | 71 | 340 | 472 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 26 | 121 | 152 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4000 | 0 | 60 | 294.4 | 350 | 1179 | 1370 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 102 | 0 | 45 | 103.1 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 506 | 0 | 14 | 52.5 | 74 | 219 | 354 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 414 | 456 | 30 | 26.7 | 203 | 683 | 900 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1411 | 269 | 60 | 78.8 | 457 | 1550 | 1801 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2332 | 0 | 45 | 238.5 | 153 | 603 | 809 | 0 | — |
| ITEM-0142 | B - Core Products | Lead-time risk | 180 | 1680 | 60 | 14.3 | 552 | 1320 | 1584 | 0 | 15 |
| ITEM-0143 | B - Core Products | Healthy | 509 | 236 | 45 | 46.9 | 170 | 670 | 898 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 933 | 0 | 7 | 74.2 | 38 | 139 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 120 | 470 | 590 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 178 | 636 | 90 | 42.9 | 128 | 506 | 593 | 0 | 43 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 46.9 | 333 | 590 | 949 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 698 | 0 | 60 | 146.1 | 102 | 394 | 494 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 367.1 | 229 | 460 | 513 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 33 | 200 | 60 | 20.5 | 27 | 126 | 174 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 648 | 0 | 14 | 91.8 | 41 | 147 | 295 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 732 | 266 | 30 | 40.4 | 239 | 801 | 1054 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 26.6 | 301 | 487 | 812 | 0 | — |
