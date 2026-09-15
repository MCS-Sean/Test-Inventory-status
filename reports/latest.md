# Synthetic Inventory Health

**Simulation date: 2026-09-15**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 68 |
| Lead-time risk | 17 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 496 | 745 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 268 | 0 | 7 | 47.6 | 84 | 130 | 248 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 915 | 517 | 60 | 59.4 | 392 | 1332 | 1547 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2020 | 0 | 45 | 314.0 | 104 | 400 | 536 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 271 | 0 | 14 | 36.2 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 267 | 0 | 14 | 31.5 | 53 | 181 | 359 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 58 | 198 | 60 | 27.5 | 36 | 165 | 229 | 0 | 28 |
| ITEM-0010 | B - Core Products | Lead-time risk | 144 | 410 | 90 | 45.3 | 99 | 389 | 455 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 420 | 0 | 90 | 151.2 | 66 | 319 | 403 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1180 | 0 | 7 | 93.1 | 33 | 135 | 401 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 172.8 | 23 | 37 | 86 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 35 | 235 | 45 | 11.5 | 85 | 226 | 318 | 0 | 12 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 413 | 554 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1210 | 0 | 30 | 239.9 | 58 | 215 | 321 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3179 | 0 | 60 | 301.5 | 217 | 861 | 1082 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 357 | 0 | 14 | 38.1 | 56 | 197 | 394 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 587 | 0 | 60 | 416.0 | 24 | 111 | 153 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 640 | 2174 | 2410 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 9 | 45 | 30 | 12.7 | 8 | 31 | 52 | 0 | — |
| ITEM-0027 | A - Top Movers | Reorder | 816 | 717 | 60 | 65.3 | 793 | 1556 | 1731 | 198 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 128 | 224 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 325 | 960 | 90 | 40.7 | 248 | 974 | 1142 | 0 | 41 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1350 | 0 | 14 | 175.8 | 46 | 162 | 323 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 312 | 434 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 398 | 0 | 45 | 74.3 | 88 | 335 | 447 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 290.9 | 79 | 225 | 297 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 354 | 0 | 14 | 32.8 | 62 | 224 | 451 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 13.3 | 141 | 222 | 434 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 213 | 0 | 14 | 32.1 | 40 | 140 | 280 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 86 | 337 | 507 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 150 | 579 | 869 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4622 | 0 | 60 | 397.7 | 303 | 1012 | 1175 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 46.1 | 262 | 461 | 740 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 233 | 0 | 14 | 30.3 | 49 | 165 | 326 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 795 | 0 | 45 | 234.6 | 42 | 198 | 300 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 58 | 145 | 188 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 25 | 80 | 45 | 23.9 | 15 | 64 | 95 | 0 | 24 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 129 | 290 | 369 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 236 | 0 | 7 | 23.6 | 27 | 108 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 167 | 0 | 7 | 23.1 | 20 | 78 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4628 | 0 | 60 | 373.9 | 326 | 1082 | 1255 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 592 | 0 | 14 | 51.6 | 91 | 264 | 424 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1533 | 865 | 90 | 86.0 | 675 | 2297 | 2547 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 478 | 1011 | 1372 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 93 | 350 | 466 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 137 | 0 | 14 | 27.8 | 29 | 103 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 128 | 0 | 30 | 54.3 | 21 | 95 | 165 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 793 | 0 | 14 | 118.9 | 38 | 138 | 278 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1236 | 0 | 60 | 104.2 | 245 | 969 | 1219 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 457 | 0 | 45 | 79.6 | 89 | 354 | 474 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 497 | 0 | 14 | 29.0 | 123 | 381 | 621 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 124 | 390 | 30 | 17.6 | 80 | 299 | 447 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 18 | 90 | 7 | 6.4 | 7 | 30 | 114 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 105 | 104 | 45 | 38.4 | 77 | 203 | 285 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 26.8 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 236 | 931 | 1169 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3614 | 0 | 90 | 543.0 | 207 | 813 | 953 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 84 | 0 | 14 | 38.8 | 10 | 43 | 108 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 392 | 0 | 7 | 126.5 | 8 | 33 | 126 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 597 | 275 | 45 | 47.4 | 197 | 777 | 1041 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 610 | 0 | 45 | 248.4 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 594 | 393 | 90 | 84.2 | 215 | 858 | 1006 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 166 | 0 | 7 | 15.1 | 29 | 118 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1255 | 0 | 14 | 119.0 | 62 | 221 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 116 | 337 | 60 | 31.2 | 79 | 307 | 385 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 49 | 0 | 14 | 30.0 | 9 | 34 | 83 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 86 | 0 | 30 | 56.1 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1133 | 735 | 90 | 83.1 | 417 | 1658 | 1944 | 0 | 116 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 198 | 0 | 7 | 27.8 | 22 | 79 | 229 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7522 | 0 | 90 | 420.5 | 679 | 2307 | 2558 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4214 | 0 | 60 | 321.7 | 338 | 1138 | 1321 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 263 | 0 | 7 | 28.9 | 30 | 103 | 294 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 245 | 0 | 14 | 46.2 | 34 | 114 | 225 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 60 | 210 | 45 | 21.8 | 35 | 162 | 245 | 0 | 22 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 898 | 422 | 90 | 100.4 | 411 | 1225 | 1413 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 647 | 0 | 45 | 81.4 | 124 | 490 | 657 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1519 | 773 | 90 | 87.9 | 657 | 2230 | 2472 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 628 | 481 | 60 | 56.7 | 228 | 904 | 1136 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 181.9 | 66 | 162 | 255 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 212 | 915 | 90 | 23.8 | 273 | 1085 | 1273 | 0 | 24 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2221 | 0 | 90 | 148.7 | 567 | 1926 | 2135 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1093 | 622 | 60 | 61.3 | 458 | 1547 | 1797 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 29.6 | 829 | 1635 | 1880 | 0 | 30 |
| ITEM-0114 | C - Slow Moving | Healthy | 42 | 0 | 14 | 29.3 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 67.1 | 274 | 499 | 813 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 83 | 125 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 132 | 530 | 90 | 24.6 | 165 | 654 | 767 | 0 | 25 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 66 | 258 | 388 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 60 | 55 | 30 | 32.5 | 16 | 74 | 129 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 278 | 0 | 7 | 21.0 | 36 | 142 | 420 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 63.6 | 94 | 139 | 202 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 263 | 0 | 14 | 26.2 | 58 | 209 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 56 | 134 | 7 | 9.0 | 17 | 67 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 550 | 737 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 771 | 0 | 14 | 125.7 | 34 | 126 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 437 | 0 | 60 | 98.3 | 72 | 344 | 477 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 110 | 139 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4270 | 0 | 60 | 315.3 | 348 | 1175 | 1364 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 1.0 | 26 | 71 | 100 | 0 | 2 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 669 | 0 | 14 | 57.1 | 90 | 266 | 430 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 199 | 669 | 881 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1732 | 0 | 60 | 93.9 | 470 | 1596 | 1854 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2541 | 0 | 45 | 261.4 | 153 | 601 | 805 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 589 | 1407 | 1688 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 466 | 243 | 45 | 42.5 | 171 | 675 | 906 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1166 | 0 | 7 | 88.9 | 38 | 143 | 419 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 156 | 607 | 761 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 234 | 636 | 90 | 43.7 | 166 | 654 | 766 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 802 | 0 | 14 | 37.6 | 444 | 765 | 1063 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 137.8 | 230 | 395 | 625 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 589 | 178 | 60 | 95.9 | 131 | 506 | 635 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 58 | 200 | 60 | 27.3 | 36 | 166 | 230 | 0 | 28 |
| ITEM-0155 | B - Core Products | Excess | 821 | 0 | 14 | 120.5 | 40 | 143 | 286 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 244 | 812 | 1068 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 597 | 0 | 7 | 24.0 | 324 | 524 | 872 | 0 | — |
