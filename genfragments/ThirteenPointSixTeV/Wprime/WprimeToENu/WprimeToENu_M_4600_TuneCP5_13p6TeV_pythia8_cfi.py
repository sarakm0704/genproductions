import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        filterEfficiency = cms.untracked.double(1),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        comEnergy = cms.double(13600.0),

        PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CP5SettingsBlock,
            processParameters = cms.vstring(
                        'NewGaugeBoson:ffbar2Wprime = on',
                        '34:m0 = 4600',
                        '34:onMode = off',
                        '34:onIfAny = 11,12',
                        ),
            parameterSets = cms.vstring(
                        'pythia8CommonSettings',
                        'pythia8CP5Settings',
                        'processParameters'
                        )
            )
)
ProductionFilterSequence = cms.Sequence(generator)
