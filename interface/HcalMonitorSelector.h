#ifndef HcalMonitorSelector_H
#define HcalMonitorSelector_H

/*
 * \file HcalMonitorSelector.h
 *
 * $Date: 2005/11/17 22:55:26 $
 * $Revision: 1.3 $
 * \author W. Fisher
 *
*/
#include <FWCore/Framework/interface/Event.h>
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TBDataFormats/HcalTBObjects/interface/HcalTBTriggerData.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const int DO_HCAL_DIGIMON         = 0x0001;
static const int DO_HCAL_DFMON           = 0x0002;
static const int DO_HCAL_RECHITMON       = 0x0004;
static const int DO_HCAL_LED_CALIBMON    = 0x0008;
static const int DO_HCAL_LASER_CALIBMON  = 0x0010;
static const int DO_HCAL_PED_CALIBMON    = 0x0020;


class HcalMonitorSelector{

public:

/// Constructor
HcalMonitorSelector() {};
HcalMonitorSelector(const edm::ParameterSet& ps);

/// Destructor
~HcalMonitorSelector();

  inline unsigned int getEventMask() const { return m_eventMask; }
  void processEvent(const edm::Event& e);

protected:

private:

  unsigned int m_eventMask;

};

#endif
