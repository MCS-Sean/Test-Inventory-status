# Synthetic Inventory Health

**Simulation date: 2026-09-20**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 66 |
| Lead-time risk | 14 |
| Reorder | 4 |
| Stockout | 26 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 497 | 747 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 175 | 0 | 7 | 26.2 | 95 | 149 | 289 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 853 | 517 | 60 | 55.9 | 390 | 1322 | 1535 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2002 | 0 | 45 | 324.1 | 100 | 385 | 514 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 233 | 0 | 14 | 31.1 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 141 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 236 | 0 | 14 | 29.0 | 50 | 172 | 343 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 51 | 198 | 60 | 26.4 | 33 | 151 | 209 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 137 | 410 | 90 | 47.8 | 89 | 350 | 411 | 0 | 48 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 10.6 | 774 | 1624 | 1819 | 0 | 11 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 94.6 | 337 | 495 | 770 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 406 | 0 | 90 | 143.9 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1113 | 0 | 7 | 87.9 | 33 | 135 | 401 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 234.0 | 20 | 30 | 67 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 11 | 235 | 45 | 4.0 | 80 | 208 | 292 | 0 | 4 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 412 | 552 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1198 | 0 | 30 | 253.1 | 55 | 202 | 302 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3115 | 0 | 60 | 291.1 | 220 | 873 | 1098 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 329 | 0 | 14 | 36.4 | 55 | 191 | 381 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 582 | 0 | 60 | 419.0 | 24 | 109 | 151 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 633 | 2151 | 2385 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 7 | 45 | 30 | 10.0 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 27 | 119 | 208 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 302 | 960 | 90 | 39.3 | 239 | 939 | 1101 | 0 | 40 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1329 | 0 | 14 | 182.9 | 44 | 153 | 306 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 317 | 441 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 386 | 0 | 45 | 77.9 | 82 | 310 | 415 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 290.9 | 79 | 225 | 297 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 302 | 0 | 14 | 27.7 | 62 | 226 | 455 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 16.5 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 200 | 0 | 14 | 32.8 | 37 | 129 | 257 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 88 | 343 | 515 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 150 | 581 | 873 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4589 | 0 | 60 | 421.4 | 285 | 950 | 1102 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 386 | 195 | 14 | 28.9 | 337 | 538 | 725 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 210 | 0 | 14 | 29.6 | 45 | 152 | 301 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 781 | 0 | 45 | 232.7 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 143 | 185 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 296 | 175 | 60 | 64.5 | 166 | 446 | 584 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 384 | 0 | 14 | 39.5 | 169 | 315 | 519 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 20 | 80 | 45 | 19.8 | 14 | 61 | 91 | 0 | 20 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 132 | 316 | 407 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 182 | 0 | 7 | 18.2 | 26 | 106 | 316 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 131 | 0 | 7 | 18.3 | 20 | 78 | 228 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4591 | 0 | 60 | 392.0 | 309 | 1024 | 1188 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 567 | 0 | 14 | 52.5 | 87 | 249 | 401 | 0 | — |
| ITEM-0056 | A - Top Movers | Reorder | 1449 | 865 | 90 | 80.5 | 681 | 2319 | 2571 | 260 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 509 | 1073 | 1455 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 88 | 331 | 442 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 110 | 0 | 14 | 22.5 | 28 | 102 | 204 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 120 | 0 | 30 | 52.9 | 20 | 91 | 159 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 762 | 0 | 14 | 115.3 | 37 | 137 | 275 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 518 | 310 | 60 | 73.1 | 272 | 705 | 854 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1165 | 0 | 60 | 96.9 | 248 | 982 | 1234 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 437 | 0 | 45 | 77.3 | 88 | 349 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 419 | 0 | 14 | 24.6 | 123 | 379 | 617 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 101 | 390 | 30 | 15.2 | 76 | 283 | 423 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 98 | 0 | 7 | 35.9 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 91 | 193 | 45 | 31.5 | 78 | 211 | 298 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 16 | 0 | 7 | 18.7 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 232 | 912 | 1145 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3597 | 0 | 90 | 567.0 | 197 | 775 | 908 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 76 | 0 | 14 | 35.8 | 10 | 42 | 106 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 387 | 0 | 7 | 134.0 | 8 | 32 | 118 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 544 | 275 | 45 | 43.8 | 195 | 766 | 1027 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 600 | 0 | 45 | 250.0 | 29 | 140 | 212 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 555 | 393 | 90 | 77.6 | 218 | 870 | 1020 | 0 | — |
| ITEM-0082 | B - Core Products | Reorder | 114 | 0 | 7 | 10.4 | 29 | 118 | 349 | 235 | — |
| ITEM-0083 | B - Core Products | Excess | 1197 | 0 | 14 | 112.0 | 62 | 223 | 447 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 107 | 337 | 60 | 31.0 | 74 | 285 | 358 | 0 | 31 |
| ITEM-0085 | B - Core Products | Reorder | 310 | 0 | 14 | 39.1 | 215 | 334 | 501 | 195 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 45 | 0 | 14 | 29.3 | 8 | 31 | 77 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 68 | 268 | 360 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 711 | 0 | 14 | 49.8 | 382 | 597 | 797 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 83 | 0 | 30 | 54.5 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1075 | 735 | 90 | 81.0 | 405 | 1613 | 1891 | 0 | 114 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 181 | 0 | 7 | 27.5 | 20 | 73 | 211 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7401 | 0 | 90 | 405.9 | 692 | 2352 | 2607 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4137 | 0 | 60 | 312.6 | 341 | 1149 | 1334 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 244 | 0 | 7 | 28.6 | 28 | 97 | 276 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 230 | 0 | 14 | 46.3 | 31 | 106 | 210 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 53 | 210 | 45 | 20.4 | 33 | 153 | 231 | 0 | 21 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 809 | 689 | 90 | 84.8 | 429 | 1298 | 1498 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 626 | 0 | 45 | 81.9 | 120 | 472 | 633 | 0 | — |
| ITEM-0106 | A - Top Movers | Reorder | 1437 | 773 | 90 | 83.0 | 659 | 2236 | 2478 | 268 | — |
| ITEM-0107 | B - Core Products | Healthy | 561 | 481 | 60 | 50.0 | 231 | 915 | 1151 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 172 | 915 | 90 | 19.6 | 269 | 1069 | 1254 | 0 | 20 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2146 | 0 | 90 | 144.6 | 564 | 1915 | 2123 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1010 | 622 | 60 | 57.3 | 452 | 1527 | 1774 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 37 | 0 | 14 | 25.8 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 72.5 | 267 | 475 | 766 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 123 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 99 | 648 | 90 | 18.2 | 167 | 662 | 776 | 0 | 19 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 250 | 376 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 43 | 55 | 30 | 22.1 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 203 | 0 | 7 | 14.9 | 36 | 145 | 431 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 212 | 401 | 487 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 212 | 0 | 14 | 21.1 | 58 | 209 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 29 | 134 | 7 | 4.7 | 17 | 67 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 18.3 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 138 | 546 | 733 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 128.0 | 655 | 1711 | 1955 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 749 | 0 | 14 | 124.8 | 34 | 124 | 250 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 409 | 0 | 60 | 90.0 | 73 | 351 | 487 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4202 | 0 | 60 | 307.5 | 350 | 1184 | 1375 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 28 | 79 | 111 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 628 | 0 | 14 | 56.5 | 85 | 252 | 408 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 203 | 683 | 899 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1661 | 0 | 60 | 90.0 | 470 | 1596 | 1855 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2491 | 0 | 45 | 251.3 | 156 | 612 | 821 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 628 | 1542 | 1857 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 396 | 479 | 45 | 35.0 | 177 | 698 | 935 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1102 | 0 | 7 | 84.5 | 39 | 144 | 418 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 152 | 591 | 742 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 219 | 636 | 90 | 43.4 | 156 | 616 | 721 | 0 | 44 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 37.6 | 358 | 679 | 1127 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 572 | 178 | 60 | 100.4 | 122 | 470 | 590 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 52 | 200 | 60 | 26.9 | 32 | 150 | 208 | 0 | 27 |
| ITEM-0155 | B - Core Products | Excess | 783 | 0 | 14 | 113.8 | 41 | 145 | 289 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 243 | 805 | 1058 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 481 | 367 | 7 | 19.9 | 315 | 509 | 848 | 0 | — |
