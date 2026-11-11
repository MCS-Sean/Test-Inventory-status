# Synthetic Inventory Health

**Simulation date: 2026-11-11**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 98 |
| Lead-time risk | 4 |
| Reorder | 3 |
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
| ITEM-0001 | B - Core Products | Healthy | 465 | 302 | 30 | 35.8 | 137 | 540 | 812 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 167 | 0 | 7 | 26.2 | 91 | 142 | 276 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 529 | 884 | 60 | 34.6 | 392 | 1324 | 1538 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1815 | 0 | 45 | 479.0 | 60 | 235 | 314 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 191 | 0 | 14 | 27.7 | 41 | 145 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 90 | 0 | 45 | 60.4 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 89 | 125 | 14 | 15.8 | 32 | 117 | 235 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 184 | 0 | 60 | 142.8 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 48 | 410 | 90 | 26.2 | 57 | 224 | 263 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1564 | 515 | 60 | 95.3 | 890 | 1892 | 2121 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 269 | 90 | 90 | 99.2 | 64 | 311 | 393 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 420 | 0 | 7 | 32.6 | 33 | 137 | 407 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 263 | 155 | 45 | 40.5 | 102 | 401 | 538 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1055 | 0 | 30 | 378.3 | 32 | 119 | 178 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2606 | 0 | 60 | 250.8 | 215 | 849 | 1067 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 64 | 120 | 14 | 11.9 | 31 | 112 | 225 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 536 | 0 | 60 | 588.3 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 592 | 1998 | 2214 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 22 | 20 | 30 | 42.1 | 6 | 23 | 38 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 161 | 0 | 30 | 84.7 | 16 | 75 | 132 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1022 | 0 | 90 | 207.6 | 150 | 598 | 702 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 15 | 0 | 7 | 26.0 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1102 | 0 | 14 | 240.7 | 27 | 96 | 192 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 208 | 135 | 60 | 49.3 | 68 | 326 | 453 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 239 | 0 | 45 | 82.4 | 47 | 181 | 242 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 652 | 0 | 60 | 604.9 | 49 | 115 | 148 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 206 | 245 | 14 | 18.1 | 66 | 237 | 476 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 20.6 | 110 | 167 | 314 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 112 | 0 | 14 | 30.4 | 22 | 78 | 155 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 109 | 355 | 30 | 13.1 | 89 | 347 | 521 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 531 | 315 | 30 | 35.9 | 157 | 616 | 927 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4253 | 0 | 60 | 629.6 | 173 | 586 | 680 | 0 | — |
| ITEM-0041 | A - Top Movers | Reorder | 351 | 0 | 14 | 27.4 | 313 | 506 | 685 | 335 | — |
| ITEM-0042 | B - Core Products | Healthy | 101 | 0 | 14 | 21.5 | 27 | 98 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 499 | 1324 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 618 | 0 | 45 | 191.1 | 40 | 189 | 286 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 95.6 | 113 | 287 | 372 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 185.3 | 84 | 127 | 186 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 66 | 0 | 45 | 100.7 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 118 | 0 | 7 | 11.9 | 22 | 102 | 311 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 58 | 155 | 7 | 8.0 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4192 | 0 | 60 | 539.0 | 199 | 674 | 783 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 222 | 0 | 14 | 31.9 | 51 | 156 | 253 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 557 | 1950 | 90 | 31.0 | 679 | 2312 | 2564 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 452 | 0 | 45 | 125.9 | 57 | 223 | 298 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 86 | 105 | 14 | 17.4 | 28 | 102 | 206 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 49 | 43 | 30 | 33.9 | 13 | 58 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 446 | 0 | 14 | 69.9 | 37 | 133 | 267 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 60.3 | 191 | 467 | 561 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 505 | 525 | 60 | 41.4 | 252 | 997 | 1253 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 130 | 246 | 45 | 23.5 | 88 | 343 | 458 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 300 | 245 | 14 | 17.9 | 122 | 374 | 609 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 278 | 0 | 30 | 67.6 | 45 | 173 | 259 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 47 | 0 | 7 | 17.3 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 13 | 0 | 7 | 19.8 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 912 | 249 | 60 | 81.7 | 232 | 914 | 1148 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3408 | 0 | 90 | 873.8 | 119 | 474 | 556 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 36 | 60 | 14 | 18.3 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 24 | 54 | 45 | 27.3 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 958 | 1084 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 302 | 0 | 7 | 169.9 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 25.3 | 107 | 295 | 356 | 0 | 26 |
| ITEM-0079 | B - Core Products | Healthy | 242 | 515 | 45 | 21.8 | 175 | 687 | 921 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 480 | 0 | 45 | 213.9 | 28 | 132 | 199 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 363 | 547 | 90 | 51.4 | 218 | 861 | 1009 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 259 | 0 | 7 | 22.5 | 29 | 121 | 363 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 637 | 0 | 14 | 59.6 | 62 | 223 | 447 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 324 | 0 | 60 | 144.4 | 47 | 184 | 232 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 33 | 0 | 14 | 33.8 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 167 | 135 | 45 | 38.2 | 54 | 255 | 386 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 31.6 | 457 | 745 | 1013 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Reorder | 59 | 0 | 30 | 40.5 | 13 | 59 | 102 | 45 | — |
| ITEM-0092 | B - Core Products | Reorder | 473 | 1027 | 90 | 38.2 | 376 | 1502 | 1762 | 262 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 744 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 53 | 0 | 7 | 11.7 | 12 | 49 | 144 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6493 | 0 | 90 | 354.6 | 692 | 2359 | 2615 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3411 | 0 | 60 | 248.8 | 352 | 1189 | 1381 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 125 | 0 | 7 | 26.3 | 13 | 52 | 151 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 87 | 0 | 14 | 29.8 | 17 | 61 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1145 | 675 | 60 | 72.8 | 724 | 1684 | 1904 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 174 | 0 | 45 | 99.7 | 22 | 103 | 155 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 84.9 | 317 | 911 | 1048 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 229 | 340 | 45 | 30.6 | 119 | 463 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 600 | 1789 | 90 | 35.4 | 645 | 2188 | 2426 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 496 | 498 | 60 | 44.8 | 227 | 903 | 1136 | 0 | 45 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1046 | 1227 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1342 | 665 | 90 | 91.5 | 560 | 1895 | 2100 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 459 | 1047 | 60 | 26.9 | 439 | 1481 | 1719 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 14 | 45 | 14 | 10.2 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 88 | 50 | 45 | 57.8 | 19 | 90 | 135 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 181 | 716 | 840 | 0 | 1 |
| ITEM-0119 | B - Core Products | Lead-time risk | 213 | 125 | 30 | 35.6 | 64 | 250 | 375 | 0 | 36 |
| ITEM-0120 | C - Slow Moving | Healthy | 64 | 58 | 30 | 33.3 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 221 | 0 | 7 | 18.2 | 32 | 130 | 385 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 167 | 0 | 14 | 41.8 | 106 | 166 | 250 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 149 | 211 | 14 | 15.5 | 56 | 200 | 402 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 98 | 0 | 7 | 16.5 | 17 | 65 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 420 | 191 | 45 | 47.7 | 138 | 543 | 728 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 427 | 0 | 14 | 69.7 | 35 | 127 | 256 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 211 | 130 | 60 | 51.7 | 66 | 315 | 438 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3489 | 0 | 60 | 257.0 | 348 | 1177 | 1367 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 54.2 | 28 | 76 | 107 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 253 | 0 | 14 | 35.4 | 52 | 160 | 260 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 622 | 238 | 30 | 41.7 | 198 | 661 | 869 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 683 | 1068 | 60 | 36.5 | 476 | 1618 | 1880 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1963 | 0 | 45 | 198.7 | 155 | 610 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 365 | 463 | 45 | 34.6 | 167 | 653 | 875 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 479 | 0 | 7 | 37.8 | 37 | 139 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 847 | 0 | 60 | 189.6 | 92 | 365 | 459 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 81 | 636 | 90 | 27.4 | 91 | 360 | 423 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 577 | 0 | 60 | 164.9 | 73 | 287 | 360 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 183 | 0 | 60 | 135.0 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 393 | 0 | 14 | 55.8 | 41 | 147 | 295 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 683 | 259 | 30 | 39.7 | 228 | 762 | 1003 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 203 | 498 | 7 | 9.2 | 322 | 500 | 810 | 0 | — |
