#############################################################
########## General settings
#############################################################
# flag to be Tested

flags = {
    'passing_mvaFall17Iso_WP90'    : '(passingCutBasedMedium94X   == 1) && (passingMVA94Xwp90iso == 1 ) &&\
    (   (el_sc_abseta <= 1.479)*(el_dxy < 0.05 && el_dz <0.1) + (el_sc_abseta > 1.479)*(el_dxy < 0.1 && el_dz <0.2 && el_sieie < 0.03 && el_IoEmIop < 0.014 ))',
    }##FIXME :: add conveto

baseOutDir = 'results/Data2017/tnpEleID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'
samplesDef={
    'data'   : tnpSamples.dict2017['data_Run2017B'].clone(),
    'mcNom'  : tnpSamples.dict2017['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.dict2017['DY_amcatnlo'].clone(),
    'tagSel' : tnpSamples.dict2017['DY_madgraph'].clone(),
    'tagSel2' : tnpSamples.dict2017['DY_madgraph'].clone(),
}

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 35') #
if not samplesDef['tagSel2'] is None:
    samplesDef['tagSel2'].rename('mcAltSel2_DY_madgraph')
    samplesDef['tagSel2'].set_cut('tag_Ele_pt > 45') #

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]},
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.] },


]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 40 && abs(tag_sc_eta) < 2.17 '

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
##---FIXME add impact parameter cut for each region
additionalCuts = { }
#etabins = biningDef[0]['bins']
#netabins = len(etabins-1)
#ptbins  = biningDef[1]['bins']
#nptbins = len(ptinbs-1)
#for ieta in range(0,netabins):
#    for ipt in range(0, nptbins):
#        i= nptbins*ipt + ieta
        
#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
