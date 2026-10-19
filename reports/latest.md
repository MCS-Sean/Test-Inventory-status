# Synthetic Inventory Health

**Simulation date: 2026-10-19**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 92 |
| Lead-time risk | 3 |
| Reorder | 2 |
| Stockout | 12 |

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
| ITEM-0001 | B - Core Products | Healthy | 437 | 291 | 30 | 33.4 | 138 | 544 | 819 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 19.3 | 97 | 157 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 375 | 968 | 60 | 24.5 | 392 | 1325 | 1539 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1899 | 0 | 45 | 413.8 | 74 | 286 | 382 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 191 | 0 | 14 | 26.4 | 42 | 151 | 303 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 122 | 0 | 45 | 76.8 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 84 | 145 | 14 | 13.1 | 39 | 136 | 271 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 216 | 0 | 60 | 158.0 | 23 | 107 | 148 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 92 | 410 | 90 | 44.3 | 65 | 255 | 298 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 787 | 1654 | 1852 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 327 | 90 | 90 | 112.3 | 69 | 334 | 422 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 750 | 0 | 7 | 59.9 | 32 | 133 | 396 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 174 | 0 | 7 | 102.4 | 23 | 37 | 88 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Reorder | 408 | 0 | 45 | 60.3 | 106 | 418 | 560 | 155 | — |
| ITEM-0018 | B - Core Products | Excess | 1120 | 0 | 30 | 326.2 | 40 | 147 | 219 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2838 | 0 | 60 | 273.8 | 215 | 848 | 1066 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 197 | 0 | 14 | 31.3 | 37 | 132 | 264 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 559 | 0 | 60 | 546.8 | 19 | 82 | 113 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 602 | 2043 | 2265 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 36 | 0 | 30 | 63.5 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 41.6 | 766 | 1501 | 1669 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 199 | 0 | 30 | 89.5 | 25 | 94 | 141 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 185 | 960 | 90 | 33.8 | 169 | 668 | 783 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1221 | 0 | 14 | 231.8 | 32 | 111 | 222 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 298 | 135 | 60 | 68.1 | 70 | 338 | 469 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 303 | 0 | 45 | 87.4 | 56 | 216 | 289 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 180 | 265 | 14 | 15.2 | 67 | 245 | 494 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 104 | 0 | 14 | 23.9 | 27 | 93 | 184 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 292 | 172 | 30 | 35.5 | 88 | 343 | 516 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 518 | 315 | 30 | 35.4 | 157 | 611 | 919 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4414 | 0 | 60 | 586.8 | 193 | 652 | 758 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 500 | 210 | 14 | 42.7 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 88 | 116 | 14 | 18.0 | 29 | 103 | 206 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 686 | 0 | 45 | 203.8 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 257 | 330 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 8 | 760 | 60 | 1.2 | 282 | 693 | 834 | 0 | 2 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 82 | 0 | 45 | 113.5 | 11 | 45 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 108 | 0 | 7 | 10.6 | 25 | 107 | 322 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 59 | 155 | 7 | 8.1 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4408 | 0 | 60 | 511.9 | 225 | 751 | 871 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 379 | 0 | 14 | 47.8 | 59 | 178 | 289 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 925 | 1680 | 90 | 49.8 | 703 | 2394 | 2654 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 79.1 | 471 | 918 | 1221 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 549 | 0 | 45 | 144.5 | 62 | 237 | 317 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 87 | 110 | 14 | 18.0 | 28 | 101 | 202 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 85 | 0 | 30 | 54.6 | 14 | 63 | 109 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 576 | 0 | 14 | 86.5 | 38 | 138 | 278 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 433 | 310 | 60 | 78.3 | 229 | 567 | 683 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 801 | 260 | 60 | 67.2 | 246 | 973 | 1223 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 276 | 115 | 45 | 50.8 | 85 | 335 | 450 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 422 | 0 | 14 | 25.7 | 120 | 367 | 596 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 389 | 0 | 30 | 83.0 | 53 | 199 | 297 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 22 | 85 | 7 | 8.1 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 32.6 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 223 | 880 | 1105 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3497 | 0 | 90 | 760.2 | 141 | 560 | 657 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 19 | 61 | 14 | 9.3 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 46 | 26 | 45 | 53.1 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 727 | 90 | 0.0 | 288 | 644 | 727 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 344 | 0 | 7 | 160.4 | 6 | 24 | 88 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 268 | 540 | 45 | 23.0 | 184 | 720 | 964 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 542 | 0 | 45 | 248.9 | 27 | 128 | 193 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 360 | 558 | 90 | 51.9 | 214 | 845 | 991 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 260 | 0 | 7 | 23.4 | 27 | 116 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 880 | 0 | 14 | 79.1 | 65 | 232 | 466 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 49 | 337 | 60 | 20.4 | 51 | 198 | 248 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 296 | 205 | 14 | 36.6 | 206 | 328 | 497 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 24 | 35 | 14 | 22.7 | 6 | 22 | 54 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 279 | 0 | 45 | 65.1 | 53 | 251 | 379 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 40 | 50 | 30 | 26.9 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 732 | 1027 | 90 | 58.8 | 380 | 1514 | 1776 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 530 | 0 | 7 | 29.3 | 255 | 400 | 781 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 61 | 0 | 7 | 12.3 | 14 | 54 | 158 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6917 | 0 | 90 | 382.9 | 687 | 2332 | 2584 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3681 | 0 | 60 | 257.2 | 367 | 1240 | 1441 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 73 | 225 | 7 | 11.2 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 123 | 0 | 7 | 20.9 | 20 | 68 | 191 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 151 | 0 | 14 | 43.0 | 22 | 75 | 149 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 60.7 | 672 | 1531 | 1728 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 218 | 0 | 45 | 112.8 | 24 | 113 | 171 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 89.4 | 363 | 1064 | 1226 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 401 | 180 | 45 | 53.8 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1003 | 1286 | 90 | 59.2 | 643 | 2184 | 2421 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 262 | 740 | 60 | 23.9 | 225 | 894 | 1124 | 0 | 68 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 232.5 | 54 | 122 | 188 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 270 | 1073 | 1259 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1745 | 0 | 90 | 129.5 | 515 | 1742 | 1931 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 496 | 1161 | 60 | 28.7 | 444 | 1498 | 1739 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 42 | 0 | 14 | 30.0 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 908 | 0 | 14 | 79.3 | 249 | 421 | 662 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 173 | 683 | 801 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 214 | 135 | 30 | 35.8 | 64 | 250 | 375 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 50 | 59 | 30 | 26.2 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 164 | 0 | 7 | 12.4 | 34 | 140 | 418 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 96 | 92 | 14 | 33.5 | 65 | 108 | 194 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 144 | 216 | 14 | 14.1 | 59 | 212 | 427 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 105 | 0 | 7 | 17.7 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 642 | 0 | 45 | 72.2 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 564 | 0 | 14 | 93.0 | 34 | 125 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 303 | 130 | 60 | 72.5 | 67 | 322 | 448 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 29 | 133 | 167 | 0 | 1 |
| ITEM-0135 | B - Core Products | Excess | 3798 | 0 | 60 | 273.5 | 287 | 1135 | 1426 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 419 | 0 | 14 | 50.1 | 61 | 187 | 304 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 436 | 229 | 30 | 27.9 | 206 | 691 | 910 | 245 | 43 |
| ITEM-0140 | A - Top Movers | Healthy | 1188 | 539 | 60 | 66.0 | 459 | 1557 | 1809 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2201 | 0 | 45 | 224.3 | 155 | 607 | 813 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 565 | 1295 | 1547 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 381 | 470 | 45 | 35.5 | 169 | 663 | 889 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 779 | 0 | 7 | 61.7 | 37 | 139 | 404 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 105 | 412 | 517 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 145 | 636 | 90 | 40.4 | 111 | 438 | 513 | 0 | — |
| ITEM-0148 | A - Top Movers | Reorder | 312 | 385 | 14 | 14.8 | 465 | 782 | 1078 | 385 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 664 | 0 | 60 | 163.7 | 86 | 334 | 419 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 17 | 200 | 60 | 11.4 | 25 | 116 | 161 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 555 | 0 | 14 | 75.2 | 43 | 154 | 309 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 506 | 540 | 30 | 27.7 | 240 | 806 | 1061 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 28.0 | 277 | 429 | 695 | 0 | — |
