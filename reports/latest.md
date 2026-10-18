# Synthetic Inventory Health

**Simulation date: 2026-10-18**

All products, quantities, demand, and supplier lead times are fictional. No financial fields.

Snapshot: after demand and receipts, before new simulated orders. No real orders are placed.

## Health summary

| Status | Items |
|---|---:|
| Dead inventory | 22 |
| Excess | 30 |
| Healthy | 91 |
| Lead-time risk | 3 |
| Reorder | 2 |
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
| ITEM-0001 | B - Core Products | Healthy | 451 | 291 | 30 | 34.6 | 138 | 543 | 816 | 0 | — |
| ITEM-0002 | B - Core Products | Reorder | 143 | 0 | 7 | 19.3 | 97 | 157 | 312 | 170 | — |
| ITEM-0003 | Dead Inv | Dead inventory | 35 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0004 | A - Top Movers | Healthy | 395 | 968 | 60 | 25.7 | 394 | 1332 | 1547 | 0 | — |
| ITEM-0005 | B - Core Products | Excess | 1901 | 0 | 45 | 406.4 | 75 | 291 | 389 | 0 | — |
| ITEM-0006 | B - Core Products | Healthy | 198 | 0 | 14 | 27.3 | 42 | 151 | 304 | 0 | — |
| ITEM-0007 | C - Slow Moving | Healthy | 124 | 0 | 45 | 78.0 | 20 | 94 | 141 | 0 | — |
| ITEM-0008 | B - Core Products | Healthy | 92 | 145 | 14 | 14.2 | 39 | 137 | 273 | 0 | — |
| ITEM-0009 | C - Slow Moving | Healthy | 218 | 0 | 60 | 158.2 | 24 | 109 | 150 | 0 | — |
| ITEM-0010 | B - Core Products | Healthy | 93 | 410 | 90 | 44.1 | 66 | 259 | 303 | 0 | — |
| ITEM-0011 | A - Top Movers | Stockout | 0 | 2145 | 60 | 0.0 | 732 | 1495 | 1670 | 0 | 1 |
| ITEM-0012 | A - Top Movers | Excess | 1632 | 0 | 7 | 172.2 | 247 | 323 | 456 | 0 | — |
| ITEM-0013 | C - Slow Moving | Healthy | 331 | 90 | 90 | 114.1 | 69 | 333 | 420 | 0 | — |
| ITEM-0014 | B - Core Products | Excess | 754 | 0 | 7 | 59.6 | 32 | 134 | 399 | 0 | — |
| ITEM-0015 | C - Slow Moving | Excess | 199 | 0 | 7 | 139.9 | 21 | 33 | 76 | 0 | — |
| ITEM-0016 | C - Slow Moving | Healthy | 235 | 0 | 45 | 105.8 | 72 | 175 | 241 | 0 | — |
| ITEM-0017 | B - Core Products | Healthy | 416 | 0 | 45 | 61.9 | 105 | 415 | 556 | 0 | — |
| ITEM-0018 | B - Core Products | Excess | 1123 | 0 | 30 | 323.9 | 40 | 148 | 221 | 0 | — |
| ITEM-0019 | B - Core Products | Excess | 2849 | 0 | 60 | 274.5 | 215 | 849 | 1066 | 0 | — |
| ITEM-0020 | B - Core Products | Healthy | 204 | 0 | 14 | 32.7 | 37 | 131 | 262 | 0 | — |
| ITEM-0021 | C - Slow Moving | Excess | 561 | 0 | 60 | 548.8 | 19 | 82 | 113 | 0 | — |
| ITEM-0022 | Dead Inv | Dead inventory | 99 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0023 | Dead Inv | Dead inventory | 65 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0024 | A - Top Movers | Stockout | 0 | 2305 | 90 | 0.0 | 607 | 2059 | 2283 | 0 | 1 |
| ITEM-0025 | Dead Inv | Dead inventory | 21 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0026 | C - Slow Moving | Healthy | 37 | 0 | 30 | 65.3 | 7 | 25 | 42 | 0 | — |
| ITEM-0027 | A - Top Movers | Healthy | 500 | 1169 | 60 | 41.6 | 766 | 1501 | 1669 | 0 | — |
| ITEM-0028 | B - Core Products | Healthy | 201 | 0 | 30 | 88.2 | 26 | 97 | 145 | 0 | — |
| ITEM-0029 | B - Core Products | Healthy | 193 | 960 | 90 | 34.9 | 171 | 675 | 791 | 0 | — |
| ITEM-0030 | C - Slow Moving | Healthy | 10 | 20 | 7 | 18.8 | 6 | 11 | 27 | 0 | — |
| ITEM-0031 | B - Core Products | Excess | 1227 | 0 | 14 | 231.5 | 33 | 113 | 224 | 0 | — |
| ITEM-0032 | C - Slow Moving | Healthy | 305 | 135 | 60 | 70.0 | 70 | 336 | 467 | 0 | — |
| ITEM-0033 | B - Core Products | Healthy | 306 | 0 | 45 | 88.0 | 56 | 216 | 290 | 0 | — |
| ITEM-0034 | C - Slow Moving | Excess | 682 | 0 | 60 | 451.3 | 62 | 155 | 200 | 0 | — |
| ITEM-0035 | B - Core Products | Healthy | 183 | 265 | 14 | 15.3 | 67 | 247 | 499 | 0 | — |
| ITEM-0036 | B - Core Products | Healthy | 358 | 0 | 7 | 43.2 | 127 | 194 | 368 | 0 | — |
| ITEM-0037 | B - Core Products | Healthy | 107 | 0 | 14 | 24.5 | 27 | 93 | 185 | 0 | — |
| ITEM-0038 | B - Core Products | Healthy | 304 | 172 | 30 | 37.3 | 88 | 341 | 513 | 0 | — |
| ITEM-0039 | B - Core Products | Healthy | 532 | 315 | 30 | 36.5 | 157 | 610 | 916 | 0 | — |
| ITEM-0040 | A - Top Movers | Excess | 4417 | 0 | 60 | 578.6 | 196 | 662 | 769 | 0 | — |
| ITEM-0041 | A - Top Movers | Healthy | 500 | 210 | 14 | 42.7 | 306 | 482 | 646 | 0 | — |
| ITEM-0042 | B - Core Products | Healthy | 94 | 116 | 14 | 19.0 | 29 | 104 | 208 | 0 | — |
| ITEM-0043 | B - Core Products | Stockout | 0 | 2040 | 90 | 0.0 | 466 | 1222 | 1396 | 0 | 1 |
| ITEM-0044 | C - Slow Moving | Excess | 689 | 0 | 45 | 205.3 | 41 | 196 | 297 | 0 | — |
| ITEM-0045 | C - Slow Moving | Healthy | 305 | 220 | 90 | 94.7 | 133 | 427 | 523 | 0 | — |
| ITEM-0046 | C - Slow Moving | Stockout | 0 | 273 | 60 | 0.0 | 107 | 257 | 330 | 0 | 1 |
| ITEM-0047 | B - Core Products | Lead-time risk | 8 | 760 | 60 | 1.2 | 282 | 693 | 834 | 0 | 2 |
| ITEM-0048 | Dead Inv | Dead inventory | 66 | 0 | 45 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0049 | B - Core Products | Healthy | 532 | 0 | 14 | 72.1 | 148 | 259 | 414 | 0 | — |
| ITEM-0050 | C - Slow Moving | Healthy | 83 | 0 | 45 | 113.2 | 11 | 45 | 67 | 0 | — |
| ITEM-0051 | C - Slow Moving | Healthy | 205 | 154 | 60 | 57.7 | 136 | 353 | 460 | 0 | — |
| ITEM-0052 | B - Core Products | Healthy | 123 | 0 | 7 | 12.1 | 25 | 107 | 319 | 0 | — |
| ITEM-0053 | B - Core Products | Healthy | 69 | 155 | 7 | 9.5 | 20 | 79 | 231 | 0 | — |
| ITEM-0054 | A - Top Movers | Excess | 4412 | 0 | 60 | 502.6 | 230 | 766 | 889 | 0 | — |
| ITEM-0055 | A - Top Movers | Healthy | 385 | 0 | 14 | 48.2 | 59 | 179 | 291 | 0 | — |
| ITEM-0056 | A - Top Movers | Healthy | 951 | 1680 | 90 | 51.6 | 698 | 2376 | 2634 | 0 | — |
| ITEM-0057 | Dead Inv | Dead inventory | 64 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0058 | Dead Inv | Dead inventory | 43 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0059 | B - Core Products | Healthy | 1140 | 0 | 30 | 79.1 | 471 | 918 | 1221 | 0 | — |
| ITEM-0060 | B - Core Products | Excess | 554 | 0 | 45 | 145.8 | 62 | 237 | 317 | 0 | — |
| ITEM-0061 | B - Core Products | Reorder | 93 | 0 | 14 | 19.4 | 27 | 99 | 200 | 110 | — |
| ITEM-0062 | C - Slow Moving | Healthy | 87 | 0 | 30 | 55.9 | 14 | 63 | 109 | 0 | — |
| ITEM-0063 | B - Core Products | Excess | 581 | 0 | 14 | 87.0 | 38 | 139 | 279 | 0 | — |
| ITEM-0064 | B - Core Products | Healthy | 433 | 310 | 60 | 78.3 | 229 | 567 | 683 | 0 | — |
| ITEM-0065 | B - Core Products | Healthy | 811 | 260 | 60 | 68.4 | 245 | 969 | 1218 | 0 | — |
| ITEM-0066 | B - Core Products | Healthy | 285 | 115 | 45 | 53.0 | 84 | 332 | 445 | 0 | — |
| ITEM-0067 | A - Top Movers | Healthy | 443 | 0 | 14 | 26.9 | 120 | 368 | 599 | 0 | — |
| ITEM-0068 | B - Core Products | Healthy | 391 | 0 | 30 | 80.0 | 57 | 209 | 312 | 0 | — |
| ITEM-0069 | C - Slow Moving | Healthy | 24 | 85 | 7 | 8.8 | 6 | 28 | 110 | 0 | — |
| ITEM-0070 | C - Slow Moving | Healthy | 117 | 235 | 45 | 31.9 | 91 | 260 | 370 | 0 | — |
| ITEM-0071 | C - Slow Moving | Healthy | 25 | 0 | 7 | 32.6 | 3 | 10 | 33 | 0 | — |
| ITEM-0072 | B - Core Products | Stockout | 0 | 1070 | 60 | 0.0 | 223 | 881 | 1107 | 0 | 1 |
| ITEM-0073 | B - Core Products | Excess | 3499 | 0 | 90 | 751.6 | 143 | 567 | 665 | 0 | — |
| ITEM-0074 | C - Slow Moving | Healthy | 22 | 61 | 14 | 10.8 | 10 | 41 | 102 | 0 | — |
| ITEM-0075 | C - Slow Moving | Healthy | 46 | 26 | 45 | 52.4 | 13 | 54 | 80 | 0 | — |
| ITEM-0076 | B - Core Products | Stockout | 0 | 727 | 90 | 0.0 | 288 | 644 | 727 | 0 | 1 |
| ITEM-0077 | C - Slow Moving | Excess | 347 | 0 | 7 | 160.2 | 6 | 24 | 89 | 0 | — |
| ITEM-0078 | C - Slow Moving | Healthy | 150 | 170 | 90 | 80.8 | 95 | 264 | 320 | 0 | — |
| ITEM-0079 | B - Core Products | Healthy | 276 | 540 | 45 | 23.7 | 184 | 721 | 966 | 0 | — |
| ITEM-0080 | C - Slow Moving | Excess | 544 | 0 | 45 | 248.5 | 27 | 128 | 194 | 0 | — |
| ITEM-0081 | B - Core Products | Healthy | 368 | 558 | 90 | 52.8 | 215 | 849 | 996 | 0 | — |
| ITEM-0082 | B - Core Products | Healthy | 270 | 0 | 7 | 24.3 | 27 | 116 | 350 | 0 | — |
| ITEM-0083 | B - Core Products | Excess | 888 | 0 | 14 | 79.5 | 65 | 233 | 467 | 0 | — |
| ITEM-0084 | B - Core Products | Healthy | 52 | 337 | 60 | 21.3 | 52 | 202 | 253 | 0 | — |
| ITEM-0085 | B - Core Products | Healthy | 296 | 205 | 14 | 36.6 | 206 | 328 | 497 | 0 | — |
| ITEM-0086 | C - Slow Moving | Healthy | 24 | 35 | 14 | 22.0 | 7 | 24 | 56 | 0 | — |
| ITEM-0087 | Dead Inv | Dead inventory | 56 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0088 | C - Slow Moving | Healthy | 284 | 0 | 45 | 66.6 | 52 | 249 | 377 | 0 | — |
| ITEM-0089 | B - Core Products | Healthy | 702 | 0 | 14 | 42.7 | 349 | 596 | 941 | 0 | — |
| ITEM-0090 | Dead Inv | Dead inventory | 90 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0091 | C - Slow Moving | Healthy | 40 | 50 | 30 | 26.5 | 14 | 61 | 107 | 0 | — |
| ITEM-0092 | B - Core Products | Lead-time risk | 739 | 1027 | 90 | 58.8 | 383 | 1528 | 1792 | 0 | 94 |
| ITEM-0093 | B - Core Products | Healthy | 530 | 0 | 7 | 29.3 | 255 | 400 | 781 | 0 | — |
| ITEM-0094 | B - Core Products | Healthy | 64 | 0 | 7 | 12.9 | 15 | 55 | 160 | 0 | — |
| ITEM-0095 | A - Top Movers | Excess | 6949 | 0 | 90 | 387.7 | 681 | 2312 | 2563 | 0 | — |
| ITEM-0096 | A - Top Movers | Excess | 3700 | 0 | 60 | 261.2 | 363 | 1228 | 1426 | 0 | — |
| ITEM-0097 | B - Core Products | Healthy | 73 | 225 | 7 | 11.2 | 104 | 157 | 294 | 0 | — |
| ITEM-0098 | Dead Inv | Dead inventory | 96 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0099 | B - Core Products | Healthy | 126 | 0 | 7 | 21.3 | 20 | 68 | 192 | 0 | — |
| ITEM-0100 | B - Core Products | Healthy | 153 | 0 | 14 | 43.3 | 22 | 75 | 150 | 0 | — |
| ITEM-0101 | A - Top Movers | Healthy | 854 | 865 | 60 | 60.7 | 672 | 1531 | 1728 | 0 | — |
| ITEM-0102 | C - Slow Moving | Healthy | 221 | 0 | 45 | 113.0 | 25 | 115 | 174 | 0 | — |
| ITEM-0103 | Dead Inv | Dead inventory | 87 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0104 | B - Core Products | Healthy | 688 | 689 | 90 | 89.4 | 363 | 1064 | 1226 | 0 | — |
| ITEM-0105 | B - Core Products | Healthy | 412 | 180 | 45 | 55.3 | 118 | 461 | 618 | 0 | — |
| ITEM-0106 | A - Top Movers | Healthy | 1008 | 1286 | 90 | 59.7 | 642 | 2178 | 2415 | 0 | — |
| ITEM-0107 | B - Core Products | Lead-time risk | 275 | 740 | 60 | 25.3 | 223 | 886 | 1114 | 0 | 70 |
| ITEM-0108 | C - Slow Moving | Excess | 519 | 0 | 30 | 249.8 | 53 | 118 | 180 | 0 | — |
| ITEM-0109 | B - Core Products | Stockout | 0 | 1100 | 90 | 0.0 | 268 | 1067 | 1252 | 0 | 1 |
| ITEM-0110 | C - Slow Moving | Healthy | 516 | 0 | 60 | 112.2 | 134 | 415 | 553 | 0 | — |
| ITEM-0111 | A - Top Movers | Healthy | 1761 | 0 | 90 | 129.7 | 519 | 1755 | 1945 | 0 | — |
| ITEM-0112 | A - Top Movers | Healthy | 519 | 1161 | 60 | 30.3 | 441 | 1486 | 1726 | 0 | — |
| ITEM-0113 | A - Top Movers | Healthy | 705 | 1235 | 45 | 38.0 | 826 | 1679 | 1938 | 0 | — |
| ITEM-0114 | C - Slow Moving | Healthy | 43 | 0 | 14 | 31.0 | 7 | 28 | 70 | 0 | — |
| ITEM-0115 | B - Core Products | Excess | 1004 | 0 | 14 | 96.6 | 241 | 397 | 615 | 0 | — |
| ITEM-0116 | C - Slow Moving | Stockout | 0 | 115 | 45 | 0.0 | 18 | 84 | 127 | 0 | 1 |
| ITEM-0117 | Dead Inv | Dead inventory | 61 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0118 | B - Core Products | Stockout | 0 | 772 | 90 | 0.0 | 171 | 675 | 791 | 0 | 1 |
| ITEM-0119 | B - Core Products | Healthy | 222 | 135 | 30 | 37.5 | 64 | 248 | 372 | 0 | — |
| ITEM-0120 | C - Slow Moving | Healthy | 51 | 59 | 30 | 26.7 | 17 | 77 | 134 | 0 | — |
| ITEM-0121 | B - Core Products | Healthy | 179 | 0 | 7 | 13.5 | 34 | 141 | 419 | 0 | — |
| ITEM-0122 | B - Core Products | Healthy | 180 | 238 | 45 | 43.9 | 202 | 391 | 477 | 0 | — |
| ITEM-0123 | C - Slow Moving | Healthy | 96 | 92 | 14 | 33.5 | 65 | 108 | 194 | 0 | — |
| ITEM-0124 | B - Core Products | Healthy | 157 | 216 | 14 | 15.6 | 59 | 211 | 423 | 0 | — |
| ITEM-0125 | B - Core Products | Healthy | 111 | 0 | 7 | 18.7 | 16 | 64 | 189 | 0 | — |
| ITEM-0126 | Dead Inv | Dead inventory | 13 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0127 | A - Top Movers | Excess | 1119 | 0 | 30 | 214.3 | 290 | 452 | 525 | 0 | — |
| ITEM-0128 | B - Core Products | Healthy | 653 | 0 | 45 | 73.5 | 139 | 548 | 735 | 0 | — |
| ITEM-0129 | Dead Inv | Dead inventory | 9 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0130 | B - Core Products | Healthy | 998 | 1320 | 90 | 73.4 | 730 | 1968 | 2254 | 0 | — |
| ITEM-0131 | B - Core Products | Excess | 571 | 0 | 14 | 94.1 | 34 | 125 | 253 | 0 | — |
| ITEM-0132 | Dead Inv | Dead inventory | 42 | 0 | 7 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0133 | C - Slow Moving | Healthy | 306 | 130 | 60 | 72.5 | 68 | 326 | 453 | 0 | — |
| ITEM-0134 | C - Slow Moving | Stockout | 0 | 135 | 90 | 0.0 | 28 | 131 | 164 | 0 | 1 |
| ITEM-0135 | A - Top Movers | Excess | 3817 | 0 | 60 | 277.0 | 354 | 1195 | 1388 | 0 | — |
| ITEM-0136 | C - Slow Moving | Healthy | 85 | 0 | 45 | 81.4 | 29 | 78 | 109 | 0 | — |
| ITEM-0137 | Dead Inv | Dead inventory | 15 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0138 | A - Top Movers | Healthy | 423 | 0 | 14 | 49.7 | 63 | 191 | 310 | 0 | — |
| ITEM-0139 | A - Top Movers | Healthy | 462 | 229 | 30 | 29.7 | 205 | 688 | 905 | 0 | — |
| ITEM-0140 | A - Top Movers | Healthy | 1209 | 539 | 60 | 68.0 | 455 | 1540 | 1789 | 0 | — |
| ITEM-0141 | B - Core Products | Excess | 2215 | 0 | 45 | 227.8 | 154 | 602 | 806 | 0 | — |
| ITEM-0142 | B - Core Products | Stockout | 0 | 1680 | 60 | 0.0 | 565 | 1295 | 1547 | 0 | 1 |
| ITEM-0143 | B - Core Products | Healthy | 388 | 470 | 45 | 36.2 | 168 | 661 | 886 | 0 | — |
| ITEM-0144 | B - Core Products | Excess | 792 | 0 | 7 | 62.8 | 37 | 138 | 403 | 0 | — |
| ITEM-0145 | B - Core Products | Stockout | 0 | 888 | 60 | 0.0 | 106 | 415 | 521 | 0 | 1 |
| ITEM-0146 | Dead Inv | Dead inventory | 23 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0147 | B - Core Products | Healthy | 150 | 636 | 90 | 42.1 | 110 | 435 | 510 | 0 | — |
| ITEM-0148 | B - Core Products | Healthy | 416 | 385 | 14 | 20.8 | 369 | 669 | 1088 | 0 | — |
| ITEM-0149 | B - Core Products | Excess | 1161 | 0 | 14 | 93.4 | 255 | 442 | 703 | 0 | — |
| ITEM-0150 | B - Core Products | Excess | 667 | 0 | 60 | 161.4 | 88 | 341 | 427 | 0 | — |
| ITEM-0151 | Dead Inv | Dead inventory | 51 | 0 | 30 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0152 | Dead Inv | Dead inventory | 80 | 0 | 60 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0153 | B - Core Products | Healthy | 838 | 400 | 90 | 300.5 | 252 | 506 | 565 | 0 | — |
| ITEM-0154 | C - Slow Moving | Healthy | 19 | 200 | 60 | 13.0 | 25 | 115 | 159 | 0 | — |
| ITEM-0155 | B - Core Products | Excess | 559 | 0 | 14 | 75.8 | 43 | 154 | 309 | 0 | — |
| ITEM-0156 | Dead Inv | Dead inventory | 37 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0157 | A - Top Movers | Healthy | 516 | 540 | 30 | 28.0 | 242 | 813 | 1070 | 0 | — |
| ITEM-0158 | Dead Inv | Dead inventory | 25 | 0 | 14 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0159 | Dead Inv | Dead inventory | 58 | 0 | 90 | N/A | 0 | 0 | 0 | 0 | — |
| ITEM-0160 | A - Top Movers | Healthy | 531 | 0 | 7 | 26.8 | 279 | 438 | 716 | 0 | — |
