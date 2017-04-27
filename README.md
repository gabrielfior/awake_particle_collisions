# Master Thesis - Gabriel Fior
Link to pdf

Master thesis, developed at the Max-Planck-Institute for Physics. Investigated proton ionization of rubidium for the AWAKE collaboration using Geant4. 

This repository includes different files used for the simulation and data processing. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
cmake
Geant4 configuration - (http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/InstallationGuide/html/)
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```


End with an example of getting some data out of the system or using it for a little demo

## Geant4 part

```
cd Geant4
mkdir awake-build
cd awake-build
cmake -DCMAKE_INSTALL_PREFIX=<Path-to-Geant4-install-folder> <Path-to-awake-folder-of-this-repository> 
make
./TestEm8 testPAI.mac >> output.txt
```


## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **Gabriel Fior** - *Initial work* - [PurpleBooth](https://github.com/gabrielfior)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
If you used code from this repository, please cite the Master thesis refered in the top of the page. Thank you!