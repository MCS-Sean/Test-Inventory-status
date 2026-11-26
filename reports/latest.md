# Synthetic Inventory Health

**Simulation date: 2026-11-26**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 23 |
| Healthy | 101 |
| Lead-time risk | 6 |
| Reorder | 3 |
| Stockout | 5 |

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
| ITEM-0001 | B - Core Products | Healthy | 265 | 302 | 30 | 19.9 | 140 | 552 | 832 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 163 | 185 | 7 | 19.5 | 105 | 173 | 348 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 336 | 1107 | 60 | 22.3 | 390 | 1312 | 1523 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1728 | 0 | 45 | 428.4 | 65 | 251 | 336 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 79 | 150 | 14 | 11.3 | 41 | 146 | 293 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 63 | 46 | 45 | 42.0 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 110 | 130 | 14 | 18.9 | 34 | 122 | 244 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 155 | 0 | 60 | 111.6 | 24 | 109 | 151 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 419 | 0 | 90 | 221.8 | 59 | 231 | 271 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1422 | 765 | 60 | 97.7 | 802 | 1690 | 1894 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1111 | 0 | 7 | 91.3 | 272 | 370 | 540 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 233 | 90 | 90 | 88.9 | 62 | 301 | 380 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 216 | 0 | 7 | 16.2 | 33 | 140 | 420 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 101 | 0 | 7 | 49.1 | 24 | 41 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 156 | 80 | 45 | 63.2 | 74 | 188 | 262 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 168 | 300 | 45 | 26.7 | 99 | 389 | 522 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 995 | 0 | 30 | 337.9 | 33 | 125 | 187 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2449 | 0 | 60 | 237.3 | 214 | 844 | 1061 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 75 | 135 | 14 | 13.4 | 33 | 117 | 235 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 520 | 0 | 60 | 570.7 | 17 | 73 | 100 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2162 | 0 | 90 | 138.1 | 600 | 2025 | 2244 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 12 | 20 | 30 | 22.0 | 7 | 24 | 41 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 650 | 1299 | 60 | 41.0 | 925 | 1892 | 2114 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 124 | 0 | 30 | 63.8 | 17 | 78 | 136 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 936 | 0 | 90 | 189.7 | 150 | 599 | 703 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.0 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1023 | 0 | 14 | 228.5 | 27 | 95 | 189 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 142 | 265 | 60 | 33.3 | 68 | 329 | 457 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 169 | 75 | 45 | 53.9 | 51 | 196 | 261 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 292 | 0 | 14 | 25.9 | 65 | 235 | 472 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 56.1 | 97 | 142 | 260 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 43 | 90 | 14 | 11.7 | 22 | 77 | 154 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 118 | 364 | 30 | 13.6 | 93 | 363 | 545 | 0 | — |
| ITEM-0039 | B - Core Products | Reorder | 300 | 315 | 30 | 20.1 | 158 | 621 | 935 | 320 | — |
| ITEM-0040 | A - Top Movers | Excess | 4113 | 0 | 60 | 582.0 | 181 | 613 | 711 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 565 | 0 | 14 | 46.1 | 288 | 472 | 644 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 123 | 0 | 14 | 26.6 | 27 | 97 | 194 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 475 | 1227 | 1400 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 572 | 0 | 45 | 176.9 | 40 | 189 | 286 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 306 | 235 | 90 | 97.3 | 127 | 414 | 508 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 112.3 | 107 | 255 | 328 | 0 | — |
| ITEM-0047 | B - Core Products | Healthy | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 55 | 0 | 45 | 83.9 | 10 | 41 | 60 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 344 | 465 | 60 | 51.8 | 264 | 670 | 809 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 202 | 0 | 7 | 20.8 | 23 | 101 | 305 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 98 | 0 | 7 | 13.3 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4055 | 0 | 60 | 507.6 | 204 | 692 | 804 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 81 | 100 | 14 | 11.2 | 55 | 164 | 266 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 288 | 2220 | 90 | 16.2 | 676 | 2296 | 2545 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 851 | 305 | 30 | 63.2 | 455 | 873 | 1156 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 390 | 0 | 45 | 107.3 | 57 | 225 | 301 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 99 | 110 | 14 | 19.1 | 29 | 107 | 216 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 15 | 92 | 30 | 9.8 | 14 | 62 | 108 | 0 | — |
| ITEM-0063 | B - Core Products | Healthy | 363 | 0 | 14 | 59.8 | 36 | 127 | 255 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 457 | 160 | 60 | 91.8 | 207 | 511 | 616 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 285 | 790 | 60 | 22.0 | 266 | 1058 | 1331 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 32 | 367 | 45 | 5.4 | 93 | 365 | 490 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 324 | 245 | 14 | 19.6 | 121 | 370 | 602 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 209 | 0 | 30 | 52.0 | 44 | 169 | 254 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 93 | 0 | 7 | 35.2 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 149.5 | 65 | 164 | 228 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.8 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Reorder | 708 | 249 | 60 | 59.7 | 245 | 969 | 1218 | 261 | — |
| ITEM-0073 | B - Core Products | Excess | 3323 | 0 | 90 | 837.7 | 122 | 483 | 567 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 60 | 14 | 0.0 | 9 | 39 | 98 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Healthy | 39 | 28 | 45 | 41.8 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | C - Slow Moving | Stockout | 0 | 1350 | 90 | 0.0 | 406 | 1225 | 1495 | 0 | — |
| ITEM-0077 | C - Slow Moving | Excess | 264 | 0 | 7 | 144.9 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 128 | 381 | 465 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 355 | 495 | 45 | 32.4 | 173 | 678 | 908 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 437 | 0 | 45 | 185.5 | 29 | 138 | 209 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 508 | 464 | 90 | 74.0 | 212 | 837 | 982 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 73 | 245 | 7 | 6.3 | 29 | 122 | 366 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 531 | 0 | 14 | 51.0 | 60 | 217 | 435 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 272 | 0 | 60 | 111.8 | 51 | 200 | 251 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 170 | 465 | 14 | 13.0 | 257 | 454 | 729 | 0 | — |
| ITEM-0086 | C - Slow Moving | Lead-time risk | 10 | 30 | 14 | 9.8 | 6 | 22 | 52 | 0 | 10 |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 222 | 137 | 45 | 48.9 | 57 | 267 | 403 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 899 | 0 | 14 | 52.0 | 349 | 609 | 972 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 32 | 45 | 30 | 22.0 | 13 | 59 | 102 | 0 | 22 |
| ITEM-0092 | B - Core Products | Healthy | 725 | 853 | 90 | 60.0 | 368 | 1469 | 1722 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 679 | 0 | 7 | 38.3 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 73 | 0 | 7 | 16.0 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6265 | 0 | 90 | 353.7 | 669 | 2281 | 2529 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3188 | 0 | 60 | 227.2 | 360 | 1217 | 1413 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Lead-time risk | 15 | 115 | 7 | 3.0 | 15 | 55 | 160 | 0 | 4 |
| ITEM-0100 | B - Core Products | Healthy | 28 | 65 | 14 | 9.4 | 17 | 62 | 125 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1046 | 675 | 60 | 80.9 | 605 | 1394 | 1575 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 131 | 0 | 45 | 70.6 | 23 | 109 | 165 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 970 | 267 | 90 | 183.4 | 276 | 758 | 869 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 326 | 160 | 45 | 46.2 | 114 | 439 | 587 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 917 | 1265 | 90 | 55.1 | 636 | 2150 | 2383 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 338 | 757 | 60 | 30.8 | 225 | 895 | 1126 | 0 | 31 |
| ITEM-0108 | C - Slow Moving | Excess | 469 | 0 | 30 | 238.5 | 53 | 114 | 173 | 0 | — |
| ITEM-0109 | B - Core Products | Healthy | 902 | 185 | 90 | 105.0 | 262 | 1044 | 1224 | 0 | — |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1115 | 890 | 90 | 74.9 | 567 | 1921 | 2130 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 396 | 1301 | 60 | 21.4 | 472 | 1602 | 1862 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 38 | 0 | 14 | 27.4 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 593 | 0 | 14 | 124.1 | 129 | 201 | 301 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 68 | 50 | 45 | 43.7 | 19 | 91 | 138 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 472 | 242 | 90 | 81.4 | 178 | 706 | 828 | 0 | — |
| ITEM-0119 | B - Core Products | Healthy | 127 | 125 | 30 | 21.2 | 65 | 251 | 376 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 39 | 58 | 30 | 21.0 | 16 | 74 | 130 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 291 | 0 | 7 | 25.0 | 30 | 124 | 369 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 126 | 762 | 45 | 11.7 | 389 | 884 | 1110 | 0 | 12 |
| ITEM-0123 | B - Core Products | Healthy | 63 | 222 | 14 | 13.9 | 121 | 189 | 285 | 0 | — |
| ITEM-0124 | B - Core Products | Reorder | 196 | 0 | 14 | 20.3 | 57 | 202 | 405 | 209 | — |
| ITEM-0125 | B - Core Products | Healthy | 131 | 0 | 7 | 20.9 | 17 | 68 | 200 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Healthy | 748 | 0 | 30 | 125.4 | 305 | 490 | 574 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 314 | 374 | 45 | 36.0 | 137 | 538 | 721 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 161.4 | 607 | 1522 | 1732 | 0 | — |
| ITEM-0131 | B - Core Products | Healthy | 352 | 0 | 14 | 60.2 | 34 | 122 | 245 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 157 | 255 | 60 | 39.6 | 65 | 307 | 426 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3267 | 0 | 60 | 241.0 | 347 | 1174 | 1364 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Lead-time risk | 94 | 135 | 14 | 12.4 | 56 | 170 | 276 | 0 | 13 |
| ITEM-0139 | A - Top Movers | Healthy | 367 | 449 | 30 | 24.5 | 198 | 663 | 873 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 721 | 1087 | 60 | 39.5 | 466 | 1581 | 1836 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1799 | 0 | 45 | 182.7 | 154 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1259 | 315 | 60 | 109.6 | 569 | 1270 | 1512 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 439 | 229 | 45 | 41.2 | 167 | 657 | 881 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 336 | 0 | 7 | 28.1 | 33 | 129 | 381 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 753 | 0 | 60 | 164.1 | 95 | 375 | 472 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 26 | 636 | 90 | 9.0 | 90 | 354 | 415 | 0 | — |
| ITEM-0148 | B - Core Products | Excess | 1055 | 0 | 14 | 90.1 | 269 | 445 | 691 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 58.4 | 232 | 401 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 483 | 0 | 60 | 126.4 | 81 | 315 | 395 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 151.9 | 296 | 646 | 727 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 159 | 0 | 60 | 117.3 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 275 | 0 | 14 | 36.7 | 43 | 156 | 313 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 349 | 514 | 30 | 19.3 | 239 | 800 | 1053 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 475 | 371 | 7 | 22.3 | 315 | 486 | 784 | 0 | — |
