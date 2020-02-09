from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18_OOTid = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_04012019-OOTID/2017Data_FullJson/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eos2017UL = '/eos/cms/store/group/phys_egamma/swmukher/UL/ntuple_2017_UltraLegacy/'

Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosMoriond18_OOTid + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18_OOTid + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Moriond18' : tnpSample('DY_amcatnlo_Moriond18', 
                                       eosMoriond18_OOTid + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 13.96 ),

    }

UL2017 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eos2017UL + 'mc.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_2017UL' : tnpSample('DY_madgraph_2017UL', 
                                        eos2017UL + 'mc.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_2017UL' : tnpSample('DY_amcatnlo_2017UL', 
                                       eos2017UL + 'mc.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017C' : tnpSample('data_Run2017C' , eos2017UL + 'data_C_try4.root' , lumi = 9.9 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eos2017UL + 'data_F_try4.root' , lumi = 13.96 ),

    }


Moriond18_94X_OOTid = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18_OOTid + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18_OOTid + 'data/17Nov2017_RunB.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18_OOTid + 'data/17Nov2017_RunC.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18_OOTid + 'data/17Nov2017_RunD.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18_OOTid + 'data/17Nov2017_RunE.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18_OOTid + 'data/17Nov2017_RunF.root' , lumi = 13.96 ),

    }
