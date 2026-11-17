# Synthetic Inventory Health

**Simulation date: 2026-11-17**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 25 |
| Healthy | 95 |
| Lead-time risk | 5 |
| Reorder | 6 |
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
| ITEM-0001 | B - Core Products | Healthy | 415 | 302 | 30 | 32.4 | 136 | 534 | 803 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 107 | 190 | 7 | 15.5 | 94 | 150 | 294 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Reorder | 436 | 884 | 60 | 28.4 | 393 | 1329 | 1543 | 223 | — |
| ITEM-0005 | B - Core Products | Excess | 1783 | 0 | 45 | 462.4 | 61 | 239 | 320 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 145 | 0 | 14 | 21.1 | 41 | 144 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 80 | 46 | 45 | 53.7 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | A - Top Movers | Healthy | 50 | 125 | 14 | 8.8 | 40 | 125 | 205 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 175 | 0 | 60 | 135.8 | 22 | 101 | 140 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 441 | 0 | 90 | 234.9 | 58 | 229 | 269 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 88.4 | 894 | 1904 | 2135 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 259 | 90 | 90 | 98.4 | 63 | 303 | 382 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 338 | 0 | 7 | 25.8 | 33 | 138 | 413 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 57.6 | 23 | 39 | 99 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 77.3 | 71 | 176 | 245 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 225 | 300 | 45 | 34.8 | 102 | 400 | 536 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1033 | 0 | 30 | 366.0 | 32 | 120 | 179 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2542 | 0 | 60 | 240.6 | 219 | 864 | 1086 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 145 | 0 | 14 | 26.6 | 32 | 114 | 228 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 527 | 0 | 60 | 558.0 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 594 | 2005 | 2222 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 18 | 20 | 30 | 34.5 | 7 | 24 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 67.0 | 684 | 1560 | 1861 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 149 | 0 | 30 | 79.8 | 16 | 74 | 130 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 992 | 0 | 90 | 202.9 | 149 | 594 | 697 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 4 | 30 | 7 | 6.3 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1065 | 0 | 14 | 229.3 | 27 | 97 | 195 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 181 | 265 | 60 | 42.5 | 68 | 328 | 456 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 216 | 0 | 45 | 73.1 | 48 | 184 | 247 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 142 | 245 | 14 | 12.5 | 66 | 237 | 475 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 82 | 0 | 14 | 22.0 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 34 | 355 | 30 | 4.0 | 91 | 355 | 533 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 438 | 315 | 30 | 29.1 | 159 | 626 | 942 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4196 | 0 | 60 | 614.0 | 175 | 592 | 688 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 351 | 335 | 14 | 27.4 | 252 | 445 | 714 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 73 | 100 | 14 | 15.9 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 521 | 1415 | 1622 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 600 | 0 | 45 | 187.5 | 39 | 187 | 283 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 57.8 | 138 | 452 | 555 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.0 | 314 | 844 | 1026 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 60 | 0 | 45 | 90.0 | 10 | 41 | 61 | 0 | — |
| ITEM-0051 | B - Core Products | Healthy | 150 | 502 | 60 | 25.5 | 242 | 601 | 724 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 61 | 210 | 7 | 6.2 | 23 | 102 | 310 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 165 | 0 | 7 | 22.5 | 20 | 79 | 233 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4137 | 0 | 60 | 522.9 | 202 | 685 | 796 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 177 | 0 | 14 | 26.0 | 50 | 153 | 248 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 476 | 1950 | 90 | 27.8 | 651 | 2212 | 2452 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1018 | 0 | 30 | 80.2 | 439 | 833 | 1100 | 0 | — |
| ITEM-0060 | B - Core Products | Healthy | 428 | 0 | 45 | 122.3 | 55 | 216 | 290 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 45 | 105 | 14 | 8.8 | 29 | 106 | 213 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 38 | 43 | 30 | 26.5 | 13 | 58 | 101 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 409 | 0 | 14 | 66.2 | 36 | 129 | 259 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 272 | 470 | 60 | 67.4 | 179 | 426 | 510 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 413 | 790 | 60 | 33.7 | 253 | 1002 | 1259 | 0 | — |
| ITEM-0066 | B - Core Products | Reorder | 98 | 246 | 45 | 17.5 | 89 | 347 | 465 | 121 | — |
| ITEM-0067 | A - Top Movers | Healthy | 222 | 245 | 14 | 13.5 | 120 | 367 | 598 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 249 | 0 | 30 | 61.2 | 45 | 172 | 257 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 33 | 0 | 7 | 12.4 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Reorder | 8 | 0 | 7 | 12.0 | 3 | 9 | 29 | 25 | — |
| ITEM-0072 | B - Core Products | Healthy | 844 | 249 | 60 | 75.4 | 231 | 914 | 1149 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3374 | 0 | 90 | 862.7 | 119 | 475 | 558 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 20 | 60 | 14 | 10.1 | 9 | 39 | 99 | 0 | 11 |
| ITEM-0075 | C - Slow Moving | Healthy | 47 | 28 | 45 | 52.9 | 13 | 54 | 81 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 477 | 1186 | 1350 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 286 | 0 | 7 | 158.9 | 5 | 20 | 74 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 140 | 430 | 525 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 173 | 515 | 45 | 15.6 | 174 | 686 | 920 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 464 | 0 | 45 | 202.7 | 28 | 134 | 202 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 323 | 547 | 90 | 45.4 | 219 | 868 | 1017 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 175 | 0 | 7 | 15.3 | 29 | 121 | 362 | 0 | — |
| ITEM-0083 | B - Core Products | Healthy | 599 | 0 | 14 | 56.7 | 61 | 220 | 442 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 300 | 0 | 60 | 126.2 | 50 | 196 | 245 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 25 | 0 | 14 | 25.9 | 6 | 21 | 50 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Reorder | 261 | 0 | 45 | 58.0 | 56 | 263 | 398 | 137 | — |
| ITEM-0089 | A - Top Movers | Healthy | 974 | 0 | 14 | 52.4 | 456 | 735 | 995 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 48 | 45 | 30 | 32.7 | 13 | 59 | 103 | 0 | 33 |
| ITEM-0092 | B - Core Products | Healthy | 395 | 1289 | 90 | 32.0 | 375 | 1499 | 1758 | 0 | — |
| ITEM-0093 | B - Core Products | Reorder | 353 | 0 | 7 | 18.5 | 275 | 428 | 828 | 475 | — |
| ITEM-0094 | B - Core Products | Healthy | 123 | 0 | 7 | 27.3 | 12 | 49 | 143 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6396 | 0 | 90 | 353.2 | 685 | 2334 | 2587 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3318 | 0 | 60 | 241.8 | 353 | 1191 | 1383 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.5 | 72 | 104 | 186 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 83 | 0 | 7 | 17.2 | 14 | 53 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 64 | 0 | 14 | 21.5 | 17 | 62 | 125 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 67.8 | 732 | 1722 | 1949 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 158 | 0 | 45 | 90.0 | 22 | 103 | 156 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 192 | 340 | 45 | 26.3 | 116 | 452 | 605 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1088 | 1265 | 90 | 67.0 | 622 | 2100 | 2327 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 428 | 498 | 60 | 38.3 | 229 | 912 | 1147 | 0 | 39 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 262 | 1044 | 1224 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1273 | 665 | 90 | 87.7 | 554 | 1876 | 2079 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 324 | 1292 | 60 | 18.3 | 454 | 1536 | 1784 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1231 | 475 | 45 | 88.0 | 705 | 1349 | 1545 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 51 | 0 | 14 | 37.0 | 7 | 28 | 69 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 749 | 0 | 14 | 153.6 | 144 | 218 | 320 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 80 | 50 | 45 | 51.4 | 19 | 91 | 138 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 524 | 242 | 90 | 92.1 | 176 | 694 | 814 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 172 | 125 | 30 | 28.8 | 64 | 250 | 375 | 0 | 29 |
| ITEM-0120 | C - Slow Moving | Healthy | 51 | 58 | 30 | 26.4 | 17 | 77 | 135 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 132 | 0 | 7 | 11.0 | 31 | 127 | 379 | 0 | — |
| ITEM-0122 | B - Core Products | Stockout | 0 | 794 | 45 | 0.0 | 346 | 741 | 921 | 0 | 1 |
| ITEM-0123 | C - Slow Moving | Healthy | 167 | 0 | 14 | 49.4 | 77 | 128 | 229 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 301 | 0 | 14 | 32.0 | 55 | 197 | 394 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 55 | 133 | 7 | 9.0 | 17 | 67 | 196 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 901 | 0 | 30 | 211.2 | 275 | 408 | 467 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 379 | 191 | 45 | 43.2 | 137 | 541 | 726 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1202 | 1042 | 90 | 111.8 | 623 | 1602 | 1828 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 398 | 0 | 14 | 66.0 | 35 | 126 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Reorder | 186 | 130 | 60 | 45.4 | 67 | 318 | 441 | 125 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3404 | 0 | 60 | 251.3 | 348 | 1175 | 1364 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 56 | 43 | 45 | 60.0 | 27 | 70 | 98 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 190 | 0 | 14 | 26.6 | 51 | 159 | 259 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 517 | 238 | 30 | 34.5 | 198 | 663 | 872 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 856 | 799 | 60 | 45.5 | 479 | 1627 | 1890 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1889 | 0 | 45 | 187.2 | 158 | 623 | 834 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 985 | 635 | 60 | 69.1 | 645 | 1514 | 1814 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 294 | 463 | 45 | 27.6 | 168 | 659 | 883 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 417 | 0 | 7 | 33.4 | 36 | 136 | 398 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 814 | 0 | 60 | 183.6 | 92 | 363 | 456 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 68 | 636 | 90 | 24.4 | 86 | 340 | 399 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 65.6 | 327 | 569 | 907 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 544 | 0 | 60 | 152.5 | 75 | 293 | 368 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 125.1 | 327 | 752 | 850 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 172 | 0 | 60 | 127.9 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 346 | 0 | 14 | 47.3 | 42 | 152 | 306 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 549 | 259 | 30 | 31.0 | 235 | 785 | 1033 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
