# Synthetic Inventory Health

**Simulation date: 2026-09-27**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 77 |
| Lead-time risk | 12 |
| Reorder | 1 |
| Stockout | 21 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 130 | 504 | 757 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 37 | 195 | 7 | 4.5 | 104 | 170 | 342 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 719 | 737 | 60 | 46.2 | 398 | 1348 | 1566 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1977 | 0 | 45 | 350.3 | 91 | 351 | 470 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 185 | 0 | 14 | 24.4 | 43 | 157 | 317 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 93 | 140 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 203 | 0 | 14 | 26.3 | 49 | 165 | 327 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 44 | 198 | 60 | 25.1 | 30 | 138 | 190 | 0 | — |
| ITEM-0010 | B - Core Products | Lead-time risk | 123 | 410 | 90 | 46.5 | 82 | 323 | 379 | 0 | 47 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.5 | 705 | 1417 | 1580 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 388 | 0 | 90 | 134.8 | 68 | 330 | 417 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1021 | 0 | 7 | 80.3 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 244 | 0 | 7 | 175.7 | 21 | 33 | 74 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 77 | 198 | 277 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 411 | 550 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1179 | 0 | 30 | 272.8 | 51 | 185 | 276 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3043 | 0 | 60 | 287.1 | 218 | 865 | 1088 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 292 | 0 | 14 | 35.4 | 51 | 175 | 349 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 574 | 0 | 60 | 430.5 | 23 | 105 | 145 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 611 | 2074 | 2298 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 70.8 | 8 | 30 | 50 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 240 | 0 | 30 | 86.7 | 25 | 111 | 194 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 279 | 960 | 90 | 39.9 | 218 | 855 | 1002 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1303 | 0 | 14 | 190.7 | 41 | 144 | 287 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 67 | 320 | 445 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 371 | 0 | 45 | 86.1 | 71 | 270 | 360 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 351.4 | 72 | 193 | 252 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 182 | 245 | 14 | 15.8 | 66 | 240 | 482 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 173 | 0 | 14 | 30.9 | 35 | 119 | 237 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 459 | 0 | 30 | 56.0 | 88 | 343 | 515 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 567 | 290 | 30 | 40.7 | 151 | 583 | 876 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4553 | 0 | 60 | 470.5 | 253 | 844 | 979 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 299 | 465 | 14 | 20.9 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 183 | 0 | 14 | 27.4 | 42 | 142 | 282 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 633 | 1776 | 2040 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 757 | 0 | 45 | 225.6 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 73 | 184 | 238 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 16 | 80 | 45 | 16.6 | 14 | 59 | 88 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 110 | 0 | 7 | 10.9 | 25 | 107 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Reorder | 78 | 0 | 7 | 10.9 | 20 | 78 | 229 | 155 | — |
| ITEM-0054 | A - Top Movers | Excess | 4551 | 0 | 60 | 413.7 | 290 | 961 | 1115 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 527 | 0 | 14 | 53.4 | 80 | 228 | 367 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1332 | 1125 | 90 | 72.9 | 690 | 2353 | 2608 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 54.0 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 81 | 303 | 405 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 75 | 110 | 14 | 15.1 | 29 | 104 | 208 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 109 | 0 | 30 | 51.9 | 19 | 85 | 148 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 717 | 0 | 14 | 106.7 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1058 | 0 | 60 | 85.2 | 255 | 1013 | 1273 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 397 | 0 | 45 | 71.2 | 87 | 344 | 461 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 291 | 245 | 14 | 17.4 | 121 | 373 | 607 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 463 | 0 | 30 | 77.0 | 69 | 256 | 382 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 77 | 0 | 7 | 27.8 | 7 | 30 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Lead-time risk | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | 8 |
| ITEM-0071 | C - Slow Moving | Healthy | 10 | 25 | 7 | 12.5 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 228 | 895 | 1125 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3573 | 0 | 90 | 611.3 | 182 | 714 | 837 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 64 | 0 | 14 | 31.0 | 10 | 41 | 104 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 53 | 79 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 377 | 0 | 7 | 140.8 | 7 | 29 | 109 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Healthy | 476 | 275 | 45 | 39.4 | 190 | 747 | 1000 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 585 | 0 | 45 | 248.3 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 515 | 393 | 90 | 72.6 | 217 | 863 | 1011 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 270 | 0 | 7 | 24.0 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1116 | 0 | 14 | 103.3 | 63 | 225 | 452 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 95 | 337 | 60 | 30.9 | 66 | 254 | 319 | 0 | 31 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 41 | 0 | 14 | 29.3 | 8 | 29 | 71 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 265 | 356 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 297 | 702 | 14 | 18.0 | 417 | 665 | 897 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 74 | 0 | 30 | 49.0 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 980 | 735 | 90 | 73.3 | 408 | 1625 | 1906 | 0 | 106 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 50.6 | 231 | 350 | 662 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 152 | 0 | 7 | 25.0 | 18 | 67 | 195 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7290 | 0 | 90 | 396.7 | 697 | 2370 | 2627 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4020 | 0 | 60 | 299.3 | 347 | 1167 | 1355 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 217 | 0 | 7 | 28.7 | 24 | 85 | 244 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 209 | 0 | 14 | 46.8 | 28 | 95 | 189 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 43 | 210 | 45 | 18.0 | 30 | 140 | 212 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 584 | 0 | 45 | 78.3 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1326 | 1041 | 90 | 76.6 | 658 | 2234 | 2476 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 496 | 481 | 60 | 44.2 | 231 | 916 | 1152 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 185.7 | 65 | 158 | 248 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 91 | 1100 | 90 | 10.2 | 272 | 1082 | 1269 | 0 | 11 |
| ITEM-0110 | C - Slow Moving | Healthy | 644 | 0 | 60 | 184.0 | 115 | 329 | 434 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2046 | 0 | 90 | 142.0 | 548 | 1860 | 2062 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 903 | 622 | 60 | 51.4 | 450 | 1522 | 1768 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 27 | 45 | 14 | 19.0 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 67 | 648 | 90 | 12.6 | 164 | 649 | 761 | 0 | 13 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 63 | 245 | 368 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 28 | 55 | 30 | 14.1 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 100 | 290 | 7 | 7.3 | 36 | 146 | 433 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 138 | 216 | 14 | 13.4 | 59 | 214 | 429 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 123 | 0 | 7 | 20.7 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 941 | 200 | 30 | 114.1 | 393 | 649 | 764 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 560 | 750 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 712 | 0 | 14 | 122.1 | 33 | 121 | 243 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 381 | 0 | 60 | 83.8 | 73 | 351 | 487 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 25 | 113 | 142 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4100 | 0 | 60 | 295.7 | 355 | 1201 | 1395 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 29 | 80 | 112 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 577 | 0 | 14 | 55.5 | 80 | 236 | 382 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 534 | 227 | 30 | 34.2 | 204 | 688 | 906 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1555 | 269 | 60 | 86.1 | 462 | 1564 | 1817 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2420 | 0 | 45 | 244.4 | 155 | 611 | 819 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 350 | 479 | 45 | 32.1 | 171 | 673 | 903 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1016 | 0 | 7 | 78.2 | 38 | 142 | 415 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 135 | 529 | 665 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 200 | 636 | 90 | 44.1 | 140 | 553 | 648 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 136.9 | 223 | 381 | 602 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 729 | 0 | 60 | 136.7 | 114 | 440 | 552 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 41 | 200 | 60 | 22.1 | 31 | 145 | 200 | 0 | 23 |
| ITEM-0155 | B - Core Products | Excess | 725 | 0 | 14 | 105.1 | 41 | 145 | 290 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 625 | 259 | 30 | 34.4 | 242 | 805 | 1059 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 25.3 | 309 | 507 | 851 | 0 | — |
