### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
Close Dishwasher,Sit,261
0,Walk,272
Close Drawer 2,Stand,302
Close Dishwasher,Sit,315
0,Walk,319
0,Walk,326
Close Drawer 2,Stand,330
Close Drawer 2,Walk,336
0,Stand,339
Close Drawer 3,Stand,343
0,Walk,345
0,Sit,347
0,Stand,355
Close Drawer 2,Sit,355
0,Sit,359
0,Walk,362
Close Dishwasher,Sit,366
Close Dishwasher,Stand,366
0,Stand,371
0,None,371
Close Drawer 2,Sit,378
0,Walk,380
Close Drawer 2,Walk,383
0,None,384
Close Drawer 2,Stand,385
0,Walk,387
Close Drawer 2,Walk,389
0,Stand,390
Close Drawer 2,None,391
0,Walk,393
Close Drawer 3,Stand,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Sit,422
Close Drawer 2,Walk,424
Close Dishwasher,0,427
Close Drawer 2,Stand,427
Close Dishwasher,0,428
Close Drawer 2,Sit,428
0,Walk,428
Close Drawer 2,Walk,436
Close Dishwasher,Walk,436
0,Walk,438
0,Walk,439
0,None,443
Close Drawer 2,Walk,443
Close Dishwasher,0,447
Close Drawer 2,Walk,447
0,Walk,447
0,Walk,673
0,Walk,675
Close Dishwasher,Walk,676
0,Walk,678
0,Walk,678
Close Dishwasher,Walk,678
Close Dishwasher,0,679
Close Drawer 2,Sit,679
0,Sit,679
0,Walk,685
0,Walk,687
Close Drawer 2,Stand,689
0,Sit,690
Close Drawer 2,Sit,699
Close Dishwasher,Stand,700
0,Sit,701
Close Drawer 2,Sit,702
Close Drawer 2,0,704
Close Drawer 2,0,704
Close Dishwasher,Sit,704
Close Drawer 2,0,705
Close Drawer 2,Sit,705
Close Drawer 2,Walk,706
0,Stand,708
0,Walk,711
0,Sit,714
0,Walk,718
0,Sit,721
0,Walk,722
Close Drawer 2,Walk,723
Close Drawer 2,Walk,724
0,Walk,726
Close Drawer 2,Stand,733
0,Stand,735
0,Walk,747
0,Stand,749
Close Drawer 2,Walk,843
Close Dishwasher,Walk,850
Close Drawer 2,0,850
Close Drawer 2,Walk,851
Close Drawer 2,0,851
Close Drawer 2,Sit,855
0,Walk,862
Close Drawer 2,Walk,865
0,Sit,874
Close Drawer 3,Walk,876
0,Walk,885
0,Walk,889
0,Sit,896
0,Stand,897
0,Sit,900
0,Walk,905
Close Drawer 2,Walk,907
0,Walk,909
0,Sit,947
0,Stand,949
0,None,992
Close Drawer 2,Sit,993
Close Drawer 2,0,994
Close Drawer 2,Stand,994
0,None,995
Close Drawer 2,Walk,1004
0,Walk,1006
Close Drawer 2,Sit,1007
0,Walk,1007
Close Drawer 2,Stand,1010
0,Walk,1012
0,Walk,1012
0,Walk,1015
0,Walk,1025
0,Walk,1026
0,Walk,1031
0,Stand,1034
0,Walk,1037
0,Walk,1039
0,Sit,1040
Close Drawer 2,Sit,1043
Close Drawer 2,0,1043
Close Drawer 2,Stand,1043
0,Stand,1046
Close Drawer 2,Sit,1047
Close Drawer 2,Sit,1048
0,Walk,1049
0,Stand,1051
Close Dishwasher,Walk,1063
Close Drawer 2,Walk,1066
Close Drawer 2,0,1066
Close Drawer 2,Stand,1066
0,Stand,1068
Close Dishwasher,Stand,1071
0,Stand,1073
0,Sit,1073
0,Stand,1077
0,Sit,1100
Close Drawer 2,Stand,1102
0,Sit,1109
0,Sit,1311
Close Drawer 2,Sit,1313
Close Drawer 2,0,1314
Close Drawer 3,Sit,1314
0,Walk,1315
Close Drawer 2,Walk,1326
Close Drawer 2,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Close Drawer 2,Walk,1337
Close Dishwasher,Walk,1338
0,Sit,1340
0,Sit,1352
Close Drawer 2,Stand,1353
0,Walk,1356
0,None,1357
0,Walk,1362
0,Walk,1364
0,Sit,1365
0,Walk,1367
0,Walk,1373
0,Walk,1374
Close Drawer 2,Walk,1379
0,Walk,1382
0,Walk,1383
0,Walk,1387
Close Drawer 2,Walk,1397
Close Dishwasher,Walk,1401
Close Drawer 2,0,1401
Close Drawer 2,Walk,1401
Close Drawer 2,Walk,1402
0,Stand,1404
Close Drawer 2,Sit,1404
0,Walk,1406
Close Drawer 2,Walk,1407
0,Stand,1410
0,Sit,1411
Close Drawer 2,Walk,1414
0,Walk,1419
0,None,1419
Close Drawer 2,Walk,1423
Close Drawer 2,0,1423
Close Drawer 2,Stand,1423
0,Walk,1426
0,Sit,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Close Drawer 2,Walk,1440
0,Sit,1446
0,Walk,1448
Close Drawer 2,0,1451
Close Drawer 2,Walk,1451
0,Stand,1452
0,Walk,1453
0,Walk,1457
0,Walk,1460
0,Stand,1461
0,Sit,1463
0,Walk,1469
Close Dishwasher,Stand,1469
Close Dishwasher,Walk,1473
0,Walk,1473
Close Dishwasher,Walk,1476
Close Drawer 2,0,1476
Close Drawer 2,Stand,1476
0,Walk,1481
Close Drawer 2,Walk,1484
Close Drawer 2,Sit,1485
0,Walk,1489
0,Walk,1490
Close Drawer 3,Sit,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to identify the start and end times of each activity based on the sensor labels provided in the CSV file. Here are the steps we can follow to calculate the duration for each activity:

1. Identify the sensor labels corresponding to each activity:
   - Relaxing (Resting or Sitting): 'Sit'
   - Coffee time (Drinking from the coffee machine or any other coffee-related activities): 'Drink'
   - Early morning (Morning activities like 'Walk' or 'Stand'): 'Walk', 'Stand'
   - Cleanup (Cleaning activities like 'Close Dishwasher' or 'Close Drawer'): 'Close Dishwasher', 'Close Drawer'
   - Sandwich time (Eating activities): None provided in the sensor labels, so we can assume any 'Eat' or 'Drink' activities indicate lunchtime.

2. Calculate the duration for each identified activity by finding the difference between the start and end timestamps of consecutive sensor labels for that activity. 

Now, let's go through the sensor labels and calculate the duration for each activity accordingly.
