# Synthetic Inventory Health

**Simulation date: 2026-09-23**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 69 |
| Lead-time risk | 12 |
| Reorder | 2 |
| Stockout | 27 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 496 | 744 | 0 | 1 |
| ITEM-0002 | B - Core Products | Reorder | 116 | 0 | 7 | 15.8 | 98 | 157 | 311 | 195 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 783 | 737 | 60 | 51.0 | 392 | 1330 | 1545 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1991 | 0 | 45 | 331.2 | 97 | 374 | 500 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 223 | 0 | 14 | 30.0 | 43 | 155 | 311 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 226 | 0 | 14 | 28.4 | 50 | 170 | 337 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 47 | 198 | 60 | 25.6 | 31 | 143 | 198 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 130 | 410 | 90 | 46.2 | 87 | 343 | 402 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 8.4 | 755 | 1565 | 1750 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 94.6 | 337 | 495 | 770 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 400 | 0 | 90 | 140.1 | 68 | 328 | 414 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1065 | 0 | 7 | 82.7 | 33 | 137 | 407 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 282.9 | 18 | 27 | 57 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 82 | 217 | 305 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 103 | 407 | 545 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1189 | 0 | 30 | 256.0 | 54 | 198 | 296 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3093 | 0 | 60 | 292.4 | 218 | 864 | 1086 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 314 | 0 | 14 | 36.1 | 53 | 184 | 367 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 578 | 0 | 60 | 426.4 | 24 | 107 | 148 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 633 | 2149 | 2382 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 50 | 0 | 30 | 73.8 | 8 | 30 | 50 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 26 | 116 | 202 | 0 | 1 |
| ITEM-0029 | B - Core Products | Healthy | 293 | 960 | 90 | 39.8 | 229 | 899 | 1053 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1318 | 0 | 14 | 184.2 | 43 | 151 | 301 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 319 | 444 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 378 | 0 | 45 | 79.5 | 79 | 298 | 398 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 309.7 | 77 | 214 | 282 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 256 | 0 | 14 | 22.9 | 63 | 231 | 467 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 188 | 0 | 14 | 31.9 | 36 | 125 | 248 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 88 | 345 | 519 | 0 | — |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 149 | 579 | 869 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4568 | 0 | 60 | 433.7 | 276 | 919 | 1066 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 386 | 195 | 14 | 28.9 | 337 | 538 | 725 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 203 | 0 | 14 | 30.1 | 43 | 144 | 286 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 615 | 1692 | 1941 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 770 | 0 | 45 | 228.7 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 140 | 181 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 40 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 313 | 240 | 14 | 33.2 | 164 | 306 | 504 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 18 | 80 | 45 | 18.0 | 14 | 60 | 90 | 0 | 19 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 149 | 0 | 7 | 14.9 | 26 | 107 | 317 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 103 | 0 | 7 | 14.2 | 20 | 79 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4573 | 0 | 60 | 411.6 | 293 | 971 | 1127 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 548 | 0 | 14 | 52.0 | 86 | 245 | 392 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1402 | 1125 | 90 | 77.9 | 681 | 2319 | 2571 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 488 | 1001 | 1348 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 84 | 316 | 422 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 91 | 110 | 14 | 18.3 | 29 | 104 | 209 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 114 | 0 | 30 | 51.6 | 20 | 89 | 155 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 739 | 0 | 14 | 111.8 | 38 | 138 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 63.9 | 279 | 738 | 895 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1120 | 0 | 60 | 92.5 | 250 | 989 | 1244 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 416 | 0 | 45 | 73.6 | 88 | 349 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 361 | 245 | 14 | 21.4 | 122 | 376 | 612 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 481 | 0 | 30 | 75.4 | 73 | 271 | 405 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 88 | 0 | 7 | 31.8 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 58 | 193 | 45 | 17.8 | 84 | 234 | 332 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 14 | 0 | 7 | 17.0 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 230 | 904 | 1136 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3585 | 0 | 90 | 579.3 | 192 | 756 | 886 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 71 | 0 | 14 | 34.2 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 53 | 79 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 384 | 0 | 7 | 138.2 | 7 | 30 | 113 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 511 | 275 | 45 | 41.1 | 194 | 766 | 1027 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 593 | 0 | 45 | 247.1 | 29 | 140 | 212 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 540 | 393 | 90 | 75.9 | 217 | 865 | 1014 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 75 | 235 | 7 | 6.7 | 28 | 118 | 351 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1162 | 0 | 14 | 107.0 | 63 | 226 | 454 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 101 | 337 | 60 | 31.0 | 69 | 268 | 336 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 44 | 0 | 14 | 30.2 | 8 | 30 | 74 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 265 | 356 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Reorder | 533 | 0 | 14 | 32.8 | 408 | 652 | 880 | 347 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 80 | 0 | 30 | 53.3 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1050 | 735 | 90 | 79.3 | 404 | 1610 | 1888 | 0 | 113 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 50.6 | 231 | 350 | 662 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 167 | 0 | 7 | 26.0 | 20 | 72 | 206 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7354 | 0 | 90 | 405.1 | 689 | 2342 | 2596 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4086 | 0 | 60 | 304.9 | 345 | 1163 | 1350 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 229 | 0 | 7 | 28.7 | 25 | 89 | 257 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 221 | 0 | 14 | 46.1 | 30 | 102 | 203 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 49 | 210 | 45 | 19.7 | 32 | 147 | 222 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 773 | 689 | 90 | 80.5 | 428 | 1302 | 1504 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 606 | 0 | 45 | 79.9 | 120 | 470 | 629 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1392 | 1041 | 90 | 81.2 | 653 | 2214 | 2454 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 530 | 481 | 60 | 47.1 | 232 | 919 | 1155 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 142 | 915 | 90 | 16.3 | 266 | 1059 | 1242 | 185 | 17 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2103 | 0 | 90 | 143.6 | 556 | 1889 | 2094 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 969 | 622 | 60 | 55.4 | 449 | 1516 | 1760 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 33 | 0 | 14 | 23.2 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 73.3 | 267 | 473 | 760 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 124 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 81 | 648 | 90 | 15.0 | 166 | 658 | 771 | 0 | 16 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 249 | 375 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 37 | 55 | 30 | 18.9 | 17 | 78 | 137 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 168 | 0 | 7 | 12.5 | 36 | 144 | 427 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 223 | 440 | 539 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 183 | 216 | 14 | 18.1 | 58 | 210 | 423 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 147 | 0 | 7 | 24.4 | 17 | 66 | 192 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 941 | 200 | 30 | 114.1 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 553 | 741 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 128.0 | 655 | 1711 | 1955 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 738 | 0 | 14 | 127.2 | 33 | 120 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 394 | 0 | 60 | 86.1 | 74 | 354 | 491 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 115 | 145 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4141 | 0 | 60 | 294.8 | 359 | 1216 | 1413 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 27 | 73 | 103 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 610 | 0 | 14 | 56.5 | 83 | 245 | 396 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 205 | 690 | 909 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Healthy | 1610 | 0 | 60 | 88.1 | 467 | 1582 | 1838 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2457 | 0 | 45 | 248.2 | 156 | 612 | 820 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 376 | 479 | 45 | 34.1 | 173 | 681 | 913 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1055 | 0 | 7 | 80.3 | 39 | 145 | 420 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 146 | 567 | 712 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 212 | 636 | 90 | 44.7 | 146 | 578 | 678 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 741 | 0 | 60 | 134.2 | 118 | 455 | 571 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 47 | 200 | 60 | 24.7 | 32 | 148 | 205 | 0 | 25 |
| ITEM-0155 | B - Core Products | Excess | 757 | 0 | 14 | 109.4 | 41 | 145 | 291 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 240 | 795 | 1046 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 391 | 367 | 7 | 15.5 | 318 | 520 | 873 | 0 | — |
