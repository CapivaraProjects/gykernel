# gykernel
This repository saves all classification models and their respective notes.  
  
This works as "model control", where each trained model shold be versioned into the directory *saved_model* following by a sequence number of the new version.  
The tensorflow server will look for saved_model directory and load the last model that was deployed.  
