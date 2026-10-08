# Synthetic Inventory Health

**Simulation date: 2026-10-08**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 28 |
| Healthy | 88 |
| Lead-time risk | 8 |
| Reorder | 1 |
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
| ITEM-0001 | B - Core Products | Healthy | 607 | 0 | 30 | 48.3 | 133 | 523 | 788 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 232 | 0 | 7 | 31.6 | 99 | 158 | 312 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 549 | 968 | 60 | 35.3 | 398 | 1347 | 1564 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1943 | 0 | 45 | 381.0 | 83 | 318 | 425 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 90 | 160 | 14 | 11.9 | 43 | 157 | 315 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 140 | 0 | 45 | 86.3 | 21 | 96 | 145 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 150 | 0 | 14 | 22.0 | 41 | 144 | 287 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 34 | 198 | 60 | 22.5 | 26 | 119 | 164 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 112 | 410 | 90 | 49.4 | 71 | 278 | 325 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 58 | 2145 | 60 | 5.4 | 679 | 1340 | 1492 | 0 | 6 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 111.9 | 296 | 413 | 617 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 362 | 0 | 90 | 125.3 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 875 | 0 | 7 | 68.7 | 33 | 135 | 403 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 240 | 0 | 7 | 184.6 | 21 | 32 | 71 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 78 | 203 | 285 | 0 | 1 |
| ITEM-0017 | B - Core Products | Healthy | 480 | 0 | 45 | 71.4 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1151 | 0 | 30 | 300.3 | 44 | 163 | 244 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2954 | 0 | 60 | 288.0 | 212 | 838 | 1053 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 245 | 0 | 14 | 34.3 | 43 | 150 | 300 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 565 | 0 | 60 | 475.2 | 21 | 94 | 130 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 612 | 2075 | 2299 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 44 | 0 | 30 | 76.2 | 7 | 25 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 219 | 0 | 30 | 89.6 | 27 | 103 | 155 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 235 | 960 | 90 | 38.7 | 190 | 744 | 871 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 14 | 0 | 7 | 22.5 | 7 | 12 | 31 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1256 | 0 | 14 | 215.3 | 35 | 123 | 245 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 346 | 0 | 60 | 81.5 | 68 | 327 | 455 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 338 | 0 | 45 | 91.1 | 60 | 231 | 309 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 335.4 | 73 | 198 | 259 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 296 | 0 | 14 | 24.6 | 68 | 249 | 501 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 136 | 0 | 14 | 27.9 | 30 | 103 | 206 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 375 | 0 | 30 | 46.4 | 87 | 338 | 508 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 416 | 290 | 30 | 29.3 | 153 | 593 | 891 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4492 | 0 | 60 | 529.9 | 221 | 739 | 857 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 342 | 270 | 14 | 28.5 | 313 | 494 | 662 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 130 | 0 | 14 | 22.0 | 37 | 126 | 250 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 520 | 1404 | 1608 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 722 | 0 | 45 | 211.0 | 42 | 200 | 303 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 353 | 115 | 90 | 131.3 | 118 | 363 | 444 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 259 | 334 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 138 | 475 | 60 | 24.5 | 196 | 540 | 709 | 0 | 25 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 58.4 | 161 | 298 | 489 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 7 | 80 | 45 | 8.3 | 12 | 51 | 77 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 113 | 275 | 354 | 0 | 1 |
| ITEM-0052 | B - Core Products | Healthy | 213 | 0 | 7 | 20.8 | 25 | 108 | 323 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 156 | 0 | 7 | 22.1 | 20 | 77 | 225 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4478 | 0 | 60 | 448.8 | 263 | 872 | 1012 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 454 | 0 | 14 | 50.3 | 70 | 206 | 332 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1119 | 1390 | 90 | 61.3 | 690 | 2352 | 2607 | 0 | 123 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1209 | 0 | 30 | 81.4 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 72 | 272 | 363 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 141 | 0 | 14 | 29.6 | 27 | 99 | 199 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 100 | 0 | 30 | 56.2 | 17 | 73 | 126 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 643 | 0 | 14 | 96.0 | 38 | 139 | 280 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 77.8 | 245 | 622 | 751 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 919 | 260 | 60 | 74.7 | 254 | 1005 | 1263 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 336 | 0 | 45 | 61.8 | 85 | 335 | 450 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 391 | 0 | 14 | 24.2 | 118 | 361 | 587 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 426 | 0 | 30 | 81.1 | 60 | 223 | 334 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 48 | 0 | 7 | 17.5 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 130 | 235 | 45 | 36.9 | 90 | 253 | 358 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 29 | 0 | 7 | 36.8 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 220 | 864 | 1085 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3535 | 0 | 90 | 694.7 | 157 | 621 | 727 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 43 | 0 | 14 | 21.3 | 10 | 41 | 101 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 57 | 0 | 45 | 64.9 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 360 | 0 | 7 | 145.3 | 7 | 27 | 102 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 378 | 540 | 45 | 32.1 | 186 | 729 | 976 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 563 | 0 | 45 | 248.4 | 28 | 133 | 201 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 431 | 558 | 90 | 60.6 | 218 | 866 | 1015 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 128 | 0 | 7 | 11.5 | 27 | 117 | 351 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 991 | 0 | 14 | 90.4 | 64 | 229 | 459 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 71 | 337 | 60 | 25.5 | 59 | 230 | 288 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 505 | 0 | 14 | 87.7 | 174 | 261 | 382 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 33 | 0 | 14 | 27.0 | 7 | 26 | 63 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 329 | 0 | 45 | 78.5 | 51 | 244 | 370 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 347 | 355 | 14 | 19.9 | 354 | 616 | 983 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 57 | 50 | 30 | 38.0 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 846 | 735 | 90 | 65.8 | 392 | 1563 | 1834 | 0 | 100 |
| ITEM-0093 | B - Core Products | Healthy | 141 | 435 | 7 | 6.5 | 283 | 456 | 910 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 114 | 0 | 7 | 21.7 | 16 | 58 | 169 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7105 | 0 | 90 | 391.1 | 690 | 2344 | 2598 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3871 | 0 | 60 | 281.6 | 353 | 1192 | 1384 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 214 | 0 | 7 | 32.8 | 100 | 153 | 290 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 162 | 0 | 7 | 24.1 | 22 | 76 | 217 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 181 | 0 | 14 | 45.4 | 25 | 85 | 169 | 0 | — |
| ITEM-0101 | A - Top Movers | Reorder | 626 | 765 | 60 | 46.6 | 661 | 1481 | 1669 | 280 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 28 | 210 | 45 | 13.2 | 27 | 125 | 189 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 690 | 689 | 90 | 74.1 | 417 | 1265 | 1460 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 492 | 0 | 45 | 64.6 | 120 | 471 | 630 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1166 | 1041 | 90 | 68.7 | 645 | 2189 | 2427 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 367 | 740 | 60 | 32.6 | 231 | 917 | 1154 | 0 | 76 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 218.3 | 57 | 131 | 203 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 7 | 1100 | 90 | 0.8 | 272 | 1080 | 1267 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 562 | 0 | 60 | 137.4 | 127 | 377 | 500 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1911 | 0 | 90 | 136.8 | 532 | 1803 | 1999 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 713 | 902 | 60 | 40.7 | 450 | 1519 | 1764 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 515 | 1395 | 45 | 37.7 | 715 | 1344 | 1535 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 11 | 45 | 14 | 7.7 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 90.2 | 245 | 412 | 646 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 19 | 87 | 132 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 648 | 90 | 0.0 | 167 | 659 | 772 | 124 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 289 | 0 | 30 | 49.8 | 62 | 242 | 364 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 68 | 59 | 30 | 35.6 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 284 | 0 | 7 | 21.2 | 35 | 143 | 423 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 285 | 238 | 45 | 86.4 | 163 | 315 | 385 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 182 | 0 | 14 | 95.2 | 63 | 92 | 132 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 262 | 0 | 14 | 26.5 | 58 | 207 | 415 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 57 | 126 | 7 | 9.6 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 1119 | 0 | 30 | 132.7 | 394 | 656 | 774 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 139 | 549 | 736 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1142 | 1320 | 90 | 84.9 | 713 | 1937 | 2219 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 643 | 0 | 14 | 108.4 | 33 | 122 | 247 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 342 | 0 | 60 | 79.1 | 70 | 334 | 464 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 26 | 122 | 153 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3960 | 0 | 60 | 289.3 | 352 | 1188 | 1379 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 102 | 0 | 45 | 116.2 | 26 | 67 | 93 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 495 | 0 | 14 | 53.0 | 70 | 210 | 341 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 380 | 456 | 30 | 24.6 | 203 | 683 | 899 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1368 | 269 | 60 | 75.9 | 460 | 1560 | 1812 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2318 | 0 | 45 | 239.0 | 153 | 600 | 803 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 635 | 1547 | 1861 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 476 | 236 | 45 | 43.3 | 173 | 679 | 910 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 913 | 0 | 7 | 73.4 | 37 | 137 | 398 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 118 | 462 | 580 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 175 | 636 | 90 | 42.9 | 126 | 498 | 583 | 0 | 43 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 51.2 | 323 | 559 | 888 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1266 | 0 | 14 | 112.4 | 246 | 415 | 652 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 692 | 0 | 60 | 150.4 | 98 | 379 | 476 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Excess | 930 | 400 | 90 | 526.4 | 193 | 354 | 391 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 31 | 200 | 60 | 19.5 | 27 | 124 | 172 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 639 | 0 | 14 | 90.3 | 42 | 149 | 297 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 705 | 266 | 30 | 39.2 | 238 | 796 | 1048 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 617 | 0 | 7 | 27.8 | 298 | 476 | 786 | 0 | — |
