# Synthetic Inventory Health

**Simulation date: 2026-11-22**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 24 |
| Healthy | 100 |
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
| ITEM-0001 | B - Core Products | Healthy | 328 | 302 | 30 | 24.9 | 140 | 549 | 826 | 0 | — |
| ITEM-0002 | B - Core Products | Healthy | 258 | 0 | 7 | 35.2 | 96 | 155 | 309 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 382 | 1107 | 60 | 25.3 | 389 | 1312 | 1524 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1755 | 0 | 45 | 452.6 | 62 | 241 | 322 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 109 | 150 | 14 | 15.8 | 41 | 145 | 289 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 71 | 46 | 45 | 47.7 | 19 | 88 | 133 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 140 | 0 | 14 | 24.1 | 34 | 122 | 244 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 167 | 0 | 60 | 127.4 | 22 | 102 | 142 | 0 | — |
| ITEM-0010 | B - Core Products | Excess | 427 | 0 | 90 | 222.1 | 60 | 235 | 276 | 0 | — |
| ITEM-0011 | A - Top Movers | Healthy | 1463 | 765 | 60 | 103.8 | 798 | 1659 | 1856 | 0 | — |
| ITEM-0012 | A - Top Movers | Excess | 1205 | 0 | 7 | 108.3 | 268 | 357 | 513 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 243 | 90 | 90 | 92.3 | 63 | 303 | 382 | 0 | — |
| ITEM-0014 | B - Core Products | Healthy | 257 | 0 | 7 | 19.3 | 34 | 141 | 421 | 0 | — |
| ITEM-0015 | C - Slow Moving | Healthy | 114 | 0 | 7 | 59.7 | 23 | 39 | 96 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 176 | 80 | 45 | 78.4 | 71 | 175 | 242 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 198 | 300 | 45 | 31.1 | 100 | 393 | 527 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1015 | 0 | 30 | 348.7 | 33 | 124 | 185 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2493 | 0 | 60 | 241.3 | 214 | 845 | 1062 | 0 | — |
| ITEM-0020 | B - Core Products | Lead-time risk | 101 | 0 | 14 | 18.0 | 33 | 118 | 236 | 135 | 18 |
| ITEM-0021 | C - Slow Moving | Excess | 523 | 0 | 60 | 553.8 | 17 | 75 | 103 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Healthy | 2232 | 0 | 90 | 144.5 | 592 | 1998 | 2214 | 0 | — |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 15 | 20 | 30 | 28.7 | 7 | 24 | 39 | 0 | — |
| ITEM-0027 | B - Core Products | Healthy | 961 | 971 | 60 | 77.6 | 632 | 1388 | 1648 | 0 | — |
| ITEM-0028 | C - Slow Moving | Healthy | 133 | 0 | 30 | 68.8 | 17 | 77 | 135 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 964 | 0 | 90 | 195.4 | 150 | 599 | 703 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 29 | 0 | 7 | 45.0 | 8 | 14 | 33 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1046 | 0 | 14 | 233.6 | 27 | 95 | 189 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 158 | 265 | 60 | 36.6 | 69 | 332 | 462 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 191 | 0 | 45 | 62.7 | 49 | 190 | 253 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 642 | 0 | 60 | 540.0 | 51 | 124 | 160 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 339 | 0 | 14 | 29.9 | 65 | 235 | 473 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 315 | 0 | 7 | 46.0 | 110 | 165 | 309 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 59 | 90 | 14 | 15.9 | 22 | 78 | 156 | 0 | — |
| ITEM-0038 | B - Core Products | Reorder | 168 | 183 | 30 | 19.8 | 91 | 354 | 532 | 181 | — |
| ITEM-0039 | B - Core Products | Healthy | 367 | 315 | 30 | 24.5 | 159 | 624 | 939 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4159 | 0 | 60 | 605.7 | 176 | 595 | 691 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 629 | 0 | 14 | 46.8 | 316 | 518 | 706 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 49 | 100 | 14 | 10.7 | 27 | 96 | 193 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 511 | 1357 | 1552 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 585 | 0 | 45 | 182.2 | 39 | 187 | 284 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 199 | 350 | 90 | 65.1 | 126 | 405 | 496 | 0 | — |
| ITEM-0046 | C - Slow Moving | Healthy | 272 | 98 | 60 | 108.3 | 108 | 262 | 337 | 0 | — |
| ITEM-0047 | B - Core Products | Lead-time risk | 35 | 1050 | 60 | 4.1 | 312 | 834 | 1013 | 0 | 5 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Excess | 488 | 0 | 14 | 150.4 | 87 | 136 | 204 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 59 | 0 | 45 | 94.8 | 10 | 39 | 58 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 150 | 502 | 60 | 25.5 | 188 | 547 | 723 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 234 | 0 | 7 | 23.9 | 23 | 102 | 307 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 128 | 0 | 7 | 17.3 | 20 | 80 | 235 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4087 | 0 | 60 | 507.4 | 205 | 697 | 810 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 126 | 100 | 14 | 18.0 | 52 | 158 | 256 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 372 | 1950 | 90 | 21.4 | 660 | 2241 | 2484 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Reorder | 851 | 0 | 30 | 63.2 | 455 | 873 | 1156 | 305 | — |
| ITEM-0060 | B - Core Products | Healthy | 409 | 0 | 45 | 113.3 | 57 | 224 | 299 | 0 | — |
| ITEM-0061 | B - Core Products | Healthy | 126 | 0 | 14 | 24.5 | 29 | 106 | 214 | 0 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 23 | 43 | 30 | 15.4 | 14 | 61 | 105 | 0 | — |
| ITEM-0063 | B - Core Products | Healthy | 385 | 0 | 14 | 62.4 | 36 | 129 | 258 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 471 | 160 | 60 | 89.4 | 215 | 537 | 647 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 341 | 790 | 60 | 26.7 | 263 | 1042 | 1310 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 65 | 367 | 45 | 11.4 | 90 | 352 | 471 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 138 | 245 | 14 | 8.4 | 122 | 370 | 601 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 228 | 0 | 30 | 57.3 | 44 | 168 | 251 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 19 | 85 | 7 | 7.2 | 6 | 28 | 107 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 319 | 0 | 45 | 108.8 | 82 | 217 | 305 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 6 | 25 | 7 | 9.5 | 3 | 9 | 28 | 0 | — |
| ITEM-0072 | B - Core Products | Healthy | 772 | 249 | 60 | 67.0 | 238 | 941 | 1183 | 0 | — |
| ITEM-0073 | B - Core Products | Excess | 3351 | 0 | 90 | 869.1 | 118 | 469 | 550 | 0 | — |
| ITEM-0074 | C - Slow Moving | Lead-time risk | 9 | 60 | 14 | 4.6 | 9 | 39 | 98 | 0 | 5 |
| ITEM-0075 | C - Slow Moving | Healthy | 42 | 28 | 45 | 45.5 | 13 | 56 | 84 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 1350 | 90 | 0.0 | 523 | 1342 | 1531 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 275 | 0 | 7 | 152.8 | 5 | 20 | 74 | 0 | — |
| ITEM-0078 | C - Slow Moving | Stockout | 0 | 525 | 90 | 0.0 | 144 | 454 | 556 | 0 | 1 |
| ITEM-0079 | B - Core Products | Healthy | 398 | 495 | 45 | 36.2 | 173 | 679 | 910 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 448 | 0 | 45 | 192.0 | 29 | 137 | 207 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 299 | 699 | 90 | 42.9 | 215 | 849 | 996 | 0 | — |
| ITEM-0082 | B - Core Products | Reorder | 120 | 0 | 7 | 10.4 | 29 | 122 | 365 | 245 | — |
| ITEM-0083 | B - Core Products | Healthy | 560 | 0 | 14 | 53.8 | 61 | 218 | 436 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 287 | 0 | 60 | 121.8 | 49 | 193 | 243 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 242 | 465 | 14 | 19.2 | 253 | 442 | 707 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 17 | 30 | 14 | 17.0 | 6 | 21 | 51 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 244 | 137 | 45 | 54.4 | 56 | 263 | 398 | 0 | — |
| ITEM-0089 | A - Top Movers | Healthy | 899 | 0 | 14 | 52.0 | 433 | 693 | 935 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Lead-time risk | 41 | 45 | 30 | 28.6 | 13 | 58 | 101 | 0 | 29 |
| ITEM-0092 | B - Core Products | Healthy | 769 | 853 | 90 | 62.9 | 372 | 1486 | 1743 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 204 | 475 | 7 | 11.5 | 263 | 405 | 778 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 100 | 0 | 7 | 22.4 | 12 | 48 | 142 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6302 | 0 | 90 | 342.1 | 696 | 2373 | 2631 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3257 | 0 | 60 | 237.9 | 353 | 1189 | 1380 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 202 | 0 | 7 | 51.9 | 72 | 104 | 185 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 55 | 0 | 7 | 11.4 | 14 | 53 | 154 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 44 | 65 | 14 | 14.9 | 17 | 62 | 123 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 1100 | 675 | 60 | 77.9 | 641 | 1503 | 1701 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 144 | 0 | 45 | 80.0 | 23 | 106 | 160 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 548 | 689 | 90 | 93.4 | 296 | 830 | 954 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 354 | 160 | 45 | 50.3 | 113 | 438 | 585 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1000 | 1265 | 90 | 61.8 | 620 | 2094 | 2320 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 373 | 498 | 60 | 33.8 | 226 | 899 | 1130 | 259 | 34 |
| ITEM-0108 | C - Slow Moving | Excess | 478 | 0 | 30 | 256.1 | 53 | 111 | 167 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 265 | 1056 | 1239 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 475 | 0 | 60 | 152.1 | 101 | 292 | 386 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1188 | 890 | 90 | 81.6 | 555 | 1880 | 2084 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 238 | 1563 | 60 | 13.1 | 462 | 1569 | 1822 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 1145 | 475 | 45 | 76.6 | 719 | 1407 | 1616 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 43 | 0 | 14 | 30.7 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 593 | 0 | 14 | 124.1 | 129 | 201 | 301 | 0 | — |
| ITEM-0116 | C - Slow Moving | Healthy | 75 | 50 | 45 | 48.9 | 19 | 90 | 136 | 0 | — |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Healthy | 497 | 242 | 90 | 86.2 | 178 | 703 | 824 | 0 | — |
| ITEM-0119 | B - Core Products | Lead-time risk | 146 | 125 | 30 | 24.5 | 64 | 249 | 375 | 0 | 25 |
| ITEM-0120 | C - Slow Moving | Healthy | 44 | 58 | 30 | 23.3 | 16 | 75 | 132 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 74 | 255 | 7 | 6.2 | 30 | 125 | 374 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 238 | 762 | 45 | 25.0 | 362 | 800 | 1000 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 63 | 222 | 14 | 13.9 | 121 | 189 | 285 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 239 | 0 | 14 | 25.1 | 56 | 199 | 399 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 157 | 0 | 7 | 25.2 | 17 | 67 | 198 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 831 | 0 | 30 | 164.7 | 288 | 445 | 515 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 335 | 374 | 45 | 37.8 | 139 | 547 | 733 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1621 | 623 | 90 | 161.4 | 607 | 1522 | 1732 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 379 | 0 | 14 | 65.6 | 34 | 121 | 242 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 172 | 255 | 60 | 42.4 | 66 | 314 | 436 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 175 | 90 | 0.0 | 29 | 134 | 168 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3324 | 0 | 60 | 246.4 | 346 | 1169 | 1358 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 51 | 43 | 45 | 51.6 | 27 | 73 | 103 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 160 | 0 | 14 | 22.4 | 51 | 159 | 259 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 440 | 238 | 30 | 29.8 | 196 | 654 | 860 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 786 | 1087 | 60 | 42.3 | 473 | 1607 | 1868 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 1829 | 0 | 45 | 182.1 | 158 | 621 | 831 | 0 | — |
| ITEM-0142 | B - Core Products | Healthy | 939 | 635 | 60 | 63.6 | 650 | 1551 | 1860 | 0 | — |
| ITEM-0143 | B - Core Products | Healthy | 253 | 463 | 45 | 23.8 | 167 | 657 | 881 | 0 | — |
| ITEM-0144 | B - Core Products | Healthy | 360 | 0 | 7 | 29.5 | 33 | 131 | 388 | 0 | — |
| ITEM-0145 | B - Core Products | Excess | 781 | 0 | 60 | 171.9 | 94 | 372 | 467 | 0 | — |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 45 | 636 | 90 | 15.8 | 88 | 347 | 407 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 1055 | 0 | 14 | 73.8 | 310 | 525 | 825 | 0 | — |
| ITEM-0149 | B - Core Products | Healthy | 655 | 0 | 14 | 54.6 | 237 | 417 | 669 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 515 | 0 | 60 | 143.1 | 75 | 295 | 371 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 584 | 400 | 90 | 151.9 | 296 | 646 | 727 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 165 | 0 | 60 | 122.7 | 23 | 106 | 146 | 0 | — |
| ITEM-0155 | B - Core Products | Healthy | 296 | 0 | 14 | 39.1 | 43 | 157 | 316 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 448 | 514 | 30 | 25.3 | 234 | 784 | 1032 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 529 | 0 | 7 | 23.2 | 330 | 513 | 831 | 0 | — |
