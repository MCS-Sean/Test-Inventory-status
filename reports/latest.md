# Synthetic Inventory Health

**Simulation date: 2026-11-14**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 93 |
| Lead-time risk | 6 |
| Reorder | 4 |
| Stockout | 8 |

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
| ITEM-0001 | B - Core Products | Healthy | 432 | 302 | 30 | 33.1 | 138 | 543 | 817 | 0 | — |
| ITEM-0002 | B - Core Products | Reorder | 107 | 0 | 7 | 15.5 | 94 | 150 | 294 | 190 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 488 | 884 | 60 | 31.6 | 395 | 1336 | 1552 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1802 | 0 | 45 | 472.8 | 60 | 236 | 316 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 177 | 0 | 14 | 26.5 | 40 | 141 | 281 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 86 | 46 | 45 | 57.8 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 73 | 125 | 14 | 13.0 | 32 | 117 | 235 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 180 | 0 | 60 | 139.7 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 448 | 0 | 90 | 240.0 | 58 | 228 | 268 | 0 | — |
| ITEM-0011 | A - Top Movers | Reorder | 1463 | 515 | 60 | 83.4 | 913 | 1983 | 2228 | 250 | — |
| ITEM-0012 | A - Top Movers | Excess | 1308 | 0 | 7 | 131.1 | 261 | 341 | 481 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 262 | 90 | 90 | 97.8 | 64 | 308 | 389 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 381 | 0 | 7 | 29.7 | 33 | 136 | 406 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Reorder | 240 | 155 | 45 | 36.8 | 102 | 403 | 539 | 145 | — |
| ITEM-0018 | B - Core Products | Excess | 1045 | 0 | 30 | 374.7 | 32 | 119 | 178 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2587 | 0 | 60 | 250.4 | 214 | 845 | 1062 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 38 | 120 | 14 | 6.9 | 32 | 115 | 232 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 532 | 0 | 60 | 570.0 | 17 | 74 | 102 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 592 | 1999 | 2215 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 21 | 20 | 30 | 40.2 | 6 | 23 | 38 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 155 | 0 | 30 | 82.5 | 16 | 75 | 131 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1011 | 0 | 90 | 206.8 | 149 | 594 | 697 | 0 | — |
| ITEM-0030 | C - Slow Moving | Lead-time risk | 4 | 0 | 7 | 6.3 | 8 | 14 | 33 | 30 | 7 |
| ITEM-0031 | B - Core Products | Excess | 1082 | 0 | 14 | 232.4 | 27 | 97 | 195 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 193 | 135 | 60 | 45.5 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 230 | 0 | 45 | 79.0 | 47 | 181 | 243 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 652 | 0 | 60 | 604.9 | 49 | 115 | 148 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 173 | 245 | 14 | 15.1 | 66 | 239 | 480 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 21.2 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 94 | 0 | 14 | 24.9 | 23 | 80 | 159 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 67 | 355 | 30 | 7.9 | 91 | 355 | 533 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 487 | 315 | 30 | 32.9 | 157 | 617 | 928 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4225 | 0 | 60 | 623.4 | 173 | 587 | 682 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 351 | 335 | 14 | 27.4 | 313 | 506 | 685 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 88 | 100 | 14 | 18.7 | 27 | 98 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 607 | 0 | 45 | 187.1 | 40 | 190 | 287 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 201 | 350 | 90 | 58.7 | 137 | 449 | 552 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 63 | 0 | 45 | 96.1 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 88 | 210 | 7 | 8.9 | 23 | 103 | 312 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 188 | 0 | 7 | 26.1 | 19 | 77 | 229 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4156 | 0 | 60 | 526.8 | 202 | 684 | 794 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 196 | 0 | 14 | 28.5 | 50 | 153 | 250 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 508 | 1950 | 90 | 28.7 | 671 | 2281 | 2529 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1018 | 0 | 30 | 80.2 | 439 | 833 | 1100 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 443 | 0 | 45 | 126.6 | 56 | 217 | 291 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 65 | 105 | 14 | 12.9 | 29 | 105 | 210 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 41 | 43 | 30 | 27.7 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 428 | 0 | 14 | 68.3 | 36 | 130 | 262 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 67.4 | 179 | 426 | 510 | 0 | — |
| ITEM-0065 | B - Core Products | Reorder | 465 | 525 | 60 | 38.1 | 251 | 995 | 1251 | 265 | — |
| ITEM-0066 | B - Core Products | Healthy | 115 | 246 | 45 | 20.8 | 88 | 343 | 459 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 259 | 245 | 14 | 15.6 | 121 | 371 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 263 | 0 | 30 | 63.6 | 45 | 174 | 260 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 39 | 0 | 7 | 14.5 | 6 | 28 | 109 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 10 | 0 | 7 | 15.0 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 881 | 249 | 60 | 78.8 | 232 | 914 | 1149 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3391 | 0 | 90 | 877.0 | 118 | 470 | 552 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 27 | 60 | 14 | 13.4 | 10 | 41 | 101 | 0 | 14 |
| ITEM-0075 | C - Slow Moving | Healthy | 23 | 54 | 45 | 26.2 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 433 | 1037 | 1176 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 294 | 0 | 7 | 164.3 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 410 | 90 | 0.0 | 140 | 430 | 525 | 115 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 221 | 515 | 45 | 20.0 | 173 | 681 | 913 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 472 | 0 | 45 | 206.2 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 342 | 547 | 90 | 48.5 | 217 | 859 | 1006 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 222 | 0 | 7 | 19.5 | 29 | 121 | 360 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 623 | 0 | 14 | 59.0 | 61 | 220 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 312 | 0 | 60 | 133.7 | 49 | 192 | 241 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 28 | 0 | 14 | 28.6 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 143 | 135 | 45 | 32.1 | 55 | 260 | 394 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 32.5 | 456 | 735 | 996 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 53 | 45 | 30 | 35.9 | 13 | 59 | 104 | 0 | 36 |
| ITEM-0092 | B - Core Products | Healthy | 434 | 1289 | 90 | 35.0 | 377 | 1507 | 1768 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 743 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 43 | 99 | 7 | 9.6 | 12 | 48 | 142 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6452 | 0 | 90 | 356.5 | 684 | 2332 | 2585 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3353 | 0 | 60 | 243.6 | 354 | 1194 | 1387 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 102 | 0 | 7 | 21.2 | 13 | 52 | 153 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 75 | 0 | 14 | 25.3 | 17 | 62 | 124 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 165 | 0 | 45 | 93.4 | 22 | 104 | 157 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 84.9 | 317 | 911 | 1048 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 211 | 340 | 45 | 28.3 | 119 | 462 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1112 | 1265 | 90 | 67.1 | 633 | 2142 | 2374 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 464 | 498 | 60 | 42.0 | 226 | 900 | 1132 | 0 | 43 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 225.2 | 56 | 122 | 186 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1046 | 1227 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1304 | 665 | 90 | 87.8 | 567 | 1919 | 2127 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 401 | 1292 | 60 | 23.2 | 444 | 1498 | 1740 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 55 | 0 | 14 | 40.2 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 85 | 50 | 45 | 55.8 | 19 | 90 | 135 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 179 | 708 | 830 | 0 | 1 |
| ITEM-0119 | B - Core Products | Lead-time risk | 190 | 125 | 30 | 31.3 | 65 | 254 | 381 | 0 | 32 |
| ITEM-0120 | C - Slow Moving | Healthy | 56 | 58 | 30 | 29.0 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 174 | 0 | 7 | 14.6 | 31 | 127 | 378 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 167 | 0 | 14 | 41.8 | 106 | 166 | 250 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 336 | 0 | 14 | 35.7 | 54 | 196 | 394 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 75 | 0 | 7 | 12.4 | 17 | 66 | 193 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 211.2 | 275 | 408 | 467 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 403 | 191 | 45 | 45.5 | 139 | 547 | 734 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 410 | 0 | 14 | 67.5 | 35 | 127 | 254 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 200 | 130 | 60 | 49.6 | 66 | 313 | 434 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3463 | 0 | 60 | 258.0 | 345 | 1164 | 1352 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 54.2 | 28 | 76 | 107 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 218 | 0 | 14 | 30.5 | 51 | 159 | 259 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 565 | 238 | 30 | 37.5 | 201 | 668 | 879 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 900 | 799 | 60 | 47.9 | 478 | 1625 | 1888 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1922 | 0 | 45 | 192.8 | 157 | 616 | 825 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 324 | 463 | 45 | 30.8 | 166 | 651 | 871 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 441 | 0 | 7 | 35.1 | 36 | 137 | 401 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 829 | 0 | 60 | 187.0 | 92 | 363 | 456 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 78 | 636 | 90 | 27.2 | 89 | 350 | 411 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 776 | 0 | 14 | 63.4 | 242 | 426 | 683 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 561 | 0 | 60 | 159.8 | 73 | 288 | 361 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 178 | 0 | 60 | 132.4 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 365 | 0 | 14 | 50.5 | 42 | 151 | 302 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 606 | 259 | 30 | 34.5 | 233 | 779 | 1025 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 701 | 0 | 7 | 31.6 | 322 | 500 | 810 | 0 | — |
