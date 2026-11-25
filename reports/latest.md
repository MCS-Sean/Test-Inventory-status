# Synthetic Inventory Health

**Simulation date: 2026-11-25**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 24 |
| Healthy | 99 |
| Lead-time risk | 7 |
| Reorder | 4 |
| Stockout | 4 |

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
| ITEM-0001 | B - Core Products | Healthy | 282 | 302 | 30 | 21.3 | 140 | 550 | 828 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 163 | 185 | 7 | 19.5 | 105 | 173 | 348 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 336 | 1107 | 60 | 21.9 | 394 | 1329 | 1544 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1732 | 0 | 45 | 429.4 | 65 | 251 | 336 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 86 | 150 | 14 | 12.4 | 41 | 146 | 292 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 65 | 46 | 45 | 43.3 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Reorder | 117 | 0 | 14 | 19.9 | 34 | 122 | 246 | 130 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 158 | 0 | 60 | 114.7 | 23 | 108 | 149 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 420 | 0 | 90 | 218.5 | 60 | 235 | 276 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1452 | 765 | 60 | 102.1 | 798 | 1666 | 1865 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 234 | 90 | 90 | 88.9 | 63 | 303 | 382 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 231 | 0 | 7 | 17.4 | 33 | 140 | 419 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 101 | 0 | 7 | 49.1 | 24 | 41 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 156 | 80 | 45 | 63.2 | 74 | 188 | 262 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 177 | 300 | 45 | 27.8 | 100 | 393 | 526 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1002 | 0 | 30 | 348.2 | 32 | 122 | 182 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2462 | 0 | 60 | 240.1 | 213 | 839 | 1054 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 78 | 135 | 14 | 13.7 | 34 | 120 | 239 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 521 | 0 | 60 | 578.9 | 16 | 71 | 98 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2180 | 0 | 90 | 139.7 | 598 | 2018 | 2236 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 20 | 30 | 24.4 | 7 | 24 | 40 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 650 | 1299 | 60 | 41.0 | 925 | 1892 | 2114 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 128 | 0 | 30 | 66.2 | 17 | 77 | 135 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 945 | 0 | 90 | 192.9 | 149 | 595 | 698 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.0 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1031 | 0 | 14 | 232.0 | 27 | 94 | 187 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 145 | 265 | 60 | 33.9 | 68 | 329 | 458 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 173 | 75 | 45 | 55.8 | 51 | 194 | 259 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 301 | 0 | 14 | 26.6 | 65 | 235 | 473 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 56.1 | 97 | 142 | 260 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 46 | 90 | 14 | 12.5 | 22 | 77 | 154 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 132 | 364 | 30 | 15.4 | 92 | 358 | 538 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 319 | 315 | 30 | 21.3 | 159 | 624 | 939 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4123 | 0 | 60 | 589.9 | 180 | 607 | 705 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 629 | 0 | 14 | 46.8 | 254 | 456 | 738 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 128 | 0 | 14 | 27.8 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 475 | 1227 | 1400 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 574 | 0 | 45 | 175.7 | 40 | 191 | 289 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 314 | 235 | 90 | 102.8 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 112.3 | 107 | 255 | 328 | 0 | — |
| ITEM-0047 | B - Core Products | Healthy | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 57 | 0 | 45 | 88.4 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | B - Core Products | Reorder | 344 | 239 | 60 | 51.8 | 264 | 670 | 809 | 226 | — |
| ITEM-0052 | B - Core Products | Healthy | 212 | 0 | 7 | 21.9 | 23 | 101 | 304 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 98 | 0 | 7 | 13.1 | 20 | 80 | 238 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4061 | 0 | 60 | 507.6 | 204 | 692 | 804 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 99 | 100 | 14 | 13.9 | 53 | 160 | 260 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 318 | 2220 | 90 | 18.0 | 671 | 2280 | 2528 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 851 | 305 | 30 | 63.2 | 455 | 873 | 1156 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 393 | 0 | 45 | 107.5 | 58 | 227 | 303 | 0 | — |
| ITEM-0061 | B - Core Products | Reorder | 106 | 0 | 14 | 20.6 | 29 | 107 | 215 | 110 | — |
| ITEM-0062 | C - Slow Moving | Reorder | 17 | 43 | 30 | 11.0 | 14 | 62 | 109 | 49 | — |
| ITEM-0063 | B - Core Products | Healthy | 368 | 0 | 14 | 60.2 | 36 | 128 | 256 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 457 | 160 | 60 | 91.8 | 207 | 511 | 616 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 297 | 790 | 60 | 22.9 | 266 | 1057 | 1329 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 41 | 367 | 45 | 7.0 | 92 | 362 | 485 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 87 | 490 | 14 | 5.2 | 123 | 376 | 611 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 211 | 0 | 30 | 52.6 | 44 | 169 | 253 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 12 | 85 | 7 | 4.5 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 123.7 | 76 | 195 | 272 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.8 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 724 | 249 | 60 | 61.5 | 243 | 962 | 1209 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3330 | 0 | 90 | 846.6 | 121 | 479 | 562 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 2 | 60 | 14 | 1.0 | 9 | 39 | 98 | 0 | 2 |
| ITEM-0075 | C - Slow Moving | Healthy | 40 | 28 | 45 | 43.4 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | C - Slow Moving | Stockout | 0 | 1350 | 90 | 0.0 | 406 | 1225 | 1495 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 267 | 0 | 7 | 145.6 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 128 | 381 | 465 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 372 | 495 | 45 | 33.9 | 173 | 678 | 909 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 439 | 0 | 45 | 186.4 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 511 | 464 | 90 | 74.2 | 212 | 839 | 984 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 87 | 245 | 7 | 7.5 | 30 | 123 | 368 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 539 | 0 | 14 | 51.9 | 60 | 216 | 434 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 273 | 0 | 60 | 112.2 | 51 | 200 | 251 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.7 | 253 | 438 | 696 | 0 | — |
| ITEM-0086 | C - Slow Moving | Lead-time risk | 11 | 30 | 14 | 10.6 | 6 | 22 | 53 | 0 | 11 |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 228 | 137 | 45 | 50.3 | 56 | 265 | 401 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 52.0 | 433 | 693 | 935 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 35 | 45 | 30 | 24.2 | 13 | 58 | 102 | 0 | 25 |
| ITEM-0092 | B - Core Products | Healthy | 726 | 853 | 90 | 59.6 | 371 | 1480 | 1735 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 679 | 0 | 7 | 38.3 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 77 | 0 | 7 | 16.8 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6267 | 0 | 90 | 349.5 | 677 | 2309 | 2560 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3206 | 0 | 60 | 231.2 | 356 | 1202 | 1396 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 24 | 115 | 7 | 4.8 | 15 | 55 | 160 | 0 | 5 |
| ITEM-0100 | B - Core Products | Healthy | 33 | 65 | 14 | 11.2 | 17 | 62 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1046 | 675 | 60 | 77.4 | 616 | 1441 | 1630 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 135 | 0 | 45 | 73.6 | 23 | 108 | 163 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 970 | 267 | 90 | 183.4 | 276 | 758 | 869 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 331 | 160 | 45 | 46.8 | 114 | 440 | 589 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 933 | 1265 | 90 | 56.3 | 633 | 2141 | 2373 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 343 | 757 | 60 | 31.1 | 226 | 900 | 1132 | 0 | 32 |
| ITEM-0108 | C - Slow Moving | Excess | 469 | 0 | 30 | 238.5 | 53 | 114 | 173 | 0 | — |
| ITEM-0109 | B - Core Products | Healthy | 908 | 185 | 90 | 105.0 | 264 | 1051 | 1233 | 0 | — |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1123 | 890 | 90 | 75.1 | 569 | 1929 | 2139 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 162 | 1563 | 60 | 8.8 | 472 | 1602 | 1861 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 40 | 0 | 14 | 29.0 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 593 | 0 | 14 | 124.1 | 129 | 201 | 301 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 70 | 50 | 45 | 45.0 | 19 | 91 | 138 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 480 | 242 | 90 | 82.6 | 178 | 707 | 829 | 0 | — |
| ITEM-0119 | B - Core Products | Healthy | 133 | 125 | 30 | 22.3 | 64 | 249 | 374 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 40 | 58 | 30 | 21.3 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 50 | 255 | 7 | 4.3 | 30 | 124 | 369 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 126 | 762 | 45 | 11.7 | 389 | 884 | 1110 | 0 | 12 |
| ITEM-0123 | B - Core Products | Healthy | 63 | 222 | 14 | 13.9 | 121 | 189 | 285 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 214 | 0 | 14 | 22.4 | 56 | 200 | 400 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 134 | 0 | 7 | 21.4 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 318 | 374 | 45 | 36.4 | 138 | 540 | 724 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 161.4 | 607 | 1522 | 1732 | 0 | — |
| ITEM-0131 | B - Core Products | Healthy | 360 | 0 | 14 | 62.1 | 34 | 121 | 243 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 162 | 255 | 60 | 40.5 | 65 | 309 | 429 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 133 | 167 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3278 | 0 | 60 | 242.0 | 347 | 1174 | 1363 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Lead-time risk | 108 | 135 | 14 | 14.4 | 56 | 169 | 274 | 0 | 15 |
| ITEM-0139 | A - Top Movers | Healthy | 383 | 449 | 30 | 25.4 | 199 | 666 | 877 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 737 | 1087 | 60 | 40.3 | 466 | 1581 | 1836 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1811 | 0 | 45 | 185.4 | 153 | 603 | 808 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1259 | 315 | 60 | 95.8 | 612 | 1414 | 1690 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 457 | 229 | 45 | 43.3 | 166 | 652 | 874 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 347 | 0 | 7 | 29.0 | 33 | 129 | 381 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 760 | 0 | 60 | 165.2 | 95 | 376 | 473 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 29 | 636 | 90 | 9.9 | 90 | 356 | 418 | 0 | — |
| ITEM-0148 | B - Core Products | Excess | 1055 | 0 | 14 | 90.1 | 269 | 445 | 691 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 58.4 | 232 | 401 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 489 | 0 | 60 | 129.8 | 80 | 310 | 389 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 151.9 | 296 | 646 | 727 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 161 | 0 | 60 | 118.8 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 281 | 0 | 14 | 37.4 | 43 | 156 | 314 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 377 | 514 | 30 | 20.9 | 238 | 797 | 1049 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 475 | 371 | 7 | 20.3 | 331 | 518 | 846 | 0 | — |
