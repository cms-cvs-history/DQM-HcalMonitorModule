import FWCore.ParameterSet.Config as cms

from DQM.HcalMonitorClient.HcalMonitorClient_cfi import *
hcalOfflineDQMClient = cms.Sequence(hcalClient)

hcalClient.baseHtmlDir       = ''
hcalClient.databaseDir       = ''
hcalClient.minevents         = 500  # Don't count errors when less than 500 events processed
hcalClient.enabledClients    = ["DeadCellMonitor",
                                "HotCellMonitor",
                                "RecHitMonitor",
                                "DigiMonitor",
                                "RawDataMonitor",
                                #"TrigPrimMonitor", # can't enable trig prim monitor, because no trig sim available offline!
                                "NZSMonitor",
                                "BeamMonitor",
                                "DetDiagNoiseMonitor",
                                "Summary"
                                ]
