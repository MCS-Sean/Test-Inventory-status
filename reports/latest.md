# Synthetic Inventory Health

**Simulation date: 2026-11-16**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 26 |
| Healthy | 100 |
| Lead-time risk | 5 |
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
| ITEM-0001 | B - Core Products | Healthy | 422 | 302 | 30 | 32.9 | 137 | 536 | 805 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 107 | 190 | 7 | 15.5 | 94 | 150 | 294 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 454 | 884 | 60 | 29.6 | 394 | 1331 | 1546 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1787 | 0 | 45 | 462.2 | 62 | 240 | 322 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 157 | 0 | 14 | 23.0 | 40 | 143 | 286 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 83 | 46 | 45 | 56.2 | 19 | 87 | 132 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 56 | 125 | 14 | 9.8 | 41 | 127 | 206 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 177 | 0 | 60 | 138.5 | 22 | 100 | 139 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 443 | 0 | 90 | 235.9 | 58 | 229 | 269 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1308 | 0 | 7 | 131.1 | 261 | 341 | 481 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 259 | 90 | 90 | 97.5 | 63 | 305 | 385 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 352 | 0 | 7 | 27.0 | 33 | 138 | 412 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 226 | 300 | 45 | 34.7 | 102 | 403 | 539 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1035 | 0 | 30 | 369.6 | 32 | 119 | 178 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2555 | 0 | 60 | 242.1 | 219 | 863 | 1085 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 151 | 0 | 14 | 27.8 | 32 | 114 | 228 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 528 | 0 | 60 | 559.1 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 593 | 2001 | 2217 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 20 | 20 | 30 | 39.1 | 6 | 22 | 38 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 151 | 0 | 30 | 80.4 | 16 | 75 | 131 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 997 | 0 | 90 | 203.5 | 149 | 595 | 698 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 4 | 30 | 7 | 6.3 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1075 | 0 | 14 | 233.1 | 27 | 97 | 193 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 187 | 265 | 60 | 44.4 | 67 | 324 | 451 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 220 | 0 | 45 | 74.4 | 48 | 184 | 247 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 146 | 245 | 14 | 12.7 | 66 | 239 | 481 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 83 | 0 | 14 | 22.0 | 23 | 80 | 159 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 46 | 355 | 30 | 5.4 | 91 | 354 | 531 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 454 | 315 | 30 | 30.3 | 158 | 622 | 937 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4208 | 0 | 60 | 617.8 | 174 | 590 | 685 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 351 | 335 | 14 | 27.4 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 83 | 100 | 14 | 18.1 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 602 | 0 | 45 | 187.5 | 40 | 188 | 285 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 57.8 | 138 | 452 | 555 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 61 | 0 | 45 | 90.0 | 10 | 42 | 62 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 150 | 502 | 60 | 25.5 | 242 | 601 | 724 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 70 | 210 | 7 | 7.1 | 23 | 103 | 311 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 178 | 0 | 7 | 24.5 | 19 | 78 | 230 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4141 | 0 | 60 | 523.4 | 202 | 685 | 796 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 186 | 0 | 14 | 27.4 | 50 | 152 | 247 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 487 | 1950 | 90 | 28.0 | 659 | 2240 | 2483 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1018 | 0 | 30 | 80.2 | 439 | 833 | 1100 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 431 | 0 | 45 | 120.8 | 57 | 222 | 296 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 51 | 105 | 14 | 10.0 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 39 | 43 | 30 | 27.0 | 13 | 58 | 102 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 416 | 0 | 14 | 67.0 | 36 | 130 | 260 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 67.4 | 179 | 426 | 510 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 422 | 790 | 60 | 34.2 | 255 | 1009 | 1268 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 102 | 246 | 45 | 18.3 | 88 | 345 | 462 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 232 | 245 | 14 | 14.1 | 120 | 367 | 596 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 255 | 0 | 30 | 62.5 | 45 | 172 | 258 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 35 | 0 | 7 | 13.1 | 6 | 28 | 108 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 10 | 0 | 7 | 15.3 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 855 | 249 | 60 | 75.4 | 235 | 927 | 1165 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3378 | 0 | 90 | 861.2 | 120 | 477 | 560 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 22 | 60 | 14 | 11.1 | 9 | 39 | 99 | 0 | 12 |
| ITEM-0075 | C - Slow Moving | Healthy | 48 | 28 | 45 | 54.7 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 477 | 1186 | 1350 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 289 | 0 | 7 | 161.6 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 140 | 430 | 525 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 189 | 515 | 45 | 16.9 | 176 | 691 | 925 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 467 | 0 | 45 | 204.0 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 333 | 547 | 90 | 47.4 | 216 | 856 | 1003 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 190 | 0 | 7 | 16.7 | 29 | 121 | 359 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 602 | 0 | 14 | 56.6 | 62 | 222 | 446 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 303 | 0 | 60 | 126.8 | 50 | 196 | 246 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 26 | 0 | 14 | 26.9 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 264 | 0 | 45 | 59.0 | 55 | 261 | 396 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 974 | 0 | 14 | 52.4 | 456 | 735 | 996 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 50 | 45 | 30 | 34.1 | 13 | 59 | 103 | 0 | 35 |
| ITEM-0092 | B - Core Products | Healthy | 410 | 1289 | 90 | 33.1 | 377 | 1506 | 1766 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 598 | 0 | 7 | 35.3 | 252 | 388 | 743 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 34 | 99 | 7 | 7.7 | 12 | 48 | 141 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6424 | 0 | 90 | 356.2 | 682 | 2324 | 2576 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3319 | 0 | 60 | 238.8 | 357 | 1205 | 1400 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 211 | 0 | 7 | 55.2 | 72 | 103 | 183 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 92 | 0 | 7 | 19.1 | 13 | 52 | 153 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 69 | 0 | 14 | 23.2 | 17 | 62 | 125 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 159 | 0 | 45 | 90.0 | 22 | 104 | 157 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 554 | 689 | 90 | 95.5 | 295 | 823 | 945 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 193 | 340 | 45 | 26.2 | 117 | 456 | 610 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1090 | 1265 | 90 | 66.7 | 625 | 2113 | 2342 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 438 | 498 | 60 | 39.1 | 229 | 913 | 1148 | 0 | 40 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 262 | 1044 | 1224 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1285 | 665 | 90 | 87.9 | 558 | 1889 | 2094 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 354 | 1292 | 60 | 20.2 | 448 | 1515 | 1760 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 52 | 0 | 14 | 37.7 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 153.6 | 144 | 218 | 320 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 82 | 50 | 45 | 53.5 | 19 | 90 | 136 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 527 | 242 | 90 | 91.4 | 178 | 703 | 824 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 180 | 125 | 30 | 30.2 | 64 | 249 | 375 | 0 | 31 |
| ITEM-0120 | C - Slow Moving | Healthy | 53 | 58 | 30 | 27.3 | 17 | 78 | 136 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 145 | 0 | 7 | 12.0 | 31 | 128 | 382 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 313 | 647 | 800 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 41.8 | 82 | 142 | 262 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 311 | 0 | 14 | 32.9 | 55 | 197 | 395 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 60 | 133 | 7 | 9.8 | 17 | 67 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 211.2 | 275 | 408 | 467 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 390 | 191 | 45 | 44.4 | 137 | 541 | 726 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1233 | 1042 | 90 | 118.4 | 618 | 1566 | 1785 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 405 | 0 | 14 | 67.3 | 35 | 126 | 252 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 191 | 130 | 60 | 46.8 | 66 | 315 | 438 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3427 | 0 | 60 | 252.6 | 349 | 1177 | 1367 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 60.0 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 201 | 0 | 14 | 28.2 | 51 | 158 | 258 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 529 | 238 | 30 | 34.7 | 202 | 675 | 888 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 882 | 799 | 60 | 47.4 | 475 | 1611 | 1872 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1898 | 0 | 45 | 189.4 | 157 | 619 | 829 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1171 | 635 | 60 | 96.2 | 583 | 1326 | 1582 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 310 | 463 | 45 | 29.4 | 166 | 651 | 872 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 428 | 0 | 7 | 34.5 | 36 | 136 | 396 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 818 | 0 | 60 | 183.6 | 92 | 364 | 458 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 71 | 636 | 90 | 25.1 | 88 | 346 | 406 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 552 | 0 | 60 | 155.7 | 74 | 291 | 365 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 175 | 0 | 60 | 132.4 | 22 | 103 | 143 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 352 | 0 | 14 | 48.1 | 42 | 152 | 306 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 570 | 259 | 30 | 32.3 | 234 | 782 | 1029 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 701 | 0 | 7 | 33.6 | 317 | 484 | 776 | 0 | — |
