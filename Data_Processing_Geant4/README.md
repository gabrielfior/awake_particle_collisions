# Data processing

## Description of files

- process_csv_pandas.ipynb (IPython notebook) => reads export from Geant4 and cleans the data by including a particleID to each particle of the run, thus making the aggregation process easier. Can be used to process the raw export from Geant4 and export a complete csv, such as csv file Geant4Export_AWAKE.csv, described below.

- energy_loss_figures.ipynb (IPython notebook) => reads export from Geant4 and plots several figures, mainly related to energy loss and energy of secondary electrons.

- Geant4Export_AWAKE.csv => Data obtained as output of the Geant4 simulation (only 100k first lines), which used the PAI Model and where the detector geometry had the following dimensions:
	width: 4 cm
	length: 10 cm
	rubidium density: 1e-7 g/cm3

- particles_tracking_1000.png => tracking figure showing trajectories of different particles and how they evolve with time.

