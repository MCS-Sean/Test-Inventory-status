# Synthetic Inventory Health

**Simulation date: 2026-11-06**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 97 |
| Lead-time risk | 4 |
| Reorder | 4 |
| Stockout | 6 |

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
| ITEM-0001 | B - Core Products | Healthy | 219 | 593 | 30 | 16.6 | 139 | 548 | 824 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 384 | 1107 | 60 | 25.2 | 390 | 1318 | 1531 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1829 | 0 | 45 | 467.6 | 62 | 242 | 325 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 215 | 0 | 14 | 30.6 | 41 | 147 | 294 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 98 | 0 | 45 | 65.3 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 123 | 0 | 14 | 21.6 | 33 | 119 | 238 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 192 | 0 | 60 | 151.6 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 60 | 410 | 90 | 34.0 | 55 | 216 | 253 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 145.2 | 780 | 1618 | 1810 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 102.8 | 292 | 396 | 576 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 284 | 90 | 90 | 103.9 | 65 | 314 | 396 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 482 | 0 | 7 | 37.4 | 34 | 138 | 409 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 294 | 155 | 45 | 44.7 | 103 | 406 | 544 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1073 | 0 | 30 | 374.3 | 33 | 122 | 183 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2653 | 0 | 60 | 253.7 | 216 | 854 | 1074 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 100 | 120 | 14 | 18.3 | 32 | 114 | 229 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 543 | 0 | 60 | 603.3 | 17 | 72 | 99 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 579 | 1958 | 2170 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 24 | 20 | 30 | 41.5 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Reorder | 1000 | 452 | 60 | 84.2 | 735 | 1460 | 1626 | 174 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 171 | 0 | 30 | 89.5 | 17 | 77 | 134 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1054 | 0 | 90 | 217.6 | 147 | 588 | 690 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 44.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1133 | 0 | 14 | 245.7 | 27 | 97 | 193 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 228 | 135 | 60 | 53.3 | 69 | 330 | 459 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 257 | 0 | 45 | 87.9 | 47 | 182 | 243 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 255 | 0 | 14 | 22.1 | 66 | 239 | 481 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 41.4 | 100 | 148 | 272 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 125 | 0 | 14 | 32.5 | 23 | 81 | 162 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 148 | 355 | 30 | 17.7 | 89 | 349 | 524 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 590 | 315 | 30 | 39.4 | 158 | 623 | 938 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4281 | 0 | 60 | 612.5 | 179 | 606 | 704 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 61.2 | 221 | 371 | 579 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 131 | 0 | 14 | 28.3 | 27 | 97 | 194 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 629 | 0 | 45 | 190.6 | 40 | 192 | 291 | 0 | — |
| ITEM-0045 | C - Slow Moving | Reorder | 221 | 220 | 90 | 62.7 | 141 | 462 | 568 | 130 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 192 | 179 | 60 | 67.8 | 113 | 286 | 371 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 115 | 790 | 60 | 13.7 | 302 | 814 | 989 | 0 | 14 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 110.4 | 117 | 189 | 289 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 67 | 0 | 45 | 98.9 | 10 | 42 | 62 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 174 | 0 | 7 | 17.6 | 23 | 103 | 310 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 92 | 0 | 7 | 12.5 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4257 | 0 | 60 | 550.5 | 198 | 670 | 778 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 264 | 0 | 14 | 37.5 | 51 | 157 | 256 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 639 | 1950 | 90 | 35.4 | 683 | 2326 | 2578 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 476 | 0 | 45 | 133.5 | 57 | 222 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 107 | 0 | 14 | 21.6 | 29 | 104 | 208 | 0 | — |
| ITEM-0062 | C - Slow Moving | Reorder | 58 | 0 | 30 | 40.5 | 13 | 58 | 101 | 43 | — |
| ITEM-0063 | B - Core Products | Excess | 467 | 0 | 14 | 72.5 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 52.9 | 210 | 524 | 632 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 577 | 525 | 60 | 47.1 | 253 | 1001 | 1258 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 155 | 246 | 45 | 27.7 | 89 | 347 | 465 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 378 | 0 | 14 | 22.8 | 119 | 368 | 600 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 312 | 0 | 30 | 76.3 | 45 | 172 | 258 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 60 | 0 | 7 | 22.0 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 95.7 | 88 | 242 | 342 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 24.0 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 969 | 0 | 60 | 85.5 | 235 | 927 | 1165 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3428 | 0 | 90 | 869.1 | 120 | 479 | 562 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 46 | 0 | 14 | 23.3 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 27 | 54 | 45 | 30.4 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 415 | 964 | 1090 | 148 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 312 | 0 | 7 | 176.6 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 22.5 | 113 | 324 | 393 | 0 | 23 |
| ITEM-0079 | B - Core Products | Healthy | 298 | 515 | 45 | 26.7 | 175 | 688 | 922 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 494 | 0 | 45 | 219.0 | 28 | 132 | 200 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 242 | 705 | 90 | 34.6 | 216 | 852 | 999 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 44 | 250 | 7 | 3.7 | 29 | 124 | 371 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 678 | 0 | 14 | 61.0 | 65 | 232 | 466 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 339 | 0 | 60 | 151.0 | 47 | 184 | 232 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 501 | 0 | 14 | 47.6 | 223 | 381 | 603 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 38 | 0 | 14 | 38.9 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 203 | 135 | 45 | 47.7 | 53 | 249 | 377 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 859 | 0 | 14 | 47.1 | 365 | 639 | 1021 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 16 | 50 | 30 | 11.1 | 13 | 58 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 515 | 1027 | 90 | 41.1 | 381 | 1523 | 1786 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 32.9 | 256 | 402 | 784 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 80 | 0 | 7 | 17.2 | 12 | 50 | 147 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6572 | 0 | 90 | 363.8 | 684 | 2329 | 2581 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3483 | 0 | 60 | 259.1 | 346 | 1167 | 1355 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 41.7 | 89 | 130 | 236 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 32 | 115 | 7 | 6.3 | 15 | 56 | 163 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 95 | 0 | 14 | 30.2 | 18 | 66 | 132 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 41.3 | 711 | 1629 | 1840 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 184 | 0 | 45 | 101.6 | 23 | 107 | 161 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 76.8 | 352 | 1034 | 1191 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 273 | 340 | 45 | 36.6 | 119 | 462 | 619 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 671 | 1542 | 90 | 39.3 | 650 | 2203 | 2441 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 547 | 498 | 60 | 50.3 | 223 | 886 | 1115 | 0 | 51 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 265 | 1055 | 1237 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1412 | 665 | 90 | 97.2 | 555 | 1877 | 2080 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 176 | 1407 | 60 | 10.2 | 444 | 1500 | 1742 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 17 | 45 | 14 | 11.9 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 128.3 | 182 | 276 | 407 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 98 | 0 | 45 | 65.8 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 177 | 700 | 821 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 119 | 135 | 30 | 20.2 | 63 | 246 | 370 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 76 | 0 | 30 | 40.2 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 271 | 0 | 7 | 22.3 | 33 | 131 | 386 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 45 | 238 | 45 | 8.0 | 260 | 518 | 636 | 353 | 9 |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 182 | 211 | 14 | 18.5 | 57 | 205 | 412 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 122 | 0 | 7 | 20.4 | 17 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 214.3 | 278 | 414 | 475 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 462 | 191 | 45 | 52.0 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 458 | 0 | 14 | 74.9 | 35 | 127 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 238 | 130 | 60 | 59.0 | 65 | 312 | 433 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3547 | 0 | 60 | 257.7 | 355 | 1195 | 1388 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 292 | 0 | 14 | 39.1 | 54 | 166 | 271 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 448 | 245 | 30 | 29.9 | 200 | 665 | 874 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 782 | 1068 | 60 | 41.5 | 480 | 1631 | 1895 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2005 | 0 | 45 | 204.8 | 155 | 606 | 811 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 86.3 | 619 | 1452 | 1738 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 415 | 463 | 45 | 38.8 | 169 | 662 | 886 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 543 | 0 | 7 | 43.4 | 38 | 139 | 401 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 877 | 0 | 60 | 197.8 | 92 | 363 | 456 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 97 | 636 | 90 | 31.6 | 95 | 375 | 439 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 60.0 | 430 | 698 | 948 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 594 | 0 | 60 | 163.0 | 76 | 299 | 375 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 193 | 0 | 60 | 142.4 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 425 | 0 | 14 | 59.2 | 42 | 150 | 301 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Reorder | 479 | 274 | 30 | 27.6 | 230 | 769 | 1012 | 259 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 314 | 498 | 7 | 14.3 | 321 | 497 | 805 | 0 | — |
