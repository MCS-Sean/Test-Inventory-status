# Synthetic Inventory Health

**Simulation date: 2026-09-30**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 83 |
| Lead-time risk | 9 |
| Reorder | 2 |
| Stockout | 17 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 131 | 513 | 772 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 28.3 | 104 | 170 | 342 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 672 | 737 | 60 | 43.0 | 400 | 1355 | 1574 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1969 | 0 | 45 | 360.9 | 88 | 339 | 454 | 0 | — |
| ITEM-0006 | B - Core Products | Reorder | 157 | 0 | 14 | 20.8 | 43 | 157 | 315 | 160 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 96 | 145 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 195 | 0 | 14 | 25.8 | 48 | 162 | 321 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 42 | 198 | 60 | 24.5 | 29 | 134 | 185 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 118 | 410 | 90 | 45.0 | 81 | 320 | 375 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.6 | 704 | 1407 | 1568 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 379 | 0 | 90 | 129.2 | 70 | 337 | 425 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 989 | 0 | 7 | 78.8 | 33 | 134 | 397 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 76 | 196 | 274 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 549 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1171 | 0 | 30 | 285.6 | 48 | 176 | 262 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3018 | 0 | 60 | 288.7 | 216 | 854 | 1074 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 279 | 0 | 14 | 34.8 | 50 | 171 | 339 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 571 | 0 | 60 | 439.2 | 23 | 103 | 142 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 619 | 2103 | 2331 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 78.5 | 7 | 26 | 45 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 233 | 0 | 30 | 85.6 | 31 | 116 | 173 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 267 | 960 | 90 | 39.7 | 210 | 823 | 965 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1288 | 0 | 14 | 195.5 | 40 | 139 | 278 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 380 | 0 | 60 | 90.7 | 67 | 323 | 449 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 365 | 0 | 45 | 87.6 | 69 | 261 | 349 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 685 | 0 | 60 | 327.9 | 73 | 201 | 264 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 159 | 245 | 14 | 13.8 | 66 | 239 | 480 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 162 | 0 | 14 | 30.7 | 32 | 112 | 222 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 433 | 0 | 30 | 52.9 | 88 | 342 | 514 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 520 | 290 | 30 | 36.9 | 152 | 590 | 886 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4537 | 0 | 60 | 481.0 | 248 | 824 | 956 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 494 | 270 | 14 | 34.5 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 167 | 0 | 14 | 26.2 | 40 | 136 | 270 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 747 | 0 | 45 | 221.9 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 66 | 153 | 196 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 14 | 80 | 45 | 15.0 | 14 | 57 | 85 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 77 | 218 | 7 | 7.6 | 25 | 106 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 51 | 155 | 7 | 7.1 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4535 | 0 | 60 | 423.0 | 282 | 937 | 1087 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 514 | 0 | 14 | 53.1 | 80 | 226 | 361 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1276 | 1125 | 90 | 70.2 | 687 | 2342 | 2596 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 54.0 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 78 | 292 | 390 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 63 | 110 | 14 | 12.7 | 29 | 104 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 108 | 0 | 30 | 54.0 | 18 | 80 | 140 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 691 | 0 | 14 | 102.0 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1026 | 0 | 60 | 82.5 | 256 | 1015 | 1276 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 389 | 0 | 45 | 71.7 | 85 | 335 | 449 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 252 | 245 | 14 | 15.2 | 120 | 369 | 602 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 454 | 0 | 30 | 78.1 | 67 | 248 | 370 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 68 | 0 | 7 | 24.1 | 6 | 29 | 114 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 9 | 25 | 7 | 11.2 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 886 | 1113 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3563 | 0 | 90 | 655.8 | 168 | 663 | 777 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 57 | 0 | 14 | 27.3 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 66 | 0 | 45 | 77.1 | 12 | 52 | 78 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 372 | 0 | 7 | 144.3 | 7 | 28 | 105 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 67.5 | 107 | 310 | 376 | 0 | 68 |
| ITEM-0079 | B - Core Products | Healthy | 451 | 540 | 45 | 37.4 | 190 | 746 | 999 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 578 | 0 | 45 | 244.2 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 502 | 393 | 90 | 71.9 | 213 | 848 | 995 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 232 | 0 | 7 | 20.5 | 28 | 119 | 357 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1082 | 0 | 14 | 99.2 | 64 | 228 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 90 | 337 | 60 | 30.9 | 62 | 240 | 301 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 63.7 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 38 | 0 | 14 | 28.7 | 8 | 28 | 68 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 363 | 0 | 45 | 85.1 | 52 | 249 | 377 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 297 | 702 | 14 | 23.4 | 361 | 552 | 729 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 70 | 0 | 30 | 46.0 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 934 | 735 | 90 | 70.0 | 407 | 1622 | 1902 | 0 | 103 |
| ITEM-0093 | B - Core Products | Healthy | 608 | 0 | 7 | 37.0 | 239 | 371 | 715 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 141 | 0 | 7 | 24.1 | 18 | 65 | 188 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7241 | 0 | 90 | 393.8 | 697 | 2371 | 2628 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3972 | 0 | 60 | 292.3 | 350 | 1179 | 1370 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 202 | 0 | 7 | 27.6 | 24 | 83 | 237 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 198 | 0 | 14 | 45.2 | 28 | 94 | 186 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 761 | 765 | 60 | 63.8 | 630 | 1358 | 1525 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 42 | 210 | 45 | 18.2 | 30 | 137 | 206 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 565 | 0 | 45 | 76.2 | 118 | 459 | 615 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1294 | 1041 | 90 | 76.7 | 642 | 2177 | 2413 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 457 | 481 | 60 | 40.8 | 230 | 913 | 1148 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 236.5 | 56 | 130 | 200 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 64 | 1100 | 90 | 7.1 | 276 | 1100 | 1289 | 0 | 8 |
| ITEM-0110 | C - Slow Moving | Healthy | 644 | 0 | 60 | 184.0 | 115 | 329 | 434 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2005 | 0 | 90 | 140.5 | 542 | 1841 | 2040 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 835 | 902 | 60 | 47.2 | 453 | 1532 | 1779 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 22 | 45 | 14 | 15.1 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 86 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 45 | 648 | 90 | 8.4 | 165 | 652 | 764 | 0 | 9 |
| ITEM-0119 | B - Core Products | Healthy | 338 | 0 | 30 | 58.3 | 62 | 242 | 364 | 0 | — |
| ITEM-0120 | C - Slow Moving | Reorder | 24 | 55 | 30 | 12.1 | 17 | 79 | 138 | 59 | — |
| ITEM-0121 | B - Core Products | Healthy | 73 | 290 | 7 | 5.4 | 36 | 144 | 427 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 125 | 216 | 14 | 12.6 | 57 | 206 | 415 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 109 | 0 | 7 | 18.5 | 16 | 64 | 187 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 919 | 200 | 30 | 108.3 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 556 | 745 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 694 | 0 | 14 | 119.0 | 33 | 121 | 243 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 375 | 0 | 60 | 85.4 | 71 | 339 | 471 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 114 | 144 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4068 | 0 | 60 | 298.1 | 351 | 1184 | 1375 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 30 | 82 | 115 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 558 | 0 | 14 | 55.6 | 77 | 228 | 369 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 514 | 227 | 30 | 33.2 | 164 | 645 | 970 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1491 | 269 | 60 | 81.5 | 467 | 1583 | 1839 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2392 | 0 | 45 | 242.2 | 154 | 609 | 816 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 552 | 1320 | 1584 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 325 | 479 | 45 | 30.0 | 170 | 668 | 896 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 982 | 0 | 7 | 75.8 | 38 | 142 | 414 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 129 | 506 | 636 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 197 | 636 | 90 | 44.2 | 138 | 544 | 638 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 42.8 | 339 | 620 | 1013 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 147.4 | 218 | 365 | 570 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 719 | 0 | 60 | 138.6 | 111 | 428 | 537 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 266.6 | 276 | 594 | 667 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 39 | 200 | 60 | 22.1 | 30 | 138 | 191 | 0 | 23 |
| ITEM-0155 | B - Core Products | Excess | 701 | 0 | 14 | 100.0 | 41 | 147 | 294 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 572 | 259 | 30 | 31.7 | 239 | 799 | 1051 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 26.9 | 301 | 487 | 810 | 0 | — |
