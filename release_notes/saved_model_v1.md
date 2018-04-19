## Tomate dieseas classifier model  

### Parameters used 
    learning rate: 0.01
    how many images: 1400
    test percentage: 10%
    validation percentage: 10%
    how many steps: 4000
    architecture: inceptionv3
    train batch size: 100
    test batcch size: -1
    any distortions: N/A
 
### Output classes 
    1) Corynespora 
    2) tetranychus 
    3) yelow leaf 
    4) health 
    5) alternaria 
    6) septoria 
    7) xanthomonas 
    8) phytophthora 

### Final evaluation result 
     
 
### Plot of confusion matrix 
|      |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
| ---  |      ---      |      ---      |      ---     |    ---   |      ---     |     ---    |      ---      |       ---      |
|**1** |     **0**     |       0       |       0      |     0    |       0      |      0     |       0       |        0       |
|**2** |       0       |     **0**     |       0      |     0    |       0      |      0     |       0       |        0       |
|**3** |       0       |       0       |     **0**    |     0    |       0      |      0     |       0       |        0       |
|**4** |       0       |       0       |       0      |   **0**  |       0      |      0     |       0       |        0       |
|**5** |       0       |       0       |       0      |     0    |     **0**    |      0     |       0       |        0       |
|**6** |       0       |       0       |       0      |     0    |       0      |    **0**   |       0       |        0       |
|**7** |       0       |       0       |       0      |     0    |       0      |      0     |     **0**     |        0       |
|**8** |       0       |       0       |       0      |     0    |       0      |      0     |       0       |      **0**     |
