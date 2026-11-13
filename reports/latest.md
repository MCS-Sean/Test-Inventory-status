# Synthetic Inventory Health

**Simulation date: 2026-11-13**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 97 |
| Lead-time risk | 5 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Healthy | 444 | 302 | 30 | 34.0 | 138 | 544 | 818 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 167 | 0 | 7 | 26.2 | 91 | 142 | 276 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 498 | 884 | 60 | 32.5 | 393 | 1330 | 1544 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1808 | 0 | 45 | 477.2 | 60 | 235 | 314 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 181 | 0 | 14 | 26.9 | 40 | 141 | 283 | 0 | — |
| ITEM-0007 | C - Slow Moving | Reorder | 87 | 0 | 45 | 58.4 | 19 | 88 | 133 | 46 | — |
| ITEM-0008 | B - Core Products | Healthy | 80 | 125 | 14 | 14.2 | 32 | 117 | 235 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 182 | 0 | 60 | 143.7 | 21 | 99 | 137 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 43 | 410 | 90 | 23.3 | 57 | 225 | 264 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1564 | 515 | 60 | 95.3 | 890 | 1892 | 2121 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1308 | 0 | 7 | 122.5 | 263 | 349 | 498 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 264 | 90 | 90 | 98.2 | 64 | 309 | 390 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 391 | 0 | 7 | 30.3 | 33 | 137 | 408 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 145 | 0 | 7 | 88.8 | 20 | 34 | 83 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 252 | 155 | 45 | 38.8 | 102 | 401 | 537 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1051 | 0 | 30 | 386.1 | 31 | 116 | 173 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2587 | 0 | 60 | 248.5 | 216 | 852 | 1070 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 45 | 120 | 14 | 8.1 | 32 | 115 | 231 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 534 | 0 | 60 | 579.0 | 17 | 74 | 101 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 593 | 2002 | 2219 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 21 | 20 | 30 | 39.4 | 7 | 24 | 40 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 156 | 0 | 30 | 82.6 | 16 | 75 | 132 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1016 | 0 | 90 | 208.3 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 15 | 0 | 7 | 29.3 | 7 | 12 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1092 | 0 | 14 | 239.1 | 27 | 96 | 192 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 198 | 135 | 60 | 46.5 | 68 | 328 | 456 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 235 | 0 | 45 | 81.7 | 47 | 180 | 240 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 652 | 0 | 60 | 604.9 | 49 | 115 | 148 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 186 | 245 | 14 | 16.3 | 66 | 238 | 478 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 145 | 170 | 7 | 21.2 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 99 | 0 | 14 | 26.5 | 23 | 79 | 158 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 78 | 355 | 30 | 9.2 | 90 | 352 | 530 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 500 | 315 | 30 | 33.6 | 157 | 618 | 931 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4231 | 0 | 60 | 622.2 | 174 | 589 | 684 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 351 | 335 | 14 | 27.4 | 313 | 506 | 685 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 92 | 100 | 14 | 19.5 | 27 | 98 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 612 | 0 | 45 | 189.3 | 40 | 189 | 286 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 95.6 | 113 | 287 | 372 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 66 | 0 | 45 | 102.4 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 95 | 210 | 7 | 9.6 | 23 | 103 | 312 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 40 | 155 | 7 | 5.5 | 19 | 77 | 229 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4163 | 0 | 60 | 523.3 | 204 | 690 | 801 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 202 | 0 | 14 | 29.3 | 51 | 155 | 252 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 521 | 1950 | 90 | 29.4 | 673 | 2288 | 2537 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 446 | 0 | 45 | 126.6 | 56 | 219 | 292 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 71 | 105 | 14 | 14.2 | 29 | 104 | 209 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 44 | 43 | 30 | 30.0 | 13 | 59 | 103 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 434 | 0 | 14 | 68.9 | 36 | 131 | 263 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 60.3 | 191 | 467 | 561 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 482 | 525 | 60 | 39.6 | 251 | 994 | 1249 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 122 | 246 | 45 | 22.1 | 88 | 342 | 458 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 269 | 245 | 14 | 16.1 | 122 | 374 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 267 | 0 | 30 | 63.9 | 46 | 176 | 264 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 41 | 0 | 7 | 15.1 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 11 | 0 | 7 | 16.5 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 890 | 249 | 60 | 79.5 | 232 | 915 | 1150 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3396 | 0 | 90 | 878.3 | 118 | 470 | 552 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 30 | 60 | 14 | 15.1 | 9 | 39 | 99 | 0 | 16 |
| ITEM-0075 | C - Slow Moving | Healthy | 23 | 54 | 45 | 26.2 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 958 | 1084 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 297 | 0 | 7 | 166.0 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 410 | 90 | 0.0 | 133 | 396 | 483 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 231 | 515 | 45 | 21.1 | 172 | 675 | 904 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 474 | 0 | 45 | 209.1 | 28 | 133 | 201 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 349 | 547 | 90 | 49.5 | 218 | 861 | 1009 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 235 | 0 | 7 | 20.7 | 29 | 120 | 359 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 627 | 0 | 14 | 58.4 | 62 | 223 | 449 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 315 | 0 | 60 | 136.3 | 48 | 189 | 238 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 30 | 0 | 14 | 31.0 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 149 | 135 | 45 | 33.4 | 55 | 260 | 394 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 31.6 | 457 | 745 | 1013 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 54 | 45 | 30 | 36.0 | 14 | 61 | 106 | 0 | 37 |
| ITEM-0092 | B - Core Products | Healthy | 449 | 1289 | 90 | 36.2 | 377 | 1505 | 1765 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 744 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 43 | 99 | 7 | 9.4 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6457 | 0 | 90 | 351.6 | 694 | 2366 | 2623 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3376 | 0 | 60 | 246.0 | 352 | 1190 | 1382 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 108 | 0 | 7 | 22.3 | 13 | 52 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 80 | 0 | 14 | 27.4 | 17 | 61 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 169 | 0 | 45 | 96.9 | 22 | 103 | 155 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 84.9 | 317 | 911 | 1048 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 217 | 340 | 45 | 29.0 | 119 | 463 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1112 | 1265 | 90 | 66.3 | 639 | 2166 | 2401 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 469 | 498 | 60 | 42.4 | 227 | 903 | 1135 | 0 | 43 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 228.6 | 56 | 122 | 185 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 264 | 1050 | 1231 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1318 | 665 | 90 | 89.3 | 563 | 1906 | 2113 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 419 | 1292 | 60 | 24.4 | 441 | 1487 | 1727 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 12 | 45 | 14 | 8.8 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 86 | 50 | 45 | 56.5 | 19 | 90 | 135 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 180 | 714 | 838 | 0 | 1 |
| ITEM-0119 | B - Core Products | Lead-time risk | 196 | 125 | 30 | 32.4 | 65 | 253 | 380 | 0 | 33 |
| ITEM-0120 | C - Slow Moving | Healthy | 59 | 58 | 30 | 30.9 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 186 | 0 | 7 | 15.4 | 32 | 129 | 382 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 167 | 0 | 14 | 41.8 | 106 | 166 | 250 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 342 | 0 | 14 | 35.9 | 55 | 198 | 398 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 83 | 0 | 7 | 13.8 | 17 | 66 | 192 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 408 | 191 | 45 | 46.3 | 138 | 544 | 729 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 417 | 0 | 14 | 68.1 | 35 | 127 | 256 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 203 | 130 | 60 | 50.2 | 66 | 313 | 435 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3470 | 0 | 60 | 257.7 | 346 | 1168 | 1356 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 54.2 | 28 | 76 | 107 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 229 | 0 | 14 | 31.7 | 53 | 162 | 263 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 578 | 238 | 30 | 38.3 | 201 | 669 | 880 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 922 | 799 | 60 | 49.5 | 475 | 1613 | 1874 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1935 | 0 | 45 | 194.1 | 157 | 616 | 825 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 341 | 463 | 45 | 32.6 | 165 | 646 | 866 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 455 | 0 | 7 | 36.3 | 36 | 137 | 400 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 833 | 0 | 60 | 187.0 | 92 | 364 | 458 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 79 | 636 | 90 | 27.2 | 90 | 354 | 415 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 776 | 0 | 14 | 63.4 | 242 | 426 | 683 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 565 | 0 | 60 | 159.9 | 74 | 290 | 364 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 179 | 0 | 60 | 131.0 | 23 | 107 | 148 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 372 | 0 | 14 | 51.6 | 42 | 151 | 302 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 621 | 259 | 30 | 35.3 | 233 | 779 | 1025 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 701 | 0 | 7 | 31.6 | 322 | 500 | 810 | 0 | — |
