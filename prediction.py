import main_1
def prediction():
    rfr_best_model = main_1.rfr_best_model

    x =[["LOS_Y", "LOS", "Black", "White", "Asian", "Latino", "MI", "PVD", "CHF", "CVD", "DEMENT", "COPD", "DM Complicated", "DM Simple", "Renal Disease", "All CNS", "Pure CNS", "Stroke", "Seizure", "OldSyncope", "OldOtherNeuro", "OtherBmLsm", "Age.1"],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #Collect Length of Stay at a hospital data
    los_y = input("Did/are you staying at a hospital? (y/n)")
    if los_y == 'y':
        x[0] = 1
        los = input("How long have/were you in the hospital? (integer value)")
        while not los.isdigit():
            los = input("How long have/were you in the hospital? (MUST be an integer value)")
        x[1] = los

    else:
        x[0] = 0
        x[1] = 0

    #Collect ethnicity data
    ethnicity = input("What ethnicity do you identify as? (Black, White, Asian, Latino)")
    ethnicity = ethnicity.lower()
    if ethnicity == "black":
        x[2] = 1
        x[3] = 0
        x[4] = 0
        x[5] = 0
    elif ethnicity == "white":
        x[2] = 0
        x[3] = 1
        x[4] = 0
        x[5] = 0
    elif ethnicity == "asian":
        x[2] = 0
        x[3] = 0
        x[4] = 1
        x[5] = 0
    elif ethnicity == "latino":
        x[2] = 0
        x[3] = 0
        x[4] = 0
        x[5] = 1
    else:
        x[2] = 0
        x[3] = 0
        x[4] = 0
        x[5] = 0

    #Collect Myocardial Infraction Data
    mi = input("Do you have myocardial infraction? (y/n)")
    if mi == 'y':
        x[6] = 1
    else:
        x[6] = 0

    #Collect Peripheral vascular disease data
    pvd = input("Do you have peripheral vascular disease? (y/n)")
    if pvd == 'y':
        x[7] = 1
    else:
        x[7] = 0

    #Collect Congestive heart failure data
    chf = input("Do you have congestive heart failure? (y/n)")
    if chf == 'y':
        x[8] = 1
    else:
        x[8] = 0

    #Collect cardiovascular disease data
    cvd = input("Do you have cardiovascular disease? (y/n)")
    if cvd == 'y':
        x[9] = 1
    else:
        x[9] = 0

    #Collect dementia data
    dement = input("Do you have dementia? (y/n)")
    if dement == 'y':
        x[10] = 1
    else:
        x[10] = 0

    #Collect Chronic obstructive pulmonary disease
    copd = input("Do you have chronic obstructive pulmonary disease? (y/n)")
    if copd == 'y':
        x[11] = 1
    else:
        x[11] = 0

    #collect diabetes mellitus simple/complicated data
    dmc = input("Do you have diabetes mellitus complicated? (y/n)")
    if dmc == 'y':
        x[12] = 1
    else:
        x[12] = 0

    dms = input("Do you have diabetes mellitus simple? (y/n)")
    if dms == 'y':
        x[13] = 1
    else:
        x[13] = 0

    #Collect renal disease data
    rd = input("Do you have renal disease? (y/n)")
    if rd == 'y':
        x[14] = 1
    else:
        x[14] = 0

    #Collect CNS data
    cns_all = input("Do you have CNS? (y/n)")
    if cns_all == 'y':
        x[15] = 1
        cns_pure = input("Do you have CNS pure? (y/n)")
        if cns_pure == 'y':
            x[16] = 1
        else:
            x[16] = 0
    else:
        x[15] = 0
        x[16] = 0

    #Collect stroke data
    stroke = input("Have you ever had a stroke? (y/n)")
    if stroke == 'y':
        x[17] = 1
    else:
        x[17] = 0

    #Collect seizure data
    seizure = input("Have you ever had a seizure? (y/n)")
    if seizure == 'y':
        x[18] = 1
    else:
        x[18] = 0

    #Collect Age data
    age = input("How old are you? (integer)")
    while not age.isdigit():
        age = input("How old are you? (MUST BE an integer)")
    x[22] = age

    if int(age) >= 75:
        syncope = input("Do you have a history of fainting/passing out? (y/n)")
        if syncope == 'y':
            x[19] = 1
        else:
            x[19] = 0

        other_neuro = input("Do you have any other neurological diseases? (y/n)")
        if other_neuro == 'y':
            x[20] = 1
        else:
            x[20] = 0

        other_BmLsn = input("Do you have any other BmLsn?(y/n)")
        if other_BmLsn == 'y':
            x[21] = 1
        else:
            x[21] = 0


    #Make prediction
    predicted_risk_level = rfr_best_model.predict(x)
    if predicted_risk_level > 6:
        print("You are at a high risk of mortality due to COVID-19")
    elif 6 >= predicted_risk_level > 3:
        print("You are at a medium risk of mortality due to COVID-19")
    else:
        print("You are at a low risk of mortality due to COVID-19")

    #Another prediction
    another = input("Would you like to make another prediction? (y/n)")
    if another == 'y':
        prediction()

