# Synthetic Inventory Health

**Simulation date: 2026-10-23**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 31 |
| Healthy | 92 |
| Lead-time risk | 3 |
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
| ITEM-0001 | B - Core Products | Healthy | 387 | 291 | 30 | 29.6 | 138 | 544 | 819 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 143 | 170 | 7 | 21.3 | 93 | 147 | 288 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 307 | 1184 | 60 | 19.9 | 395 | 1338 | 1554 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1885 | 0 | 45 | 429.5 | 70 | 272 | 365 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 155 | 0 | 14 | 21.8 | 41 | 148 | 297 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 117 | 0 | 45 | 75.2 | 20 | 92 | 139 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 206 | 0 | 14 | 34.0 | 35 | 126 | 253 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 211 | 0 | 60 | 159.6 | 23 | 104 | 144 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 83 | 410 | 90 | 41.3 | 63 | 247 | 289 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 787 | 1654 | 1852 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 320 | 90 | 90 | 110.8 | 69 | 332 | 419 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 673 | 0 | 7 | 52.2 | 34 | 138 | 408 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 174 | 0 | 7 | 102.4 | 23 | 37 | 88 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 232 | 0 | 45 | 102.9 | 72 | 176 | 244 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 385 | 155 | 45 | 56.9 | 106 | 418 | 560 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1112 | 0 | 30 | 343.9 | 37 | 138 | 206 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2798 | 0 | 60 | 270.5 | 214 | 846 | 1063 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 177 | 0 | 14 | 29.2 | 36 | 127 | 255 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 556 | 0 | 60 | 562.2 | 18 | 79 | 108 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 602 | 2044 | 2266 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 33 | 0 | 30 | 56.0 | 7 | 26 | 43 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 50.8 | 677 | 1278 | 1416 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 193 | 0 | 30 | 90.0 | 19 | 86 | 150 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 165 | 960 | 90 | 31.5 | 160 | 637 | 747 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 22 | 0 | 7 | 36.7 | 7 | 12 | 30 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1200 | 0 | 14 | 235.3 | 31 | 108 | 215 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 280 | 135 | 60 | 63.8 | 70 | 338 | 470 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 289 | 0 | 45 | 83.9 | 55 | 214 | 286 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 142 | 265 | 14 | 11.9 | 67 | 246 | 496 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 310 | 0 | 7 | 38.3 | 126 | 191 | 361 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 86 | 95 | 14 | 20.2 | 26 | 90 | 180 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 256 | 172 | 30 | 30.8 | 89 | 347 | 522 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 456 | 315 | 30 | 31.1 | 156 | 610 | 918 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4394 | 0 | 60 | 606.5 | 186 | 628 | 730 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 500 | 210 | 14 | 45.6 | 242 | 407 | 637 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 73 | 116 | 14 | 15.1 | 28 | 101 | 203 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 529 | 1416 | 1621 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 675 | 0 | 45 | 201.2 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 371 | 60 | 0.0 | 113 | 286 | 371 | 0 | 1 |
| ITEM-0047 | B - Core Products | Stockout | 0 | 760 | 60 | 0.0 | 290 | 728 | 879 | 0 | 1 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 525 | 0 | 14 | 91.9 | 130 | 216 | 336 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 79 | 0 | 45 | 112.9 | 10 | 43 | 64 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 57 | 231 | 7 | 5.4 | 25 | 109 | 330 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 24 | 155 | 7 | 3.2 | 20 | 80 | 237 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4372 | 0 | 60 | 526.0 | 217 | 724 | 841 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 357 | 0 | 14 | 46.6 | 57 | 172 | 280 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 853 | 1680 | 90 | 46.5 | 695 | 2365 | 2622 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 90.0 | 445 | 838 | 1104 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 536 | 0 | 45 | 148.4 | 58 | 225 | 300 | 0 | — |
| ITEM-0061 | B - Core Products | Lead-time risk | 63 | 110 | 14 | 12.6 | 28 | 103 | 208 | 0 | 13 |
| ITEM-0062 | C - Slow Moving | Healthy | 81 | 0 | 30 | 54.8 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 558 | 0 | 14 | 85.3 | 37 | 136 | 273 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 339 | 310 | 60 | 60.9 | 231 | 571 | 688 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 741 | 260 | 60 | 60.5 | 252 | 999 | 1257 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 246 | 115 | 45 | 44.5 | 87 | 342 | 458 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 385 | 0 | 14 | 23.9 | 118 | 360 | 585 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 371 | 0 | 30 | 82.4 | 51 | 191 | 285 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 93 | 0 | 7 | 33.9 | 6 | 28 | 111 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 22 | 0 | 7 | 28.7 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 226 | 891 | 1119 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3483 | 0 | 90 | 799.7 | 133 | 530 | 621 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 10 | 61 | 14 | 4.9 | 10 | 41 | 103 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 42 | 26 | 45 | 47.2 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 942 | 90 | 0.0 | 358 | 833 | 942 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 338 | 0 | 7 | 163.5 | 6 | 23 | 85 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 484 | 265 | 45 | 41.9 | 182 | 714 | 957 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 530 | 0 | 45 | 237.3 | 28 | 131 | 198 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 337 | 558 | 90 | 48.4 | 214 | 848 | 995 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 216 | 0 | 7 | 19.2 | 28 | 119 | 355 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 827 | 0 | 14 | 73.5 | 65 | 234 | 470 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 38 | 337 | 60 | 16.0 | 50 | 196 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Lead-time risk | 31 | 605 | 14 | 2.8 | 242 | 406 | 636 | 0 | 3 |
| ITEM-0086 | C - Slow Moving | Healthy | 19 | 35 | 14 | 18.2 | 6 | 22 | 53 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 261 | 0 | 45 | 60.5 | 53 | 252 | 381 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 523 | 468 | 14 | 28.4 | 368 | 645 | 1031 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 33 | 50 | 30 | 21.5 | 14 | 62 | 108 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 680 | 1027 | 90 | 54.8 | 378 | 1508 | 1769 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 509 | 0 | 7 | 27.7 | 255 | 402 | 787 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 46 | 104 | 7 | 9.4 | 14 | 54 | 157 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6838 | 0 | 90 | 377.6 | 688 | 2337 | 2590 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3627 | 0 | 60 | 251.7 | 368 | 1248 | 1449 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 298 | 0 | 7 | 45.7 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 102 | 0 | 7 | 18.5 | 17 | 62 | 178 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 136 | 0 | 14 | 40.1 | 20 | 71 | 142 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 65.9 | 642 | 1433 | 1614 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 211 | 0 | 45 | 111.7 | 24 | 111 | 168 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 658 | 689 | 90 | 81.9 | 371 | 1103 | 1271 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 377 | 180 | 45 | 50.3 | 119 | 464 | 621 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 915 | 1542 | 90 | 52.7 | 659 | 2240 | 2483 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 459 | 499 | 60 | 41.9 | 225 | 893 | 1123 | 0 | 64 |
| ITEM-0108 | C - Slow Moving | Excess | 509 | 0 | 30 | 254.5 | 52 | 114 | 174 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 269 | 1073 | 1259 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 508 | 0 | 60 | 136.9 | 113 | 340 | 451 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1666 | 220 | 90 | 122.0 | 522 | 1765 | 1956 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 417 | 1161 | 60 | 23.6 | 452 | 1528 | 1775 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 36 | 0 | 14 | 25.7 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 908 | 0 | 14 | 94.0 | 236 | 381 | 584 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 172 | 679 | 796 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 188 | 135 | 30 | 31.2 | 64 | 252 | 378 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 43 | 59 | 30 | 22.5 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 110 | 285 | 7 | 8.4 | 34 | 140 | 416 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 80 | 146 | 14 | 23.5 | 103 | 154 | 226 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 108 | 216 | 14 | 10.8 | 59 | 210 | 420 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 85 | 0 | 7 | 14.3 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1109 | 0 | 30 | 207.9 | 290 | 456 | 530 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 605 | 0 | 45 | 68.7 | 138 | 544 | 729 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 540 | 0 | 14 | 88.5 | 35 | 127 | 255 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 286 | 130 | 60 | 68.6 | 67 | 322 | 447 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 135 | 169 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3725 | 0 | 60 | 262.9 | 364 | 1229 | 1427 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 92.2 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 394 | 0 | 14 | 47.8 | 61 | 185 | 301 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 384 | 474 | 30 | 25.0 | 203 | 680 | 894 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1100 | 539 | 60 | 60.3 | 465 | 1579 | 1835 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2157 | 0 | 45 | 213.8 | 159 | 624 | 835 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 1360 | 320 | 60 | 109.9 | 569 | 1325 | 1584 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 335 | 470 | 45 | 31.4 | 168 | 659 | 882 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 745 | 0 | 7 | 60.9 | 36 | 134 | 391 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 100 | 393 | 493 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 136 | 636 | 90 | 40.1 | 104 | 413 | 484 | 0 | — |
| ITEM-0148 | A - Top Movers | Healthy | 312 | 770 | 14 | 14.8 | 465 | 782 | 1078 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1048 | 0 | 14 | 113.6 | 217 | 356 | 549 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 650 | 0 | 60 | 163.9 | 84 | 326 | 410 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 13 | 200 | 60 | 9.1 | 24 | 112 | 155 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 525 | 0 | 14 | 70.3 | 43 | 155 | 312 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 717 | 274 | 30 | 40.2 | 235 | 788 | 1038 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 28.0 | 277 | 429 | 695 | 0 | — |
