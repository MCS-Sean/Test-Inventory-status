# Synthetic Inventory Health

**Simulation date: 2026-09-14**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 65 |
| Lead-time risk | 18 |
| Reorder | 3 |
| Stockout | 24 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 497 | 747 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 268 | 0 | 7 | 47.6 | 84 | 130 | 248 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 937 | 517 | 60 | 61.1 | 391 | 1327 | 1541 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2023 | 0 | 45 | 309.1 | 105 | 407 | 544 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 275 | 0 | 14 | 36.8 | 43 | 155 | 312 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 142 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 271 | 0 | 14 | 31.4 | 54 | 184 | 365 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 59 | 198 | 60 | 27.5 | 36 | 167 | 232 | 0 | 28 |
| ITEM-0010 | B - Core Products | Lead-time risk | 146 | 410 | 90 | 45.3 | 101 | 395 | 462 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 424 | 0 | 90 | 152.6 | 66 | 319 | 403 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1196 | 0 | 7 | 94.4 | 32 | 134 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 42 | 235 | 45 | 14.1 | 84 | 221 | 311 | 0 | 15 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 412 | 553 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1213 | 0 | 30 | 239.4 | 58 | 216 | 322 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3189 | 0 | 60 | 305.3 | 216 | 854 | 1073 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 357 | 0 | 14 | 37.5 | 57 | 200 | 400 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 589 | 0 | 60 | 417.4 | 24 | 111 | 153 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 642 | 2182 | 2419 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 10 | 45 | 30 | 14.3 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1021 | 717 | 60 | 99.9 | 701 | 1325 | 1468 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 129 | 225 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 331 | 960 | 90 | 41.7 | 247 | 970 | 1137 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1351 | 0 | 14 | 172.5 | 47 | 165 | 329 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 312 | 434 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 403 | 0 | 45 | 76.0 | 88 | 332 | 444 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 272.0 | 82 | 238 | 315 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 371 | 0 | 14 | 34.3 | 62 | 225 | 452 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 13.3 | 141 | 222 | 434 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 214 | 0 | 14 | 31.3 | 42 | 145 | 288 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 87 | 340 | 510 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 148 | 573 | 861 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4627 | 0 | 60 | 389.6 | 310 | 1035 | 1201 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 46.1 | 262 | 461 | 740 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 240 | 0 | 14 | 30.9 | 49 | 166 | 329 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 559 | 1484 | 1697 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 800 | 0 | 45 | 236.1 | 42 | 198 | 300 | 0 | — |
| ITEM-0045 | C - Slow Moving | Reorder | 390 | 0 | 90 | 125.8 | 129 | 412 | 505 | 115 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 58 | 145 | 188 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 25 | 80 | 45 | 23.7 | 15 | 64 | 96 | 0 | 24 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 129 | 290 | 369 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 245 | 0 | 7 | 24.7 | 27 | 107 | 315 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 171 | 0 | 7 | 23.3 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4633 | 0 | 60 | 370.6 | 329 | 1092 | 1267 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 595 | 0 | 14 | 50.6 | 93 | 270 | 434 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1549 | 865 | 90 | 86.5 | 678 | 2307 | 2558 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 899 | 1213 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 94 | 356 | 475 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 29 | 102 | 205 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 128 | 0 | 30 | 53.1 | 21 | 96 | 169 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 800 | 0 | 14 | 119.8 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1237 | 0 | 60 | 103.1 | 247 | 979 | 1231 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 463 | 0 | 45 | 80.0 | 90 | 357 | 478 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 516 | 0 | 14 | 30.1 | 123 | 381 | 621 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 126 | 390 | 30 | 17.6 | 81 | 304 | 454 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 21 | 90 | 7 | 7.5 | 7 | 30 | 114 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 105 | 104 | 45 | 38.4 | 77 | 203 | 285 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 26.8 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 234 | 921 | 1157 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3618 | 0 | 90 | 540.9 | 207 | 816 | 957 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 86 | 0 | 14 | 39.9 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 52 | 78 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 393 | 0 | 7 | 126.3 | 8 | 33 | 127 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 609 | 275 | 45 | 48.5 | 197 | 775 | 1039 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 612 | 0 | 45 | 251.5 | 30 | 142 | 215 | 0 | — |
| ITEM-0081 | B - Core Products | Reorder | 605 | 235 | 90 | 86.4 | 214 | 851 | 998 | 158 | — |
| ITEM-0082 | B - Core Products | Healthy | 181 | 0 | 7 | 16.6 | 29 | 117 | 347 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1268 | 0 | 14 | 120.3 | 62 | 221 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 118 | 337 | 60 | 31.3 | 80 | 310 | 389 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 50 | 0 | 14 | 30.4 | 9 | 34 | 83 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 273 | 367 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 89 | 0 | 30 | 58.9 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1142 | 735 | 90 | 83.1 | 420 | 1671 | 1960 | 0 | 115 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 199 | 0 | 7 | 27.8 | 22 | 80 | 230 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7531 | 0 | 90 | 421.0 | 679 | 2307 | 2558 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4236 | 0 | 60 | 324.7 | 337 | 1133 | 1316 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 269 | 0 | 7 | 29.5 | 30 | 104 | 295 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 246 | 0 | 14 | 46.2 | 34 | 114 | 226 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 61 | 210 | 45 | 21.9 | 35 | 164 | 247 | 0 | 22 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 115.5 | 390 | 1145 | 1319 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 652 | 0 | 45 | 81.5 | 125 | 493 | 661 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1534 | 773 | 90 | 88.5 | 659 | 2237 | 2479 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 628 | 481 | 60 | 56.0 | 231 | 916 | 1152 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 181.9 | 66 | 162 | 255 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 220 | 915 | 90 | 24.5 | 274 | 1090 | 1279 | 0 | 25 |
| ITEM-0110 | C - Slow Moving | Excess | 702 | 0 | 60 | 245.8 | 104 | 279 | 364 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2226 | 0 | 90 | 149.0 | 568 | 1928 | 2138 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1119 | 622 | 60 | 63.1 | 455 | 1537 | 1785 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 26.0 | 897 | 1815 | 2095 | 0 | 27 |
| ITEM-0114 | C - Slow Moving | Healthy | 43 | 0 | 14 | 29.8 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 67.1 | 274 | 499 | 813 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 123 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 139 | 530 | 90 | 26.1 | 164 | 649 | 761 | 0 | 27 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 66 | 259 | 390 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 61 | 55 | 30 | 32.5 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 292 | 0 | 7 | 21.9 | 36 | 143 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 63.6 | 94 | 139 | 202 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 270 | 0 | 14 | 26.9 | 58 | 209 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Reorder | 63 | 0 | 7 | 10.2 | 17 | 67 | 197 | 134 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 555 | 744 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 776 | 0 | 14 | 125.8 | 34 | 127 | 256 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 440 | 0 | 60 | 99.2 | 72 | 343 | 476 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4285 | 0 | 60 | 316.9 | 347 | 1172 | 1362 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 1.0 | 26 | 72 | 102 | 0 | 2 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 674 | 0 | 14 | 57.2 | 91 | 268 | 433 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 12 | 787 | 30 | 0.8 | 201 | 676 | 890 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1754 | 0 | 60 | 96.1 | 466 | 1579 | 1835 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2551 | 0 | 45 | 262.1 | 153 | 601 | 806 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 589 | 1407 | 1688 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 480 | 243 | 45 | 43.9 | 170 | 673 | 902 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1179 | 0 | 7 | 89.4 | 39 | 145 | 422 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 161 | 624 | 784 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 237 | 636 | 90 | 44.1 | 166 | 656 | 769 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Healthy | 802 | 0 | 14 | 37.6 | 444 | 765 | 1063 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 137.8 | 230 | 395 | 625 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 590 | 178 | 60 | 94.7 | 132 | 513 | 644 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 58 | 200 | 60 | 26.6 | 36 | 169 | 235 | 0 | 27 |
| ITEM-0155 | B - Core Products | Excess | 831 | 0 | 14 | 122.4 | 40 | 142 | 285 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 245 | 819 | 1077 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 597 | 0 | 7 | 24.0 | 324 | 524 | 872 | 0 | — |
