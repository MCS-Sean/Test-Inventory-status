# Synthetic Inventory Health

**Simulation date: 2026-10-27**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 92 |
| Lead-time risk | 3 |
| Reorder | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 336 | 291 | 30 | 25.5 | 139 | 548 | 825 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 313 | 0 | 7 | 50.4 | 91 | 141 | 272 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 511 | 890 | 60 | 32.2 | 405 | 1373 | 1595 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1874 | 0 | 45 | 445.0 | 67 | 261 | 350 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 133 | 155 | 14 | 19.0 | 41 | 146 | 293 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 112 | 0 | 45 | 72.0 | 20 | 92 | 139 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 193 | 0 | 14 | 33.0 | 34 | 122 | 245 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 203 | 0 | 60 | 154.8 | 22 | 102 | 142 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 75 | 410 | 90 | 39.0 | 60 | 235 | 276 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 2145 | 0 | 60 | 131.1 | 866 | 1865 | 2094 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 309 | 90 | 90 | 109.5 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 610 | 0 | 7 | 47.0 | 34 | 138 | 411 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 359 | 155 | 45 | 53.2 | 105 | 416 | 557 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1104 | 0 | 30 | 356.1 | 36 | 133 | 198 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2765 | 0 | 60 | 268.7 | 213 | 841 | 1057 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 160 | 0 | 14 | 27.2 | 35 | 124 | 247 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 553 | 0 | 60 | 585.5 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 593 | 2009 | 2227 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 31 | 0 | 30 | 55.8 | 7 | 25 | 41 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 500 | 1169 | 60 | 50.8 | 545 | 1146 | 1353 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 187 | 0 | 30 | 90.5 | 18 | 83 | 145 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 147 | 960 | 90 | 29.3 | 153 | 610 | 715 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1187 | 0 | 14 | 246.2 | 29 | 102 | 203 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 264 | 135 | 60 | 61.2 | 69 | 332 | 462 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 282 | 0 | 45 | 88.4 | 51 | 198 | 265 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 97 | 265 | 14 | 8.2 | 67 | 245 | 494 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 72 | 95 | 14 | 17.5 | 25 | 87 | 174 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 226 | 172 | 30 | 27.1 | 89 | 348 | 523 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 394 | 315 | 30 | 26.5 | 157 | 618 | 931 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4359 | 0 | 60 | 607.3 | 184 | 622 | 723 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 710 | 0 | 14 | 64.8 | 242 | 407 | 637 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 173 | 0 | 14 | 37.1 | 28 | 98 | 196 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 662 | 0 | 45 | 200.6 | 41 | 193 | 292 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 306 | 795 | 963 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 73 | 0 | 45 | 102.7 | 11 | 44 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 201 | 351 | 60 | 46.4 | 157 | 422 | 552 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 251 | 0 | 7 | 24.2 | 24 | 107 | 325 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 151 | 0 | 7 | 20.1 | 20 | 81 | 239 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4340 | 0 | 60 | 535.1 | 212 | 707 | 821 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 333 | 0 | 14 | 44.7 | 55 | 167 | 272 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 786 | 1680 | 90 | 43.2 | 688 | 2345 | 2599 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 516 | 0 | 45 | 142.0 | 58 | 226 | 302 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 41 | 110 | 14 | 8.3 | 28 | 102 | 205 | 0 | 9 |
| ITEM-0062 | C - Slow Moving | Healthy | 75 | 0 | 30 | 50.8 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 540 | 0 | 14 | 84.7 | 37 | 133 | 267 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 312 | 310 | 60 | 53.2 | 235 | 593 | 717 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 711 | 525 | 60 | 59.2 | 248 | 981 | 1233 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 219 | 246 | 45 | 39.3 | 88 | 345 | 462 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 320 | 245 | 14 | 19.8 | 118 | 361 | 587 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 353 | 0 | 30 | 81.9 | 48 | 182 | 273 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 83 | 0 | 7 | 30.2 | 7 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 30.0 | 3 | 9 | 31 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 227 | 894 | 1123 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3459 | 0 | 90 | 796.2 | 133 | 529 | 620 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 63 | 0 | 14 | 30.2 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 36 | 26 | 45 | 39.0 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 332 | 0 | 7 | 168.8 | 5 | 21 | 80 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Reorder | 430 | 265 | 45 | 37.6 | 179 | 705 | 945 | 250 | — |
| ITEM-0080 | C - Slow Moving | Excess | 522 | 0 | 45 | 236.1 | 27 | 129 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 314 | 558 | 90 | 45.3 | 213 | 844 | 990 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 179 | 0 | 7 | 15.9 | 28 | 119 | 355 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 779 | 0 | 14 | 70.5 | 64 | 230 | 462 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 27 | 337 | 60 | 11.5 | 49 | 193 | 242 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 205 | 400 | 14 | 18.1 | 243 | 414 | 652 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 15 | 35 | 14 | 14.4 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 243 | 135 | 45 | 56.2 | 53 | 252 | 382 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 391 | 468 | 14 | 19.7 | 468 | 767 | 1045 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 28 | 50 | 30 | 18.8 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 626 | 1027 | 90 | 49.9 | 382 | 1524 | 1787 | 0 | 85 |
| ITEM-0093 | B - Core Products | Healthy | 307 | 485 | 7 | 17.3 | 245 | 388 | 761 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 28 | 104 | 7 | 5.8 | 14 | 53 | 154 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6767 | 0 | 90 | 375.2 | 685 | 2327 | 2579 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3586 | 0 | 60 | 254.5 | 361 | 1221 | 1418 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 47.6 | 104 | 155 | 286 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 83 | 0 | 7 | 15.4 | 16 | 60 | 172 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 125 | 0 | 14 | 37.8 | 20 | 70 | 140 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 66.3 | 642 | 1428 | 1608 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 205 | 0 | 45 | 109.8 | 23 | 109 | 165 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 354 | 180 | 45 | 47.9 | 117 | 457 | 613 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 870 | 1542 | 90 | 51.3 | 644 | 2186 | 2424 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 417 | 499 | 60 | 38.4 | 223 | 886 | 1114 | 0 | 61 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 264 | 1051 | 1233 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Reorder | 1561 | 220 | 90 | 111.6 | 537 | 1810 | 2006 | 225 | — |
| ITEM-0112 | A - Top Movers | Reorder | 353 | 1161 | 60 | 20.2 | 449 | 1516 | 1760 | 246 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 125.9 | 609 | 1145 | 1307 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 30 | 0 | 14 | 20.9 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 833 | 0 | 14 | 79.4 | 241 | 399 | 619 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 113 | 0 | 45 | 77.6 | 18 | 85 | 129 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 680 | 797 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 169 | 135 | 30 | 28.3 | 64 | 250 | 375 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 37 | 59 | 30 | 19.8 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 93 | 285 | 7 | 7.3 | 34 | 137 | 404 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 49 | 146 | 14 | 13.3 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 67 | 216 | 14 | 6.6 | 59 | 211 | 423 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 68 | 0 | 7 | 11.8 | 16 | 63 | 184 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Reorder | 550 | 0 | 45 | 61.4 | 140 | 552 | 741 | 191 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 955 | 1320 | 90 | 67.8 | 740 | 2022 | 2317 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 515 | 0 | 14 | 85.7 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 268 | 130 | 60 | 64.3 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 137 | 172 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3691 | 0 | 60 | 266.4 | 357 | 1203 | 1397 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 76 | 0 | 45 | 81.4 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 380 | 0 | 14 | 48.8 | 58 | 175 | 284 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 318 | 474 | 30 | 20.7 | 203 | 681 | 896 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1018 | 799 | 60 | 55.2 | 471 | 1597 | 1856 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2114 | 0 | 45 | 212.8 | 157 | 614 | 823 | 0 | — |
| ITEM-0142 | B - Core Products | Reorder | 1178 | 320 | 60 | 81.8 | 630 | 1509 | 1811 | 315 | — |
| ITEM-0143 | B - Core Products | Healthy | 283 | 470 | 45 | 26.2 | 171 | 669 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 684 | 0 | 7 | 55.3 | 37 | 136 | 396 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 99 | 388 | 488 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 129 | 636 | 90 | 39.6 | 101 | 398 | 466 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 16.4 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 633 | 0 | 60 | 165.1 | 81 | 315 | 396 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 205 | 0 | 60 | 141.9 | 24 | 113 | 156 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 488 | 0 | 14 | 65.5 | 43 | 155 | 312 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 654 | 274 | 30 | 37.5 | 230 | 772 | 1016 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 15.6 | 300 | 465 | 753 | 0 | — |
