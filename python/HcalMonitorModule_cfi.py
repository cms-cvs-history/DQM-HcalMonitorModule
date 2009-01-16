import FWCore.ParameterSet.Config as cms
from copy import deepcopy

hcalMonitor = cms.EDFilter("HcalMonitorModule",

                           # GLOBAL VARIABLES
                           debug = cms.untracked.int32(0), # make debug an int so that different values can trigger different levels of messaging

                           # eta runs from -43->+43  (-41 -> +41 for HCAL, plus ZDC, which we put at |eta|=43.
                           # add one empty bin beyond that for histogramming prettiness 
                           MaxEta = cms.untracked.double(44.5),
                           MinEta = cms.untracked.double(-44.5),
                           # likewise, phi runs from 1-72.  Add some buffering bins around that region 
                           MaxPhi = cms.untracked.double(73.5),
                           MinPhi = cms.untracked.double(-0.5),

                           # Determine whether or not to check individual subdetectors
                           checkHF = cms.untracked.bool(True),
                           checkHE = cms.untracked.bool(True),
                           checkHB = cms.untracked.bool(True),
                           checkHO = cms.untracked.bool(True),

                           MonitorDaemon = cms.untracked.bool(True),
                           HcalAnalysis = cms.untracked.bool(False),
                           HotCells = cms.untracked.vstring(),
                           checkNevents = cms.untracked.int32(250),
                           
                           #minimum Error Rate that will cause problem histograms to be filled.  Should normally be 0, or close to it?
                           minErrorFlag = cms.untracked.double(0.05), 

                           # Turn on/off timing diagnostic info
                            diagnosticPrescaleLS = cms.untracked.int32(-1),
                           diagnosticPrescaleEvt = cms.untracked.int32(-1),
                           diagnosticPrescaleTime = cms.untracked.int32(-1),
                           diagnosticPrescaleUpdate = cms.untracked.int32(-1),

                           showTiming          = cms.untracked.bool(False), # shows time taken by each process
                           dump2database       = cms.untracked.bool(False), # dumps channel status to text file
                           # Make expert-level diagnostic plots (enabling this may drastically slow code!)
                           makeDiagnosticPlots = cms.untracked.bool(False),

                           # Specify whether or not to fill the unphysical iphi bins
                           fillUnphysicalIphi = cms.untracked.bool(True),
                           
                           # Specify Pedestal Units
                           pedestalsInFC                               = cms.untracked.bool(False),
                           # Specify Digis
                           digiLabel = cms.InputTag("hcalDigis"),
                           #Specify RecHits
                           hbheRecHitLabel = cms.InputTag("hbhereco"),
                           hoRecHitLabel = cms.InputTag("horeco"),
                           hfRecHitLabel = cms.InputTag("hfreco"),
                           zdcRecHitLabel = cms.InputTag("zdcreco"),                           
                           hcalLaserLabel = cms.InputTag("hcalLaserReco"),                       

                           # PEDESTAL MONITOR
                           PedestalMonitor                              = cms.untracked.bool(True),
                           # Add in a make diagnostic plot variable here somewhere?  Peds don't currently have diagnostic plots
                           PedestalMonitor_pedestalsPerChannel          = cms.untracked.bool(True), # not used
                           PedestalMonitor_pedestalsInFC                = cms.untracked.bool(False),
                           PedestalMonitor_nominalPedMeanInADC          = cms.untracked.double(3.),
                           PedestalMonitor_nominalPedWidthInADC         = cms.untracked.double(1.),
                           PedestalMonitor_maxPedMeanDiffADC            = cms.untracked.double(1.),
                           PedestalMonitor_maxPedWidthDiffADC           = cms.untracked.double(1.),
                           PedestalMonitor_startingTimeSlice            = cms.untracked.int32(0),
                           PedestalMonitor_endingTimeSlice              = cms.untracked.int32(1),
                           PedestalMonitor_minErrorFlag                 = cms.untracked.double(0.05),
                           PedestalMonitor_checkNevents                 = cms.untracked.int32(500),
                           PedestalMonitor_minEntriesPerPed = cms.untracked.uint32(10),

                           # DEAD CELL MONITOR
                           DeadCellMonitor                              = cms.untracked.bool(True),
                           DeadCellMonitor_pedestalsInFC                = cms.untracked.bool(False),
                           DeadCellMonitor_makeDiagnosticPlots          = cms.untracked.bool(False),
                           DeadCellMonitor_test_occupancy               = cms.untracked.bool(True),
                           DeadCellMonitor_test_rechit_occupancy        = cms.untracked.bool(True),
                           DeadCellMonitor_test_neighbor                = cms.untracked.bool(False), # doesn't give much useful info
                           DeadCellMonitor_test_pedestal                = cms.untracked.bool(True),
                           DeadCellMonitor_test_energy                  = cms.untracked.bool(True),
                           DeadCellMonitor_checkNevents                 = cms.untracked.int32(500),
                           DeadCellMonitor_checkNevents_occupancy       = cms.untracked.int32(500),
                           DeadCellMonitor_checkNevents_rechit_occupancy= cms.untracked.int32(500),
                           DeadCellMonitor_checkNevents_pedestal        = cms.untracked.int32(500),
                           DeadCellMonitor_checkNevents_neighbor        = cms.untracked.int32(500),
                           DeadCellMonitor_checkNevents_energy          = cms.untracked.int32(500),
                           #checking for cells consistently below (ped + Nsigma*width)
                           DeadCellMonitor_pedestal_Nsigma              = cms.untracked.double(0.),
                           DeadCellMonitor_pedestal_HB_Nsigma           = cms.untracked.double(0.),
                           DeadCellMonitor_pedestal_HE_Nsigma           = cms.untracked.double(0.),
                           DeadCellMonitor_pedestal_HO_Nsigma           = cms.untracked.double(0.),
                           DeadCellMonitor_pedestal_HF_Nsigma           = cms.untracked.double(0.),
                           DeadCellMonitor_pedestal_ZDC_Nsigma          = cms.untracked.double(0.),
                           # Checking for cells consistently below energy threshold
                           DeadCellMonitor_energyThreshold              = cms.untracked.double(-1.),
                           DeadCellMonitor_HB_energyThreshold           = cms.untracked.double(-1.),
                           DeadCellMonitor_HE_energyThreshold           = cms.untracked.double(-1.), 
                           DeadCellMonitor_HO_energyThreshold           = cms.untracked.double(-1.),
                           DeadCellMonitor_HF_energyThreshold           = cms.untracked.double(-1.),
                           DeadCellMonitor_ZDC_energyThreshold          = cms.untracked.double(-999.), # not yet implemented
                           # Check for cells below their neighbors
                           DeadCellMonitor_neighbor_deltaIeta           = cms.untracked.int32(1),
                           DeadCellMonitor_neighbor_deltaIphi           = cms.untracked.int32(1),
                           DeadCellMonitor_neighbor_deltaDepth          = cms.untracked.int32(4),
                           DeadCellMonitor_neighbor_maxCellEnergy       = cms.untracked.double(3.),
                           DeadCellMonitor_neighbor_minNeighborEnergy   = cms.untracked.double(1.),
                           DeadCellMonitor_neighbor_minGoodNeighborFrac = cms.untracked.double(.7),
                           DeadCellMonitor_neighbor_maxEnergyFrac       = cms.untracked.double(.2),
                           # HB neighbor flags
                           DeadCellMonitor_HB_neighbor_deltaIeta           = cms.untracked.int32(1),
                           DeadCellMonitor_HB_neighbor_deltaIphi           = cms.untracked.int32(1),
                           DeadCellMonitor_HB_neighbor_deltaDepth          = cms.untracked.int32(4),
                           DeadCellMonitor_HB_neighbor_maxCellEnergy       = cms.untracked.double(3.),
                           DeadCellMonitor_HB_neighbor_minNeighborEnergy   = cms.untracked.double(1.),
                           DeadCellMonitor_HB_neighbor_minGoodNeighborFrac = cms.untracked.double(.7),
                           DeadCellMonitor_HB_neighbor_maxEnergyFrac       = cms.untracked.double(.2),
                           # HE neighbor flags
                           DeadCellMonitor_HE_neighbor_deltaIeta           = cms.untracked.int32(1),
                           DeadCellMonitor_HE_neighbor_deltaIphi           = cms.untracked.int32(1),
                           DeadCellMonitor_HE_neighbor_deltaDepth          = cms.untracked.int32(4),
                           DeadCellMonitor_HE_neighbor_maxCellEnergy       = cms.untracked.double(3.),
                           DeadCellMonitor_HE_neighbor_minNeighborEnergy   = cms.untracked.double(1.),
                           DeadCellMonitor_HE_neighbor_minGoodNeighborFrac = cms.untracked.double(.7),
                           DeadCellMonitor_HE_neighbor_maxEnergyFrac       = cms.untracked.double(.2),
                           # HO neighbor flags
                           DeadCellMonitor_HO_neighbor_deltaIeta           = cms.untracked.int32(1),
                           DeadCellMonitor_HO_neighbor_deltaIphi           = cms.untracked.int32(1),
                           DeadCellMonitor_HO_neighbor_deltaDepth          = cms.untracked.int32(4),
                           DeadCellMonitor_HO_neighbor_maxCellEnergy       = cms.untracked.double(3.),
                           DeadCellMonitor_HO_neighbor_minNeighborEnergy   = cms.untracked.double(1.),
                           DeadCellMonitor_HO_neighbor_minGoodNeighborFrac = cms.untracked.double(.7),
                           DeadCellMonitor_HO_neighbor_maxEnergyFrac       = cms.untracked.double(.2),
                           # HF neighbor flags
                           DeadCellMonitor_HF_neighbor_deltaIeta           = cms.untracked.int32(1),
                           DeadCellMonitor_HF_neighbor_deltaIphi           = cms.untracked.int32(1),
                           DeadCellMonitor_HF_neighbor_deltaDepth          = cms.untracked.int32(4),
                           DeadCellMonitor_HF_neighbor_maxCellEnergy       = cms.untracked.double(3.),
                           DeadCellMonitor_HF_neighbor_minNeighborEnergy   = cms.untracked.double(1.),
                           DeadCellMonitor_HF_neighbor_minGoodNeighborFrac = cms.untracked.double(.7),
                           DeadCellMonitor_HF_neighbor_maxEnergyFrac       = cms.untracked.double(.2),

                           DeadCellMonitor_minErrorFlag                    = cms.untracked.double(0.05),
                           
                           # HOT CELL MONITOR
                           HotCellMonitor                              = cms.untracked.bool(True),
                           HotCellMonitor_pedestalsInFC                = cms.untracked.bool(False),
                           HotCellMonitor_makeDiagnosticPlots          = cms.untracked.bool(False),
                           HotCellMonitor_test_neighbor                = cms.untracked.bool(False),
                           HotCellMonitor_test_pedestal                = cms.untracked.bool(True),
                           HotCellMonitor_test_energy                  = cms.untracked.bool(True),
                           HotCellMonitor_test_persistent              = cms.untracked.bool(True),
                           HotCellMonitor_checkNevents                 = cms.untracked.int32(500),
                           HotCellMonitor_checkNevents_pedestal        = cms.untracked.int32(500),
                           HotCellMonitor_checkNevents_neighbor        = cms.untracked.int32(500),
                           HotCellMonitor_checkNevents_energy          = cms.untracked.int32(500),
                           HotCellMonitor_checkNevents_persistent      = cms.untracked.int32(500),
                           #checking for cells consistently above (ped + Nsigma*width)
                           HotCellMonitor_pedestal_Nsigma              = cms.untracked.double(3.),
                           HotCellMonitor_pedestal_HB_Nsigma           = cms.untracked.double(3.),
                           HotCellMonitor_pedestal_HE_Nsigma           = cms.untracked.double(3.),
                           HotCellMonitor_pedestal_HO_Nsigma           = cms.untracked.double(3.),
                           HotCellMonitor_pedestal_HF_Nsigma           = cms.untracked.double(3.),
                           HotCellMonitor_pedestal_ZDC_Nsigma          = cms.untracked.double(5.),
                           # Checking for cells above energy threshold at any time
                           HotCellMonitor_energyThreshold              = cms.untracked.double(5.),
                           HotCellMonitor_HB_energyThreshold           = cms.untracked.double(5.),
                           HotCellMonitor_HE_energyThreshold           = cms.untracked.double(5.), 
                           HotCellMonitor_HO_energyThreshold           = cms.untracked.double(5.),
                           HotCellMonitor_HF_energyThreshold           = cms.untracked.double(5.),
                           HotCellMonitor_ZDC_energyThreshold          = cms.untracked.double(999.), # not yet implemented
                           # Checking for cells consistently babove energy threshold
                           HotCellMonitor_persistentThreshold              = cms.untracked.double(3.),
                           HotCellMonitor_HB_persistentThreshold           = cms.untracked.double(3.),
                           HotCellMonitor_HE_persistentThreshold           = cms.untracked.double(3.), 
                           HotCellMonitor_HO_persistentThreshold           = cms.untracked.double(3.),
                           HotCellMonitor_HF_persistentThreshold           = cms.untracked.double(3.),
                           HotCellMonitor_ZDC_persistentThreshold          = cms.untracked.double(999.), # not yet implemented
                           # Check for cells above their neighbors
                           HotCellMonitor_neighbor_deltaIeta           = cms.untracked.int32(1),
                           HotCellMonitor_neighbor_deltaIphi           = cms.untracked.int32(1),
                           HotCellMonitor_neighbor_deltaDepth          = cms.untracked.int32(4),
                           HotCellMonitor_neighbor_minCellEnergy       = cms.untracked.double(0.),
                           HotCellMonitor_neighbor_minNeighborEnergy   = cms.untracked.double(0.),
                           HotCellMonitor_neighbor_maxEnergy           = cms.untracked.double(25),
                           HotCellMonitor_neighbor_HotEnergyFrac       = cms.untracked.double(.02),
                           # HB neighbor flags
                           HotCellMonitor_HB_neighbor_deltaIeta           = cms.untracked.int32(1),
                           HotCellMonitor_HB_neighbor_deltaIphi           = cms.untracked.int32(1),
                           HotCellMonitor_HB_neighbor_deltaDepth          = cms.untracked.int32(4),
                           HotCellMonitor_HB_neighbor_minCellEnergy       = cms.untracked.double(2.),
                           HotCellMonitor_HB_neighbor_minNeighborEnergy   = cms.untracked.double(0.),
                           HotCellMonitor_HB_neighbor_maxEnergy           = cms.untracked.double(25),
                           HotCellMonitor_HB_neighbor_HotEnergyFrac       = cms.untracked.double(.02),
                           # HE neighbor flags
                           HotCellMonitor_HE_neighbor_deltaIeta           = cms.untracked.int32(1),
                           HotCellMonitor_HE_neighbor_deltaIphi           = cms.untracked.int32(1),
                           HotCellMonitor_HE_neighbor_deltaDepth          = cms.untracked.int32(4),
                           HotCellMonitor_HE_neighbor_minCellEnergy       = cms.untracked.double(2.),
                           HotCellMonitor_HE_neighbor_minNeighborEnergy   = cms.untracked.double(0.),
                           HotCellMonitor_HE_neighbor_maxEnergy           = cms.untracked.double(25),
                           HotCellMonitor_HE_neighbor_HotEnergyFrac       = cms.untracked.double(.02),
                           # HO neighbor flags
                           HotCellMonitor_HO_neighbor_deltaIeta           = cms.untracked.int32(1),
                           HotCellMonitor_HO_neighbor_deltaIphi           = cms.untracked.int32(1),
                           HotCellMonitor_HO_neighbor_deltaDepth          = cms.untracked.int32(4),
                           HotCellMonitor_HO_neighbor_minCellEnergy       = cms.untracked.double(5.),
                           HotCellMonitor_HO_neighbor_minNeighborEnergy   = cms.untracked.double(0.),
                           HotCellMonitor_HO_neighbor_maxEnergy           = cms.untracked.double(25),
                           HotCellMonitor_HO_neighbor_HotEnergyFrac       = cms.untracked.double(.02),
                           # HF neighbor flags
                           HotCellMonitor_HF_neighbor_deltaIeta           = cms.untracked.int32(1),
                           HotCellMonitor_HF_neighbor_deltaIphi           = cms.untracked.int32(1),
                           HotCellMonitor_HF_neighbor_deltaDepth          = cms.untracked.int32(4),
                           HotCellMonitor_HF_neighbor_minCellEnergy       = cms.untracked.double(2.),
                           HotCellMonitor_HF_neighbor_minNeighborEnergy   = cms.untracked.double(0.),
                           HotCellMonitor_HF_neighbor_maxEnergy           = cms.untracked.double(25),
                           HotCellMonitor_HF_neighbor_HotEnergyFrac       = cms.untracked.double(.02),
                           
                           HotCellMonitor_minErrorFlag                    = cms.untracked.double(0.05),

                           # DIGI MONITOR
                           DigiMonitor                                    = cms.untracked.bool(True),
                           DigiMonitor_checkNevents                       = cms.untracked.int32(500),
                           DigiMonitor_problems_checkForMissingDigis      = cms.untracked.bool(False), # also checked in DeadCellMonitor, which may be the more appropriate place for the check
                           DigiMonitor_problems_checkCapID                = cms.untracked.bool(True),
                           DigiMonitor_problems_checkDigiSize             = cms.untracked.bool(True),
                           DigiMonitor_problems_checkADCsum               = cms.untracked.bool(True),
                           DigiMonitor_problems_checkDVerr                = cms.untracked.bool(True),
                           DigiMonitor_minDigiSize                        = cms.untracked.int32(10),
                           DigiMonitor_maxDigiSize                        = cms.untracked.int32(10),
                           # ADC counts must be above the threshold values below for appropriate histograms to be filled
                           DigiMonitor_shapeThresh                        = cms.untracked.int32(-1),
                           DigiMonitor_ADCsumThresh                       = cms.untracked.int32(-1),
                           DigMonitor_makeDiagnosticPlots                 = cms.untracked.bool(False), # doesn't do anything yet
                           DigiMonitor_DigisPerChannel                    = cms.untracked.bool(False), # not currently used

                           # RECHIT MONITOR
                           RecHitMonitor                                  = cms.untracked.bool(True),
                           RecHitMonitor_checkNevents                     = cms.untracked.int32(500),
                           RecHitMonitor_minErrorFlag                     = cms.untracked.double(0.),
                           RecHitMonitor_makeDiagnosticPlots              = cms.untracked.bool(False),
                           RecHitMonitor_energyThreshold                  = cms.untracked.double(2.),
                           RecHitMonitor_HB_energyThreshold               = cms.untracked.double(2.),
                           RecHitMonitor_HO_energyThreshold               = cms.untracked.double(2.),
                           RecHitMonitor_HE_energyThreshold               = cms.untracked.double(2.),
                           RecHitMonitor_HF_energyThreshold               = cms.untracked.double(2.),
                           RecHitMonitor_ZDC_energyThreshold              = cms.untracked.double(2.),
                           
                           # BEAM MONITOR
                           BeamMonitor                                    = cms.untracked.bool(True),
                           BeamMonitor_checkNevents                       = cms.untracked.int32(500),
                           BeamMonitor_minErrorFlag                       = cms.untracked.double(0.),
                           BeamMonitor_makeDiagnosticPlots                = cms.untracked.bool(False),

                           # DATA FORMAT MONITOR
                           DataFormatMonitor                              = cms.untracked.bool(True),
                           DataFormatMonitor_checkNevents                 = cms.untracked.int32(500),
                           dfPrtLvl                                       = cms.untracked.int32(0), # this seems similar to the debug int we have; deprecate this?

                           # DATA INTEGRITY TASK
                           DataIntegrityTask = cms.untracked.bool(False),

                           # TRIG PRIM MONITOR
                           TrigPrimMonitor = cms.untracked.bool(True),
                           TrigPrimMonitor_OccThresh                      = cms.untracked.double(1.),
                           TrigPrimMonitor_Threshold                      = cms.untracked.double(1.),
                           TrigPrimMonitor_TPdigiTS                       = cms.untracked.int32(1),
                           TrigPrimMonitor_ADCdigiTS                      = cms.untracked.int32(3),
                           TrigPrimMonitor_checkNevents                   = cms.untracked.int32(500),
                           TrigPrimMonitor_makeDiagnostics                = cms.untracked.bool(False),
                           gtLabel = cms.InputTag("l1GtUnpack"),
                           
                           # LED MONITOR
                           LEDMonitor = cms.untracked.bool(True),
                           LED_ADC_Thresh = cms.untracked.double(-1000.0),
                           LEDPerChannel = cms.untracked.bool(True),

                           # ------------- DEPRECATED/UNUSED MONITORS ----------------------- #
                           # EXPERT MONITOR (should generally be turned off)
                           ExpertMonitor = cms.untracked.bool(False),

                           # CALO TOWER MONITOR
                           CaloTowerMonitor = cms.untracked.bool(False),
                           caloTowerLabel = cms.InputTag("towerMaker"),

                           # MTCC MONITOR
                           MTCCMonitor = cms.untracked.bool(False),
                           MTCCOccThresh = cms.untracked.double(10.0),
                           DumpPhiLow = cms.untracked.int32(10),
                           DumpPhiHigh = cms.untracked.int32(10),
                           DumpEtaLow = cms.untracked.int32(0),
                           DumpEtaHigh = cms.untracked.int32(10),
                           DumpThreshold = cms.untracked.double(500.0),
                           # --------------------------------------------------------------- #
                           )


def setHcalTaskValues(process):
    # If you import this function directly, you can then set all the individual subtask values to the global settings
    # (This is useful if you've changed the global value, and you want it to propagate everywhere)

    # Set minimum value needed to put an entry into Problem histograms.  (values are between 0-1)

    # Insidious python-ness:  You need to make a copy of the process.minErrorFlag, etc. variables,
    # or future changes to PedestalMonitor_minErrorFlag will also change minErrorFlag!

    # set minimum error value
    minErrorFlag = deepcopy(process.minErrorFlag)
    process.BeamMonitor_minErrorFlag     = minErrorFlag
    process.DeadCellMonitor_minErrorFlag = minErrorFlag
    process.HotCellMonitor_minErrorFlag  = minErrorFlag
    process.PedestalMonitor_minErrorFlag = minErrorFlag
    process.RecHitMonitor_minErrorFlag   = minErrorFlag
        
    # create a minErrorFlag for DigiMonitor?  I think we want the DigiMonitor errors to appear whenever an error exists, even if it's at a low rate.

    # set checkNevents
    checkNevents = deepcopy(process.checkNevents)
    process.BeamMonitor_checkNevents                      = checkNevents
    process.DeadCellMonitor_checkNevents                  = checkNevents
    process.DeadCellMonitor_checkNevents_occupancy        = checkNevents
    process.DeadCellMonitor_checkNevents_rechit_occupancy = checkNevents
    process.DeadCellMonitor_checkNevents_pedestal         = checkNevents
    process.DeadCellMonitor_checkNevents_neighbor         = checkNevents
    process.DeadCellMonitor_checkNevents_energy           = checkNevents
    process.DigiMonitor_checkNevents                      = checkNevents
    process.HotCellMonitor_checkNevents                   = checkNevents
    process.HotCellMonitor_checkNevents_persistent        = checkNevents
    process.HotCellMonitor_checkNevents_pedestal          = checkNevents
    process.HotCellMonitor_checkNevents_neighbor          = checkNevents
    process.HotCellMonitor_checkNevents_energy            = checkNevents
    process.PedestalMonitor_checkNevents                  = checkNevents
    process.RecHitMonitor_checkNevents                    = checkNevents
    process.TrigPrimMonitor_checkNevents                  = checkNevents
    
    # set pedestalsInFC
    pedestalsInFC = deepcopy(process.pedestalsInFC)
    process.DeadCellMonitor_pedestalsInFC = pedestalsInFC
    process.HotCellMonitor_pedestalsInFC  = pedestalsInFC
    process.PedestalMonitor_pedestalsInFC = pedestalsInFC

    # set makeDiagnoticPlots
    makeDiagnosticPlots                         = deepcopy(process.makeDiagnosticPlots)
    process.BeamMonitor_makeDiagnosticPlots     = makeDiagnosticPlots
    process.DeadCellMonitor_makeDiagnosticPlots = makeDiagnosticPlots
    process.DigiMonitor_makeDiagnosticsPlots    = makeDiagnosticPlots
    process.HotCellMonitor_makeDiagnosticPlots  = makeDiagnosticPlots
    process.RecHitMonitor_makeDiagnosticPlots   = makeDiagnosticPlots
    process.TrigPrimMonitor_makeDiagnosticPlots = makeDiagnosticPlots
    return


def setHcalSubdetTaskValues(process):
    # Set HB/HE/HO/HF

    # Dead Cell Monitor
    dead_nsigma = deepcopy(process.DeadCellMonitor_pedestal_Nsigma)
    process.DeadCellMonitor_pedestal_HB_Nsigma           = dead_nsigma
    process.DeadCellMonitor_pedestal_HE_Nsigma           = dead_nsigma
    process.DeadCellMonitor_pedestal_HO_Nsigma           = dead_nsigma
    process.DeadCellMonitor_pedestal_HF_Nsigma           = dead_nsigma
    process.DeadCellMonitor_pedestal_ZDC_Nsigma          = dead_nsigmax

    dead_deltaIeta = deepcopy(process.DeadCellMonitor_neighbor_deltaIeta)
    process.DeadCellMonitor_HB_neighbor_deltaIeta           = dead_deltaIeta
    process.DeadCellMonitor_HE_neighbor_deltaIeta           = dead_deltaIeta
    process.DeadCellMonitor_HO_neighbor_deltaIeta           = dead_deltaIeta
    process.DeadCellMonitor_HF_neighbor_deltaIeta           = dead_deltaIeta
    process.DeadCellMonitor_ZDC_neighbor_deltaIeta          = dead_deltaIeta
    
    dead_deltaIphi = deepcopy(process.DeadCellMonitor_neighbor_deltaIphi)
    process.DeadCellMonitor_HB_neighbor_deltaIphi           = dead_deltaIphi
    process.DeadCellMonitor_HE_neighbor_deltaIphi           = dead_deltaIphi
    process.DeadCellMonitor_HO_neighbor_deltaIphi           = dead_deltaIphi
    process.DeadCellMonitor_HF_neighbor_deltaIphi           = dead_deltaIphi
    process.DeadCellMonitor_ZDC_neighbor_deltaIphi          = dead_deltaIphi

    dead_deltaDepth = deepcopy(process.DeadCellMonitor_neighbor_deltaDepth)
    process.DeadCellMonitor_HB_neighbor_deltaDepth           = dead_deltaDepth
    process.DeadCellMonitor_HE_neighbor_deltaDepth           = dead_deltaDepth
    process.DeadCellMonitor_HO_neighbor_deltaDepth           = dead_deltaDepth
    process.DeadCellMonitor_HF_neighbor_deltaDepth           = dead_deltaDepth
    process.DeadCellMonitor_ZDC_neighbor_deltaDepth          = dead_deltaDepth

    dead_maxCellEnergy = deepcopy(process.DeadCellMonitor_neighbor_maxCellEnergy)
    process.DeadCellMonitor_HB_neighbor_maxCellEnergy           = dead_maxCellEnergy
    process.DeadCellMonitor_HE_neighbor_maxCellEnergy           = dead_maxCellEnergy
    process.DeadCellMonitor_HO_neighbor_maxCellEnergy           = dead_maxCellEnergy
    process.DeadCellMonitor_HF_neighbor_maxCellEnergy           = dead_maxCellEnergy
    process.DeadCellMonitor_ZDC_neighbor_maxCellEnergy          = dead_maxCellEnergy
    
    dead_minNeighborEnergy = deepcopy(process.DeadCellMonitor_neighbor_minNeighborEnergy)
    process.DeadCellMonitor_HB_neighbor_minNeighborEnergy           = dead_minNeighborEnergy
    process.DeadCellMonitor_HE_neighbor_minNeighborEnergy           = dead_minNeighborEnergy
    process.DeadCellMonitor_HO_neighbor_minNeighborEnergy           = dead_minNeighborEnergy
    process.DeadCellMonitor_HF_neighbor_minNeighborEnergy           = dead_minNeighborEnergy
    process.DeadCellMonitor_ZDC_neighbor_minNeighborEnergy          = dead_minNeighborEnergy

    dead_minGoodNeighborFrac = deepcopy(process.DeadCellMonitor_neighbor_minGoodNeighborFrac)
    process.DeadCellMonitor_HB_neighbor_minGoodNeighborFrac           = dead_minGoodNeighborFrac
    process.DeadCellMonitor_HE_neighbor_minGoodNeighborFrac           = dead_minGoodNeighborFrac
    process.DeadCellMonitor_HO_neighbor_minGoodNeighborFrac           = dead_minGoodNeighborFrac
    process.DeadCellMonitor_HF_neighbor_minGoodNeighborFrac           = dead_minGoodNeighborFrac
    process.DeadCellMonitor_ZDC_neighbor_minGoodNeighborFrac          = dead_minGoodNeighborFrac

    dead_maxEnergyFrac = deepcopy(process.DeadCellMonitor_neighbor_maxEnergyFrac)
    process.DeadCellMonitor_HB_neighbor_maxEnergyFrac           = dead_maxEnergyFrac
    process.DeadCellMonitor_HE_neighbor_maxEnergyFrac           = dead_maxEnergyFrac
    process.DeadCellMonitor_HO_neighbor_maxEnergyFrac           = dead_maxEnergyFrac
    process.DeadCellMonitor_HF_neighbor_maxEnergyFrac           = dead_maxEnergyFrac
    process.DeadCellMonitor_ZDC_neighbor_maxEnergyFrac          = dead_maxEnergyFrac

    dead_energyThreshold = deepcopy(process.DeadCellMonitor_energyThreshold)
    process.DeadCellMonitor_HB_energyThreshold           = dead_energyThreshold
    process.DeadCellMonitor_HE_energyThreshold           = dead_energyThreshold
    process.DeadCellMonitor_HO_energyThreshold           = dead_energyThreshold
    process.DeadCellMonitor_HF_energyThreshold           = dead_energyThreshold
    process.DeadCellMonitor_ZDC_energyThreshold          = dead_energyThreshold

    # Hot Cell Monitor
    hot_nsigma = deepcopy(process.HotCellMonitor_pedestal_Nsigma)
    process.HotCellMonitor_pedestal_HB_Nsigma           = hot_nsigma
    process.HotCellMonitor_pedestal_HE_Nsigma           = hot_nsigma
    process.HotCellMonitor_pedestal_HO_Nsigma           = hot_nsigma
    process.HotCellMonitor_pedestal_HF_Nsigma           = hot_nsigma
    process.HotCellMonitor_pedestal_ZDC_Nsigma          = hot_nsigmax

    hot_deltaIeta = deepcopy(process.HotCellMonitor_neighbor_deltaIeta)
    process.HotCellMonitor_HB_neighbor_deltaIeta           = hot_deltaIeta
    process.HotCellMonitor_HE_neighbor_deltaIeta           = hot_deltaIeta
    process.HotCellMonitor_HO_neighbor_deltaIeta           = hot_deltaIeta
    process.HotCellMonitor_HF_neighbor_deltaIeta           = hot_deltaIeta
    process.HotCellMonitor_ZDC_neighbor_deltaIeta          = hot_deltaIeta
    
    hot_deltaIphi = deepcopy(process.HotCellMonitor_neighbor_deltaIphi)
    process.HotCellMonitor_HB_neighbor_deltaIphi           = hot_deltaIphi
    process.HotCellMonitor_HE_neighbor_deltaIphi           = hot_deltaIphi
    process.HotCellMonitor_HO_neighbor_deltaIphi           = hot_deltaIphi
    process.HotCellMonitor_HF_neighbor_deltaIphi           = hot_deltaIphi
    process.HotCellMonitor_ZDC_neighbor_deltaIphi          = hot_deltaIphi

    hot_deltaDepth = deepcopy(process.HotCellMonitor_neighbor_deltaDepth)
    process.HotCellMonitor_HB_neighbor_deltaDepth           = hot_deltaDepth
    process.HotCellMonitor_HE_neighbor_deltaDepth           = hot_deltaDepth
    process.HotCellMonitor_HO_neighbor_deltaDepth           = hot_deltaDepth
    process.HotCellMonitor_HF_neighbor_deltaDepth           = hot_deltaDepth
    process.HotCellMonitor_ZDC_neighbor_deltaDepth          = hot_deltaDepth

    hot_minCellEnergy = deepcopy(process.HotCellMonitor_neighbor_minCellEnergy)
    process.HotCellMonitor_HB_neighbor_minCellEnergy           = hot_minCellEnergy
    process.HotCellMonitor_HE_neighbor_minCellEnergy           = hot_minCellEnergy
    process.HotCellMonitor_HO_neighbor_minCellEnergy           = hot_minCellEnergy
    process.HotCellMonitor_HF_neighbor_minCellEnergy           = hot_minCellEnergy
    process.HotCellMonitor_ZDC_neighbor_minCellEnergy          = hot_minCellEnergy
    
    hot_minNeighborEnergy = deepcopy(process.HotCellMonitor_neighbor_minNeighborEnergy)
    process.HotCellMonitor_HB_neighbor_minNeighborEnergy           = hot_minNeighborEnergy
    process.HotCellMonitor_HE_neighbor_minNeighborEnergy           = hot_minNeighborEnergy
    process.HotCellMonitor_HO_neighbor_minNeighborEnergy           = hot_minNeighborEnergy
    process.HotCellMonitor_HF_neighbor_minNeighborEnergy           = hot_minNeighborEnergy
    process.HotCellMonitor_ZDC_neighbor_minNeighborEnergy          = hot_minNeighborEnergy

    hot_maxEnergy = deepcopy(process.HotCellMonitor_neighbor_maxEnergy)
    process.HotCellMonitor_HB_neighbor_maxEnergy           = hot_maxEnergy
    process.HotCellMonitor_HE_neighbor_maxEnergy           = hot_maxEnergy
    process.HotCellMonitor_HO_neighbor_maxEnergy           = hot_maxEnergy
    process.HotCellMonitor_HF_neighbor_maxEnergy           = hot_maxEnergy
    process.HotCellMonitor_ZDC_neighbor_maxEnergy          = hot_maxEnergy

    hot_HotEnergyFrac = deepcopy(process.HotCellMonitor_neighbor_HotEnergyFrac)
    process.HotCellMonitor_HB_neighbor_HotEnergyFrac           = hot_HotEnergyFrac
    process.HotCellMonitor_HE_neighbor_HotEnergyFrac           = hot_HotEnergyFrac
    process.HotCellMonitor_HO_neighbor_HotEnergyFrac           = hot_HotEnergyFrac
    process.HotCellMonitor_HF_neighbor_HotEnergyFrac           = hot_HotEnergyFrac
    process.HotCellMonitor_ZDC_neighbor_HotEnergyFrac          = hot_HotEnergyFrac

    hot_energyThreshold = deepcopy(process.HotCellMonitor_energyThreshold)
    process.HotCellMonitor_HB_energyThreshold           = hot_energyThreshold
    process.HotCellMonitor_HE_energyThreshold           = hot_energyThreshold
    process.HotCellMonitor_HO_energyThreshold           = hot_energyThreshold
    process.HotCellMonitor_HF_energyThreshold           = hot_energyThreshold
    process.HotCellMonitor_ZDC_energyThreshold          = hot_energyThreshold

    hot_persistentThreshold = deepcopy(process.HotCellMonitor_persistentThreshold)
    process.HotCellMonitor_HB_persistentThreshold           = hot_persistentThreshold
    process.HotCellMonitor_HE_persistentThreshold           = hot_persistentThreshold
    process.HotCellMonitor_HO_persistentThreshold           = hot_persistentThreshold
    process.HotCellMonitor_HF_persistentThreshold           = hot_persistentThreshold
    process.HotCellMonitor_ZDC_persistentThreshold          = hot_persistentThreshold

    # Rec Hit Monitor
    rechit_energyThreshold = deepcopy(process.RecHitMonitor_energyThreshold)
    process.DeadCellMonitor_HB_energyThreshold           = rechit_energyThreshold
    process.DeadCellMonitor_HE_energyThreshold           = rechit_energyThreshold
    process.DeadCellMonitor_HO_energyThreshold           = rechit_energyThreshold
    process.DeadCellMonitor_HF_energyThreshold           = rechit_energyThreshold
    process.DeadCellMonitor_ZDC_energyThreshold          = rechit_energyThreshold
    return 
