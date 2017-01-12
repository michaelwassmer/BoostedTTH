import FWCore.ParameterSet.Config as cms
Inputs_tth_sl= cms.PSet(
    puInfo=cms.InputTag("slimmedAddPileupInfo"),
    rho=cms.InputTag("fixedGridRhoFastjetAll"),
    hcalNoise=cms.InputTag("hcalnoise"),
    triggerBits=cms.InputTag("TriggerResults::HLT"),
    triggerObjects=cms.InputTag("selectedPatTrigger"),
    triggerPrescales=cms.InputTag("patTrigger"),
    filterBits=cms.InputTag("TriggerResults::PAT"),
    additionalFilters=cms.VInputTag(["BadChargedCandidateFilter","BadPFMuonFilter"]),
    beamSpot=cms.InputTag("offlineBeamSpot"),
    primaryVertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
    selectedMuons=cms.InputTag("SelectedMuonProducer:selectedMuons"),
    selectedMuonsDL=cms.InputTag("SelectedMuonProducer:selectedMuonsDL"),
    selectedMuonsLoose=cms.InputTag("SelectedMuonProducer:selectedMuonsLoose"),
    selectedElectrons=cms.InputTag("SelectedElectronProducer:selectedElectrons"),
    selectedElectronsDL=cms.InputTag("SelectedElectronProducer:selectedElectronsDL"),
    selectedElectronsLoose=cms.InputTag("SelectedElectronProducer:selectedElectronsLoose"),
    rawJets=cms.InputTag("SelectedJetProducer:rawJets"),
    selectedJets=cms.VInputTag("SelectedJetProducer:selectedJets"),
    selectedJetsLoose=cms.VInputTag("SelectedJetProducer:selectedJetsLoose"),
    selectedJetsDL=cms.VInputTag("SelectedJetProducer:selectedJetsDL"),
    selectedJetsLooseDL=cms.VInputTag("SelectedJetProducer:selectedJetsLooseDL"),
    correctedMETs=cms.VInputTag("slimmedMETs"),
    boostedJets=cms.InputTag("BoostedJetMatcher:boostedjets:p"),
    genInfo=cms.InputTag("generator"),
    lheInfo=cms.InputTag("externalLHEProducer"),
    genParticles=cms.InputTag("prunedGenParticles"),
    genJets=cms.InputTag("slimmedGenJets"),
    conversionCollection= cms.InputTag("reducedEgamma:reducedConversions"),
    electronMVAvalues = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
    electronMVAcategories = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
)
