# Synthetic Inventory Health

**Simulation date: 2026-10-20**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 92 |
| Lead-time risk | 2 |
| Reorder | 3 |
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
| ITEM-0001 | B - Core Products | Healthy | 419 | 291 | 30 | 32.0 | 138 | 545 | 820 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 19.3 | 97 | 157 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 359 | 968 | 60 | 23.4 | 393 | 1328 | 1543 | 216 | — |
| ITEM-0005 | B - Core Products | Excess | 1896 | 0 | 45 | 417.2 | 73 | 283 | 378 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 182 | 0 | 14 | 25.2 | 42 | 151 | 302 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 120 | 0 | 45 | 75.5 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 78 | 145 | 14 | 12.3 | 38 | 134 | 268 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 215 | 0 | 60 | 159.9 | 23 | 106 | 146 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 90 | 410 | 90 | 43.5 | 65 | 254 | 297 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 787 | 1654 | 1852 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 325 | 90 | 90 | 111.2 | 69 | 335 | 423 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 733 | 0 | 7 | 58.3 | 33 | 134 | 398 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 174 | 0 | 7 | 102.4 | 23 | 37 | 88 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 407 | 155 | 45 | 60.9 | 105 | 413 | 553 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1119 | 0 | 30 | 333.5 | 39 | 144 | 214 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2829 | 0 | 60 | 271.2 | 216 | 853 | 1072 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 194 | 0 | 14 | 30.8 | 37 | 132 | 264 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 558 | 0 | 60 | 551.9 | 18 | 80 | 111 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 606 | 2056 | 2279 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 36 | 0 | 30 | 63.5 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 50.8 | 677 | 1278 | 1416 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 197 | 0 | 30 | 88.6 | 25 | 94 | 141 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 182 | 960 | 90 | 33.5 | 168 | 663 | 777 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 30 | 0 | 7 | 58.7 | 6 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1219 | 0 | 14 | 232.9 | 32 | 111 | 221 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 291 | 135 | 60 | 66.1 | 71 | 340 | 472 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 298 | 0 | 45 | 86.5 | 56 | 215 | 287 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 174 | 265 | 14 | 14.8 | 67 | 244 | 491 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 99 | 0 | 14 | 22.8 | 27 | 92 | 183 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 280 | 172 | 30 | 33.6 | 89 | 347 | 522 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 504 | 315 | 30 | 34.5 | 157 | 611 | 918 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4407 | 0 | 60 | 592.9 | 191 | 645 | 749 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 500 | 210 | 14 | 42.7 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 85 | 116 | 14 | 17.5 | 29 | 102 | 205 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 680 | 0 | 45 | 199.3 | 42 | 199 | 302 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 260 | 335 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 8 | 760 | 60 | 1.2 | 282 | 693 | 834 | 0 | 2 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 82.0 | 139 | 237 | 373 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 82 | 0 | 45 | 117.1 | 11 | 44 | 65 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Reorder | 94 | 0 | 7 | 9.1 | 25 | 108 | 325 | 231 | — |
| ITEM-0053 | B - Core Products | Healthy | 50 | 155 | 7 | 6.7 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4401 | 0 | 60 | 515.7 | 223 | 744 | 863 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 371 | 0 | 14 | 47.1 | 59 | 178 | 288 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 906 | 1680 | 90 | 48.8 | 703 | 2394 | 2654 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 79.1 | 471 | 918 | 1221 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 546 | 0 | 45 | 142.4 | 63 | 240 | 320 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 79 | 110 | 14 | 16.2 | 28 | 102 | 204 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 84 | 0 | 30 | 54.8 | 14 | 62 | 108 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 576 | 0 | 14 | 87.3 | 38 | 137 | 276 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 404 | 310 | 60 | 73.0 | 229 | 567 | 683 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 782 | 260 | 60 | 65.1 | 248 | 981 | 1233 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 272 | 115 | 45 | 50.3 | 85 | 334 | 448 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 412 | 0 | 14 | 25.3 | 119 | 364 | 592 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 384 | 0 | 30 | 82.3 | 53 | 198 | 296 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 19 | 85 | 7 | 7.0 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 33.6 | 3 | 9 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 224 | 883 | 1109 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3494 | 0 | 90 | 778.4 | 137 | 546 | 640 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 17 | 61 | 14 | 8.4 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 44 | 26 | 45 | 49.5 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 727 | 90 | 0.0 | 358 | 833 | 942 | 215 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 342 | 0 | 7 | 161.2 | 6 | 23 | 87 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 528 | 265 | 45 | 45.8 | 182 | 713 | 955 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 538 | 0 | 45 | 244.5 | 27 | 129 | 195 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 355 | 558 | 90 | 50.8 | 215 | 851 | 998 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 241 | 0 | 7 | 21.4 | 27 | 117 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 865 | 0 | 14 | 77.4 | 65 | 233 | 468 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 46 | 337 | 60 | 19.2 | 51 | 198 | 248 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 197 | 205 | 14 | 21.5 | 216 | 354 | 547 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 22 | 35 | 14 | 20.8 | 6 | 22 | 54 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 274 | 0 | 45 | 63.9 | 53 | 251 | 379 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 38 | 50 | 30 | 25.1 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 716 | 1027 | 90 | 57.6 | 379 | 1510 | 1771 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 57 | 0 | 7 | 11.6 | 14 | 54 | 158 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6901 | 0 | 90 | 385.1 | 682 | 2313 | 2564 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3666 | 0 | 60 | 256.2 | 367 | 1240 | 1441 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 73 | 225 | 7 | 11.2 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 117 | 0 | 7 | 20.4 | 18 | 64 | 185 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 149 | 0 | 14 | 44.0 | 20 | 71 | 142 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 60.7 | 672 | 1531 | 1728 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 217 | 0 | 45 | 112.2 | 24 | 113 | 171 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 89.4 | 363 | 1064 | 1226 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 398 | 180 | 45 | 53.1 | 119 | 464 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 975 | 1286 | 90 | 57.3 | 647 | 2197 | 2435 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 252 | 740 | 60 | 23.0 | 225 | 894 | 1125 | 0 | 67 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 266 | 1058 | 1241 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 108.3 | 135 | 422 | 562 | 0 | — |
| ITEM-0111 | A - Top Movers | Reorder | 1722 | 0 | 90 | 127.1 | 518 | 1751 | 1941 | 220 | — |
| ITEM-0112 | A - Top Movers | Healthy | 474 | 1161 | 60 | 27.2 | 448 | 1513 | 1758 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 40 | 0 | 14 | 28.8 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 908 | 0 | 14 | 79.3 | 249 | 421 | 662 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 85 | 128 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 680 | 797 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 208 | 135 | 30 | 34.7 | 64 | 250 | 376 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 48 | 59 | 30 | 25.0 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 148 | 0 | 7 | 11.1 | 34 | 141 | 420 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 96 | 92 | 14 | 33.5 | 65 | 108 | 194 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 139 | 216 | 14 | 13.7 | 59 | 211 | 423 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 99 | 0 | 7 | 16.6 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 635 | 0 | 45 | 71.7 | 139 | 547 | 733 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 558 | 0 | 14 | 92.1 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 299 | 130 | 60 | 71.4 | 68 | 324 | 450 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | B - Core Products | Excess | 3772 | 0 | 60 | 267.3 | 292 | 1153 | 1450 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 413 | 0 | 14 | 49.7 | 61 | 186 | 303 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 420 | 474 | 30 | 26.8 | 206 | 692 | 911 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1155 | 539 | 60 | 63.9 | 461 | 1564 | 1817 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2192 | 0 | 45 | 222.4 | 156 | 610 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 565 | 1295 | 1547 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 362 | 470 | 45 | 33.6 | 169 | 665 | 892 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 771 | 0 | 7 | 61.1 | 37 | 138 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 104 | 408 | 513 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 144 | 636 | 90 | 40.8 | 109 | 431 | 505 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 14.8 | 465 | 782 | 1078 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 660 | 0 | 60 | 162.3 | 86 | 335 | 420 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 16 | 200 | 60 | 10.8 | 25 | 116 | 160 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 549 | 0 | 14 | 74.2 | 43 | 154 | 310 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 497 | 540 | 30 | 27.4 | 239 | 801 | 1054 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 28.0 | 277 | 429 | 695 | 0 | — |
