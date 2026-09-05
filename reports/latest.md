# Synthetic Inventory Health

**Simulation date: 2026-09-05**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 62 |
| Lead-time risk | 29 |
| Reorder | 1 |
| Stockout | 19 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 501 | 752 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1057 | 294 | 60 | 69.5 | 388 | 1316 | 1529 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2060 | 0 | 45 | 295.2 | 113 | 434 | 581 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 337 | 0 | 14 | 44.9 | 43 | 156 | 314 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 98 | 147 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 326 | 0 | 14 | 33.5 | 61 | 207 | 412 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 70 | 198 | 60 | 29.6 | 40 | 185 | 256 | 0 | 30 |
| ITEM-0010 | B - Core Products | Lead-time risk | 160 | 410 | 90 | 44.0 | 113 | 444 | 520 | 0 | 45 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2128 | 0 | 7 | 127.9 | 306 | 440 | 673 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 450 | 0 | 90 | 161.4 | 67 | 321 | 405 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1316 | 0 | 7 | 103.5 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 105 | 416 | 558 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1237 | 0 | 30 | 217.4 | 64 | 241 | 360 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3295 | 0 | 60 | 325.9 | 209 | 826 | 1039 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 93 | 323 | 14 | 9.1 | 61 | 214 | 429 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 594 | 0 | 60 | 363.7 | 28 | 128 | 177 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 35 | 2305 | 90 | 2.0 | 654 | 2223 | 2464 | 0 | 3 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 17.7 | 8 | 31 | 53 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1161 | 717 | 60 | 104.5 | 773 | 1451 | 1607 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 31 | 139 | 243 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 369 | 960 | 90 | 41.6 | 275 | 1083 | 1270 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 32 | 0 | 7 | 57.6 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1388 | 0 | 14 | 151.4 | 55 | 193 | 385 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 63 | 301 | 417 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 427 | 0 | 45 | 69.0 | 102 | 387 | 517 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 722 | 0 | 60 | 306.5 | 76 | 220 | 291 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 462 | 0 | 14 | 42.0 | 63 | 228 | 459 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 326 | 0 | 7 | 41.0 | 127 | 191 | 358 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 236 | 0 | 14 | 31.7 | 43 | 155 | 312 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 332 | 499 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 101 | 575 | 30 | 7.3 | 149 | 579 | 870 | 0 | 8 |
| ITEM-0040 | A - Top Movers | Excess | 4693 | 0 | 60 | 351.4 | 349 | 1164 | 1351 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 37.4 | 284 | 530 | 873 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 282 | 0 | 14 | 33.5 | 53 | 180 | 356 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 835 | 0 | 45 | 249.7 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 171.8 | 116 | 349 | 426 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 385 | 175 | 60 | 87.9 | 172 | 440 | 571 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 482 | 0 | 14 | 45.9 | 185 | 343 | 564 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 30 | 80 | 45 | 25.0 | 16 | 72 | 108 | 0 | 26 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 338 | 0 | 7 | 32.8 | 28 | 111 | 327 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 236 | 0 | 7 | 32.0 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4712 | 0 | 60 | 335.2 | 370 | 1228 | 1425 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 665 | 0 | 14 | 53.3 | 98 | 286 | 460 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1764 | 580 | 90 | 101.7 | 658 | 2237 | 2480 | 0 | 102 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 12 | 564 | 45 | 1.9 | 108 | 406 | 542 | 0 | 2 |
| ITEM-0061 | B - Core Products | Lead-time risk | 16 | 145 | 14 | 3.3 | 29 | 103 | 207 | 0 | 4 |
| ITEM-0062 | C - Slow Moving | Healthy | 142 | 0 | 30 | 50.7 | 25 | 112 | 196 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 852 | 0 | 14 | 125.7 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 84.5 | 270 | 700 | 848 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1361 | 0 | 60 | 115.1 | 244 | 966 | 1214 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 517 | 0 | 45 | 90.2 | 90 | 354 | 475 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 680 | 0 | 14 | 40.6 | 122 | 374 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 150 | 390 | 30 | 18.6 | 90 | 341 | 511 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 45 | 0 | 7 | 15.6 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 30 | 0 | 7 | 35.1 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 237 | 934 | 1173 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3650 | 0 | 90 | 488.8 | 231 | 911 | 1068 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 107 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 11 | 47 | 71 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 412 | 0 | 7 | 118.5 | 9 | 37 | 142 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.5 | 104 | 286 | 346 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 713 | 275 | 45 | 56.3 | 198 | 781 | 1047 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 634 | 0 | 45 | 257.0 | 30 | 144 | 218 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 680 | 235 | 90 | 100.2 | 207 | 825 | 968 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 295 | 0 | 7 | 27.2 | 28 | 115 | 343 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1378 | 0 | 14 | 133.1 | 61 | 217 | 434 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 137 | 337 | 60 | 32.2 | 91 | 351 | 440 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 58 | 0 | 14 | 32.6 | 9 | 36 | 89 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 101 | 0 | 30 | 64.9 | 14 | 63 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1260 | 436 | 90 | 96.2 | 403 | 1596 | 1871 | 0 | — |
| ITEM-0093 | B - Core Products | Reorder | 365 | 0 | 7 | 21.2 | 248 | 387 | 749 | 385 | — |
| ITEM-0094 | B - Core Products | Healthy | 246 | 0 | 7 | 31.5 | 26 | 89 | 253 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7718 | 0 | 90 | 434.1 | 676 | 2294 | 2543 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4363 | 0 | 60 | 330.3 | 342 | 1148 | 1333 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 310 | 0 | 7 | 31.5 | 32 | 111 | 318 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 36 | 125 | 250 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1129 | 420 | 60 | 85.1 | 551 | 1361 | 1639 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 74 | 210 | 45 | 24.1 | 38 | 180 | 272 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 112.9 | 410 | 1236 | 1426 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 726 | 0 | 45 | 91.0 | 125 | 492 | 660 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1711 | 524 | 90 | 99.6 | 656 | 2220 | 2460 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 741 | 241 | 60 | 68.0 | 226 | 891 | 1120 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 226.3 | 61 | 144 | 223 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 291 | 915 | 90 | 31.7 | 280 | 1116 | 1308 | 0 | 32 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 315.2 | 96 | 241 | 312 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2339 | 0 | 90 | 154.9 | 571 | 1946 | 2157 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1324 | 360 | 60 | 76.5 | 445 | 1501 | 1743 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 3 | 55 | 14 | 2.0 | 7 | 30 | 74 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 59.3 | 298 | 552 | 908 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 185 | 530 | 90 | 33.9 | 167 | 664 | 779 | 0 | 34 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 255 | 383 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 80 | 0 | 30 | 43.4 | 16 | 74 | 129 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 400 | 0 | 7 | 30.0 | 36 | 143 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Lead-time risk | 51 | 292 | 14 | 4.9 | 60 | 217 | 436 | 0 | 5 |
| ITEM-0125 | B - Core Products | Healthy | 125 | 0 | 7 | 20.2 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 546 | 732 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1534 | 419 | 90 | 121.9 | 700 | 1846 | 2110 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 836 | 0 | 14 | 133.4 | 35 | 129 | 261 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 483 | 0 | 60 | 113.8 | 69 | 328 | 456 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 6 | 135 | 90 | 6.7 | 23 | 105 | 132 | 0 | 7 |
| ITEM-0135 | A - Top Movers | Excess | 4396 | 0 | 60 | 321.7 | 351 | 1185 | 1376 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 723 | 0 | 14 | 53.5 | 103 | 306 | 495 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 158 | 560 | 30 | 10.7 | 195 | 653 | 859 | 0 | 11 |
| ITEM-0140 | A - Top Movers | Healthy | 1952 | 0 | 60 | 108.2 | 462 | 1563 | 1816 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2631 | 0 | 45 | 265.8 | 156 | 612 | 820 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 584 | 1375 | 1647 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 594 | 243 | 45 | 54.9 | 168 | 666 | 894 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1329 | 0 | 7 | 104.6 | 37 | 139 | 406 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 20 | 888 | 60 | 2.4 | 177 | 688 | 864 | 0 | 3 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 263 | 636 | 90 | 44.2 | 183 | 724 | 849 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 422 | 705 | 968 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 625 | 178 | 60 | 88.2 | 151 | 584 | 733 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 71 | 200 | 60 | 30.0 | 40 | 185 | 256 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 888 | 0 | 14 | 126.9 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 166 | 671 | 30 | 9.3 | 237 | 792 | 1042 | 0 | 10 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 498 | 0 | 7 | 21.7 | 305 | 489 | 810 | 0 | — |
