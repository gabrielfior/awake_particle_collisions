//
/////////////////////////////////////////////////////////////////////////
//
// Detector Construction File
//
// Created: 23.03.2017 Gabriel Fior
//
// Adapted from: TestEm8, Geant4 examples, authored by V. Ivanchenko based on V. Grichine code.
// Source: http://geant4.web.cern.ch/geant4/UserDocumentation/Doxygen/examples_doc/html/ExampleTestEm8.html
//
////////////////////////////////////////////////////////////////////////
// 
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#include "DetectorConstruction.hh"
#include "DetectorMessenger.hh"
#include "TargetSD.hh"

#include "G4Material.hh"
#include "G4Tubs.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"

#include "G4SDManager.hh"
#include "G4GeometryManager.hh"
#include "G4RunManager.hh"
#include "G4NistManager.hh"

#include "G4Region.hh"
#include "G4RegionStore.hh"
#include "G4PhysicalVolumeStore.hh"
#include "G4LogicalVolumeStore.hh"
#include "G4SolidStore.hh"
#include "G4ProductionCuts.hh"

#include "G4VisAttributes.hh"
#include "G4Colour.hh"

#include "G4UnitsTable.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"
#include "G4ios.hh"
#include "TestParameters.hh"
#include "G4PionPlus.hh"

#include "G4PVReplica.hh"
#include "G4Box.hh"
#include "G4UserLimits.hh"


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

DetectorConstruction::DetectorConstruction()
  : G4VUserDetectorConstruction(),
    fGasMat(0), fWindowMat(0), fWorldMaterial(0),
    fSolidWorld(0), fSolidContainer(0), fSolidDetector(0),
    fPhysWorld(0), fLogicWorld(0), fLogicContainer(0), fLogicDetector(0),
    fDetectorMessenger(0), fGasDetectorCuts(0), fRegGasDet(0)
,stepLimit(0),layerLV(0)
{
  fGasThickness = 1.0*cm;
  fGasRadius    = 4.*cm;

  fWindowThick  = 0.0*mm;

  DefineMaterials();

  fDetectorMessenger = new DetectorMessenger(this);

  //G4double cut = 0.1*mm;
  G4double cut = 1.8*mm;
  
  fGasDetectorCuts   = new G4ProductionCuts();
  fGasDetectorCuts->SetProductionCut(cut,"gamma");
  fGasDetectorCuts->SetProductionCut(cut,"e-");
  fGasDetectorCuts->SetProductionCut(cut,"e+");
  fGasDetectorCuts->SetProductionCut(cut,"proton");
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

DetectorConstruction::~DetectorConstruction()
{ 
  delete fDetectorMessenger;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::DefineMaterials()
{ 
  //This function illustrates the possible ways to define materials 
  G4String name, symbol ;          
  G4double density;  
  G4int nel; 
  G4int ncomponents; 
  G4double fractionmass;

  G4NistManager* manager = G4NistManager::Instance();
  //
  // define Elements
  //
  G4Element* elH  = manager->FindOrBuildElement(1);
  G4Element* elC  = manager->FindOrBuildElement(6);
  G4Element* elO  = manager->FindOrBuildElement(8);
  G4Element* elF  = manager->FindOrBuildElement(9);
  G4Element* elNe = manager->FindOrBuildElement(10);
  G4Element* elXe = manager->FindOrBuildElement(54);
  //
  // simple gases at STP conditions 
  //
  G4Material* Argon = manager->FindOrBuildMaterial("G4_Ar");
  G4Material* Kr = manager->FindOrBuildMaterial("G4_Kr");
  G4Material* Xe     = manager->FindOrBuildMaterial("G4_Xe");
  // 
  // gases at STP conditions
  //
  G4Material* CarbonDioxide = 
    manager->FindOrBuildMaterial("G4_CARBON_DIOXIDE");
  G4Material* Mylar  = manager->FindOrBuildMaterial("G4_MYLAR");
  G4Material* Methane= manager->FindOrBuildMaterial("G4_METHANE");
  G4Material* Propane= manager->FindOrBuildMaterial("G4_PROPANE");
  G4Material* empty  = manager->FindOrBuildMaterial("G4_Galactic");

 G4double a;  // mass of a mole;
  G4double z;  // z=mean number of protons;  
  //G4double density; 
  G4Material* Awake10minus7 = new G4Material("AwakegasRb10minus7", z=37, a = 85.46*g/mole, density = 0.9937e-7*g/cm3);
  G4Material* Awake10minus6 = new G4Material("AwakegasRb10minus6", z=37, a = 85.46*g/mole, density = 0.9937e-6*g/cm3);
  G4Material* Awake10minus5 = new G4Material("AwakegasRb10minus5", z=37, a = 85.46*g/mole, density = 0.9937e-5*g/cm3);
  G4Material* Awake10minus4 = new G4Material("AwakegasRb10minus4", z=37, a = 85.46*g/mole, density = 0.9937e-4*g/cm3);

  
  
  
  //fGasMat = Argon;
  fGasMat = Awake10minus7;
  fWindowMat = Mylar;
  fWorldMaterial = empty; 

  G4cout << *(G4Material::GetMaterialTable()) << G4endl;

}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
  
G4VPhysicalVolume* DetectorConstruction::Construct()
{
  G4double contThick = fWindowThick*2 + fGasThickness;
  G4double contR     = fWindowThick*2 + fGasRadius;

  G4double worldSizeZ = contThick*1.2;
  G4double worldSizeR = contR*1.2;

  TestParameters::GetPointer()->SetPositionZ(-0.55*contThick);

  // Printout parameters
  G4cout << "\n The  WORLD   is made of " 
         << worldSizeZ/mm << "mm of " << fWorldMaterial->GetName() ;
  G4cout << ", the transverse size (R) of the world is " << worldSizeR/mm 
         << " mm. " << G4endl;
  G4cout << " The CONTAINER is made of " 
         << fWindowThick/mm << "mm of " << fWindowMat->GetName() << G4endl;
  G4cout << " The TARGET is made of " 
         << fGasThickness/mm << "mm of " << fGasMat->GetName() ;
  G4cout << ", the transverse size (R) is " << fGasRadius/mm << " mm. " 
         << G4endl;
  G4cout << G4endl;
      
  // World
  fSolidWorld = 
    new G4Tubs("World",0.,worldSizeR,worldSizeZ/2.,0.,CLHEP::twopi);
                   
  fLogicWorld = new G4LogicalVolume(fSolidWorld, fWorldMaterial, "World");
                                   
  fPhysWorld = new G4PVPlacement(0,      
                                   G4ThreeVector(0.,0.,0.),     
                                 "World", 
                                 fLogicWorld,
                                 0,      
                                 false,  
                                 0);     

  // Window
  fSolidContainer = new G4Tubs("Absorber",                
                               0.,contR,contThick/2.,0.,CLHEP::twopi); 

  fLogicContainer = new G4LogicalVolume(fSolidContainer, fWindowMat, "Window"); 

  G4PVPlacement* PhysWind = new G4PVPlacement(0, G4ThreeVector(0.,0.,0.),
                                              "Window",  fLogicContainer,
                                              fPhysWorld, false, 0);
                                        
  // Detector volume
  fSolidDetector = new G4Tubs("Gas", 0., fGasRadius, fGasThickness/2.,
                              0., CLHEP::twopi); 

  fLogicDetector = new G4LogicalVolume(fSolidDetector, fGasMat, "Gas"); 

  new G4PVPlacement(0, G4ThreeVector(0.,0.,0.), "Gas", fLogicDetector, 
                    PhysWind, false, 0);
//////////////////////
//max step size - http://geant4.web.cern.ch/geant4/UserDocumentation/Doxygen/examples_doc/html_ParN02/html/ExN02DetectorConstruction_8cc_source.html
 G4double maxStep = 1.*um;
   stepLimit = new G4UserLimits(maxStep);
     fLogicDetector->SetUserLimits(stepLimit);
fLogicContainer->SetUserLimits(stepLimit);
fLogicWorld->SetUserLimits(stepLimit);
/////////////////////////////////////////////

 G4int nofLayers = 15;

 G4VSolid* layerS 
    = new G4Tubs("Layer",0.,           // its name
                 fGasRadius, fGasThickness/(nofLayers*2),0.,CLHEP::twopi); // its size
                         
  //G4LogicalVolume* layerLV
  layerLV
    = new G4LogicalVolume(
                 layerS,           // its solid
                 fGasMat,  // its material
                 "Layer");         // its name

  new G4PVReplica(
                 "Layer",          // its name
                 layerLV,          // its logical volume
                 fLogicDetector,          // its mother
                 kZAxis,           // axis of replication
                 nofLayers,        // number of replica
                 fGasThickness/nofLayers);  // witdth of replica

///////////////////////////////////////////////

  // defined gas detector region
  fRegGasDet = new G4Region("GasDetector");
  fRegGasDet->SetProductionCuts(fGasDetectorCuts);
  fRegGasDet->AddRootLogicalVolume(fLogicDetector);
  //fRegGasDet->AddRootLogicalVolume(layerLV);


  // visualisation
  fLogicWorld->SetVisAttributes(G4VisAttributes::Invisible);
  G4VisAttributes* color1 = new G4VisAttributes(G4Colour(0.3, 0.3, 0.3));
  fLogicContainer->SetVisAttributes(color1);
  G4VisAttributes* color2 = new G4VisAttributes(G4Colour(0.0, 0.3, 0.7));
  fLogicDetector->SetVisAttributes(color2);

  G4VisAttributes* color3 = new G4VisAttributes(G4Colour(0.3, 0.7, 0.0));
  //layerLV->SetVisAttributes(color3);


  if(0.0 == fGasMat->GetIonisation()->GetMeanEnergyPerIonPair()) {
    SetPairEnergy(26.3*eV);
  }
  return fPhysWorld;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::ConstructSDandField()
{  
  //commented out 26.01
  //SetSensitiveDetector(fLogicDetector, new TargetSD("GasSD")); 
  //gabriel added 26.01
  SetSensitiveDetector(layerLV, new TargetSD("GasSD")); 

}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetGasMaterial(const G4String& name)
{
  // get the pointer to the existing material
  G4Material* mat = G4Material::GetMaterial(name, false);

  // create the material by its name
  if(!mat) { mat = G4NistManager::Instance()->FindOrBuildMaterial(name); }

  if (mat && mat != fGasMat) {
    G4cout << "### New target material: " << mat->GetName() << G4endl;
    fGasMat = mat;
    if(fLogicDetector) { 
      fLogicDetector->SetMaterial(mat); 
      G4RunManager::GetRunManager()->PhysicsHasBeenModified();
    }
  }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetContainerMaterial(const G4String& name)
{
  // get the pointer to the existing material
  G4Material* mat = G4Material::GetMaterial(name, false);

  // create the material by its name
  if(!mat) { mat = G4NistManager::Instance()->FindOrBuildMaterial(name); }

  if (mat && mat != fWindowMat) {
    G4cout << "### New material for container: " << mat->GetName() << G4endl;
    fWindowMat = mat;
    if(fLogicContainer) { 
      fLogicContainer->SetMaterial(mat); 
      G4RunManager::GetRunManager()->PhysicsHasBeenModified();
    }
  }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetWorldMaterial(const G4String& name)
{
  // get the pointer to the existing material
  G4Material* mat = G4Material::GetMaterial(name, false);

  // create the material by its name
  if(!mat) { mat = G4NistManager::Instance()->FindOrBuildMaterial(name); }

  if (mat && mat != fWorldMaterial) {
    G4cout << "### New World material: " << mat->GetName() << G4endl;
    fWorldMaterial = mat;
    if(fLogicWorld) { 
      fLogicWorld->SetMaterial(mat); 
      G4RunManager::GetRunManager()->PhysicsHasBeenModified();
    }
  }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetGasThickness(G4double val)
{
  fGasThickness = val;
  if(fPhysWorld) { ChangeGeometry(); }
}  

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetGasRadius(G4double val)
{
  fGasRadius = val;
  if(fPhysWorld) { ChangeGeometry(); }
}  

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetContainerThickness(G4double val)
{
  fWindowThick = val;
  if(fPhysWorld) { ChangeGeometry(); }
}  

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::SetPairEnergy(G4double val)
{
  if(val > 0.0) {
    fGasMat->GetIonisation()->SetMeanEnergyPerIonPair(val);
  }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void DetectorConstruction::ChangeGeometry()
{
  G4double contThick = fWindowThick*2 + fGasThickness;
  G4double contR     = fWindowThick*2 + fGasRadius;

  G4double worldSizeZ = contThick*1.2;
  G4double worldSizeR = contR*1.2;

  TestParameters::GetPointer()->SetPositionZ(-0.55*contThick);

  fSolidWorld->SetOuterRadius(worldSizeR);
  fSolidWorld->SetZHalfLength(worldSizeZ*0.5);

  fSolidContainer->SetOuterRadius(contR);
  fSolidContainer->SetZHalfLength(contThick*0.5);

  fSolidDetector->SetOuterRadius(fGasRadius);
  fSolidDetector->SetZHalfLength(fGasThickness*0.5);

}