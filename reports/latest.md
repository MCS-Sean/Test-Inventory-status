# Synthetic Inventory Health

**Simulation date: 2026-10-29**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 97 |
| Lead-time risk | 3 |
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
| ITEM-0001 | B - Core Products | Healthy | 320 | 291 | 30 | 24.4 | 139 | 545 | 820 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 313 | 0 | 7 | 50.4 | 91 | 141 | 272 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 488 | 890 | 60 | 31.3 | 398 | 1348 | 1566 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1868 | 0 | 45 | 450.7 | 66 | 257 | 344 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 121 | 155 | 14 | 17.1 | 41 | 147 | 295 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 111 | 0 | 45 | 72.4 | 20 | 91 | 137 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 185 | 0 | 14 | 32.2 | 34 | 121 | 241 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 201 | 0 | 60 | 157.3 | 22 | 100 | 139 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 72 | 410 | 90 | 37.9 | 59 | 232 | 272 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1993 | 0 | 60 | 140.0 | 787 | 1656 | 1855 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1586 | 0 | 7 | 158.8 | 248 | 328 | 468 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 304 | 90 | 90 | 107.7 | 67 | 324 | 409 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 583 | 0 | 7 | 44.7 | 34 | 139 | 413 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 148 | 0 | 7 | 74.4 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 75.9 | 79 | 200 | 279 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 345 | 155 | 45 | 51.3 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1097 | 0 | 30 | 357.7 | 35 | 131 | 195 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2736 | 0 | 60 | 262.8 | 215 | 851 | 1069 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 147 | 0 | 14 | 25.5 | 34 | 121 | 242 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 551 | 0 | 60 | 576.6 | 18 | 77 | 105 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 587 | 1989 | 2204 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 30 | 0 | 30 | 52.9 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 411 | 1169 | 60 | 39.3 | 695 | 1334 | 1480 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 182 | 0 | 30 | 87.6 | 18 | 83 | 145 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 136 | 960 | 90 | 27.6 | 150 | 599 | 703 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1176 | 0 | 14 | 246.1 | 29 | 101 | 201 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 253 | 135 | 60 | 58.2 | 70 | 336 | 466 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 279 | 0 | 45 | 89.0 | 50 | 195 | 260 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 548.0 | 56 | 132 | 170 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 84 | 265 | 14 | 7.2 | 67 | 242 | 486 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 62 | 95 | 14 | 15.2 | 25 | 87 | 172 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 211 | 172 | 30 | 25.1 | 90 | 351 | 528 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 365 | 315 | 30 | 24.5 | 157 | 619 | 932 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4340 | 0 | 60 | 600.0 | 186 | 628 | 729 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 609 | 0 | 14 | 50.4 | 251 | 433 | 686 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 170 | 0 | 14 | 37.0 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 656 | 0 | 45 | 197.5 | 41 | 194 | 294 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 104.0 | 126 | 393 | 481 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 965 | 60 | 0.0 | 312 | 825 | 1001 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 73 | 0 | 45 | 104.3 | 10 | 43 | 64 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 172 | 351 | 60 | 36.9 | 161 | 445 | 585 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 227 | 0 | 7 | 22.0 | 23 | 106 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 141 | 0 | 7 | 18.9 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4332 | 0 | 60 | 558.6 | 201 | 675 | 783 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 315 | 0 | 14 | 42.5 | 55 | 167 | 270 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 762 | 1680 | 90 | 41.9 | 687 | 2341 | 2595 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1055 | 0 | 30 | 85.8 | 438 | 819 | 1078 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 510 | 0 | 45 | 140.8 | 58 | 225 | 301 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 29 | 110 | 14 | 5.9 | 28 | 102 | 205 | 0 | 6 |
| ITEM-0062 | C - Slow Moving | Healthy | 71 | 0 | 30 | 49.2 | 13 | 58 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 523 | 0 | 14 | 81.0 | 37 | 134 | 270 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 312 | 310 | 60 | 53.2 | 235 | 593 | 717 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 683 | 525 | 60 | 56.8 | 248 | 983 | 1235 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 210 | 246 | 45 | 37.6 | 88 | 345 | 462 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 288 | 245 | 14 | 17.7 | 118 | 363 | 591 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 345 | 0 | 30 | 80.9 | 48 | 181 | 270 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 79 | 0 | 7 | 28.3 | 6 | 29 | 112 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 33.1 | 90 | 253 | 359 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 20 | 0 | 7 | 27.3 | 3 | 9 | 31 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 231 | 911 | 1145 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3454 | 0 | 90 | 818.1 | 129 | 514 | 602 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 59 | 0 | 14 | 28.5 | 10 | 41 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 35 | 26 | 45 | 38.9 | 13 | 55 | 82 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 327 | 0 | 7 | 168.2 | 5 | 21 | 79 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 108 | 170 | 90 | 46.5 | 113 | 325 | 394 | 120 | 47 |
| ITEM-0079 | B - Core Products | Healthy | 400 | 515 | 45 | 35.0 | 179 | 705 | 946 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 515 | 0 | 45 | 230.6 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 299 | 558 | 90 | 42.8 | 215 | 851 | 998 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 158 | 0 | 7 | 13.9 | 28 | 119 | 357 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 748 | 0 | 14 | 66.5 | 65 | 234 | 470 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 24 | 337 | 60 | 10.4 | 49 | 190 | 239 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 205 | 400 | 14 | 18.1 | 243 | 414 | 652 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 14 | 35 | 14 | 13.7 | 6 | 22 | 52 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 228 | 135 | 45 | 51.8 | 54 | 257 | 389 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 391 | 468 | 14 | 19.7 | 377 | 676 | 1093 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 24 | 50 | 30 | 16.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 608 | 1027 | 90 | 49.0 | 378 | 1508 | 1769 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 307 | 485 | 7 | 18.1 | 243 | 379 | 736 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 118 | 0 | 7 | 24.7 | 13 | 52 | 152 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6730 | 0 | 90 | 370.5 | 689 | 2343 | 2597 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3573 | 0 | 60 | 255.8 | 358 | 1210 | 1406 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 56.0 | 96 | 139 | 251 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 75 | 0 | 7 | 14.2 | 16 | 59 | 169 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 117 | 0 | 14 | 35.3 | 20 | 70 | 140 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 66.3 | 642 | 1428 | 1608 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 200 | 0 | 45 | 108.4 | 23 | 108 | 164 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 82.9 | 369 | 1091 | 1258 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 331 | 180 | 45 | 43.9 | 120 | 467 | 625 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 828 | 1542 | 90 | 48.6 | 647 | 2198 | 2436 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 382 | 738 | 60 | 34.5 | 227 | 903 | 1136 | 0 | 57 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 267.9 | 52 | 111 | 168 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1065 | 1249 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1532 | 445 | 90 | 108.7 | 540 | 1823 | 2020 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 328 | 1407 | 60 | 18.9 | 445 | 1504 | 1746 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1465 | 475 | 45 | 125.9 | 609 | 1145 | 1307 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 29 | 45 | 14 | 20.6 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 833 | 0 | 14 | 84.3 | 239 | 388 | 595 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 110 | 0 | 45 | 74.4 | 19 | 87 | 132 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 173 | 684 | 802 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 160 | 135 | 30 | 27.0 | 64 | 248 | 372 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 33 | 59 | 30 | 17.6 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 362 | 0 | 7 | 28.5 | 34 | 136 | 403 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 49 | 146 | 14 | 13.3 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 39 | 216 | 14 | 3.9 | 58 | 208 | 418 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 53 | 132 | 7 | 9.1 | 16 | 63 | 185 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 533 | 191 | 45 | 60.2 | 138 | 546 | 732 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 92.2 | 723 | 1940 | 2221 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 505 | 0 | 14 | 83.4 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 258 | 130 | 60 | 61.9 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 137 | 172 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3641 | 0 | 60 | 261.5 | 359 | 1209 | 1404 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 66 | 43 | 45 | 63.2 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 359 | 0 | 14 | 46.5 | 57 | 173 | 281 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 299 | 474 | 30 | 19.6 | 202 | 675 | 888 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 982 | 799 | 60 | 53.6 | 467 | 1585 | 1842 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2100 | 0 | 45 | 213.8 | 155 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1178 | 635 | 60 | 81.8 | 630 | 1509 | 1811 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 259 | 470 | 45 | 24.1 | 170 | 665 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 638 | 0 | 7 | 50.7 | 38 | 139 | 404 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 97 | 383 | 481 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 124 | 636 | 90 | 38.9 | 98 | 389 | 456 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 697 | 385 | 14 | 36.7 | 438 | 723 | 989 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 625 | 0 | 60 | 166.4 | 79 | 309 | 387 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 799 | 400 | 90 | 248.0 | 263 | 557 | 624 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 204 | 0 | 60 | 145.7 | 24 | 110 | 152 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 480 | 0 | 14 | 65.1 | 43 | 154 | 309 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 608 | 274 | 30 | 34.3 | 233 | 783 | 1031 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 322 | 448 | 7 | 17.2 | 286 | 436 | 699 | 0 | — |
