# Synthetic Inventory Health

**Simulation date: 2026-11-12**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 96 |
| Lead-time risk | 5 |
| Reorder | 4 |
| Stockout | 7 |

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
| ITEM-0001 | B - Core Products | Healthy | 458 | 302 | 30 | 35.3 | 137 | 539 | 812 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 167 | 0 | 7 | 26.2 | 91 | 142 | 276 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 513 | 884 | 60 | 33.3 | 395 | 1335 | 1550 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1810 | 0 | 45 | 474.9 | 60 | 236 | 316 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 187 | 0 | 14 | 27.3 | 41 | 144 | 288 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 89 | 0 | 45 | 60.2 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 87 | 125 | 14 | 15.6 | 32 | 116 | 234 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 183 | 0 | 60 | 144.5 | 21 | 99 | 137 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 46 | 410 | 90 | 25.1 | 57 | 224 | 263 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1564 | 515 | 60 | 95.3 | 890 | 1892 | 2121 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 266 | 90 | 90 | 98.5 | 64 | 310 | 391 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 406 | 0 | 7 | 31.5 | 33 | 137 | 407 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 257 | 155 | 45 | 39.4 | 102 | 403 | 539 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1051 | 0 | 30 | 376.9 | 32 | 119 | 178 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2598 | 0 | 60 | 249.3 | 216 | 852 | 1071 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 52 | 120 | 14 | 9.6 | 32 | 114 | 228 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 535 | 0 | 60 | 587.2 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 594 | 2004 | 2221 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 21 | 20 | 30 | 39.4 | 7 | 24 | 40 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 160 | 0 | 30 | 85.7 | 16 | 74 | 130 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1022 | 0 | 90 | 211.9 | 147 | 586 | 688 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 15 | 0 | 7 | 26.0 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1095 | 0 | 14 | 239.2 | 27 | 96 | 192 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 202 | 135 | 60 | 47.6 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 236 | 0 | 45 | 81.7 | 47 | 180 | 241 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 652 | 0 | 60 | 604.9 | 49 | 115 | 148 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 199 | 245 | 14 | 17.5 | 66 | 237 | 476 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 20.6 | 110 | 167 | 314 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 107 | 0 | 14 | 29.2 | 22 | 77 | 154 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 95 | 355 | 30 | 11.4 | 89 | 349 | 525 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 514 | 315 | 30 | 34.4 | 158 | 622 | 936 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4241 | 0 | 60 | 629.9 | 172 | 583 | 677 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 351 | 335 | 14 | 27.4 | 313 | 506 | 685 | 0 | — |
| ITEM-0042 | B - Core Products | Reorder | 96 | 0 | 14 | 20.5 | 27 | 98 | 196 | 100 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 499 | 1324 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 615 | 0 | 45 | 190.9 | 40 | 189 | 285 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 95.6 | 113 | 287 | 372 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 66 | 0 | 45 | 102.4 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Reorder | 103 | 0 | 7 | 10.3 | 23 | 103 | 313 | 210 | — |
| ITEM-0053 | B - Core Products | Healthy | 49 | 155 | 7 | 6.8 | 19 | 77 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4179 | 0 | 60 | 535.0 | 200 | 677 | 786 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 211 | 0 | 14 | 30.5 | 51 | 155 | 252 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 527 | 1950 | 90 | 29.3 | 682 | 2320 | 2572 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 448 | 0 | 45 | 126.0 | 56 | 220 | 295 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 80 | 105 | 14 | 16.3 | 28 | 102 | 205 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 46 | 43 | 30 | 31.6 | 13 | 59 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 438 | 0 | 14 | 69.2 | 36 | 131 | 264 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 60.3 | 191 | 467 | 561 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 491 | 525 | 60 | 40.3 | 251 | 995 | 1251 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 128 | 246 | 45 | 23.3 | 87 | 340 | 456 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 279 | 245 | 14 | 16.5 | 122 | 375 | 612 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 275 | 0 | 30 | 66.9 | 45 | 173 | 259 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 44 | 0 | 7 | 16.2 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 12 | 0 | 7 | 18.3 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 906 | 249 | 60 | 80.9 | 233 | 917 | 1152 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3401 | 0 | 90 | 877.0 | 118 | 471 | 553 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 32 | 60 | 14 | 16.0 | 10 | 40 | 100 | 0 | 17 |
| ITEM-0075 | C - Slow Moving | Healthy | 23 | 54 | 45 | 25.9 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 958 | 1084 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 300 | 0 | 7 | 168.8 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 13 | 290 | 90 | 5.2 | 121 | 348 | 423 | 120 | 6 |
| ITEM-0079 | B - Core Products | Healthy | 242 | 515 | 45 | 22.0 | 173 | 678 | 909 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 477 | 0 | 45 | 211.5 | 28 | 132 | 200 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 357 | 547 | 90 | 51.0 | 216 | 853 | 1000 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 255 | 0 | 7 | 22.4 | 29 | 121 | 359 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 627 | 0 | 14 | 58.1 | 62 | 224 | 451 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 319 | 0 | 60 | 140.7 | 48 | 187 | 234 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 32 | 0 | 14 | 33.5 | 6 | 21 | 49 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 157 | 135 | 45 | 35.2 | 55 | 260 | 394 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 31.6 | 457 | 745 | 1013 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 57 | 45 | 30 | 38.9 | 13 | 59 | 103 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 464 | 1289 | 90 | 37.6 | 375 | 1499 | 1758 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 744 | 0 | — |
| ITEM-0094 | B - Core Products | Reorder | 46 | 0 | 7 | 10.0 | 12 | 49 | 145 | 99 | — |
| ITEM-0095 | A - Top Movers | Excess | 6480 | 0 | 90 | 353.2 | 693 | 2363 | 2620 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3395 | 0 | 60 | 247.0 | 353 | 1192 | 1384 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 115 | 0 | 7 | 23.9 | 13 | 52 | 153 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 84 | 0 | 14 | 28.7 | 17 | 61 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 172 | 0 | 45 | 98.6 | 22 | 103 | 155 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 84.9 | 317 | 911 | 1048 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 226 | 340 | 45 | 30.3 | 119 | 463 | 620 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 589 | 1789 | 90 | 34.9 | 642 | 2178 | 2415 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 480 | 498 | 60 | 43.2 | 228 | 907 | 1141 | 0 | 44 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 228.6 | 56 | 122 | 185 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 264 | 1051 | 1233 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1329 | 665 | 90 | 90.2 | 563 | 1904 | 2110 | 0 | — |
| ITEM-0112 | A - Top Movers | Reorder | 436 | 1047 | 60 | 25.4 | 441 | 1488 | 1728 | 245 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 13 | 45 | 14 | 9.4 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 87 | 50 | 45 | 57.2 | 19 | 90 | 135 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 180 | 713 | 836 | 0 | 1 |
| ITEM-0119 | B - Core Products | Lead-time risk | 204 | 125 | 30 | 33.9 | 65 | 252 | 379 | 0 | 34 |
| ITEM-0120 | C - Slow Moving | Healthy | 62 | 58 | 30 | 32.4 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 202 | 0 | 7 | 16.6 | 32 | 130 | 385 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 167 | 0 | 14 | 41.8 | 106 | 166 | 250 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 140 | 211 | 14 | 14.8 | 55 | 197 | 396 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 94 | 0 | 7 | 15.8 | 17 | 65 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 413 | 191 | 45 | 46.9 | 138 | 543 | 728 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 418 | 0 | 14 | 67.9 | 35 | 128 | 257 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 209 | 130 | 60 | 51.7 | 66 | 313 | 435 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3484 | 0 | 60 | 257.6 | 347 | 1172 | 1362 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 54.2 | 28 | 76 | 107 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 239 | 0 | 14 | 33.0 | 53 | 162 | 263 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 606 | 238 | 30 | 40.6 | 198 | 661 | 869 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 675 | 1068 | 60 | 36.4 | 472 | 1604 | 1863 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1951 | 0 | 45 | 198.2 | 155 | 608 | 815 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 355 | 463 | 45 | 34.0 | 165 | 646 | 865 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 469 | 0 | 7 | 37.0 | 37 | 139 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 838 | 0 | 60 | 186.2 | 93 | 368 | 462 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 80 | 636 | 90 | 27.2 | 91 | 359 | 421 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 776 | 0 | 14 | 63.4 | 242 | 426 | 683 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 571 | 0 | 60 | 161.6 | 74 | 290 | 364 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 181 | 0 | 60 | 134.6 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 381 | 0 | 14 | 53.4 | 41 | 148 | 298 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 651 | 259 | 30 | 37.4 | 231 | 771 | 1015 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 701 | 0 | 7 | 31.6 | 322 | 500 | 810 | 0 | — |
