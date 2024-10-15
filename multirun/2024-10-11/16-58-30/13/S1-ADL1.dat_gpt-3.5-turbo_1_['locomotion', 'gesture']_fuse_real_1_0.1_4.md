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
0,Walk,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Stand,378
0,Swim,380
Close Drawer 2,Swim,383
0,Swim,384
Open Drawer 1,Stand,385
0,Stand,387
Shake Hands,Stand,389
0,Stand,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Stand,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Walk,422
Close Door 2,Walk,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Walk,428
0,Swim,428
Toggle Switch,Walk,436
Toggle Switch,Stand,436
0,Stand,438
0,Walk,439
0,Stand,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Walk,447
0,Walk,447
0,Stand,673
0,Walk,675
Close Door 1,Walk,676
0,Walk,678
0,Stand,678
Shake Hands,Stand,678
Close Door 1,0,679
Shake Hands,Walk,679
0,Walk,679
0,Stand,685
Open Door 2,Stand,687
0,Stand,689
0,Walk,690
Open Drawer 2,Walk,699
Open Drawer 2,Stand,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Open Drawer 1,Walk,704
Open Drawer 1,0,705
Shake Hands,Stand,705
Close Drawer 1,Stand,706
0,Stand,708
0,Walk,711
0,Stand,714
0,Walk,718
0,Stand,721
0,Walk,722
Open Fridge,Walk,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Stand,733
0,Swim,735
0,Walk,747
0,Stand,749
Drink from Cup,Swim,843
Shake Hands,Walk,850
Shake Hands,0,850
Shake Hands,Swim,851
Shake Hands,0,851
Shake Hands,Sit,855
0,Swim,862
Drink from Cup,Sit,865
0,Swim,874
Drink from Cup,Swim,876
0,Sit,885
0,Stand,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Stand,905
Open Fridge,Stand,907
0,Stand,909
0,Swim,947
0,Stand,949
0,Walk,992
Shake Hands,Walk,993
Open Drawer 1,0,994
Shake Hands,Stand,994
0,Stand,995
Shake Hands,Stand,1004
0,Stand,1006
Open Drawer 2,Swim,1007
0,Stand,1007
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
Open Fridge,Swim,1043
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
Shake Hands,Stand,1066
0,Stand,1068
Close Drawer 3,Stand,1071
0,Stand,1073
0,Walk,1073
0,Stand,1077
0,Swim,1100
0,Stand,1102
0,Sit,1109
0,Swim,1311
Shake Hands,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Stand,1315
Close Fridge,Stand,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Open Dishwasher,Walk,1337
Shake Hands,Stand,1338
0,Stand,1340
0,Walk,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Swim,1362
0,Stand,1364
0,Walk,1365
0,Stand,1367
0,Walk,1373
0,Stand,1374
Close Dishwasher,Stand,1379
0,Stand,1382
0,Walk,1383
0,Stand,1387
0,Walk,1397
Shake Hands,Walk,1401
Open Drawer 2,0,1401
Open Drawer 2,Stand,1401
Close Drawer 2,Swim,1402
0,Stand,1404
Shake Hands,Stand,1404
0,Stand,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Walk,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Swim,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Close Door 2,Stand,1423
0,Stand,1426
0,Swim,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Clean Table,Stand,1440
0,Stand,1446
0,Walk,1448
Clean Table,0,1451
Clean Table,Swim,1451
0,Stand,1452
0,Walk,1453
0,Stand,1457
0,Walk,1460
0,Stand,1461
0,Walk,1463
0,Stand,1469
Open Door 2,Stand,1469
Open Door 2,Walk,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Close Door 1,Stand,1476
0,Walk,1481
Close Door 2,Walk,1484
Close Door 2,Stand,1485
0,Stand,1489
0,Walk,1490
0,Lie,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to look for the start and end timestamps of each activity and then calculate the duration based on the difference between these timestamps.

Here is the breakdown for each activity:

1. **Relaxing (Stand)**:
   - Start Timestamp: 336
   - End Timestamp: 1046
   - Duration: 1046 - 336 = 710

2. **Coffee time (Drink from Cup)**:
   - Start Timestamp: 843
   - End Timestamp: 876
   - Duration: 876 - 843 = 33

3. **Early morning (Lie)**:
   - Start Timestamp: 1504
   - End Timestamp: 1522
   - Duration: 1522 - 1504 = 18

4. **Cleanup (Clean Table)**:
   - Start Timestamp: 1440
   - End Timestamp: 1451
   - Duration: 1451 - 1440 = 11

5. **Sandwich time (Eat Sandwich)**:
   - Not captured in the provided data

Please note that the duration of each activity is calculated in seconds. Let me know if you need any further assistance.
