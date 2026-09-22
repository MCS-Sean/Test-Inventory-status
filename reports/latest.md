# Synthetic Inventory Health

**Simulation date: 2026-09-22**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 66 |
| Lead-time risk | 13 |
| Reorder | 4 |
| Stockout | 27 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 498 | 748 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 175 | 0 | 7 | 26.2 | 95 | 149 | 289 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 808 | 517 | 60 | 52.6 | 392 | 1330 | 1545 | 220 | — |
| ITEM-0005 | B - Core Products | Excess | 1995 | 0 | 45 | 330.1 | 98 | 377 | 503 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 228 | 0 | 14 | 30.5 | 43 | 155 | 312 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 230 | 0 | 14 | 28.8 | 50 | 170 | 338 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 47 | 198 | 60 | 24.7 | 32 | 148 | 205 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 133 | 410 | 90 | 47.5 | 87 | 342 | 401 | 0 | 48 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 11.4 | 750 | 1535 | 1715 | 0 | 12 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 94.6 | 337 | 495 | 770 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 402 | 0 | 90 | 140.8 | 68 | 328 | 414 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1082 | 0 | 7 | 84.8 | 33 | 136 | 404 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 282.9 | 18 | 27 | 57 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 82 | 218 | 307 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 411 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1192 | 0 | 30 | 257.3 | 54 | 198 | 295 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3099 | 0 | 60 | 291.1 | 219 | 869 | 1092 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 320 | 0 | 14 | 36.5 | 53 | 185 | 369 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 578 | 0 | 60 | 419.5 | 24 | 109 | 150 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 630 | 2138 | 2370 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 5 | 45 | 30 | 7.3 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 26 | 117 | 204 | 0 | 1 |
| ITEM-0029 | B - Core Products | Healthy | 295 | 960 | 90 | 39.5 | 232 | 912 | 1069 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1322 | 0 | 14 | 183.3 | 43 | 152 | 303 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 317 | 441 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 381 | 0 | 45 | 78.5 | 81 | 305 | 407 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 309.7 | 77 | 214 | 282 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 272 | 0 | 14 | 24.6 | 63 | 230 | 462 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 192 | 0 | 14 | 32.1 | 37 | 127 | 253 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 88 | 344 | 518 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 150 | 581 | 872 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4575 | 0 | 60 | 429.8 | 279 | 929 | 1078 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 386 | 195 | 14 | 28.9 | 337 | 538 | 725 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 205 | 0 | 14 | 30.0 | 43 | 146 | 290 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 775 | 0 | 45 | 231.0 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 143 | 185 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 40 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Reorder | 313 | 0 | 14 | 29.8 | 175 | 333 | 553 | 240 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 20 | 80 | 45 | 20.5 | 14 | 59 | 89 | 0 | 21 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 165 | 0 | 7 | 16.4 | 26 | 107 | 318 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 112 | 0 | 7 | 15.5 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4575 | 0 | 60 | 404.9 | 297 | 987 | 1145 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 552 | 0 | 14 | 52.0 | 86 | 246 | 395 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1418 | 1125 | 90 | 79.2 | 678 | 2308 | 2559 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 509 | 1073 | 1455 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 86 | 323 | 431 | 0 | 1 |
| ITEM-0061 | B - Core Products | Reorder | 98 | 0 | 14 | 19.8 | 29 | 104 | 208 | 110 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 115 | 0 | 30 | 51.2 | 20 | 90 | 157 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 745 | 0 | 14 | 112.1 | 38 | 138 | 278 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 63.9 | 279 | 738 | 895 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1138 | 0 | 60 | 93.9 | 250 | 990 | 1245 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 424 | 0 | 45 | 75.1 | 88 | 348 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Reorder | 373 | 0 | 14 | 22.0 | 122 | 377 | 614 | 245 | — |
| ITEM-0068 | B - Core Products | Healthy | 95 | 390 | 30 | 14.7 | 74 | 275 | 411 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 92 | 0 | 7 | 33.8 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 58 | 193 | 45 | 17.8 | 84 | 234 | 332 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 14 | 0 | 7 | 16.6 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 231 | 908 | 1141 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3590 | 0 | 90 | 579.0 | 193 | 758 | 888 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 72 | 0 | 14 | 34.1 | 10 | 42 | 105 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 54 | 80 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 385 | 0 | 7 | 137.5 | 7 | 30 | 114 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 526 | 275 | 45 | 42.1 | 196 | 771 | 1033 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 597 | 0 | 45 | 251.1 | 29 | 139 | 210 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 544 | 393 | 90 | 76.3 | 218 | 868 | 1017 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 91 | 235 | 7 | 8.2 | 28 | 117 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1173 | 0 | 14 | 108.9 | 63 | 225 | 451 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 103 | 337 | 60 | 31.0 | 71 | 274 | 344 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 44 | 0 | 14 | 30.0 | 8 | 30 | 74 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 68 | 269 | 360 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 711 | 0 | 14 | 49.8 | 382 | 597 | 797 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 81 | 0 | 30 | 53.6 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1056 | 735 | 90 | 79.7 | 405 | 1612 | 1890 | 0 | 113 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 172 | 0 | 7 | 26.6 | 20 | 72 | 208 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7367 | 0 | 90 | 404.3 | 691 | 2350 | 2605 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4108 | 0 | 60 | 306.1 | 346 | 1165 | 1353 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 236 | 0 | 7 | 28.9 | 26 | 92 | 263 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 224 | 0 | 14 | 45.8 | 31 | 105 | 207 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 89.2 | 450 | 1081 | 1298 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 50 | 210 | 45 | 19.9 | 32 | 148 | 223 | 0 | 20 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 773 | 689 | 90 | 80.5 | 428 | 1302 | 1504 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 608 | 0 | 45 | 79.3 | 121 | 474 | 635 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1408 | 1041 | 90 | 81.9 | 655 | 2221 | 2461 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 542 | 481 | 60 | 48.3 | 231 | 916 | 1152 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 149 | 915 | 90 | 17.1 | 267 | 1061 | 1244 | 0 | 18 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2117 | 0 | 90 | 144.2 | 558 | 1894 | 2100 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 984 | 622 | 60 | 56.0 | 451 | 1523 | 1769 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 34 | 0 | 14 | 23.9 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 73.3 | 267 | 473 | 760 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 124 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 83 | 648 | 90 | 15.2 | 168 | 666 | 781 | 0 | 16 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 249 | 374 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 39 | 55 | 30 | 20.1 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 182 | 0 | 7 | 13.5 | 36 | 144 | 426 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 223 | 440 | 539 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 194 | 216 | 14 | 19.3 | 58 | 209 | 421 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 155 | 0 | 7 | 25.5 | 17 | 66 | 193 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 18.3 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 548 | 735 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 128.0 | 655 | 1711 | 1955 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 740 | 0 | 14 | 125.7 | 33 | 122 | 245 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 399 | 0 | 60 | 87.2 | 74 | 354 | 491 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 114 | 144 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4158 | 0 | 60 | 297.2 | 358 | 1212 | 1408 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 27 | 73 | 103 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 613 | 0 | 14 | 56.5 | 83 | 246 | 398 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 205 | 691 | 910 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1625 | 0 | 60 | 88.2 | 471 | 1595 | 1853 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2468 | 0 | 45 | 247.6 | 157 | 616 | 825 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 628 | 1542 | 1857 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 376 | 479 | 45 | 33.5 | 175 | 691 | 927 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1068 | 0 | 7 | 81.3 | 39 | 145 | 420 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 149 | 578 | 725 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 214 | 636 | 90 | 44.0 | 150 | 593 | 696 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 746 | 0 | 60 | 133.7 | 119 | 460 | 577 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 49 | 200 | 60 | 25.6 | 32 | 149 | 206 | 0 | 26 |
| ITEM-0155 | B - Core Products | Excess | 768 | 0 | 14 | 111.5 | 41 | 145 | 289 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 239 | 792 | 1041 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 481 | 367 | 7 | 19.9 | 315 | 509 | 848 | 0 | — |
