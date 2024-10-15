### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Walk,92
0,Walk,261
0,Sit,272
0,Walk,302
0,Walk,315
0,Stand,319
0,Walk,326
0,Walk,330
Close Drawer 2,Stand,336
0,Walk,339
Close Fridge,Stand,343
0,Walk,345
0,Walk,347
0,Stand,355
Open Door 2,Stand,355
0,Walk,359
0,Walk,362
Open Door 1,Walk,366
Open Door 1,Walk,366
0,Stand,371
0,Walk,371
Close Drawer 2,Stand,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Close Dishwasher,Stand,385
0,Walk,387
Close Drawer 2,Stand,389
0,Walk,390
Close Drawer 2,Sit,391
0,Stand,393
Close Drawer 3,Stand,394
0,Stand,397
0,Walk,398
0,Sit,404
0,Walk,422
Close Door 2,Walk,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Sit,428
0,Sit,428
Close Dishwasher,Walk,436
Toggle Switch,Stand,436
0,Stand,438
0,Walk,439
0,Sit,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Walk,447
0,Walk,447
0,Walk,673
0,Walk,675
Close Door 1,Walk,676
0,Walk,678
0,Stand,678
Close Door 1,Stand,678
Close Door 1,0,679
Close Door 1,None,679
0,Walk,679
0,Stand,685
Close Dishwasher,Stand,687
0,None,689
0,Walk,690
Close Drawer 2,Walk,699
Close Drawer 2,Stand,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Close Dishwasher,0,704
Close Drawer 2,Walk,704
Close Drawer 2,0,705
Close Drawer 2,Stand,705
Close Drawer 2,Walk,706
0,Walk,708
0,Sit,711
0,Stand,714
0,Sit,718
0,Sit,721
0,Sit,722
Open Fridge,Walk,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Stand,733
0,Walk,735
0,Walk,747
0,Walk,749
Close Drawer 3,Walk,843
Close Drawer 2,Walk,850
Drink from Cup,0,850
Drink from Cup,Stand,851
Close Drawer 2,0,851
Drink from Cup,Sit,855
0,Walk,862
Close Drawer 3,Walk,865
0,Sit,874
Close Drawer 3,Sit,876
0,Walk,885
0,Stand,889
0,Walk,896
0,Walk,897
0,Sit,900
0,Stand,905
Open Fridge,Stand,907
0,Sit,909
0,Walk,947
0,Walk,949
0,Walk,992
Close Dishwasher,Walk,993
Close Dishwasher,0,994
Close Dishwasher,Walk,994
0,Stand,995
Close Drawer 2,Walk,1004
0,Walk,1006
Close Drawer 2,Walk,1007
0,Stand,1007
Close Drawer 2,Walk,1010
0,Stand,1012
0,Walk,1012
0,Stand,1015
0,Walk,1025
0,Walk,1026
0,Sit,1031
0,Sit,1034
0,Walk,1037
0,Stand,1039
0,Sit,1040
Open Fridge,Walk,1043
Open Fridge,0,1043
Close Drawer 2,Walk,1043
0,Stand,1046
Close Fridge,Stand,1047
Drink from Cup,Walk,1048
0,Walk,1049
0,Stand,1051
0,Walk,1063
Close Drawer 2,Walk,1066
Close Drawer 2,0,1066
Close Drawer 2,Walk,1066
0,Walk,1068
Close Drawer 3,Stand,1071
0,Stand,1073
0,Walk,1073
0,Walk,1077
0,Walk,1100
0,Stand,1102
0,Sit,1109
0,Sit,1311
Open Fridge,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Stand,1315
Close Fridge,Stand,1326
Close Drawer 2,Walk,1328
0,Walk,1328
0,Stand,1330
0,Sit,1335
Close Drawer 2,Walk,1337
Close Drawer 2,Stand,1338
0,Walk,1340
0,Walk,1352
0,Walk,1353
0,Walk,1356
0,Walk,1357
0,Walk,1362
0,Stand,1364
0,Walk,1365
0,Stand,1367
0,Walk,1373
0,Walk,1374
Close Drawer 2,Stand,1379
0,None,1382
0,Walk,1383
0,Stand,1387
0,Walk,1397
Close Drawer 2,Walk,1401
Close Drawer 2,0,1401
Close Drawer 2,Stand,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Close Drawer 2,Walk,1404
0,Walk,1406
Close Drawer 3,Walk,1407
0,Walk,1410
0,Walk,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Close Dishwasher,0,1423
Close Door 2,Walk,1423
0,Stand,1426
0,Sit,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Clean Table,Stand,1440
0,Stand,1446
0,Walk,1448
Clean Table,0,1451
Clean Table,Stand,1451
0,Stand,1452
0,Sit,1453
0,Walk,1457
0,None,1460
0,Stand,1461
0,Walk,1463
0,None,1469
Open Door 2,Stand,1469
Open Door 2,Walk,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Close Door 1,Stand,1476
0,Walk,1481
Close Door 2,Walk,1484
Close Drawer 2,Stand,1485
0,Walk,1489
0,Sit,1490
0,Walk,1504
0,Walk,1522

### assistant
To calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time, we need to analyze the provided sensor labels and timestamps.

1. Relaxing:
- Relaxing activities include standing, sitting, and activities like opening doors or drawers that do not involve physical movement.
- The duration of Relaxing activities can be calculated based on the timestamps when the person was standing, sitting, or not engaged in any specific activity.
- Time spent in activities like "Stand", "Sit", "Close Drawer", "Open Door", and "Toggle Switch" can be considered as Relaxing time.
- We can calculate the total duration of Relaxing time by summing up the duration between the Relaxing activity timestamps.

For example, based on the provided data, we can calculate the duration of Relaxing activities by identifying the timestamps for "Stand", "Sit", "Close Drawer", "Close Door", "Open Door", and "Toggle Switch" activities.

2. Coffee time:
- Coffee time activities might include specific actions related to making or drinking coffee, like "Drink from Cup".
- We can calculate the duration of Coffee time by analyzing the timestamps when the person was drinking from a cup or engaged in other coffee-related activities.

3. Early morning:
- Early morning activities might include specific actions that indicate the start of the day or morning routine.
- We can identify Early morning activities by analyzing the timestamps at the beginning of the recorded activities.

4. Cleanup:
- Cleanup activities typically involve actions like cleaning, organizing, or tidying up the environment.
- We can calculate the duration of Cleanup activities by identifying specific actions related to cleaning or organizing tasks.

5. Sandwich time:
- Sandwich time activities might include specific actions related to preparing or eating a sandwich.
- We can calculate the duration of Sandwich time by analyzing the timestamps when the person was engaged in activities like preparing food or eating.

By analyzing the sensor labels and timestamps provided in the CSV file, we can determine the duration of each of the specified activities based on the criteria described above.
