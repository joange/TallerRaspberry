"""
This code computes pi. 

To execute this code:

python mpipypi.py
""" 

import time
import math

slice_size = 1000000
print("%15s - %20s - %24s - %24s" %("Termes calculats","Valor de pi","Error absolut","temps"))
for slices in range(1,100):


    termes=slice_size*slices
    #termes=1000000
    start = time.time()
    pi4=0.0
    i = 0
    while i < termes:
        if i%2 == 0:
            pi4 += 1.0 / (2*i+1)
        else:
            pi4 -= 1.0 / (2*i+1)
        i += 1


    end = time.time()
    pi=pi4*4;
    error = abs(pi - math.pi)
    print ("%15d - %.20f - %.24f - %4.6f" % (termes,pi,error,end - start))
    

"""
Termes calculats -          Valor de pi -            Error absolut -                    temps
        1000000 - 3.14159165358977432447 - 0.000001000000018791524781 - 0.320696
        2000000 - 3.14159215358972421228 - 0.000000500000068903716510 - 0.678612
        3000000 - 3.14159232025637358277 - 0.000000333333419533232700 - 0.951159
        4000000 - 3.14159240358965519135 - 0.000000250000137924644150 - 1.304954
        5000000 - 3.14159245358977967655 - 0.000000200000013439449731 - 1.590691
        6000000 - 3.14159248692318238128 - 0.000000166666610734722553 - 1.934949
        7000000 - 3.14159251073260037401 - 0.000000142857192741985273 - 2.217037
        8000000 - 3.14159252858969662014 - 0.000000125000096495853086 - 2.594630
        9000000 - 3.14159254247865193932 - 0.000000111111141176678530 - 2.842303
       10000000 - 3.14159255358979150330 - 0.000000100000001612698952 - 3.165223
       11000000 - 3.14159256268088782349 - 0.000000090908905292508280 - 3.474832
       12000000 - 3.14159257025672866703 - 0.000000083333064448964933 - 3.908899
       13000000 - 3.14159257666679181398 - 0.000000076923001302020566 - 4.119862
       14000000 - 3.14159258216136061392 - 0.000000071428432502074202 - 4.463009
       15000000 - 3.14159258692329590446 - 0.000000066666497211542719 - 4.769657
       16000000 - 3.14159259108978261565 - 0.000000062500010500343706 - 5.072468
       17000000 - 3.14159259476626395724 - 0.000000058823529158757992 - 5.372013
       18000000 - 3.14159259803423029922 - 0.000000055555562816778092 - 5.680238
       19000000 - 3.14159260095807679747 - 0.000000052631716318529698 - 6.038320
       20000000 - 3.14159260358981695660 - 0.000000049999976159398329 - 6.338159
       21000000 - 3.14159260597076439581 - 0.000000047619028720191636 - 6.642478
       22000000 - 3.14159260813517438038 - 0.000000045454618735618624 - 6.937639
       23000000 - 3.14159261011133894570 - 0.000000043478454170298164 - 7.261245
       24000000 - 3.14159261192298355780 - 0.000000041666809558194018 - 7.667837
       25000000 - 3.14159261358981733991 - 0.000000039999975776083829 - 7.898508
       26000000 - 3.14159261512816323503 - 0.000000038461629880970349 - 8.237002
       27000000 - 3.14159261655265309443 - 0.000000037037140021567438 - 8.678711
       28000000 - 3.14159261787536081556 - 0.000000035714432300437693 - 9.053452
       29000000 - 3.14159261910717724220 - 0.000000034482615873798750 - 9.168983
       30000000 - 3.14159262025663288398 - 0.000000033333160232018599 - 9.458880
       31000000 - 3.14159262133207173306 - 0.000000032257721382933369 - 9.793051
       32000000 - 3.14159262234036340544 - 0.000000031249429710555887 - 10.136262
       33000000 - 3.14159262328743649206 - 0.000000030302356623934656 - 10.487347
       34000000 - 3.14159262417870488449 - 0.000000029411088231512394 - 10.753532
       35000000 - 3.14159262501891278774 - 0.000000028570880328260273 - 11.182204
       36000000 - 3.14159262581249487667 - 0.000000027777298239328729 - 11.393090
       37000000 - 3.14159262656324678176 - 0.000000027026546334241175 - 11.696798
       38000000 - 3.14159262727463550746 - 0.000000026315157608536310 - 12.344476
       39000000 - 3.14159262794942861774 - 0.000000025640364498258350 - 13.105320
       40000000 - 3.14159262859046428673 - 0.000000024999328829267142 - 12.927407
       41000000 - 3.14159262920029558330 - 0.000000024389497532695259 - 12.989904
       42000000 - 3.14159262978113806852 - 0.000000023808655047474758 - 13.295428
       43000000 - 3.14159263033450919522 - 0.000000023255283920775582 - 13.642038
       44000000 - 3.14159263086306106416 - 0.000000022726732051836507 - 14.166529
       45000000 - 3.14159263136792210602 - 0.000000022221871009975303 - 18.144089
       46000000 - 3.14159263185110448902 - 0.000000021738688626982139 - 15.526126
       47000000 - 3.14159263231364427327 - 0.000000021276148842730436 - 14.984807
       48000000 - 3.14159263275689948358 - 0.000000020832893632416472 - 15.998638
       49000000 - 3.14159263318206249949 - 0.000000020407730616511799 - 16.211900
       50000000 - 3.14159263359025064943 - 0.000000019999542466564435 - 15.824917

       51000000 - 3.14159263398259369637 - 0.000000019607199419624521 - 16.671767
       52000000 - 3.14159263435969560163 - 0.000000019230097514366662 - 18.165961
       53000000 - 3.14159263472257777039 - 0.000000018867215345608201 - 20.870288
       54000000 - 3.14159263507204267185 - 0.000000018517750444146941 - 19.432410
       55000000 - 3.14159263540841537932 - 0.000000018181377736681270 - 20.778116
       56000000 - 3.14159263573304858852 - 0.000000017856744527477986 - 21.691004
       57000000 - 3.14159263604633354205 - 0.000000017543459573943210 - 22.481795
       58000000 - 3.14159263634877161664 - 0.000000017241021499359022 - 20.109126
       59000000 - 3.14159263664097387903 - 0.000000016948819236972668 - 22.266783
       60000000 - 3.14159263692348433850 - 0.000000016666308777502081 - 24.452328
       61000000 - 3.14159263719678616411 - 0.000000016393006951886946 - 22.161241
       62000000 - 3.14159263746117467520 - 0.000000016128618440802711 - 24.638953
       63000000 - 3.14159263771716767977 - 0.000000015872625436230692 - 23.759246
       64000000 - 3.14159263796508625433 - 0.000000015624706861672166 - 30.939856
       65000000 - 3.14159263820549350399 - 0.000000015384299612009045 - 26.219840
       66000000 - 3.14159263843852309961 - 0.000000015151270016389162 - 24.608658
       67000000 - 3.14159263866465110482 - 0.000000014925142011179560 - 26.468933
       68000000 - 3.14159263888416750987 - 0.000000014705625606126205 - 25.876692
       69000000 - 3.14159263909724995045 - 0.000000014492543165545158 - 24.941987
       70000000 - 3.14159263930424215161 - 0.000000014285550964387994 - 25.939534
       71000000 - 3.14159263950544964672 - 0.000000014084343469278338 - 22.769373
       72000000 - 3.14159263970097324403 - 0.000000013888819871965552 - 23.195288
       73000000 - 3.14159263989122505834 - 0.000000013698568057662897 - 34.548183
       74000000 - 3.14159264007625482762 - 0.000000013513538288378868 - 31.370914
       75000000 - 3.14159264025639517470 - 0.000000013333397941295289 - 26.865900
       76000000 - 3.14159264043182506754 - 0.000000013157968048460589 - 26.387717
       77000000 - 3.14159264060268972329 - 0.000000012987103392703148 - 25.522628
       78000000 - 3.14159264076914857000 - 0.000000012820644545996629 - 26.438994
       79000000 - 3.14159264093141299412 - 0.000000012658380121877144 - 26.401431
       80000000 - 3.14159264108963309781 - 0.000000012500160018191764 - 27.866634
       81000000 - 3.14159264124405979146 - 0.000000012345733324536923 - 27.918238
       82000000 - 3.14159264139464688981 - 0.000000012195146226190445 - 26.004379
       83000000 - 3.14159264154157114035 - 0.000000012048221975646811 - 26.371993
       84000000 - 3.14159264168505547588 - 0.000000011904737640122676 - 27.103613
       85000000 - 3.14159264182496977824 - 0.000000011764823337756525 - 26.899919
       86000000 - 3.14159264196174969896 - 0.000000011628043417033496 - 27.464610
       87000000 - 3.14159264209541300161 - 0.000000011494380114385194 - 27.921106
       88000000 - 3.14159264222603429317 - 0.000000011363758822824366 - 80.641338
       89000000 - 3.14159264235373214547 - 0.000000011236060970531980 - 32.767072
       90000000 - 3.14159264247847280771 - 0.000000011111320308287986 - 28.494015
       91000000 - 3.14159264260052273343 - 0.000000010989270382566474 - 31.774435
       92000000 - 3.14159264271997695772 - 0.000000010869816158276535 - 31.161478
       93000000 - 3.14159264283681682883 - 0.000000010752976287164984 - 29.581811
       94000000 - 3.14159264295118223487 - 0.000000010638610881130717 - 29.931979
       95000000 - 3.14159264306292218549 - 0.000000010526870930505083 - 30.186862
       96000000 - 3.14159264317261044397 - 0.000000010417182672028957 - 30.378450
       97000000 - 3.14159264327994813826 - 0.000000010309844977740568 - 30.907589
       98000000 - 3.14159264338518839921 - 0.000000010204604716790300 - 30.975943
       99000000 - 3.14159264348826283708 - 0.000000010101530278916471 - 31.239084
       
       Computat en:
            Nombre del modelo:	MacBook Pro
            Identificador del modelo:	MacBookPro12,1
            Nombre del procesador:	Intel Core i5 de doble núcleo
            Velocidad del procesador:	2.7 GHz
            Cantidad de procesadores:	1
            Cantidad total de núcleos:	2
            Caché de nivel 2 (por núcleo):	256 KB
            Caché de nivel 3:	3 MB
            Tecnología Hyper-Threading:	Activado
       """


"""
En la raspberry Pi 3b
pi@node1:~/cloud $ python pi.py 
Termes calculats - Valor de pi          - Error absolut            - temps                   
        1000000 - 3.14159165358977432447 - 0.000001000000018791524781 - 2.226878
        2000000 - 3.14159215358972421228 - 0.000000500000068903716510 - 4.451041
        3000000 - 3.14159232025637358277 - 0.000000333333419533232700 - 6.684953
        4000000 - 3.14159240358965519135 - 0.000000250000137924644150 - 8.915636
        5000000 - 3.14159245358977967655 - 0.000000200000013439449731 - 11.140476
        6000000 - 3.14159248692318238128 - 0.000000166666610734722553 - 13.364931
        7000000 - 3.14159251073260037401 - 0.000000142857192741985273 - 15.596777
        8000000 - 3.14159252858969662014 - 0.000000125000096495853086 - 17.816602
        9000000 - 3.14159254247865193932 - 0.000000111111141176678530 - 20.058275
       10000000 - 3.14159255358979150330 - 0.000000100000001612698952 - 22.288024
       11000000 - 3.14159256268088782349 - 0.000000090908905292508280 - 24.503358
       12000000 - 3.14159257025672866703 - 0.000000083333064448964933 - 26.746585
       13000000 - 3.14159257666679181398 - 0.000000076923001302020566 - 28.967858
       14000000 - 3.14159258216136061392 - 0.000000071428432502074202 - 31.200578
       15000000 - 3.14159258692329590446 - 0.000000066666497211542719 - 33.430177
       16000000 - 3.14159259108978261565 - 0.000000062500010500343706 - 35.641517
       17000000 - 3.14159259476626395724 - 0.000000058823529158757992 - 37.879202
       18000000 - 3.14159259803423029922 - 0.000000055555562816778092 - 40.106844
       19000000 - 3.14159260095807679747 - 0.000000052631716318529698 - 42.351395
       20000000 - 3.14159260358981695660 - 0.000000049999976159398329 - 44.570882
       21000000 - 3.14159260597076439581 - 0.000000047619028720191636 - 46.812782
       22000000 - 3.14159260813517438038 - 0.000000045454618735618624 - 49.050457
       23000000 - 3.14159261011133894570 - 0.000000043478454170298164 - 51.251129
       24000000 - 3.14159261192298355780 - 0.000000041666809558194018 - 53.471301
       25000000 - 3.14159261358981733991 - 0.000000039999975776083829 - 55.699009
       26000000 - 3.14159261512816323503 - 0.000000038461629880970349 - 57.947729
       27000000 - 3.14159261655265309443 - 0.000000037037140021567438 - 60.168473
       28000000 - 3.14159261787536081556 - 0.000000035714432300437693 - 62.415261
       29000000 - 3.14159261910717724220 - 0.000000034482615873798750 - 64.640479
       30000000 - 3.14159262025663288398 - 0.000000033333160232018599 - 66.855950
       31000000 - 3.14159262133207173306 - 0.000000032257721382933369 - 69.103934
       32000000 - 3.14159262234036340544 - 0.000000031249429710555887 - 71.332312
       33000000 - 3.14159262328743649206 - 0.000000030302356623934656 - 73.542635
       34000000 - 3.14159262417870488449 - 0.000000029411088231512394 - 75.762697
       35000000 - 3.14159262501891278774 - 0.000000028570880328260273 - 77.967030
       36000000 - 3.14159262581249487667 - 0.000000027777298239328729 - 80.166290
       37000000 - 3.14159262656324678176 - 0.000000027026546334241175 - 82.426869
       38000000 - 3.14159262727463550746 - 0.000000026315157608536310 - 84.700377
       39000000 - 3.14159262794942861774 - 0.000000025640364498258350 - 86.899936
       40000000 - 3.14159262859046428673 - 0.000000024999328829267142 - 89.142474
       41000000 - 3.14159262920029558330 - 0.000000024389497532695259 - 91.363036
       42000000 - 3.14159262978113806852 - 0.000000023808655047474758 - 93.616701
       43000000 - 3.14159263033450919522 - 0.000000023255283920775582 - 95.861488
       44000000 - 3.14159263086306106416 - 0.000000022726732051836507 - 98.079601
       45000000 - 3.14159263136792210602 - 0.000000022221871009975303 - 100.284547
       46000000 - 3.14159263185110448902 - 0.000000021738688626982139 - 102.511627
       47000000 - 3.14159263231364427327 - 0.000000021276148842730436 - 104.746016
       48000000 - 3.14159263275689948358 - 0.000000020832893632416472 - 106.944472
       49000000 - 3.14159263318206249949 - 0.000000020407730616511799 - 109.194680
       50000000 - 3.14159263359025064943 - 0.000000019999542466564435 - 111.418706
       51000000 - 3.14159263398259369637 - 0.000000019607199419624521 - 113.686152
       52000000 - 3.14159263435969560163 - 0.000000019230097514366662 - 115.886222
       53000000 - 3.14159263472257777039 - 0.000000018867215345608201 - 118.127504
       54000000 - 3.14159263507204267185 - 0.000000018517750444146941 - 120.357104
       55000000 - 3.14159263540841537932 - 0.000000018181377736681270 - 122.604068
       56000000 - 3.14159263573304858852 - 0.000000017856744527477986 - 124.798340
       57000000 - 3.14159263604633354205 - 0.000000017543459573943210 - 127.084744
       58000000 - 3.14159263634877161664 - 0.000000017241021499359022 - 129.277483
       59000000 - 3.14159263664097387903 - 0.000000016948819236972668 - 131.509665
       60000000 - 3.14159263692348433850 - 0.000000016666308777502081 - 133.731752
       61000000 - 3.14159263719678616411 - 0.000000016393006951886946 - 135.951909
       62000000 - 3.14159263746117467520 - 0.000000016128618440802711 - 138.194960
       63000000 - 3.14159263771716767977 - 0.000000015872625436230692 - 140.461678
       64000000 - 3.14159263796508625433 - 0.000000015624706861672166 - 142.620294
       65000000 - 3.14159263820549350399 - 0.000000015384299612009045 - 144.865217
       66000000 - 3.14159263843852309961 - 0.000000015151270016389162 - 147.078035
       67000000 - 3.14159263866465110482 - 0.000000014925142011179560 - 149.343685
       68000000 - 3.14159263888416750987 - 0.000000014705625606126205 - 151.562355
       69000000 - 3.14159263909724995045 - 0.000000014492543165545158 - 153.767968
       70000000 - 3.14159263930424215161 - 0.000000014285550964387994 - 156.045050
       71000000 - 3.14159263950544964672 - 0.000000014084343469278338 - 158.247371
       72000000 - 3.14159263970097324403 - 0.000000013888819871965552 - 160.477253
       73000000 - 3.14159263989122505834 - 0.000000013698568057662897 - 162.753048
       74000000 - 3.14159264007625482762 - 0.000000013513538288378868 - 164.986339
       75000000 - 3.14159264025639517470 - 0.000000013333397941295289 - 167.160425
       76000000 - 3.14159264043182506754 - 0.000000013157968048460589 - 169.387634
       77000000 - 3.14159264060268972329 - 0.000000012987103392703148 - 171.617572
       78000000 - 3.14159264076914857000 - 0.000000012820644545996629 - 173.851326
       79000000 - 3.14159264093141299412 - 0.000000012658380121877144 - 176.094447
       80000000 - 3.14159264108963309781 - 0.000000012500160018191764 - 178.272599
       81000000 - 3.14159264124405979146 - 0.000000012345733324536923 - 180.538979
       82000000 - 3.14159264139464688981 - 0.000000012195146226190445 - 182.743554
       83000000 - 3.14159264154157114035 - 0.000000012048221975646811 - 185.070622
       84000000 - 3.14159264168505547588 - 0.000000011904737640122676 - 187.237890
       85000000 - 3.14159264182496977824 - 0.000000011764823337756525 - 189.393319
       86000000 - 3.14159264196174969896 - 0.000000011628043417033496 - 191.674468
       87000000 - 3.14159264209541300161 - 0.000000011494380114385194 - 193.852352
       88000000 - 3.14159264222603429317 - 0.000000011363758822824366 - 196.159563
       89000000 - 3.14159264235373214547 - 0.000000011236060970531980 - 198.378236
       90000000 - 3.14159264247847280771 - 0.000000011111320308287986 - 200.599990
       91000000 - 3.14159264260052273343 - 0.000000010989270382566474 - 202.841030
       92000000 - 3.14159264271997695772 - 0.000000010869816158276535 - 205.024236
       93000000 - 3.14159264283681682883 - 0.000000010752976287164984 - 207.260638
       94000000 - 3.14159264295118223487 - 0.000000010638610881130717 - 209.496520
       95000000 - 3.14159264306292218549 - 0.000000010526870930505083 - 211.722310
       96000000 - 3.14159264317261044397 - 0.000000010417182672028957 - 214.054830
       97000000 - 3.14159264327994813826 - 0.000000010309844977740568 - 216.154399
       98000000 - 3.14159264338518839921 - 0.000000010204604716790300 - 218.444615
       99000000 - 3.14159264348826283708 - 0.000000010101530278916471 - 220.646635
"""

"""

    AMB 4 CORES PER NODE
pi@node1:~/cloud $ mpiexec -np 4 -f machinefile_4.4 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 47.627513
pi@node1:~/cloud $ mpiexec -np 8 -f machinefile_4.4 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 22.411443
pi@node1:~/cloud $ mpiexec -np 16 -f machinefile_4.4 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977369762 - 0.000000020000019418375814 - 11.242724
pi@node1:~/cloud $ mpiexec -np 32 -f machinefile_4.4 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 11.460950
pi@node1:~/cloud $ mpiexec -np 64 -f machinefile_4.4 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 12.539022

    AMB DOS CORES PER NODE
pi@node1:~/cloud $ mpiexec -np 4 -f machinefile_4.2 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 47.776898
pi@node1:~/cloud $ mpiexec -np 8 -f machinefile_4.2 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 22.385452
pi@node1:~/cloud $ mpiexec -np 16 -f machinefile_4.2 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 11.251353
pi@node1:~/cloud $ mpiexec -np 32 -f machinefile_4.2 python mpipypi.py
Termes calculats - Valor de pi          - Error absolut            - temps                   
       50000000 - 3.14159263358977325353 - 0.000000020000019862465024 - 11.402110
"""