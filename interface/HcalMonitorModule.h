#ifndef HcalMonitorModule_GUARD_H
#define HcalMonitorModule_GUARD_H

/*
 * \file HcalMonitorModule.h
 *

 * $Date: 2010/02/18 20:36:30 $
 * $Revision: 1.00 $
 * \author J. Temple
 *
*/

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"

#include "EventFilter/HcalRawToDigi/interface/HcalDCCHeader.h"
#include "EventFilter/HcalRawToDigi/interface/HcalHTRData.h"

#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"

#include "CondFormats/HcalObjects/interface/HcalCondObjectContainer.h"

#include "DataFormats/Provenance/interface/EventID.h"  
#include "DataFormats/HcalDigi/interface/HcalUnpackerReport.h"
#include "DataFormats/FEDRawData/interface/FEDRawDataCollection.h"
#include "DataFormats/HcalDigi/interface/HcalCalibrationEventTypes.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"
#include "DataFormats/FEDRawData/interface/FEDNumbering.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"

#include "EventFilter/HcalRawToDigi/interface/HcalDCCHeader.h"
#include "EventFilter/HcalRawToDigi/interface/HcalHTRData.h"

#include "FWCore/Utilities/interface/CPUTimer.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include <memory>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>


class HcalMonitorModule : public edm::EDAnalyzer
{

public:

  // Constructor
  HcalMonitorModule(const edm::ParameterSet& ps);

  // Destructor
  ~HcalMonitorModule();

 protected:

  // Analyze
  void analyze(const edm::Event& e, const edm::EventSetup& c);

  // BeginJob
  void beginJob();

  // BeginRun
  void beginRun(const edm::Run& run, const edm::EventSetup& c);

  // Begin LumiBlock
  void beginLuminosityBlock(const edm::LuminosityBlock& lumiSeg,
                            const edm::EventSetup& c) ;

  // End LumiBlock
  void endLuminosityBlock(const edm::LuminosityBlock& lumiSeg,
                          const edm::EventSetup& c);

 // EndJob
  void endJob(void);

  // EndRun
  void endRun(const edm::Run& run, const edm::EventSetup& c);

  // Reset
  void reset(void);

  // cleanup
  void cleanup(void);

  // setup
  void setup(void);
  
  // CheckSubdetectorStatus
  void CheckSubdetectorStatus(const edm::Handle<FEDRawDataCollection>& rawraw,
			      HcalSubdetector subdet,
			      const HcalElectronicsMap& emap);

 private:

  int ievt_;
  int runNumber_;
  int evtNumber_;

  MonitorElement* meStatus_;
  MonitorElement* meRun_;
  MonitorElement* meEvt_;
  MonitorElement* meFEDS_;
  MonitorElement* meCalibType_;
  MonitorElement* meCurrentCalibType_;
  MonitorElement* meHB_;
  MonitorElement* meHE_;
  MonitorElement* meHO_;
  MonitorElement* meHF_;
  MonitorElement* meIevt_;
  MonitorElement* meProcessedEndLumi_;
  MonitorElement* meOnline_;

  bool fedsListed_;

  bool Online_;
  bool mergeRuns_;
  bool enableCleanup_;
  int debug_;
  bool init_;
  edm::InputTag FEDRawDataCollection_;
  edm::InputTag inputLabelReport_;
  std::string prefixME_;

  int HBpresent_, HEpresent_, HOpresent_, HFpresent_;
  DQMStore* dbe_;

  const HcalElectronicsMap*    eMap_;

}; //class HcalMonitorModule : public edm::EDAnalyzer

#endif
