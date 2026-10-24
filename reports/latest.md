# Synthetic Inventory Health

**Simulation date: 2026-10-24**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 31 |
| Healthy | 87 |
| Lead-time risk | 3 |
| Reorder | 4 |
| Stockout | 13 |

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
| ITEM-0001 | B - Core Products | Healthy | 374 | 291 | 30 | 28.5 | 138 | 545 | 820 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 21.3 | 93 | 147 | 288 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 278 | 1184 | 60 | 17.7 | 401 | 1357 | 1576 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1884 | 0 | 45 | 434.8 | 69 | 269 | 360 | 0 | — |
| ITEM-0006 | B - Core Products | Reorder | 145 | 0 | 14 | 20.5 | 41 | 148 | 297 | 155 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 117 | 0 | 45 | 75.8 | 20 | 92 | 138 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 203 | 0 | 14 | 34.0 | 35 | 125 | 250 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 210 | 0 | 60 | 160.2 | 23 | 103 | 143 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 79 | 410 | 90 | 39.3 | 63 | 247 | 289 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 866 | 1865 | 2094 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 316 | 90 | 90 | 109.4 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 646 | 0 | 7 | 49.5 | 35 | 140 | 414 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 162 | 0 | 7 | 88.4 | 23 | 38 | 93 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 232 | 0 | 45 | 102.9 | 72 | 176 | 244 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 376 | 155 | 45 | 55.2 | 107 | 421 | 564 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1112 | 0 | 30 | 351.2 | 37 | 136 | 202 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2796 | 0 | 60 | 272.6 | 212 | 838 | 1053 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 171 | 0 | 14 | 28.3 | 35 | 126 | 253 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 556 | 0 | 60 | 568.6 | 18 | 78 | 107 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 601 | 2041 | 2263 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 32 | 0 | 30 | 55.4 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 500 | 1169 | 60 | 50.8 | 545 | 1146 | 1353 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 191 | 0 | 30 | 90.5 | 18 | 84 | 147 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 159 | 960 | 90 | 30.6 | 159 | 633 | 742 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1197 | 0 | 14 | 238.9 | 31 | 107 | 212 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 276 | 135 | 60 | 63.0 | 70 | 338 | 469 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 288 | 0 | 45 | 85.3 | 54 | 210 | 281 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 139 | 265 | 14 | 11.7 | 67 | 245 | 495 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 81 | 95 | 14 | 19.2 | 26 | 90 | 178 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 248 | 172 | 30 | 29.6 | 89 | 349 | 525 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 446 | 315 | 30 | 30.6 | 155 | 607 | 912 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4386 | 0 | 60 | 606.4 | 186 | 628 | 729 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 45.6 | 242 | 407 | 637 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 72 | 116 | 14 | 15.0 | 28 | 100 | 201 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 670 | 0 | 45 | 199.0 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 760 | 60 | 0.0 | 291 | 741 | 896 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 77 | 0 | 45 | 106.6 | 11 | 45 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 135 | 154 | 60 | 31.2 | 157 | 422 | 552 | 263 | 67 |
| ITEM-0052 | B - Core Products | Healthy | 51 | 231 | 7 | 4.9 | 25 | 109 | 329 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 21 | 155 | 7 | 2.8 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4363 | 0 | 60 | 525.0 | 217 | 724 | 841 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 356 | 0 | 14 | 47.7 | 56 | 168 | 273 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 835 | 1680 | 90 | 45.1 | 700 | 2385 | 2644 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 100.5 | 429 | 781 | 1019 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 534 | 0 | 45 | 150.2 | 57 | 221 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 55 | 110 | 14 | 11.0 | 28 | 103 | 208 | 0 | 12 |
| ITEM-0062 | C - Slow Moving | Healthy | 77 | 0 | 30 | 51.3 | 14 | 61 | 106 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 553 | 0 | 14 | 84.9 | 37 | 135 | 272 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 339 | 310 | 60 | 60.9 | 231 | 571 | 688 | 0 | — |
| ITEM-0065 | B - Core Products | Reorder | 732 | 260 | 60 | 59.9 | 252 | 997 | 1254 | 265 | — |
| ITEM-0066 | B - Core Products | Healthy | 243 | 115 | 45 | 44.0 | 87 | 342 | 457 | 0 | — |
| ITEM-0067 | A - Top Movers | Reorder | 352 | 0 | 14 | 21.6 | 120 | 365 | 593 | 245 | — |
| ITEM-0068 | B - Core Products | Healthy | 366 | 0 | 30 | 82.8 | 50 | 188 | 280 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 91 | 0 | 7 | 33.2 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 29.1 | 3 | 10 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 886 | 1114 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3477 | 0 | 90 | 794.2 | 134 | 533 | 625 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 69 | 0 | 14 | 33.6 | 10 | 41 | 103 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 39 | 26 | 45 | 42.8 | 13 | 55 | 83 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 336 | 0 | 7 | 165.2 | 5 | 22 | 83 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 467 | 265 | 45 | 40.6 | 181 | 710 | 952 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 528 | 0 | 45 | 236.4 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 331 | 558 | 90 | 47.4 | 215 | 851 | 998 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 207 | 0 | 7 | 18.4 | 28 | 119 | 355 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 812 | 0 | 14 | 71.9 | 65 | 235 | 472 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 35 | 337 | 60 | 14.7 | 50 | 196 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Stockout | 0 | 605 | 14 | 0.0 | 243 | 414 | 652 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 16 | 35 | 14 | 14.8 | 6 | 23 | 55 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 255 | 0 | 45 | 58.4 | 53 | 254 | 385 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 523 | 468 | 14 | 28.4 | 457 | 734 | 991 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 33 | 50 | 30 | 21.8 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 667 | 1027 | 90 | 53.7 | 378 | 1508 | 1769 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 41 | 104 | 7 | 8.3 | 14 | 54 | 158 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6816 | 0 | 90 | 373.1 | 693 | 2356 | 2611 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3614 | 0 | 60 | 251.4 | 368 | 1246 | 1447 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 47.6 | 104 | 155 | 286 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 94 | 0 | 7 | 17.2 | 17 | 61 | 176 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 134 | 0 | 14 | 40.3 | 20 | 70 | 140 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 65.9 | 642 | 1433 | 1614 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 208 | 0 | 45 | 108.2 | 24 | 113 | 171 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 367 | 180 | 45 | 48.6 | 120 | 468 | 627 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 895 | 1542 | 90 | 51.6 | 657 | 2235 | 2477 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 449 | 499 | 60 | 41.2 | 224 | 889 | 1118 | 0 | 64 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 269 | 1072 | 1258 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1639 | 220 | 90 | 119.8 | 523 | 1768 | 1960 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 398 | 1161 | 60 | 22.5 | 454 | 1534 | 1782 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1000 | 940 | 45 | 54.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 34 | 0 | 14 | 23.9 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 908 | 0 | 14 | 94.0 | 236 | 381 | 584 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 681 | 798 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 181 | 135 | 30 | 30.1 | 64 | 251 | 378 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 42 | 59 | 30 | 22.1 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 106 | 285 | 7 | 8.1 | 34 | 139 | 415 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 80 | 146 | 14 | 23.5 | 103 | 154 | 226 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 101 | 216 | 14 | 10.1 | 59 | 210 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 78 | 0 | 7 | 13.2 | 16 | 64 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 594 | 0 | 45 | 67.1 | 139 | 547 | 733 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 532 | 0 | 14 | 87.4 | 34 | 126 | 254 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 280 | 130 | 60 | 66.8 | 68 | 324 | 450 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 136 | 171 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3716 | 0 | 60 | 264.8 | 361 | 1218 | 1414 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 92.2 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 394 | 0 | 14 | 48.2 | 61 | 184 | 298 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 363 | 474 | 30 | 23.6 | 203 | 680 | 894 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1093 | 539 | 60 | 60.1 | 464 | 1574 | 1829 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2141 | 0 | 45 | 212.0 | 159 | 624 | 836 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1360 | 320 | 60 | 109.9 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 330 | 470 | 45 | 31.2 | 167 | 654 | 875 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 735 | 0 | 7 | 60.1 | 36 | 134 | 391 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 100 | 393 | 494 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 134 | 636 | 90 | 39.7 | 104 | 412 | 483 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 14.8 | 465 | 782 | 1078 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 646 | 0 | 60 | 164.2 | 84 | 324 | 407 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 11 | 200 | 60 | 7.6 | 24 | 113 | 156 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 516 | 0 | 14 | 69.0 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 697 | 274 | 30 | 39.1 | 235 | 788 | 1037 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Reorder | 322 | 0 | 7 | 15.1 | 301 | 472 | 770 | 448 | — |
