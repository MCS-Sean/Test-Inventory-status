# Synthetic Inventory Health

**Simulation date: 2026-09-24**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 71 |
| Lead-time risk | 12 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 127 | 493 | 741 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 116 | 195 | 7 | 15.8 | 98 | 157 | 311 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 751 | 737 | 60 | 48.0 | 400 | 1355 | 1574 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1989 | 0 | 45 | 337.8 | 96 | 367 | 491 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 210 | 0 | 14 | 28.1 | 43 | 156 | 313 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 221 | 0 | 14 | 27.7 | 50 | 170 | 337 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 46 | 198 | 60 | 25.1 | 31 | 143 | 198 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 129 | 410 | 90 | 46.6 | 86 | 338 | 396 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 8.4 | 755 | 1565 | 1750 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 94.6 | 337 | 495 | 770 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 396 | 0 | 90 | 138.7 | 68 | 328 | 414 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1046 | 0 | 7 | 81.4 | 33 | 136 | 406 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 270 | 0 | 7 | 227.1 | 19 | 29 | 65 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 82 | 217 | 305 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 410 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1188 | 0 | 30 | 261.4 | 53 | 194 | 290 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3087 | 0 | 60 | 294.0 | 216 | 857 | 1077 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 308 | 0 | 14 | 35.8 | 53 | 183 | 363 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 577 | 0 | 60 | 425.7 | 24 | 107 | 148 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 627 | 2126 | 2356 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 49 | 0 | 30 | 71.1 | 8 | 30 | 51 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 26 | 115 | 201 | 0 | 1 |
| ITEM-0029 | B - Core Products | Healthy | 289 | 960 | 90 | 39.5 | 228 | 895 | 1049 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1314 | 0 | 14 | 184.5 | 43 | 150 | 300 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 66 | 319 | 444 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 376 | 0 | 45 | 80.8 | 77 | 292 | 389 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 309.7 | 77 | 214 | 282 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 237 | 0 | 14 | 21.0 | 64 | 233 | 470 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 184 | 0 | 14 | 31.7 | 36 | 123 | 245 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 479 | 0 | 30 | 58.2 | 88 | 344 | 517 | 0 | — |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 149 | 577 | 867 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4564 | 0 | 60 | 439.8 | 272 | 906 | 1051 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 386 | 195 | 14 | 28.9 | 337 | 538 | 725 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 199 | 0 | 14 | 30.0 | 42 | 142 | 281 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 615 | 1692 | 1941 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 767 | 0 | 45 | 227.1 | 42 | 198 | 299 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 125.8 | 129 | 412 | 505 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 57 | 140 | 181 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 40 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 313 | 240 | 14 | 33.2 | 164 | 306 | 504 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 17 | 80 | 45 | 17.0 | 14 | 60 | 90 | 0 | 18 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 138 | 0 | 7 | 13.6 | 25 | 107 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 93 | 0 | 7 | 12.8 | 20 | 79 | 232 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4567 | 0 | 60 | 415.6 | 290 | 961 | 1115 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 542 | 0 | 14 | 52.6 | 84 | 239 | 384 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1391 | 1125 | 90 | 77.6 | 678 | 2309 | 2560 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 51.6 | 479 | 961 | 1288 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 82 | 308 | 412 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 87 | 110 | 14 | 17.4 | 29 | 104 | 209 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 113 | 0 | 30 | 51.9 | 20 | 88 | 153 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 732 | 0 | 14 | 109.4 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1103 | 0 | 60 | 90.1 | 252 | 999 | 1257 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 409 | 0 | 45 | 71.8 | 89 | 352 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 344 | 245 | 14 | 20.4 | 122 | 375 | 611 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 475 | 0 | 30 | 74.6 | 73 | 271 | 405 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 85 | 0 | 7 | 30.7 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 58 | 193 | 45 | 17.8 | 84 | 234 | 332 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 12 | 0 | 7 | 14.6 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 229 | 900 | 1131 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3581 | 0 | 90 | 588.1 | 189 | 744 | 871 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 69 | 0 | 14 | 33.2 | 10 | 42 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 54 | 81 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 382 | 0 | 7 | 137.5 | 7 | 30 | 113 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 510 | 275 | 45 | 41.8 | 192 | 754 | 1011 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 591 | 0 | 45 | 247.4 | 29 | 139 | 211 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 532 | 393 | 90 | 74.2 | 219 | 872 | 1022 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 63 | 235 | 7 | 5.7 | 28 | 117 | 350 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1152 | 0 | 14 | 106.0 | 63 | 226 | 455 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 100 | 337 | 60 | 31.2 | 68 | 264 | 331 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 43 | 0 | 14 | 29.5 | 8 | 30 | 74 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 263 | 353 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 533 | 347 | 14 | 32.8 | 408 | 652 | 880 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 78 | 0 | 30 | 52.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1030 | 735 | 90 | 77.6 | 405 | 1613 | 1891 | 0 | 111 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 50.6 | 231 | 350 | 662 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 163 | 0 | 7 | 25.4 | 20 | 72 | 206 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7344 | 0 | 90 | 406.0 | 687 | 2334 | 2587 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4065 | 0 | 60 | 302.1 | 347 | 1168 | 1357 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 62.0 | 92 | 135 | 246 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 227 | 0 | 7 | 28.9 | 25 | 88 | 253 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 218 | 0 | 14 | 46.6 | 29 | 100 | 198 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 48 | 210 | 45 | 19.5 | 31 | 145 | 219 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 773 | 689 | 90 | 81.5 | 427 | 1291 | 1490 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 592 | 0 | 45 | 77.4 | 121 | 473 | 634 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1382 | 1041 | 90 | 80.9 | 651 | 2207 | 2446 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 523 | 481 | 60 | 46.8 | 230 | 912 | 1146 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 131 | 1100 | 90 | 14.9 | 268 | 1068 | 1253 | 0 | 15 |
| ITEM-0110 | C - Slow Moving | Excess | 668 | 0 | 60 | 206.6 | 111 | 309 | 406 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2086 | 0 | 90 | 143.0 | 554 | 1882 | 2086 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 946 | 622 | 60 | 53.9 | 451 | 1523 | 1769 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 32 | 0 | 14 | 22.5 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 83 | 125 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 81 | 648 | 90 | 15.2 | 165 | 652 | 764 | 0 | 16 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 250 | 376 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 35 | 55 | 30 | 18.0 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Reorder | 145 | 0 | 7 | 10.7 | 36 | 145 | 431 | 290 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 168 | 216 | 14 | 16.4 | 59 | 213 | 428 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 143 | 0 | 7 | 23.7 | 17 | 66 | 192 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 941 | 200 | 30 | 114.1 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 551 | 739 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 131.8 | 649 | 1675 | 1911 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 732 | 0 | 14 | 126.2 | 33 | 120 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 389 | 0 | 60 | 85.4 | 73 | 351 | 488 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 114 | 144 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4135 | 0 | 60 | 296.8 | 357 | 1207 | 1402 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 27 | 72 | 101 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 599 | 0 | 14 | 56.0 | 82 | 243 | 393 | 0 | — |
| ITEM-0139 | A - Top Movers | Stockout | 0 | 787 | 30 | 0.0 | 204 | 688 | 906 | 0 | 1 |
| ITEM-0140 | A - Top Movers | Reorder | 1586 | 0 | 60 | 86.0 | 471 | 1597 | 1855 | 269 | — |
| ITEM-0141 | B - Core Products | Excess | 2451 | 0 | 45 | 248.4 | 155 | 609 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 376 | 479 | 45 | 34.3 | 173 | 678 | 909 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1045 | 0 | 7 | 79.8 | 39 | 144 | 419 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 143 | 556 | 698 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 210 | 636 | 90 | 44.8 | 145 | 572 | 671 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 155.2 | 218 | 364 | 569 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 737 | 0 | 60 | 135.4 | 116 | 449 | 563 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 45 | 200 | 60 | 23.8 | 32 | 148 | 204 | 0 | 24 |
| ITEM-0155 | B - Core Products | Excess | 746 | 0 | 14 | 107.1 | 41 | 146 | 292 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 242 | 804 | 1057 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 391 | 367 | 7 | 15.5 | 318 | 520 | 873 | 0 | — |
