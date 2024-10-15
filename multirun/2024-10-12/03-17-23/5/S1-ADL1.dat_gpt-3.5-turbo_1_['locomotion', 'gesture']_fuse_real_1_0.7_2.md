### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Swim,92
0,Walk,261
0,Swim,272
0,Stand,302
0,Walk,315
0,Swim,319
0,Swim,326
0,Swim,330
Open Fridge,Stand,336
0,Swim,339
Shake Hands,Stand,343
0,Swim,345
0,Swim,347
0,Stand,355
Shake Hands,Stand,355
0,Swim,359
0,Swim,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Shake Hands,Stand,378
0,Swim,380
Shake Hands,Swim,383
0,Swim,384
Shake Hands,Stand,385
0,Stand,387
Shake Hands,Stand,389
0,Swim,390
Shake Hands,Stand,391
0,Stand,393
Close Drawer 3,Swim,394
0,Stand,397
0,Swim,398
0,Swim,404
0,Swim,422
Shake Hands,Swim,424
Close Door 2,0,427
Close Door 2,Swim,427
Close Door 2,0,428
Close Door 2,Swim,428
0,Swim,428
Shake Hands,Walk,436
Shake Hands,Stand,436
0,Swim,438
0,Walk,439
0,Swim,443
Shake Hands,Swim,443
Open Door 1,0,447
Open Door 1,Swim,447
0,Swim,447
0,Swim,673
0,Swim,675
Close Door 1,Swim,676
0,Swim,678
0,Stand,678
Shake Hands,Stand,678
Close Door 1,0,679
Shake Hands,Swim,679
0,Walk,679
0,Swim,685
Shake Hands,Swim,687
0,Swim,689
0,Walk,690
Shake Hands,Swim,699
Shake Hands,Stand,700
0,Swim,701
Shake Hands,Swim,702
Shake Hands,0,704
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
0,Swim,722
Open Fridge,Swim,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Swim,733
0,Swim,735
0,Swim,747
0,Stand,749
Shake Hands,Swim,843
Shake Hands,Swim,850
Shake Hands,0,850
Drink from Cup,Swim,851
Shake Hands,0,851
Shake Hands,Swim,855
0,Swim,862
Drink from Cup,Swim,865
0,Swim,874
Drink from Cup,Swim,876
0,Swim,885
0,Swim,889
0,Walk,896
0,Stand,897
0,Swim,900
0,Swim,905
Open Fridge,Swim,907
0,Swim,909
Shake Hands,Swim,947
0,Swim,949
0,Swim,992
Shake Hands,Swim,993
Shake Hands,0,994
Shake Hands,Swim,994
0,Stand,995
Shake Hands,Stand,1004
0,Stand,1006
Shake Hands,Stand,1007
0,Stand,1007
Close Drawer 2,Swim,1010
0,Swim,1012
0,Swim,1012
0,Swim,1015
0,Swim,1025
0,Stand,1026
0,Swim,1031
0,Swim,1034
0,Swim,1037
0,Swim,1039
0,Swim,1040
Shake Hands,Swim,1043
Open Fridge,0,1043
Open Fridge,Swim,1043
0,Stand,1046
Shake Hands,Stand,1047
Shake Hands,Swim,1048
0,Swim,1049
0,Swim,1051
0,Swim,1063
Shake Hands,Swim,1066
Shake Hands,0,1066
Shake Hands,Stand,1066
0,Swim,1068
Shake Hands,Swim,1071
0,Swim,1073
0,Walk,1073
0,Swim,1077
0,Swim,1100
0,Stand,1102
0,Swim,1109
0,Swim,1311
Shake Hands,Swim,1313
Open Fridge,0,1314
Open Fridge,Swim,1314
0,Stand,1315
Close Fridge,Stand,1326
Shake Hands,Swim,1328
0,Walk,1328
0,Swim,1330
0,Swim,1335
Shake Hands,Swim,1337
Shake Hands,Swim,1338
0,Swim,1340
0,Swim,1352
0,Swim,1353
0,Walk,1356
0,Swim,1357
0,Swim,1362
0,Swim,1364
0,Swim,1365
0,Swim,1367
0,Swim,1373
0,Swim,1374
Shake Hands,Swim,1379
0,Stand,1382
0,Swim,1383
0,Swim,1387
0,Swim,1397
Shake Hands,Swim,1401
Shake Hands,0,1401
Shake Hands,Swim,1401
Close Drawer 2,Swim,1402
0,Swim,1404
Shake Hands,Swim,1404
Shake Hands,Stand,1406
Shake Hands,Swim,1407
0,Stand,1410
0,Swim,1411
Open Door 1,Swim,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Swim,1423
Close Door 2,0,1423
Close Door 2,Swim,1423
0,Stand,1426
0,Walk,1427
0,Swim,1436
0,Walk,1438
0,Stand,1439
Shake Hands,Swim,1440
0,Swim,1446
0,Swim,1448
Shake Hands,0,1451
Shake Hands,Swim,1451
0,Swim,1452
0,Swim,1453
0,Swim,1457
0,Walk,1460
0,Swim,1461
0,Swim,1463
0,Swim,1469
Shake Hands,Swim,1469
Shake Hands,Walk,1473
0,Walk,1473
Shake Hands,Walk,1476
Shake Hands,0,1476
Shake Hands,Swim,1476
0,Walk,1481
Shake Hands,Walk,1484
Shake Hands,Swim,1485
0,Swim,1489
0,Swim,1490
0,Swim,1504
0,Swim,1522

### assistant
To calculate the duration of each activity, we need to determine the start and end times for each activity label. Then we can calculate the duration by subtracting the start time from the end time.

Here are the start and end times for the activities mentioned:

- Relaxing: Start time is when no activity is recorded before relaxation, and it ends when a different activity is recorded.
- Coffee time: Start time is when "Open Fridge" activity is recorded, and it ends when "Close Fridge" activity is recorded.
- Early morning: Start time is when the first activity of the day is recorded, and it ends when the last activity before "Sandwich time" is recorded.
- Cleanup: Start time is when "Close Drawer 2, Swim" activity is recorded, and it ends when the last activity before "Open Door 1" is recorded.
- Sandwich time: Start time is when the first activity after "Open Door 1" is recorded, and it ends when the last activity of the day is recorded.

By analyzing the activity log, we can identify the timestamps for each activity and calculate their respective durations. Let's proceed with this analysis.
