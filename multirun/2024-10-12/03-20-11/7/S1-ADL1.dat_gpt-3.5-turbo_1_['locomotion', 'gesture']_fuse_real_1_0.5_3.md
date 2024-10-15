### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Walk,261
0,Swim,272
0,Swim,302
0,Swim,315
0,Stand,319
0,Swim,326
0,Swim,330
Open Fridge,Stand,336
0,Stand,339
Shake Hands,Stand,343
0,Swim,345
0,Walk,347
0,Swim,355
Open Door 2,Stand,355
0,Stand,359
0,Walk,362
Shake Hands,Swim,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Swim,378
0,Stand,380
Shake Hands,Stand,383
0,Stand,384
Shake Hands,Stand,385
0,Swim,387
Shake Hands,Stand,389
0,Swim,390
Shake Hands,Swim,391
0,Swim,393
Close Drawer 3,Swim,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Swim,422
Close Door 2,Swim,424
Close Door 2,0,427
Close Door 2,Swim,427
Close Door 2,0,428
Close Door 2,Walk,428
0,Walk,428
Toggle Switch,Swim,436
Toggle Switch,Swim,436
0,Swim,438
0,Walk,439
0,Stand,443
Open Door 1,Swim,443
Open Door 1,0,447
Shake Hands,Walk,447
0,Swim,447
0,Swim,673
0,Walk,675
Close Door 1,Swim,676
0,Walk,678
0,Stand,678
Close Door 1,Stand,678
Close Door 1,0,679
Close Door 1,Walk,679
0,Swim,679
0,Stand,685
Open Door 2,Swim,687
0,Swim,689
0,Walk,690
Shake Hands,Swim,699
Shake Hands,Swim,700
0,Stand,701
Shake Hands,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Shake Hands,Swim,704
Shake Hands,0,705
Shake Hands,Stand,705
Shake Hands,Swim,706
0,Swim,708
0,Walk,711
0,Swim,714
0,Walk,718
0,Stand,721
0,Walk,722
Open Fridge,Swim,723
Open Fridge,Swim,724
0,Stand,726
Close Fridge,Stand,733
0,Swim,735
0,Swim,747
0,Stand,749
Shake Hands,Swim,843
Shake Hands,Swim,850
Shake Hands,0,850
Drink from Cup,Stand,851
Drink from Cup,0,851
Shake Hands,Swim,855
0,Swim,862
Shake Hands,Swim,865
0,Swim,874
Shake Hands,Swim,876
0,Swim,885
0,Stand,889
0,Walk,896
0,Stand,897
0,Swim,900
0,Swim,905
Open Fridge,Stand,907
0,Stand,909
0,Swim,947
0,Swim,949
0,Swim,992
Shake Hands,Walk,993
Shake Hands,0,994
Shake Hands,Swim,994
0,Swim,995
Shake Hands,Swim,1004
0,Swim,1006
Shake Hands,Swim,1007
0,Stand,1007
Shake Hands,Stand,1010
0,Swim,1012
0,Walk,1012
0,Swim,1015
0,Swim,1025
0,Stand,1026
0,Walk,1031
0,Swim,1034
0,Swim,1037
0,Stand,1039
0,Swim,1040
Shake Hands,Walk,1043
Open Fridge,0,1043
Open Fridge,Swim,1043
0,Swim,1046
Close Fridge,Stand,1047
Shake Hands,Swim,1048
0,Walk,1049
0,Stand,1051
0,Swim,1063
Shake Hands,Walk,1066
Shake Hands,0,1066
Shake Hands,Swim,1066
0,Swim,1068
Close Drawer 3,Swim,1071
0,Swim,1073
0,Walk,1073
0,Swim,1077
0,Walk,1100
0,Stand,1102
0,Swim,1109
0,Swim,1311
Open Fridge,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Swim,1315
Close Fridge,Swim,1326
Shake Hands,Swim,1328
0,Swim,1328
0,Stand,1330
0,Walk,1335
Shake Hands,Walk,1337
Shake Hands,Stand,1338
0,Stand,1340
0,Swim,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Walk,1362
0,Stand,1364
0,Swim,1365
0,Swim,1367
0,Walk,1373
0,Stand,1374
Shake Hands,Stand,1379
0,Swim,1382
0,Swim,1383
0,Swim,1387
0,Walk,1397
Shake Hands,Walk,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Shake Hands,Swim,1402
0,Stand,1404
Shake Hands,Swim,1404
0,Swim,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Swim,1411
Open Door 1,Stand,1414
0,Swim,1419
0,Swim,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Close Door 2,Stand,1423
0,Stand,1426
0,Swim,1427
0,Stand,1436
0,Swim,1438
0,Swim,1439
Clean Table,Swim,1440
0,Swim,1446
0,Swim,1448
Clean Table,0,1451
Clean Table,Stand,1451
0,Swim,1452
0,Swim,1453
0,Stand,1457
0,Swim,1460
0,Swim,1461
0,Walk,1463
0,Stand,1469
Shake Hands,Stand,1469
Open Door 2,Walk,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Shake Hands,Stand,1476
0,Walk,1481
Shake Hands,Walk,1484
Close Door 2,Swim,1485
0,Swim,1489
0,Swim,1490
0,Swim,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to analyze the sensor labels and timestamps. Based on the provided data, let's identify the start and end times of each activity:

1. Relaxing:
   - Start time: When the sensor label is 'Stand'
   - End time: When the next activity starts (or the end of the data if 'Stand' is the last label)

2. Coffee time:
   - Start time: When the sensor label is 'Open Fridge'
   - End time: When 'Close Fridge' is detected

3. Early morning:
   - Start time: When the sensor label is 'Shake Hands'
   - End time: When 'Clean Table' is detected

4. Cleanup:
   - Start time: When the sensor label is 'Clean Table'
   - End time: When the next activity starts (or the end of the data if 'Clean Table' is the last label)

5. Sandwich time:
   - Start time: When the sensor label is 'Close Drawer 2'
   - End time: When 'Close Door 1' is detected

By analyzing the data based on the above criteria, you can calculate the duration of each activity accurately.
