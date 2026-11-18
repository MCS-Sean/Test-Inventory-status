# Synthetic Inventory Health

**Simulation date: 2026-11-18**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 25 |
| Healthy | 97 |
| Lead-time risk | 5 |
| Reorder | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 398 | 302 | 30 | 30.9 | 137 | 537 | 807 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 107 | 190 | 7 | 15.5 | 94 | 150 | 294 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 419 | 1107 | 60 | 27.2 | 394 | 1333 | 1549 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1779 | 0 | 45 | 464.1 | 61 | 238 | 318 | 0 | — |
| ITEM-0006 | B - Core Products | Reorder | 139 | 0 | 14 | 20.4 | 40 | 143 | 286 | 150 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 79 | 46 | 45 | 53.5 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 44 | 125 | 14 | 7.8 | 40 | 125 | 205 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 174 | 0 | 60 | 135.0 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 440 | 0 | 90 | 235.7 | 58 | 228 | 268 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 256 | 90 | 90 | 97.2 | 63 | 303 | 382 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 323 | 0 | 7 | 24.6 | 33 | 139 | 415 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 218 | 300 | 45 | 33.6 | 102 | 401 | 537 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1031 | 0 | 30 | 363.9 | 32 | 120 | 180 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2531 | 0 | 60 | 239.0 | 219 | 865 | 1088 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 137 | 0 | 14 | 25.0 | 32 | 115 | 230 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 526 | 0 | 60 | 550.5 | 17 | 76 | 104 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2280 | 0 | 90 | 145.7 | 600 | 2024 | 2243 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 18 | 20 | 30 | 34.5 | 7 | 24 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 146 | 0 | 30 | 77.3 | 21 | 80 | 120 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 986 | 0 | 90 | 202.1 | 148 | 592 | 695 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 4 | 30 | 7 | 6.3 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1060 | 0 | 14 | 229.3 | 27 | 97 | 194 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 178 | 265 | 60 | 42.0 | 68 | 327 | 454 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 215 | 0 | 45 | 73.9 | 47 | 181 | 243 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 130 | 245 | 14 | 11.4 | 66 | 237 | 476 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Reorder | 72 | 0 | 14 | 19.1 | 23 | 80 | 159 | 90 | — |
| ITEM-0038 | B - Core Products | Healthy | 27 | 355 | 30 | 3.2 | 90 | 352 | 530 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 416 | 315 | 30 | 27.5 | 160 | 630 | 948 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4181 | 0 | 60 | 605.9 | 177 | 598 | 695 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 351 | 335 | 14 | 27.4 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 63 | 100 | 14 | 13.7 | 27 | 97 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 598 | 0 | 45 | 189.5 | 39 | 185 | 279 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 65.1 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 60 | 0 | 45 | 91.5 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 268 | 0 | 7 | 27.3 | 23 | 102 | 309 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 156 | 0 | 7 | 21.3 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4130 | 0 | 60 | 521.3 | 203 | 687 | 798 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 173 | 0 | 14 | 25.7 | 50 | 152 | 246 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 469 | 1950 | 90 | 27.6 | 645 | 2190 | 2428 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1018 | 0 | 30 | 80.2 | 439 | 833 | 1100 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 422 | 0 | 45 | 118.7 | 56 | 220 | 295 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 38 | 105 | 14 | 7.4 | 29 | 106 | 214 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 35 | 43 | 30 | 24.0 | 13 | 59 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 409 | 0 | 14 | 66.9 | 36 | 128 | 256 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 215 | 470 | 60 | 46.1 | 199 | 484 | 582 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 389 | 790 | 60 | 31.2 | 258 | 1020 | 1282 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 90 | 367 | 45 | 16.0 | 89 | 349 | 467 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 222 | 245 | 14 | 13.6 | 120 | 364 | 592 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 240 | 0 | 30 | 59.2 | 45 | 171 | 256 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 29 | 0 | 7 | 11.0 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 8 | 25 | 7 | 12.2 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 836 | 249 | 60 | 74.5 | 232 | 917 | 1153 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3370 | 0 | 90 | 871.6 | 118 | 470 | 552 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 17 | 60 | 14 | 8.5 | 9 | 40 | 100 | 0 | 9 |
| ITEM-0075 | C - Slow Moving | Healthy | 45 | 28 | 45 | 49.4 | 13 | 55 | 83 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 477 | 1186 | 1350 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 285 | 0 | 7 | 159.3 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 140 | 430 | 525 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 166 | 515 | 45 | 15.1 | 173 | 680 | 911 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 463 | 0 | 45 | 203.3 | 28 | 133 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Reorder | 317 | 547 | 90 | 44.6 | 219 | 867 | 1016 | 152 | — |
| ITEM-0082 | B - Core Products | Healthy | 167 | 0 | 7 | 14.5 | 29 | 121 | 363 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 593 | 0 | 14 | 56.5 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 300 | 0 | 60 | 128.0 | 49 | 193 | 242 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 23 | 0 | 14 | 23.8 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 256 | 137 | 45 | 56.7 | 56 | 264 | 399 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 974 | 0 | 14 | 52.4 | 456 | 735 | 995 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 46 | 45 | 30 | 31.4 | 13 | 59 | 103 | 0 | 32 |
| ITEM-0092 | B - Core Products | Healthy | 379 | 1289 | 90 | 30.9 | 372 | 1489 | 1746 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 353 | 475 | 7 | 19.0 | 275 | 424 | 815 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 117 | 0 | 7 | 25.6 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6376 | 0 | 90 | 349.5 | 690 | 2351 | 2606 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3303 | 0 | 60 | 239.3 | 355 | 1197 | 1390 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.5 | 72 | 104 | 186 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 80 | 0 | 7 | 16.6 | 14 | 53 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 63 | 0 | 14 | 21.6 | 17 | 61 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 157 | 0 | 45 | 90.6 | 22 | 102 | 154 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 192 | 340 | 45 | 26.8 | 115 | 445 | 595 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1072 | 1265 | 90 | 65.5 | 626 | 2117 | 2346 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 428 | 498 | 60 | 38.9 | 225 | 896 | 1127 | 0 | 39 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1048 | 1229 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1251 | 665 | 90 | 85.6 | 558 | 1889 | 2094 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 307 | 1292 | 60 | 17.3 | 454 | 1536 | 1784 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 49 | 0 | 14 | 35.3 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 153.6 | 144 | 218 | 320 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 80 | 50 | 45 | 52.2 | 19 | 90 | 136 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 521 | 242 | 90 | 91.8 | 175 | 692 | 811 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 167 | 125 | 30 | 27.8 | 65 | 252 | 378 | 0 | 28 |
| ITEM-0120 | C - Slow Moving | Healthy | 48 | 58 | 30 | 24.8 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Reorder | 120 | 0 | 7 | 10.1 | 30 | 125 | 375 | 255 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 362 | 800 | 1000 | 206 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 49.4 | 77 | 128 | 229 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 297 | 0 | 14 | 31.9 | 55 | 195 | 391 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 48 | 133 | 7 | 7.7 | 17 | 67 | 197 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 379 | 191 | 45 | 44.0 | 135 | 532 | 713 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1202 | 1042 | 90 | 111.8 | 623 | 1602 | 1828 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 397 | 0 | 14 | 66.9 | 34 | 123 | 248 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 183 | 255 | 60 | 45.1 | 66 | 314 | 436 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 132 | 166 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3391 | 0 | 60 | 250.2 | 348 | 1175 | 1365 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 60.0 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 186 | 0 | 14 | 26.1 | 51 | 158 | 258 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 511 | 238 | 30 | 34.4 | 197 | 658 | 866 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 846 | 799 | 60 | 45.1 | 478 | 1624 | 1887 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1874 | 0 | 45 | 184.7 | 159 | 626 | 839 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 985 | 635 | 60 | 69.1 | 645 | 1514 | 1814 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 283 | 463 | 45 | 26.5 | 168 | 659 | 883 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 405 | 0 | 7 | 33.0 | 35 | 134 | 392 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 808 | 0 | 60 | 181.8 | 92 | 364 | 457 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 65 | 636 | 90 | 23.5 | 85 | 337 | 395 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 538 | 0 | 60 | 150.4 | 75 | 294 | 369 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 171 | 0 | 60 | 127.2 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 338 | 0 | 14 | 46.0 | 42 | 153 | 307 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Reorder | 521 | 259 | 30 | 29.3 | 235 | 786 | 1035 | 255 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
