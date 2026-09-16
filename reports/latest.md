# Synthetic Inventory Health

**Simulation date: 2026-09-16**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 69 |
| Lead-time risk | 16 |
| Stockout | 25 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 504 | 756 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 268 | 0 | 7 | 47.6 | 84 | 130 | 248 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 899 | 517 | 60 | 58.3 | 393 | 1334 | 1550 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2015 | 0 | 45 | 312.7 | 104 | 401 | 536 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 267 | 0 | 14 | 35.9 | 43 | 155 | 311 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 141 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 266 | 0 | 14 | 31.6 | 53 | 180 | 357 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 58 | 198 | 60 | 28.1 | 35 | 162 | 224 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 142 | 410 | 90 | 45.5 | 98 | 383 | 448 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 418 | 0 | 90 | 150.5 | 66 | 319 | 403 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1168 | 0 | 7 | 91.9 | 32 | 134 | 401 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 181.3 | 23 | 36 | 83 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 35 | 235 | 45 | 11.5 | 85 | 226 | 318 | 0 | 12 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 411 | 551 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1209 | 0 | 30 | 242.9 | 58 | 213 | 317 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3160 | 0 | 60 | 295.6 | 220 | 873 | 1097 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 354 | 0 | 14 | 38.3 | 56 | 195 | 389 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 585 | 0 | 60 | 408.1 | 25 | 113 | 156 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 644 | 2190 | 2428 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 9 | 45 | 30 | 12.9 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 28 | 125 | 218 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 318 | 960 | 90 | 40.1 | 246 | 967 | 1134 | 0 | 41 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1344 | 0 | 14 | 176.1 | 46 | 161 | 321 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 315 | 437 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 395 | 0 | 45 | 75.3 | 86 | 328 | 438 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 290.9 | 79 | 225 | 297 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 342 | 0 | 14 | 31.5 | 62 | 225 | 453 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 134 | 300 | 7 | 13.3 | 141 | 222 | 434 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 209 | 0 | 14 | 31.9 | 40 | 139 | 276 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 85 | 333 | 501 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 149 | 574 | 862 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4618 | 0 | 60 | 404.7 | 298 | 995 | 1154 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 49.5 | 257 | 443 | 702 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 226 | 0 | 14 | 29.7 | 48 | 163 | 322 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1522 | 1742 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 794 | 0 | 45 | 235.8 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 58 | 145 | 188 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 24 | 80 | 45 | 23.2 | 15 | 63 | 94 | 0 | 24 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 129 | 290 | 369 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 227 | 0 | 7 | 22.8 | 27 | 107 | 317 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 161 | 0 | 7 | 22.3 | 20 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4622 | 0 | 60 | 380.2 | 320 | 1062 | 1232 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 585 | 0 | 14 | 52.0 | 89 | 258 | 416 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1511 | 865 | 90 | 84.7 | 676 | 2300 | 2550 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 459 | 946 | 1275 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 92 | 346 | 462 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 133 | 0 | 14 | 27.0 | 29 | 103 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 126 | 0 | 30 | 53.5 | 21 | 95 | 165 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 788 | 0 | 14 | 119.4 | 38 | 137 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1223 | 0 | 60 | 102.8 | 246 | 972 | 1222 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 455 | 0 | 45 | 80.0 | 89 | 351 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 473 | 0 | 14 | 27.6 | 123 | 381 | 621 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 118 | 390 | 30 | 16.9 | 79 | 296 | 442 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 18 | 90 | 7 | 6.5 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 105 | 104 | 45 | 38.4 | 77 | 203 | 285 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 20 | 0 | 7 | 23.7 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 234 | 921 | 1157 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3612 | 0 | 90 | 548.2 | 205 | 805 | 943 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 82 | 0 | 14 | 37.7 | 10 | 43 | 108 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 51 | 77 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 390 | 0 | 7 | 127.6 | 8 | 33 | 125 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 593 | 275 | 45 | 47.6 | 196 | 769 | 1031 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 607 | 0 | 45 | 246.1 | 30 | 144 | 218 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 588 | 393 | 90 | 83.5 | 215 | 857 | 1004 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 156 | 0 | 7 | 14.3 | 28 | 116 | 346 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1237 | 0 | 14 | 116.6 | 62 | 222 | 444 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 114 | 337 | 60 | 30.7 | 79 | 306 | 384 | 0 | 31 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 48 | 0 | 14 | 30.0 | 9 | 33 | 81 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 86 | 0 | 30 | 56.5 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1122 | 735 | 90 | 82.3 | 417 | 1658 | 1944 | 0 | 115 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 196 | 0 | 7 | 28.2 | 21 | 77 | 223 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7495 | 0 | 90 | 414.6 | 686 | 2332 | 2585 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4194 | 0 | 60 | 320.2 | 338 | 1138 | 1321 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 261 | 0 | 7 | 29.4 | 29 | 100 | 287 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 244 | 0 | 14 | 46.3 | 34 | 113 | 224 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 74.6 | 524 | 1279 | 1539 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 59 | 210 | 45 | 21.7 | 35 | 161 | 242 | 0 | 22 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 898 | 422 | 90 | 100.4 | 411 | 1225 | 1413 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 642 | 0 | 45 | 81.3 | 124 | 488 | 654 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1510 | 773 | 90 | 88.5 | 650 | 2204 | 2442 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 611 | 481 | 60 | 55.2 | 228 | 904 | 1136 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 181.9 | 66 | 162 | 255 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 198 | 915 | 90 | 22.2 | 272 | 1083 | 1271 | 0 | 23 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2217 | 0 | 90 | 150.0 | 562 | 1907 | 2114 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1077 | 622 | 60 | 60.8 | 455 | 1537 | 1785 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 29.6 | 829 | 1635 | 1880 | 0 | 30 |
| ITEM-0114 | C - Slow Moving | Healthy | 41 | 0 | 14 | 28.6 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 72.5 | 267 | 475 | 766 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 124 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 123 | 530 | 90 | 22.8 | 166 | 658 | 771 | 118 | 23 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 256 | 385 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 57 | 55 | 30 | 30.7 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 265 | 0 | 7 | 20.0 | 36 | 142 | 421 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 63.6 | 94 | 139 | 202 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 250 | 0 | 14 | 24.7 | 58 | 210 | 422 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 50 | 134 | 7 | 8.0 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 548 | 734 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 765 | 0 | 14 | 125.0 | 34 | 126 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 434 | 0 | 60 | 98.9 | 71 | 339 | 471 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4263 | 0 | 60 | 315.5 | 347 | 1172 | 1361 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 28 | 79 | 111 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 663 | 0 | 14 | 57.3 | 90 | 264 | 426 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 199 | 670 | 882 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1729 | 0 | 60 | 94.6 | 467 | 1582 | 1838 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2525 | 0 | 45 | 257.1 | 155 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 628 | 1542 | 1857 | 320 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 460 | 243 | 45 | 41.9 | 171 | 676 | 906 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1160 | 0 | 7 | 88.9 | 38 | 143 | 417 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 155 | 602 | 756 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 230 | 636 | 90 | 43.6 | 163 | 644 | 755 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 802 | 0 | 14 | 37.6 | 444 | 765 | 1063 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 137.8 | 230 | 395 | 625 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 584 | 178 | 60 | 95.9 | 130 | 502 | 630 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 58 | 200 | 60 | 28.1 | 35 | 162 | 224 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 811 | 0 | 14 | 117.9 | 41 | 145 | 289 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 243 | 808 | 1063 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 597 | 0 | 7 | 24.0 | 324 | 524 | 872 | 0 | — |
