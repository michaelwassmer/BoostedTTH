#include "BoostedTTH/BoostedAnalyzer/interface/DiLeptonMassSelection.hpp"

using namespace std;

DiLeptonMassSelection::DiLeptonMassSelection(float minMass_,float maxMass_,bool invertCut_):minMass(minMass_),maxMass(maxMass_),invertCut(invertCut_)
{}

DiLeptonMassSelection::~DiLeptonMassSelection (){}

void DiLeptonMassSelection::InitCutflow(Cutflow& cutflow){
    selectionName="Same Flavor Dilepton mass ";
    if(invertCut) selectionName+="not ";
    selectionName+="between ";
    selectionName+=std::to_string(minMass);
    selectionName+=" and ";
    selectionName+=std::to_string(maxMass);
    cutflow.AddStep(selectionName);
    initialized=true;
}

bool DiLeptonMassSelection::IsSelected(const InputCollections& input,Cutflow& cutflow){
    if(!initialized) cerr << "DiLeptonMassSelection not initialized" << endl;

    if((input.selectedMuonsDL.size()+input.selectedElectronsDL.size())<2) {
      return false;
    }

    float mumu_mass=-1;
    float elel_mass=-1;
    if(input.selectedElectronsDL.size()>=2){
      elel_mass=(input.selectedElectronsDL[0].p4()+input.selectedElectronsDL[1].p4()).M();
    }
    if(input.selectedMuonsDL.size()>=2){
      mumu_mass=(input.selectedMuonsDL[0].p4()+input.selectedMuonsDL[1].p4()).M();
    }
    if(input.selectedMuonsDL.size()<2 && input.selectedElectronsDL.size()<2) {
      cutflow.EventSurvivedStep(selectionName,input.weights.at("Weight"));
      return true;
    }
    
    if(!invertCut){
      // both dilepton masses are outside of the window
      if( (elel_mass<minMass||elel_mass>maxMass) && (mumu_mass<minMass||mumu_mass>maxMass)){
	return false;
      }
    }
    if(invertCut){
      // one dilepton mass is inside of the window
      if( (elel_mass>minMass&&elel_mass<maxMass) || (mumu_mass>minMass&&mumu_mass<maxMass)){
	return false;
      }
    }

    cutflow.EventSurvivedStep(selectionName,input.weights.at("Weight"));
    
    return true;
}