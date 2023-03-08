# Lucid-CSV-to-ROM
A small script that will convert a CSV into a ROM to be used in Lucid HDL. 

Just run the CSV2ROM script in the directory containing the rom.csv and template.luc files (I hardcoded the file names LMAO feel free to change them so that they jack straight into your working directories for )

Just follow the format in the rom.csv and edit that file. Make sure that only letters and underscores are used in your variable names. Length of adress of the rom will be calculated automatically using the length of the csv file. Addresses in the rom will reflect the row index of the CSV, which is why the values of the bottom row are at the front of the rom array, while the first rows are at the end ie. address 0 will refer to the first row etc. 
