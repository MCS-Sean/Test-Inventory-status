# Synthetic Inventory Health

**Simulation date: 2026-09-13**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 66 |
| Lead-time risk | 18 |
| Reorder | 2 |
| Stockout | 24 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 128 | 497 | 746 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 268 | 0 | 7 | 47.6 | 84 | 130 | 248 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 941 | 517 | 60 | 61.2 | 391 | 1330 | 1545 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2024 | 0 | 45 | 306.2 | 106 | 411 | 549 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 279 | 0 | 14 | 37.1 | 43 | 156 | 314 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 142 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 276 | 0 | 14 | 31.4 | 55 | 187 | 371 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 61 | 198 | 60 | 28.0 | 37 | 170 | 236 | 0 | 29 |
| ITEM-0010 | B - Core Products | Lead-time risk | 149 | 410 | 90 | 45.9 | 101 | 397 | 465 | 0 | 46 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 426 | 0 | 90 | 152.1 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1208 | 0 | 7 | 95.0 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 141.4 | 26 | 43 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 42 | 235 | 45 | 14.1 | 84 | 221 | 311 | 0 | 15 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 105 | 417 | 560 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1216 | 0 | 30 | 235.9 | 59 | 219 | 328 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3197 | 0 | 60 | 306.7 | 215 | 851 | 1070 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 361 | 0 | 14 | 37.0 | 58 | 205 | 409 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 589 | 0 | 60 | 404.7 | 25 | 114 | 158 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 639 | 2173 | 2409 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 10 | 45 | 30 | 14.1 | 8 | 31 | 52 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1021 | 717 | 60 | 99.9 | 701 | 1325 | 1468 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 29 | 130 | 228 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 334 | 960 | 90 | 41.8 | 248 | 975 | 1143 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1353 | 0 | 14 | 168.9 | 48 | 169 | 337 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 65 | 312 | 433 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 406 | 0 | 45 | 76.1 | 88 | 334 | 446 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 695 | 0 | 60 | 272.0 | 82 | 238 | 315 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 386 | 0 | 14 | 36.1 | 62 | 223 | 448 | 0 | — |
| ITEM-0036 | B - Core Products | Reorder | 134 | 0 | 7 | 13.3 | 141 | 222 | 434 | 300 | — |
| ITEM-0037 | B - Core Products | Healthy | 217 | 0 | 14 | 31.6 | 42 | 145 | 290 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 86 | 338 | 508 | 0 | 1 |
| ITEM-0039 | B - Core Products | Stockout | 0 | 865 | 30 | 0.0 | 148 | 574 | 863 | 0 | 1 |
| ITEM-0040 | A - Top Movers | Excess | 4633 | 0 | 60 | 383.2 | 316 | 1054 | 1223 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 46.1 | 262 | 461 | 740 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 246 | 0 | 14 | 31.9 | 49 | 165 | 327 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1745 | 90 | 0.0 | 566 | 1524 | 1745 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 800 | 0 | 45 | 232.3 | 42 | 201 | 304 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 419 | 0 | 90 | 150.8 | 120 | 373 | 457 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 58 | 145 | 188 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Healthy | 342 | 175 | 60 | 70.4 | 176 | 473 | 618 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 463 | 0 | 14 | 44.9 | 183 | 338 | 555 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 25 | 80 | 45 | 23.0 | 15 | 66 | 98 | 0 | 23 |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 115 | 242 | 304 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 258 | 0 | 7 | 26.0 | 27 | 107 | 316 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 181 | 0 | 7 | 24.7 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4644 | 0 | 60 | 362.5 | 339 | 1121 | 1300 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 602 | 0 | 14 | 50.2 | 95 | 275 | 443 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1575 | 865 | 90 | 88.4 | 675 | 2297 | 2547 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 899 | 1213 | 0 | 1 |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 96 | 362 | 483 | 0 | 1 |
| ITEM-0061 | B - Core Products | Stockout | 0 | 145 | 14 | 0.0 | 29 | 102 | 203 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 129 | 0 | 30 | 52.3 | 22 | 99 | 173 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 800 | 0 | 14 | 118.6 | 38 | 140 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1245 | 0 | 60 | 102.5 | 250 | 991 | 1246 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 469 | 0 | 45 | 80.2 | 91 | 360 | 483 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 536 | 0 | 14 | 31.5 | 122 | 378 | 616 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 128 | 390 | 30 | 17.8 | 81 | 305 | 456 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 24 | 90 | 7 | 8.5 | 7 | 30 | 115 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 124 | 104 | 45 | 49.2 | 74 | 191 | 266 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 23 | 0 | 7 | 27.2 | 3 | 10 | 36 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 235 | 926 | 1164 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3621 | 0 | 90 | 528.2 | 213 | 837 | 981 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 88 | 0 | 14 | 40.8 | 10 | 43 | 107 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 52 | 78 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 396 | 0 | 7 | 128.2 | 8 | 33 | 126 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 162 | 170 | 90 | 74.4 | 106 | 305 | 370 | 0 | 75 |
| ITEM-0079 | B - Core Products | Healthy | 629 | 275 | 45 | 50.3 | 196 | 772 | 1035 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 614 | 0 | 45 | 252.3 | 30 | 142 | 215 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 617 | 235 | 90 | 88.8 | 212 | 844 | 990 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 195 | 0 | 7 | 17.9 | 28 | 116 | 344 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1281 | 0 | 14 | 121.6 | 62 | 220 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 119 | 337 | 60 | 31.2 | 81 | 314 | 394 | 0 | 32 |
| ITEM-0085 | B - Core Products | Healthy | 465 | 0 | 14 | 74.9 | 189 | 283 | 413 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 52 | 0 | 14 | 31.6 | 9 | 34 | 83 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 271 | 364 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 784 | 0 | 14 | 58.2 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 90 | 0 | 30 | 58.7 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 1152 | 735 | 90 | 84.3 | 418 | 1662 | 1949 | 0 | 117 |
| ITEM-0093 | B - Core Products | Healthy | 750 | 0 | 7 | 44.1 | 248 | 385 | 742 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 204 | 0 | 7 | 28.0 | 22 | 81 | 234 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7554 | 0 | 90 | 424.6 | 676 | 2295 | 2544 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4244 | 0 | 60 | 321.2 | 341 | 1147 | 1332 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 275 | 0 | 7 | 30.3 | 30 | 103 | 293 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 251 | 0 | 14 | 46.7 | 34 | 115 | 228 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 1009 | 420 | 60 | 88.5 | 505 | 1201 | 1440 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 62 | 210 | 45 | 21.7 | 36 | 168 | 254 | 0 | 22 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 112.0 | 395 | 1173 | 1352 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 659 | 0 | 45 | 82.0 | 125 | 495 | 664 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1561 | 773 | 90 | 90.2 | 658 | 2233 | 2475 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 643 | 481 | 60 | 57.5 | 230 | 913 | 1148 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 562 | 0 | 30 | 181.9 | 66 | 162 | 255 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 225 | 915 | 90 | 25.0 | 275 | 1093 | 1282 | 0 | 26 |
| ITEM-0110 | C - Slow Moving | Excess | 702 | 0 | 60 | 245.8 | 104 | 279 | 364 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2238 | 0 | 90 | 149.3 | 569 | 1933 | 2143 | 0 | — |
| ITEM-0112 | A - Top Movers | Reorder | 1151 | 360 | 60 | 65.4 | 452 | 1527 | 1773 | 262 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 519 | 1395 | 45 | 26.0 | 897 | 1815 | 2095 | 0 | 27 |
| ITEM-0114 | C - Slow Moving | Healthy | 43 | 0 | 14 | 29.8 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 67.1 | 274 | 499 | 813 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 140 | 530 | 90 | 25.9 | 166 | 658 | 771 | 0 | 26 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 67 | 262 | 395 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 63 | 55 | 30 | 34.0 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 301 | 0 | 7 | 22.6 | 36 | 143 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 91 | 285 | 45 | 27.0 | 190 | 345 | 416 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 56.1 | 97 | 148 | 219 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 279 | 0 | 14 | 27.5 | 59 | 212 | 425 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 73 | 0 | 7 | 12.0 | 17 | 66 | 194 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 140 | 553 | 742 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 781 | 0 | 14 | 126.2 | 34 | 127 | 257 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 443 | 0 | 60 | 99.9 | 72 | 343 | 476 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 110 | 139 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4293 | 0 | 60 | 318.0 | 347 | 1171 | 1360 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 1 | 102 | 45 | 1.0 | 26 | 72 | 102 | 0 | 2 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 676 | 0 | 14 | 56.9 | 91 | 270 | 436 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 20 | 787 | 30 | 1.3 | 201 | 675 | 889 | 0 | 2 |
| ITEM-0140 | A - Top Movers | Healthy | 1775 | 0 | 60 | 96.7 | 469 | 1589 | 1846 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2561 | 0 | 45 | 263.7 | 153 | 600 | 804 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 589 | 1407 | 1688 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 487 | 243 | 45 | 44.4 | 171 | 676 | 907 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1198 | 0 | 7 | 91.8 | 38 | 143 | 417 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 162 | 629 | 789 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 239 | 636 | 90 | 43.9 | 168 | 664 | 778 | 0 | 44 |
| ITEM-0148 | A - Top Movers | Healthy | 995 | 0 | 14 | 51.8 | 417 | 705 | 974 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1511 | 0 | 14 | 137.8 | 230 | 395 | 625 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 592 | 178 | 60 | 93.5 | 134 | 521 | 654 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 185.6 | 333 | 790 | 895 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 59 | 200 | 60 | 26.8 | 37 | 172 | 238 | 0 | 27 |
| ITEM-0155 | B - Core Products | Excess | 832 | 0 | 14 | 121.0 | 40 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Stockout | 0 | 930 | 30 | 0.0 | 244 | 815 | 1072 | 0 | 1 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 383 | 418 | 7 | 16.9 | 304 | 485 | 802 | 0 | — |
