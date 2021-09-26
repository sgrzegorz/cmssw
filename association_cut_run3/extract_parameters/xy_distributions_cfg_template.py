import FWCore.ParameterSet.Config as cms

# load common code
import direct_simu_reco_cff as profile
process = cms.Process('PPSXYDistributions', profile.era)
profile.LoadConfig(process)
import CalibPPS.ESProducers.ppsAssociationCuts_non_DB_cff as ac

profile.config.UseConstantXangleBetaStar(process, $xangle, 0.3)

# minimal logger settings
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('detailedInfo'),
  detailedInfo   = cms.untracked.PSet(
    threshold  = cms.untracked.string('INFO') 
  )
)

# minimal logger settings
# process.MessageLogger = cms.Service("MessageLogger",
#   statistics = cms.untracked.vstring(),
#   destinations = cms.untracked.vstring('cout'),
#   cout = cms.untracked.PSet(
#     threshold = cms.untracked.string('DEBUG')
#   )
# )


# number of events
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(int($n_events))
)

# xangle and beta* plotter
process.ctppsLHCInfoPlotter = cms.EDAnalyzer("CTPPSLHCInfoPlotter",
  lhcInfoLabel = cms.string(""),
  outputFile = cms.string("output_lhcInfo.root"),
)

# optics plotter
process.ctppsOpticsPlotter = cms.EDAnalyzer("CTPPSOpticsPlotter",
  opticsLabel = cms.string(""),

  rpId_45_F = cms.uint32(23),
  rpId_45_N = cms.uint32(3),
  rpId_56_N = cms.uint32(103),
  rpId_56_F = cms.uint32(123),

  outputFile = cms.string("output_optics.root")
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
  
  * process.ctppsLHCInfoPlotter
  * process.ctppsOpticsPlotter
  * process.ctppsTrackDistributionPlotter
)
