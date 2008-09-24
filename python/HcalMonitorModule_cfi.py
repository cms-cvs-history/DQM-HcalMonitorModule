# The following comments couldn't be translated into the new config version:

# of sigma above threshold for a cell to be considered hot
# orig vale was 0.02
# HotCell Tags for individual subdetectors
# If these aren't specified, then the global 
# values are used
#untracked bool HBdebug = false
#untracked bool HEdebug = false
#untracked bool HOdebug = false
#untracked bool HFdebug = false
# Re-tuned threshold based on CRUZET1 run 43636 
# First threshold is used when looking for hot cells 

import FWCore.ParameterSet.Config as cms

hcalMonitor = cms.EDFilter("HcalMonitorModule",
                           PedestalsPerChannel = cms.untracked.bool(True),
                           DumpThreshold = cms.untracked.double(500.0),
                           thresholds = cms.untracked.vdouble(15.0, 5.0, 2.0, 1.5, 1.0),
                           coolcellfrac = cms.untracked.double(0.5),
                           NADA_maxeta = cms.untracked.int32(1),
                           hoRecHitLabel = cms.InputTag("horeco"),
                           PedestalMonitor = cms.untracked.bool(True),
                           MakeHotCellDiagnosticPlots = cms.untracked.bool(False),
                           DigiMonitor = cms.untracked.bool(True),
                           HotCell_checkNADA = cms.untracked.bool(True),
                           digiLabel = cms.InputTag("hcalDigis"),
                           hfRecHitLabel = cms.InputTag("hfreco"),
                           zdcRecHitLabel = cms.InputTag("zdcreco"),                           
                           hcalLaserLabel = cms.InputTag("hcalLaserReco"),                       
                           DumpPhiLow = cms.untracked.int32(10),
                           DigiOccThresh = cms.untracked.int32(0),
                           RecHitsPerChannel = cms.untracked.bool(False),
                           HE_NADA_Ecell_cut = cms.untracked.double(0.0),
                           HF_NADA_Ecube_frac = cms.untracked.double(0.5714),
                           HB_NADA_Ecell_frac = cms.untracked.double(0.0),
                           HF_NADA_Ecand_cut2 = cms.untracked.double(20.0),
                           HF_NADA_Ecand_cut0 = cms.untracked.double(1.5),
                           HF_NADA_Ecand_cut1 = cms.untracked.double(1.5),
                           diagnosticPrescaleLS = cms.untracked.int32(-1),
                           MakeDigiDiagnosticPlots = cms.untracked.bool(False),
                           CaloTowerMonitor = cms.untracked.bool(False),
                           BeamMonitor = cms.untracked.bool(True),                                        ExpertMonitor = cms.untracked.bool(False),
                           NADA_Ecube_frac = cms.untracked.double(0.3),
                           NADA_maxphi = cms.untracked.int32(1),
                           debug = cms.untracked.bool(False),
                           RecHitOccThresh = cms.untracked.double(2.0),
                           NADA_Ecand_cut0 = cms.untracked.double(1.5),
                           NADA_Ecand_cut1 = cms.untracked.double(2.5),
                           NADA_Ecand_cut2 = cms.untracked.double(500.0),
                           MonitorDaemon = cms.untracked.bool(True),
                           HE_NADA_Ecand_cut1 = cms.untracked.double(2.5),
                           RecHitMonitor = cms.untracked.bool(True),
                           caloTowerLabel = cms.InputTag("towerMaker"),
                           HE_NADA_Ecand_cut2 = cms.untracked.double(10.0),
                           HF_NADA_Ecell_cut = cms.untracked.double(0.0),
                           MakeDiagnosticPlots = cms.untracked.bool(True),
                           NADA_Ecell_frac = cms.untracked.double(0.02),
                           HO_NADA_Ecube_cut = cms.untracked.double(0.1),
                           HF_NADA_Ecell_frac = cms.untracked.double(0.0),
                           HB_NADA_Ecell_cut = cms.untracked.double(0.0),
                           MTCCMonitor = cms.untracked.bool(False),
                           HcalAnalysis = cms.untracked.bool(False),
                           DumpEtaHigh = cms.untracked.int32(10),
                           MaxPhi = cms.untracked.double(73.5),
                           DigisPerChannel = cms.untracked.bool(False),
                           HEthresholds = cms.untracked.vdouble(3.0, 2.0, 1.0, 5.0, 10.0),
                           LED_ADC_Thresh = cms.untracked.double(-1000.0),
                           diagnosticPrescaleTime = cms.untracked.int32(-1),
                           LEDPerChannel = cms.untracked.bool(True),
                           MaxEta = cms.untracked.double(42.5),
                           NADA_NegCand_cut = cms.untracked.double(-1.5),
                           HE_NADA_Ecand_cut0 = cms.untracked.double(1.5),
                           NADA_maxdepth = cms.untracked.int32(0),
                           hbheRecHitLabel = cms.InputTag("hbhereco"),
                           HotCellDigiSigma = cms.untracked.double(5.0),
                           DataFormatMonitor = cms.untracked.bool(True),
                           HFthresholds = cms.untracked.vdouble(9.0, 2.0, 4.0, 6.0, 10.0),
                           HotCell_checkThreshold = cms.untracked.bool(True),
                           minADCcount = cms.untracked.double(0.0),
                           PedestalsInFC = cms.untracked.bool(False),
                           HO_NADA_Ecell_frac = cms.untracked.double(0.0),
                           HE_NADA_Ecell_frac = cms.untracked.double(0.0),
                           showTiming = cms.untracked.bool(False),
                           HB_NADA_Ecube_frac = cms.untracked.double(0.333),
                           HB_NADA_Ecand_cut2 = cms.untracked.double(10.0),
                           HB_NADA_Ecand_cut0 = cms.untracked.double(1.5),
                           HB_NADA_Ecand_cut1 = cms.untracked.double(2.25),
                           HF_NADA_Ecube_cut = cms.untracked.double(0.1),
                           HOthresholds = cms.untracked.vdouble(2.0, 3.0, 1.0, 5.0, 10.0),
                           ped_Nsigma = cms.untracked.double(-3.1),
                           HotCells = cms.untracked.vstring(),
                           DeadCellMonitor = cms.untracked.bool(True),
                           HO_NADA_Ecand_cut2 = cms.untracked.double(10.0),
                           HO_NADA_Ecand_cut1 = cms.untracked.double(2.5),
                           HO_NADA_Ecand_cut0 = cms.untracked.double(1.5),
                           NADA_Ecell_cut = cms.untracked.double(0.1),
                           diagnosticPrescaleEvt = cms.untracked.int32(-1),
                           HE_NADA_Ecube_frac = cms.untracked.double(0.222),
                           DumpPhiHigh = cms.untracked.int32(10),
                           HB_NADA_Ecube_cut = cms.untracked.double(0.1),
                           DeadCell_checkAbovePed = cms.untracked.bool(True),
                           gtLabel = cms.InputTag("l1GtUnpack"),
                           HO_NADA_Ecell_cut = cms.untracked.double(0.0),
                           DumpEtaLow = cms.untracked.int32(0),
                           HotCell_checkAbovePed = cms.untracked.bool(True),
                           TrigPrimMonitor = cms.untracked.bool(True),
                           MinPhi = cms.untracked.double(-0.5),
                           MakeDeadCellDiagnosticPlots = cms.untracked.bool(False),
                           HotCellMonitor = cms.untracked.bool(True),
                           deadcellmindiff = cms.untracked.double(1.0),
                           checkNevents = cms.untracked.int32(250),
                           HBcheckNevents = cms.untracked.int32(250),
                           HEcheckNevents = cms.untracked.int32(250),
                           HOcheckNevents = cms.untracked.int32(1000),
                           HFcheckNevents = cms.untracked.int32(250),
                           
                           diagnosticPrescaleUpdate = cms.untracked.int32(-1),
                           HE_NADA_Ecube_cut = cms.untracked.double(0.1),
                           HO_NADA_Ecube_frac = cms.untracked.double(0.2),
                           checkHF = cms.untracked.bool(True),
                           checkHE = cms.untracked.bool(True),
                           checkHB = cms.untracked.bool(True),
                           checkHO = cms.untracked.bool(True),
                           MTCCOccThresh = cms.untracked.double(10.0),
                           NADA_Ecube_cut = cms.untracked.double(0.5),
                           HBthresholds = cms.untracked.vdouble(3.0, 2.0, 1.0, 5.0, 10.0),
                           LEDMonitor = cms.untracked.bool(True),
                           MinEta = cms.untracked.double(-42.5),
                           deadcellfloor = cms.untracked.double(-10.0),
                           dfPrtLvl = cms.untracked.int32(0)
                           )


