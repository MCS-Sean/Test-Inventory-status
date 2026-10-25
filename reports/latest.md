# Synthetic Inventory Health

**Simulation date: 2026-10-25**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 31 |
| Healthy | 89 |
| Lead-time risk | 3 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Healthy | 365 | 291 | 30 | 27.9 | 138 | 544 | 819 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 313 | 0 | 7 | 50.4 | 91 | 141 | 272 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 252 | 1184 | 60 | 16.0 | 402 | 1362 | 1582 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1879 | 0 | 45 | 437.0 | 69 | 267 | 358 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 142 | 155 | 14 | 20.1 | 41 | 148 | 296 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 115 | 0 | 45 | 73.9 | 20 | 92 | 139 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 201 | 0 | 14 | 33.8 | 35 | 125 | 249 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 207 | 0 | 60 | 154.0 | 23 | 106 | 146 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 78 | 410 | 90 | 39.9 | 61 | 239 | 281 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 866 | 1865 | 2094 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 316 | 90 | 90 | 111.5 | 67 | 325 | 410 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 638 | 0 | 7 | 49.3 | 35 | 139 | 411 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 162 | 0 | 7 | 88.4 | 23 | 38 | 93 | 0 | — |
| ITEM-0016 | C - Slow Moving | Reorder | 199 | 0 | 45 | 75.9 | 79 | 200 | 279 | 80 | — |
| ITEM-0017 | B - Core Products | Healthy | 371 | 155 | 45 | 55.1 | 105 | 415 | 557 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1112 | 0 | 30 | 354.9 | 37 | 135 | 200 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2788 | 0 | 60 | 271.3 | 213 | 840 | 1056 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 167 | 0 | 14 | 27.7 | 35 | 126 | 252 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 556 | 0 | 60 | 588.7 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 597 | 2027 | 2247 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 31 | 0 | 30 | 52.6 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 500 | 1169 | 60 | 50.8 | 545 | 1146 | 1353 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 190 | 0 | 30 | 90.5 | 18 | 84 | 147 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 156 | 960 | 90 | 30.7 | 155 | 619 | 725 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1192 | 0 | 14 | 242.7 | 30 | 104 | 207 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 270 | 135 | 60 | 61.5 | 70 | 338 | 470 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 285 | 0 | 45 | 85.2 | 54 | 208 | 279 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 117 | 265 | 14 | 9.8 | 68 | 248 | 500 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 77 | 95 | 14 | 18.4 | 26 | 89 | 177 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 240 | 172 | 30 | 28.8 | 89 | 347 | 522 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 431 | 315 | 30 | 29.3 | 156 | 612 | 921 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4376 | 0 | 60 | 605.0 | 186 | 628 | 729 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 45.6 | 242 | 407 | 637 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 70 | 116 | 14 | 14.8 | 28 | 99 | 198 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 667 | 0 | 45 | 199.4 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 760 | 60 | 0.0 | 291 | 741 | 896 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 76 | 0 | 45 | 105.2 | 11 | 45 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 201 | 351 | 60 | 46.4 | 157 | 422 | 552 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 39 | 231 | 7 | 3.7 | 25 | 109 | 328 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 166 | 0 | 7 | 22.1 | 21 | 81 | 239 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4355 | 0 | 60 | 531.1 | 214 | 715 | 829 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 347 | 0 | 14 | 46.0 | 56 | 170 | 275 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 815 | 1680 | 90 | 44.5 | 693 | 2362 | 2618 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 100.5 | 429 | 781 | 1019 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 529 | 0 | 45 | 147.9 | 57 | 222 | 297 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 48 | 110 | 14 | 9.6 | 28 | 103 | 208 | 0 | 10 |
| ITEM-0062 | C - Slow Moving | Healthy | 77 | 0 | 30 | 52.1 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 549 | 0 | 14 | 85.0 | 37 | 134 | 270 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 339 | 310 | 60 | 60.9 | 231 | 571 | 688 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 722 | 525 | 60 | 59.5 | 250 | 991 | 1245 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 234 | 115 | 45 | 42.1 | 88 | 344 | 461 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 335 | 245 | 14 | 20.8 | 118 | 360 | 585 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 364 | 0 | 30 | 82.5 | 50 | 187 | 280 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 85 | 0 | 7 | 30.6 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 29.1 | 3 | 10 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 226 | 890 | 1118 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3473 | 0 | 90 | 801.5 | 132 | 527 | 618 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 66 | 0 | 14 | 31.8 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 37 | 26 | 45 | 39.6 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 336 | 0 | 7 | 168.0 | 6 | 22 | 82 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 455 | 265 | 45 | 39.9 | 179 | 704 | 943 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 525 | 0 | 45 | 233.9 | 28 | 132 | 199 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 325 | 558 | 90 | 46.6 | 215 | 850 | 997 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 192 | 0 | 7 | 16.9 | 28 | 119 | 358 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 799 | 0 | 14 | 71.1 | 65 | 234 | 470 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 33 | 337 | 60 | 13.9 | 50 | 196 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Stockout | 0 | 605 | 14 | 0.0 | 243 | 414 | 652 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 16 | 35 | 14 | 15.2 | 6 | 22 | 54 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Reorder | 250 | 0 | 45 | 57.3 | 53 | 254 | 385 | 135 | — |
| ITEM-0089 | A - Top Movers | Healthy | 523 | 468 | 14 | 28.4 | 457 | 734 | 991 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 30 | 50 | 30 | 19.7 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 654 | 1027 | 90 | 52.1 | 382 | 1525 | 1789 | 0 | 87 |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 35 | 104 | 7 | 7.1 | 14 | 54 | 157 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6796 | 0 | 90 | 373.2 | 691 | 2349 | 2604 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3600 | 0 | 60 | 251.9 | 365 | 1237 | 1437 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 47.6 | 104 | 155 | 286 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 89 | 0 | 7 | 16.1 | 16 | 61 | 176 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 132 | 0 | 14 | 40.3 | 19 | 69 | 137 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 65.9 | 642 | 1433 | 1614 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 207 | 0 | 45 | 108.3 | 24 | 112 | 170 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 366 | 180 | 45 | 49.2 | 118 | 460 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 877 | 1542 | 90 | 50.4 | 660 | 2244 | 2487 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 435 | 499 | 60 | 39.6 | 226 | 897 | 1128 | 0 | 62 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 269 | 1073 | 1259 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1601 | 220 | 90 | 115.3 | 533 | 1797 | 1992 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 395 | 1161 | 60 | 22.5 | 452 | 1525 | 1771 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1000 | 940 | 45 | 62.6 | 745 | 1480 | 1703 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 33 | 0 | 14 | 23.2 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 908 | 0 | 14 | 94.0 | 236 | 381 | 584 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 680 | 797 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 180 | 135 | 30 | 30.2 | 64 | 249 | 375 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 41 | 59 | 30 | 21.7 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 99 | 285 | 7 | 7.6 | 34 | 138 | 411 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 80 | 146 | 14 | 23.5 | 103 | 154 | 226 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 91 | 216 | 14 | 9.2 | 58 | 208 | 416 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 74 | 0 | 7 | 12.6 | 16 | 63 | 186 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 576 | 0 | 45 | 65.0 | 139 | 547 | 734 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 522 | 0 | 14 | 85.6 | 35 | 127 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 278 | 130 | 60 | 66.9 | 67 | 321 | 446 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 137 | 172 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3708 | 0 | 60 | 264.6 | 361 | 1216 | 1412 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 102.0 | 26 | 65 | 90 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 386 | 0 | 14 | 47.5 | 61 | 183 | 297 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 347 | 474 | 30 | 22.5 | 203 | 681 | 897 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1064 | 539 | 60 | 58.2 | 466 | 1581 | 1837 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2138 | 0 | 45 | 214.0 | 157 | 617 | 827 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1360 | 320 | 60 | 109.9 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 321 | 470 | 45 | 30.4 | 167 | 654 | 875 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 711 | 0 | 7 | 57.4 | 37 | 137 | 396 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 99 | 391 | 491 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 132 | 636 | 90 | 39.9 | 102 | 404 | 473 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 16.4 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 640 | 0 | 60 | 164.1 | 83 | 321 | 403 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 209 | 0 | 60 | 144.7 | 24 | 113 | 156 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 503 | 0 | 14 | 67.1 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 681 | 274 | 30 | 38.5 | 233 | 782 | 1030 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 15.1 | 301 | 472 | 770 | 0 | — |
