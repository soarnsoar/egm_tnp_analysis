#############################################################
########## General settings
#############################################################
# flag to be Tested

flags = {
    'passHLT27_HWWID':'passHltEle27WPTightGsf'
    }##FIXME :: add conveto

baseOutDir = 'results/Data2016/tnpEleTrig/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleTrig'
samplesDef={

    'data_Run2016B'   : tnpSamples.dict2016['data_Run2016B'].clone(),
    'data_Run2016C'   : tnpSamples.dict2016['data_Run2016C'].clone(),
    'data_Run2016D'   : tnpSamples.dict2016['data_Run2016D'].clone(),
    'data_Run2016D'   : tnpSamples.dict2016['data_Run2016D'].clone(),
    'data_Run2016E'   : tnpSamples.dict2016['data_Run2016E'].clone(),
    'data_Run2016F'   : tnpSamples.dict2016['data_Run2016F'].clone(),
    'data_Run2016G'   : tnpSamples.dict2016['data_Run2016G'].clone(),
    'data_Run2016H'   : tnpSamples.dict2016['data_Run2016H'].clone(),
    
    'mcNom'  : tnpSamples.dict2016['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.dict2016['DY_amcatnlo'].clone(),

    

    ##--tagsel for sys.

    'data_Run2016B_tagSeldown' : tnpSamples.dict2016['data_Run2016B'].clone(),
    'data_Run2016C_tagSeldown' : tnpSamples.dict2016['data_Run2016C'].clone(),
    'data_Run2016D_tagSeldown' : tnpSamples.dict2016['data_Run2016D'].clone(),
    'data_Run2016E_tagSeldown' : tnpSamples.dict2016['data_Run2016E'].clone(),
    'data_Run2016F_tagSeldown' : tnpSamples.dict2016['data_Run2016F'].clone(),
    'data_Run2016G_tagSeldown' : tnpSamples.dict2016['data_Run2016G'].clone(),
    'data_Run2016H_tagSeldown' : tnpSamples.dict2016['data_Run2016H'].clone(),


    'data_Run2016B_tagSelup' : tnpSamples.dict2016['data_Run2016B'].clone(),
    'data_Run2016C_tagSelup' : tnpSamples.dict2016['data_Run2016C'].clone(),
    'data_Run2016D_tagSelup' : tnpSamples.dict2016['data_Run2016D'].clone(),
    'data_Run2016E_tagSelup' : tnpSamples.dict2016['data_Run2016E'].clone(),    
    'data_Run2016F_tagSelup' : tnpSamples.dict2016['data_Run2016F'].clone(),
    'data_Run2016G_tagSelup' : tnpSamples.dict2016['data_Run2016G'].clone(),
    'data_Run2016H_tagSelup' : tnpSamples.dict2016['data_Run2016H'].clone(),

    ##--mllvar

    'data_Run2016B_mllvar' : tnpSamples.dict2016['data_Run2016B'].clone(),
    'data_Run2016C_mllvar' : tnpSamples.dict2016['data_Run2016C'].clone(),
    'data_Run2016D_mllvar' : tnpSamples.dict2016['data_Run2016D'].clone(),
    'data_Run2016E_mllvar' : tnpSamples.dict2016['data_Run2016E'].clone(),
    'data_Run2016F_mllvar' : tnpSamples.dict2016['data_Run2016F'].clone(),
    'data_Run2016G_mllvar' : tnpSamples.dict2016['data_Run2016G'].clone(),
    'data_Run2016H_mllvar' : tnpSamples.dict2016['data_Run2016H'].clone(),

    
    
    
}

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()



for s in ['data_Run2016B_tagSeldown','data_Run2016C_tagSeldown','data_Run2016D_tagSeldown','data_Run2016E_tagSeldown','data_Run2016F_tagSeldown','data_Run2016G_tagSeldown','data_Run2016H_tagSeldown']:
    #continue
    cutBase   = '(\
    (tag_Ele_pt > 30) && (abs(tag_sc_eta) < 2.5) &&(el_lost_hits < 1) && (passingHLTsafe   == 1) && (passingMVA80Xwp90 == 1 ) &&\
    (   ((el_sc_abseta <= 1.479) && (fabs(el_dxy) < 0.05) && (fabs(el_dz) <0.1) && (el_relIso_fall17 <0.05880 )) || (  (el_sc_abseta > 1.479) && (fabs(el_dxy) < 0.1) && (fabs(el_dz) < 0.2) && ( el_relIso_fall17 < 0.0571) ))\
    )'

    samplesDef[s].rename(s)
    samplesDef[s].set_cut(cutBase) #
for s in ['data_Run2016B_tagSelup','data_Run2016C_tagSelup','data_Run2016D_tagSelup','data_Run2016E_tagSelup','data_Run2016F_tagSelup','data_Run2016G_tagSelup','data_Run2016H_tagSelup']:
    #continue
    cutBase   = '(\
    (tag_Ele_pt > 40) && (abs(tag_sc_eta) < 2.5) &&(el_lost_hits < 1) && (passingHLTsafe   == 1) && (passingMVA80Xwp90 == 1 ) &&\
    (   ((el_sc_abseta <= 1.479) && (fabs(el_dxy) < 0.05) && (fabs(el_dz) <0.1) && (el_relIso_fall17 <0.05880 )) || (  (el_sc_abseta > 1.479) && (fabs(el_dxy) < 0.1) && (fabs(el_dz) < 0.2) && ( el_relIso_fall17 < 0.0571) ))\
    )'

    samplesDef[s].rename(s)
    samplesDef[s].set_cut(cutBase) #

for s in ['data_Run2016B_mllvar','data_Run2016C_mllvar','data_Run2016D_mllvar','data_Run2016E_mllvar','data_Run2016F_mllvar','data_Run2016G_mllvar','data_Run2016H_mllvar']:
    #continue
    cutBase   = '(\
    (tag_Ele_pt > 35) && (abs(tag_sc_eta) < 2.5) &&(el_lost_hits < 1) && (passingHLTsafe   == 1) && (passingMVA80Xwp90 == 1 ) &&\
    (   ((el_sc_abseta <= 1.479) && (fabs(el_dxy) < 0.05) && (fabs(el_dz) <0.1) && (el_relIso_fall17 <0.05880 )) || (  (el_sc_abseta > 1.479) && (fabs(el_dxy) < 0.1) && (fabs(el_dz) < 0.2) && ( el_relIso_fall17 < 0.0571) )) && (pair_mass > 70. && pair_mass <110.)\
    )'

    samplesDef[s].rename(s)
    samplesDef[s].set_cut(cutBase)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.17, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.17, 2.500]},
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [0., 25., 26.,27.,29.,31.,34., 37.,40.,50.,100.,200]},
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = '(\
(tag_Ele_pt > 35) && (abs(tag_sc_eta) < 2.5) &&(el_lost_hits < 1) && (passingHLTsafe   == 1) && (passingMVA80Xwp90 == 1 ) &&\
(   ((el_sc_abseta <= 1.479) && (fabs(el_dxy) < 0.05) && (fabs(el_dz) <0.1) && (el_relIso_fall17 <0.05880 )) || (  (el_sc_abseta > 1.479) && (fabs(el_dxy) < 0.1) && (fabs(el_dz) < 0.2) && ( el_relIso_fall17 < 0.0571) ))\
)'


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
'''
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
        
'''
