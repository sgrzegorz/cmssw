from Configuration.Eras.Era_Run3_cff import *
process = cms.Process('Test', Run3)

import Validation.CTPPS.simu_config.year_2021_cff as config
process.load("Validation.CTPPS.simu_config.year_2021_cff")
process.ctppsCompositeESSource.periods = [config.profile_2021_default]

process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# number of events
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(int(1E4))
)

process.generator.nParticlesSector45 = 4
process.generator.nParticlesSector56 = 4

# distribution plotter
process.ctppsTrackDistributionPlotter = cms.EDAnalyzer("CTPPSTrackDistributionPlotter",
  tagTracks = cms.InputTag("ctppsLocalTrackLiteProducer"),

  rpId_45_F = process.rpIds.rp_45_F,
  rpId_45_N = process.rpIds.rp_45_N,
  rpId_56_N = process.rpIds.rp_56_N,
  rpId_56_F = process.rpIds.rp_56_F,

  outputFile = cms.string("output_xy_distributions.root")
)

# processing path
process.p = cms.Path(
  process.generator
  * process.beamDivergenceVtxGenerator
  * process.ctppsDirectProtonSimulation

  * process.reco_local
  
  * process.ctppsTrackDistributionPlotter
)
