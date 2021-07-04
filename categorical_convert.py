# categorical_convert.py
## convert categorical into numbers

import numpy as np

def cat_convert(x):
    X = x.copy()
    kk = list(x.keys())
    
    for j in kk:
        uni = x[j].unique()
        if ("Strongly agree" in uni):
            X[j][X[j] == "Strongly agree"]             = 1
            X[j][X[j] == "Agree"]                      = 2
            X[j][X[j] == "Neither agree nor disagree"] = 3
            X[j][X[j] == "Disagree"]                   = 4
            X[j][X[j] == "Strongly disagree"]          = 5
            X[j][X[j] == "Do not know"]                = 6
            X[j][X[j] == " "]                          = np.nan
            
        elif ("Tick" in uni):
            X[j][X[j] == "Tick"] = 1
            X[j][X[j] == " "]    = 0
            
            
        elif ("No" in uni):
            X[j][X[j] == "Yes"]                        = 1
            X[j][X[j] == "No"]                         = 2
            X[j][X[j] == "Not Sure"]                   = 3
            X[j][X[j] == "Not sure"]                   = 3
            X[j][X[j] == "Would prefer not to answer"] = 4
            X[j][X[j] == " "]                          = np.nan
            
        elif ("Impartial" in uni):
            X[j][X[j] == "Impartial"]            = 1
            X[j][X[j] == "Committed to service"] = 2
            X[j][X[j] == "Accountable"]          = 3
            X[j][X[j] == "Respectful"]           = 4
            X[j][X[j] == "Ethical"]              = 5
            X[j][X[j] == " "]                    = np.nan
            
        elif ("Positive change" in uni):
            X[j][X[j] == "Very positive change"] = 1
            X[j][X[j] == "Positive change"]      = 2
            X[j][X[j] == "No change"]            = 3
            X[j][X[j] == "Negative change"]      = 4
            X[j][X[j] == "Very negative change"] = 5
            X[j][X[j] == " "]                    = np.nan
            
        elif ("To a large extent" in uni):
            X[j][X[j] == "To a very large extent"] = 1
            X[j][X[j] == "To a large extent"]      = 2
            X[j][X[j] == "Somewhat"]               = 3
            X[j][X[j] == "To a small extent"]      = 4
            X[j][X[j] == "To a very small extent"] = 5
            X[j][X[j] == " "]                      = np.nan
            
        # q 28, q29
        elif ("2" in uni):
            X[j][X[j] == "Don't know"] = 0
            X[j][X[j] == '1']          = 1
            X[j][X[j] == '2']          = 2
            X[j][X[j] == '3']          = 4
            X[j][X[j] == '5']          = 5
            X[j][X[j] == '6']          = 6
            X[j][X[j] == '7']          = 7
            X[j][X[j] == '8']          = 8
            X[j][X[j] == '9']          = 9
            X[j][X[j] == '10']         = 10
            X[j][X[j] == " "]          = np.nan
            
        # AS question only
        elif ("Large (1,001 or more employees)" in uni):
            X[j][X[j] == "Large (1,001 or more employees)"] = 3
            X[j][X[j] == "Medium (251 to 1,000 employees)"] = 2
            X[j][X[j] == "Small (Less than 250 employees)"] = 1
            X[j][X[j] == " "]                               = np.nan
        
        # q1 only
        elif ("Male" in uni):
            X[j][X[j] == "Male"]                                   = 1
            X[j][X[j] == "Female"]                                 = 2
            X[j][X[j] == "X (Indeterminate/Intersex/Unspecified)"] = 3
            X[j][X[j] == "Prefer not to say"]                      = 4
            X[j][X[j] == " "]                                      = np.nan
        
        # q2@ only
        elif ("Under 40 years" in uni):
            X[j][X[j] == "Under 40 years"]    = 1
            X[j][X[j] == "40 to 54 years"]    = 2
            X[j][X[j] == "55 years or older"] = 3
            X[j][X[j] == " "]                 = np.nan
            
        # q5@ only
        elif ("SES" in uni):
            X[j][X[j] == "Trainee/Graduate/APS"] = 1
            X[j][X[j] == "EL"]                   = 2
            X[j][X[j] == "SES"]                  = 3
            X[j][X[j] == " "]                   = np.nan
            
            
        elif ("To a great extent" in uni):
            X[j][X[j] == "Not at all"]             = 1
            X[j][X[j] == "Very little"]            = 2
            X[j][X[j] == "Somewhat"]               = 3
            X[j][X[j] == "To a great extent"]      = 4
            X[j][X[j] == "To a very great extent"] = 5
            X[j][X[j] == " "]                      = np.nan
            
        elif ("Often" in uni):
            X[j][X[j] == "Always"]    = 1
            X[j][X[j] == "Often"]     = 2
            X[j][X[j] == "Sometimes"] = 3
            X[j][X[j] == "Rarely"]    = 4
            X[j][X[j] == "Never"]     = 5
            X[j][X[j] == " "]         = np.nan
            
        # q27 only
        elif ("Increased clarity around priorities" in uni):
            X[j][X[j] == "Increased clarity around my role and responsibilities"] = 1
            X[j][X[j] == "Increased clarity around priorities"]                   = 2
            X[j][X[j] == "Improved technology and a more digital environment"]    = 3
            X[j][X[j] == "Improved internal communication"]                       = 4
            X[j][X[j] == "Fewer layers of decision making"]                       = 5
            X[j][X[j] == "Increased experimentation with new ideas"]              = 6
            X[j][X[j] == "Increased mobility"]                                    = 7
            X[j][X[j] == "Increased flexibility in work practices"]               = 8
            X[j][X[j] == "Increased instances of working as one APS"]             = 9
            X[j][X[j] == "Other"]                                                 = 10
            X[j][X[j] == " "]                                                     = np.nan
            
        # q30 only
        elif ("Reduced" in uni):
            X[j][X[j] == "Significantly improved"] = 1
            X[j][X[j] == "Improved"]               = 2
            X[j][X[j] == "No change"]              = 3
            X[j][X[j] == "Reduced"]                = 4
            X[j][X[j] == "Significantly reduced"]  = 5
            X[j][X[j] == " "]                      = np.nan
            
        # q31 only
        elif ("Slightly above capacity – lots of work to do" in uni):
            X[j][X[j] == "Well above capacity – too much work"]                = 1
            X[j][X[j] == "Slightly above capacity – lots of work to do"]       = 2
            X[j][X[j] == "At capacity – about the right amount of work to do"] = 3
            X[j][X[j] == "Slightly below capacity – available for more work"]  = 4
            X[j][X[j] == "Below capacity – not enough work"]                   = 5
            X[j][X[j] == " "]                                                  = np.nan
            
    return X 
