# Synthetic Inventory Health

**Simulation date: 2026-09-01**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 54 |
| Lead-time risk | 46 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 509 | 765 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 127 | 180 | 7 | 17.8 | 99 | 156 | 306 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1135 | 294 | 60 | 77.6 | 373 | 1265 | 1470 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2072 | 0 | 45 | 276.3 | 121 | 466 | 624 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 367 | 0 | 14 | 48.5 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Lead-time risk | 4 | 142 | 45 | 2.4 | 21 | 98 | 147 | 0 | 3 |
| ITEM-0008 | B - Core Products | Healthy | 346 | 0 | 14 | 34.1 | 63 | 215 | 428 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 77 | 198 | 60 | 31.2 | 41 | 192 | 266 | 0 | 32 |
| ITEM-0010 | B - Core Products | Lead-time risk | 167 | 410 | 90 | 42.9 | 121 | 475 | 557 | 0 | 43 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 2128 | 0 | 7 | 127.9 | 306 | 440 | 673 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 461 | 0 | 90 | 165.3 | 67 | 321 | 405 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1373 | 0 | 7 | 107.2 | 34 | 137 | 406 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 118.1 | 28 | 48 | 121 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Lead-time risk | 1 | 510 | 45 | 0.1 | 106 | 418 | 561 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1244 | 0 | 30 | 210.1 | 66 | 250 | 374 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3337 | 0 | 60 | 328.6 | 210 | 830 | 1043 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 112 | 323 | 14 | 10.4 | 64 | 226 | 453 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 597 | 0 | 60 | 346.6 | 29 | 135 | 186 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 104 | 2305 | 90 | 6.0 | 653 | 2222 | 2463 | 0 | 7 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Lead-time risk | 13 | 45 | 30 | 17.5 | 8 | 32 | 54 | 0 | 18 |
| ITEM-0027 | B - Core Products | Healthy | 1161 | 717 | 60 | 87.4 | 685 | 1496 | 1775 | 0 | — |
| ITEM-0028 | C - Slow Moving | Lead-time risk | 4 | 243 | 30 | 1.1 | 32 | 144 | 253 | 0 | 2 |
| ITEM-0029 | B - Core Products | Lead-time risk | 392 | 960 | 90 | 42.5 | 285 | 1126 | 1320 | 0 | 43 |
| ITEM-0030 | C - Slow Moving | Healthy | 2 | 35 | 7 | 4.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1412 | 0 | 14 | 148.3 | 57 | 200 | 400 | 0 | — |
| ITEM-0032 | C - Slow Moving | Lead-time risk | 6 | 395 | 60 | 1.5 | 64 | 305 | 423 | 0 | 2 |
| ITEM-0033 | B - Core Products | Healthy | 440 | 0 | 45 | 68.8 | 105 | 400 | 534 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 749 | 0 | 60 | 364.4 | 69 | 195 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 498 | 0 | 14 | 44.4 | 64 | 233 | 468 | 0 | — |
| ITEM-0036 | B - Core Products | Stockout | 0 | 350 | 7 | 0.0 | 126 | 188 | 349 | 0 | 1 |
| ITEM-0037 | B - Core Products | Healthy | 260 | 0 | 14 | 33.4 | 46 | 163 | 327 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 87 | 340 | 512 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 165 | 575 | 30 | 12.1 | 147 | 571 | 858 | 0 | 13 |
| ITEM-0040 | A - Top Movers | Excess | 4723 | 0 | 60 | 345.0 | 356 | 1192 | 1383 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 659 | 0 | 14 | 41.7 | 351 | 589 | 810 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 300 | 0 | 14 | 33.4 | 57 | 192 | 381 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 850 | 0 | 45 | 254.2 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 148.5 | 124 | 393 | 482 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 11.1 | 83 | 205 | 264 | 0 | 12 |
| ITEM-0047 | C - Slow Moving | Healthy | 462 | 0 | 60 | 121.6 | 159 | 391 | 505 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 540 | 0 | 14 | 54.7 | 181 | 329 | 537 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 33 | 80 | 45 | 26.8 | 17 | 74 | 111 | 0 | 27 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 12 | 224 | 60 | 5.9 | 116 | 241 | 302 | 66 | 6 |
| ITEM-0052 | B - Core Products | Healthy | 378 | 0 | 7 | 37.1 | 28 | 110 | 324 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 259 | 0 | 7 | 34.7 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4739 | 0 | 60 | 331.7 | 375 | 1247 | 1447 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 700 | 0 | 14 | 53.8 | 102 | 298 | 480 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1834 | 580 | 90 | 106.6 | 652 | 2218 | 2458 | 0 | 107 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 802 | 30 | 0.0 | 379 | 765 | 1027 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 27 | 564 | 45 | 3.9 | 115 | 433 | 579 | 0 | 4 |
| ITEM-0061 | B - Core Products | Lead-time risk | 43 | 145 | 14 | 8.9 | 29 | 102 | 204 | 0 | 9 |
| ITEM-0062 | C - Slow Moving | Healthy | 149 | 0 | 30 | 51.4 | 26 | 116 | 203 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 873 | 0 | 14 | 128.4 | 38 | 140 | 283 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 595 | 310 | 60 | 82.3 | 272 | 714 | 866 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1409 | 0 | 60 | 119.7 | 243 | 961 | 1208 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 544 | 0 | 45 | 94.7 | 90 | 355 | 475 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 762 | 0 | 14 | 45.7 | 121 | 371 | 605 | 0 | — |
| ITEM-0068 | B - Core Products | Lead-time risk | 165 | 390 | 30 | 19.6 | 93 | 355 | 531 | 0 | 20 |
| ITEM-0069 | C - Slow Moving | Healthy | 58 | 0 | 7 | 20.0 | 7 | 31 | 118 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 50.7 | 82 | 215 | 301 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 32 | 0 | 7 | 37.4 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Lead-time risk | 25 | 1070 | 60 | 2.2 | 236 | 930 | 1169 | 0 | 3 |
| ITEM-0073 | B - Core Products | Excess | 3665 | 0 | 90 | 469.9 | 241 | 951 | 1115 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 42 | 106 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Lead-time risk | 2 | 66 | 45 | 2.6 | 11 | 46 | 69 | 0 | 3 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 61.4 | 214 | 412 | 457 | 0 | 62 |
| ITEM-0077 | C - Slow Moving | Excess | 420 | 0 | 7 | 117.4 | 9 | 38 | 145 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.0 | 104 | 288 | 348 | 0 | 91 |
| ITEM-0079 | B - Core Products | Reorder | 762 | 0 | 45 | 60.7 | 196 | 774 | 1037 | 275 | — |
| ITEM-0080 | C - Slow Moving | Excess | 641 | 0 | 45 | 258.7 | 30 | 144 | 219 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 713 | 235 | 90 | 106.6 | 204 | 813 | 954 | 0 | — |
| ITEM-0082 | B - Core Products | Stockout | 0 | 305 | 7 | 0.0 | 28 | 112 | 333 | 0 | 1 |
| ITEM-0083 | B - Core Products | Excess | 1423 | 0 | 14 | 135.8 | 62 | 220 | 440 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 143 | 337 | 60 | 31.6 | 96 | 372 | 467 | 0 | 32 |
| ITEM-0085 | B - Core Products | Lead-time risk | 26 | 465 | 14 | 3.5 | 218 | 329 | 483 | 0 | 4 |
| ITEM-0086 | C - Slow Moving | Healthy | 62 | 0 | 14 | 33.4 | 9 | 37 | 93 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Lead-time risk | 12 | 365 | 45 | 2.7 | 71 | 280 | 374 | 0 | 3 |
| ITEM-0089 | A - Top Movers | Lead-time risk | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | 4 |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 106 | 0 | 30 | 66.7 | 14 | 64 | 111 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1320 | 436 | 90 | 101.0 | 401 | 1591 | 1865 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 495 | 0 | 7 | 31.3 | 241 | 368 | 700 | 0 | — |
| ITEM-0094 | B - Core Products | Lead-time risk | 1 | 262 | 7 | 0.1 | 28 | 95 | 268 | 0 | 1 |
| ITEM-0095 | A - Top Movers | Excess | 7776 | 0 | 90 | 439.9 | 673 | 2282 | 2530 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4404 | 0 | 60 | 324.1 | 351 | 1180 | 1371 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 82 | 245 | 7 | 13.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Stockout | 0 | 330 | 7 | 0.0 | 32 | 114 | 326 | 0 | — |
| ITEM-0100 | B - Core Products | Lead-time risk | 3 | 256 | 14 | 0.5 | 38 | 132 | 262 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1129 | 420 | 60 | 75.3 | 585 | 1500 | 1815 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 80 | 210 | 45 | 24.7 | 40 | 189 | 286 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 1024 | 422 | 90 | 111.0 | 413 | 1253 | 1446 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 750 | 0 | 45 | 92.5 | 126 | 500 | 670 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1809 | 524 | 90 | 107.3 | 644 | 2179 | 2415 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 797 | 241 | 60 | 74.0 | 223 | 880 | 1106 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 187.2 | 67 | 167 | 263 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 331 | 915 | 90 | 36.1 | 280 | 1115 | 1307 | 0 | 37 |
| ITEM-0110 | C - Slow Moving | Excess | 746 | 0 | 60 | 315.2 | 96 | 241 | 312 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2392 | 0 | 90 | 161.3 | 562 | 1912 | 2120 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1380 | 360 | 60 | 78.5 | 452 | 1525 | 1772 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 692 | 1100 | 45 | 38.4 | 878 | 1708 | 1960 | 0 | 39 |
| ITEM-0114 | C - Slow Moving | Healthy | 11 | 55 | 14 | 7.6 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1014 | 0 | 14 | 60.3 | 298 | 551 | 904 | 0 | — |
| ITEM-0116 | C - Slow Moving | Lead-time risk | 1 | 115 | 45 | 0.7 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 204 | 530 | 90 | 37.6 | 166 | 660 | 774 | 0 | 38 |
| ITEM-0119 | B - Core Products | Lead-time risk | 4 | 355 | 30 | 0.7 | 65 | 254 | 381 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 86 | 0 | 30 | 46.1 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 459 | 0 | 7 | 35.3 | 37 | 141 | 414 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Lead-time risk | 15 | 218 | 14 | 4.1 | 102 | 157 | 233 | 0 | 5 |
| ITEM-0124 | B - Core Products | Lead-time risk | 77 | 292 | 14 | 7.3 | 60 | 219 | 441 | 0 | 8 |
| ITEM-0125 | B - Core Products | Healthy | 143 | 0 | 7 | 22.8 | 17 | 68 | 200 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 11.1 | 526 | 947 | 1137 | 0 | 12 |
| ITEM-0128 | B - Core Products | Lead-time risk | 8 | 698 | 45 | 0.9 | 140 | 551 | 739 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1686 | 419 | 90 | 134.3 | 698 | 1841 | 2105 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 855 | 0 | 14 | 134.5 | 35 | 131 | 264 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 501 | 0 | 60 | 119.3 | 68 | 325 | 451 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 7 | 135 | 90 | 7.4 | 24 | 110 | 139 | 0 | 8 |
| ITEM-0135 | A - Top Movers | Excess | 4451 | 0 | 60 | 323.1 | 354 | 1195 | 1388 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 749 | 0 | 14 | 52.7 | 107 | 320 | 519 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 227 | 560 | 30 | 15.4 | 195 | 652 | 858 | 0 | 16 |
| ITEM-0140 | A - Top Movers | Healthy | 2033 | 0 | 60 | 113.1 | 460 | 1557 | 1809 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2662 | 0 | 45 | 267.1 | 157 | 616 | 825 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 547 | 1246 | 1486 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 641 | 243 | 45 | 59.7 | 167 | 661 | 887 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1373 | 0 | 7 | 108.2 | 37 | 139 | 405 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 35 | 888 | 60 | 4.0 | 187 | 726 | 912 | 0 | 4 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 274 | 636 | 90 | 44.2 | 190 | 755 | 885 | 0 | 45 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 431 | 721 | 991 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 636 | 178 | 60 | 84.2 | 160 | 621 | 780 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 75 | 200 | 60 | 30.3 | 41 | 193 | 267 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 925 | 0 | 14 | 134.3 | 40 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 258 | 671 | 30 | 14.9 | 231 | 769 | 1011 | 0 | 15 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 662 | 0 | 7 | 31.4 | 292 | 461 | 756 | 0 | — |
