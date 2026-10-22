# Synthetic Inventory Health

**Simulation date: 2026-10-22**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 90 |
| Lead-time risk | 5 |
| Reorder | 3 |
| Stockout | 11 |

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
| ITEM-0001 | B - Core Products | Healthy | 391 | 291 | 30 | 29.8 | 138 | 545 | 820 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 19.3 | 97 | 157 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 328 | 1184 | 60 | 21.3 | 393 | 1331 | 1546 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1888 | 0 | 45 | 418.5 | 73 | 281 | 376 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 168 | 0 | 14 | 23.6 | 42 | 149 | 299 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 118 | 0 | 45 | 75.3 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 70 | 145 | 14 | 11.5 | 35 | 127 | 254 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 211 | 0 | 60 | 156.9 | 23 | 106 | 146 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 85 | 410 | 90 | 41.8 | 64 | 250 | 292 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 787 | 1654 | 1852 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 320 | 90 | 90 | 109.5 | 69 | 335 | 423 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 681 | 0 | 7 | 52.8 | 34 | 138 | 408 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 174 | 0 | 7 | 102.4 | 23 | 37 | 88 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 393 | 155 | 45 | 58.4 | 105 | 415 | 557 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1114 | 0 | 30 | 333.1 | 39 | 143 | 213 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2800 | 0 | 60 | 267.2 | 216 | 856 | 1076 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 185 | 0 | 14 | 30.2 | 36 | 128 | 257 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 557 | 0 | 60 | 550.9 | 18 | 80 | 111 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 604 | 2050 | 2273 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 34 | 0 | 30 | 57.7 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 50.8 | 677 | 1278 | 1416 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 194 | 0 | 30 | 89.5 | 19 | 87 | 152 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 170 | 960 | 90 | 31.9 | 164 | 650 | 762 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1205 | 0 | 14 | 233.2 | 32 | 110 | 218 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 283 | 135 | 60 | 64.0 | 71 | 341 | 474 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 290 | 0 | 45 | 83.7 | 56 | 216 | 289 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 155 | 265 | 14 | 13.1 | 67 | 245 | 493 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 35.2 | 129 | 200 | 385 | 0 | — |
| ITEM-0037 | B - Core Products | Reorder | 89 | 0 | 14 | 20.6 | 26 | 91 | 182 | 95 | — |
| ITEM-0038 | B - Core Products | Healthy | 263 | 172 | 30 | 31.5 | 89 | 348 | 523 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 475 | 315 | 30 | 32.5 | 156 | 610 | 917 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4398 | 0 | 60 | 600.6 | 188 | 635 | 738 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 42.7 | 246 | 422 | 668 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 75 | 116 | 14 | 15.3 | 29 | 103 | 206 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 677 | 0 | 45 | 201.8 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 8 | 760 | 60 | 1.2 | 282 | 693 | 834 | 0 | 2 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 82.0 | 139 | 237 | 373 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 80 | 0 | 45 | 112.5 | 11 | 44 | 66 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 70 | 231 | 7 | 6.7 | 25 | 109 | 328 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 38 | 155 | 7 | 5.1 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4385 | 0 | 60 | 527.6 | 217 | 724 | 841 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 360 | 0 | 14 | 46.7 | 57 | 173 | 281 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 876 | 1680 | 90 | 47.5 | 699 | 2378 | 2636 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 90.0 | 445 | 838 | 1104 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 538 | 0 | 45 | 145.0 | 60 | 231 | 309 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 69 | 110 | 14 | 13.9 | 28 | 103 | 207 | 0 | 14 |
| ITEM-0062 | C - Slow Moving | Healthy | 82 | 0 | 30 | 55.1 | 14 | 61 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 566 | 0 | 14 | 86.8 | 37 | 135 | 272 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 339 | 310 | 60 | 60.9 | 231 | 571 | 688 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 755 | 260 | 60 | 61.7 | 252 | 999 | 1256 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 256 | 115 | 45 | 46.5 | 87 | 341 | 457 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 394 | 0 | 14 | 24.2 | 119 | 363 | 591 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 377 | 0 | 30 | 83.0 | 52 | 193 | 289 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 96 | 0 | 7 | 35.3 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 24 | 0 | 7 | 31.8 | 3 | 10 | 32 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 225 | 886 | 1114 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3488 | 0 | 90 | 798.8 | 133 | 531 | 623 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 13 | 61 | 14 | 6.4 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 42 | 26 | 45 | 47.2 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 340 | 0 | 7 | 162.8 | 6 | 23 | 86 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 499 | 265 | 45 | 43.3 | 181 | 712 | 954 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 532 | 0 | 45 | 238.2 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 340 | 558 | 90 | 48.4 | 216 | 856 | 1003 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 226 | 0 | 7 | 20.1 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 838 | 0 | 14 | 74.7 | 65 | 234 | 469 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 40 | 337 | 60 | 16.7 | 50 | 196 | 246 | 0 | — |
| ITEM-0085 | B - Core Products | Lead-time risk | 31 | 205 | 14 | 2.8 | 242 | 406 | 636 | 400 | 3 |
| ITEM-0086 | C - Slow Moving | Healthy | 21 | 35 | 14 | 20.3 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 266 | 0 | 45 | 61.9 | 53 | 251 | 380 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 523 | 468 | 14 | 28.4 | 368 | 645 | 1031 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 35 | 50 | 30 | 23.0 | 14 | 62 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 686 | 1027 | 90 | 54.7 | 382 | 1524 | 1787 | 0 | 90 |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 52 | 104 | 7 | 10.5 | 14 | 54 | 158 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6852 | 0 | 90 | 377.9 | 689 | 2340 | 2593 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3635 | 0 | 60 | 252.6 | 368 | 1246 | 1448 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 73 | 225 | 7 | 11.2 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 106 | 0 | 7 | 19.2 | 17 | 62 | 178 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 139 | 0 | 14 | 40.6 | 20 | 72 | 144 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 65.9 | 642 | 1433 | 1614 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 212 | 0 | 45 | 111.6 | 24 | 112 | 169 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 379 | 180 | 45 | 50.4 | 119 | 466 | 623 | 0 | — |
| ITEM-0106 | A - Top Movers | Reorder | 933 | 1286 | 90 | 53.9 | 657 | 2233 | 2475 | 256 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 474 | 499 | 60 | 43.4 | 224 | 890 | 1119 | 0 | 66 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 267 | 1064 | 1248 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 121.0 | 125 | 382 | 508 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1683 | 220 | 90 | 123.2 | 522 | 1765 | 1956 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 429 | 1161 | 60 | 24.3 | 452 | 1528 | 1775 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 38 | 0 | 14 | 27.1 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 908 | 0 | 14 | 83.5 | 247 | 411 | 639 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 85 | 128 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 680 | 797 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 195 | 135 | 30 | 32.2 | 65 | 253 | 380 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 45 | 59 | 30 | 23.7 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 121 | 285 | 7 | 9.2 | 34 | 140 | 416 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Reorder | 80 | 0 | 14 | 23.5 | 103 | 154 | 226 | 146 | — |
| ITEM-0124 | B - Core Products | Healthy | 112 | 216 | 14 | 11.0 | 59 | 212 | 425 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 90 | 0 | 7 | 15.1 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 618 | 0 | 45 | 70.1 | 138 | 544 | 730 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 551 | 0 | 14 | 91.2 | 34 | 125 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 287 | 130 | 60 | 68.0 | 68 | 326 | 453 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 136 | 171 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3747 | 0 | 60 | 267.2 | 361 | 1217 | 1413 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 401 | 0 | 14 | 48.7 | 61 | 185 | 300 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 402 | 474 | 30 | 26.3 | 202 | 676 | 889 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1115 | 539 | 60 | 61.4 | 464 | 1573 | 1827 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2173 | 0 | 45 | 217.1 | 157 | 618 | 828 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1360 | 320 | 60 | 109.9 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 346 | 470 | 45 | 32.5 | 168 | 659 | 882 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 751 | 0 | 7 | 61.1 | 36 | 135 | 393 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 101 | 396 | 498 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 138 | 636 | 90 | 39.8 | 107 | 423 | 496 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 14.8 | 465 | 782 | 1078 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 99.5 | 230 | 388 | 610 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 652 | 0 | 60 | 162.5 | 85 | 330 | 414 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 15 | 200 | 60 | 10.5 | 24 | 112 | 155 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 533 | 0 | 14 | 71.2 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 731 | 274 | 30 | 40.6 | 238 | 797 | 1049 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 28.0 | 277 | 429 | 695 | 0 | — |
