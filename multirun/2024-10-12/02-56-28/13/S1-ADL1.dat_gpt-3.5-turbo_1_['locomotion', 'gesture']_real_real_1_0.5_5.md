### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Walk,261
0,Walk,272
0,Stand,302
0,Walk,315
0,Sit,319
0,Sit,326
0,Stand,330
Close Drawer 2,None,336
0,None,339
Close Drawer 2,Walk,343
0,Walk,345
0,Walk,347
0,Walk,355
Close Drawer 2,Walk,355
0,Stand,359
0,Sit,362
Open Door 1,Walk,366
Open Door 1,Stand,366
0,Walk,371
0,Walk,371
Close Drawer 2,Stand,378
0,Stand,380
Close Drawer 2,Stand,383
0,Stand,384
Close Drawer 2,None,385
0,None,387
Close Drawer 2,Stand,389
Close Drawer 2,Stand,390
Close Drawer 2,Stand,391
0,Stand,393
Close Drawer 2,Stand,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Walk,422
Close Drawer 3,None,424
Close Dishwasher,0,427
Close Drawer 2,Stand,427
Close Drawer 2,0,428
Close Drawer 2,Walk,428
0,Walk,428
Close Drawer 2,Walk,436
Close Drawer 2,Walk,436
0,Stand,438
0,Lie,439
0,Sit,443
Open Door 1,None,443
Close Drawer 2,0,447
Close Drawer 2,Walk,447
0,Walk,447
0,Walk,673
0,Walk,675
Close Drawer 2,Walk,676
0,Sit,678
0,Stand,678
Close Drawer 3,Walk,678
Open Door 1,0,679
Open Door 1,Sit,679
0,Walk,679
0,Stand,685
Close Drawer 2,Stand,687
0,Walk,689
0,Walk,690
Close Drawer 2,Walk,699
Close Drawer 2,Walk,700
0,Stand,701
Close Drawer 2,Stand,702
Close Drawer 2,0,704
Close Dishwasher,0,704
Close Dishwasher,Walk,704
Close Drawer 2,0,705
Close Drawer 2,None,705
Close Drawer 2,Stand,706
0,Stand,708
0,Walk,711
0,Sit,714
0,Walk,718
0,Stand,721
0,Walk,722
Close Dishwasher,Walk,723
Close Dishwasher,Walk,724
0,Walk,726
Close Drawer 2,Walk,733
0,Stand,735
0,Sit,747
0,None,749
Close Drawer 2,Walk,843
Close Drawer 3,Sit,850
Close Drawer 3,0,850
Close Drawer 2,Walk,851
Close Drawer 2,0,851
Close Drawer 2,Walk,855
0,Walk,862
Close Drawer 2,Sit,865
Close Drawer 2,Walk,874
Close Drawer 2,Sit,876
0,Sit,885
0,Walk,889
0,Walk,896
0,Stand,897
0,Walk,900
0,Walk,905
Open Fridge,Stand,907
0,Stand,909
0,Walk,947
0,Stand,949
0,Sit,992
Close Drawer 2,Walk,993
Close Dishwasher,0,994
Close Drawer 2,Stand,994
0,Stand,995
Close Drawer 2,Lie,1004
0,Walk,1006
Close Drawer 2,Walk,1007
0,Walk,1007
Close Drawer 2,Sit,1010
0,Walk,1012
Close Drawer 2,Walk,1012
0,Walk,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Stand,1034
0,Walk,1037
0,Stand,1039
0,Walk,1040
Close Drawer 2,Sit,1043
Close Drawer 2,0,1043
Close Drawer 2,Stand,1043
0,Stand,1046
Close Drawer 3,Stand,1047
Close Drawer 2,Walk,1048
Close Drawer 2,Walk,1049
0,Stand,1051
0,Walk,1063
Close Drawer 2,Walk,1066
Close Drawer 2,0,1066
Close Drawer 2,Stand,1066
0,Stand,1068
Close Dishwasher,Walk,1071
0,Stand,1073
0,Walk,1073
0,Stand,1077
0,Walk,1100
0,Stand,1102
0,Sit,1109
0,None,1311
Close Drawer 2,Walk,1313
Open Fridge,0,1314
Open Fridge,Walk,1314
0,None,1315
Close Drawer 2,Stand,1326
Close Dishwasher,Walk,1328
0,Sit,1328
0,Walk,1330
0,Walk,1335
Close Drawer 2,Walk,1337
Close Drawer 2,Stand,1338
0,Stand,1340
0,Walk,1352
0,Stand,1353
0,Walk,1356
0,Stand,1357
0,Walk,1362
Close Drawer 2,Walk,1364
0,Walk,1365
0,None,1367
0,Sit,1373
0,Walk,1374
Close Dishwasher,Stand,1379
0,Stand,1382
0,Walk,1383
0,Walk,1387
0,Sit,1397
Close Drawer 2,Walk,1401
Close Drawer 2,0,1401
Close Drawer 2,Sit,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Close Drawer 2,Stand,1404
0,Walk,1406
Close Drawer 2,Walk,1407
0,Walk,1410
0,Walk,1411
Close Drawer 2,Stand,1414
0,Walk,1419
0,Sit,1419
Close Dishwasher,Walk,1423
Close Door 2,0,1423
Close Door 2,Walk,1423
0,Stand,1426
0,Walk,1427
0,Walk,1436
0,Walk,1438
0,Stand,1439
Close Dishwasher,Sit,1440
0,Walk,1446
0,Walk,1448
Close Drawer 2,0,1451
Close Dishwasher,Walk,1451
0,Stand,1452
0,Lie,1453
0,Walk,1457
Close Drawer 2,Walk,1460
0,Stand,1461
0,Walk,1463
Close Drawer 2,Stand,1469
Close Drawer 2,Stand,1469
Close Drawer 2,Sit,1473
0,Walk,1473
Close Drawer 2,Walk,1476
Close Drawer 2,0,1476
Close Drawer 2,Walk,1476
0,None,1481
Close Drawer 2,Walk,1484
Close Drawer 2,Walk,1485
0,Stand,1489
0,Walk,1490
0,Sit,1504
0,Walk,1522

### assistant
To calculate the duration of each activity mentioned: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time, you need to analyze the activities provided in the CSV file based on the labels.

Given the complexity of the activities captured by different sensors and the variations in the labels, it may not be straightforward to accurately determine the exact durations of each activity without additional context or information.

However, as an initial approach, you can try to:

1. Filter the data based on the labels related to the activities you are interested in (Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time).
2. Calculate the duration between the timestamps for each activity label.
3. Aggregate the durations for each activity to get the total duration.

One approach could be to filter the data for specific labels related to each activity and then calculate the duration between consecutive timestamps for those labels. By summing up these durations, you can approximate the total duration for each activity.

If you need further assistance or have specific criteria to define each activity, feel free to provide more details for a more accurate analysis.
