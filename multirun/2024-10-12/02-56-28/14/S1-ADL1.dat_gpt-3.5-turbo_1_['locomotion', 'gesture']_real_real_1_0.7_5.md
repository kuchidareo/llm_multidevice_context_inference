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
0,Sit,330
Close Drawer 2,Stand,336
0,Stand,339
Close Drawer 2,Walk,343
0,Walk,345
0,Sit,347
0,Walk,355
Close Drawer 2,Stand,355
0,Walk,359
0,Walk,362
Close Drawer 2,Sit,366
Close Dishwasher,Walk,366
0,Stand,371
Close Drawer 2,Sit,371
Close Drawer 2,Stand,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Close Drawer 2,Walk,385
0,Stand,387
Close Drawer 2,Stand,389
0,Walk,390
Close Drawer 2,Sit,391
0,Stand,393
Close Dishwasher,Stand,394
0,Walk,397
Close Drawer 2,Sit,398
0,Walk,404
Close Dishwasher,Walk,422
Close Dishwasher,Walk,424
Close Drawer 2,0,427
Close Drawer 2,Stand,427
Close Drawer 2,0,428
Close Drawer 2,Sit,428
0,Sit,428
Close Dishwasher,Sit,436
Close Drawer 2,Stand,436
0,Sit,438
0,Walk,439
0,Stand,443
Close Drawer 2,Stand,443
Close Drawer 2,0,447
Close Drawer 2,Walk,447
0,Walk,447
0,Walk,673
0,Walk,675
Close Drawer 2,Sit,676
0,Sit,678
0,Stand,678
Close Dishwasher,Stand,678
Close Drawer 2,0,679
Close Drawer 2,None,679
0,Sit,679
0,Stand,685
Close Drawer 2,Walk,687
0,Stand,689
0,Walk,690
Close Drawer 2,Sit,699
Close Drawer 2,Walk,700
0,Stand,701
Close Drawer 2,Sit,702
Close Drawer 2,0,704
Close Dishwasher,0,704
Close Drawer 2,Sit,704
Close Dishwasher,0,705
Close Drawer 2,Walk,705
Close Drawer 2,Stand,706
Close Dishwasher,Walk,708
0,Walk,711
0,Walk,714
0,Walk,718
0,Stand,721
0,Walk,722
Close Drawer 2,Sit,723
0,Walk,724
0,Stand,726
Close Drawer 2,Stand,733
0,Walk,735
0,Sit,747
0,Walk,749
Close Drawer 2,Stand,843
Close Drawer 3,Sit,850
Close Drawer 2,0,850
Close Dishwasher,Stand,851
Close Drawer 2,0,851
Close Drawer 2,Sit,855
0,Walk,862
Close Drawer 2,Sit,865
0,Sit,874
Close Drawer 2,Sit,876
0,Walk,885
0,Sit,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Walk,905
Close Drawer 2,Walk,907
0,Stand,909
0,Walk,947
0,Stand,949
0,Sit,992
Close Dishwasher,Walk,993
Close Dishwasher,0,994
Close Dishwasher,Stand,994
0,Stand,995
Close Drawer 2,Sit,1004
0,Walk,1006
Close Drawer 2,Sit,1007
0,Walk,1007
Close Drawer 2,Stand,1010
0,Stand,1012
0,Walk,1012
Close Drawer 2,Sit,1015
0,Walk,1025
0,Stand,1026
0,Sit,1031
0,Walk,1034
0,Walk,1037
0,Sit,1039
0,Walk,1040
Close Drawer 2,Sit,1043
Close Drawer 2,0,1043
Close Dishwasher,Stand,1043
0,Stand,1046
Close Drawer 2,Sit,1047
Close Drawer 2,Walk,1048
0,Walk,1049
0,Stand,1051
0,Walk,1063
Close Dishwasher,Walk,1066
Close Drawer 2,0,1066
Close Drawer 2,Walk,1066
0,Stand,1068
Close Drawer 2,Stand,1071
0,Stand,1073
0,Walk,1073
Close Dishwasher,Stand,1077
0,Sit,1100
Close Dishwasher,Sit,1102
0,Sit,1109
0,Walk,1311
Close Drawer 2,Walk,1313
Close Dishwasher,0,1314
Close Dishwasher,Stand,1314
0,Walk,1315
Close Drawer 2,Walk,1326
Close Drawer 2,Walk,1328
0,Sit,1328
0,Walk,1330
0,Sit,1335
Close Drawer 2,Sit,1337
Close Drawer 2,Stand,1338
0,Walk,1340
0,Walk,1352
0,Walk,1353
0,Walk,1356
0,Sit,1357
0,Walk,1362
0,Walk,1364
0,Walk,1365
0,Stand,1367
0,Walk,1373
0,Walk,1374
Close Drawer 2,Walk,1379
0,Stand,1382
0,Walk,1383
Close Drawer 2,Stand,1387
0,Walk,1397
Close Drawer 2,Walk,1401
Close Dishwasher,0,1401
Close Drawer 2,Stand,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Close Drawer 2,Walk,1404
0,Stand,1406
Close Dishwasher,None,1407
0,Stand,1410
0,Walk,1411
Close Dishwasher,Stand,1414
0,Walk,1419
0,Walk,1419
Close Drawer 2,None,1423
Close Drawer 2,0,1423
Close Drawer 2,Walk,1423
0,Stand,1426
Close Drawer 2,Walk,1427
Close Drawer 2,Stand,1436
0,Walk,1438
0,None,1439
Close Drawer 2,Walk,1440
0,Sit,1446
0,Walk,1448
Close Dishwasher,0,1451
Close Drawer 2,Stand,1451
0,Stand,1452
0,Sit,1453
0,Walk,1457
0,Walk,1460
Close Drawer 2,Stand,1461
0,Sit,1463
0,Stand,1469
0,None,1469
Close Drawer 2,Walk,1473
0,Walk,1473
Close Drawer 2,Walk,1476
Close Drawer 2,0,1476
Close Drawer 2,Walk,1476
Close Drawer 2,Sit,1481
Close Drawer 2,Sit,1484
Close Drawer 2,Sit,1485
0,Walk,1489
0,Walk,1490
Close Drawer 2,Sit,1504
0,Walk,1522

### assistant
To calculate the duration of each activity, we need to find the timestamps for the start and end of each activity. Then, we can calculate the duration by subtracting the start time from the end time.

Here are the timestamps for each activity:
- Relaxing: 678 to 704
- Coffee time: 851 to 854
- Early morning: 0 to 303
- Cleanup: 1066 to 1313
- Sandwich time: 704 to 727

Now, we can calculate the duration of each activity:
- Relaxing: 704 - 678 = 26
- Coffee time: 854 - 851 = 3
- Early morning: 303 - 0 = 303
- Cleanup: 1313 - 1066 = 247
- Sandwich time: 727 - 704 = 23

Therefore, the durations of each activity are as follows:
- Relaxing: 26 minutes
- Coffee time: 3 minutes
- Early morning: 303 minutes
- Cleanup: 247 minutes
- Sandwich time: 23 minutes
