# Synthetic Inventory Health

**Simulation date: 2026-10-17**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 88 |
| Lead-time risk | 3 |
| Reorder | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 468 | 291 | 30 | 36.0 | 137 | 540 | 813 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 220 | 0 | 7 | 33.6 | 91 | 144 | 281 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 417 | 968 | 60 | 27.3 | 392 | 1324 | 1537 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1903 | 0 | 45 | 395.5 | 78 | 300 | 401 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 202 | 0 | 14 | 27.8 | 42 | 151 | 304 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 126 | 0 | 45 | 79.9 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 97 | 145 | 14 | 14.8 | 40 | 139 | 276 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 220 | 0 | 60 | 158.4 | 24 | 109 | 151 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 96 | 410 | 90 | 45.5 | 66 | 259 | 303 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 732 | 1495 | 1670 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 334 | 90 | 90 | 113.9 | 70 | 337 | 425 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 771 | 0 | 7 | 61.5 | 32 | 133 | 396 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 199 | 0 | 7 | 139.9 | 21 | 33 | 76 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 420 | 0 | 45 | 62.5 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1127 | 0 | 30 | 326.1 | 40 | 148 | 220 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2859 | 0 | 60 | 274.0 | 216 | 853 | 1072 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 210 | 0 | 14 | 33.1 | 38 | 134 | 267 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 561 | 0 | 60 | 548.8 | 19 | 82 | 113 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 604 | 2049 | 2272 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 38 | 0 | 30 | 67.1 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 41.6 | 766 | 1501 | 1669 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 202 | 0 | 30 | 88.3 | 26 | 97 | 146 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 196 | 960 | 90 | 35.6 | 170 | 672 | 788 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1233 | 0 | 14 | 230.7 | 33 | 114 | 226 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 310 | 135 | 60 | 71.2 | 70 | 336 | 467 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 309 | 0 | 45 | 88.8 | 56 | 216 | 290 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 383.6 | 68 | 177 | 230 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 198 | 265 | 14 | 16.6 | 67 | 246 | 496 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 110 | 0 | 14 | 24.8 | 27 | 94 | 187 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 313 | 172 | 30 | 38.4 | 87 | 340 | 511 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 265 | 605 | 30 | 18.2 | 156 | 608 | 913 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4429 | 0 | 60 | 584.5 | 195 | 658 | 764 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 500 | 210 | 14 | 42.7 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 99 | 116 | 14 | 19.6 | 30 | 106 | 212 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 466 | 1222 | 1396 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 692 | 0 | 45 | 204.9 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 257 | 330 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 42 | 760 | 60 | 6.6 | 276 | 664 | 797 | 0 | 7 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 84 | 0 | 45 | 112.8 | 11 | 46 | 68 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 224 | 154 | 60 | 67.0 | 133 | 338 | 438 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 129 | 0 | 7 | 12.6 | 25 | 107 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Reorder | 77 | 0 | 7 | 10.6 | 20 | 78 | 231 | 155 | — |
| ITEM-0054 | A - Top Movers | Excess | 4418 | 0 | 60 | 492.7 | 235 | 782 | 908 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 392 | 0 | 14 | 48.5 | 60 | 182 | 295 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 951 | 1680 | 90 | 51.0 | 705 | 2403 | 2664 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 78.2 | 471 | 923 | 1230 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 556 | 0 | 45 | 142.6 | 64 | 244 | 326 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 101 | 0 | 14 | 21.2 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 88 | 0 | 30 | 55.4 | 15 | 65 | 112 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 587 | 0 | 14 | 87.8 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 433 | 310 | 60 | 78.3 | 229 | 567 | 683 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 824 | 260 | 60 | 69.4 | 246 | 971 | 1220 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 290 | 115 | 45 | 54.1 | 84 | 331 | 443 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 479 | 0 | 14 | 29.7 | 118 | 360 | 586 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 393 | 0 | 30 | 79.8 | 57 | 210 | 313 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 24 | 85 | 7 | 8.7 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 32.6 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 226 | 892 | 1121 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3503 | 0 | 90 | 747.1 | 144 | 571 | 670 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 24 | 61 | 14 | 11.7 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 48 | 26 | 45 | 54.7 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 727 | 90 | 0.0 | 288 | 644 | 727 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 348 | 0 | 7 | 159.0 | 6 | 24 | 90 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 287 | 540 | 45 | 24.5 | 185 | 725 | 972 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 544 | 0 | 45 | 243.6 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 380 | 558 | 90 | 54.9 | 213 | 843 | 989 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 35 | 240 | 7 | 3.1 | 27 | 117 | 352 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 904 | 0 | 14 | 81.9 | 64 | 230 | 462 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 53 | 337 | 60 | 21.3 | 53 | 205 | 258 | 0 | — |
| ITEM-0085 | B - Core Products | Reorder | 296 | 0 | 14 | 36.6 | 206 | 328 | 497 | 205 | — |
| ITEM-0086 | C - Slow Moving | Reorder | 24 | 0 | 14 | 21.6 | 7 | 24 | 57 | 35 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 291 | 0 | 45 | 68.6 | 52 | 248 | 375 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 42 | 50 | 30 | 28.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 750 | 1027 | 90 | 59.5 | 384 | 1531 | 1796 | 0 | 95 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 32.7 | 255 | 396 | 766 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 68 | 0 | 7 | 13.5 | 15 | 56 | 161 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6970 | 0 | 90 | 390.6 | 679 | 2303 | 2553 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3721 | 0 | 60 | 263.9 | 362 | 1223 | 1420 | 0 | — |
| ITEM-0097 | B - Core Products | Reorder | 73 | 0 | 7 | 11.2 | 104 | 157 | 294 | 225 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 129 | 0 | 7 | 21.5 | 20 | 69 | 195 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 156 | 0 | 14 | 43.3 | 23 | 77 | 153 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 55.8 | 707 | 1641 | 1856 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 223 | 0 | 45 | 112.8 | 25 | 116 | 176 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 82.3 | 385 | 1146 | 1321 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 417 | 180 | 45 | 55.7 | 119 | 464 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1035 | 1286 | 90 | 62.3 | 632 | 2143 | 2375 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 282 | 740 | 60 | 26.0 | 223 | 886 | 1115 | 0 | 71 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 269 | 1071 | 1256 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1777 | 0 | 90 | 130.9 | 519 | 1755 | 1945 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 540 | 1161 | 60 | 31.3 | 445 | 1497 | 1739 | 0 | — |
| ITEM-0113 | A - Top Movers | Reorder | 705 | 760 | 45 | 38.0 | 826 | 1679 | 1938 | 475 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 46 | 0 | 14 | 33.7 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 96.6 | 241 | 397 | 615 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 169 | 668 | 783 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 226 | 135 | 30 | 38.1 | 64 | 248 | 373 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 52 | 59 | 30 | 27.4 | 17 | 76 | 133 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 190 | 0 | 7 | 14.3 | 34 | 141 | 419 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 96 | 92 | 14 | 33.5 | 65 | 108 | 194 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 170 | 216 | 14 | 16.9 | 59 | 210 | 421 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 113 | 0 | 7 | 18.8 | 16 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 214.3 | 290 | 452 | 525 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 660 | 0 | 45 | 74.0 | 140 | 551 | 738 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 577 | 0 | 14 | 95.3 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 310 | 130 | 60 | 73.0 | 68 | 327 | 455 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 130 | 163 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3826 | 0 | 60 | 276.4 | 356 | 1201 | 1395 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 433 | 0 | 14 | 50.2 | 64 | 194 | 315 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 483 | 229 | 30 | 31.5 | 203 | 679 | 894 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1227 | 539 | 60 | 68.7 | 457 | 1547 | 1797 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2225 | 0 | 45 | 229.6 | 154 | 600 | 804 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 565 | 1295 | 1547 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 401 | 470 | 45 | 37.5 | 168 | 661 | 885 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 812 | 0 | 7 | 65.0 | 37 | 137 | 400 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 108 | 422 | 529 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 153 | 636 | 90 | 42.5 | 111 | 439 | 515 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 416 | 385 | 14 | 20.8 | 369 | 669 | 1088 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 670 | 0 | 60 | 159.1 | 90 | 347 | 436 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 19 | 200 | 60 | 12.7 | 25 | 117 | 162 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 568 | 0 | 14 | 77.2 | 43 | 154 | 308 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 518 | 540 | 30 | 28.0 | 242 | 817 | 1076 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 26.8 | 279 | 438 | 716 | 0 | — |
