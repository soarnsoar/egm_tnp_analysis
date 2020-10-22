from libPython.tnpClassUtils import tnpSample

### qll stat
eos2016 = '/eos/cms/store/group/phys_egamma/tnpTuples/tomc/2020-06-09/2016/merged/'
#DY_LO.root  DY_NLO.root  Run2016B.root  Run2016C.root  Run2016D.root  Run2016E.root  Run2016F.root  Run2016G.root  Run2016H.root
dict2016 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eos2016 + 'DY_LO.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', 
                                       eos2016 + 'DY_NLO.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , eos2016 + 'Run2016B.root' , lumi = 1 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eos2016 + 'Run2016C.root' , lumi = 1 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eos2016 + 'Run2016D.root' , lumi = 1 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , eos2016 + 'Run2016E.root' , lumi = 1 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eos2016 + 'Run2016F.root' , lumi = 1 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eos2016 + 'Run2016G.root' , lumi = 1 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eos2016 + 'Run2016H.root' , lumi = 1 ),

    }



eos2017 = '/eos/cms/store/group/phys_egamma/tnpTuples/tomc/2020-06-09/2017/merged/'
#DY1_LO.root  DY1_LO_ext.root  DY_LO.root  DY_LO_ext.root  DY_NLO.root  DY_NLO_ext.root
dict2017 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eos2017 + 'DY_LO.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_ext' : tnpSample('DY_madgraph_ext', 
                                       eos2017 + 'DY_LO_ext.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', 
                                       eos2017 + 'DY_NLO.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eos2017 + 'Run2017B.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eos2017 + 'Run2017C.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eos2017 + 'Run2017D.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eos2017 + 'Run2017E.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eos2017 + 'Run2017F.root' , lumi = 13.96 ),

    }




#DY.root  DY_NLO.root  DY_NLO_ext.root  DY_pow.root
eos2018 = '/eos/cms/store/group/phys_egamma/tnpTuples/tomc/2020-06-09/2018/merged/'
dict2018 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eos2018 + 'DY.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_pow' : tnpSample('DY_pow', 
                                       eos2018 + 'DY_pow.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', 
                                       eos2018 + 'DY_NLO.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2018B' : tnpSample('data_Run2018B' , eos2018 + 'Run2018B.root' , lumi = 1. ),
    'data_Run2018C' : tnpSample('data_Run2018C' , eos2018 + 'Run2018C.root' , lumi = 1. ),
    'data_Run2018D' : tnpSample('data_Run2018D' , eos2018 + 'Run2018D.root' , lumi = 1. ),
    'data_Run2018A' : tnpSample('data_Run2018A' , eos2018 + 'Run2018A.root' , lumi = 1. ),

    }

