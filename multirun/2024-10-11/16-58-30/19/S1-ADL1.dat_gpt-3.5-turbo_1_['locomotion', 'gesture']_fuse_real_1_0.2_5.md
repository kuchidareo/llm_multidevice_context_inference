### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Swim,261
0,Lie,272
0,Stand,302
0,Walk,315
0,Stand,319
0,Walk,326
0,Stand,330
Open Fridge,Stand,336
0,Stand,339
Close Fridge,Swim,343
0,Stand,345
0,Swim,347
0,Swim,355
Open Door 2,Stand,355
0,Stand,359
0,Swim,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Stand,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Shake Hands,Swim,385
0,Stand,387
Shake Hands,Stand,389
0,Stand,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Stand,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Swim,422
Close Door 2,Walk,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Walk,428
0,Walk,428
Toggle Switch,Walk,436
Toggle Switch,Stand,436
0,Stand,438
0,Swim,439
0,Stand,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Walk,447
0,Walk,447
0,Stand,673
0,Walk,675
Close Door 1,Walk,676
0,Walk,678
0,Swim,678
Close Door 1,Stand,678
Close Door 1,0,679
Close Door 1,Walk,679
0,Walk,679
0,Stand,685
Open Door 2,Stand,687
0,Stand,689
0,Walk,690
Shake Hands,Walk,699
Shake Hands,Stand,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Shake Hands,Walk,704
Shake Hands,0,705
Shake Hands,Stand,705
Shake Hands,Swim,706
0,Stand,708
0,Walk,711
0,Swim,714
0,Walk,718
0,Stand,721
0,Walk,722
Open Fridge,Walk,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Swim,733
0,Stand,735
0,Swim,747
0,Stand,749
Drink from Cup,Stand,843
Shake Hands,Swim,850
Shake Hands,0,850
Shake Hands,Stand,851
Shake Hands,0,851
Drink from Cup,Swim,855
0,Swim,862
Drink from Cup,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Stand,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Stand,905
Shake Hands,Stand,907
0,Stand,909
0,Walk,947
0,Swim,949
0,Walk,992
Shake Hands,Walk,993
Shake Hands,0,994
Shake Hands,Stand,994
0,Stand,995
Shake Hands,Swim,1004
0,Swim,1006
Shake Hands,Swim,1007
0,Stand,1007
Shake Hands,Stand,1010
0,Stand,1012
0,Walk,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Stand,1034
0,Swim,1037
0,Stand,1039
0,Walk,1040
Shake Hands,Swim,1043
Open Fridge,0,1043
Open Fridge,Stand,1043
0,Stand,1046
Close Fridge,Stand,1047
Close Fridge,Walk,1048
0,Walk,1049
0,Stand,1051
0,Walk,1063
Shake Hands,Walk,1066
Shake Hands,0,1066
Open Drawer 3,Swim,1066
0,Stand,1068
Close Drawer 3,Stand,1071
0,Stand,1073
0,Walk,1073
0,Stand,1077
0,Walk,1100
0,Stand,1102
0,Swim,1109
0,Walk,1311
Open Fridge,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Swim,1315
Close Fridge,Stand,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Open Dishwasher,Walk,1337
Shake Hands,Swim,1338
0,Stand,1340
0,Swim,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Walk,1362
0,Stand,1364
0,Walk,1365
0,Stand,1367
0,Swim,1373
0,Swim,1374
Shake Hands,Stand,1379
0,Stand,1382
0,Walk,1383
0,Stand,1387
0,Swim,1397
Shake Hands,Walk,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Open Drawer 3,Swim,1404
0,Stand,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Walk,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Shake Hands,Stand,1423
0,Stand,1426
0,Walk,1427
0,Stand,1436
0,Swim,1438
0,Stand,1439
Clean Table,Swim,1440
0,Stand,1446
0,Swim,1448
Clean Table,0,1451
Clean Table,Stand,1451
0,Swim,1452
0,Swim,1453
0,Stand,1457
0,Walk,1460
0,Swim,1461
0,Walk,1463
0,Stand,1469
Open Door 2,Stand,1469
Open Door 2,Walk,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Close Door 1,Swim,1476
0,Walk,1481
Close Door 2,Walk,1484
Close Door 2,Stand,1485
0,Stand,1489
0,Walk,1490
0,Lie,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to analyze the timestamps provided in the CSV file for the specific activities mentioned. Let's calculate the durations for each activity:

1. Relaxing:
   - Lie: 272 - 0 = 272 seconds

2. Coffee time:
   - Open Fridge to Close Fridge: 733 - 336 = 397 seconds

3. Early morning:
   - Open Door 2 to Toggle Switch: 436 - 355 = 81 seconds

4. Cleanup:
   - Close Drawer 2 to Close Drawer 3: 394 - 383 = 11 seconds
   - Close Door 1 to Open Fridge: 678 - 676 = 2 seconds
   - Drink from Cup to Close Fridge: 865 - 843 = 22 seconds
   - Close Fridge to Open Fridge: 733 - 1043 = 310 seconds
   - Close Fridge to Open Drawer 3: 1326 - 1066 = 260 seconds
   - Clean Table: 1451 - 1440 = 11 seconds

5. Sandwich Time:
   - Open Fridge to Clean Table: 1313 - 1043 = 270 seconds
   - Clean Table to Open Door 2: 1469 - 1451 = 18 seconds

These are the calculated durations for each activity as per the provided sensor data.
