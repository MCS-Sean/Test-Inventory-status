# Synthetic Inventory Health

**Simulation date: 2026-11-19**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 25 |
| Healthy | 99 |
| Lead-time risk | 5 |
| Reorder | 3 |
| Stockout | 6 |

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
| ITEM-0001 | B - Core Products | Healthy | 379 | 302 | 30 | 29.2 | 138 | 541 | 814 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 107 | 190 | 7 | 15.5 | 94 | 150 | 294 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 397 | 1107 | 60 | 25.7 | 396 | 1338 | 1554 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1770 | 0 | 45 | 459.1 | 62 | 240 | 321 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 128 | 150 | 14 | 18.7 | 41 | 144 | 288 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 78 | 46 | 45 | 52.8 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 32 | 125 | 14 | 5.6 | 41 | 127 | 207 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 172 | 0 | 60 | 132.3 | 22 | 102 | 141 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 436 | 0 | 90 | 229.5 | 59 | 232 | 272 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 253 | 90 | 90 | 96.5 | 63 | 302 | 381 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 296 | 0 | 7 | 22.2 | 34 | 141 | 421 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 214 | 300 | 45 | 33.2 | 101 | 398 | 533 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1027 | 0 | 30 | 359.6 | 32 | 121 | 181 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2520 | 0 | 60 | 237.7 | 220 | 867 | 1090 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 130 | 0 | 14 | 23.6 | 32 | 115 | 230 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 525 | 0 | 60 | 543.1 | 17 | 76 | 105 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2263 | 0 | 90 | 144.9 | 599 | 2021 | 2240 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 18 | 20 | 30 | 35.2 | 7 | 23 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 143 | 0 | 30 | 75.7 | 21 | 80 | 120 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 980 | 0 | 90 | 200.0 | 149 | 595 | 698 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 4 | 30 | 7 | 6.3 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1057 | 0 | 14 | 230.9 | 27 | 96 | 192 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 175 | 265 | 60 | 41.3 | 68 | 327 | 454 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 210 | 0 | 45 | 72.1 | 47 | 181 | 243 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 364 | 0 | 14 | 31.8 | 66 | 238 | 479 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 67 | 90 | 14 | 17.9 | 23 | 80 | 158 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 191 | 183 | 30 | 22.6 | 90 | 352 | 530 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 412 | 315 | 30 | 27.4 | 159 | 626 | 942 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4169 | 0 | 60 | 602.3 | 178 | 601 | 698 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 686 | 0 | 14 | 53.5 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 62 | 100 | 14 | 13.6 | 27 | 96 | 192 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 593 | 0 | 45 | 185.3 | 39 | 187 | 283 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 65.1 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 60 | 0 | 45 | 93.1 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 263 | 0 | 7 | 26.9 | 23 | 102 | 307 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 151 | 0 | 7 | 20.5 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4119 | 0 | 60 | 517.0 | 204 | 690 | 802 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 160 | 0 | 14 | 23.4 | 50 | 153 | 249 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 456 | 1950 | 90 | 26.8 | 647 | 2198 | 2436 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1010 | 0 | 30 | 86.3 | 428 | 791 | 1037 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 422 | 0 | 45 | 119.4 | 56 | 219 | 293 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 35 | 105 | 14 | 6.8 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 33 | 43 | 30 | 22.5 | 14 | 60 | 104 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 407 | 0 | 14 | 67.1 | 36 | 127 | 255 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 215 | 470 | 60 | 46.1 | 199 | 484 | 582 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 376 | 790 | 60 | 30.0 | 259 | 1024 | 1287 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 83 | 367 | 45 | 14.5 | 90 | 353 | 473 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 195 | 245 | 14 | 11.9 | 121 | 368 | 598 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 236 | 0 | 30 | 58.5 | 44 | 170 | 254 | 0 | — |
| ITEM-0069 | C - Slow Moving | Reorder | 26 | 0 | 7 | 9.8 | 6 | 28 | 107 | 85 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 7 | 25 | 7 | 10.9 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 821 | 249 | 60 | 72.7 | 233 | 922 | 1159 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3367 | 0 | 90 | 873.3 | 118 | 469 | 550 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 16 | 60 | 14 | 8.0 | 9 | 39 | 99 | 0 | 9 |
| ITEM-0075 | C - Slow Moving | Healthy | 44 | 28 | 45 | 47.7 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 523 | 1342 | 1531 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 283 | 0 | 7 | 158.2 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 144 | 454 | 556 | 0 | 1 |
| ITEM-0079 | B - Core Products | Reorder | 156 | 515 | 45 | 14.1 | 173 | 681 | 913 | 245 | — |
| ITEM-0080 | C - Slow Moving | Excess | 459 | 0 | 45 | 200.5 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 308 | 699 | 90 | 43.0 | 220 | 873 | 1023 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 151 | 0 | 7 | 13.1 | 29 | 122 | 365 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 582 | 0 | 14 | 55.1 | 61 | 220 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 295 | 0 | 60 | 124.6 | 50 | 195 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 23 | 0 | 14 | 24.1 | 6 | 21 | 49 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 256 | 137 | 45 | 57.2 | 56 | 262 | 397 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 46.3 | 460 | 752 | 1023 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 45 | 45 | 30 | 30.9 | 13 | 59 | 102 | 0 | 31 |
| ITEM-0092 | B - Core Products | Healthy | 354 | 1289 | 90 | 28.4 | 379 | 1514 | 1776 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 204 | 475 | 7 | 10.1 | 283 | 446 | 871 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 112 | 0 | 7 | 24.7 | 12 | 49 | 144 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6361 | 0 | 90 | 348.9 | 689 | 2349 | 2604 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3293 | 0 | 60 | 239.0 | 354 | 1195 | 1388 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.5 | 72 | 104 | 186 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 76 | 0 | 7 | 15.9 | 13 | 52 | 152 | 0 | — |
| ITEM-0100 | B - Core Products | Reorder | 58 | 0 | 14 | 19.8 | 17 | 61 | 123 | 65 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 77.9 | 641 | 1503 | 1701 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 155 | 0 | 45 | 89.4 | 22 | 102 | 154 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 187 | 340 | 45 | 26.5 | 113 | 439 | 587 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1049 | 1265 | 90 | 64.0 | 626 | 2118 | 2347 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 411 | 498 | 60 | 37.5 | 224 | 893 | 1123 | 0 | 38 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1048 | 1229 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1239 | 665 | 90 | 84.6 | 559 | 1892 | 2097 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 291 | 1292 | 60 | 16.3 | 457 | 1548 | 1798 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 47 | 0 | 14 | 33.6 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 246.0 | 92 | 138 | 202 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 78 | 50 | 45 | 50.1 | 19 | 91 | 138 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 517 | 242 | 90 | 90.9 | 176 | 694 | 814 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 156 | 125 | 30 | 25.8 | 65 | 253 | 380 | 0 | 26 |
| ITEM-0120 | C - Slow Moving | Healthy | 47 | 58 | 30 | 24.5 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 104 | 255 | 7 | 8.7 | 30 | 126 | 378 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 1000 | 45 | 0.0 | 362 | 800 | 1000 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 49.4 | 77 | 128 | 229 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 287 | 0 | 14 | 30.7 | 55 | 195 | 391 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 41 | 133 | 7 | 6.6 | 17 | 67 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 375 | 191 | 45 | 43.4 | 136 | 534 | 715 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1202 | 1042 | 90 | 111.8 | 623 | 1602 | 1828 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 397 | 0 | 14 | 68.1 | 34 | 122 | 244 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 181 | 255 | 60 | 44.5 | 66 | 315 | 437 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3373 | 0 | 60 | 250.1 | 346 | 1169 | 1358 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 183 | 0 | 14 | 25.8 | 51 | 158 | 257 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 494 | 238 | 30 | 33.4 | 195 | 654 | 860 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 833 | 799 | 60 | 44.8 | 473 | 1607 | 1867 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1861 | 0 | 45 | 183.0 | 159 | 627 | 841 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 939 | 635 | 60 | 63.6 | 650 | 1551 | 1860 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 278 | 463 | 45 | 26.1 | 168 | 659 | 882 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 394 | 0 | 7 | 32.6 | 33 | 130 | 384 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 801 | 0 | 60 | 177.6 | 93 | 369 | 463 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 59 | 636 | 90 | 21.2 | 86 | 339 | 398 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 73.8 | 310 | 525 | 825 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 531 | 0 | 60 | 148.4 | 75 | 294 | 369 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 169 | 0 | 60 | 124.7 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 330 | 0 | 14 | 44.7 | 42 | 153 | 308 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 498 | 514 | 30 | 28.0 | 236 | 788 | 1037 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
