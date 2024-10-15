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
0,Swim,319
0,Walk,326
0,Stand,330
Open Fridge,Stand,336
0,Stand,339
Close Fridge,Stand,343
0,Stand,345
0,Walk,347
0,Stand,355
Open Door 2,Stand,355
0,Stand,359
0,Swim,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Swim,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Open Drawer 1,Swim,385
0,Swim,387
Shake Hands,Swim,389
0,Stand,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Stand,394
0,Stand,397
0,Swim,398
0,Stand,404
0,Walk,422
Close Door 2,Walk,424
Close Door 2,0,427
Shake Hands,Stand,427
Close Door 2,0,428
Close Door 2,Walk,428
0,Walk,428
Toggle Switch,Walk,436
Toggle Switch,Stand,436
0,Stand,438
0,Walk,439
0,Swim,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Walk,447
0,Walk,447
0,Swim,673
0,Walk,675
Close Door 1,Walk,676
0,Swim,678
0,Stand,678
Close Door 1,Swim,678
Shake Hands,0,679
Close Door 1,Swim,679
0,Swim,679
0,Stand,685
Open Door 2,Swim,687
0,Swim,689
0,Walk,690
Shake Hands,Walk,699
Shake Hands,Stand,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Open Drawer 1,Swim,704
Open Drawer 1,0,705
Open Drawer 1,Swim,705
Shake Hands,Stand,706
0,Swim,708
0,Swim,711
0,Swim,714
0,Walk,718
0,Stand,721
0,Swim,722
Open Fridge,Walk,723
Open Fridge,Swim,724
0,Swim,726
Close Fridge,Stand,733
0,Stand,735
0,Walk,747
0,Swim,749
Drink from Cup,Stand,843
Shake Hands,Walk,850
Drink from Cup,0,850
Drink from Cup,Swim,851
Drink from Cup,0,851
Drink from Cup,Swim,855
0,Swim,862
Drink from Cup,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Swim,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Stand,905
Open Fridge,Stand,907
0,Swim,909
0,Walk,947
0,Stand,949
0,Walk,992
Shake Hands,Walk,993
Open Drawer 1,0,994
Shake Hands,Swim,994
0,Stand,995
Shake Hands,Stand,1004
0,Stand,1006
Shake Hands,Swim,1007
0,Swim,1007
Close Drawer 2,Stand,1010
0,Stand,1012
0,Walk,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Stand,1034
0,Walk,1037
0,Stand,1039
0,Walk,1040
Open Fridge,Walk,1043
Open Fridge,0,1043
Open Fridge,Stand,1043
0,Swim,1046
Close Fridge,Stand,1047
Shake Hands,Walk,1048
0,Walk,1049
0,Swim,1051
0,Walk,1063
Shake Hands,Walk,1066
Open Drawer 3,0,1066
Shake Hands,Stand,1066
0,Stand,1068
Close Drawer 3,Stand,1071
0,Swim,1073
0,Walk,1073
0,Stand,1077
0,Walk,1100
0,Stand,1102
0,Swim,1109
0,Walk,1311
Open Fridge,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Stand,1315
Close Fridge,Swim,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Shake Hands,Walk,1337
Open Dishwasher,Stand,1338
0,Stand,1340
0,Walk,1352
0,Stand,1353
0,Swim,1356
0,Stand,1357
0,Swim,1362
0,Swim,1364
0,Walk,1365
0,Swim,1367
0,Walk,1373
0,Stand,1374
Shake Hands,Stand,1379
0,Swim,1382
0,Walk,1383
0,Stand,1387
0,Walk,1397
Shake Hands,Swim,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Close Drawer 2,Stand,1402
0,Swim,1404
Shake Hands,Swim,1404
0,Stand,1406
Close Drawer 3,Swim,1407
0,Stand,1410
0,Swim,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Shake Hands,0,1423
Close Door 2,Stand,1423
0,Stand,1426
0,Walk,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Clean Table,Stand,1440
0,Stand,1446
0,Swim,1448
Clean Table,0,1451
Clean Table,Stand,1451
0,Stand,1452
0,Walk,1453
0,Stand,1457
0,Swim,1460
0,Stand,1461
0,Swim,1463
0,Stand,1469
Open Door 2,Stand,1469
Open Door 2,Walk,1473
0,Swim,1473
Shake Hands,Swim,1476
Close Door 1,0,1476
Close Door 1,Stand,1476
0,Walk,1481
Shake Hands,Swim,1484
Close Door 2,Stand,1485
0,Stand,1489
0,Walk,1490
0,Swim,1504
0,Walk,1522

### assistant
To calculate the duration of the specified activities (Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time) from the provided timestamp data, we need to:

1. Identify the activities by their labels.
2. Calculate the duration for each occurrence by taking the difference between the start and end timestamps.

Based on the data provided and the activities we need to track, we found:

- **Cleanup** corresponds to the "Clean Table" activity in the data.
- The other activities (Relaxing, Coffee time, Early morning, and Sandwich time) do not appear to have specific labels in the provided timeline.

Let's extract the duration for the "Clean Table" activities:

1. **Clean Table, Stand:** Time stamp = 1440
2. **Clean Table, 0:** Time stamp = 1451
3. **Clean Table, Stand:** Time stamp = 1451

- Here we can see that "Clean Table, Stand" occurs at 1440 and then 1451 with no prior duration. 
- However, we can view from the data how long it has been marked on 1440 (starting) up to 1451 (ending):

Duration for Cleanup:
- **Start**: 1440
- **End**: 1451
- **Duration** = 1451 - 1440 = 11 seconds

Since no other actions relevant to the highlighted activities appear, we can provide the duration for Clean Table:

**Cleanup: 11 seconds**

For the remaining activities (Relaxing, Coffee time, Early morning, Sandwich time), there are no entries listed in the provided dataset. If you need to analyze more activities or find specific segments, please ensure the relevant labels are present in the data you provide.
