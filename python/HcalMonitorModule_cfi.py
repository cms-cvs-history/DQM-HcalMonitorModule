import FWCore.ParameterSet.Config as cms

hcalMonitor=cms.EDAnalyzer("HcalMonitorModule",
                           debug=cms.int32(0),
                           online=cms.bool(False),
                           #AllowedCalibTypes=cms.vint32(),
                           mergeRuns=cms.bool(False),
                           enableCleanup=cms.bool(False),
                           FEDRawDataCollection=cms.InputTag("source"),
                           UnpackerReport=cms.InputTag("hcalDigis"),
                           subSystemFolder=cms.string("Hcal/"),
                           )
