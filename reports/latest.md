# Synthetic Inventory Health

**Simulation date: 2026-11-03**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 95 |
| Lead-time risk | 2 |
| Reorder | 3 |
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
| ITEM-0001 | B - Core Products | Healthy | 266 | 291 | 30 | 20.2 | 139 | 547 | 824 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 420 | 1107 | 60 | 27.3 | 394 | 1333 | 1548 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1842 | 0 | 45 | 455.4 | 65 | 252 | 336 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 77 | 155 | 14 | 10.9 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 106 | 0 | 45 | 72.3 | 19 | 87 | 131 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 150 | 0 | 14 | 26.8 | 32 | 116 | 234 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 195 | 0 | 60 | 151.3 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 66 | 410 | 90 | 36.9 | 56 | 219 | 257 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 291 | 90 | 90 | 103.9 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 513 | 0 | 7 | 38.9 | 34 | 140 | 417 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 316 | 155 | 45 | 48.4 | 102 | 403 | 540 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1081 | 0 | 30 | 374.2 | 33 | 123 | 184 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2692 | 0 | 60 | 256.7 | 217 | 857 | 1078 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 115 | 120 | 14 | 20.5 | 33 | 118 | 236 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 546 | 0 | 60 | 599.3 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 596 | 2019 | 2238 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Reorder | 25 | 0 | 30 | 41.7 | 7 | 26 | 44 | 20 | — |
| ITEM-0027 | B - Core Products | Healthy | 1128 | 452 | 60 | 107.9 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 175 | 0 | 30 | 88.0 | 17 | 79 | 139 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1069 | 0 | 90 | 214.3 | 152 | 606 | 711 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 38.1 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1149 | 0 | 14 | 241.6 | 29 | 101 | 201 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 236 | 135 | 60 | 54.9 | 69 | 332 | 461 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 267 | 0 | 45 | 90.7 | 47 | 183 | 245 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 677 | 0 | 60 | 846.2 | 44 | 93 | 117 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 284 | 0 | 14 | 24.3 | 67 | 243 | 488 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 33.5 | 116 | 175 | 329 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 41 | 95 | 14 | 10.5 | 23 | 82 | 163 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 178 | 172 | 30 | 21.7 | 88 | 343 | 515 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 634 | 0 | 30 | 42.9 | 157 | 616 | 927 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4303 | 0 | 60 | 603.2 | 183 | 619 | 718 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 51.0 | 251 | 430 | 681 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 145 | 0 | 14 | 31.5 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 640 | 0 | 45 | 192.0 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 257 | 220 | 90 | 75.8 | 135 | 444 | 546 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 286 | 757 | 919 | 0 | 23 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 69 | 0 | 45 | 98.6 | 10 | 43 | 64 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 190 | 0 | 7 | 19.0 | 22 | 103 | 313 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 110 | 0 | 7 | 14.7 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4286 | 0 | 60 | 555.0 | 198 | 670 | 778 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 281 | 0 | 14 | 39.3 | 52 | 160 | 260 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 672 | 1950 | 90 | 36.9 | 689 | 2346 | 2600 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 490 | 0 | 45 | 136.1 | 58 | 224 | 300 | 0 | — |
| ITEM-0061 | B - Core Products | Stockout | 0 | 110 | 14 | 0.0 | 29 | 105 | 210 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 64 | 0 | 30 | 45.4 | 13 | 57 | 100 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 487 | 0 | 14 | 74.8 | 37 | 135 | 272 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 281 | 470 | 60 | 48.2 | 234 | 590 | 713 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 626 | 525 | 60 | 51.6 | 250 | 990 | 1245 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 174 | 246 | 45 | 30.9 | 89 | 349 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 422 | 0 | 14 | 25.3 | 121 | 372 | 606 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 324 | 0 | 30 | 78.4 | 46 | 175 | 261 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 69 | 0 | 7 | 25.5 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 352 | 0 | 45 | 118.7 | 81 | 218 | 307 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 22.9 | 3 | 9 | 30 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 1011 | 0 | 60 | 89.8 | 233 | 920 | 1156 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3441 | 0 | 90 | 850.8 | 124 | 493 | 577 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 52 | 0 | 14 | 26.4 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 30 | 26 | 45 | 34.2 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 319 | 0 | 7 | 175.1 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 64 | 290 | 90 | 27.6 | 113 | 325 | 394 | 0 | 28 |
| ITEM-0079 | B - Core Products | Healthy | 357 | 515 | 45 | 32.2 | 174 | 685 | 917 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 501 | 0 | 45 | 223.2 | 28 | 132 | 199 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 271 | 705 | 90 | 39.5 | 212 | 837 | 982 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 87 | 250 | 7 | 7.4 | 28 | 122 | 368 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 715 | 0 | 14 | 64.4 | 65 | 232 | 465 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 348 | 0 | 60 | 152.0 | 48 | 188 | 236 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 42 | 0 | 14 | 43.0 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 210 | 135 | 45 | 48.5 | 53 | 253 | 383 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 21 | 50 | 30 | 14.4 | 13 | 59 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 550 | 1027 | 90 | 43.6 | 383 | 1531 | 1796 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 598 | 0 | 7 | 32.9 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 93 | 0 | 7 | 19.7 | 12 | 50 | 149 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6638 | 0 | 90 | 367.6 | 684 | 2328 | 2580 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3505 | 0 | 60 | 255.4 | 352 | 1190 | 1382 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 57.6 | 96 | 138 | 247 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 45 | 115 | 7 | 8.8 | 15 | 56 | 164 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 105 | 0 | 14 | 33.4 | 18 | 66 | 132 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 40.2 | 718 | 1662 | 1878 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 191 | 0 | 45 | 104.8 | 23 | 107 | 162 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 74.4 | 357 | 1061 | 1224 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 290 | 180 | 45 | 38.7 | 119 | 464 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 746 | 1542 | 90 | 44.1 | 645 | 2185 | 2422 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 344 | 738 | 60 | 31.8 | 222 | 882 | 1109 | 0 | 55 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1044 | 1224 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1475 | 445 | 90 | 103.1 | 547 | 1850 | 2050 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 221 | 1407 | 60 | 12.6 | 449 | 1518 | 1763 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 20 | 45 | 14 | 13.6 | 7 | 29 | 73 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 833 | 0 | 14 | 133.9 | 182 | 276 | 406 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 102 | 0 | 45 | 68.5 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 176 | 697 | 817 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 133 | 135 | 30 | 22.3 | 64 | 249 | 375 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 23 | 59 | 30 | 12.2 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 320 | 0 | 7 | 26.0 | 34 | 133 | 392 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Reorder | 204 | 0 | 14 | 20.5 | 57 | 207 | 415 | 211 | — |
| ITEM-0125 | B - Core Products | Healthy | 139 | 0 | 7 | 23.2 | 17 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 214.3 | 278 | 414 | 475 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 494 | 191 | 45 | 56.0 | 138 | 544 | 730 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 475 | 0 | 14 | 78.9 | 34 | 125 | 251 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 246 | 130 | 60 | 60.3 | 66 | 315 | 438 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 133 | 167 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3585 | 0 | 60 | 259.2 | 357 | 1201 | 1395 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 320 | 0 | 14 | 43.4 | 54 | 165 | 268 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 242 | 474 | 30 | 16.1 | 200 | 667 | 877 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 850 | 799 | 60 | 45.3 | 478 | 1623 | 1885 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2044 | 0 | 45 | 209.3 | 154 | 604 | 809 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 86.3 | 619 | 1452 | 1738 | 0 | — |
| ITEM-0143 | B - Core Products | Reorder | 441 | 234 | 45 | 40.4 | 172 | 675 | 904 | 229 | — |
| ITEM-0144 | B - Core Products | Healthy | 567 | 0 | 7 | 45.2 | 38 | 139 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 91 | 361 | 454 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 107 | 636 | 90 | 34.5 | 96 | 379 | 444 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 39.3 | 430 | 696 | 945 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 605 | 0 | 60 | 163.0 | 78 | 305 | 383 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 739 | 400 | 90 | 251.0 | 241 | 509 | 571 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 197 | 0 | 60 | 141.8 | 24 | 109 | 151 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 452 | 0 | 14 | 63.0 | 42 | 150 | 301 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 522 | 274 | 30 | 29.7 | 233 | 778 | 1024 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 521 | 0 | 7 | 24.2 | 308 | 481 | 782 | 0 | — |
