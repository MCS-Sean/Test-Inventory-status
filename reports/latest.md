# Synthetic Inventory Health

**Simulation date: 2026-10-28**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 94 |
| Lead-time risk | 3 |
| Reorder | 3 |
| Stockout | 10 |

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
| ITEM-0001 | B - Core Products | Healthy | 330 | 291 | 30 | 25.1 | 139 | 547 | 822 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 313 | 0 | 7 | 50.4 | 91 | 141 | 272 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 504 | 890 | 60 | 32.2 | 400 | 1355 | 1574 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1873 | 0 | 45 | 453.1 | 66 | 257 | 343 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 126 | 155 | 14 | 17.9 | 41 | 147 | 295 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 111 | 0 | 45 | 70.9 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 190 | 0 | 14 | 33.1 | 34 | 121 | 241 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 202 | 0 | 60 | 156.7 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 74 | 410 | 90 | 38.7 | 60 | 234 | 275 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 2145 | 0 | 60 | 144.7 | 824 | 1729 | 1936 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 306 | 90 | 90 | 108.0 | 67 | 325 | 410 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 596 | 0 | 7 | 45.8 | 34 | 138 | 411 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 355 | 155 | 45 | 53.1 | 105 | 413 | 554 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1099 | 0 | 30 | 352.0 | 36 | 133 | 199 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2754 | 0 | 60 | 266.2 | 214 | 846 | 1063 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 151 | 0 | 14 | 25.8 | 35 | 123 | 246 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 552 | 0 | 60 | 577.7 | 18 | 77 | 105 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 593 | 2011 | 2229 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 30 | 0 | 30 | 52.9 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 411 | 1169 | 60 | 39.3 | 695 | 1334 | 1480 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 185 | 0 | 30 | 90.0 | 18 | 82 | 144 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 141 | 960 | 90 | 28.2 | 153 | 608 | 713 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1182 | 0 | 14 | 245.1 | 29 | 102 | 203 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 258 | 135 | 60 | 59.7 | 69 | 333 | 463 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 280 | 0 | 45 | 87.8 | 51 | 198 | 265 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 97 | 265 | 14 | 8.3 | 67 | 242 | 487 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 66 | 95 | 14 | 16.1 | 25 | 87 | 173 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 217 | 172 | 30 | 25.9 | 89 | 349 | 525 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 374 | 315 | 30 | 25.1 | 158 | 621 | 934 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4346 | 0 | 60 | 602.7 | 185 | 625 | 726 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 50.4 | 251 | 433 | 686 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 171 | 0 | 14 | 36.8 | 27 | 97 | 195 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 658 | 0 | 45 | 196.7 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 306 | 795 | 963 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 73 | 0 | 45 | 104.3 | 10 | 43 | 64 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 172 | 351 | 60 | 36.9 | 161 | 445 | 585 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 242 | 0 | 7 | 23.3 | 24 | 108 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 145 | 0 | 7 | 19.4 | 20 | 80 | 238 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4336 | 0 | 60 | 542.0 | 209 | 697 | 809 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 321 | 0 | 14 | 43.2 | 55 | 167 | 271 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 778 | 1680 | 90 | 42.7 | 688 | 2345 | 2599 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 514 | 0 | 45 | 141.5 | 58 | 226 | 302 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 34 | 110 | 14 | 6.9 | 28 | 102 | 206 | 0 | 7 |
| ITEM-0062 | C - Slow Moving | Healthy | 73 | 0 | 30 | 49.8 | 14 | 60 | 104 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 532 | 0 | 14 | 82.8 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 312 | 310 | 60 | 53.2 | 235 | 593 | 717 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 697 | 525 | 60 | 58.0 | 248 | 982 | 1234 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 215 | 246 | 45 | 38.5 | 88 | 346 | 463 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 306 | 245 | 14 | 18.9 | 118 | 362 | 589 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 349 | 0 | 30 | 82.2 | 47 | 179 | 268 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 80 | 0 | 7 | 28.8 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 20 | 0 | 7 | 27.3 | 3 | 9 | 31 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 230 | 907 | 1140 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3457 | 0 | 90 | 804.0 | 131 | 523 | 613 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 61 | 0 | 14 | 29.4 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 36 | 26 | 45 | 40.0 | 13 | 55 | 82 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 330 | 0 | 7 | 168.8 | 5 | 21 | 80 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 413 | 515 | 45 | 35.9 | 180 | 709 | 950 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 520 | 0 | 45 | 234.0 | 28 | 131 | 197 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 309 | 558 | 90 | 44.9 | 212 | 839 | 984 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 172 | 0 | 7 | 15.3 | 28 | 119 | 355 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 766 | 0 | 14 | 68.9 | 64 | 231 | 465 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 26 | 337 | 60 | 11.2 | 49 | 191 | 240 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 205 | 400 | 14 | 18.1 | 243 | 414 | 652 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 14 | 35 | 14 | 13.5 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 232 | 135 | 45 | 52.7 | 54 | 257 | 389 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 25 | 50 | 30 | 16.7 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 614 | 1027 | 90 | 48.8 | 383 | 1528 | 1792 | 0 | 84 |
| ITEM-0093 | B - Core Products | Healthy | 307 | 485 | 7 | 18.1 | 243 | 379 | 736 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 123 | 0 | 7 | 25.9 | 13 | 52 | 151 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6743 | 0 | 90 | 369.1 | 693 | 2356 | 2611 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3582 | 0 | 60 | 255.7 | 359 | 1214 | 1410 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 47.6 | 104 | 155 | 286 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 78 | 0 | 7 | 14.6 | 16 | 59 | 171 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 121 | 0 | 14 | 36.7 | 19 | 69 | 138 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 66.3 | 642 | 1428 | 1608 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 202 | 0 | 45 | 108.2 | 23 | 109 | 165 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 82.9 | 369 | 1091 | 1258 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 339 | 180 | 45 | 45.0 | 120 | 467 | 625 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 851 | 1542 | 90 | 50.1 | 645 | 2190 | 2428 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 397 | 499 | 60 | 35.9 | 227 | 903 | 1135 | 239 | 58 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1066 | 1250 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1548 | 445 | 90 | 110.6 | 537 | 1811 | 2007 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 339 | 1407 | 60 | 19.3 | 451 | 1524 | 1770 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 125.9 | 609 | 1145 | 1307 | 0 | — |
| ITEM-0114 | C - Slow Moving | Reorder | 29 | 0 | 14 | 20.2 | 7 | 29 | 72 | 45 | — |
| ITEM-0115 | B - Core Products | Healthy | 833 | 0 | 14 | 84.3 | 239 | 388 | 595 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 112 | 0 | 45 | 76.4 | 18 | 86 | 130 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 173 | 684 | 802 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 165 | 135 | 30 | 27.7 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 35 | 59 | 30 | 18.8 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 372 | 0 | 7 | 29.4 | 34 | 136 | 402 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 49 | 146 | 14 | 13.3 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 51 | 216 | 14 | 5.1 | 58 | 210 | 422 | 0 | — |
| ITEM-0125 | B - Core Products | Reorder | 55 | 0 | 7 | 9.4 | 16 | 63 | 187 | 132 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 540 | 191 | 45 | 60.1 | 141 | 555 | 744 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 955 | 1320 | 90 | 71.4 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 512 | 0 | 14 | 85.2 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 262 | 130 | 60 | 62.9 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 137 | 172 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3665 | 0 | 60 | 263.0 | 360 | 1210 | 1405 | 0 | — |
| ITEM-0136 | C - Slow Moving | Reorder | 66 | 0 | 45 | 63.2 | 29 | 78 | 109 | 43 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 371 | 0 | 14 | 47.6 | 58 | 175 | 285 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 299 | 474 | 30 | 19.4 | 203 | 681 | 896 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 998 | 799 | 60 | 54.3 | 468 | 1589 | 1846 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2105 | 0 | 45 | 212.9 | 156 | 611 | 819 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 81.8 | 630 | 1509 | 1811 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 271 | 470 | 45 | 25.1 | 170 | 666 | 893 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 668 | 0 | 7 | 54.0 | 37 | 137 | 396 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 97 | 383 | 481 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 126 | 636 | 90 | 39.1 | 99 | 393 | 460 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 36.7 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 629 | 0 | 60 | 165.0 | 81 | 314 | 394 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 799 | 400 | 90 | 248.0 | 263 | 557 | 624 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 204 | 0 | 60 | 142.3 | 24 | 112 | 155 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 483 | 0 | 14 | 65.3 | 43 | 154 | 310 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 637 | 274 | 30 | 36.3 | 231 | 775 | 1021 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 17.2 | 286 | 436 | 699 | 0 | — |
