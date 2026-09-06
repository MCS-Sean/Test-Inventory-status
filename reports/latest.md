# Synthetic Inventory Health

**Simulation date: 2026-09-06**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 62 |
| Lead-time risk | 28 |
| Reorder | 2 |
| Stockout | 19 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 501 | 753 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 307 | 0 | 7 | 44.1 | 99 | 155 | 301 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1037 | 294 | 60 | 67.5 | 392 | 1330 | 1545 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2056 | 0 | 45 | 293.7 | 113 | 435 | 582 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 333 | 0 | 14 | 44.3 | 43 | 156 | 314 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 95 | 143 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 319 | 0 | 14 | 33.2 | 61 | 205 | 407 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 68 | 198 | 60 | 29.0 | 39 | 183 | 253 | 0 | 30 |
| ITEM-0010 | B - Core Products | Lead-time risk | 158 | 410 | 90 | 43.9 | 112 | 440 | 516 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 447 | 0 | 90 | 159.6 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1296 | 0 | 7 | 101.5 | 33 | 136 | 404 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 413 | 554 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1236 | 0 | 30 | 221.2 | 63 | 237 | 354 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3274 | 0 | 60 | 321.3 | 211 | 833 | 1047 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 89 | 323 | 14 | 8.8 | 61 | 213 | 424 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 593 | 0 | 60 | 370.6 | 27 | 125 | 173 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 30 | 2305 | 90 | 1.8 | 651 | 2211 | 2450 | 0 | 2 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 18.0 | 8 | 31 | 53 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1161 | 717 | 60 | 104.5 | 773 | 1451 | 1607 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 31 | 140 | 244 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 364 | 960 | 90 | 41.6 | 271 | 1068 | 1252 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 32 | 0 | 7 | 68.6 | 6 | 10 | 24 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1384 | 0 | 14 | 153.0 | 54 | 190 | 380 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 63 | 299 | 415 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 423 | 0 | 45 | 68.8 | 102 | 385 | 514 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 722 | 0 | 60 | 306.5 | 76 | 220 | 291 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 454 | 0 | 14 | 41.7 | 62 | 226 | 454 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 326 | 0 | 7 | 41.0 | 127 | 191 | 358 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 232 | 0 | 14 | 31.3 | 43 | 155 | 311 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 84 | 330 | 496 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 84 | 575 | 30 | 6.1 | 149 | 580 | 871 | 0 | 7 |
| ITEM-0040 | A - Top Movers | Excess | 4682 | 0 | 60 | 354.1 | 345 | 1152 | 1337 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 37.4 | 284 | 530 | 873 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 277 | 0 | 14 | 33.1 | 53 | 179 | 355 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 830 | 0 | 45 | 246.5 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 171.8 | 116 | 349 | 426 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 379 | 175 | 60 | 85.3 | 172 | 444 | 577 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 482 | 0 | 14 | 47.7 | 183 | 335 | 547 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 29 | 80 | 45 | 24.2 | 16 | 72 | 108 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 327 | 0 | 7 | 32.0 | 28 | 110 | 325 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 232 | 0 | 7 | 31.5 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4697 | 0 | 60 | 336.3 | 368 | 1220 | 1416 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 661 | 0 | 14 | 53.6 | 98 | 283 | 456 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1733 | 580 | 90 | 98.8 | 666 | 2263 | 2509 | 0 | 99 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 8 | 564 | 45 | 1.3 | 105 | 397 | 530 | 0 | 2 |
| ITEM-0061 | B - Core Products | Lead-time risk | 12 | 145 | 14 | 2.4 | 29 | 103 | 206 | 0 | 3 |
| ITEM-0062 | C - Slow Moving | Healthy | 141 | 0 | 30 | 51.6 | 25 | 110 | 192 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 851 | 0 | 14 | 127.0 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 83.4 | 264 | 681 | 824 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1341 | 0 | 60 | 113.3 | 245 | 967 | 1216 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 509 | 0 | 45 | 89.0 | 90 | 354 | 474 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 663 | 0 | 14 | 39.5 | 122 | 374 | 609 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 147 | 390 | 30 | 18.6 | 88 | 333 | 499 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 43 | 0 | 7 | 15.0 | 7 | 30 | 116 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 30 | 0 | 7 | 36.0 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 238 | 941 | 1182 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3646 | 0 | 90 | 496.4 | 227 | 896 | 1050 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 107 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 49 | 72 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 409 | 0 | 7 | 117.6 | 9 | 37 | 142 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.5 | 104 | 286 | 346 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 700 | 275 | 45 | 55.2 | 198 | 782 | 1049 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 631 | 0 | 45 | 257.0 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 667 | 235 | 90 | 97.0 | 210 | 836 | 981 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 284 | 0 | 7 | 26.1 | 28 | 115 | 344 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1372 | 0 | 14 | 131.6 | 61 | 218 | 437 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 136 | 337 | 60 | 32.1 | 91 | 350 | 439 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 56 | 0 | 14 | 31.9 | 9 | 36 | 88 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 49 | 735 | 14 | 3.5 | 379 | 588 | 784 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 99 | 0 | 30 | 63.6 | 14 | 63 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1251 | 436 | 90 | 95.2 | 404 | 1601 | 1877 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.2 | 248 | 387 | 749 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 242 | 0 | 7 | 31.5 | 26 | 88 | 249 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7685 | 0 | 90 | 426.4 | 686 | 2327 | 2579 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4344 | 0 | 60 | 328.0 | 343 | 1151 | 1337 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 307 | 0 | 7 | 31.5 | 32 | 110 | 315 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 36 | 124 | 247 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 84.9 | 539 | 1320 | 1588 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 73 | 210 | 45 | 24.0 | 38 | 179 | 270 | 0 | 24 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 103.3 | 420 | 1264 | 1458 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 718 | 0 | 45 | 90.0 | 125 | 492 | 660 | 0 | — |
| ITEM-0106 | A - Top Movers | Reorder | 1692 | 524 | 90 | 98.3 | 657 | 2224 | 2465 | 249 | — |
| ITEM-0107 | B - Core Products | Healthy | 729 | 241 | 60 | 67.8 | 223 | 880 | 1105 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 226.3 | 61 | 144 | 223 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 281 | 915 | 90 | 30.5 | 281 | 1119 | 1312 | 0 | 31 |
| ITEM-0110 | C - Slow Moving | Excess | 714 | 0 | 60 | 262.3 | 103 | 270 | 351 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2306 | 0 | 90 | 150.1 | 581 | 1980 | 2195 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1308 | 360 | 60 | 76.1 | 442 | 1491 | 1732 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 1 | 55 | 14 | 0.7 | 8 | 31 | 75 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 59.3 | 298 | 552 | 908 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 82 | 123 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 178 | 530 | 90 | 32.5 | 168 | 667 | 782 | 0 | 33 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 65 | 254 | 381 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 79 | 0 | 30 | 43.4 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 391 | 0 | 7 | 29.5 | 36 | 143 | 421 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 42 | 292 | 14 | 4.0 | 60 | 218 | 438 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 119 | 0 | 7 | 19.3 | 17 | 67 | 196 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 549 | 736 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Reorder | 1485 | 419 | 90 | 113.1 | 711 | 1907 | 2182 | 278 | — |
| ITEM-0131 | B - Core Products | Excess | 833 | 0 | 14 | 134.1 | 34 | 128 | 258 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 480 | 0 | 60 | 114.3 | 68 | 325 | 451 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 4 | 135 | 90 | 4.4 | 23 | 106 | 134 | 0 | 5 |
| ITEM-0135 | A - Top Movers | Excess | 4382 | 0 | 60 | 321.9 | 349 | 1180 | 1370 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 721 | 0 | 14 | 54.3 | 102 | 302 | 488 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 144 | 560 | 30 | 9.7 | 195 | 654 | 861 | 0 | 10 |
| ITEM-0140 | A - Top Movers | Healthy | 1933 | 0 | 60 | 106.3 | 465 | 1574 | 1829 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2626 | 0 | 45 | 267.7 | 154 | 606 | 812 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 584 | 1375 | 1647 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 580 | 243 | 45 | 53.4 | 169 | 669 | 897 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1306 | 0 | 7 | 102.2 | 37 | 140 | 408 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 17 | 888 | 60 | 2.1 | 175 | 680 | 854 | 0 | 3 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 258 | 636 | 90 | 43.4 | 183 | 724 | 849 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Stockout | 0 | 995 | 14 | 0.0 | 422 | 705 | 968 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1664 | 0 | 14 | 149.8 | 236 | 403 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 617 | 178 | 60 | 86.9 | 151 | 585 | 734 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 126.6 | 436 | 1105 | 1259 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 69 | 200 | 60 | 30.0 | 38 | 179 | 248 | 0 | 31 |
| ITEM-0155 | B - Core Products | Excess | 884 | 0 | 14 | 126.7 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 128 | 671 | 30 | 7.1 | 241 | 804 | 1058 | 259 | 8 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 498 | 0 | 7 | 22.2 | 305 | 485 | 798 | 0 | — |
