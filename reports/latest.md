# Synthetic Inventory Health

**Simulation date: 2026-10-11**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 29 |
| Healthy | 87 |
| Lead-time risk | 7 |
| Reorder | 2 |
| Stockout | 13 |

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
| ITEM-0001 | B - Core Products | Healthy | 557 | 0 | 30 | 43.4 | 136 | 535 | 804 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 502 | 968 | 60 | 32.0 | 403 | 1361 | 1580 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1931 | 0 | 45 | 384.5 | 81 | 313 | 418 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 231 | 0 | 14 | 30.4 | 44 | 158 | 318 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 137 | 0 | 45 | 86.8 | 20 | 93 | 140 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 135 | 145 | 14 | 20.3 | 41 | 141 | 281 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 30 | 198 | 60 | 20.6 | 25 | 114 | 158 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 106 | 410 | 90 | 47.7 | 69 | 272 | 318 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 55 | 2145 | 60 | 5.1 | 679 | 1342 | 1494 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 352 | 0 | 90 | 121.4 | 69 | 333 | 420 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 837 | 0 | 7 | 65.6 | 32 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 86.7 | 78 | 203 | 285 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 460 | 0 | 45 | 69.1 | 104 | 411 | 550 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1141 | 0 | 30 | 302.0 | 44 | 162 | 241 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2928 | 0 | 60 | 287.7 | 211 | 832 | 1046 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 236 | 0 | 14 | 35.2 | 40 | 141 | 282 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 562 | 0 | 60 | 481.7 | 21 | 93 | 128 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 603 | 2047 | 2269 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 42 | 0 | 30 | 71.3 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 95.7 | 622 | 1142 | 1262 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 213 | 0 | 30 | 89.6 | 27 | 101 | 151 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 223 | 960 | 90 | 37.4 | 186 | 729 | 855 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 28.6 | 6 | 10 | 25 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1251 | 0 | 14 | 223.4 | 34 | 118 | 236 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 336 | 0 | 60 | 78.5 | 69 | 330 | 459 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 327 | 0 | 45 | 91.1 | 58 | 224 | 299 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 339.1 | 73 | 196 | 257 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 265 | 0 | 14 | 22.0 | 67 | 248 | 500 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 40.0 | 130 | 202 | 390 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 128 | 0 | 14 | 27.4 | 29 | 99 | 197 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 363 | 0 | 30 | 44.8 | 87 | 339 | 509 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 367 | 290 | 30 | 26.1 | 151 | 588 | 883 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4469 | 0 | 60 | 545.0 | 213 | 714 | 828 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 230 | 480 | 14 | 17.4 | 325 | 524 | 710 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 118 | 0 | 14 | 21.4 | 33 | 116 | 232 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 453 | 1160 | 1323 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 712 | 0 | 45 | 209.4 | 42 | 199 | 301 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 315 | 115 | 90 | 101.2 | 131 | 415 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 58 | 475 | 60 | 8.9 | 279 | 677 | 814 | 285 | 9 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 63.8 | 159 | 284 | 459 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.9 | 12 | 49 | 72 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 133 | 338 | 438 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 182 | 0 | 7 | 17.7 | 26 | 109 | 325 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 131 | 0 | 7 | 18.4 | 20 | 77 | 227 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4458 | 0 | 60 | 464.9 | 253 | 838 | 973 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 436 | 0 | 14 | 51.7 | 63 | 190 | 308 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1072 | 1390 | 90 | 58.6 | 691 | 2357 | 2613 | 0 | 121 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 69 | 262 | 350 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 126 | 0 | 14 | 26.4 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 96 | 0 | 30 | 56.5 | 16 | 69 | 120 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 628 | 0 | 14 | 94.0 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 85.0 | 234 | 579 | 697 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 898 | 260 | 60 | 74.1 | 251 | 990 | 1245 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 322 | 115 | 45 | 59.5 | 85 | 334 | 448 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 340 | 245 | 14 | 21.1 | 117 | 360 | 586 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 415 | 0 | 30 | 80.7 | 59 | 219 | 327 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 42 | 0 | 7 | 15.3 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 27 | 0 | 7 | 33.8 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 223 | 880 | 1105 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3525 | 0 | 90 | 701.9 | 155 | 613 | 718 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 35 | 61 | 14 | 17.3 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 54 | 0 | 45 | 62.3 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 355 | 0 | 7 | 149.3 | 6 | 26 | 97 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 327 | 540 | 45 | 27.0 | 190 | 747 | 1000 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 560 | 0 | 45 | 253.3 | 27 | 129 | 196 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 410 | 558 | 90 | 57.4 | 219 | 870 | 1020 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 101 | 240 | 7 | 9.1 | 27 | 116 | 349 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 966 | 0 | 14 | 88.4 | 64 | 228 | 458 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 66 | 337 | 60 | 24.9 | 56 | 218 | 274 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 29 | 0 | 14 | 23.9 | 7 | 26 | 62 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 314 | 0 | 45 | 73.6 | 52 | 249 | 377 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 52 | 50 | 30 | 34.9 | 13 | 60 | 104 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 817 | 735 | 90 | 64.1 | 388 | 1548 | 1816 | 0 | 99 |
| ITEM-0093 | B - Core Products | Healthy | 576 | 0 | 7 | 28.2 | 281 | 445 | 874 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 99 | 0 | 7 | 19.2 | 15 | 57 | 165 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7080 | 0 | 90 | 393.8 | 684 | 2320 | 2572 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3818 | 0 | 60 | 278.2 | 353 | 1191 | 1383 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 35.7 | 98 | 146 | 272 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 151 | 0 | 7 | 23.2 | 22 | 75 | 212 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 173 | 0 | 14 | 44.7 | 24 | 82 | 164 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 626 | 1045 | 60 | 46.6 | 661 | 1481 | 1669 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 23 | 210 | 45 | 11.0 | 27 | 124 | 186 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 81.1 | 388 | 1163 | 1342 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 468 | 0 | 45 | 62.1 | 119 | 466 | 624 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1120 | 1041 | 90 | 67.2 | 635 | 2153 | 2387 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 328 | 740 | 60 | 28.9 | 233 | 925 | 1163 | 0 | 72 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 267 | 1062 | 1246 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 533 | 0 | 60 | 120.8 | 132 | 402 | 534 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1873 | 0 | 90 | 136.3 | 525 | 1776 | 1969 | 0 | — |
| ITEM-0112 | A - Top Movers | Reorder | 635 | 902 | 60 | 35.6 | 458 | 1546 | 1796 | 259 | — |
| ITEM-0113 | A - Top Movers | Healthy | 311 | 1395 | 45 | 19.5 | 761 | 1494 | 1717 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 9 | 45 | 14 | 6.4 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 87 | 131 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 166 | 656 | 769 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 275 | 0 | 30 | 48.4 | 61 | 238 | 357 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 60 | 59 | 30 | 30.9 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 250 | 0 | 7 | 18.7 | 35 | 142 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 97.2 | 157 | 292 | 354 | 0 | — |
| ITEM-0123 | C - Slow Moving | Reorder | 100 | 0 | 14 | 35.4 | 65 | 108 | 192 | 92 | — |
| ITEM-0124 | B - Core Products | Healthy | 221 | 0 | 14 | 22.2 | 58 | 208 | 417 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 36 | 126 | 7 | 6.0 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 181.1 | 308 | 500 | 586 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 142 | 559 | 748 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 84.9 | 713 | 1937 | 2219 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 623 | 0 | 14 | 104.2 | 34 | 124 | 250 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 332 | 130 | 60 | 76.6 | 70 | 335 | 465 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 27 | 126 | 158 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3912 | 0 | 60 | 282.1 | 356 | 1202 | 1396 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 92 | 0 | 45 | 95.2 | 28 | 73 | 102 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 474 | 0 | 14 | 52.3 | 68 | 204 | 331 | 0 | — |
| ITEM-0139 | B - Core Products | Healthy | 569 | 229 | 30 | 36.8 | 163 | 642 | 967 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1313 | 269 | 60 | 72.9 | 460 | 1559 | 1811 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2282 | 0 | 45 | 235.3 | 152 | 599 | 802 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 449 | 236 | 45 | 40.6 | 173 | 682 | 914 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 885 | 0 | 7 | 71.1 | 37 | 137 | 399 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 115 | 452 | 567 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 165 | 636 | 90 | 42.4 | 120 | 474 | 556 | 0 | 43 |
| ITEM-0148 | A - Top Movers | Healthy | 581 | 385 | 14 | 32.0 | 439 | 711 | 965 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 685 | 0 | 60 | 153.4 | 95 | 368 | 462 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 26 | 200 | 60 | 16.4 | 27 | 124 | 172 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 615 | 0 | 14 | 85.8 | 42 | 150 | 300 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 651 | 266 | 30 | 36.0 | 238 | 799 | 1051 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
