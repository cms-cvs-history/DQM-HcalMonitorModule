import FWCore.ParameterSet.Config as cms
from DQM.HcalMonitorModule.HcalMonitorModule_cfi import * # there's probably a better way to do this, once I discover the difference between import and load
from DQM.HcalMonitorClient.HcalMonitorClient_cfi import * # ditto

process = cms.Process("HCALDQM")
#----------------------------
# Event Source
#-----------------------------

#####################  SET THE NUMBER OF EVENTS OVER WHICH TO RUN HERE #################################

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
    )

##################### SET YOUR FILE TO CHECK HERE #####################################################

### Case 1:  PoolSource (from DBS, etc.)

process.source = cms.Source("PoolSource",
                            
                            fileNames = cms.untracked.vstring
                            (
    # Test -- claim that there is noise in HB around phi=70?
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/08E115E1-D1A5-DD11-BCE7-000423D99AA2.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/184F395C-CEA5-DD11-A2E2-000423D60FF6.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/18D42E5A-DDA5-DD11-B0AB-001617C3B778.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/1E6AA65A-CEA5-DD11-89F4-001617C3B6FE.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/2AB5D440-D1A5-DD11-918D-001617E30CD4.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/2CDF3B0F-CFA5-DD11-AE18-000423D99A8E.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/38419E41-D1A5-DD11-8B68-001617C3B6E2.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/708C5612-CFA5-DD11-AD52-0019DB29C5FC.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/84204A5E-CEA5-DD11-8821-000423D99614.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/9E77EF30-D1A5-DD11-83AF-000423D94C68.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/A44C0AE0-D1A5-DD11-BEC7-001617C3B65A.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/A455EEC2-CFA5-DD11-A5FD-000423D94534.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/A88C89CE-CFA5-DD11-A3FD-000423D952C0.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/B01DD909-CFA5-DD11-876F-001617E30F4C.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/CA59E7A6-D2A5-DD11-B2E5-001617DF785A.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/CA89A8C7-CFA5-DD11-ADFE-000423D985B0.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/E01CA6C6-CFA5-DD11-87CE-000423D60FF6.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/068/000/E4E9FEF9-D1A5-DD11-A6AE-001617C3B6C6.root',

    

    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/484/C2869114-23AF-DD11-851F-000423D98FBC.root',
     
    # Andreas' test of reportsummary
    #'/store/data/Commissioning08/Cosmics/RAW/CRUZET4_v1/000/058/555/02E4041E-1571-DD11-98CE-001D09F241B9.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/195/00766F08-1BAE-DD11-8CE5-001617DBD5B2.root',

    # run with HO out
    '/store/data/Commissioning08/Cosmics/RAW/v1/000/069/987/32803ED3-54AD-DD11-BA3D-000423D94E1C.root',

    # recent cosmics run with known hot cell in HF
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/067/838/006945C8-40A5-DD11-BD7E-001617DBD556.root',

    # NON-ZERO-SUPPRESSED RUN
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/064/103/2A983512-E18F-DD11-BE84-001617E30CA4.root'
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/904/02944F1F-EB9E-DD11-8D88-001D09F2A465.root',

    # ZERO-SUPPRESSED RUN
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/064/042/0A36AA7D-978F-DD11-BA36-000423D6C8E6.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/064/042/5A2D217E-978F-DD11-9CB7-000423D6B444.root',
    #'/store/data/Commissioning08/Cosmics/RAW/v1/000/064/042/68175229-A08F-DD11-A352-000423D992DC.root',
    
    )
                            )


###  Case 2:  Run on raw .dat files

###process.source = cms.Source("NewEventStreamFileReader",
###                            fileNames = cms.untracked.vstring('/store/data/GlobalCruzet3MW33/A/000/056/416/GlobalCruzet3MW33.00056416.0001.A.storageManager.0.0000.dat')
###                            )



###  Case 3:  Run on HCAL local runs (pedestal, LED, etc.).  You need to have access to /bigspool or have a local copy of the file available.  This syntax has now been tested, and is found to work in python.

###process.source = cms.Source("HcalTBSource",
###                            fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/s/stjohn/scratch0/USC_044790.root'),
###                            streams   = cms.untracked.vstring(#HBHEa,b,c:
###                                                              'HCAL_DCC700','HCAL_DCC701','HCAL_DCC702','HCAL_DCC703','HCAL_DCC704','HCAL_DCC705',
###                                                              'HCAL_DCC706','HCAL_DCC707','HCAL_DCC708','HCAL_DCC709','HCAL_DCC710','HCAL_DCC711',
###                                                              'HCAL_DCC712','HCAL_DCC713','HCAL_DCC714','HCAL_DCC715','HCAL_DCC716','HCAL_DCC717',
###                                                              #HF:
###                                                              'HCAL_DCC718','HCAL_DCC719','HCAL_DCC720','HCAL_DCC721','HCAL_DCC722','HCAL_DCC723',
###                                                              #HO:
###                                                              'HCAL_DCC724','HCAL_DCC725','HCAL_DCC726','HCAL_DCC727','HCAL_DCC728','HCAL_DCC729',
###                                                              'HCAL_DCC730','HCAL_DCC731',
###                                                              'HCAL_Trigger','HCAL_SlowData'
###                                                              )
###                            )



#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.DQM.collectorHost = 'cmsru2'
process.DQM.collectorPort = 9190
process.dqmSaver.convention = 'Online'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'Hcal'
# optionally change fileSaving  conditions
# replace dqmSaver.prescaleLS =   -1
# replace dqmSaver.prescaleTime = -1 # in minutes
#process.dqmSaver.prescaleEvt =  2

# For Hcal local run files, replace dqmSaver.saveByRun = 2 
process.dqmSaver.saveByRun = 1


#-----------------------------
# Hcal Conditions: from Global Conditions Tag 
#-----------------------------
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = 'frontier://Frontier/CMS_COND_21X_GLOBALTAG'
process.GlobalTag.globaltag = 'CRAFT_V3P::All'  # update GlobalTag as neceesary
process.prefer("GlobalTag")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery=100

#-----------------------------
# Hcal DQM Source, including SimpleReconstructor
#-----------------------------
process.load("DQM.HcalMonitorModule.HcalMonitorModule_cfi")
process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalSimpleReconstructor_hbhe_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalSimpleReconstructor_ho_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalSimpleReconstructor_hf_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalSimpleReconstructor_zdc_cfi")

# hcalMonitor configurable values -----------------------
process.hcalMonitor.debug = 0
#process.hcalMonitor.DigiOccThresh = -999999999 ##Temporary measure while DigiOcc is reworked.
process.hcalMonitor.pedestalsInFC = True
process.hcalMonitor.showTiming = False
process.hcalMonitor.checkNevents=500
process.hcalMonitor.dump2database = False

# Turn on/off individual hcalMonitor modules ------------
process.hcalMonitor.DataFormatMonitor   = True
process.hcalMonitor.DataIntegrityTask   = False
process.hcalMonitor.DigiMonitor         = True
process.hcalMonitor.RecHitMonitor       = True
process.hcalMonitor.TrigPrimMonitor     = False
process.hcalMonitor.DeadCellMonitor     = True
process.hcalMonitor.HotCellMonitor      = True
process.hcalMonitor.BeamMonitor         = False
process.hcalMonitor.PedestalMonitor     = True
process.hcalMonitor.LEDMonitor          = False
process.hcalMonitor.CaloTowerMonitor    = False
process.hcalMonitor.MTCCMonitor         = False
process.hcalMonitor.HcalAnalysis        = False
process.hcalMonitor.EEUSMonitor         = False

# This takes the default cfg values from the hcalMonitor base class and applies them to the subtasks.
setHcalTaskValues(process.hcalMonitor)

# Set individual Task values here (otherwise they will remain set to the values specified for the hcalMonitor.)
process.hcalMonitor.DeadCellMonitor_pedestal_Nsigma     = 0
process.hcalMonitor.DeadCellMonitor_makeDiagnosticPlots = False
process.hcalMonitor.DeadCellMonitor_test_pedestal       = True
process.hcalMonitor.DeadCellMonitor_test_occupancy      = True
process.hcalMonitor.DeadCellMonitor_test_neighbor       = False

process.hcalMonitor.HotCellMonitor_makeDiagnosticPlots  = False
process.hcalMonitor.HotCellMonitor_test_neighbor        = False
process.hcalMonitor.HotCellMonitor_test_pedestal        = True

process.hcalMonitor.RecHitMonitor_makeDiagnosticPlots   = True
process.hcalMonitor.BeamMonitor_makeDiagnosticPlots     = True

process.hcalMonitor.PedestalMonitor_makeDiagnosticPlots = True
process.hcalMonitor.PedestalMonitor_minEntriesPerPed    = 10
#-----------------------------
# Hcal DQM Client
#-----------------------------
process.load("DQM.HcalMonitorClient.HcalMonitorClient_cfi")

# hcalClient configurable values ------------------------
# suppresses html output from HCalClient  
process.hcalClient.baseHtmlDir = '/tmp/temple'  # set to '' to ignore html output

# Set client settings to the same as monitor.  At the moment, this doesn't affect client minErrorFlag
# Summary Client is also unaffected
setHcalClientValuesFromMonitor(process.hcalClient,process.hcalMonitor, debug=False)  # turn debug to True to dump out client settings

#process.hcalClient.debug =process.hcalMonitor.debug
process.hcalClient.debug = 0
process.hcalClient.SummaryClient        = True
#process.hcalClient.DigiClient = False
#process.hcalClient.TrigPrimClient = False

#-----------------------------
# Scheduling
#-----------------------------
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound', 
        'TooManyProducts', 
        'TooFewProducts')
)

process.p = cms.Path(process.hcalDigis*process.horeco*process.hfreco*process.hbhereco*process.zdcreco*process.hcalMonitor*process.hcalClient*process.dqmEnv*process.dqmSaver)


#-----------------------------
# Quality Tester 
# will add switch to select histograms to be saved soon
#-----------------------------
process.qTester = cms.EDFilter("QualityTester",
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/HcalMonitorClient/data/hcal_qualitytest_config.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

