# Synthetic Inventory Health

**Simulation date: 2026-09-04**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 61 |
| Lead-time risk | 30 |
| Stockout | 20 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 506 | 761 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1091 | 294 | 60 | 73.3 | 379 | 1287 | 1495 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2062 | 0 | 45 | 291.8 | 114 | 440 | 588 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 345 | 0 | 14 | 46.2 | 43 | 155 | 312 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 21 | 98 | 148 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 331 | 0 | 14 | 33.9 | 62 | 209 | 414 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 73 | 198 | 60 | 31.0 | 40 | 184 | 255 | 0 | 31 |
| ITEM-0010 | B - Core Products | Lead-time risk | 162 | 410 | 90 | 43.5 | 116 | 455 | 533 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2128 | 0 | 7 | 127.9 | 306 | 440 | 673 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 455 | 0 | 90 | 163.8 | 66 | 319 | 403 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1328 | 0 | 7 | 104.6 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 106 | 419 | 561 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1237 | 0 | 30 | 212.9 | 65 | 246 | 368 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3306 | 0 | 60 | 326.6 | 209 | 827 | 1040 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 98 | 323 | 14 | 9.5 | 61 | 215 | 431 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 594 | 0 | 60 | 356.4 | 28 | 130 | 180 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 51 | 2305 | 90 | 2.9 | 657 | 2234 | 2476 | 0 | 3 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.7 | 8 | 31 | 53 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 104.5 | 622 | 1300 | 1534 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 31 | 140 | 245 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 376 | 960 | 90 | 42.2 | 276 | 1087 | 1275 | 0 | 43 |
| ITEM-0030 | C - Slow Moving | Healthy | 32 | 0 | 7 | 57.6 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1395 | 0 | 14 | 150.5 | 55 | 194 | 389 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 64 | 305 | 423 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 433 | 0 | 45 | 69.1 | 104 | 393 | 524 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 471 | 0 | 14 | 42.3 | 64 | 231 | 465 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 331 | 0 | 7 | 41.9 | 127 | 191 | 357 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 238 | 0 | 14 | 31.5 | 44 | 158 | 317 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 84 | 329 | 495 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 114 | 575 | 30 | 8.2 | 149 | 579 | 869 | 0 | 9 |
| ITEM-0040 | A - Top Movers | Excess | 4701 | 0 | 60 | 347.9 | 352 | 1177 | 1366 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 611 | 0 | 14 | 37.4 | 353 | 599 | 828 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 290 | 0 | 14 | 34.1 | 54 | 182 | 361 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 837 | 0 | 45 | 247.8 | 41 | 197 | 298 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 154.9 | 122 | 380 | 465 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 405 | 175 | 60 | 97.5 | 170 | 424 | 549 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 482 | 0 | 14 | 45.9 | 185 | 343 | 564 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 30 | 80 | 45 | 24.8 | 16 | 72 | 109 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 347 | 0 | 7 | 33.9 | 28 | 110 | 326 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 237 | 0 | 7 | 31.9 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4715 | 0 | 60 | 333.1 | 372 | 1236 | 1434 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 671 | 0 | 14 | 53.3 | 99 | 288 | 465 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1783 | 580 | 90 | 102.9 | 657 | 2234 | 2476 | 0 | 103 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 14 | 564 | 45 | 2.1 | 109 | 413 | 551 | 0 | 3 |
| ITEM-0061 | B - Core Products | Lead-time risk | 22 | 145 | 14 | 4.5 | 29 | 103 | 207 | 0 | 5 |
| ITEM-0062 | C - Slow Moving | Healthy | 145 | 0 | 30 | 51.4 | 25 | 113 | 198 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 858 | 0 | 14 | 126.4 | 38 | 140 | 283 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 84.5 | 270 | 700 | 848 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1374 | 0 | 60 | 116.7 | 244 | 963 | 1210 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 523 | 0 | 45 | 90.9 | 90 | 355 | 476 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 695 | 0 | 14 | 41.3 | 123 | 376 | 611 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 154 | 390 | 30 | 18.8 | 91 | 346 | 518 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 50 | 0 | 7 | 17.4 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 30 | 0 | 7 | 34.6 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 237 | 935 | 1175 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3654 | 0 | 90 | 482.2 | 235 | 925 | 1084 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 107 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 11 | 47 | 71 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 413 | 0 | 7 | 117.3 | 9 | 38 | 143 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.5 | 104 | 286 | 346 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 724 | 275 | 45 | 57.1 | 198 | 782 | 1048 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 635 | 0 | 45 | 258.6 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 692 | 235 | 90 | 103.6 | 204 | 812 | 952 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 115 | 341 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1386 | 0 | 14 | 134.0 | 61 | 217 | 434 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 138 | 337 | 60 | 32.3 | 91 | 352 | 442 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 224 | 348 | 520 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 60 | 0 | 14 | 33.5 | 9 | 36 | 90 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 70 | 275 | 369 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 103 | 0 | 30 | 65.7 | 14 | 63 | 110 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1278 | 436 | 90 | 98.2 | 400 | 1585 | 1858 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 31.3 | 241 | 368 | 700 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 251 | 0 | 7 | 32.1 | 26 | 89 | 253 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7728 | 0 | 90 | 430.4 | 683 | 2317 | 2569 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4378 | 0 | 60 | 331.9 | 341 | 1146 | 1331 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 310 | 0 | 7 | 30.9 | 32 | 113 | 323 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 37 | 127 | 252 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1129 | 420 | 60 | 85.1 | 551 | 1361 | 1639 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 75 | 210 | 45 | 24.1 | 39 | 183 | 276 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 112.9 | 410 | 1236 | 1426 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 726 | 0 | 45 | 89.9 | 126 | 498 | 668 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1749 | 524 | 90 | 103.8 | 643 | 2177 | 2413 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 756 | 241 | 60 | 69.4 | 226 | 891 | 1119 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 226.3 | 61 | 144 | 223 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 296 | 915 | 90 | 32.0 | 283 | 1126 | 1320 | 0 | 32 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 315.2 | 96 | 241 | 312 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2359 | 0 | 90 | 158.1 | 565 | 1923 | 2132 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1331 | 360 | 60 | 76.4 | 447 | 1510 | 1753 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 5 | 55 | 14 | 3.4 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1007 | 0 | 14 | 59.6 | 298 | 552 | 906 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 187 | 530 | 90 | 34.1 | 168 | 667 | 782 | 0 | 35 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 255 | 383 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 82 | 0 | 30 | 44.5 | 16 | 74 | 129 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 422 | 0 | 7 | 31.8 | 36 | 143 | 421 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Lead-time risk | 60 | 292 | 14 | 5.8 | 60 | 216 | 433 | 0 | 6 |
| ITEM-0125 | B - Core Products | Healthy | 129 | 0 | 7 | 20.9 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 549 | 737 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 842 | 0 | 14 | 134.4 | 35 | 129 | 261 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 489 | 0 | 60 | 115.5 | 69 | 328 | 455 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 6 | 135 | 90 | 6.6 | 23 | 106 | 134 | 0 | 7 |
| ITEM-0135 | A - Top Movers | Excess | 4409 | 0 | 60 | 322.6 | 351 | 1185 | 1376 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 731 | 0 | 14 | 53.4 | 104 | 310 | 501 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 174 | 560 | 30 | 11.8 | 195 | 653 | 859 | 0 | 12 |
| ITEM-0140 | A - Top Movers | Healthy | 1987 | 0 | 60 | 110.9 | 458 | 1551 | 1802 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2638 | 0 | 45 | 265.6 | 156 | 613 | 822 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 584 | 1375 | 1647 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 602 | 243 | 45 | 55.5 | 169 | 669 | 897 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1340 | 0 | 7 | 105.7 | 37 | 139 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 21 | 888 | 60 | 2.5 | 178 | 693 | 870 | 0 | 3 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 265 | 636 | 90 | 43.8 | 186 | 738 | 865 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 422 | 705 | 968 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 628 | 178 | 60 | 87.6 | 152 | 590 | 740 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 73 | 200 | 60 | 30.6 | 40 | 186 | 258 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 890 | 0 | 14 | 125.7 | 41 | 148 | 296 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 193 | 671 | 30 | 11.0 | 234 | 780 | 1026 | 0 | 11 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 498 | 0 | 7 | 21.7 | 305 | 489 | 810 | 0 | — |
