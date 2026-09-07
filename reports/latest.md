# Synthetic Inventory Health

**Simulation date: 2026-09-07**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 27 |
| Healthy | 63 |
| Lead-time risk | 29 |
| Stockout | 19 |

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
| ITEM-0001 | B - Core Products | Stockout | 0 | 728 | 30 | 0.0 | 129 | 502 | 754 | 0 | 1 |
| ITEM-0002 | B - Core Products | Healthy | 307 | 0 | 7 | 44.1 | 99 | 155 | 301 | 0 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 1030 | 294 | 60 | 67.5 | 390 | 1322 | 1535 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 2048 | 0 | 45 | 295.4 | 112 | 431 | 577 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 321 | 0 | 14 | 42.4 | 43 | 157 | 316 | 0 | — |
| ITEM-0007 | C - Slow Moving | Stockout | 0 | 142 | 45 | 0.0 | 20 | 94 | 141 | 0 | 1 |
| ITEM-0008 | B - Core Products | Healthy | 313 | 0 | 14 | 32.8 | 60 | 204 | 404 | 0 | — |
| ITEM-0009 | C - Slow Moving | Lead-time risk | 67 | 198 | 60 | 29.3 | 38 | 178 | 247 | 0 | 30 |
| ITEM-0010 | B - Core Products | Lead-time risk | 156 | 410 | 90 | 43.7 | 111 | 436 | 511 | 0 | 44 |
| ITEM-0011 | A - Top Movers | Lead-time risk | 147 | 2145 | 60 | 9.0 | 873 | 1872 | 2101 | 0 | 9 |
| ITEM-0012 | A - Top Movers | Excess | 1879 | 0 | 7 | 96.8 | 337 | 493 | 765 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 445 | 0 | 90 | 158.9 | 67 | 322 | 406 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 1280 | 0 | 7 | 100.7 | 33 | 135 | 402 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 286 | 0 | 7 | 122.6 | 28 | 47 | 117 | 0 | — |
| ITEM-0016 | C - Slow Moving | Lead-time risk | 78 | 235 | 45 | 26.3 | 84 | 221 | 310 | 0 | 27 |
| ITEM-0017 | B - Core Products | Stockout | 0 | 510 | 45 | 0.0 | 104 | 412 | 553 | 0 | 1 |
| ITEM-0018 | B - Core Products | Excess | 1234 | 0 | 30 | 224.8 | 62 | 233 | 348 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 3262 | 0 | 60 | 318.1 | 212 | 838 | 1053 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 82 | 323 | 14 | 8.1 | 61 | 214 | 427 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 592 | 0 | 60 | 372.6 | 27 | 124 | 172 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Lead-time risk | 6 | 2305 | 90 | 0.3 | 658 | 2237 | 2480 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 13 | 45 | 30 | 18.3 | 8 | 31 | 52 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 1161 | 717 | 60 | 104.5 | 773 | 1451 | 1607 | 0 | — |
| ITEM-0028 | C - Slow Moving | Stockout | 0 | 243 | 30 | 0.0 | 31 | 138 | 240 | 0 | 1 |
| ITEM-0029 | B - Core Products | Lead-time risk | 360 | 960 | 90 | 41.2 | 271 | 1066 | 1250 | 0 | 42 |
| ITEM-0030 | C - Slow Moving | Healthy | 32 | 0 | 7 | 68.6 | 6 | 10 | 24 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1377 | 0 | 14 | 154.5 | 53 | 187 | 374 | 0 | — |
| ITEM-0032 | C - Slow Moving | Stockout | 0 | 395 | 60 | 0.0 | 63 | 301 | 418 | 0 | 1 |
| ITEM-0033 | B - Core Products | Healthy | 420 | 0 | 45 | 70.1 | 99 | 375 | 501 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 722 | 0 | 60 | 306.5 | 76 | 220 | 291 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 439 | 0 | 14 | 40.2 | 63 | 227 | 457 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 233 | 0 | 7 | 25.9 | 133 | 205 | 394 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 230 | 0 | 14 | 31.4 | 43 | 153 | 307 | 0 | — |
| ITEM-0038 | B - Core Products | Stockout | 0 | 484 | 30 | 0.0 | 84 | 330 | 496 | 0 | 1 |
| ITEM-0039 | B - Core Products | Lead-time risk | 83 | 575 | 30 | 6.1 | 148 | 573 | 861 | 0 | 7 |
| ITEM-0040 | A - Top Movers | Excess | 4678 | 0 | 60 | 358.9 | 341 | 1137 | 1319 | 0 | — |
| ITEM-0041 | B - Core Products | Healthy | 611 | 0 | 14 | 37.4 | 284 | 530 | 873 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 274 | 0 | 14 | 32.9 | 53 | 178 | 353 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 1515 | 90 | 0.0 | 518 | 1327 | 1514 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 826 | 0 | 45 | 242.9 | 42 | 199 | 301 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 439 | 0 | 90 | 171.8 | 116 | 349 | 426 | 0 | — |
| ITEM-0046 | C - Slow Moving | Lead-time risk | 22 | 192 | 60 | 12.1 | 81 | 192 | 246 | 0 | 13 |
| ITEM-0047 | C - Slow Moving | Healthy | 379 | 175 | 60 | 85.3 | 172 | 444 | 577 | 0 | — |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 482 | 0 | 14 | 47.7 | 183 | 335 | 547 | 0 | — |
| ITEM-0050 | C - Slow Moving | Lead-time risk | 29 | 80 | 45 | 24.9 | 16 | 70 | 105 | 0 | 25 |
| ITEM-0051 | C - Slow Moving | Lead-time risk | 7 | 290 | 60 | 3.4 | 116 | 244 | 307 | 0 | 4 |
| ITEM-0052 | B - Core Products | Healthy | 322 | 0 | 7 | 32.0 | 27 | 108 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 230 | 0 | 7 | 31.7 | 20 | 79 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4691 | 0 | 60 | 342.1 | 361 | 1198 | 1390 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 659 | 0 | 14 | 54.4 | 97 | 279 | 449 | 0 | — |
| ITEM-0056 | A - Top Movers | Lead-time risk | 1718 | 580 | 90 | 98.2 | 664 | 2256 | 2501 | 0 | 99 |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Stockout | 0 | 1209 | 30 | 0.0 | 435 | 897 | 1209 | 0 | 1 |
| ITEM-0060 | B - Core Products | Lead-time risk | 3 | 564 | 45 | 0.5 | 103 | 389 | 520 | 0 | 1 |
| ITEM-0061 | B - Core Products | Lead-time risk | 4 | 145 | 14 | 0.8 | 29 | 104 | 209 | 0 | 1 |
| ITEM-0062 | C - Slow Moving | Healthy | 139 | 0 | 30 | 51.7 | 24 | 108 | 189 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 842 | 0 | 14 | 124.8 | 38 | 140 | 281 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 569 | 310 | 60 | 87.2 | 260 | 658 | 795 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 1326 | 0 | 60 | 111.5 | 246 | 972 | 1221 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 501 | 0 | 45 | 86.9 | 90 | 356 | 477 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 645 | 0 | 14 | 38.6 | 122 | 373 | 607 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 145 | 390 | 30 | 18.6 | 87 | 329 | 493 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 38 | 0 | 7 | 13.2 | 7 | 31 | 117 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 146 | 104 | 45 | 53.9 | 81 | 206 | 288 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 29 | 0 | 7 | 34.8 | 3 | 10 | 35 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 239 | 943 | 1185 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3641 | 0 | 90 | 494.3 | 228 | 899 | 1054 | 0 | — |
| ITEM-0074 | C - Slow Moving | Stockout | 0 | 99 | 14 | 0.0 | 10 | 43 | 107 | 0 | 1 |
| ITEM-0075 | C - Slow Moving | Stockout | 0 | 66 | 45 | 0.0 | 12 | 49 | 72 | 0 | 1 |
| ITEM-0076 | B - Core Products | Lead-time risk | 133 | 441 | 90 | 69.6 | 209 | 383 | 424 | 0 | 70 |
| ITEM-0077 | C - Slow Moving | Excess | 407 | 0 | 7 | 119.3 | 9 | 37 | 139 | 0 | — |
| ITEM-0078 | C - Slow Moving | Lead-time risk | 181 | 170 | 90 | 90.5 | 104 | 286 | 346 | 0 | 91 |
| ITEM-0079 | B - Core Products | Healthy | 691 | 275 | 45 | 54.5 | 198 | 782 | 1049 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 629 | 0 | 45 | 256.2 | 30 | 143 | 217 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 657 | 235 | 90 | 94.5 | 212 | 845 | 992 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 273 | 0 | 7 | 25.3 | 28 | 115 | 341 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 1358 | 0 | 14 | 129.5 | 61 | 219 | 439 | 0 | — |
| ITEM-0084 | B - Core Products | Lead-time risk | 133 | 337 | 60 | 32.5 | 87 | 337 | 423 | 0 | 33 |
| ITEM-0085 | B - Core Products | Stockout | 0 | 465 | 14 | 0.0 | 189 | 283 | 413 | 0 | 1 |
| ITEM-0086 | C - Slow Moving | Healthy | 56 | 0 | 14 | 32.1 | 9 | 36 | 88 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | B - Core Products | Stockout | 0 | 365 | 45 | 0.0 | 69 | 272 | 365 | 0 | 1 |
| ITEM-0089 | A - Top Movers | Healthy | 49 | 735 | 14 | 3.6 | 377 | 579 | 768 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 97 | 0 | 30 | 62.8 | 14 | 62 | 109 | 0 | — |
| ITEM-0092 | B - Core Products | Healthy | 1234 | 436 | 90 | 92.5 | 409 | 1623 | 1903 | 0 | — |
| ITEM-0093 | B - Core Products | Healthy | 365 | 385 | 7 | 21.2 | 248 | 387 | 749 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 235 | 0 | 7 | 31.6 | 24 | 84 | 240 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 7665 | 0 | 90 | 420.6 | 692 | 2351 | 2606 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 4327 | 0 | 60 | 325.1 | 344 | 1156 | 1343 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 327 | 0 | 7 | 53.4 | 98 | 147 | 276 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 303 | 0 | 7 | 31.6 | 31 | 108 | 309 | 0 | — |
| ITEM-0100 | B - Core Products | Stockout | 0 | 256 | 14 | 0.0 | 36 | 123 | 244 | 0 | 1 |
| ITEM-0101 | B - Core Products | Healthy | 1086 | 420 | 60 | 84.9 | 539 | 1320 | 1588 | 0 | — |
| ITEM-0102 | C - Slow Moving | Lead-time risk | 72 | 210 | 45 | 24.2 | 37 | 174 | 264 | 0 | 25 |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 957 | 422 | 90 | 103.3 | 420 | 1264 | 1458 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 716 | 0 | 45 | 90.5 | 124 | 488 | 655 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1669 | 773 | 90 | 96.4 | 661 | 2238 | 2480 | 0 | — |
| ITEM-0107 | B - Core Products | Healthy | 717 | 241 | 60 | 66.2 | 224 | 885 | 1113 | 0 | — |
| ITEM-0108 | C - Slow Moving | Excess | 601 | 0 | 30 | 226.3 | 61 | 144 | 223 | 0 | — |
| ITEM-0109 | B - Core Products | Lead-time risk | 271 | 915 | 90 | 29.4 | 282 | 1122 | 1315 | 0 | 30 |
| ITEM-0110 | C - Slow Moving | Excess | 714 | 0 | 60 | 262.3 | 103 | 270 | 351 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 2285 | 0 | 90 | 147.5 | 586 | 1996 | 2213 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 1288 | 360 | 60 | 75.3 | 440 | 1484 | 1724 | 0 | — |
| ITEM-0113 | A - Top Movers | Lead-time risk | 554 | 1395 | 45 | 28.3 | 894 | 1795 | 2068 | 0 | 29 |
| ITEM-0114 | C - Slow Moving | Healthy | 55 | 0 | 14 | 36.9 | 8 | 31 | 75 | 0 | — |
| ITEM-0115 | A - Top Movers | Healthy | 1004 | 0 | 14 | 59.3 | 370 | 624 | 861 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 81 | 122 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Lead-time risk | 171 | 530 | 90 | 31.2 | 168 | 667 | 782 | 0 | 32 |
| ITEM-0119 | B - Core Products | Stockout | 0 | 355 | 30 | 0.0 | 64 | 252 | 379 | 0 | 1 |
| ITEM-0120 | C - Slow Moving | Healthy | 77 | 0 | 30 | 42.3 | 16 | 73 | 128 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 375 | 0 | 7 | 28.2 | 36 | 143 | 422 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 113 | 285 | 45 | 36.2 | 188 | 332 | 398 | 0 | — |
| ITEM-0123 | B - Core Products | Healthy | 15 | 218 | 14 | 5.2 | 93 | 137 | 198 | 0 | — |
| ITEM-0124 | B - Core Products | Lead-time risk | 29 | 292 | 14 | 2.8 | 60 | 218 | 438 | 0 | 3 |
| ITEM-0125 | B - Core Products | Healthy | 118 | 0 | 7 | 19.3 | 17 | 66 | 195 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Lead-time risk | 151 | 990 | 30 | 13.0 | 482 | 843 | 1006 | 0 | 13 |
| ITEM-0128 | B - Core Products | Stockout | 0 | 698 | 45 | 0.0 | 141 | 557 | 746 | 0 | 1 |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 1485 | 697 | 90 | 113.1 | 711 | 1907 | 2182 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 824 | 0 | 14 | 132.4 | 35 | 129 | 259 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 476 | 0 | 60 | 113.0 | 68 | 325 | 452 | 0 | — |
| ITEM-0134 | C - Slow Moving | Lead-time risk | 2 | 135 | 90 | 2.2 | 24 | 108 | 136 | 0 | 3 |
| ITEM-0135 | A - Top Movers | Excess | 4366 | 0 | 60 | 320.2 | 350 | 1182 | 1373 | 0 | — |
| ITEM-0136 | C - Slow Moving | Lead-time risk | 7 | 102 | 45 | 6.7 | 27 | 76 | 107 | 0 | 7 |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 720 | 0 | 14 | 55.1 | 101 | 297 | 480 | 0 | — |
| ITEM-0139 | A - Top Movers | Lead-time risk | 137 | 560 | 30 | 9.3 | 195 | 654 | 861 | 0 | 10 |
| ITEM-0140 | A - Top Movers | Healthy | 1913 | 0 | 60 | 105.0 | 466 | 1578 | 1833 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2609 | 0 | 45 | 265.6 | 155 | 607 | 814 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1540 | 60 | 0.0 | 584 | 1375 | 1647 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 564 | 243 | 45 | 51.8 | 169 | 670 | 898 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 1295 | 0 | 7 | 101.3 | 37 | 140 | 408 | 0 | — |
| ITEM-0145 | B - Core Products | Lead-time risk | 13 | 888 | 60 | 1.6 | 173 | 673 | 845 | 0 | 2 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Lead-time risk | 257 | 636 | 90 | 43.7 | 181 | 716 | 840 | 0 | 44 |
| ITEM-0148 | B - Core Products | Stockout | 0 | 995 | 14 | 0.0 | 327 | 598 | 977 | 0 | 1 |
| ITEM-0149 | B - Core Products | Excess | 1518 | 0 | 14 | 119.2 | 254 | 445 | 713 | 0 | — |
| ITEM-0150 | B - Core Products | Healthy | 614 | 178 | 60 | 87.6 | 149 | 577 | 724 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 930 | 400 | 90 | 149.7 | 389 | 955 | 1085 | 0 | — |
| ITEM-0154 | C - Slow Moving | Lead-time risk | 66 | 200 | 60 | 28.4 | 38 | 180 | 250 | 0 | 29 |
| ITEM-0155 | B - Core Products | Excess | 875 | 0 | 14 | 125.4 | 41 | 146 | 293 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Lead-time risk | 107 | 930 | 30 | 5.9 | 240 | 801 | 1053 | 0 | 6 |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 498 | 0 | 7 | 22.2 | 305 | 485 | 798 | 0 | — |
