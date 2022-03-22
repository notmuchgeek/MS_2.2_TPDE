# MS_2.2_TPDE

## Mapping the phase diagram of a three-liquid mixture with the help of a solvatochromic fluorescent dye.

### Task symmetry
1.  Construct Binodal curve
2.  Trace tie-lines

### File list
1. __curve_fit_tie_line.ipynb__
  Save the spectrum (.csv) to 'curve_fit_tie_line/' and run the jupyter notebook
  Plot the spectrum curve and find wavelength for upper and lower layer of the 3 mixtures

2. __curve_fit_binodal.ipynb__
  Save the spectrum (.csv) to 'curve_fit_binodal/' and run the jupyter notebook
  Plot the spectrum curve and find wavelength for all 4 mixtures

3. __Tabulation_for_experiment_data_Workbook.ipynb__
  Calculate the mass fraction with the volumes as the input.
 
4. __Ternary_Phase_Diagram.csv__
  Save all the mass fraction values

|Colour| Corresponding String|
|:-|-:|
|black|'Binodal'|
|red|'Tie Line 1'|
|blue|'Tie Line 2'|

### Experimental Procedure

Step 1- Set up burettes with solvents

Step 2- Dispense the solution mixture for tie line into sep. funnels:
| V_water/ml | V_toluene/ml | V_ethanol/ml |
|:-:|:-:|:-:|
|8.0|5.3|9.4|
|6.0|4.6|12.7|
|3.0|10.15|10.4|

Shake for 5 min and set aside for later measurement

Step 3- Dispense the solution mixture for binodal into conical flasks (2 ppl):
| V_water/ml | V_toluene/ml | V_ethanol/ml |
|:-:|:-:|:-:|
|4.0|25.4|upon adding|
|10.0|11.5|upon adding|
|10.5|4.9|upon adding|
|16.5|1.0|upon adding|

Record vol. of ethanol added from burette

Step 4- Determine int time & scans to ave (1 ppl):
| V_water/ml | V_toluene/ml | V_ethanol/ml |
|:-:|:-:|:-:|
|2|0|0|
|0|2|0|
|0|0|2|

Add 2 μL prodan
Change int time till signal saturation (not background subtracted) & record int time
Use lowest int time of the 3 pure solvents

Step 5- Measure prodan spectra, pure solv

Step 6- Test binodal solns, plot & analyse on ternary plot

Step 7- Test tie line solns, plot & analyse on ternary plot

### Other parameters for control
| Intergration time/ms | Scans to average |
|-:|-:|
|?|10|
