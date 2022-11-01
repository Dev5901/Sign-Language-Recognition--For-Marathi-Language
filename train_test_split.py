import splitfolders

input_folder = 'C:/Users/Dev Prajapati/Desktop/Sign Language  Files/MarathiDatasetv1/'

splitfolders.ratio(input_folder, output="C:/Users/Dev Prajapati/Desktop/CNN/final_marathi_mask_splitdataset_v2/",
                   seed=42, ratio=(.8,.0,.2),
                   group_prefix=None)