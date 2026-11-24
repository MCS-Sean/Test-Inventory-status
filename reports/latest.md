# Synthetic Inventory Health

**Simulation date: 2026-11-24**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 24 |
| Healthy | 97 |
| Lead-time risk | 7 |
| Reorder | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 298 | 302 | 30 | 22.5 | 140 | 551 | 829 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 163 | 185 | 7 | 19.5 | 105 | 173 | 348 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 343 | 1107 | 60 | 22.4 | 394 | 1330 | 1544 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1742 | 0 | 45 | 437.9 | 64 | 247 | 331 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 93 | 150 | 14 | 13.5 | 41 | 145 | 290 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 67 | 46 | 45 | 44.7 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 127 | 0 | 14 | 21.9 | 34 | 121 | 243 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 162 | 0 | 60 | 120.5 | 23 | 106 | 146 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 423 | 0 | 90 | 220.1 | 60 | 235 | 276 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1452 | 765 | 60 | 102.1 | 798 | 1666 | 1865 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 237 | 90 | 90 | 90.0 | 63 | 303 | 382 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 241 | 0 | 7 | 18.1 | 33 | 140 | 420 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 101 | 0 | 7 | 49.1 | 24 | 41 | 103 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 156 | 80 | 45 | 63.2 | 74 | 188 | 262 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 186 | 300 | 45 | 29.6 | 99 | 389 | 521 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1007 | 0 | 30 | 348.6 | 33 | 123 | 184 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2470 | 0 | 60 | 240.3 | 213 | 840 | 1056 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 87 | 135 | 14 | 15.2 | 34 | 120 | 240 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 521 | 0 | 60 | 558.2 | 17 | 74 | 102 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2194 | 0 | 90 | 140.7 | 598 | 2017 | 2235 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 14 | 20 | 30 | 26.8 | 7 | 24 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Reorder | 697 | 971 | 60 | 45.5 | 739 | 1674 | 1996 | 328 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 130 | 0 | 30 | 67.2 | 17 | 77 | 135 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 952 | 0 | 90 | 193.8 | 150 | 597 | 701 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.0 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1036 | 0 | 14 | 233.1 | 27 | 94 | 187 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 150 | 265 | 60 | 35.1 | 68 | 329 | 458 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 177 | 75 | 45 | 57.1 | 51 | 194 | 259 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 315 | 0 | 14 | 27.7 | 65 | 236 | 475 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 50 | 90 | 14 | 13.5 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 142 | 364 | 30 | 16.4 | 93 | 361 | 542 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 345 | 315 | 30 | 23.3 | 157 | 617 | 928 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4134 | 0 | 60 | 595.3 | 178 | 602 | 699 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 629 | 0 | 14 | 46.8 | 316 | 518 | 706 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 137 | 0 | 14 | 30.1 | 27 | 96 | 191 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 475 | 1227 | 1400 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 576 | 0 | 45 | 177.5 | 40 | 190 | 287 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 314 | 235 | 90 | 102.8 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 57 | 0 | 45 | 88.4 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 217 | 0 | 7 | 22.4 | 23 | 101 | 305 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 109 | 0 | 7 | 14.7 | 20 | 80 | 236 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4069 | 0 | 60 | 506.5 | 205 | 696 | 808 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 104 | 100 | 14 | 14.7 | 53 | 160 | 259 | 0 | — |
| ITEM-0056 | A - Top Movers | Reorder | 326 | 1950 | 90 | 18.3 | 675 | 2293 | 2542 | 270 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 851 | 305 | 30 | 63.2 | 455 | 873 | 1156 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 399 | 0 | 45 | 110.2 | 57 | 224 | 300 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 113 | 0 | 14 | 22.1 | 29 | 106 | 214 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 20 | 43 | 30 | 13.2 | 14 | 61 | 107 | 0 | — |
| ITEM-0063 | B - Core Products | Healthy | 372 | 0 | 14 | 60.7 | 36 | 128 | 257 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 457 | 160 | 60 | 84.3 | 217 | 548 | 662 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 308 | 790 | 60 | 24.0 | 264 | 1049 | 1319 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 51 | 367 | 45 | 8.8 | 91 | 357 | 479 | 0 | — |
| ITEM-0067 | A - Top Movers | Reorder | 114 | 245 | 14 | 6.9 | 122 | 372 | 604 | 245 | — |
| ITEM-0068 | B - Core Products | Healthy | 217 | 0 | 30 | 54.2 | 44 | 168 | 252 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 16 | 85 | 7 | 6.1 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 123.7 | 76 | 195 | 272 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 6 | 25 | 7 | 9.6 | 3 | 8 | 27 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 747 | 249 | 60 | 64.2 | 240 | 951 | 1195 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3334 | 0 | 90 | 842.9 | 121 | 481 | 565 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 2 | 60 | 14 | 1.0 | 9 | 39 | 99 | 0 | 2 |
| ITEM-0075 | C - Slow Moving | Healthy | 41 | 28 | 45 | 44.5 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 523 | 1342 | 1531 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 269 | 0 | 7 | 146.7 | 5 | 20 | 75 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 132 | 404 | 494 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 375 | 495 | 45 | 33.9 | 174 | 683 | 915 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 443 | 0 | 45 | 189.0 | 29 | 137 | 208 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 518 | 464 | 90 | 74.4 | 215 | 849 | 996 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 104 | 245 | 7 | 9.0 | 29 | 122 | 363 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 547 | 0 | 14 | 52.9 | 60 | 216 | 433 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 276 | 0 | 60 | 113.9 | 51 | 199 | 250 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.7 | 253 | 438 | 696 | 0 | — |
| ITEM-0086 | C - Slow Moving | Lead-time risk | 13 | 30 | 14 | 12.7 | 6 | 22 | 52 | 0 | 13 |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 232 | 137 | 45 | 51.2 | 56 | 265 | 401 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 52.0 | 433 | 693 | 935 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 37 | 45 | 30 | 25.6 | 13 | 58 | 102 | 0 | 26 |
| ITEM-0092 | B - Core Products | Healthy | 739 | 853 | 90 | 60.4 | 373 | 1488 | 1745 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 204 | 475 | 7 | 11.5 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 84 | 0 | 7 | 18.4 | 12 | 49 | 145 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6279 | 0 | 90 | 346.9 | 683 | 2331 | 2584 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3224 | 0 | 60 | 231.9 | 357 | 1205 | 1400 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 31 | 115 | 7 | 6.2 | 15 | 55 | 160 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 38 | 65 | 14 | 13.0 | 17 | 61 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1046 | 675 | 60 | 77.4 | 616 | 1441 | 1630 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 138 | 0 | 45 | 76.2 | 23 | 107 | 161 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 970 | 267 | 90 | 183.4 | 276 | 758 | 869 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 341 | 160 | 45 | 48.3 | 114 | 439 | 587 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 959 | 1265 | 90 | 58.8 | 625 | 2111 | 2339 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 356 | 757 | 60 | 32.4 | 226 | 897 | 1128 | 0 | 33 |
| ITEM-0108 | C - Slow Moving | Excess | 469 | 0 | 30 | 238.5 | 53 | 114 | 173 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 267 | 1063 | 1247 | 0 | — |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1143 | 890 | 90 | 77.5 | 562 | 1904 | 2111 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 187 | 1563 | 60 | 10.2 | 468 | 1587 | 1843 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 41 | 0 | 14 | 29.5 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 593 | 0 | 14 | 124.1 | 129 | 201 | 301 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 71 | 50 | 45 | 46.0 | 19 | 91 | 137 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 487 | 242 | 90 | 84.5 | 177 | 702 | 823 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 134 | 125 | 30 | 22.5 | 64 | 249 | 375 | 0 | 23 |
| ITEM-0120 | C - Slow Moving | Healthy | 41 | 58 | 30 | 21.8 | 16 | 75 | 131 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 58 | 255 | 7 | 4.9 | 30 | 125 | 372 | 0 | — |
| ITEM-0122 | B - Core Products | Lead-time risk | 126 | 762 | 45 | 11.7 | 389 | 884 | 1110 | 0 | 12 |
| ITEM-0123 | B - Core Products | Healthy | 63 | 222 | 14 | 13.9 | 121 | 189 | 285 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 226 | 0 | 14 | 23.8 | 56 | 199 | 398 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 138 | 0 | 7 | 22.1 | 17 | 68 | 199 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 329 | 374 | 45 | 37.6 | 138 | 541 | 724 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 161.4 | 607 | 1522 | 1732 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 368 | 0 | 14 | 63.7 | 34 | 121 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 165 | 255 | 60 | 41.4 | 65 | 309 | 428 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3300 | 0 | 60 | 244.6 | 345 | 1168 | 1357 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 125 | 135 | 14 | 16.9 | 55 | 166 | 270 | 0 | — |
| ITEM-0139 | A - Top Movers | Reorder | 411 | 238 | 30 | 27.9 | 196 | 654 | 860 | 211 | — |
| ITEM-0140 | A - Top Movers | Healthy | 749 | 1087 | 60 | 40.4 | 473 | 1605 | 1864 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1816 | 0 | 45 | 184.5 | 154 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1259 | 315 | 60 | 85.3 | 650 | 1551 | 1860 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 468 | 229 | 45 | 44.1 | 167 | 656 | 879 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 354 | 0 | 7 | 29.6 | 33 | 129 | 381 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 770 | 0 | 60 | 168.2 | 95 | 375 | 471 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 34 | 636 | 90 | 11.8 | 89 | 352 | 413 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 73.8 | 310 | 525 | 825 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 58.4 | 232 | 401 | 636 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 496 | 0 | 60 | 132.5 | 79 | 308 | 387 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 151.9 | 296 | 646 | 727 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 162 | 0 | 60 | 118.5 | 23 | 107 | 148 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 281 | 0 | 14 | 36.9 | 43 | 158 | 317 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 401 | 514 | 30 | 22.4 | 237 | 793 | 1044 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Reorder | 475 | 0 | 7 | 20.3 | 331 | 518 | 846 | 371 | — |
