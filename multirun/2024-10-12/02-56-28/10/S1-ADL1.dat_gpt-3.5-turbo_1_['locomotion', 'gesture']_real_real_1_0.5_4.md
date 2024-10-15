### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Walk,92
0,Walk,261
0,Sit,272
0,Stand,302
0,Walk,315
0,Walk,319
0,Walk,326
0,Stand,330
Drink from Cup,Sit,336
0,Sit,339
Close Drawer 2,Walk,343
0,Stand,345
0,Walk,347
0,Sit,355
Close Drawer 2,Walk,355
0,Stand,359
0,Walk,362
Close Drawer 2,Walk,366
Drink from Cup,Walk,366
0,Sit,371
0,Sit,371
Drink from Cup,None,378
0,Stand,380
Close Drawer 2,Walk,383
0,Stand,384
Close Dishwasher,Stand,385
0,Sit,387
Close Drawer 2,Stand,389
0,Stand,390
Close Drawer 2,Stand,391
0,Stand,393
Close Dishwasher,Stand,394
0,Walk,397
0,Walk,398
0,Sit,404
0,Sit,422
Close Drawer 2,Sit,424
Close Dishwasher,0,427
0,Stand,427
Close Door 2,0,428
Close Drawer 2,Sit,428
0,Walk,428
Close Drawer 2,Walk,436
Close Dishwasher,Stand,436
0,Walk,438
0,Walk,439
0,Walk,443
Close Drawer 2,Stand,443
Close Drawer 2,0,447
Close Drawer 2,Sit,447
0,None,447
0,Sit,673
0,Sit,675
Close Drawer 2,Walk,676
0,Walk,678
0,Stand,678
Close Dishwasher,Walk,678
Close Drawer 2,0,679
Drink from Cup,Walk,679
0,Sit,679
0,Stand,685
Drink from Cup,Walk,687
0,Stand,689
0,Sit,690
Drink from Cup,Sit,699
Close Drawer 2,Stand,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Drink from Cup,0,704
Close Drawer 2,Walk,704
Close Drawer 2,0,705
Drink from Cup,Stand,705
Close Dishwasher,Stand,706
0,Walk,708
0,Sit,711
0,Stand,714
0,Sit,718
0,Stand,721
0,Sit,722
Close Drawer 2,Sit,723
Close Drawer 2,Stand,724
Close Drawer 2,Stand,726
Close Drawer 2,Walk,733
0,Stand,735
0,Walk,747
0,Stand,749
Drink from Cup,Walk,843
Close Drawer 3,Sit,850
Close Drawer 2,0,850
Drink from Cup,Stand,851
Close Drawer 3,0,851
Drink from Cup,Walk,855
0,Walk,862
Close Drawer 2,Sit,865
0,Sit,874
Close Dishwasher,Walk,876
0,Sit,885
0,Stand,889
0,Walk,896
0,None,897
0,None,900
0,Stand,905
Close Drawer 2,Walk,907
0,Walk,909
0,Sit,947
0,Stand,949
0,Walk,992
Close Dishwasher,Walk,993
Close Drawer 2,0,994
Close Dishwasher,Stand,994
0,Stand,995
Close Drawer 2,Stand,1004
0,Stand,1006
Close Drawer 2,Stand,1007
0,Stand,1007
Close Drawer 2,Stand,1010
0,Walk,1012
0,Walk,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Sit,1031
0,Stand,1034
0,Sit,1037
0,Sit,1039
0,Walk,1040
Close Drawer 2,Sit,1043
Close Drawer 2,0,1043
Open Fridge,Stand,1043
0,Stand,1046
Close Dishwasher,Stand,1047
Close Dishwasher,Sit,1048
0,Walk,1049
0,Walk,1051
0,Sit,1063
Close Drawer 2,Walk,1066
Close Drawer 2,0,1066
Close Drawer 2,Stand,1066
0,Walk,1068
Close Dishwasher,Stand,1071
0,Sit,1073
0,Walk,1073
0,Walk,1077
0,Walk,1100
0,Stand,1102
0,Sit,1109
0,Walk,1311
Close Drawer 2,Walk,1313
Close Drawer 2,0,1314
Close Dishwasher,Walk,1314
0,None,1315
Close Dishwasher,Stand,1326
Close Dishwasher,Walk,1328
0,Walk,1328
0,Stand,1330
0,Sit,1335
Close Drawer 2,Walk,1337
Close Drawer 2,Stand,1338
0,Walk,1340
0,Sit,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Walk,1362
0,Sit,1364
0,Sit,1365
0,Stand,1367
0,Sit,1373
0,Stand,1374
Close Drawer 2,Stand,1379
0,Walk,1382
0,Sit,1383
0,Stand,1387
0,Walk,1397
Close Drawer 2,Walk,1401
Close Drawer 2,0,1401
Close Drawer 2,Stand,1401
Close Drawer 2,Walk,1402
0,Stand,1404
Close Drawer 2,Stand,1404
0,Stand,1406
Close Drawer 2,Stand,1407
0,Walk,1410
0,Walk,1411
Close Dishwasher,Stand,1414
0,Walk,1419
0,Sit,1419
Close Drawer 2,None,1423
Close Drawer 2,0,1423
Close Drawer 2,Stand,1423
0,Stand,1426
0,Walk,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Close Drawer 2,Stand,1440
Close Drawer 2,Stand,1446
0,Walk,1448
Close Dishwasher,0,1451
Close Drawer 2,Walk,1451
0,Stand,1452
0,Walk,1453
Drink from Cup,Stand,1457
0,Sit,1460
0,Stand,1461
0,Sit,1463
Drink from Cup,Stand,1469
Close Drawer 2,Stand,1469
Close Drawer 2,Walk,1473
0,Sit,1473
Close Drawer 2,Walk,1476
Close Drawer 2,0,1476
Close Drawer 2,Stand,1476
0,Sit,1481
Close Drawer 2,Walk,1484
Close Door 2,Stand,1485
0,Stand,1489
0,Walk,1490
0,Sit,1504
0,Sit,1522

### assistant
To calculate the duration of each activity, we first need to identify the start and end timestamps for each activity. From the provided data, it seems that the activities are represented by different labels such as "Relaxing," "Coffee time," "Early morning," "Cleanup," and "Sandwich time."

We should first map the sensor labels to the corresponding activities based on their descriptions. Then, we can calculate the duration of each activity by finding the time elapsed between the start and end timestamps.

Here are the mapping of sensor labels to activities based on the provided data:

- "Relaxing": Sit
- "Coffee time": Drink from Cup
- "Early morning": Open Fridge
- "Cleanup": Close Dishwasher
- "Sandwich time": Close Drawer

We will now calculate the duration of each activity by analyzing the timestamps and identifying the start and end of each activity. Let's perform the calculations:
