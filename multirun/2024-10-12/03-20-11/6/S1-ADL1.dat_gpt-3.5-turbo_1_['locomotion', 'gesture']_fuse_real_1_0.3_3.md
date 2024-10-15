### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Walk,261
0,Swim,272
0,Stand,302
0,Swim,315
0,Stand,319
0,Swim,326
0,Stand,330
Open Fridge,Stand,336
0,Stand,339
Close Fridge,Stand,343
0,Swim,345
0,Swim,347
0,Stand,355
Open Door 2,Stand,355
0,Stand,359
0,Walk,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Stand,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Shake Hands,Stand,385
0,Stand,387
Shake Hands,Swim,389
0,Swim,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Stand,394
0,Stand,397
0,Swim,398
0,Stand,404
0,Swim,422
Close Door 2,Swim,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Swim,428
0,Walk,428
Toggle Switch,Swim,436
Toggle Switch,Stand,436
0,Stand,438
0,Swim,439
0,Stand,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Swim,447
0,Walk,447
0,Swim,673
0,Walk,675
Shake Hands,Swim,676
0,Swim,678
0,Stand,678
Close Door 1,Stand,678
Close Door 1,0,679
Close Door 1,Walk,679
0,Walk,679
0,Swim,685
Open Door 2,Stand,687
0,Stand,689
0,Walk,690
Open Drawer 2,Swim,699
Shake Hands,Swim,700
0,Swim,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Open Drawer 1,0,704
Shake Hands,Walk,704
Shake Hands,0,705
Shake Hands,Swim,705
Shake Hands,Stand,706
0,Stand,708
0,Walk,711
0,Stand,714
0,Walk,718
0,Swim,721
0,Swim,722
Open Fridge,Walk,723
Open Fridge,Stand,724
0,Swim,726
Shake Hands,Stand,733
0,Stand,735
0,Walk,747
0,Stand,749
Drink from Cup,Stand,843
Drink from Cup,Walk,850
Drink from Cup,0,850
Drink from Cup,Stand,851
Drink from Cup,0,851
Drink from Cup,Swim,855
0,Swim,862
Drink from Cup,Swim,865
0,Swim,874
Drink from Cup,Swim,876
0,Swim,885
0,Stand,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Swim,905
Open Fridge,Stand,907
0,Stand,909
0,Walk,947
0,Stand,949
0,Swim,992
Shake Hands,Swim,993
Open Drawer 1,0,994
Open Drawer 1,Stand,994
0,Stand,995
Shake Hands,Stand,1004
0,Stand,1006
Shake Hands,Stand,1007
0,Stand,1007
Close Drawer 2,Swim,1010
0,Swim,1012
0,Swim,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Swim,1034
0,Walk,1037
0,Stand,1039
0,Walk,1040
Shake Hands,Walk,1043
Open Fridge,0,1043
Open Fridge,Stand,1043
0,Stand,1046
Close Fridge,Stand,1047
Shake Hands,Walk,1048
0,Walk,1049
0,Stand,1051
0,Swim,1063
Shake Hands,Walk,1066
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
Close Fridge,Stand,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Shake Hands,Walk,1337
Shake Hands,Stand,1338
0,Stand,1340
0,Walk,1352
0,Stand,1353
0,Swim,1356
0,Stand,1357
0,Walk,1362
0,Swim,1364
0,Walk,1365
0,Swim,1367
0,Walk,1373
0,Stand,1374
Shake Hands,Swim,1379
0,Stand,1382
0,Walk,1383
0,Stand,1387
0,Walk,1397
Shake Hands,Walk,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Shake Hands,Swim,1402
0,Stand,1404
Shake Hands,Stand,1404
0,Stand,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Swim,1411
Open Door 1,Swim,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Close Door 2,Stand,1423
0,Stand,1426
0,Walk,1427
0,Stand,1436
0,Walk,1438
0,Swim,1439
Clean Table,Stand,1440
0,Stand,1446
0,Walk,1448
Clean Table,0,1451
Clean Table,Stand,1451
0,Swim,1452
0,Walk,1453
0,Swim,1457
0,Walk,1460
0,Stand,1461
0,Walk,1463
0,Stand,1469
Open Door 2,Swim,1469
Open Door 2,Swim,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Close Door 1,Stand,1476
0,Swim,1481
Close Door 2,Walk,1484
Close Door 2,Swim,1485
0,Stand,1489
0,Walk,1490
0,Swim,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to find the start and end timestamps for the following activities: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time from the given sensor data. 

Based on the data provided, we can see that there are a variety of activities captured by the sensors and some activities can be mapped to the desired activities:

- "Relaxing" activity is not directly mentioned in the data, so it might be inferred from Stand or Sit activities.
- "Coffee time" activity is not directly mentioned in the data, so we'll not consider it.
- "Early morning" activity has a few instances of "Open Door" and "Close Door" activities that could potentially be considered as part of the Early Morning routine.
- "Cleanup" activity is referred to as activities like Close Drawer, Close Fridge, Clean Table, etc.
- "Sandwich time" activity is not directly mentioned in the data, so we'll not consider it.

We will now calculate the duration of the inferred activities based on the timestamps related to them. Let's proceed with the calculations.
