# Synthetic Inventory Health

**Simulation date: 2026-11-04**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 94 |
| Lead-time risk | 3 |
| Reorder | 5 |
| Stockout | 9 |

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
| ITEM-0001 | B - Core Products | Healthy | 256 | 291 | 30 | 19.6 | 138 | 544 | 819 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 38.1 | 90 | 141 | 274 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 410 | 1107 | 60 | 26.7 | 394 | 1332 | 1547 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1837 | 0 | 45 | 460.5 | 63 | 247 | 331 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 220 | 0 | 14 | 30.7 | 42 | 150 | 300 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 104 | 0 | 45 | 70.4 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 140 | 0 | 14 | 25.0 | 32 | 117 | 234 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 194 | 0 | 60 | 150.5 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 64 | 410 | 90 | 35.6 | 56 | 220 | 258 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 289 | 90 | 90 | 104.5 | 66 | 318 | 401 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 501 | 0 | 7 | 38.2 | 34 | 139 | 415 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 81.4 | 77 | 190 | 263 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 311 | 155 | 45 | 47.4 | 103 | 406 | 543 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1081 | 0 | 30 | 380.0 | 32 | 121 | 180 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2672 | 0 | 60 | 252.9 | 218 | 863 | 1085 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 112 | 120 | 14 | 20.2 | 32 | 116 | 232 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 544 | 0 | 60 | 582.9 | 17 | 74 | 102 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 588 | 1992 | 2208 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 24 | 20 | 30 | 40.0 | 7 | 26 | 44 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 1128 | 452 | 60 | 107.9 | 559 | 1197 | 1417 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 174 | 0 | 30 | 88.5 | 17 | 78 | 137 | 0 | — |
| ITEM-0029 | B - Core Products | Excess | 1066 | 0 | 90 | 216.6 | 150 | 598 | 702 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 38.1 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1143 | 0 | 14 | 244.3 | 28 | 99 | 197 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 235 | 135 | 60 | 54.7 | 69 | 332 | 461 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 263 | 0 | 45 | 89.3 | 47 | 183 | 245 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 280 | 0 | 14 | 24.3 | 66 | 240 | 482 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 245 | 0 | 7 | 33.5 | 116 | 175 | 329 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 132 | 0 | 14 | 34.0 | 23 | 82 | 163 | 0 | — |
| ITEM-0038 | B - Core Products | Reorder | 164 | 172 | 30 | 19.8 | 89 | 346 | 519 | 183 | — |
| ITEM-0039 | B - Core Products | Reorder | 620 | 0 | 30 | 41.5 | 158 | 621 | 934 | 315 | — |
| ITEM-0040 | A - Top Movers | Excess | 4297 | 0 | 60 | 607.1 | 181 | 613 | 712 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 61.2 | 221 | 371 | 579 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 138 | 0 | 14 | 29.6 | 27 | 97 | 195 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 491 | 1280 | 1462 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 636 | 0 | 45 | 190.8 | 41 | 195 | 295 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 257 | 220 | 90 | 82.3 | 129 | 414 | 507 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 175 | 790 | 60 | 22.7 | 286 | 757 | 919 | 0 | 23 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 110.4 | 117 | 189 | 289 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 68 | 0 | 45 | 97.1 | 10 | 43 | 64 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 185 | 502 | 60 | 33.7 | 236 | 571 | 687 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 180 | 0 | 7 | 18.0 | 22 | 103 | 313 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 102 | 0 | 7 | 13.8 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4278 | 0 | 60 | 554.8 | 198 | 669 | 777 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 273 | 0 | 14 | 38.1 | 52 | 160 | 260 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 662 | 1950 | 90 | 36.4 | 689 | 2346 | 2600 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 486 | 0 | 45 | 137.1 | 56 | 220 | 294 | 0 | — |
| ITEM-0061 | B - Core Products | Stockout | 0 | 110 | 14 | 0.0 | 29 | 104 | 209 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 61 | 0 | 30 | 42.6 | 13 | 58 | 101 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 482 | 0 | 14 | 74.5 | 37 | 134 | 270 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 45.8 | 235 | 597 | 722 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 612 | 525 | 60 | 50.3 | 251 | 994 | 1249 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 170 | 246 | 45 | 30.5 | 88 | 345 | 462 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 404 | 0 | 14 | 24.1 | 121 | 373 | 607 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 320 | 0 | 30 | 78.3 | 45 | 172 | 258 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 68 | 0 | 7 | 25.3 | 6 | 28 | 109 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 352 | 0 | 45 | 118.7 | 81 | 218 | 307 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 23.2 | 3 | 9 | 30 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 997 | 0 | 60 | 88.8 | 233 | 919 | 1155 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3436 | 0 | 90 | 854.3 | 123 | 490 | 574 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 50 | 0 | 14 | 25.3 | 9 | 39 | 98 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 29 | 26 | 45 | 32.6 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 372 | 861 | 974 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 316 | 0 | 7 | 175.6 | 5 | 20 | 74 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 64 | 290 | 90 | 27.6 | 113 | 325 | 394 | 0 | 28 |
| ITEM-0079 | B - Core Products | Healthy | 340 | 515 | 45 | 30.6 | 175 | 687 | 921 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 499 | 0 | 45 | 223.4 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 268 | 705 | 90 | 39.2 | 211 | 833 | 977 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 71 | 250 | 7 | 6.0 | 29 | 124 | 371 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 705 | 0 | 14 | 63.6 | 64 | 231 | 463 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 345 | 0 | 60 | 153.0 | 47 | 185 | 232 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 101 | 400 | 14 | 8.1 | 252 | 440 | 702 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 42 | 0 | 14 | 43.0 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 209 | 135 | 45 | 49.0 | 53 | 250 | 378 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 21.5 | 365 | 639 | 1021 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 19 | 50 | 30 | 13.1 | 13 | 59 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 536 | 1027 | 90 | 42.5 | 383 | 1530 | 1795 | 0 | — |
| ITEM-0093 | A - Top Movers | Healthy | 598 | 0 | 7 | 32.9 | 318 | 464 | 718 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 90 | 0 | 7 | 19.2 | 12 | 50 | 148 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6608 | 0 | 90 | 362.6 | 690 | 2349 | 2604 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3490 | 0 | 60 | 253.9 | 352 | 1191 | 1383 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 237 | 0 | 7 | 49.7 | 89 | 128 | 228 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 43 | 115 | 7 | 8.5 | 15 | 56 | 161 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 104 | 0 | 14 | 33.5 | 18 | 65 | 130 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 621 | 1260 | 60 | 40.2 | 718 | 1662 | 1878 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 189 | 0 | 45 | 104.4 | 23 | 107 | 161 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 74.4 | 357 | 1061 | 1224 | 0 | — |
| ITEM-0105 | B - Core Products | Reorder | 284 | 180 | 45 | 37.8 | 119 | 465 | 623 | 160 | — |
| ITEM-0106 | A - Top Movers | Healthy | 718 | 1542 | 90 | 42.3 | 648 | 2194 | 2432 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 335 | 738 | 60 | 30.9 | 222 | 883 | 1111 | 0 | 54 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 262 | 1041 | 1221 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1446 | 445 | 90 | 99.4 | 556 | 1880 | 2084 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 209 | 1407 | 60 | 12.0 | 448 | 1515 | 1759 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 128.6 | 608 | 1132 | 1292 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 20 | 45 | 14 | 13.8 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 833 | 0 | 14 | 141.5 | 181 | 270 | 393 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 100 | 0 | 45 | 67.2 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 177 | 700 | 821 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 130 | 135 | 30 | 21.8 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 21 | 59 | 30 | 11.1 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 306 | 0 | 7 | 25.2 | 33 | 131 | 386 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 195 | 0 | 14 | 52.9 | 81 | 137 | 247 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 191 | 211 | 14 | 19.1 | 57 | 207 | 417 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 134 | 0 | 7 | 22.5 | 17 | 65 | 191 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 938 | 0 | 30 | 214.3 | 278 | 414 | 475 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 483 | 191 | 45 | 54.5 | 139 | 547 | 733 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 471 | 0 | 14 | 78.1 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 244 | 130 | 60 | 60.3 | 66 | 313 | 435 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3568 | 0 | 60 | 256.3 | 359 | 1209 | 1404 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 316 | 0 | 14 | 43.2 | 53 | 163 | 266 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 234 | 474 | 30 | 15.6 | 200 | 667 | 877 | 0 | — |
| ITEM-0140 | A - Top Movers | Reorder | 826 | 799 | 60 | 43.8 | 480 | 1630 | 1894 | 269 | — |
| ITEM-0141 | B - Core Products | Excess | 2033 | 0 | 45 | 209.3 | 153 | 600 | 804 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 86.3 | 619 | 1452 | 1738 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 425 | 463 | 45 | 38.8 | 173 | 678 | 908 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 556 | 0 | 7 | 44.1 | 38 | 139 | 404 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 90 | 358 | 449 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 107 | 636 | 90 | 34.8 | 95 | 376 | 440 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 686 | 385 | 14 | 38.4 | 430 | 698 | 948 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 602 | 0 | 60 | 163.7 | 77 | 302 | 379 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 739 | 400 | 90 | 251.0 | 241 | 509 | 571 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 196 | 0 | 60 | 143.4 | 23 | 107 | 148 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 443 | 0 | 14 | 61.7 | 42 | 150 | 301 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 514 | 274 | 30 | 29.6 | 230 | 769 | 1012 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Reorder | 314 | 0 | 7 | 14.1 | 321 | 500 | 812 | 498 | — |
