# Synthetic Inventory Health

**Simulation date: 2026-11-27**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 22 |
| Healthy | 104 |
| Lead-time risk | 6 |
| Reorder | 2 |
| Stockout | 4 |

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
| ITEM-0001 | B - Core Products | Reorder | 246 | 302 | 30 | 18.3 | 142 | 560 | 843 | 295 | — |
| ITEM-0002 | B - Core Products | Healthy | 163 | 185 | 7 | 19.5 | 105 | 173 | 348 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 329 | 1107 | 60 | 21.8 | 390 | 1312 | 1523 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1719 | 0 | 45 | 420.4 | 66 | 255 | 340 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 77 | 150 | 14 | 11.0 | 41 | 146 | 293 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 61 | 46 | 45 | 40.7 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 106 | 130 | 14 | 18.2 | 42 | 130 | 212 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 153 | 0 | 60 | 110.2 | 24 | 109 | 151 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 416 | 0 | 90 | 220.2 | 59 | 231 | 271 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1422 | 765 | 60 | 97.7 | 802 | 1690 | 1894 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1111 | 0 | 7 | 91.3 | 272 | 370 | 540 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 230 | 90 | 90 | 88.5 | 62 | 299 | 377 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 200 | 0 | 7 | 15.0 | 33 | 140 | 420 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 101 | 0 | 7 | 49.1 | 24 | 41 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 156 | 80 | 45 | 63.2 | 74 | 188 | 262 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 165 | 300 | 45 | 26.2 | 98 | 388 | 520 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 988 | 0 | 30 | 330.6 | 34 | 127 | 190 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2443 | 0 | 60 | 238.2 | 213 | 839 | 1054 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 68 | 135 | 14 | 12.1 | 34 | 119 | 236 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 519 | 0 | 60 | 583.9 | 16 | 71 | 97 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2135 | 0 | 90 | 136.0 | 602 | 2031 | 2251 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 11 | 20 | 30 | 20.6 | 7 | 24 | 40 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 650 | 1299 | 60 | 41.0 | 925 | 1892 | 2114 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 122 | 0 | 30 | 63.1 | 17 | 77 | 135 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 928 | 0 | 90 | 187.3 | 151 | 602 | 707 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.0 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1014 | 0 | 14 | 223.1 | 27 | 96 | 191 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 138 | 265 | 60 | 32.2 | 69 | 331 | 460 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 162 | 75 | 45 | 51.0 | 52 | 199 | 265 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 272 | 0 | 14 | 24.0 | 65 | 235 | 473 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 216 | 0 | 7 | 32.2 | 108 | 162 | 303 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 40 | 90 | 14 | 10.8 | 22 | 78 | 155 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 109 | 364 | 30 | 12.6 | 92 | 361 | 543 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 289 | 635 | 30 | 19.5 | 157 | 618 | 930 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4108 | 0 | 60 | 584.1 | 181 | 611 | 709 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 565 | 0 | 14 | 46.1 | 232 | 416 | 674 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 122 | 0 | 14 | 26.8 | 27 | 96 | 191 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 475 | 1227 | 1400 | 0 | — |
| ITEM-0044 | C - Slow Moving | Excess | 568 | 0 | 45 | 175.1 | 40 | 190 | 287 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 306 | 235 | 90 | 97.3 | 127 | 414 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 112.3 | 107 | 255 | 328 | 0 | — |
| ITEM-0047 | B - Core Products | Healthy | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 55 | 0 | 45 | 83.9 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 344 | 465 | 60 | 51.8 | 264 | 670 | 809 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 191 | 0 | 7 | 19.6 | 23 | 101 | 305 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 91 | 0 | 7 | 12.4 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4052 | 0 | 60 | 513.6 | 201 | 683 | 793 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 75 | 100 | 14 | 10.4 | 54 | 163 | 264 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 280 | 2220 | 90 | 15.8 | 674 | 2289 | 2538 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 851 | 305 | 30 | 75.8 | 410 | 758 | 994 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 382 | 0 | 45 | 104.5 | 58 | 227 | 303 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 97 | 110 | 14 | 18.7 | 29 | 107 | 216 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 12 | 92 | 30 | 7.7 | 14 | 63 | 110 | 0 | — |
| ITEM-0063 | B - Core Products | Healthy | 362 | 0 | 14 | 60.4 | 35 | 125 | 251 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 457 | 160 | 60 | 91.8 | 207 | 511 | 616 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 273 | 790 | 60 | 21.0 | 266 | 1058 | 1331 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 26 | 367 | 45 | 4.4 | 93 | 367 | 493 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 301 | 245 | 14 | 18.1 | 122 | 372 | 604 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 201 | 0 | 30 | 49.6 | 45 | 171 | 256 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 88 | 0 | 7 | 33.3 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 289 | 0 | 45 | 117.2 | 71 | 185 | 259 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 29 | 0 | 7 | 46.6 | 3 | 8 | 27 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 694 | 510 | 60 | 58.6 | 244 | 967 | 1216 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3317 | 0 | 90 | 829.2 | 123 | 487 | 571 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 60 | 14 | 0.0 | 10 | 41 | 101 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Healthy | 39 | 28 | 45 | 42.3 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | C - Slow Moving | Healthy | 441 | 909 | 90 | 49.0 | 406 | 1225 | 1495 | 0 | — |
| ITEM-0077 | C - Slow Moving | Excess | 261 | 0 | 7 | 143.2 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 128 | 381 | 465 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 342 | 495 | 45 | 31.0 | 174 | 683 | 914 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 437 | 0 | 45 | 187.3 | 29 | 137 | 207 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 505 | 464 | 90 | 74.0 | 211 | 832 | 976 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 56 | 245 | 7 | 4.8 | 30 | 124 | 370 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 531 | 0 | 14 | 52.3 | 59 | 212 | 425 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 269 | 0 | 60 | 110.5 | 51 | 200 | 251 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 170 | 465 | 14 | 13.0 | 257 | 454 | 729 | 0 | — |
| ITEM-0086 | C - Slow Moving | Lead-time risk | 9 | 30 | 14 | 8.8 | 6 | 22 | 52 | 0 | 9 |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 217 | 137 | 45 | 47.4 | 57 | 268 | 405 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 899 | 0 | 14 | 52.0 | 349 | 609 | 972 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 30 | 45 | 30 | 20.8 | 13 | 58 | 102 | 0 | 21 |
| ITEM-0092 | B - Core Products | Healthy | 710 | 853 | 90 | 59.0 | 367 | 1463 | 1715 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 679 | 0 | 7 | 38.3 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 71 | 0 | 7 | 15.6 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6263 | 0 | 90 | 359.7 | 659 | 2244 | 2488 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3184 | 0 | 60 | 227.6 | 359 | 1213 | 1409 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 10 | 115 | 7 | 2.0 | 15 | 55 | 159 | 0 | 3 |
| ITEM-0100 | B - Core Products | Healthy | 26 | 65 | 14 | 8.8 | 17 | 62 | 124 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1046 | 675 | 60 | 80.9 | 605 | 1394 | 1575 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 126 | 0 | 45 | 66.3 | 24 | 112 | 169 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 970 | 267 | 90 | 183.4 | 276 | 758 | 869 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 319 | 160 | 45 | 45.4 | 113 | 437 | 585 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 894 | 1265 | 90 | 53.9 | 634 | 2144 | 2376 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 330 | 757 | 60 | 30.2 | 225 | 893 | 1123 | 0 | 31 |
| ITEM-0108 | C - Slow Moving | Excess | 469 | 0 | 30 | 299.4 | 46 | 95 | 142 | 0 | — |
| ITEM-0109 | B - Core Products | Healthy | 890 | 185 | 90 | 104.2 | 260 | 1038 | 1217 | 0 | — |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1106 | 890 | 90 | 75.2 | 560 | 1898 | 2104 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 376 | 1301 | 60 | 20.1 | 476 | 1615 | 1876 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 37 | 0 | 14 | 26.6 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 593 | 0 | 14 | 124.1 | 129 | 201 | 301 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 67 | 50 | 45 | 43.1 | 19 | 91 | 138 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 467 | 242 | 90 | 80.4 | 178 | 707 | 829 | 0 | — |
| ITEM-0119 | B - Core Products | Reorder | 122 | 125 | 30 | 20.4 | 65 | 251 | 376 | 130 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 38 | 58 | 30 | 20.7 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 278 | 0 | 7 | 23.8 | 30 | 124 | 369 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 110 | 762 | 45 | 10.1 | 390 | 893 | 1123 | 251 | 11 |
| ITEM-0123 | B - Core Products | Healthy | 63 | 222 | 14 | 13.9 | 121 | 189 | 285 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 183 | 209 | 14 | 19.0 | 57 | 202 | 405 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 123 | 0 | 7 | 19.5 | 17 | 68 | 200 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 748 | 0 | 30 | 125.4 | 305 | 490 | 574 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 308 | 374 | 45 | 35.4 | 137 | 538 | 720 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 191.5 | 542 | 1313 | 1491 | 0 | — |
| ITEM-0131 | B - Core Products | Healthy | 347 | 0 | 14 | 59.3 | 34 | 122 | 245 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 154 | 255 | 60 | 39.2 | 64 | 304 | 422 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3253 | 0 | 60 | 240.0 | 347 | 1174 | 1364 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Lead-time risk | 78 | 135 | 14 | 10.2 | 57 | 173 | 280 | 0 | 11 |
| ITEM-0139 | A - Top Movers | Healthy | 349 | 449 | 30 | 23.2 | 199 | 665 | 875 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 708 | 1087 | 60 | 38.7 | 467 | 1584 | 1840 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1794 | 0 | 45 | 182.0 | 155 | 609 | 816 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1259 | 315 | 60 | 109.6 | 569 | 1270 | 1512 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 432 | 229 | 45 | 40.9 | 166 | 652 | 874 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 324 | 0 | 7 | 26.9 | 33 | 130 | 382 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 747 | 0 | 60 | 162.4 | 95 | 376 | 473 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 23 | 636 | 90 | 8.0 | 89 | 352 | 413 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 921 | 0 | 14 | 69.8 | 283 | 481 | 759 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 58.4 | 232 | 401 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 481 | 0 | 60 | 127.0 | 80 | 312 | 391 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 551 | 400 | 90 | 130.8 | 304 | 688 | 776 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 158 | 0 | 60 | 117.5 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 267 | 0 | 14 | 35.7 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 341 | 514 | 30 | 18.9 | 239 | 800 | 1052 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 475 | 371 | 7 | 22.3 | 315 | 486 | 784 | 0 | — |
