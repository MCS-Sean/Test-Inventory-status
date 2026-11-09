# Synthetic Inventory Health

**Simulation date: 2026-11-09**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 98 |
| Lead-time risk | 4 |
| Reorder | 3 |
| Stockout | 7 |

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
| ITEM-0001 | B - Core Products | Healthy | 485 | 302 | 30 | 37.7 | 137 | 536 | 807 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 241 | 0 | 7 | 43.5 | 84 | 129 | 245 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 332 | 1107 | 60 | 21.8 | 391 | 1320 | 1533 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1821 | 0 | 45 | 476.4 | 61 | 237 | 318 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 205 | 0 | 14 | 29.8 | 41 | 145 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 95 | 0 | 45 | 63.8 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 104 | 125 | 14 | 18.5 | 32 | 117 | 235 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 188 | 0 | 60 | 148.4 | 22 | 100 | 138 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 53 | 410 | 90 | 29.3 | 56 | 221 | 259 | 0 | — |
| ITEM-0011 | A - Top Movers | Reorder | 1605 | 0 | 60 | 97.9 | 890 | 1890 | 2120 | 515 | — |
| ITEM-0012 | A - Top Movers | Excess | 1325 | 0 | 7 | 126.3 | 263 | 347 | 494 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 275 | 90 | 90 | 101.4 | 64 | 311 | 393 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 442 | 0 | 7 | 33.9 | 34 | 139 | 413 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 145 | 0 | 7 | 72.5 | 24 | 40 | 100 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 199 | 80 | 45 | 98.4 | 68 | 162 | 222 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 275 | 155 | 45 | 42.2 | 102 | 403 | 539 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1059 | 0 | 30 | 370.9 | 32 | 121 | 181 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2629 | 0 | 60 | 252.5 | 216 | 852 | 1070 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 80 | 120 | 14 | 14.9 | 31 | 112 | 225 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 538 | 0 | 60 | 590.5 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 591 | 1997 | 2213 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 23 | 20 | 30 | 42.2 | 7 | 24 | 41 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 763 | 1169 | 60 | 53.2 | 850 | 1726 | 1926 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 163 | 0 | 30 | 83.8 | 17 | 78 | 136 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 1030 | 0 | 90 | 208.8 | 150 | 599 | 703 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 44.0 | 7 | 11 | 26 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1111 | 0 | 14 | 240.4 | 27 | 97 | 194 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 219 | 135 | 60 | 52.7 | 67 | 321 | 446 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 248 | 0 | 45 | 85.8 | 46 | 179 | 240 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 671 | 0 | 60 | 774.2 | 44 | 97 | 123 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 218 | 245 | 14 | 18.9 | 66 | 239 | 481 | 0 | — |
| ITEM-0036 | B - Core Products | Reorder | 145 | 0 | 7 | 20.6 | 110 | 167 | 314 | 170 | — |
| ITEM-0037 | B - Core Products | Healthy | 118 | 0 | 14 | 31.9 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 123 | 355 | 30 | 14.7 | 89 | 349 | 524 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 547 | 315 | 30 | 36.5 | 158 | 622 | 937 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4257 | 0 | 60 | 615.0 | 177 | 600 | 697 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 503 | 0 | 14 | 45.2 | 232 | 399 | 633 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 112 | 0 | 14 | 23.8 | 27 | 98 | 197 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 499 | 1324 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 621 | 0 | 45 | 189.5 | 40 | 191 | 290 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 221 | 350 | 90 | 69.1 | 133 | 425 | 521 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 191 | 179 | 60 | 67.1 | 113 | 287 | 372 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 3.8 | 325 | 891 | 1085 | 0 | 4 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 185.3 | 84 | 127 | 186 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 67 | 0 | 45 | 104.0 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 185 | 502 | 60 | 33.7 | 183 | 518 | 683 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 143 | 0 | 7 | 14.6 | 22 | 101 | 307 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 71 | 155 | 7 | 9.7 | 20 | 79 | 232 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4212 | 0 | 60 | 540.0 | 200 | 676 | 785 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 227 | 0 | 14 | 31.5 | 53 | 161 | 262 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 596 | 1950 | 90 | 33.2 | 680 | 2315 | 2567 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1026 | 0 | 30 | 81.4 | 439 | 830 | 1095 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 465 | 0 | 45 | 131.2 | 56 | 220 | 294 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 96 | 105 | 14 | 19.5 | 28 | 102 | 206 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 53 | 43 | 30 | 37.0 | 13 | 58 | 101 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 451 | 0 | 14 | 70.2 | 37 | 134 | 269 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 52.9 | 210 | 524 | 632 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 535 | 525 | 60 | 43.7 | 252 | 999 | 1256 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 141 | 246 | 45 | 25.4 | 88 | 344 | 461 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 324 | 245 | 14 | 19.3 | 121 | 373 | 608 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 294 | 0 | 30 | 71.9 | 45 | 172 | 258 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 51 | 0 | 7 | 18.7 | 7 | 29 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 106.7 | 82 | 220 | 310 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 15 | 0 | 7 | 22.5 | 3 | 9 | 29 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 940 | 0 | 60 | 83.2 | 235 | 925 | 1162 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3416 | 0 | 90 | 875.9 | 119 | 474 | 556 | 0 | — |
| ITEM-0074 | C - Slow Moving | Reorder | 38 | 0 | 14 | 19.2 | 9 | 39 | 98 | 60 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 26 | 54 | 45 | 30.4 | 13 | 53 | 79 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1090 | 90 | 0.0 | 415 | 964 | 1090 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 306 | 0 | 7 | 173.2 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 52 | 290 | 90 | 25.3 | 107 | 295 | 356 | 0 | 26 |
| ITEM-0079 | B - Core Products | Healthy | 266 | 515 | 45 | 23.8 | 175 | 689 | 923 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 486 | 0 | 45 | 218.7 | 28 | 131 | 197 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 376 | 547 | 90 | 53.1 | 218 | 863 | 1011 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 283 | 0 | 7 | 24.5 | 29 | 122 | 364 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 649 | 0 | 14 | 59.4 | 63 | 227 | 457 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 332 | 0 | 60 | 150.9 | 46 | 181 | 227 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 35 | 0 | 14 | 36.2 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 178 | 135 | 45 | 40.6 | 54 | 256 | 388 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 605 | 369 | 14 | 31.6 | 457 | 745 | 1013 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 11 | 50 | 30 | 7.6 | 13 | 59 | 102 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 496 | 1027 | 90 | 40.1 | 376 | 1501 | 1760 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 32.9 | 256 | 402 | 784 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 61 | 0 | 7 | 13.1 | 12 | 50 | 147 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6525 | 0 | 90 | 358.5 | 688 | 2345 | 2599 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3451 | 0 | 60 | 254.2 | 349 | 1178 | 1368 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 41.7 | 89 | 130 | 236 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 14 | 115 | 7 | 2.8 | 14 | 54 | 158 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 89 | 0 | 14 | 29.1 | 18 | 64 | 128 | 0 | — |
| ITEM-0101 | B - Core Products | Healthy | 621 | 1260 | 60 | 41.3 | 573 | 1491 | 1807 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 177 | 0 | 45 | 98.9 | 22 | 105 | 158 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 575 | 689 | 90 | 83.5 | 332 | 959 | 1104 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 242 | 340 | 45 | 32.0 | 120 | 469 | 627 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 636 | 1789 | 90 | 37.0 | 653 | 2216 | 2456 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 513 | 498 | 60 | 46.2 | 227 | 905 | 1139 | 0 | 47 |
| ITEM-0108 | C - Slow Moving | Excess | 480 | 0 | 30 | 216.0 | 56 | 125 | 192 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 259 | 1030 | 1208 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 157.1 | 105 | 303 | 400 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1372 | 665 | 90 | 93.7 | 560 | 1893 | 2098 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 501 | 1047 | 60 | 29.4 | 439 | 1481 | 1719 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 15 | 45 | 14 | 10.8 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 801 | 0 | 14 | 186.3 | 139 | 204 | 294 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 92 | 0 | 45 | 61.3 | 19 | 88 | 133 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 180 | 713 | 836 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 99 | 260 | 30 | 16.9 | 63 | 245 | 369 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 68 | 58 | 30 | 35.6 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 240 | 0 | 7 | 19.6 | 32 | 130 | 387 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | B - Core Products | Healthy | 195 | 0 | 14 | 52.9 | 105 | 161 | 238 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 162 | 211 | 14 | 16.7 | 56 | 202 | 405 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 109 | 0 | 7 | 18.3 | 17 | 65 | 190 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 188.1 | 281 | 430 | 497 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 438 | 191 | 45 | 49.6 | 138 | 545 | 730 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 103.6 | 672 | 1755 | 2005 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 435 | 0 | 14 | 70.3 | 35 | 128 | 258 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 217 | 130 | 60 | 53.1 | 67 | 317 | 440 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3519 | 0 | 60 | 262.6 | 345 | 1163 | 1350 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 62 | 43 | 45 | 57.5 | 29 | 79 | 111 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 265 | 0 | 14 | 36.5 | 52 | 161 | 263 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 394 | 245 | 30 | 26.2 | 200 | 667 | 877 | 238 | 43 |
| ITEM-0140 | A - Top Movers | Healthy | 727 | 1068 | 60 | 39.1 | 474 | 1610 | 1870 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1981 | 0 | 45 | 200.6 | 155 | 610 | 817 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 380 | 463 | 45 | 35.7 | 168 | 658 | 881 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 506 | 0 | 7 | 40.5 | 37 | 137 | 400 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 862 | 0 | 60 | 195.4 | 91 | 361 | 453 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 88 | 636 | 90 | 29.0 | 94 | 371 | 434 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 1071 | 0 | 14 | 67.3 | 406 | 645 | 868 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 850 | 0 | 14 | 74.4 | 238 | 410 | 650 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 586 | 0 | 60 | 168.5 | 72 | 285 | 358 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 625 | 400 | 90 | 148.4 | 316 | 700 | 788 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 189 | 0 | 60 | 141.8 | 23 | 105 | 145 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 407 | 0 | 14 | 57.2 | 41 | 148 | 297 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 433 | 533 | 30 | 25.0 | 229 | 767 | 1009 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 314 | 498 | 7 | 15.0 | 318 | 486 | 779 | 0 | — |
