# AspenDynamicsReader
> This is a simple python module for read the time-dependent data from 
> AspenDynamics softward.  
> During my research, I dealed with planty of data pasting from softward.
> It is a time consuming step, so I built it for saving my time.

### Requirement
* Have AspenDynamics softward
* Inkscape: convert the svg plotfile to emf plotfile. If you don't need it.
  you can commont the code in 'plot_dynamic_results', and 'multiplot_dynamic_results'.
  
### Simple Using Step
1. You have to open the AspenDynamics file and finish the simulation at fisrt.
2. Specified the plot setting and the plot file name for saving.
3. Run the python script.

### Future Work:
* OOP my code.
* rebuilt the data structure by python dictionary.
* built a function can save the data with ExcelFile.

### Contributer: 
* Shen, Shiau-Jeng (johnson840205@gmail.com)

### Reference:
* Aspen Custom Modeler 2004.1 - Aspen Modeler Reference Guide