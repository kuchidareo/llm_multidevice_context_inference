### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Swim,92
0,Walk,261
0,Swim,272
0,Swim,302
0,Swim,315
0,Swim,319
0,Swim,326
0,Swim,330
Open Fridge,Swim,336
0,Swim,339
Shake Hands,Stand,343
0,Swim,345
0,Swim,347
0,Swim,355
Shake Hands,Stand,355
0,Stand,359
0,Walk,362
Shake Hands,Walk,366
Open Door 1,Swim,366
0,Swim,371
0,Swim,371
Shake Hands,Stand,378
0,Swim,380
Shake Hands,Swim,383
0,Stand,384
Shake Hands,Stand,385
0,Swim,387
Shake Hands,Swim,389
0,Stand,390
Shake Hands,Swim,391
0,Stand,393
Shake Hands,Swim,394
0,Swim,397
0,Swim,398
0,Stand,404
0,Swim,422
Close Door 2,Walk,424
Close Door 2,0,427
Close Door 2,Swim,427
Close Door 2,0,428
Close Door 2,Swim,428
0,Swim,428
Shake Hands,Swim,436
Shake Hands,Swim,436
0,Stand,438
0,Swim,439
0,Stand,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Walk,447
0,Swim,447
0,Swim,673
0,Swim,675
Close Door 1,Walk,676
0,Swim,678
0,Stand,678
Shake Hands,Swim,678
Shake Hands,0,679
Close Door 1,Swim,679
0,Swim,679
0,Swim,685
Shake Hands,Swim,687
0,Stand,689
Shake Hands,Walk,690
Shake Hands,Walk,699
Shake Hands,Stand,700
0,Swim,701
Shake Hands,Swim,702
Shake Hands,0,704
Shake Hands,0,704
Shake Hands,Swim,704
Shake Hands,0,705
Shake Hands,Swim,705
Shake Hands,Swim,706
0,Stand,708
0,Swim,711
0,Swim,714
0,Swim,718
0,Swim,721
0,Walk,722
Shake Hands,Swim,723
Shake Hands,Stand,724
0,Swim,726
Shake Hands,Stand,733
0,Stand,735
0,Swim,747
0,Stand,749
Shake Hands,Stand,843
Drink from Cup,Swim,850
Shake Hands,0,850
Shake Hands,Swim,851
Shake Hands,0,851
Shake Hands,Swim,855
0,Swim,862
Drink from Cup,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Swim,889
0,Swim,896
0,Swim,897
0,Swim,900
0,Swim,905
Open Fridge,Swim,907
Shake Hands,Swim,909
0,Swim,947
0,Stand,949
0,Swim,992
Shake Hands,Swim,993
Shake Hands,0,994
Shake Hands,Stand,994
0,Stand,995
Shake Hands,Swim,1004
0,Stand,1006
Shake Hands,Swim,1007
0,Swim,1007
Shake Hands,Stand,1010
0,Stand,1012
0,Swim,1012
0,Swim,1015
0,Swim,1025
0,Stand,1026
0,Swim,1031
0,Stand,1034
0,Swim,1037
0,Swim,1039
0,Swim,1040
Shake Hands,Swim,1043
Open Fridge,0,1043
Open Fridge,Swim,1043
0,Swim,1046
Close Fridge,Stand,1047
Shake Hands,Swim,1048
0,Swim,1049
0,Stand,1051
0,Walk,1063
Shake Hands,Swim,1066
Shake Hands,0,1066
Shake Hands,Stand,1066
0,Stand,1068
Close Drawer 3,Stand,1071
0,Stand,1073
0,Swim,1073
0,Swim,1077
0,Swim,1100
0,Swim,1102
0,Swim,1109
0,Walk,1311
Open Fridge,Swim,1313
Open Fridge,0,1314
Open Fridge,Swim,1314
0,Stand,1315
Shake Hands,Swim,1326
Close Fridge,Swim,1328
Shake Hands,Swim,1328
0,Swim,1330
0,Swim,1335
Shake Hands,Swim,1337
Shake Hands,Swim,1338
0,Swim,1340
0,Walk,1352
0,Swim,1353
0,Swim,1356
0,Swim,1357
0,Walk,1362
0,Swim,1364
0,Swim,1365
0,Stand,1367
0,Swim,1373
0,Stand,1374
Shake Hands,Stand,1379
0,Stand,1382
0,Swim,1383
0,Swim,1387
0,Swim,1397
Shake Hands,Swim,1401
Shake Hands,0,1401
Shake Hands,Swim,1401
Shake Hands,Swim,1402
0,Stand,1404
Shake Hands,Stand,1404
0,Swim,1406
Shake Hands,Stand,1407
Shake Hands,Stand,1410
0,Swim,1411
Open Door 1,Swim,1414
0,Swim,1419
0,Swim,1419
Close Door 2,Swim,1423
Close Door 2,0,1423
Close Door 2,Swim,1423
0,Stand,1426
0,Swim,1427
0,Swim,1436
0,Swim,1438
0,Swim,1439
Shake Hands,Swim,1440
0,Stand,1446
0,Swim,1448
Shake Hands,0,1451
Shake Hands,Swim,1451
0,Stand,1452
0,Swim,1453
0,Stand,1457
0,Swim,1460
0,Swim,1461
0,Swim,1463
0,Swim,1469
Shake Hands,Swim,1469
Open Door 2,Swim,1473
0,Swim,1473
Close Door 1,Swim,1476
Close Door 1,0,1476
Close Door 1,Swim,1476
0,Swim,1481
Shake Hands,Walk,1484
Close Door 2,Swim,1485
0,Swim,1489
0,Swim,1490
0,Swim,1504
0,Swim,1522

### assistant
To calculate the duration of each activity, you need to match the start and end timestamps for each activity. Here are the steps to determine the duration for each activity:

1. Identify the timestamps for the start and end of each activity (Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time).
2. Calculate the duration by subtracting the start timestamp from the end timestamp for each activity.

Please provide the start and end labels or timestamps for each activity so that I can assist you further in calculating the duration.
