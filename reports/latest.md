# Synthetic Inventory Health

**Simulation date: 2026-11-20**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 25 |
| Healthy | 99 |
| Lead-time risk | 5 |
| Reorder | 3 |
| Stockout | 6 |

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
| ITEM-0001 | B - Core Products | Healthy | 361 | 302 | 30 | 27.8 | 138 | 541 | 814 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 68 | 190 | 7 | 9.3 | 96 | 155 | 309 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 391 | 1107 | 60 | 25.4 | 394 | 1333 | 1548 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1770 | 0 | 45 | 465.8 | 61 | 236 | 316 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 122 | 150 | 14 | 17.8 | 41 | 144 | 288 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 76 | 46 | 45 | 51.8 | 19 | 87 | 131 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 32 | 125 | 14 | 5.6 | 41 | 127 | 206 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 171 | 0 | 60 | 131.5 | 22 | 102 | 141 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 433 | 0 | 90 | 226.6 | 60 | 234 | 275 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 250 | 90 | 90 | 95.3 | 63 | 302 | 381 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 279 | 0 | 7 | 20.8 | 34 | 142 | 424 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 207 | 300 | 45 | 31.8 | 102 | 401 | 538 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1021 | 0 | 30 | 354.8 | 32 | 122 | 182 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2516 | 0 | 60 | 240.6 | 217 | 855 | 1075 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 125 | 0 | 14 | 22.8 | 32 | 115 | 230 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 525 | 0 | 60 | 549.4 | 17 | 76 | 104 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2250 | 0 | 90 | 144.3 | 598 | 2017 | 2235 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 17 | 20 | 30 | 33.3 | 7 | 23 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 139 | 0 | 30 | 73.2 | 16 | 75 | 132 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 975 | 0 | 90 | 199.0 | 149 | 595 | 698 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 34 | 0 | 7 | 53.7 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1057 | 0 | 14 | 234.3 | 27 | 95 | 190 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 170 | 265 | 60 | 39.9 | 68 | 328 | 456 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 203 | 0 | 45 | 68.4 | 48 | 185 | 247 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 354 | 0 | 14 | 31.1 | 66 | 237 | 477 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 65 | 90 | 14 | 17.6 | 22 | 78 | 155 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 182 | 183 | 30 | 21.5 | 91 | 354 | 531 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 394 | 315 | 30 | 26.2 | 159 | 625 | 941 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4162 | 0 | 60 | 594.6 | 179 | 606 | 704 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 686 | 0 | 14 | 53.5 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 62 | 100 | 14 | 13.7 | 27 | 95 | 191 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 519 | 1400 | 1603 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 592 | 0 | 45 | 186.9 | 39 | 185 | 280 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 65.1 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 60 | 0 | 45 | 94.7 | 10 | 40 | 59 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 252 | 0 | 7 | 25.8 | 23 | 102 | 307 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 143 | 0 | 7 | 19.4 | 20 | 79 | 234 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4110 | 0 | 60 | 509.5 | 206 | 699 | 811 | 0 | — |
| ITEM-0055 | A - Top Movers | Reorder | 153 | 0 | 14 | 22.4 | 51 | 154 | 250 | 100 | — |
| ITEM-0056 | A - Top Movers | Healthy | 419 | 1950 | 90 | 24.3 | 656 | 2227 | 2468 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1010 | 0 | 30 | 86.3 | 428 | 791 | 1037 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 420 | 0 | 45 | 118.5 | 56 | 220 | 294 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 31 | 105 | 14 | 6.1 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 29 | 43 | 30 | 19.6 | 14 | 60 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 402 | 0 | 14 | 66.3 | 36 | 127 | 255 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 471 | 160 | 60 | 89.4 | 215 | 537 | 647 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 363 | 790 | 60 | 28.8 | 260 | 1029 | 1294 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 77 | 367 | 45 | 13.6 | 90 | 352 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 167 | 245 | 14 | 10.1 | 121 | 368 | 599 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 233 | 0 | 30 | 57.8 | 44 | 170 | 254 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 22 | 85 | 7 | 8.2 | 6 | 28 | 109 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 7 | 25 | 7 | 11.2 | 3 | 8 | 27 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 799 | 249 | 60 | 69.6 | 237 | 938 | 1179 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3364 | 0 | 90 | 885.3 | 116 | 462 | 542 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 14 | 60 | 14 | 7.1 | 9 | 39 | 98 | 0 | 8 |
| ITEM-0075 | C - Slow Moving | Healthy | 44 | 28 | 45 | 47.7 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 523 | 1342 | 1531 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 281 | 0 | 7 | 158.1 | 5 | 20 | 73 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 144 | 454 | 556 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 156 | 760 | 45 | 14.3 | 172 | 675 | 905 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 456 | 0 | 45 | 199.2 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 305 | 699 | 90 | 43.0 | 219 | 866 | 1015 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 143 | 0 | 7 | 12.4 | 29 | 122 | 364 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 577 | 0 | 14 | 55.1 | 61 | 218 | 438 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 293 | 0 | 60 | 125.0 | 49 | 193 | 242 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Reorder | 21 | 0 | 14 | 22.0 | 6 | 21 | 49 | 30 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Healthy | 249 | 137 | 45 | 55.3 | 72 | 279 | 374 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 46.3 | 460 | 752 | 1023 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 43 | 45 | 30 | 29.3 | 13 | 59 | 103 | 0 | 30 |
| ITEM-0092 | B - Core Products | Healthy | 788 | 853 | 90 | 64.0 | 375 | 1496 | 1754 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 204 | 475 | 7 | 11.5 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 109 | 0 | 7 | 24.1 | 12 | 49 | 144 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6345 | 0 | 90 | 348.8 | 688 | 2344 | 2598 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3289 | 0 | 60 | 241.1 | 352 | 1185 | 1376 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 73 | 0 | 7 | 15.4 | 13 | 51 | 151 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 53 | 65 | 14 | 17.9 | 17 | 62 | 124 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 77.9 | 641 | 1503 | 1701 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 151 | 0 | 45 | 85.5 | 22 | 104 | 157 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 182 | 340 | 45 | 25.6 | 114 | 441 | 590 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1036 | 1265 | 90 | 63.8 | 621 | 2099 | 2326 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 401 | 498 | 60 | 36.6 | 225 | 894 | 1125 | 0 | 37 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 263 | 1049 | 1230 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Reorder | 1218 | 665 | 90 | 82.7 | 562 | 1902 | 2108 | 225 | — |
| ITEM-0112 | A - Top Movers | Healthy | 267 | 1292 | 60 | 14.8 | 459 | 1557 | 1809 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 46 | 0 | 14 | 32.6 | 7 | 29 | 71 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 246.0 | 92 | 138 | 202 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 78 | 50 | 45 | 50.9 | 19 | 90 | 136 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 506 | 242 | 90 | 87.6 | 178 | 704 | 826 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 152 | 125 | 30 | 25.1 | 65 | 253 | 380 | 0 | 26 |
| ITEM-0120 | C - Slow Moving | Healthy | 47 | 58 | 30 | 24.7 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 96 | 255 | 7 | 8.1 | 30 | 126 | 375 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 1000 | 45 | 0.0 | 362 | 800 | 1000 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 49.4 | 77 | 128 | 229 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 278 | 0 | 14 | 29.7 | 55 | 196 | 393 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 31 | 133 | 7 | 4.9 | 17 | 68 | 201 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 365 | 191 | 45 | 42.1 | 136 | 535 | 717 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1202 | 1042 | 90 | 111.8 | 623 | 1602 | 1828 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 391 | 0 | 14 | 67.3 | 34 | 122 | 244 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 180 | 255 | 60 | 44.4 | 66 | 314 | 436 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 130 | 163 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3363 | 0 | 60 | 248.1 | 348 | 1175 | 1365 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 178 | 0 | 14 | 25.2 | 51 | 157 | 256 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 479 | 238 | 30 | 32.6 | 194 | 651 | 856 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 819 | 799 | 60 | 44.1 | 473 | 1605 | 1865 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1846 | 0 | 45 | 181.6 | 159 | 627 | 841 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 939 | 635 | 60 | 63.6 | 650 | 1551 | 1860 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 268 | 463 | 45 | 24.9 | 169 | 665 | 891 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 384 | 0 | 7 | 31.9 | 33 | 130 | 382 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 791 | 0 | 60 | 172.4 | 95 | 375 | 472 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 57 | 636 | 90 | 20.5 | 86 | 339 | 398 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 73.8 | 310 | 525 | 825 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 528 | 0 | 60 | 149.9 | 74 | 289 | 363 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 167 | 0 | 60 | 123.2 | 23 | 106 | 147 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 317 | 0 | 14 | 42.5 | 43 | 155 | 312 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 483 | 514 | 30 | 27.3 | 235 | 785 | 1032 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
