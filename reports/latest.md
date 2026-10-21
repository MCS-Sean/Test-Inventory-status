# Synthetic Inventory Health

**Simulation date: 2026-10-21**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 91 |
| Lead-time risk | 3 |
| Reorder | 3 |
| Stockout | 12 |

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
| ITEM-0001 | B - Core Products | Healthy | 406 | 291 | 30 | 30.9 | 139 | 547 | 823 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 19.3 | 97 | 157 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 343 | 1184 | 60 | 22.5 | 391 | 1321 | 1534 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1892 | 0 | 45 | 415.3 | 73 | 283 | 379 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 176 | 0 | 14 | 24.6 | 42 | 150 | 300 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 119 | 0 | 45 | 74.9 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 75 | 145 | 14 | 12.0 | 38 | 132 | 264 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 213 | 0 | 60 | 158.4 | 23 | 106 | 146 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 88 | 410 | 90 | 43.3 | 64 | 250 | 292 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 787 | 1654 | 1852 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 322 | 90 | 90 | 109.8 | 69 | 336 | 424 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 711 | 0 | 7 | 55.9 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 174 | 0 | 7 | 102.4 | 23 | 37 | 88 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 399 | 155 | 45 | 59.4 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1117 | 0 | 30 | 334.0 | 39 | 143 | 213 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2816 | 0 | 60 | 267.3 | 218 | 861 | 1082 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 191 | 0 | 14 | 30.8 | 37 | 131 | 261 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 557 | 0 | 60 | 544.9 | 19 | 82 | 113 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 609 | 2068 | 2292 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 34 | 0 | 30 | 57.7 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 50.8 | 677 | 1278 | 1416 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 196 | 0 | 30 | 89.5 | 24 | 92 | 138 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 176 | 960 | 90 | 32.3 | 168 | 665 | 780 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 30 | 0 | 7 | 58.7 | 6 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1213 | 0 | 14 | 232.8 | 32 | 111 | 220 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 287 | 135 | 60 | 65.1 | 71 | 341 | 473 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 295 | 0 | 45 | 86.5 | 55 | 212 | 284 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 166 | 265 | 14 | 14.1 | 67 | 244 | 491 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 94 | 0 | 14 | 21.9 | 26 | 91 | 181 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 273 | 172 | 30 | 32.8 | 89 | 348 | 523 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 490 | 315 | 30 | 33.8 | 155 | 604 | 908 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4401 | 0 | 60 | 599.2 | 188 | 637 | 739 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 42.7 | 246 | 422 | 668 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 79 | 116 | 14 | 16.1 | 29 | 103 | 206 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 678 | 0 | 45 | 200.1 | 41 | 197 | 299 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 113 | 286 | 371 | 98 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 8 | 760 | 60 | 1.2 | 282 | 693 | 834 | 0 | 2 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 82.0 | 139 | 237 | 373 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 81 | 0 | 45 | 115.7 | 11 | 44 | 65 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 80 | 231 | 7 | 7.7 | 25 | 109 | 328 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 43 | 155 | 7 | 5.8 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4393 | 0 | 60 | 523.7 | 219 | 731 | 849 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 364 | 0 | 14 | 46.4 | 58 | 176 | 286 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 903 | 1680 | 90 | 49.0 | 698 | 2374 | 2632 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 79.1 | 471 | 918 | 1221 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 543 | 0 | 45 | 146.3 | 60 | 231 | 309 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 73 | 110 | 14 | 14.9 | 28 | 102 | 205 | 0 | 15 |
| ITEM-0062 | C - Slow Moving | Healthy | 83 | 0 | 30 | 55.3 | 14 | 61 | 106 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 572 | 0 | 14 | 87.6 | 37 | 135 | 273 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 339 | 310 | 60 | 60.9 | 231 | 571 | 688 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 770 | 260 | 60 | 63.6 | 250 | 989 | 1244 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 259 | 115 | 45 | 46.8 | 87 | 342 | 458 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 401 | 0 | 14 | 24.5 | 119 | 365 | 593 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 384 | 0 | 30 | 84.3 | 52 | 194 | 289 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 15 | 85 | 7 | 5.5 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 33.6 | 3 | 9 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 888 | 1116 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3492 | 0 | 90 | 789.6 | 135 | 538 | 631 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 15 | 61 | 14 | 7.4 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 43 | 26 | 45 | 47.8 | 13 | 55 | 82 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 341 | 0 | 7 | 163.2 | 6 | 23 | 86 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 512 | 265 | 45 | 44.1 | 183 | 718 | 961 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 536 | 0 | 45 | 243.6 | 27 | 129 | 195 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 350 | 558 | 90 | 50.0 | 215 | 852 | 999 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 241 | 0 | 7 | 21.6 | 27 | 117 | 351 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 850 | 0 | 14 | 75.4 | 65 | 234 | 471 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 42 | 337 | 60 | 17.4 | 51 | 199 | 249 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 197 | 205 | 14 | 21.5 | 216 | 354 | 547 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 21 | 35 | 14 | 20.3 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 269 | 0 | 45 | 62.4 | 53 | 252 | 381 | 0 | — |
| ITEM-0089 | A - Top Movers | Reorder | 523 | 0 | 14 | 28.4 | 457 | 734 | 991 | 468 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 36 | 50 | 30 | 23.6 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 702 | 1027 | 90 | 56.3 | 380 | 1516 | 1778 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Reorder | 54 | 0 | 7 | 10.9 | 14 | 54 | 158 | 104 | — |
| ITEM-0095 | A - Top Movers | Excess | 6873 | 0 | 90 | 377.9 | 691 | 2347 | 2601 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3654 | 0 | 60 | 256.7 | 365 | 1234 | 1433 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 73 | 225 | 7 | 11.2 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 109 | 0 | 7 | 19.3 | 17 | 63 | 181 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 145 | 0 | 14 | 42.2 | 21 | 73 | 145 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 65.9 | 642 | 1433 | 1614 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 215 | 0 | 45 | 112.5 | 24 | 112 | 170 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 390 | 180 | 45 | 52.4 | 118 | 461 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 961 | 1286 | 90 | 56.5 | 646 | 2193 | 2431 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 242 | 740 | 60 | 22.0 | 225 | 895 | 1126 | 0 | 66 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 266 | 1059 | 1242 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 108.3 | 135 | 422 | 562 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1700 | 220 | 90 | 124.8 | 521 | 1761 | 1952 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 454 | 1161 | 60 | 25.8 | 451 | 1524 | 1771 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 39 | 0 | 14 | 28.1 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 908 | 0 | 14 | 83.5 | 247 | 411 | 639 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 85 | 129 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 680 | 797 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 200 | 135 | 30 | 33.0 | 65 | 253 | 380 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 47 | 59 | 30 | 24.6 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Reorder | 134 | 0 | 7 | 10.2 | 34 | 140 | 417 | 285 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 96 | 92 | 14 | 33.5 | 65 | 108 | 194 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 120 | 216 | 14 | 11.8 | 59 | 212 | 425 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 99 | 0 | 7 | 16.7 | 16 | 64 | 188 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 624 | 0 | 45 | 70.3 | 139 | 548 | 734 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 557 | 0 | 14 | 92.7 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 294 | 130 | 60 | 70.4 | 67 | 322 | 448 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 29 | 136 | 171 | 40 | 1 |
| ITEM-0135 | B - Core Products | Excess | 3767 | 0 | 60 | 269.3 | 290 | 1144 | 1438 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 409 | 0 | 14 | 49.7 | 61 | 185 | 300 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 402 | 474 | 30 | 25.8 | 206 | 690 | 909 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1139 | 539 | 60 | 62.9 | 462 | 1567 | 1821 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2183 | 0 | 45 | 220.3 | 156 | 612 | 821 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 351 | 470 | 45 | 32.7 | 169 | 663 | 889 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 759 | 0 | 7 | 60.5 | 37 | 138 | 401 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 102 | 400 | 502 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 142 | 636 | 90 | 40.6 | 108 | 427 | 500 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 14.8 | 465 | 782 | 1078 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 105.5 | 240 | 405 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 656 | 0 | 60 | 163.1 | 85 | 331 | 415 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 16 | 200 | 60 | 11.1 | 24 | 113 | 156 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 539 | 0 | 14 | 72.4 | 43 | 155 | 311 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 742 | 274 | 30 | 41.1 | 238 | 798 | 1051 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 28.0 | 277 | 429 | 695 | 0 | — |
