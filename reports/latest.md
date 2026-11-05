# Synthetic Inventory Health

**Simulation date: 2026-11-05**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 97 |
| Lead-time risk | 4 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Lead-time risk | 234 | 291 | 30 | 17.7 | 140 | 550 | 827 | 302 | 40 |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 396 | 1107 | 60 | 25.9 | 392 | 1326 | 1540 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1833 | 0 | 45 | 467.3 | 62 | 243 | 325 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 216 | 0 | 14 | 30.5 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 100 | 0 | 45 | 66.7 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 130 | 0 | 14 | 22.9 | 33 | 118 | 237 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 194 | 0 | 60 | 153.2 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 62 | 410 | 90 | 34.7 | 56 | 219 | 257 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 145.2 | 780 | 1618 | 1810 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 102.8 | 292 | 396 | 576 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 287 | 90 | 90 | 104.2 | 66 | 317 | 400 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 490 | 0 | 7 | 37.4 | 34 | 139 | 414 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 305 | 155 | 45 | 46.4 | 103 | 406 | 544 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1077 | 0 | 30 | 377.2 | 32 | 121 | 181 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2664 | 0 | 60 | 254.5 | 216 | 855 | 1075 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 109 | 120 | 14 | 20.0 | 32 | 114 | 229 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 544 | 0 | 60 | 604.4 | 17 | 72 | 99 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 587 | 1989 | 2204 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 24 | 20 | 30 | 40.0 | 7 | 26 | 44 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 1128 | 452 | 60 | 107.9 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 172 | 0 | 30 | 88.0 | 17 | 78 | 137 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1059 | 0 | 90 | 217.1 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 44.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1138 | 0 | 14 | 246.8 | 27 | 97 | 193 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 231 | 135 | 60 | 53.7 | 69 | 332 | 461 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 259 | 0 | 45 | 88.0 | 47 | 183 | 245 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 271 | 0 | 14 | 23.4 | 66 | 240 | 483 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 41.4 | 100 | 148 | 272 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 127 | 0 | 14 | 32.7 | 23 | 82 | 163 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 158 | 355 | 30 | 19.1 | 89 | 346 | 519 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 605 | 315 | 30 | 40.6 | 158 | 620 | 933 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4290 | 0 | 60 | 613.8 | 179 | 606 | 704 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 61.2 | 221 | 371 | 579 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 137 | 0 | 14 | 29.6 | 27 | 97 | 194 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 633 | 0 | 45 | 191.2 | 41 | 194 | 293 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 257 | 220 | 90 | 82.3 | 129 | 414 | 507 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 175 | 790 | 60 | 22.7 | 286 | 757 | 919 | 0 | 23 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 110.4 | 117 | 189 | 289 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 68 | 0 | 45 | 98.7 | 10 | 42 | 63 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 176 | 0 | 7 | 17.7 | 22 | 102 | 311 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 93 | 0 | 7 | 12.5 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4267 | 0 | 60 | 548.6 | 199 | 674 | 783 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 270 | 0 | 14 | 38.3 | 51 | 157 | 256 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 655 | 1950 | 90 | 36.4 | 681 | 2317 | 2569 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 481 | 0 | 45 | 135.3 | 57 | 221 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Stockout | 0 | 110 | 14 | 0.0 | 29 | 104 | 208 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 60 | 0 | 30 | 42.2 | 13 | 58 | 100 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 473 | 0 | 14 | 72.6 | 37 | 135 | 272 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 45.8 | 235 | 597 | 722 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 591 | 525 | 60 | 48.5 | 251 | 994 | 1250 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 162 | 246 | 45 | 28.9 | 89 | 347 | 465 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 391 | 0 | 14 | 23.7 | 119 | 367 | 598 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 315 | 0 | 30 | 76.6 | 45 | 173 | 259 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 66 | 0 | 7 | 24.5 | 6 | 28 | 109 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 352 | 0 | 45 | 118.7 | 81 | 218 | 307 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 24.0 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 977 | 0 | 60 | 85.7 | 236 | 932 | 1171 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3434 | 0 | 90 | 868.1 | 121 | 481 | 565 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 48 | 0 | 14 | 24.3 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Reorder | 28 | 26 | 45 | 31.1 | 13 | 55 | 82 | 28 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 314 | 0 | 7 | 176.6 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 21.2 | 115 | 339 | 413 | 0 | 22 |
| ITEM-0079 | B - Core Products | Healthy | 318 | 515 | 45 | 28.4 | 176 | 691 | 926 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 498 | 0 | 45 | 223.0 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 258 | 705 | 90 | 37.6 | 212 | 837 | 982 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 53 | 250 | 7 | 4.5 | 29 | 124 | 372 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 689 | 0 | 14 | 61.7 | 65 | 233 | 467 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 343 | 0 | 60 | 154.3 | 47 | 183 | 230 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 501 | 0 | 14 | 40.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 40 | 0 | 14 | 40.9 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 204 | 135 | 45 | 47.4 | 53 | 251 | 380 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 859 | 0 | 14 | 47.1 | 365 | 639 | 1021 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 17 | 50 | 30 | 11.6 | 13 | 59 | 103 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 524 | 1027 | 90 | 41.6 | 383 | 1531 | 1796 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 598 | 0 | 7 | 32.9 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 84 | 0 | 7 | 18.0 | 12 | 50 | 148 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6589 | 0 | 90 | 362.9 | 688 | 2341 | 2595 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3483 | 0 | 60 | 255.9 | 349 | 1180 | 1370 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 41.7 | 89 | 130 | 236 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 40 | 115 | 7 | 8.0 | 15 | 56 | 161 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 98 | 0 | 14 | 31.5 | 18 | 65 | 130 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 41.3 | 711 | 1629 | 1840 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 186 | 0 | 45 | 103.3 | 23 | 106 | 160 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 74.4 | 357 | 1061 | 1224 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 282 | 340 | 45 | 37.9 | 118 | 460 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 694 | 1542 | 90 | 40.6 | 652 | 2208 | 2447 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 558 | 498 | 60 | 51.5 | 222 | 883 | 1111 | 0 | 52 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 264 | 1048 | 1229 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Reorder | 1427 | 445 | 90 | 97.8 | 558 | 1886 | 2090 | 220 | — |
| ITEM-0112 | A - Top Movers | Healthy | 197 | 1407 | 60 | 11.4 | 445 | 1503 | 1745 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 19 | 45 | 14 | 13.4 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 833 | 0 | 14 | 141.5 | 181 | 270 | 393 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 99 | 0 | 45 | 66.5 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 177 | 699 | 820 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 124 | 135 | 30 | 20.8 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 79 | 0 | 30 | 42.1 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 292 | 0 | 7 | 24.0 | 33 | 131 | 386 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 189 | 211 | 14 | 19.2 | 57 | 205 | 413 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 130 | 0 | 7 | 21.7 | 17 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 214.3 | 278 | 414 | 475 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 472 | 191 | 45 | 53.0 | 139 | 549 | 737 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 462 | 0 | 14 | 75.6 | 35 | 127 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 241 | 130 | 60 | 59.9 | 65 | 311 | 432 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3554 | 0 | 60 | 257.1 | 356 | 1200 | 1393 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 302 | 0 | 14 | 40.9 | 54 | 165 | 268 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 454 | 245 | 30 | 30.2 | 200 | 667 | 877 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 807 | 1068 | 60 | 42.7 | 481 | 1634 | 1898 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2020 | 0 | 45 | 207.8 | 154 | 602 | 806 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 86.3 | 619 | 1452 | 1738 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 423 | 463 | 45 | 39.3 | 170 | 666 | 892 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 543 | 0 | 7 | 42.9 | 38 | 140 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 884 | 0 | 60 | 200.9 | 91 | 360 | 452 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 102 | 636 | 90 | 33.1 | 95 | 376 | 440 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 60.0 | 430 | 698 | 948 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 599 | 0 | 60 | 164.4 | 76 | 299 | 375 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 194 | 0 | 60 | 142.0 | 23 | 107 | 148 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 436 | 0 | 14 | 60.8 | 42 | 150 | 300 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 498 | 274 | 30 | 28.6 | 230 | 770 | 1013 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 314 | 498 | 7 | 14.3 | 321 | 497 | 805 | 0 | — |
