### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,None,92
0,Walk,261
0,Sit,272
0,Stand,302
0,Walk,315
0,Stand,319
0,Walk,326
0,Walk,330
Close Drawer 2,Stand,336
0,Stand,339
Close Fridge,Stand,343
0,Sit,345
0,Walk,347
0,Stand,355
Close Drawer 2,Stand,355
0,Walk,359
0,Walk,362
Close Drawer 2,Walk,366
Close Dishwasher,Stand,366
0,Walk,371
0,Walk,371
Close Drawer 2,Walk,378
0,Walk,380
Close Drawer 2,Walk,383
0,Walk,384
Close Drawer 2,Walk,385
0,Stand,387
Close Dishwasher,Stand,389
0,Walk,390
Close Drawer 2,Stand,391
0,Stand,393
Close Drawer 2,Stand,394
0,Walk,397
0,Sit,398
0,Walk,404
0,Walk,422
Close Door 2,Sit,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Dishwasher,0,428
Drink from Cup,Walk,428
0,Walk,428
Close Drawer 3,Walk,436
Close Drawer 2,Walk,436
0,Sit,438
0,Walk,439
0,Stand,443
Close Drawer 2,Stand,443
Drink from Cup,0,447
Close Drawer 2,Walk,447
0,Walk,447
0,Walk,673
0,Sit,675
Close Door 1,Sit,676
0,Walk,678
0,Sit,678
Close Door 1,Walk,678
Close Door 1,0,679
Close Door 1,Walk,679
0,Walk,679
0,Stand,685
Close Drawer 2,Walk,687
0,Walk,689
0,Walk,690
Close Drawer 2,Walk,699
Close Drawer 2,None,700
0,Stand,701
Close Drawer 2,Walk,702
Close Drawer 2,0,704
Close Dishwasher,0,704
Close Dishwasher,Sit,704
Close Drawer 2,0,705
Close Dishwasher,Stand,705
Close Drawer 2,Walk,706
0,Stand,708
0,Sit,711
0,Stand,714
0,Walk,718
0,Walk,721
0,Sit,722
Close Drawer 2,Walk,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Walk,733
0,Stand,735
0,Walk,747
0,Sit,749
Drink from Cup,Stand,843
Close Drawer 2,Walk,850
Close Dishwasher,0,850
Drink from Cup,Walk,851
Close Dishwasher,0,851
Drink from Cup,Walk,855
0,Walk,862
Drink from Cup,Sit,865
0,Sit,874
Close Drawer 2,Walk,876
0,Walk,885
0,Walk,889
0,Sit,896
0,Walk,897
0,Sit,900
0,Stand,905
Open Fridge,Stand,907
0,Stand,909
0,Sit,947
0,Stand,949
0,Walk,992
Close Dishwasher,Walk,993
Close Drawer 2,0,994
Close Drawer 2,Stand,994
0,Stand,995
Close Drawer 2,Stand,1004
0,Stand,1006
Drink from Cup,Walk,1007
0,Walk,1007
Close Drawer 2,Stand,1010
0,Walk,1012
0,Walk,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Stand,1034
0,Sit,1037
0,Stand,1039
0,Walk,1040
Close Dishwasher,None,1043
Open Fridge,0,1043
Open Fridge,Walk,1043
0,Walk,1046
Close Fridge,Walk,1047
Close Fridge,Walk,1048
0,Walk,1049
0,Stand,1051
0,Walk,1063
Close Drawer 2,None,1066
Close Drawer 2,0,1066
Close Drawer 2,Walk,1066
0,Walk,1068
Close Drawer 2,Stand,1071
0,Stand,1073
0,Walk,1073
0,Walk,1077
0,Sit,1100
0,Walk,1102
0,Walk,1109
0,None,1311
Open Fridge,Walk,1313
Close Dishwasher,0,1314
Open Fridge,Walk,1314
0,Walk,1315
Close Fridge,Stand,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Walk,1330
0,Sit,1335
Close Drawer 2,Walk,1337
Close Drawer 2,Walk,1338
0,Walk,1340
0,Sit,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Sit,1362
0,Walk,1364
0,Lie,1365
0,Walk,1367
0,Walk,1373
0,None,1374
Close Drawer 2,Walk,1379
0,Walk,1382
0,Sit,1383
0,Stand,1387
0,Walk,1397
Close Drawer 2,None,1401
Close Drawer 2,0,1401
Drink from Cup,Stand,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Close Drawer 2,Walk,1404
0,Stand,1406
Drink from Cup,None,1407
0,Stand,1410
0,Walk,1411
Close Drawer 2,Stand,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Close Drawer 2,Sit,1423
0,Walk,1426
0,Walk,1427
0,Walk,1436
0,Walk,1438
0,Stand,1439
Close Dishwasher,Walk,1440
0,Stand,1446
0,Walk,1448
Clean Table,0,1451
Clean Table,Walk,1451
0,Stand,1452
0,Walk,1453
0,Sit,1457
0,Sit,1460
0,Stand,1461
0,Walk,1463
0,Stand,1469
Open Door 2,Walk,1469
Drink from Cup,Sit,1473
0,Walk,1473
Close Door 1,Walk,1476
Close Door 1,0,1476
Close Door 1,Stand,1476
0,Sit,1481
Close Dishwasher,Walk,1484
Close Drawer 2,Sit,1485
0,Walk,1489
0,Walk,1490
0,Walk,1504
0,None,1522

### assistant
To calculate the duration of each activity mentioned: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time, we will need to go through the provided data and identify the timestamps for transitions between these activities. Let's analyze the data:

1. Relaxing:
    - The Relaxing activity is not explicitly labeled in the data. We can assume that any period where there is no specific activity label can be considered as Relaxing.

2. Coffee time:
    - The Coffee time activity is not explicitly labeled in the data. There is no specific label for this activity.

3. Early morning:
    - The Early morning activity is not explicitly labeled in the data. There is no specific label for this activity.

4. Cleanup:
    - The Cleanup activity may be indicated by actions such as 'Close Drawer', 'Close Fridge', 'Close Dishwasher', 'Clean Table', and other similar labels associated with cleaning tasks.

5. Sandwich time:
    - The Sandwich time activity is not explicitly labeled in the data. There is no specific label for this activity.

To accurately calculate the duration of each activity, we would need more detailed information or specific labels for each activity. You may need to look into the actual activities being performed during the timestamps to categorize them into the mentioned activities accurately.
