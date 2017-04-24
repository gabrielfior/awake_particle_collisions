//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
/// \file electromagnetic/TestEm8/src/TargetSD.cc
/// \brief Implementation of the TargetSD class
//
// $Id: TargetSD.cc 86976 2014-11-21 12:07:00Z gcosmo $
//
/////////////////////////////////////////////////////////////////////////
//
// TestEm8: Gaseous detector
//
// Created: 31.08.2010 V.Ivanchenko
//
// Modified:
//
////////////////////////////////////////////////////////////////////////
// 

#include "TargetSD.hh"
#include "Run.hh"
#include "globals.hh"
#include "G4HCofThisEvent.hh"
#include "G4TouchableHistory.hh"
#include "G4Step.hh"
#include "G4RunManager.hh"

#include "G4VProcess.hh"
#include "G4Track.hh"
#include "G4ParticleDefinition.hh"
#include "G4VPhysicalVolume.hh"
#include "G4SystemOfUnits.hh"  
#include "G4ThreeVector.hh"
#include "G4ProcessType.hh"

#include "G4SteppingManager.hh"


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

TargetSD::TargetSD(const G4String& name)
  : G4VSensitiveDetector(name), fRun(0)
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

TargetSD::~TargetSD()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void TargetSD::Initialize(G4HCofThisEvent*)
{
  fRun = (Run*)G4RunManager::GetRunManager()->GetNonConstCurrentRun();  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

G4bool TargetSD::ProcessHits(G4Step* aStep, G4TouchableHistory*)
{

G4int trackId = aStep->GetTrack()->GetTrackID();
  G4int parentId = aStep->GetTrack()->GetParentID();
  G4String volumeName = aStep->GetTrack()->GetTouchable()->GetVolume()->GetName();
  G4String particleName = aStep->GetTrack()->GetDefinition()->GetParticleName();
 G4int stepNumber =  aStep->GetTrack()->GetCurrentStepNumber();

G4ThreeVector prePoint  = aStep->GetPreStepPoint() ->GetPosition();
 G4ThreeVector postPoint = aStep->GetPostStepPoint()->GetPosition();
 G4ThreeVector point = prePoint + G4UniformRand()*(postPoint - prePoint);
 G4double r = point.mag();
 
  G4double posX = point.x();
  G4double posY = point.y();
  G4double posZ = point.z();

 G4double perp1 = point.perp();
   G4double stepLength2 = aStep->GetStepLength();
  G4double kineeticEnergyDiff = aStep->GetPostStepPoint()->GetKineticEnergy() - aStep->GetPreStepPoint()->GetKineticEnergy();  

  G4String processName = aStep->GetPostStepPoint()->GetProcessDefinedStep()->GetProcessName();
  //G4String processName = aStep->GetTrack()->GetCreatorProcess ()->GetProcessName();
  G4double kineticEnergyPostStep = aStep->GetPostStepPoint()->GetKineticEnergy();

  G4double edepStep = aStep->GetTotalEnergyDeposit();

//momentum and momentum-dir
G4ThreeVector prePointMomentum = aStep->GetPreStepPoint() ->GetMomentum();
G4ThreeVector postPointMomentum = aStep->GetPostStepPoint() ->GetMomentum();

G4double momprex = prePointMomentum.x();
G4double momprey = prePointMomentum.y();
G4double momprez = prePointMomentum.z();

G4double mompostx = postPointMomentum.x();
G4double momposty = postPointMomentum.y();
G4double mompostz = postPointMomentum.z();

G4double eDeposit  = aStep->GetTotalEnergyDeposit();

//////////////////////////////////////
//add to csv

  G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
 analysisManager->FillNtupleIColumn(0, trackId);
 analysisManager->FillNtupleIColumn(1, parentId);
 analysisManager->FillNtupleSColumn(2, volumeName);
 analysisManager->FillNtupleSColumn(3, particleName); 
 analysisManager->FillNtupleIColumn(4, stepNumber); 
 analysisManager->FillNtupleDColumn(5, posX/mm); 
 analysisManager->FillNtupleDColumn(6, posY/mm); 
 analysisManager->FillNtupleDColumn(7, posZ/mm); 
 analysisManager->FillNtupleDColumn(8, perp1/mm);
 analysisManager->FillNtupleDColumn(9, kineeticEnergyDiff/eV); 
 analysisManager->FillNtupleDColumn(10, edepStep/eV); 
 analysisManager->FillNtupleDColumn(11, kineticEnergyPostStep/eV);  
 analysisManager->FillNtupleSColumn(12, processName);

 analysisManager->FillNtupleDColumn(13, momprex/eV);
 analysisManager->FillNtupleDColumn(14, momprey/eV);
 analysisManager->FillNtupleDColumn(15, momprez/eV);
 analysisManager->FillNtupleDColumn(16, mompostx/eV);
 analysisManager->FillNtupleDColumn(17, momposty/eV);
 analysisManager->FillNtupleDColumn(18, mompostz/eV);
 analysisManager->FillNtupleDColumn(19, stepLength2/mm);
 analysisManager->FillNtupleDColumn(20, eDeposit/eV);

 
  //G4cout << "end step" << G4endl;

 analysisManager->AddNtupleRow();  

 ///////////////////////////////////////////
  G4double edep = aStep->GetTotalEnergyDeposit();
  fRun->AddEnergy(edep, aStep); 
  return true;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void TargetSD::EndOfEvent(G4HCofThisEvent*)
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void TargetSD::clear()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void TargetSD::PrintAll()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

