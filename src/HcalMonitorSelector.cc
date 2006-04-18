#include <DQM/HcalMonitorModule/interface/HcalMonitorSelector.h>

/*
 * \file HcalMonitorSelector.cc
 * 
 * $Date: 2006/04/04 19:26:04 $
 * $Revision: 1.2 $
 * \author W Fisher
 *
*/

HcalMonitorSelector::HcalMonitorSelector(const edm::ParameterSet& ps){

  m_eventMask = 0;
  m_runNum = -1;
}

HcalMonitorSelector::~HcalMonitorSelector(){

}

void HcalMonitorSelector::processEvent(const edm::Event& e){
  m_eventMask = 0;

  edm::Handle<HcalTBTriggerData> triggerD;
  try{
    e.getByType(triggerD);
  }
  catch(...) { m_runNum=-1; return; }
  const HcalTBTriggerData trigger = *triggerD;
  
  m_runNum = trigger.runNumber();

  // check trigger contents
  if (trigger.wasBeamTrigger()) m_eventMask = m_eventMask|HCAL_BEAM_TRIGGER;
  if (trigger.wasOutSpillPedestalTrigger()) m_eventMask = m_eventMask|DO_HCAL_PED_CALIBMON;
  if (trigger.wasInSpillPedestalTrigger()) m_eventMask = m_eventMask|DO_HCAL_PED_CALIBMON;
  if (trigger.wasLEDTrigger()) m_eventMask = m_eventMask|DO_HCAL_LED_CALIBMON;
  if (trigger.wasLaserTrigger()) m_eventMask = m_eventMask|DO_HCAL_LASER_CALIBMON;

  ///Just pass these through for now...
  m_eventMask = m_eventMask|DO_HCAL_DIGIMON;
  m_eventMask = m_eventMask|DO_HCAL_DFMON;
  m_eventMask = m_eventMask|DO_HCAL_RECHITMON;

  return;
}
