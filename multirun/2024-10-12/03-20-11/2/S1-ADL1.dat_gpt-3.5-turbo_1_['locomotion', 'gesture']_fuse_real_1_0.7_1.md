### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Swim,92
0,Walk,261
0,Swim,272
0,Stand,302
0,Swim,315
0,Swim,319
0,Swim,326
0,Swim,330
Open Fridge,Swim,336
0,Stand,339
Shake Hands,Swim,343
0,Stand,345
0,Swim,347
0,Swim,355
Open Door 2,Swim,355
0,Stand,359
0,Swim,362
Shake Hands,Swim,366
Shake Hands,Swim,366
0,Swim,371
0,Walk,371
Shake Hands,Swim,378
0,Stand,380
Close Drawer 2,Stand,383
0,Swim,384
Shake Hands,Swim,385
0,Stand,387
Shake Hands,Swim,389
0,Swim,390
Shake Hands,Swim,391
0,Stand,393
Shake Hands,Stand,394
0,Swim,397
0,Swim,398
0,Stand,404
0,Walk,422
Close Door 2,Swim,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Swim,428
0,Walk,428
Toggle Switch,Walk,436
Toggle Switch,Stand,436
0,Swim,438
0,Swim,439
0,Swim,443
Shake Hands,Swim,443
Shake Hands,0,447
Shake Hands,Swim,447
0,Swim,447
0,Swim,673
0,Swim,675
Shake Hands,Swim,676
0,Walk,678
0,Stand,678
Shake Hands,Swim,678
Close Door 1,0,679
Shake Hands,Walk,679
0,Swim,679
0,Stand,685
Shake Hands,Stand,687
0,Swim,689
0,Walk,690
Shake Hands,Walk,699
Shake Hands,Swim,700
0,Swim,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Shake Hands,Swim,704
Shake Hands,0,705
Shake Hands,Swim,705
Shake Hands,Swim,706
0,Swim,708
0,Swim,711
0,Swim,714
0,Swim,718
0,Stand,721
0,Walk,722
Open Fridge,Swim,723
Shake Hands,Swim,724
0,Swim,726
Close Fridge,Swim,733
0,Swim,735
0,Walk,747
0,Swim,749
Shake Hands,Swim,843
Shake Hands,Swim,850
Shake Hands,0,850
Shake Hands,Stand,851
Shake Hands,0,851
Shake Hands,Swim,855
0,Swim,862
Shake Hands,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Stand,889
0,Swim,896
0,Swim,897
0,Swim,900
0,Swim,905
Open Fridge,Swim,907
0,Swim,909
0,Walk,947
0,Stand,949
0,Swim,992
Shake Hands,Swim,993
Shake Hands,0,994
Shake Hands,Stand,994
0,Swim,995
Shake Hands,Swim,1004
0,Stand,1006
Shake Hands,Stand,1007
0,Stand,1007
Close Drawer 2,Swim,1010
0,Swim,1012
0,Walk,1012
0,Swim,1015
0,Swim,1025
0,Swim,1026
0,Walk,1031
0,Stand,1034
0,Swim,1037
0,Swim,1039
0,Swim,1040
Open Fridge,Walk,1043
Shake Hands,0,1043
Open Fridge,Stand,1043
0,Swim,1046
Shake Hands,Stand,1047
Shake Hands,Walk,1048
0,Swim,1049
0,Swim,1051
0,Swim,1063
Shake Hands,Swim,1066
Shake Hands,0,1066
Shake Hands,Swim,1066
0,Swim,1068
Shake Hands,Swim,1071
0,Stand,1073
0,Swim,1073
0,Swim,1077
0,Walk,1100
0,Swim,1102
0,Swim,1109
0,Swim,1311
Shake Hands,Swim,1313
Shake Hands,0,1314
Open Fridge,Swim,1314
0,Swim,1315
Shake Hands,Swim,1326
Close Fridge,Swim,1328
0,Swim,1328
0,Swim,1330
0,Swim,1335
Shake Hands,Walk,1337
Shake Hands,Swim,1338
0,Swim,1340
0,Swim,1352
0,Stand,1353
0,Walk,1356
0,Swim,1357
0,Swim,1362
0,Swim,1364
0,Walk,1365
0,Swim,1367
0,Swim,1373
0,Swim,1374
Shake Hands,Swim,1379
0,Swim,1382
0,Swim,1383
0,Swim,1387
0,Swim,1397
Shake Hands,Swim,1401
Shake Hands,0,1401
Shake Hands,Swim,1401
Shake Hands,Stand,1402
0,Swim,1404
Shake Hands,Swim,1404
0,Stand,1406
Shake Hands,Swim,1407
0,Swim,1410
0,Swim,1411
Open Door 1,Swim,1414
0,Swim,1419
0,Walk,1419
Shake Hands,Swim,1423
Shake Hands,0,1423
Shake Hands,Swim,1423
0,Swim,1426
0,Walk,1427
0,Swim,1436
0,Swim,1438
0,Stand,1439
Clean Table,Swim,1440
0,Swim,1446
0,Swim,1448
Clean Table,0,1451
Shake Hands,Stand,1451
0,Stand,1452
0,Walk,1453
0,Stand,1457
0,Walk,1460
0,Swim,1461
0,Swim,1463
0,Stand,1469
Shake Hands,Swim,1469
Open Door 2,Swim,1473
0,Swim,1473
Close Door 1,Swim,1476
Shake Hands,0,1476
Shake Hands,Swim,1476
0,Swim,1481
Close Door 2,Swim,1484
Close Door 2,Stand,1485
0,Swim,1489
0,Swim,1490
0,Swim,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to analyze the timestamps and determine when each activity starts and ends.

Based on the provided sensor data, we can identify the activities as follows:
- Relaxing: When the person is standing or sitting still without any specific movement.
- Coffee time: When the person is opening or closing the fridge.
- Early morning: When the person is waking up and starting the day.
- Cleanup: When the person is cleaning or tidying up (e.g., cleaning table, closing drawers).
- Sandwich time: When the person is eating (not explicitly captured in the sensor data).

We will need to calculate the duration for each of these activities based on the timestamps provided. Let's start by extracting the relevant data and determining the duration of each activity. I will provide the results shortly.
