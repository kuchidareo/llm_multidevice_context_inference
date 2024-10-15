### system
You are a helpful assstant. You'll read sensor label table and analyze what might have happened.
### user

This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    
0,Stand,92
0,Walk,261
0,Swim,272
0,Stand,302
0,Walk,315
0,Stand,319
0,Walk,326
0,Stand,330
Open Fridge,Stand,336
0,Swim,339
Shake Hands,Stand,343
0,Stand,345
0,Walk,347
0,Stand,355
Open Door 2,Stand,355
0,Stand,359
0,Swim,362
Open Door 1,Swim,366
Open Door 1,Stand,366
0,Stand,371
0,Walk,371
Open Drawer 2,Stand,378
0,Stand,380
Close Drawer 2,Swim,383
0,Stand,384
Shake Hands,Stand,385
0,Stand,387
Shake Hands,Stand,389
0,Stand,390
Shake Hands,Stand,391
0,Swim,393
Close Drawer 3,Stand,394
0,Stand,397
0,Walk,398
0,Stand,404
0,Swim,422
Close Door 2,Walk,424
Close Door 2,0,427
Close Door 2,Stand,427
Close Door 2,0,428
Close Door 2,Walk,428
0,Swim,428
Toggle Switch,Swim,436
Toggle Switch,Stand,436
0,Stand,438
0,Walk,439
0,Swim,443
Open Door 1,Stand,443
Open Door 1,0,447
Open Door 1,Swim,447
0,Walk,447
0,Stand,673
0,Swim,675
Close Door 1,Walk,676
0,Walk,678
0,Swim,678
Close Door 1,Stand,678
Close Door 1,0,679
Close Door 1,Walk,679
0,Walk,679
0,Stand,685
Open Door 2,Stand,687
0,Stand,689
0,Swim,690
Shake Hands,Swim,699
Shake Hands,Stand,700
0,Stand,701
Shake Hands,Stand,702
Close Drawer 2,0,704
Shake Hands,0,704
Shake Hands,Swim,704
Shake Hands,0,705
Shake Hands,Stand,705
Shake Hands,Stand,706
0,Swim,708
0,Swim,711
0,Swim,714
0,Walk,718
0,Stand,721
0,Swim,722
Open Fridge,Swim,723
Open Fridge,Stand,724
0,Stand,726
Close Fridge,Stand,733
0,Stand,735
0,Swim,747
0,Swim,749
Drink from Cup,Swim,843
Drink from Cup,Swim,850
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
0,Swim,896
0,Swim,897
0,Walk,900
0,Stand,905
Open Fridge,Stand,907
0,Stand,909
0,Walk,947
0,Stand,949
0,Walk,992
Shake Hands,Swim,993
Shake Hands,0,994
Shake Hands,Swim,994
0,Swim,995
Shake Hands,Stand,1004
0,Stand,1006
Shake Hands,Stand,1007
0,Swim,1007
Close Drawer 2,Stand,1010
0,Swim,1012
0,Swim,1012
0,Stand,1015
0,Walk,1025
0,Stand,1026
0,Walk,1031
0,Stand,1034
0,Walk,1037
0,Stand,1039
0,Swim,1040
Open Fridge,Swim,1043
Open Fridge,0,1043
Open Fridge,Stand,1043
0,Stand,1046
Close Fridge,Stand,1047
Shake Hands,Walk,1048
0,Walk,1049
0,Stand,1051
0,Walk,1063
Shake Hands,Walk,1066
Shake Hands,0,1066
Shake Hands,Stand,1066
0,Swim,1068
Close Drawer 3,Stand,1071
0,Stand,1073
0,Walk,1073
0,Swim,1077
0,Walk,1100
0,Stand,1102
0,Swim,1109
0,Walk,1311
Open Fridge,Walk,1313
Open Fridge,0,1314
Open Fridge,Stand,1314
0,Stand,1315
Shake Hands,Swim,1326
Close Fridge,Walk,1328
0,Walk,1328
0,Stand,1330
0,Walk,1335
Open Dishwasher,Walk,1337
Open Dishwasher,Stand,1338
0,Stand,1340
0,Swim,1352
0,Stand,1353
0,Swim,1356
0,Stand,1357
0,Walk,1362
0,Stand,1364
0,Swim,1365
0,Stand,1367
0,Walk,1373
0,Stand,1374
Shake Hands,Stand,1379
0,Stand,1382
0,Walk,1383
0,Stand,1387
0,Walk,1397
Open Drawer 2,Swim,1401
Shake Hands,0,1401
Shake Hands,Stand,1401
Close Drawer 2,Stand,1402
0,Stand,1404
Shake Hands,Stand,1404
0,Swim,1406
Close Drawer 3,Stand,1407
0,Stand,1410
0,Swim,1411
Open Door 1,Stand,1414
0,Stand,1419
0,Walk,1419
Close Door 2,Walk,1423
Close Door 2,0,1423
Close Door 2,Swim,1423
0,Stand,1426
0,Swim,1427
0,Stand,1436
0,Walk,1438
0,Stand,1439
Clean Table,Swim,1440
0,Stand,1446
0,Walk,1448
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
Close Door 1,Walk,1476
Shake Hands,0,1476
Close Door 1,Stand,1476
0,Walk,1481
Close Door 2,Walk,1484
Close Door 2,Swim,1485
0,Stand,1489
0,Swim,1490
0,Swim,1504
0,Swim,1522

### assistant
To calculate the duration of each activity, we need to find the start and end timestamp of each activity and then calculate the time difference.

Here are the start and end timestamps for each activity:

- Relaxing (Stand): Start timestamp = 0, End timestamp = 673
- Coffee time (Drink from Cup): Start timestamp = 843, End timestamp = 885
- Early morning (Open Fridge): Start timestamp = 726, End timestamp = 1047
- Cleanup (Clean Table): Start timestamp = 1440, End timestamp = 1469
- Sandwich time (Open Door 2): Start timestamp = 1469, End timestamp = 1473

Now, let's calculate the duration of each activity:

- Relaxing (Stand): Duration = 673 - 0 = 673 seconds
- Coffee time (Drink from Cup): Duration = 885 - 843 = 42 seconds
- Early morning (Open Fridge): Duration = 1047 - 726 = 321 seconds
- Cleanup (Clean Table): Duration = 1469 - 1440 = 29 seconds
- Sandwich time (Open Door 2): Duration = 1473 - 1469 = 4 seconds

Therefore, the durations of each activity are as follows:
- Relaxing: 673 seconds
- Coffee time: 42 seconds
- Early morning: 321 seconds
- Cleanup: 29 seconds
- Sandwich time: 4 seconds
