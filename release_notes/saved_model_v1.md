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
    Corynespora 
    tetranychus 
    yelow leaf 
    health 
    alternaria 
    septoria 
    xanthomonas 
    phytophthora 

### Final test accuracy  
    90.7%
     
### Plot of confusion matrix  
  
    [827  51   9  27   6  22  50   3]
    [ 56 903  10  28   0  12   6   0]
    [  1  43 905   2   0  33  46   0]
    [ 74  39   0 905   0  19   0   0]
    [ 30  15   0   6 766  45  43  61]
    [ 70   7   0  17  44 847  40   7]
    [ 41   6   3   0  17  34 918   1]
    [ 37   3   0  13  43  25   3 881]
