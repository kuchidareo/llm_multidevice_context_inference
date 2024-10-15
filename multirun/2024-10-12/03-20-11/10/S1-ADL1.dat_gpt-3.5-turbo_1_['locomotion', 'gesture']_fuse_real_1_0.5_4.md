### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Swim,261
0,Swim,272
0,Stand,302
0,Swim,315
0,Stand,319
0,Swim,326
0,Swim,330
Open Fridge,Stand,336
0,Swim,339
Close Fridge,Stand,343
0,Stand,345
0,Walk,347
0,Swim,355
Shake Hands,Stand,355
0,Stand,359
0,Swim,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Swim,371
0,Swim,371
Shake Hands,Stand,378
0,Stand,380
Shake Hands,Stand,383
0,Stand,384
Shake Hands,Swim,385
0,Stand,387
Shake Hands,Stand,389
0,Stand,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Swim,394
0,Stand,397
0,Swim,398
0,Swim,404
0,Swim,422
Close Door 2,Swim,424
Close Door 2,0,427
Close Door 2,Swim,427
Close Door 2,0,428
Shake Hands,Walk,428
0,Swim,428
Toggle Switch,Walk,436
Toggle Switch,Stand,436
0,Stand,438
0,Walk,439
0,Stand,443
Open Door 1,Stand,443
Shake Hands,0,447
Shake Hands,Walk,447
0,Swim,447
0,Swim,673
0,Swim,675
Close Door 1,Walk,676
0,Swim,678
0,Swim,678
Close Door 1,Stand,678
Shake Hands,0,679
Close Door 1,Swim,679
0,Walk,679
0,Swim,685
Shake Hands,Swim,687
0,Swim,689
0,Swim,690
Shake Hands,Walk,699
Shake Hands,Swim,700
0,Stand,701
Close Drawer 2,Swim,702
Close Drawer 2,0,704
Shake Hands,0,704
Shake Hands,Swim,704
Shake Hands,0,705
Shake Hands,Swim,705
Shake Hands,Swim,706
0,Swim,708
0,Walk,711
0,Swim,714
0,Walk,718
0,Swim,721
0,Swim,722
Open Fridge,Swim,723
Open Fridge,Stand,724
0,Swim,726
Shake Hands,Stand,733
0,Stand,735
0,Swim,747
0,Swim,749
Drink from Cup,Stand,843
Drink from Cup,Walk,850
Shake Hands,0,850
Drink from Cup,Stand,851
Shake Hands,0,851
Shake Hands,Swim,855
0,Swim,862
Shake Hands,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Stand,889
0,Swim,896
0,Stand,897
0,Walk,900
0,Stand,905
Open Fridge,Stand,907
0,Stand,909
0,Swim,947
0,Stand,949
0,Walk,992
Shake Hands,Walk,993
Shake Hands,0,994
Shake Hands,Stand,994
0,Swim,995
Shake Hands,Stand,1004
0,Stand,1006
Shake Hands,Swim,1007
0,Swim,1007
Close Drawer 2,Stand,1010
0,Swim,1012
0,Swim,1012
0,Stand,1015
0,Walk,1025
0,Swim,1026
0,Walk,1031
0,Stand,1034
0,Swim,1037
0,Stand,1039
0,Walk,1040
Open Fridge,Walk,1043
Open Fridge,0,1043
Open Fridge,Stand,1043
0,Swim,1046
Close Fridge,Stand,1047
Close Fridge,Swim,1048
0,Swim,1049
0,Stand,1051
0,Walk,1063
Shake Hands,Walk,1066
Shake Hands,0,1066
Shake Hands,Stand,1066
0,Stand,1068
Close Drawer 3,Swim,1071
0,Stand,1073
0,Swim,1073
0,Stand,1077
0,Walk,1100
0,Stand,1102
0,Swim,1109
0,Walk,1311
Open Fridge,Swim,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Stand,1315
Shake Hands,Stand,1326
Close Fridge,Walk,1328
0,Swim,1328
0,Swim,1330
0,Swim,1335
Shake Hands,Swim,1337
Shake Hands,Swim,1338
0,Stand,1340
0,Swim,1352
0,Swim,1353
0,Walk,1356
0,Stand,1357
0,Swim,1362
0,Swim,1364
0,Swim,1365
0,Stand,1367
0,Swim,1373
0,Swim,1374
Shake Hands,Stand,1379
0,Swim,1382
0,Swim,1383
0,Swim,1387
0,Walk,1397
Shake Hands,Swim,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Close Drawer 2,Stand,1402
0,Swim,1404
Shake Hands,Swim,1404
0,Stand,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Walk,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Swim,1419
Close Door 2,Swim,1423
Close Door 2,0,1423
Shake Hands,Swim,1423
0,Stand,1426
0,Swim,1427
0,Swim,1436
0,Walk,1438
0,Stand,1439
Shake Hands,Stand,1440
0,Stand,1446
0,Swim,1448
Shake Hands,0,1451
Clean Table,Stand,1451
0,Swim,1452
0,Swim,1453
0,Swim,1457
0,Walk,1460
0,Swim,1461
0,Swim,1463
0,Swim,1469
Open Door 2,Swim,1469
Open Door 2,Swim,1473
0,Swim,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Shake Hands,Stand,1476
0,Swim,1481
Shake Hands,Swim,1484
Close Door 2,Swim,1485
0,Swim,1489
0,Swim,1490
0,Swim,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to analyze the timestamps and calculate the time spent on each activity. We will consider the activities mentioned in the sensor labels table: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time. 

Here is how we can approach the calculation:

1. Calculate the duration of each activity by finding the difference between the start and end times of the respective activity.

Let's begin by analyzing the timestamps and calculating the duration for each activity mentioned in the table above.
