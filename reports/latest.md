# Synthetic Inventory Health

**Simulation date: 2026-09-28**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 78 |
| Lead-time risk | 11 |
| Reorder | 2 |
| Stockout | 20 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 131 | 510 | 766 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 37 | 195 | 7 | 4.5 | 104 | 170 | 342 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 711 | 737 | 60 | 45.7 | 397 | 1346 | 1563 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1974 | 0 | 45 | 355.3 | 89 | 345 | 462 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 175 | 0 | 14 | 23.1 | 43 | 157 | 317 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 142 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 202 | 0 | 14 | 26.7 | 48 | 162 | 321 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 44 | 198 | 60 | 25.5 | 29 | 135 | 186 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 122 | 410 | 90 | 46.3 | 82 | 322 | 377 | 0 | — |
| ITEM-0011 | A - Top Movers | Lead-time risk | 111 | 2145 | 60 | 9.5 | 705 | 1417 | 1580 | 0 | 10 |
| ITEM-0012 | A - Top Movers | Excess | 1858 | 0 | 7 | 105.9 | 320 | 461 | 706 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 385 | 0 | 90 | 133.3 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1019 | 0 | 7 | 80.7 | 33 | 134 | 400 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 244 | 0 | 7 | 175.7 | 21 | 33 | 74 | 0 | — |
| ITEM-0016 | C - Slow Moving | Stockout | 0 | 235 | 45 | 0.0 | 76 | 196 | 274 | 0 | 1 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 408 | 547 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1177 | 0 | 30 | 281.0 | 49 | 179 | 267 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3039 | 0 | 60 | 289.7 | 216 | 856 | 1077 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 289 | 0 | 14 | 35.4 | 50 | 173 | 344 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 572 | 0 | 60 | 429.0 | 23 | 105 | 145 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 611 | 2073 | 2297 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 48 | 0 | 30 | 73.2 | 8 | 29 | 48 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 816 | 915 | 60 | 65.3 | 793 | 1556 | 1731 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 237 | 0 | 30 | 84.6 | 25 | 112 | 196 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 277 | 960 | 90 | 40.0 | 216 | 847 | 993 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 19 | 0 | 7 | 33.5 | 7 | 12 | 29 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1299 | 0 | 14 | 191.7 | 41 | 143 | 285 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 394 | 0 | 60 | 96.1 | 66 | 317 | 440 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 369 | 0 | 45 | 87.2 | 70 | 265 | 354 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 685 | 0 | 60 | 327.9 | 73 | 201 | 264 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 174 | 245 | 14 | 15.1 | 66 | 240 | 482 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 434 | 0 | 7 | 53.6 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 170 | 0 | 14 | 31.0 | 34 | 117 | 232 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 451 | 0 | 30 | 55.0 | 88 | 343 | 515 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 553 | 290 | 30 | 39.6 | 151 | 584 | 877 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4547 | 0 | 60 | 472.0 | 252 | 840 | 975 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 299 | 465 | 14 | 20.9 | 344 | 559 | 760 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 179 | 0 | 14 | 27.5 | 41 | 139 | 275 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 581 | 1599 | 1833 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 753 | 0 | 45 | 225.1 | 41 | 195 | 296 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 390 | 115 | 90 | 137.1 | 123 | 382 | 468 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 72 | 175 | 225 | 0 | 1 |
| ITEM-0047 | C - Slow Moving | Lead-time risk | 216 | 475 | 60 | 39.4 | 190 | 525 | 689 | 0 | 72 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 292 | 240 | 14 | 30.2 | 164 | 309 | 512 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 16 | 80 | 45 | 16.9 | 14 | 58 | 86 | 0 | — |
| ITEM-0051 | C - Slow Moving | Stockout | 0 | 378 | 60 | 0.0 | 141 | 354 | 459 | 0 | 1 |
| ITEM-0052 | B - Core Products | Reorder | 101 | 0 | 7 | 10.0 | 25 | 106 | 319 | 218 | — |
| ITEM-0053 | B - Core Products | Healthy | 68 | 155 | 7 | 9.5 | 20 | 78 | 229 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4547 | 0 | 60 | 421.9 | 284 | 942 | 1093 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 522 | 0 | 14 | 53.3 | 80 | 227 | 365 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 1307 | 1125 | 90 | 71.6 | 690 | 2353 | 2608 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 802 | 407 | 30 | 54.0 | 475 | 936 | 1247 | 0 | — |
| ITEM-0060 | B - Core Products | Stockout | 0 | 564 | 45 | 0.0 | 80 | 300 | 400 | 0 | 1 |
| ITEM-0061 | B - Core Products | Healthy | 71 | 110 | 14 | 14.4 | 29 | 103 | 207 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 109 | 0 | 30 | 53.6 | 19 | 83 | 144 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 708 | 0 | 14 | 104.5 | 38 | 140 | 282 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 480 | 310 | 60 | 69.3 | 266 | 689 | 834 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1046 | 0 | 60 | 84.0 | 256 | 1016 | 1278 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 394 | 0 | 45 | 71.3 | 86 | 341 | 456 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 285 | 245 | 14 | 17.2 | 120 | 369 | 601 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 460 | 0 | 30 | 77.7 | 68 | 252 | 376 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 73 | 0 | 7 | 26.0 | 6 | 29 | 113 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 26 | 339 | 45 | 7.2 | 90 | 257 | 365 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 10 | 25 | 7 | 12.5 | 3 | 10 | 34 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 229 | 899 | 1130 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3570 | 0 | 90 | 625.1 | 178 | 698 | 818 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 60 | 0 | 14 | 28.6 | 10 | 42 | 105 | 0 | — |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 13 | 53 | 79 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 77 | 441 | 90 | 30.4 | 233 | 464 | 517 | 0 | 31 |
| ITEM-0077 | C - Slow Moving | Excess | 375 | 0 | 7 | 141.8 | 7 | 29 | 108 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 150 | 170 | 90 | 64.9 | 108 | 319 | 388 | 0 | 65 |
| ITEM-0079 | B - Core Products | Reorder | 464 | 275 | 45 | 38.4 | 190 | 747 | 1000 | 265 | — |
| ITEM-0080 | C - Slow Moving | Excess | 583 | 0 | 45 | 246.3 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 511 | 393 | 90 | 73.1 | 213 | 849 | 996 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 263 | 0 | 7 | 23.5 | 28 | 118 | 354 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1096 | 0 | 14 | 100.6 | 64 | 228 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 93 | 337 | 60 | 30.7 | 65 | 251 | 314 | 0 | 31 |
| ITEM-0085 | B - Core Products | Healthy | 310 | 195 | 14 | 39.1 | 215 | 334 | 501 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 41 | 0 | 14 | 29.8 | 8 | 29 | 70 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 67 | 264 | 354 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 297 | 702 | 14 | 21.2 | 373 | 583 | 779 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 74 | 0 | 30 | 49.3 | 14 | 61 | 106 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 966 | 735 | 90 | 72.0 | 410 | 1632 | 1914 | 0 | 105 |
| ITEM-0093 | B - Core Products | Healthy | 608 | 0 | 7 | 37.0 | 239 | 371 | 715 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 148 | 0 | 7 | 24.6 | 18 | 67 | 193 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7274 | 0 | 90 | 396.8 | 695 | 2364 | 2620 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4006 | 0 | 60 | 296.0 | 349 | 1175 | 1364 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 294 | 0 | 7 | 52.1 | 93 | 139 | 257 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 210 | 0 | 7 | 28.2 | 24 | 84 | 240 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 204 | 0 | 14 | 45.9 | 28 | 95 | 188 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 922 | 420 | 60 | 90.9 | 448 | 1067 | 1280 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 43 | 210 | 45 | 18.3 | 30 | 138 | 209 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 723 | 689 | 90 | 74.4 | 435 | 1320 | 1524 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 576 | 0 | 45 | 77.4 | 118 | 461 | 617 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1313 | 1041 | 90 | 76.5 | 652 | 2214 | 2454 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 483 | 481 | 60 | 43.1 | 230 | 914 | 1149 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 557 | 0 | 30 | 215.2 | 59 | 140 | 217 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 77 | 1100 | 90 | 8.5 | 275 | 1096 | 1285 | 0 | 9 |
| ITEM-0110 | C - Slow Moving | Healthy | 644 | 0 | 60 | 184.0 | 115 | 329 | 434 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2033 | 0 | 90 | 142.8 | 541 | 1837 | 2036 | 0 | — |
| ITEM-0112 | A - Top Movers | Lead-time risk | 877 | 622 | 60 | 49.6 | 453 | 1532 | 1779 | 280 | 85 |
| ITEM-0113 | A - Top Movers | Healthy | 519 | 1395 | 45 | 31.6 | 814 | 1571 | 1801 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 26 | 45 | 14 | 18.1 | 7 | 29 | 72 | 0 | — |
| ITEM-0115 | B - Core Products | Healthy | 1004 | 0 | 14 | 78.2 | 263 | 456 | 725 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 63 | 648 | 90 | 11.9 | 163 | 645 | 756 | 0 | 12 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 62 | 242 | 364 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 26 | 55 | 30 | 13.1 | 17 | 79 | 139 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 90 | 290 | 7 | 6.6 | 36 | 146 | 433 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 523 | 45 | 0.0 | 231 | 467 | 575 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 190 | 0 | 14 | 104.3 | 63 | 91 | 129 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 135 | 216 | 14 | 13.3 | 58 | 211 | 425 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 117 | 0 | 7 | 19.5 | 16 | 64 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 919 | 200 | 30 | 108.3 | 394 | 658 | 776 | 0 | — |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 559 | 750 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1402 | 697 | 90 | 115.0 | 674 | 1784 | 2040 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 703 | 0 | 14 | 119.8 | 33 | 121 | 245 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 379 | 0 | 60 | 84.4 | 72 | 346 | 481 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 24 | 111 | 140 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 4100 | 0 | 60 | 299.5 | 352 | 1188 | 1379 | 0 | — |
| ITEM-0136 | C - Slow Moving | Stockout | 0 | 102 | 45 | 0.0 | 29 | 80 | 112 | 0 | 1 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Excess | 570 | 0 | 14 | 55.8 | 79 | 233 | 376 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 522 | 227 | 30 | 33.5 | 204 | 688 | 906 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1536 | 269 | 60 | 84.4 | 464 | 1574 | 1829 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2408 | 0 | 45 | 241.3 | 156 | 615 | 825 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1860 | 60 | 0.0 | 554 | 1333 | 1600 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 345 | 479 | 45 | 31.9 | 170 | 667 | 894 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1002 | 0 | 7 | 77.2 | 38 | 142 | 415 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 133 | 521 | 655 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 198 | 636 | 90 | 44.0 | 139 | 549 | 643 | 0 | 45 |
| ITEM-0148 | B - Core Products | Healthy | 802 | 0 | 14 | 39.0 | 355 | 664 | 1096 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1440 | 0 | 14 | 136.9 | 223 | 381 | 602 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 725 | 0 | 60 | 137.4 | 113 | 435 | 546 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 214.1 | 312 | 708 | 799 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 41 | 200 | 60 | 22.6 | 30 | 141 | 195 | 0 | 23 |
| ITEM-0155 | B - Core Products | Excess | 722 | 0 | 14 | 105.3 | 41 | 144 | 288 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 614 | 259 | 30 | 33.6 | 243 | 810 | 1066 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 622 | 0 | 7 | 25.3 | 309 | 507 | 851 | 0 | — |
